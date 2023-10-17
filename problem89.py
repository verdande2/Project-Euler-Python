import time
from icecream import ic
# from https://bas.codes/posts/python-roman-numerals
def from_roman_numeral(numeral):
    value_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    value = 0
    last_digit_value = 0

    for roman_digit in numeral[::-1]:  # 1
        digit_value = value_map[roman_digit]

        if digit_value >= last_digit_value:  # 2
            value += digit_value
            last_digit_value = digit_value
        else:  # 3
            value -= digit_value

    return value
def to_roman_numeral(value):
    roman_map = {
        1: "I", 4: "IV", 5: "V", 9: "IX",
        10: "X", 40: "XL", 50: "L", 90: "XC",
        100: "C", 400: "CD", 500: "D",
        900: "CM", 1000: "M",
    }
    result = ""
    remainder = value

    for i in sorted(roman_map.keys(), reverse=True):# 2
        if remainder > 0:
            multiplier = i
            roman_digit = roman_map[i]

            times = remainder // multiplier         # 3
            remainder = remainder % multiplier      # 4
            result += roman_digit * times           # 4

    return result



start = time.time()

orig_total_len = 0
new_total_len = 0
#open the file of numbers
with open("problem89_files/0089_roman.txt") as file:
#foreach number, record the original length, then convert it to number then back to numeral and get length
    for line in file:
        original_roman = line.strip()
        new_roman = to_roman_numeral(from_roman_numeral(original_roman))

        orig_len = len(original_roman)
        orig_total_len += orig_len

        new_len = len(new_roman)
        new_total_len += new_len
        ic(original_roman,new_roman,orig_len,new_len)

#accumulate lengths

end = time.time()
print("found in",str(end-start),"Answer is", str(orig_total_len-new_total_len))
