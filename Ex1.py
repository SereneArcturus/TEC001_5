def the_valid_course_code(code):
    if len(code) not in (5, 6):
        return False
    
    letters = code[:-3]
    numbers = code[-3:]

    if not letters.isalpha() or not letters.isupper():
        return False
    if not numbers.isdigit():
        return False
    return True

print(the_valid_course_code("TEC001"))
print(the_valid_course_code("AU006"))
print(the_valid_course_code("AB12"))

a