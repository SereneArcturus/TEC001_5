def hide_phone(text):
    words = text.split()
    
    for i in range(len(words)):
        w = words[i].strip(",.")
        
        if w.isdigit() and len(w) == 10:
            words[i] = "[REDACTED]"
        
        elif w.startswith("+84") and w[3:].isdigit():
            words[i] = "[REDACTED]"
    
    return " ".join(words)


text = "Call +842439999999 or 0987654321,"
print(hide_phone(text))