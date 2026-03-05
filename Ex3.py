def sum_numbers(text):
    total = 0
    num = ""
    for c in text + " ":
        if c.isdigit():
            num += c
        elif num:
            total += int(num)
            num = ""
    return total

text = "Today is January 16, 2025. The temperature is 11 degrees Celsius."
print(sum_numbers(text))