def count_consecutive_chars(s: str) -> str:
    # guard clause
    if len(s) == 1:
        return s + "1"

    res = ""
    num_of_repeated_values = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            num_of_repeated_values += 1
            if i == len(s) - 1:
                res += s[i - 1] + str(num_of_repeated_values)
                break
        elif s[i] != s[i - 1]:
            res += s[i - 1] + str(num_of_repeated_values)
            num_of_repeated_values = 1
            if i == len(s) - 1:
                res += s[i] + str(num_of_repeated_values)
                break
    return res


def main() -> None:
    print(count_consecutive_chars('a'))
    print(count_consecutive_chars('aa'))
    print(count_consecutive_chars('ab'))
    print(count_consecutive_chars('abb'))
    print(count_consecutive_chars('abba'))
    print(count_consecutive_chars('abc'))
    print(count_consecutive_chars('aabbcc'))
    print(count_consecutive_chars('aaaabbbccd'))
    # OUTPUT: 
    # a1
    # a2
    # a1b1
    # a1b2
    # a1b2a1
    # a1b1c1
    # a2b2c2
    # a4b3c2d1


if __name__ == '__main__':
    main()
