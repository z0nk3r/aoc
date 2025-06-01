/** 
 * @file
 *
 * @brief Hashtable Library for O(1) Lookup of data by keyword.
 * Analogous to a Python Dictionnary.
 */

#include <errno.h>
#include <float.h>
#include <pthread.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#include "lib_hashtable.h"

/**
 * @typedef ht_node_t
 * 
 * @brief struct ht_node_t - struct for each item in the hashtable
 * @param     key   (char *)        PTR to the KEY string
 * @param     val   (void *)        PTR to the DATA value
 * @param     next  (ht_node_t *)   PTR to the next node in the array[idx].
 */
typedef struct ht_node_t
{
    char             *key;  /** (char *)        PTR to the KEY string */
    void             *val;  /** (void *)        PTR to the DATA value */
    struct ht_node_t *next; /** (ht_node_t *)   PTR to the next node in the array[idx]. */
} ht_node_t;

struct htable_t
{
    uint32_t        table_sz;   /** (uint32_t)        SIZE of the hashtable */
    int32_t         num_nodes;  /** (int32_t)         SIZE of the number of nodes/data */
    double          l_factor;   /** (double)          DOUBLE used to calculate load factor and resize as needed */
    ht_node_t     **array;      /** (ht_node_t **)    ARRAY of nodes of the hashtable */
    pthread_mutex_t mu_lock;    /** (pthread_mutex_t) MUTEX LOCK to prevent simultaneous asynchronous read/writes */
};

static uint64_t ht_hash(const char *key, uint64_t ht_sz);
static void    *ht_search_priv(htable_t *htable, const char *key);
static int32_t  ht_resize(htable_t *htable);
static int32_t  ht_reinsert(htable_t *htable, const char *key, void *val);

htable_t *
ht_create (int32_t table_sz, double l_factor)
{

    htable_t *htable = NULL;
    if ((0 >= table_sz) || (DBL_EPSILON > l_factor))
    {
        (void)fprintf(stderr, "ht_create init error: bad starter values");
        goto HT_CREATE_RET;
    }

    if (l_factor > MAX_LFACTOR_PCT)
    {
        (void)fprintf(
            stderr,
            "ht_create init error: provided load factor too large. Must be "
            "less than 100");
        goto HT_CREATE_RET;
    }

    htable = calloc(1, sizeof(htable_t));
    if (NULL == htable)
    {
        perror("ht_create initial calloc");
        errno = 0;
        goto HT_CREATE_RET;
    }

    htable->l_factor = l_factor;
    htable->table_sz = table_sz;

    htable->array = calloc(htable->table_sz, sizeof(ht_node_t *));
    if (NULL == htable->array)
    {
        perror("ht_create array calloc");
        errno = 0;
        free(htable);
        htable = NULL;
        goto HT_CREATE_RET;
    }

    if (0 != pthread_mutex_init(&(htable->mu_lock), NULL))
    {
        perror("ht_create mutex init");
        errno = 0;
        free(htable->array);
        free(htable);
        htable = NULL;
    }

HT_CREATE_RET:
    return htable;
}

int32_t
ht_insert (htable_t *htable, const char *key, void *val)
{
    int ht_ins_ret_val = RETVAL_FAILURE;

    if ((NULL == htable) || (NULL == key) || (NULL == val))
    {
        goto HT_INSERT_RET;
    }

    pthread_mutex_lock(&(htable->mu_lock));

    ht_node_t *node = NULL;
    uint64_t   idx  = 0;

    if (htable->num_nodes
        > (htable->table_sz * (htable->l_factor / MAX_LFACTOR_PCT)))
    {
        if (0 != ht_resize(htable))
        {
            goto HT_INSERT_PRE_RET;
        }
    }

    // if the key already exists in the hashtable
    if (NULL != ht_search_priv(htable, key))
    {
        goto HT_INSERT_PRE_RET;
    }

    node = calloc(1, sizeof(*node));
    if (NULL == node)
    {
        perror("ht_insert node calloc");
        errno = 0;
        goto HT_INSERT_PRE_RET;
    }

    node->val = val;
    node->key = strdup(key);

    idx                = ht_hash(key, htable->table_sz);
    node->next         = htable->array[idx];
    htable->array[idx] = node;

    htable->num_nodes++;
    ht_ins_ret_val = RETVAL_SUCCESS;

HT_INSERT_PRE_RET:
    pthread_mutex_unlock(&(htable->mu_lock));

HT_INSERT_RET:
    return ht_ins_ret_val;
}

int32_t
ht_size (htable_t *htable)
{
    int32_t ht_sz_ret_val = RETVAL_FAILURE;
    if (NULL == htable)
    {
        goto HT_SIZE_RET;
    }

    ht_sz_ret_val = htable->num_nodes;

HT_SIZE_RET:
    return ht_sz_ret_val;
}

int32_t
ht_destroy (htable_t *htable, htiter_f freenode)
{
    int32_t ht_dest_ret_val = RETVAL_FAILURE;
    if ((NULL == htable) || (NULL == freenode))
    {
        goto HT_DEST_RET;
    }

    pthread_mutex_lock(&(htable->mu_lock));

    for (uint32_t idx = 0; idx < htable->table_sz; ++idx)
    {
        while (htable->array[idx])
        {
            ht_node_t *tmp     = htable->array[idx];
            htable->array[idx] = htable->array[idx]->next;
            freenode(tmp->val);
            free(tmp->key);
            free(tmp);
        }
    }

    free(htable->array);

    pthread_mutex_unlock(&(htable->mu_lock));
    pthread_mutex_destroy(&(htable->mu_lock));
    free(htable);

    ht_dest_ret_val = RETVAL_SUCCESS;

HT_DEST_RET:
    return ht_dest_ret_val;
}

// =============================================================================
//                               STATIC FUNCTIONS
// =============================================================================

/**
 * @brief Implementation of Bob Jenkin's One-At-A-Time Hashing algorithm.
 *  Allows for enough random uniformity for index uniqueness while being
 *      less computationally taxing than other standard hashing algorithms.
 *
 *  See the following links and writeups for further details:
 *      https://en.wikipedia.org/wiki/Jenkins_hash_function
 *      https://agkn.wordpress.com/2011/12/05/choosing-a-good-hash-function-part-1/
 *      https://agkn.wordpress.com/2011/12/29/choosing-a-good-hash-function-part-2/
 *      https://agkn.wordpress.com/2012/02/02/choosing-a-good-hash-function-part-3/
 *
 * @param   key     (const char*)   String to be hashed as the Key
 * @param   ht_sz   (uint64_t)      Size of Hashtable for index calculations
 *
 * @returns idx     (uint64_t)      Hashtable Index for associated Key
 */
static uint64_t
ht_hash (const char *key, uint64_t ht_sz)
{
    uint64_t hash = 0;

    for (uint32_t idx = 0; idx < strlen(key) + 1; ++idx)
    {
        hash += key[idx];
        hash += (hash << 10);
        hash ^= (hash >> 6);
    }
    hash += (hash << 3);
    hash ^= (hash >> 11);
    hash += (hash << 15);

    return hash % ht_sz;
}

/**
 * @brief Resize the Hashtable once given Load Factor is reached
 *
 * @param   htable  (htable_t*)     PTR to the Hashtable
 *
 * @returns 0 on Success, -1 on Failure
 */
static int32_t
ht_resize (htable_t *htable)
{
    int ht_res_ret_val = RETVAL_FAILURE;

    if (NULL == htable)
    {
        (void)fprintf(stderr, "ht_resize err: no hashtable provided");
        goto HT_RSZ_RET;
    }

    htable->table_sz *= 2;
    ht_node_t **temp = htable->array;

    htable->array = calloc(htable->table_sz, sizeof(ht_node_t *));
    if (NULL == htable->array)
    {
        perror("ht_resize new array calloc");
        errno = 0;
        goto HT_RSZ_RET;
    }

    for (uint32_t idx = 0; idx < htable->table_sz / 2; ++idx)
    {
        while (temp[idx])
        {
            ht_node_t *tmp = temp[idx];
            temp[idx]      = temp[idx]->next;
            ht_reinsert(htable, tmp->key, tmp->val);
            free(tmp->key);
            free(tmp);
        }
    }

    free(temp);
    ht_res_ret_val = RETVAL_SUCCESS;

HT_RSZ_RET:
    return ht_res_ret_val;
}

/**
 * @brief Private version of search. Searches the given Hashtable with
 * given KEY for VAL. Allows for threadsafe execution of the public search
 * without mutex race-conditions or lockouts.
 *
 * @param   htable      (htable_t*)     PTR to the Hashtable
 * @param   key         (const char*)   String to be hashed as the Key
 *
 * @returns ht_val      (void*)         PTR to the VAL stored at KEY, NULL if
 * Failed.
 */
static void *
ht_search_priv (htable_t *htable, const char *key)
{
    ht_node_t *tmp             = NULL;
    void      *ht_srch_ret_val = NULL;

    tmp = htable->array[ht_hash(key, htable->table_sz)];

    while ((tmp != NULL) && (strcmp(tmp->key, key) != 0))
    {
        tmp = tmp->next;
    }

    if (tmp == NULL)
    {
        goto HT_SRCH_RET;
    }

    ht_srch_ret_val = tmp->val;

HT_SRCH_RET:
    return ht_srch_ret_val;
}

/**
 * @brief Private ht_insert for use on ht_resize, where we insert VALUE (val)
 * into given Hashtable using given KEY. Assumes the following:
 *
 * call is within a thread-safe environemt (mutex locked),
 * all data within Hashtable has already been filtered for duplicative keys, and
 * that table size will fit all data (since it was doubled in ht_resize)
 *
 * @param   htable      (htable_t*)     PTR to the Hashtable
 * @param   key         (const char*)   String to be hashed as the Key
 * @param   val         (void*)         PTR to Value to be stored
 *
 * @returns 0 on Success, -1 if Failed.
 */
static int32_t
ht_reinsert (htable_t *htable, const char *key, void *val)
{
    int ht_ins_ret_val = RETVAL_FAILURE;

    if ((NULL == htable) || (NULL == key) || (NULL == val))
    {
        goto HT_REINSERT_RET;
    }

    ht_node_t *node = NULL;
    uint64_t   idx  = 0;

    node = calloc(1, sizeof(*node));
    if (NULL == node)
    {
        perror("ht_insert node calloc");
        errno = 0;
        goto HT_REINSERT_RET;
    }

    node->val = val;
    node->key = strdup(key);

    idx                = ht_hash(key, htable->table_sz);
    node->next         = htable->array[idx];
    htable->array[idx] = node;

    htable->num_nodes++;
    ht_ins_ret_val = RETVAL_SUCCESS;

HT_REINSERT_RET:
    return ht_ins_ret_val;
}

/*** end of file ***/
