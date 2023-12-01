# Makefile for executable

# *****************************************************
# Parameters to control Makefile operation
# BIN := ht_driver
BIN := $(shell grep "main" src/*.c -l | cut -f2 -d/ | cut -f1 -d.)

CHECK := check_$(BIN)

SRC_DIR := src
OBJ_DIR := obj
INC_DIR := src
TST_DIR := test

SRCS := $(wildcard $(SRC_DIR)/*.c)
OBJS := $(patsubst $(SRC_DIR)/%.c, $(OBJ_DIR)/%.o, $(SRCS))

TSTS := $(wildcard $(TST_DIR)/*.c)
TST_OBJS := $(filter-out $(OBJ_DIR)/$(BIN).o, $(OBJS))
TST_OBJS += $(patsubst $(TST_DIR)/%.c, $(OBJ_DIR)/%.o, $(TSTS))
TST_LIBS := -lcheck -lm -pthread -lrt -lsubunit

CC := gcc-9
CFLAGS := -Wall -Wextra -Wpedantic -Wwrite-strings -Wstack-usage=1024
CFLAGS += -Wfloat-equal -Waggregate-return -Winline -Wvla -std=c18
# CFLAGS += -fsanitize=address -static-libasan

VFLAGS := -s --track-origins=yes --leak-check=full --show-leak-kinds=all

# ****************************************************
# Entries to bring the executable up to date

all: $(BIN)

test: $(BIN)
	@./$(BIN)

backtrace: CFLAGS += -g
backtrace: clean $(BIN)
	gdb -ex="set confirm off" -ex r -ex bt -q --args ./$(BIN)

check: $(CHECK)

clean:
	@rm -rf $(OBJ_DIR) $(BIN) $(CHECK)

debug: CFLAGS += -g3
debug: $(BIN)

profile: CFLAGS += -g3 -pg
profile: $(BIN)

valgrind: CFLAGS += -g3
valgrind: clean $(BIN)
valgrind:
	valgrind $(VFLAGS) ./$(BIN)

valcheck: CFLAGS += -g3
valcheck: clean $(BIN)
valcheck:
	valgrind $(VFLAGS) -DVALGRIND ./$(CHECK)

$(OBJ_DIR):
	@mkdir -p $@

$(OBJS): | $(OBJ_DIR)

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
	@$(CC) $(CFLAGS) -I $(INC_DIR) -c $< -o $@

$(OBJ_DIR)/%.o: $(TST_DIR)/%.c
	@$(CC) $(CFLAGS) -I $(INC_DIR) -c $< -o $@

$(BIN): $(OBJS)
	@$(CC) $(CFLAGS) $^ -o $@ -lm

$(CHECK): $(TST_OBJS)
	@$(CC) $(CFLAGS) $^ -o $@ $(TST_LIBS)
	@./$(CHECK)
