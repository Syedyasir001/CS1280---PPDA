def word_count(sentence):
    words = sentence.split()
    total_words = len(words)
    frequency = {}

    for word in words:
        word = word.lower().strip(".,!?")
        frequency[word] = frequency.get(word, 0) + 1

    return total_words, frequency

sentence = input("Enter a sentence: ")
total_words, frequency_dict = word_count(sentence)

print(f"\nTotal word count: {total_words}")
print("Word frequencies:")
for word, count in frequency_dict.items():
    print(f"{word}: {count}")
