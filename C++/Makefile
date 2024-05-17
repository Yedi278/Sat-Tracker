
CC = g++

SOURCE = $(wildcard src/*.cpp)
HEADS = include
LIB = lib

CFLAGS = -Wall -g -std=c++17

LFLAGS = -lGL -lGLEW -lglfw

compile:
	$(CC) $(CFLAGS) -I$(HEADS) $(SOURCE) $(LFLAGS) -o build/Build

run:
	./build/Build

all: compile run