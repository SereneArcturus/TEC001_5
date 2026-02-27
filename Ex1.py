def check_course(code):
    if len(code) < 5 or len(code) > 6:
        return False
    
    letters = code[:-3]
    numbers = code[-3:]
    
    if letters.isupper() and letters.isalpha() and numbers.isdigit():
        return True
    else:
        return False


print(check_course("TEC001"))
print(check_course("AU006"))
print(check_course("A1001"))