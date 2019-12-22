#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //Average and round
            float sum = image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed;
            int avg = (int) round(sum / 3);
            image[i][j].rgbtBlue = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtRed = avg;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //Enter sepia formula
            int sepiaRed = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);
            int sepiaGreen = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);
            int sepiaBlue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);
            //Keep colors within range
            if (sepiaRed >= 255)
            {
                sepiaRed = 255;
            }
            if (sepiaGreen >= 255)
            {
                sepiaGreen = 255;
            }
            if (sepiaBlue >= 255)
            {
                sepiaBlue = 255;
            }
            //Assign colors
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            //Loop through half and switch it with the other half
            int redTemp = image[i][j].rgbtRed;
            int greenTemp = image[i][j].rgbtGreen;
            int blueTemp = image[i][j].rgbtBlue;
            //Map to opposite pixel
            image[i][j].rgbtBlue = image[i][width - 1 - j].rgbtBlue;
            image[i][j].rgbtGreen = image[i][width - 1 - j].rgbtGreen;
            image[i][j].rgbtRed = image[i][width - 1 - j].rgbtRed;
            image[i][width - 1 - j].rgbtBlue = blueTemp;
            image[i][width - 1 - j].rgbtRed = redTemp;
            image[i][width - 1 - j].rgbtGreen = greenTemp;
        }
    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    //make new structure to store colors so the rest of the function can just impact the original image
    RGBTRIPLE new1[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            new1[i][j] = image[i][j];
        }
    }
    //Loop through
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //Middle
            if ((i >= 1 && i <= height - 2) && (j >= 1 && j <= width - 2))
            {
                float sumRed = image[i - 1][j - 1].rgbtRed + image[i + 1][j - 1].rgbtRed + image[i][j - 1].rgbtRed +
                               image[i - 1][j].rgbtRed + image[i][j].rgbtRed + image[i + 1][j].rgbtRed + image[i - 1][j + 1].rgbtRed +
                               image[i][j + 1].rgbtRed + image[i + 1][j + 1].rgbtRed;
                float sumGreen = image[i - 1][j - 1].rgbtGreen + image[i + 1][j - 1].rgbtGreen + image[i][j - 1].rgbtGreen +
                                 image[i - 1][j].rgbtGreen + image[i][j].rgbtGreen + image[i + 1][j].rgbtGreen +
                                 image[i - 1][j + 1].rgbtGreen + image[i][j + 1].rgbtGreen + image[i + 1][j + 1].rgbtGreen;
                float sumBlue = image[i - 1][j - 1].rgbtBlue + image[i + 1][j - 1].rgbtBlue + image[i][j - 1].rgbtBlue +
                                image[i - 1][j].rgbtBlue + image[i][j].rgbtBlue + image[i + 1][j].rgbtBlue + image[i - 1][j + 1].rgbtBlue +
                                image[i][j + 1].rgbtBlue + image[i + 1][j + 1].rgbtBlue;
                //Compute average
                int avgRed = (int)round(sumRed / 9);
                int avgGreen = (int)round(sumGreen / 9);
                int avgBlue = (int)round(sumBlue / 9);
                new1[i][j].rgbtBlue = avgBlue;
                new1[i][j].rgbtGreen = avgGreen;
                new1[i][j].rgbtRed = avgRed;
            }
            //Edge
            else if (i == 0 && j > 0 && j < width - 1)
            {
                float sumRed = image[i + 1][j - 1].rgbtRed + image[i][j - 1].rgbtRed + image[i][j].rgbtRed + image[i + 1][j].rgbtRed +
                               image[i][j + 1].rgbtRed + image[i + 1][j + 1].rgbtRed;
                float sumGreen = image[i + 1][j - 1].rgbtGreen + image[i][j - 1].rgbtGreen + image[i][j].rgbtGreen + image[i + 1][j].rgbtGreen +
                                 image[i][j + 1].rgbtGreen + image[i + 1][j + 1].rgbtGreen;
                float sumBlue = image[i + 1][j - 1].rgbtBlue + image[i][j - 1].rgbtBlue + image[i][j].rgbtBlue + image[i + 1][j].rgbtBlue +
                                image[i][j + 1].rgbtBlue + image[i + 1][j + 1].rgbtBlue;
                //Average
                int avgRed = (int)round(sumRed / 6);
                int avgGreen = (int)round(sumGreen / 6);
                int avgBlue = (int)round(sumBlue / 6);
                new1[i][j].rgbtBlue = avgBlue;
                new1[i][j].rgbtGreen = avgGreen;
                new1[i][j].rgbtRed = avgRed;
            }
            //Edge
            else if (i == height - 1 && j > 0 && j < width - 1)
            {
                float sumRed = image[i - 1][j - 1].rgbtRed + image[i][j - 1].rgbtRed + image[i - 1][j].rgbtRed + image[i][j].rgbtRed +
                               image[i - 1][j + 1].rgbtRed + image[i][j + 1].rgbtRed;
                float sumGreen = image[i - 1][j - 1].rgbtGreen + image[i][j - 1].rgbtGreen + image[i - 1][j].rgbtGreen + image[i][j].rgbtGreen +
                                 image[i - 1][j + 1].rgbtGreen + image[i][j + 1].rgbtGreen;
                float sumBlue = image[i - 1][j - 1].rgbtBlue + image[i][j - 1].rgbtBlue + image[i - 1][j].rgbtBlue + image[i][j].rgbtBlue +
                                image[i - 1][j + 1].rgbtBlue + image[i][j + 1].rgbtBlue;
                //Average
                int avgRed = (int)round(sumRed / 6);
                int avgGreen = (int)round(sumGreen / 6);
                int avgBlue = (int)round(sumBlue / 6);
                new1[i][j].rgbtBlue = avgBlue;
                new1[i][j].rgbtGreen = avgGreen;
                new1[i][j].rgbtRed = avgRed;
            }
            //Edge
            else if (j == height - 1 && i > 0 && i < width - 1)
            {
                float sumRed = image[i - 1][j - 1].rgbtRed + image[i + 1][j - 1].rgbtRed + image[i][j - 1].rgbtRed + image[i - 1][j].rgbtRed +
                               image[i][j].rgbtRed + image[i + 1][j].rgbtRed;
                float sumGreen = image[i - 1][j - 1].rgbtGreen + image[i + 1][j - 1].rgbtGreen + image[i][j - 1].rgbtGreen +
                                 image[i - 1][j].rgbtGreen + image[i][j].rgbtGreen + image[i + 1][j].rgbtGreen;
                float sumBlue = image[i - 1][j - 1].rgbtBlue + image[i + 1][j - 1].rgbtBlue + image[i][j - 1].rgbtBlue +
                                image[i - 1][j].rgbtBlue + image[i][j].rgbtBlue + image[i + 1][j].rgbtBlue;
                //Average
                int avgRed = (int)round(sumRed / 6);
                int avgGreen = (int)round(sumGreen / 6);
                int avgBlue = (int)round(sumBlue / 6);
                new1[i][j].rgbtBlue = avgBlue;
                new1[i][j].rgbtGreen = avgGreen;
                new1[i][j].rgbtRed = avgRed;
            }
            //Edge
            else if (j == 0 && i > 0 && i < height - 1)
            {
                float sumRed = image[i - 1][j].rgbtRed + image[i][j].rgbtRed + image[i + 1][j].rgbtRed + image[i - 1][j + 1].rgbtRed +
                               image[i][j + 1].rgbtRed + image[i + 1][j + 1].rgbtRed;
                float sumGreen = image[i - 1][j].rgbtGreen + image[i][j].rgbtGreen + image[i + 1][j].rgbtGreen + image[i - 1][j + 1].rgbtGreen +
                                 image[i][j + 1].rgbtGreen + image[i + 1][j + 1].rgbtGreen;
                float sumBlue = image[i - 1][j].rgbtBlue + image[i][j].rgbtBlue + image[i + 1][j].rgbtBlue + image[i - 1][j + 1].rgbtBlue +
                                image[i][j + 1].rgbtBlue + image[i + 1][j + 1].rgbtBlue;
                //Average
                int avgRed = (int)round(sumRed / 6);
                int avgGreen = (int)round(sumGreen / 6);
                int avgBlue = (int)round(sumBlue / 6);
                new1[i][j].rgbtBlue = avgBlue;
                new1[i][j].rgbtGreen = avgGreen;
                new1[i][j].rgbtRed = avgRed;
            }
            //Corner
            else if (i == 0 && j == 0)
            {
                float sumRed = image[i][j].rgbtRed + image[i + 1][j].rgbtRed + image[i][j + 1].rgbtRed + image[i + 1][j + 1].rgbtRed;
                float sumGreen = image[i][j].rgbtGreen + image[i + 1][j].rgbtGreen + image[i][j + 1].rgbtGreen + image[i + 1][j + 1].rgbtGreen;
                float sumBlue = image[i][j].rgbtBlue + image[i + 1][j].rgbtBlue + image[i][j + 1].rgbtBlue + image[i + 1][j + 1].rgbtBlue;
                //Average
                int avgRed = (int)round(sumRed / 4);
                int avgGreen = (int)round(sumGreen / 4);
                int avgBlue = (int)round(sumBlue / 4);
                new1[i][j].rgbtBlue = avgBlue;
                new1[i][j].rgbtGreen = avgGreen;
                new1[i][j].rgbtRed = avgRed;
            }
            //Corner
            else if (i == 0 && j == width - 1)
            {
                float sumRed = image[i + 1][j - 1].rgbtRed + image[i][j - 1].rgbtRed + image[i][j].rgbtRed + image[i + 1][j].rgbtRed;
                float sumGreen = image[i + 1][j - 1].rgbtGreen + image[i][j - 1].rgbtGreen + image[i][j].rgbtGreen + image[i + 1][j].rgbtGreen;
                float sumBlue = image[i + 1][j - 1].rgbtBlue + image[i][j - 1].rgbtBlue + image[i][j].rgbtBlue + image[i + 1][j].rgbtBlue;
                //Average
                int avgRed = (int)round(sumRed / 4);
                int avgGreen = (int)round(sumGreen / 4);
                int avgBlue = (int)round(sumBlue / 4);
                new1[i][j].rgbtBlue = avgBlue;
                new1[i][j].rgbtGreen = avgGreen;
                new1[i][j].rgbtRed = avgRed;
            }
            //Corner
            else if (j == 0 && i == height - 1)
            {
                float sumRed = image[i - 1][j].rgbtRed + image[i][j].rgbtRed + image[i - 1][j + 1].rgbtRed + image[i][j + 1].rgbtRed;
                float sumGreen = image[i - 1][j].rgbtGreen + image[i][j].rgbtGreen + image[i - 1][j + 1].rgbtGreen + image[i][j + 1].rgbtGreen;
                float sumBlue = image[i - 1][j].rgbtBlue + image[i][j].rgbtBlue + image[i - 1][j + 1].rgbtBlue + image[i][j + 1].rgbtBlue;
                //Average
                int avgRed = (int)round(sumRed / 4);
                int avgGreen = (int)round(sumGreen / 4);
                int avgBlue = (int)round(sumBlue / 4);
                new1[i][j].rgbtBlue = avgBlue;
                new1[i][j].rgbtGreen = avgGreen;
                new1[i][j].rgbtRed = avgRed;
            }
            //Corner
            else if (j == width - 1 && i == height - 1)
            {
                float sumRed = image[i - 1][j - 1].rgbtRed + image[i][j - 1].rgbtRed + image[i - 1][j].rgbtRed + image[i][j].rgbtRed;
                float sumGreen = image[i - 1][j - 1].rgbtGreen + image[i][j - 1].rgbtGreen + image[i - 1][j].rgbtGreen + image[i][j].rgbtGreen;
                float sumBlue = image[i - 1][j - 1].rgbtBlue + image[i][j - 1].rgbtBlue + image[i - 1][j].rgbtBlue + image[i][j].rgbtBlue;
                //Average
                int avgRed = (int)round(sumRed / 4);
                int avgGreen = (int)round(sumGreen / 4);
                int avgBlue = (int)round(sumBlue / 4);
                new1[i][j].rgbtBlue = avgBlue;
                new1[i][j].rgbtGreen = avgGreen;
                new1[i][j].rgbtRed = avgRed;
            }

        }
    }
    //Put new colors back in original image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = new1[i][j];
        }
    }
    return;
}
