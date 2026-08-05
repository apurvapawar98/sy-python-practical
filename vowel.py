text = input("enter a paragraph:")
character = len(text)
spaces = text.count(" ")
words = len(text.split())
vowels = "aeiouAEIOU"
vowel_count = 0 

for i in text:
    if i in vowels:
        vowel_count += 1

print("\n ****text analysis****")
print("total character:",character)
print("total vowel:",vowel_count)
print("total spaces",spaces)
print("total word:",words)

if len(text) > 0:
    print(" first character(Indexing):",text[0])
    print("last character(indexing):",text[-1])

print("first character(slicing): ",text[:10])
print("last character (slicing):",text[-10:])
