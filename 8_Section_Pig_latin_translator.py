# 53. and 54. lesson - Pig Latin Translator
# get sentence from the user
original = input("Enter a sentence of your choice and pig will translate it: ").lower().strip()

# split sentence into words
words = original.split()
# Output: ['hello', 'world']

# loop through words and convert to pig latin
new_words = []
# "for" loop going through all the words in this list
# Output: each word on a new line when "for word in words"
for word in words:
    if word[0] in "aeiou":
# if the  first letter is vowel
        new_word = word + "yay"
# add to a new word "yay" and put it to the list of words
        new_words.append(new_word)
    else:
# loop through each word and find vowel
        vowel_pos = 0
        for letter in word:
# stop looping through once we know where our consonants end
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
# up to vowel
# if it is a value - where the first value is
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)
# continue - next iteration
# also assuming the vowel is coming next
# keeping track of the vowel index

# stick words together & print it out
output = " ".join(new_words)
print(output)
# for eat - ['eatyay']


# for words in original:
#     print(words)
# Output: each letter on a new line

# list_letters = [words for words in original]
# print(list_letters)
# Output: each letter as an element of the list

# starts with vowel, just add "yay"
# otherwise, move the first consonant cluster to end, and add "ay"

# stick words back together

# output the final string

# 55. lesson - overview
# while loops while a condition is True
# baby simulator
# for loops update a variable as they loop over an iterable
# list comprehensions
# pig latin translator