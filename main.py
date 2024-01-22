from typing import Callable

def main():
    print('what is your name?: ')
    name = input()

    print(f'hello, {name}')

    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    even_numbers = [number for number in numbers if number % 2 == 0]
    odd_numbers = [number for number in numbers if number % 2 != 0]

    print(f'even numbers: {even_numbers}')
    print(f'odd numbers: {odd_numbers}')


def filter_numbers(numbers: list[int], predicate: Callable[[int], bool]) -> list[int]:
    return [number for number in numbers if predicate(number)]

if __name__ == '__main__':
    main()
