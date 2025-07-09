def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase

    width = 4 * size - 3
    lines = []

    for i in range(size):
        # letters from size-1 down to size-1-i (descending)
        left_part = alpha[size-1:size-1-i:-1]
        # middle letter at position size-1-i
        middle = alpha[size-1-i]
        # letters from size-i up to size-1 (ascending)
        right_part = alpha[size-i:size]
        
        # combine parts for the row pattern
        row = '-'.join(left_part + middle + right_part)
        # center with dashes
        lines.append(row.center(width, '-'))
    
    # print top half (excluding middle line) + middle + bottom half (excluding middle line)
    # top half is lines[0] to lines[size-2], bottom half is reverse of that
    print('\n'.join(lines[:-1] + lines[::-1]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
