

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    l = student_marks.get(input(), [])
    print(0.00) if l == [] else print("%.2f" % (sum(l) / len(l)))
