def get_string_of_numbers(number: str) -> str:
    if not number.isdigit():
        raise TypeError('Введите целое число')
    number = int(number)
    final_string = ''
    for i in range(number + 1):
        final_string += str(i) * i
    return final_string


if __name__ == '__main__':
    print(get_string_of_numbers(input()))
