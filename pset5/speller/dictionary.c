// Implements a dictionary's functionality

#include <stdbool.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 1;

// node * table[N] = {NULL};
// Hash table
node *table[N];

int counter = 0;

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    int place = hash(word);

    // Referenced https://www.zentut.com/c-tutorial/c-linked-list/#Traverse_the_linked_list to traverse linked list
    // put cursor at start of linked list
    node *cursor = table[place];
    while (cursor != NULL)
    {
        // if matches word in dictionary
        if (strcasecmp(word, cursor->word) == 0)
        {
            // printf("check 1\n");
            return true;
        }
        // otherwise
        else
        {
            cursor = cursor->next;
        }
        // printf("check 2\n");
        // printf("%s", cursor->word);
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
// Referenced https://github.com/bahalperin/spell-checker/blob/master/dictionary.c
{
    //hash function from online
    int sum = 0;
    int word_length = strlen(word);

    for (int i = 0; i < word_length; i++)
    {
        sum += word[i];
    }
    //assign to bucket and return
    int bucket = sum % N;
    return bucket;
}


// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // open dictionary
    FILE *f = fopen(dictionary, "r");
    if (f == NULL)
    {
        return 1;
    }

    char words[LENGTH + 1];
    // loop through words
    while (fscanf(f, "%s", words) != EOF)
    {
        node *n = malloc(sizeof(node));
        n->next = NULL;
        if (n == NULL)
        {
            printf("check 3\n");
            return false;
        }
        strcpy(n->word, words);
        int place = hash(words);
        //if first word
        if (table[place] == NULL)
        {
            table[place] = n;
        }
        // otherwise
        else
        {
            n->next = table[place];
            table[place] = n;
        }
        counter++;
        // printf("check 4\n");

    }
    fclose(f);
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return counter;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    //loop through all memory allocations
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        node *temp = cursor;
        while (cursor != NULL)
        {
            temp = cursor;
            cursor = cursor->next;
            free(temp);
            // printf("check 5\n");
        }
    }
    return true;
}