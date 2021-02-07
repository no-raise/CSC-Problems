def numberToWords(num: int) -> str:

    lookup = {
        0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
        11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen",
        20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"
    }

    place_value = {
        2: "Hundred", 3: "Thousand", 6: "Million", 9: "Billion", 12: "Trillion"
    }

    place = 0
    temp = False
    result = []

    # edge case
    if num == 0:
        return lookup[0]

    while num > 0:
        digit = num % 10

        if place % 3 == 0:
            if digit != 0:
                if place in place_value:
                    result.append(place_value[place])
                result.append(lookup[digit])
            else:
                if place in place_value:
                    result.append(place_value[place])

        if place % 3 == 2:
            if digit != 0:
                result.append(place_value[2])
                result.append(lookup[digit])
            else:
                if prev_digit == 0 and place > 2:
                    result.append(place_value[2])

        if place % 3 == 1:

            if place - 1 in place_value:
                result.append(place_value[place-1])

            if result:
                temp = result.pop()
                if temp in place_value.values():
                    result.pop()

            tens = int(str(digit) + str(prev_digit))

            if tens != 0:
                if tens in lookup:
                    result.append(lookup[tens])

                else:
                    if prev_digit != 0:
                        result.append(lookup[prev_digit])

                    result.append(lookup[digit*10])
            else:
                if temp:
                    result.append(temp)

        prev_digit = digit
        num = num // 10
        place += 1

    return " ".join(result[::-1])


print(numberToWords(10000))

# place += 1
# 1 % 3
# 2 % 3
# 3 % 3
# 4 % 3
# 5 % 3
# 6 % 3
# 7 % 3

# num:              1 0 0 0 0 1

# place_value:      5 4 3 2 1 0

# modulo:           2 1 0 2 1 0
