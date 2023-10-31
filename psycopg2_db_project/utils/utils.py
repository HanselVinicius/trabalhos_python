def has_digits(text):
    for char in text:
        if char.isdigit():
            return True
    return False