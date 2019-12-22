#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    //set booleans and counters
    int counter = 0;
    int found = 0;
    //open file
    FILE *f = fopen(argv[1], "r");
    FILE *img;
    //will store images
    char *filename = malloc(4);
    // invalid check
    unsigned char buffer[512];
    if (!f)
    {
        return 1;
    }
    //loop through and read
    while (fread(buffer, 512, 1, f))
    {
        //if start of new jpeg
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            //first jpeg?
            if (counter == 0)
            {
                sprintf(filename, "%03i.jpg", counter);
                printf("%s", filename);
                img = fopen(filename, "w");
                fwrite(buffer, 512, 1, img);
            }
            else
            {
                fclose(img);
                sprintf(filename, "%03i.jpg", counter);
                printf("%s", filename);
                img = fopen(filename, "w");
                fwrite(buffer, 512, 1, img);
            }
            counter++;
            found = 1;
        }
        //keep looping through if you found
        else
        {
            if (found == 1)
            {
                fwrite(buffer, 512, 1, img);
            }
        }

    }
    //close storages
    fclose(img);
}
