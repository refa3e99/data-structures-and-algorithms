# array insert-shift
Write a function called insertShiftArray which takes in
an array and a value to be added. Without utilizing any
of the built-in methods available to your language,
return an array with the new value added at the
middle index.

## Whiteboard Process
![image](./shiftarray.png)
## Approach & Efficiency
We need to insert a number in the middle of a given array,
all of the elements should stay in the same order but the number
should be inserted between them in the middle.
we should check if the length of the array is odd or even at first to
determine where we should insert the integer,
if its even we isert the integer in the middle,
if its odd we insert it in the middle plus one.
We should initialize a new array so we can add the first part
of the given array sliced from index 0 to the middle, then 
we should append the given element at the last of the initialized
array, and at last, we add the remaining part of the given array
sliced from the middle all the way to the last element.

## time complexity
big O(log n) 
