/** 
 * @file
 *
 * @brief Hashtable Library for O(1) Lookup of data by keyword.
 * Analogous to a Python Dictionary.
 */

#ifndef LIB_HASHTABLE_H
#define LIB_HASHTABLE_H

#include <stdint.h>

/**
 * @typedef htable_t
 * 
 * @brief struct htable_t - struct for containing all Hashtable metadata
 * @param   table_sz    (uint32_t)        SIZE of the hashtable
 * @param   num_nodes   (int32_t)         SIZE of the number of nodes/data
 * @param   l_factor    (double)          DOUBLE used to calculate load factor and resize as needed
 * @param   array       (ht_node_t **)    ARRAY of nodes of the hashtable
 * @param   mu_lock     (pthread_mutex_t) MUTEX LOCK to prevent simultaneous asynchronous read/writes
 */
typedef struct htable_t htable_t;

#define RETVAL_FAILURE  -1
#define RETVAL_SUCCESS  0
#define MAX_LFACTOR_PCT 100

// =============================================================================
//                               FUNCTION POINTERS
// =============================================================================
/**
 * @brief Function pointer that takes a single data point and does FUNC on DATA.
 *
 * Used for ht_iter and free-ing on ht_delete/ht_destroy.
 */
typedef void (*htiter_f)(void *);

/**
 * @brief Create a Hashtable/Hashmap Data Structure, allowing for O(1)* lookup
 * of data. This implementation uses Bob Jenkin's One-At-A-Time Hashing
 * Algorithm and Linked-List Seperate Chaining in the event of Hash Collisions.
 * Mutexes implemented for multithreaded read/write operations.
 *
 * @param   table_sz    (int32_t)   Initial Size of the Hashtable
 * @param   l_factor    (double)    Load factor before Hashtable resizes IOT
 * maintain performance (N out of 100)
 *
 * @returns htable      (htable_t*) PTR to the Hashtable; NULL if Failed.
 */
htable_t *ht_create(int32_t table_sz, double l_factor);

/**
 * @brief Insert VALUE (val) into given Hashtable using given KEY
 *
 * @param   htable      (htable_t*)     PTR to the Hashtable
 * @param   key         (const char*)   String to be hashed as the Key
 * @param   val         (void*)         PTR to Value to be stored
 *
 * @returns 0 on Success, -1 if Failed.
 */
int32_t ht_insert(htable_t *htable, const char *key, void *val);

/**
 * @brief Returns the size of the given Hashtable
 *
 * @param   htable      (htable_t*)     PTR to the Hashtable
 *
 * @returns ht_size     (int32_t)       Size of the Hashtable, -1 if Failed
 */
int32_t ht_size(htable_t *htable);

/**
 * @brief Teardown and Destroy the entire Hashtable
 *
 * @param   htable      (htable_t*)     PTR to the Hashtable
 * @param   freenode    (htiter_f)      Func PTR for custom cleanup of Hashtable
 * data stored in VAL
 *
 * @returns 0 on Success, -1 if Failed.
 */
int32_t ht_destroy(htable_t *htable, htiter_f freenode);

#endif /* LIB_HASHTABLE_H */

/*** end of file ***/
