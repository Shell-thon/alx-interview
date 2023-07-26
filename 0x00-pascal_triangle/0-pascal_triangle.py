#!/usr/bin/python3 
 """ 
 0-pascal_triangle 
 """


def pascal_triangle(n): 
    """ 
    Returns a list of lists of integers representing the Pascal Triangle of n 
    Returns an empty list if n <= 0 
    """ 
    if n <= 0: 
        return [] 
    triangle = [[1]] 
    for i in range(1, n): 
        temp = [1] 
        for j in range(len(triangle[i - 1]) - 1): 
            temp.append(triangle[i - 1][j] + triangle[i - 1][j + 1]) 
        temp.append(1) 
        triangle.append(temp) 
    return triangle

# Call the function and print the result
if __name__ == "__main__":
    result = pascal_triangle(5)
    for row in result:
        print("[{}]".format(",".join([str(x) for x in row])))
