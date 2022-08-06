# Hashtables
<!-- Short summary or background information -->
Hashtable is a data structure that implements a set abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found. During lookup, the key is hashed and the resulting hash indicates where the corresponding value is stored.
## Challenge
<!-- Description of the challenge -->

#### Implement a Hashtable Class with the following methods:

- set
- get
- contains
- keys
- hash

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

- contains:

Time Complexity: O(n)

Space Complexity: O(n)

- keys:

Time Complexity: O(1)

Space Complexity: O(1)

- hash:

Time Complexity: O(1)

Space Complexity: O(1)

- set:

Time Complexity: O(1)

Space Complexity: O(n)

- get:

Time Complexity: O(n)

Space Complexity: O(n)
## API
<!-- Description of each method publicly available in each of your hashtable -->

- set

```Arguments: key, value```

```Returns: nothing```

This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
Should a given key already exist, replace its value from the value argument given to this method.
- get

```Arguments: key```

```Returns: Value associated with that key in the table```
- contains

```Arguments: key```

```Returns: Boolean, indicating if the key exists in the table already.```
- keys

```Returns: Collection of keys```

- hash

```Arguments: key```

```Returns: Index in the collection for that key```