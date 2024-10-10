# This one is a lot more elegant than the one I made.
def countConsecutiveChars(s):
    result = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += s[i - 1] + str(count)
            count = 1

    result += s[-1] + str(count)

    return result


def main() -> None:
    assert countConsecutiveChars('a') == "a1"
    assert countConsecutiveChars('aa') == "a2"
    assert countConsecutiveChars('ab') == "a1b1"
    assert countConsecutiveChars('abb') == "a1b2"
    assert countConsecutiveChars('abba') == "a1b2a1"
    assert countConsecutiveChars('abc') == "a1b1c1"
    assert countConsecutiveChars('aabbcc') == "a2b2c2"
    assert countConsecutiveChars('aaabbcc') == "a3b2c2"
    assert countConsecutiveChars('aaaabbbccd') == "a4b3c2d1"
    print("Everthing passed!")


if __name__ == '__main__':
    main()
