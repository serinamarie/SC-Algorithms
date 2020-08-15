#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This exercise has a constant runtime because the input size (n) does not affect how long the the code will take to run.


b) This exercise has a logarithmic runtime O(log n). As the size of the input increases in size, the the runtime used is growing at a slightly slower rate. 


c) This exercise has a linear runtime O(n) because as the input size increase, the space used will grow at the same rate.

## Exercise II

If we want to minimize the number of broken eggs, we want them to all be throw off a floor < f. While we don't know f, we can try different inputs for n (the number of stories). 
1. While n leads to broken_eggs = 0, we can input that n. 
2. We can set a counter such that we increase the floor (n) with each run-through. Our base case is, if a floor input (n) returns a broken egg, that floor is our f floor. 

That seems complicated, though. Or maybe I overcomplicated the problem. How about--

Goal: Find the value of f by iterating through range of n until our n > f. I would say this is a logarithmic runtime because while our n increases, we don't need to go through our full list regardless, so the runtime is increasing slowly.
