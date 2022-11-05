my_list = ["Text: this is a collection of words of nice words this is a fun thing it is"]
print(my_list)

unique_words = {}
word_to_count = {}
text = input(" ")

# text = "this is a collection of words of nice words this is a fun thing it is"
words = text.split()

for word in words:
    frequency = unique_words.get(word, 0)
    unique_words[word] = frequency + 1
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1

words = list(unique_words.keys())
words = list(word_to_count.keys())
words.sort()


max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, unique_words[word]))
    print("{:{}} : {}".format(word, max_length, word_to_count[word]))
