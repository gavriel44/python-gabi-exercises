from collections import Counter


def is_permutation_of_palindrome(phrase: str):
    frequency_table = create_frequency_table(phrase)
    return check_max_one_odd(frequency_table)


def create_frequency_table(phrase: str) -> Counter:
    return Counter(phrase)


def check_max_one_odd(table: Counter) -> bool:
    found_odd = False
    for key, value in table.items():
        if value % 2 != 0:
            if found_odd:
                return False
            found_odd = True
    return True


if __name__ == '__main__':
    x = 5
    print(is_permutation_of_palindrome("abccbaaaai"))
    print("blabla")

