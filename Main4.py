def main4(n: int, k: int):
    if n == 1 or n == 2:
        return 1
    return main4(n - 1, k) + k * main4(n - 2, k)

if __name__ == '__main__':
    print(main4(28, 5))