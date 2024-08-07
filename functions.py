# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a, b, c):
    return max(a, b, c)


print(max_num(3, 7, 5))  

# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


print(mult_list([1, 2, 3, 4]))  

# Write a Python function called rev_string() to reverse a string.
def rev_string(s):
    return s[::-1]


print(rev_string("hello"))  

# Write a Python function called num_within() to check whether a number falls in a given range.

def num_within(num, start, end):
    return start <= num <= end

# Example usage:
print(num_within(5, 1, 10))  # Output: True
print(num_within(15, 1, 10)) # Output: False

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.


def pascal(n):
    if n <= 0:
        return
    
    # Initialize the triangle with the first row
    triangle = [[1]]
    
    # Generate each row of the triangle
    for i in range(1, n):
        row = [1]  # Start each row with a 1
        for j in range(1, i):
            # Each value is the sum of the two values above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # End each row with a 1
        triangle.append(row)
    
    # Print the triangle
    for row in triangle:
        print(' '.join(map(str, row)))

# Example usage:
pascal(1)
# Output:
# 1

pascal(5)
# Output:
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
