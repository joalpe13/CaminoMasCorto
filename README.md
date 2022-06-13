# CaminoMasCorto

Hello, this program is responsible for finding the shortest path within a matrix. The tour goes from the first column to the last, being able to change rows as long as they are adjacent.

For example in a matrix:  
4 - 5 - 6  
7 - 8 - 1  
2 - 3 - 4

You can go from 7 to 5, 8 and 3, after 5 you can go to 6 or 1.

The algorithm goes through all the possible paths and adds them to determine which has a lower value. In the previous matrix the smallest value would be found by traversing 2, 3, 1

## Usage

To use this program you just have to modify the values ​​and/or the size of the array "M1" of the file main.py

You can see the explanation of it in the following video https://www.youtube.com/watch?v=pioBWYuHiCU

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
