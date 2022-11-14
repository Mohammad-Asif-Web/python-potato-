
def fundMinNum(numbers):
    min = numbers[0]
    for num in numbers:
        if num < min:
            min = num
    return min

digit = [20, 2, 49,18, 93, 52, 30, 82, 96]
# fundMinNum(digit)
