def word_counter():
    text = input("Enter your text: ")
    words = text.split()
    sentences = text.count('.') + text.count('!') + text.count('?')
    print(f"Words: {len(words)}")
    print(f"Characters: {len(text)}")
    print(f"Sentences: {sentences}")

word_counter()