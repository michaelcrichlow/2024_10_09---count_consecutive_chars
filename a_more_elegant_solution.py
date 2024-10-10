# def count_consecutive_chars(s: str) -> str:
#     # guard clause
#     if len(s) == 1:
#         return s + "1"

#     res = ""
#     num_of_repeated_values = 1
#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             num_of_repeated_values += 1
#             if i == len(s) - 1:
#                 res += s[i - 1] + str(num_of_repeated_values)
#                 break
#         elif s[i] != s[i - 1]:
#             res += s[i - 1] + str(num_of_repeated_values)
#             num_of_repeated_values = 1
#             if i == len(s) - 1:
#                 res += s[i] + str(num_of_repeated_values)
#                 break
#     return res


# Javascript (This works, but I'm not sure why...)
# Converted to Python, it doesn't work. Maybe I'm
# missing something.

# const countConsecutiveChars = (str) => {
#     let result = '';
#     let count = 1;

#     for (let i = 0; i < str.length; i++) {
#         if (str[i] === str[i + 1]) {
#             count++;
#         } else {
#             result += str[i] + count;
#             count = 1;
#         }
#     }

#     return result;
# }

# console.log(countConsecutiveChars('aaabbcc'));

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


# This one is a lot more elegant than the one I made.
def count_consecutive_chars(s: str) -> str:
    result = ""
    count = 1

    for i in range(0, len(s)):
        if s[i] == s[i + 1]:
            count += 1
        else:
            result += s[i] + str(count)
            count = 1

    print(result)
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
