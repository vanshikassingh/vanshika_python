message = input("Enter message: ")

# Convert message into words
words = message.split()

# 1. Total characters (excluding spaces or including spaces — here including spaces)
total_chars = len(message)

# 2. Total words
total_words = len(words)

# 3. Longest and shortest word
longest_word = max(words, key=len)
shortest_word = min(words, key=len)

# 4. Count occurrences of "Python"
python_count = 0
for w in words:
    if w == "Python":
        python_count += 1

# 5. Words having more than 4 characters
long_words = []
for w in words:
    if len(w) > 4:
        long_words.append(w)

# 6. Words starting with vowel
vowels_set = "aeiouAEIOU"
vowel_words = []
for w in words:
    if w[0] in vowels_set:
        vowel_words.append(w)

# 7. Count vowels and consonants
vowels = 0
consonants = 0

for ch in message:
    if ch.isalpha():
        if ch in vowels_set:
            vowels += 1
        else:
            consonants += 1

# OUTPUT
print("\nMessage:", message)
print("Total Characters:", total_chars)
print("Total Words:", total_words)

print("\nLongest Word:", longest_word)
print("Shortest Word:", shortest_word)

print("\nOccurrences of Python:", python_count)

print("Words Longer Than 4 Characters:", long_words)

print("Words Starting with Vowel:", vowel_words)

print("Vowels:", vowels)
print("Consonants:", consonants)
