def color_checker(color):

    if len(color) == 7 and color[0] == "#":
        for c in color[1:]:
            if c not in "0123456789abcdefABCDEF":
                return False
        return True
    
    return False


print(color_checker("#23a1f0"))
print(color_checker("#123aby"))