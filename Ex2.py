def check_hex(color):
    if len(color) != 7:
        return False
    if color[0] != "#":
        return False
    
    allowed = "0123456789abcdefABCDEF"
    
    for c in color[1:]:
        if c not in allowed:
            return False
    
    return True


print(check_hex("#FFA500"))
print(check_hex("#123abz"))