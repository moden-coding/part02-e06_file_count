#!/usr/bin/env python3

import sys

def file_count(filename):
    total_lines = 0
    total_words = 0
    total_chars = 0
    
    with open(filename, "r") as f:
        for line in f:
            total_lines += 1
            total_chars += len(line)
            if line != "\n":
                total_words += len(line.split(" "))
    
    return (total_lines, total_words, total_chars)

def main():
    
    for file in sys.argv[1:]:
        data = file_count(file)
        print(f"{data[0]}\t{data[1]}\t{data[2]}\t{file}")


if __name__ == "__main__":
    main()
