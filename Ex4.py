def hide_phone(text):
    words = text.split()
  
    for i in range(len(words)):
        word = words[i].strip(",.")
        if word.isdigit() and len(word) == 10:
            words[i] = "[REDACTED]"
        elif word.startswith("+84") and word[3:].isdigit():
            words[i] = "[REDACTED]" 
    return " ".join(words)

text = "You may reach Mr. Atkinson through his office number: +842439999999 during work hours, or his cell phone number: 0987654321,"
print(hide_phone(text))

a