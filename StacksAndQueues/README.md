# Stacks and Queues
A stack is a data structure that consists of Nodes. Each Node references the next Node in the stack, but does not reference its previous.

Common terminology for a stack is

- Push - Nodes or items that are put into the stack are pushed
- Pop - Nodes or items that are removed from the stack are popped. When you attempt to pop an empty stack an exception will be raised.
- Top - This is the top of the stack.
- Peek - When you peek you will view the value of the top Node in the stack. When you attempt to peek an empty stack an exception will be raised.
- IsEmpty - returns true when stack is empty otherwise returns false.

What is a Queue
Common terminology for a queue is

- Enqueue - Nodes or items that are added to the queue.
- Dequeue - Nodes or items that are removed from the queue. If called when the queue is empty an exception will be raised.
- Front - This is the front/first Node of the queue.
- Rear - This is the rear/last Node of the queue.
- Peek - When you peek you will view the value of the front Node in the queue. If called when the queue is empty an exception will be raised.
- IsEmpty - returns true when queue is empty otherwise returns false.
## Challenge
Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue

## Approach & Efficiency
### Created a Stack class that has a top property. It creates an empty Stack when instantiated. With push, pop, peek & is_empty methods.
**bigO(1)** 
### Create a Queue class that has a front property. It creates an empty Queue when instantiated. With enqueue, dequeue, peek & is_empty methods.
**bigO(1)**
## API
### stack
- push
Arguments: value
adds a new node with that value to the top of the stack with an O(1) Time performance.
- pop
Arguments: none
Returns: the value from node from the top of the stack
Removes the node from the top of the stack
Should raise exception when called on empty stack
- peek
Arguments: none
Returns: Value of the node located at the top of the stack
Should raise exception when called on empty stack
- is empty
Arguments: none
Returns: Boolean indicating whether or not the stack is empty.


### queue
- enqueue
Arguments: value
adds a new node with that value to the back of the queue with an O(1) Time performance.
- dequeue
Arguments: none
Returns: the value from node from the front of the queue
Removes the node from the front of the queue
Should raise exception when called on empty queue
- peek
Arguments: none
Returns: Value of the node located at the front of the queue
Should raise exception when called on empty stack
- is empty
Arguments: none
Returns: Boolean indicating whether or not the queue is empty