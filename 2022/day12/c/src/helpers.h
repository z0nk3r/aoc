#ifndef HELPERS_H
#define HELPERS_H

#include <stdio.h>
#include "lib_bfs.h"

// Parses .csv and generates db of edgelist
//
int load_file(llist_t *db, FILE *fp);

#endif
