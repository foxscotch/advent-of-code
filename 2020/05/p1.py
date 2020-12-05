# Python 3.8.3

def select_side(bounds, left):
    min, max = bounds
    if left:
        return bounds[0], (max - min + 1) // 2 + min - 1
    else:
        return max - (max - min + 1) // 2 + 1, bounds[1]

def get_input():
    with open('input.txt', 'r') as f:
        return f.read().split()

def main():
    puzzle = get_input()

    results = []
    
    for seat in puzzle:
        row_string = seat[:7]
        col_string = seat[7:]

        row_bounds = (1, 128)
        col_bounds = (1, 8)

        for side in row_string:
            row_bounds = select_side(row_bounds, side == 'F')
        for side in col_string:
            col_bounds = select_side(col_bounds, side == 'L')
    
        results.append((row_bounds[0] - 1) * 8 + (col_bounds[0] - 1))
    
    print(max(results))

if __name__ == '__main__':
    import time

    start = time.perf_counter()
    main()
    print(time.perf_counter() - start)
