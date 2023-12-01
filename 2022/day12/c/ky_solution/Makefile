CFLAGS := -std=c18
CFLAGS += -Wall -Wextra -Wpedantic
CFLAGS += -Wwrite-strings -Wvla -Wfloat-equal -Waggregate-return

all:
	gcc bfs.c llist.c graph.c -g3 -o bfs
	./bfs

clean:
	rm -rf bfs
