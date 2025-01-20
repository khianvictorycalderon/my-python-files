import re

Dictionary = {
    "hello": "kamusta",
    "goodbye": "paalam",
    "cat": "pusa",
    "dog": "aso",
    "food": "pagkain",
    "there": "diyan",
    "hi": "kamusta ka",
    "you":"ka",
    "what":"ano",
    "who":"sino",
    "which":"alin",
    "how": "paano",
    "why":"bakit",
    "where":"saan",
    "the":"ang",
    "is":"ang",
    # "":"", 
}

NonReturnables = {
    "are",
    "is",
    "am",
    "was",
    "were",
    "have",
    "has",
    "had",
    "will",
    "would",
    "shall",
    "should",
    "can",
    "could",
    "might",
    "may",
    "does",
    "do"
}

# Translates from English to Tagalog
def Translate(word):
    # Remove question mark, and other unnecessary characters
    AlphaNumericWord = re.sub(r'[^a-zA-Z0-9\s]', '', word).lower()
    if AlphaNumericWord in Dictionary:
        return Dictionary[AlphaNumericWord]
    elif AlphaNumericWord in NonReturnables:
        return None  # Skip non-returnable words
    else:
        return AlphaNumericWord  # Return the original word if no translation is found

print("-----------------------------------")
UI = input("Enter an English word or phrase to translate to Tagalog: \n")

# Translating word by word
words = UI.split()
word_by_word = []
for word in words:
    translated_word = Translate(word)
    if translated_word:  # Only add to the result if it's not None
        word_by_word.append(translated_word)

translated = " ".join(word_by_word)
print(translated)
