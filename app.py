def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

if __name__ == "__main__":
    test_strings = ["Racecar", "hello", "A man, a plan, a canal: Panama", "Python"]
    for s in test_strings:
        print(f'"{s}" is a palindrome? {is_palindrome(s)}')
