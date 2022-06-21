import nltk
import string
import re
import inflect

inflector = inflect.engine()

def convert_number_to_word(text):
	str_temp = text.split()
	str_new = []



	for word in str_temp:
		
		if word.isdigit():
			temp = inflector.number_to_words(word)
			str_new.append(temp)
		else:
			str_new.append(word)

		str_temp = ''.join(str_new)
		return str_temp

input_number_to_word = input("enter a sentence: ")
print(convert_number_to_word(input_number_to_word))