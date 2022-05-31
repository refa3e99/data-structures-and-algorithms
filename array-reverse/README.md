# Reverse an Array
**Write a function called reverseArray which takes an array as an argument. Without utilizing any of the built-in methods available to your language, return an array with elements in reversed order.**

## Whiteboard Process
![image](./White%20board%201.png)

## Approach & Efficiency

**Rational approach**
- Define the problem.
- Identify possible causes.
- Brainstorm options to solve the problem.
- Select an option.
- Create an implementation plan.
- Execute the plan and monitor the results.
- Evaluate the solution.

We need to reverse a given array by printing the value of it in a reversed order; the last element should be at first followed by the second one and so on.
We should initialize a new empty array to append in it the array but in reverse order.
I solved it by looping in range of the length of the given array and going down to index zero and append the value of the index in the empty array.
This will do the job for this task.

### time complexity : Big O(n) => where n is the number of iterations (size of the array)
