#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

const int DIRS[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

int find_cave_size(int x, int y, char buffer[100][105], bool visited[100][105], int ROWS, int COLS) {
    visited[x][y] = true;
    int size = 1;

    for (int _ = 0; _ < 4; _++) {
        int i = x + DIRS[_][0];
        int j = y + DIRS[_][1];
        if (i < 0 || j < 0 || i >= ROWS || j >= COLS) continue;
        if (visited[i][j] || buffer[x][y] >= buffer[i][j] || buffer[i][j] == '9') continue;
        size += find_cave_size(i, j, buffer, visited, ROWS, COLS);
    }

    return size;
}

int cmp (const void *a, const void *b)  { 
    int int_a = * ( (int*) a );
    int int_b = * ( (int*) b );
    return int_b - int_a;
} 

int main() {

    char buffer[100][105];
    bool visited[100][105];
    int caves[1000];

    int ROWS = 0;
    int COLS = 0;
    

    for (int i = 0; i < 100; i++) {
        for (int i = 0; i < 10; i++)
            caves[100 * i + i] = -1;
        for (int j = 0; j < 105; j++)
            visited[i][j] = false;
    }


    FILE *input = fopen("day9.txt", "r");

    while (fgets(buffer[ROWS], sizeof(buffer), input)) {
        COLS = strlen(buffer[ROWS]); // fuck the newline
        ROWS++;
    }

    int cave_index = 0;
    int risk = 0;

    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            int options = 0;
            int smaller_than = 0;
            for (int _ = 0; _ < 4; _++) {
                int ii = i + DIRS[_][0];
                int jj = j + DIRS[_][1];
                if (ii < 0 || jj < 0 || ii >= ROWS || jj >= COLS)
                    continue;
                options++;
                if (buffer[i][j] < buffer[ii][jj])
                    smaller_than++;
            }
            if (options == smaller_than && options) {
                risk += 1 + buffer[i][j] - '0';
                int cave_size = find_cave_size(i, j, buffer, visited, ROWS, COLS);
                caves[cave_index++] = cave_size;
            }
        }
    }

    qsort(caves, 1000, sizeof(int), cmp);

    printf("Part 1: %d\n", risk);
    printf("Part 2: %d\n", caves[0] * caves[1] * caves[2]);

    fclose(input);
    return 0;
}