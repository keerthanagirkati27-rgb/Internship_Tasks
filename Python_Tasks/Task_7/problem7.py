

def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    lines = []

    for i in range(size):
        left = alpha[size-1:size-i-1:-1]
        middle = alpha[size-i-1:size]
        right = alpha[size-i:size+i]
        row = "-".join(left + middle + right)
        lines.append(row)

    width = 4 * size - 3
    for row in lines:
        print(row.center(width, "-"))

    for row in lines[-2::-1]:
        print(row.center(width, "-"))
