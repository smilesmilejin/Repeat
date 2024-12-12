# Repeat 

## Problem Statement

Your goal is to find the first character repeated less than a given number of times in a data structure.

The data structure will be a ragged matrix, represented by a tuple of tuples of strings. Each string will be a single character, but each inner tuple may have a different length. For example:

```python
matrix_1 = (
    ('u','e','r','e', ' ', 'e'),
    ('d', 'z', 'o', 'b', 'i', 'v'),
    ('n',),
    ('w', 'g', 'q', ' ', '5', 'g', 'w'),
    ('r',),
    ('y', 'e'),
    ('u', 'a', 'u', 't')
)
```

Your function will receive a `matrix` and an integer, `n` where `n > 1`. Our goal is to find the first character when iterating row-wise that shows up in the matrix strictly fewer than n times.

For example, take `matrix_1` and `n = 3`. We see that, 'u' is repeated 3 times and 'e' is repeated 4 times. However, 'r' appears only 2 times. 'r' is thus the first character when iterating row-wise to appear fewer than n times. The function should return 'r' in this case.

See the tests in the [`main.py`](main.py) file for more examples.