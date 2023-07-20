

# Complete the solve function below.
def solve(s):
    for item in s.split():
        if item.isalpha():
            s = s.replace(item,item.title())
    return s

