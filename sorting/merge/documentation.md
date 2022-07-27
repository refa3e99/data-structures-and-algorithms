# Insertion Sort

The Merge Sort algorithm is a sorting algorithm that is considered an example of the divide and conquer strategy. So, in this algorithm, the array is initially divided into two equal halves and then they are combined in a sorted manner. We can think of it as a recursive algorithm that continuously splits the array in half until it cannot be further divided. This means that if the array becomes empty or has only one element left, the dividing will stop, i.e. it is the base case to stop the recursion. If the array has multiple elements, we split the array into halves and recursively invoke the merge sort on each of the halves. Finally, when both the halves are sorted, the merge operation is applied. Merge operation is the process of taking two smaller sorted arrays and combining them to eventually make a larger one.
## Pseudocode

```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left

```

### Trace 
Sample Arrray : ```[38, 27, 43, 3, 9, 82, 10]```

Pass 1

At first, check if the left index of array is less than the right index, if yes then calculate its mid point
Here, we see that an array of 7 items is divided into two arrays of size 4 and 3 respectively.
```[38, 27, 43, 3]``` AND ```[ 9, 82, 10]```

Pass 2
Now, further divide these two arrays into further halves, until the atomic units of the array is reached and further division is not possible.
```[38] , [27] , [43] , [3] , [9] , [82] , [10]```

Pass 3
After dividing the array into smallest units, start merging the elements again based on comparison of size of elements
Firstly, compare the element for each list and then combine them into another list in a sorted manner.

```[38,27] , [43,3] , [9,82] , [10]```
after that the elements are sorted
```[27,38] , [3,43] , [9,82] , [10]```

Pass 4 
We keep merging and sorting the sub arrays utill we finish at a one array
```[3,27,38,43] , [9,10,82]```

last merging
```[3,9,10,27,38,43,82]```

Finally the array is sorted

### Efficency
- Time: O(n log(n))
- Space: O(n)