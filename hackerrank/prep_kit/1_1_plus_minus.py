"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to are acceptable.

# Example

There are elements, two positive, two negative and one zero. Their ratios are , and . Results are printed as:

```
0.400000
0.400000
0.200000
```

"""

def plus_minus(arr):
    """Calculate the ratios of its elements that are positive, negative, and zero."""
    positive_num = 0
    negative_num = 0
    zero_num = 0

    for i in arr:
        if i == 0:
            zero_num += 1
        elif i < 0:
            negative_num += 1
        else:
            positive_num += 1

    arr_len = len(arr)
    positive_ratio = positive_num/arr_len
    negative_ratio = negative_num/arr_len
    zero_ratio = zero_num/arr_len

    print(f"{positive_ratio:.6f}")
    print(f"{negative_ratio:.6f}")
    print(f"{zero_ratio:.6f}")


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plus_minus(arr)
