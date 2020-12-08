# Python 3.8.3

def check(pwd):
    same = False
    prev = '/'

    for c in str(pwd):
        if prev > c:
            return False
        if prev == c:
            same = True
        prev = c

    return same

def get_input():
    return 134564, 585159

def main():
    min, max = get_input()
    
    count = 0
    for i in range(min, max+1):
        if check(i):
            count += 1
    
    return count


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)
