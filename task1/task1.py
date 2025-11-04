from typing import Callable

def caching_fibonacci() -> Callable[[], int]:
    """
    Create and return a Fibonacci function that uses an internal cache 
    to optimize repeated calculations.

    This higher-order function defines and returns a recursive Fibonacci 
    function that remembers previously computed values using a closure-based 
    cache (dictionary). This approach eliminates redundant recursive calls 
    and greatly improves performance when calculating multiple Fibonacci numbers.

    Returns:
        Callable[[], int]: A Fibonacci function that takes an integer n 
                              and returns the n-th Fibonacci number.

    Example:
        fib = caching_fibonacci()
        fib(10)  # Returns 55
        fib(15)  # Uses cached results for previous computations
    """
    # Create cache dictionary
    cache = {}

    def fibonacci(n: int) -> int:
        """
        Calculate and return the n-th Fibonacci number using recursion with caching.

        Args:
            n (int): The index of the Fibonacci sequence element to compute.
                    The sequence starts from n = 0, where:
                        F(0) = 0,
                        F(1) = 1.

        Returns:
            int: The Fibonacci number corresponding to the given index n.
        
        """      
        if n <= 0: return 0
        if n == 1: return 1

        # if value in cache - return this value
        if n in cache.keys(): return cache[n]

        # write data to cache as sum of recursive fibonacci functions
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    return fibonacci

fib = caching_fibonacci()
print(fib(4))
print(fib(10))
print(fib(40))
print(fib(100))