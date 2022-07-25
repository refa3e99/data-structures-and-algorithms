# Insertion Sort

Insertion sort is a sorting algorithm that places an unsorted element at its suitable place in each iteration. Insertion sort works similarly as we sort cards in our hand in a card game. We assume that the first card is already sorted then, we select an unsorted card.

## Pseudocode

```
 InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp
```

### Trace 
Sample Arrray : ```[8,4,23,42,16,15]```

Pass 1

Initially, the first two elements of the array are compared in insertion sort.
```[8,4,23,42,16,15]```
Here, 8 is greater than 4 hence they are not in the ascending order and 8 is not at its correct position. Thus, swap 4 and 8.
So, for now 8 is stored in a sorted variable.
```[4,8,23,42,16,15]```

Pass 2

Now, move to the next two elements and compare them
```[4,8,23,42,16,15]```
Here 23 and 42 are in the correct order for now, no swapping will occur, yet.

Pass 3

Moving to the next elements, 16 and 15 are not in the correct order.
```[4,8,23,42,16,15]```
16 is less than 42 and by moving to the left one more iteration we find that its also less than 23 and greater than 8
so we place it before 23
```[4,8,16,23,42,15]```

Pass 4 

Moving to the next elements we find 15 in the wrong index as its less than 42
```[4,8,16,23,42,15]```
and its also less than 23, 16 and greater than 8
so we place it before 16
```[4,8,15,16,23,42]```

Finally the array is sorted

### Efficency
- Time: O(n^2)
- Space: O(1)