#!/usr/bin/python3
def roman_to_int(roman_string):
    if not (isinstance(roman_string, str)):
        return 0
    elif roman_string is None:
        return 0
    else:
        upper = ""
        for cha in roman_string:
            if ord('a') <= ord(cha) <= ord('z'):
                upper += chr(ord(cha) - (ord('a') - ord('A')))
            else:
                upper += cha
        upper_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                       'C': 100, 'D': 500, 'M': 1000}
        if (set(upper) & set(list(upper_roman))) != set(upper):
            return 0
        sum_ = upper_roman.get(upper[-1])
        total = 0
        for i in range(-2, -(len(roman_string)) - 1, -1):
            j = i + 1
            if sum_ == 0:
                sum_ = upper_roman.get(upper[i])
                continue
            if (upper[i] == upper[j]):
                sum_ = sum_ + upper_roman.get(upper[i])
                continue
            if upper_roman.get(upper[i]) > upper_roman.get(upper[j]):
                if (digit(upper_roman.get(upper[i]))
                   > digit(upper_roman.get(upper[j]))):
                    total += sum_
                    sum_ = upper_roman.get(upper[i])
                    continue
                else:
                    sum_ = sum_ + upper_roman.get(upper[i])
                    total = total + sum_
                    sum_ = 0
                    continue
            if upper_roman.get(upper[i]) < upper_roman.get(upper[j]):
                sum_ = sum_ - upper_roman.get(upper[i])
                total = total + sum_
                sum_ = 0
                continue
        return total + sum_


def digit(num):
    if isinstance(num, int):
        if num == 0:
            return 1
        else:
            digit = 0
            while (num):
                digit += 1
                num = num // 10
            return digit
    return None
