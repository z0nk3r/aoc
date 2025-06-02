#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/evp.h>

#define FILENAME "input"

// Custom Print Strings for shorthand message printing
#define pass(msg, ...) printf("\033[1;32m[+]\033[0m " msg, ##__VA_ARGS__)  // green bold
#define info(msg, ...) printf("\033[1;34m[-]\033[0m " msg, ##__VA_ARGS__)  // blue bold
#define warn(msg, ...) printf("\033[1;33m[!]\033[0m " msg, ##__VA_ARGS__)  // yellow bold
#define fail(msg, ...) printf("\033[1;31m[x]\033[0m " msg, ##__VA_ARGS__)  // red bold

static int32_t part1(FILE *fp_input);
static int32_t part2(FILE *fp_input);
static int8_t  startswith(uint8_t *p_buff, const unsigned char *string);

int32_t
main (int argc, char **argv)
{
    (void)argc;
    (void)argv;

    FILE *fp_input = NULL;

    fp_input = fopen(FILENAME, "r");
    if (NULL == fp_input)
    {
        fail("Unable to open input file '%s'\n", FILENAME);
        return -1;
    }

    part1(fp_input);
    rewind(fp_input);
    part2(fp_input);

    (void)fclose(fp_input);

    return 0;
}

// =============================================================================
//                               STATIC FUNCTIONS
// =============================================================================

static int32_t
part1 (FILE *fp_input)
{
    int32_t p1_retval = 0;

    char       key[16]      = { 0 };
    int32_t    key_idx      = 0;
    char       new_key[32]  = { 0 };

    EVP_MD_CTX    *mdctx              = NULL;
    unsigned char *md5_digest         = NULL;
    unsigned int   md5_digest_len     = EVP_MD_size(EVP_md5());
    unsigned char  md5_digest_str[34] = { 0 };
    uint8_t       *p_md5_dig_str      = NULL;

    if (NULL == (fgets(key, sizeof(key), fp_input)))
    {
        warn("couldn't read the line from the file\n");
        goto RETURN;
    }

    while (1)
    {
        mdctx = EVP_MD_CTX_new();
        if (NULL == mdctx)
        {
            warn("unable to init MD context\n");
            goto RETURN;
        }

        if (0 == EVP_DigestInit_ex(mdctx, EVP_md5(), NULL))
        {
            warn("unable to setup MD context as MD5 context\n");
            goto RETURN;
        }

        md5_digest = (unsigned char *)OPENSSL_zalloc(md5_digest_len);
        if (NULL == md5_digest)
        {
            warn("unable to calloc MD5 digest buffer");
            goto RETURN;
        }

        snprintf(new_key, 32, "%s%d", key, key_idx);
        EVP_DigestUpdate(mdctx, new_key, strlen(new_key));
        EVP_DigestFinal_ex(mdctx, md5_digest, &md5_digest_len);
        EVP_MD_CTX_free(mdctx);

        // hexdump to string
        p_md5_dig_str = &md5_digest_str[0];
        for (int i = 0; i < md5_digest_len; i++)
        {
            p_md5_dig_str += sprintf(p_md5_dig_str, "%02x", md5_digest[i]);
        }

        if (startswith(md5_digest_str, "00000"))
        {
            break;
        }
        key_idx++;
    }
    
    p1_retval = key_idx;

 RETURN:
    info("Part 1 Results: %d\n", p1_retval);
    return p1_retval;
}

static int32_t
part2 (FILE *fp_input)
{
    int32_t p2_retval = 0;


    char       key[16]      = { 0 };
    int32_t    key_idx      = 0;
    char       new_key[32]  = { 0 };

    EVP_MD_CTX    *mdctx              = NULL;
    unsigned char *md5_digest         = NULL;
    unsigned int   md5_digest_len     = EVP_MD_size(EVP_md5());
    unsigned char  md5_digest_str[34] = { 0 };
    uint8_t       *p_md5_dig_str      = NULL;

    if (NULL == (fgets(key, sizeof(key), fp_input)))
    {
        warn("couldn't read the line from the file\n");
        goto RETURN;
    }

    while (1)
    {
        mdctx = EVP_MD_CTX_new();
        if (NULL == mdctx)
        {
            warn("unable to init MD context\n");
            goto RETURN;
        }

        if (0 == EVP_DigestInit_ex(mdctx, EVP_md5(), NULL))
        {
            warn("unable to setup MD context as MD5 context\n");
            goto RETURN;
        }

        md5_digest = (unsigned char *)OPENSSL_zalloc(md5_digest_len);
        if (NULL == md5_digest)
        {
            warn("unable to calloc MD5 digest buffer");
            goto RETURN;
        }

        snprintf(new_key, 32, "%s%d", key, key_idx);
        EVP_DigestUpdate(mdctx, new_key, strlen(new_key));
        EVP_DigestFinal_ex(mdctx, md5_digest, &md5_digest_len);
        EVP_MD_CTX_free(mdctx);

        // hexdump to string
        p_md5_dig_str = &md5_digest_str[0];
        for (int i = 0; i < md5_digest_len; i++)
        {
            p_md5_dig_str += sprintf(p_md5_dig_str, "%02x", md5_digest[i]);
        }

        if (startswith(md5_digest_str, "000000"))
        {
            break;
        }
        key_idx++;
    }
    
    p2_retval = key_idx;

 RETURN:
    info("Part 2 Results: %d\n", p2_retval);
    return p2_retval;
}

static int8_t
startswith(uint8_t *p_buff, const unsigned char *string)
{
    int32_t retval = 0;
    for (int i = 0; i < strlen(string); i++)
    {
        if (p_buff[i] != string[i]) 
        {
            goto RETURN_SWITH;
        }
    }
    retval = 1;

RETURN_SWITH:
    return retval;
}