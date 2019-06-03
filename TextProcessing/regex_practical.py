# These are exercises from an onlines source

import re



if __name__=='__main__':
	with open('D:\Rokid\pycharm\English\mix/text.txt', 'r', encoding='utf-8') as file:
		lines = file.read()
		
	# 1. check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
	#
	def check_characters(string):
		charRe = re.compile(r'[^a-zA-z0-9.]')
		# 匹配除 "\n" 之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用象 '[.\n]' 的模式。
		# 前面的一个r表示字符串为非转义的原始字符串，让编译器忽略反斜杠，也就是忽略转义字符
		string = charRe.search(string)
		return not bool(string)


	# print(check_characters(lines))

	#
	# 2. matches a string that has an a followed by zero or more b's.
	#
	def text_match(text):
		patterns = 'ab*?'
		if re.search(patterns, text):
			return 'Found a match!'
		else:
			return ('Not matched!')


	# print(text_match(lines))


	#
	# 3. t matches a string that has an a followed by one or more b's.
	#
	def text_match(text):
		patterns = 'ab+?'
		if re.search(patterns, text):
			return 'Found a match!'
		else:
			return('Not matched!')


	# print(text_match(lines))
	# The '*', '+', and '?' qualifiers are all greedy; they match as much text as possible.
	# Sometimes this behaviour isn’t desired;
	# if the RE <.*> is matched against ' b <c>',
	# it will match the entire string, and not just ''.
	# Adding ? after the qualifier makes it perform the match in non-greedy or minimal fashion;
	# as few characters as possible will be matched. Using the RE <.*?> will match only ''.


	# 4. matches a string that has an a followed by zero or one 'b'.
	#
	def text_match(text):
		patterns = 'ab?'
		if re.search(patterns, text):
			return 'Found a match!'
		else:
			return('Not matched!')
	#
	# 5. t matches a string that has an a followed by three 'b'.
	#
	def text_match(text):
		patterns = 'ab{3}?'
		if re.search(patterns, text):
			return 'Found a match!'
		else:
			return('Not matched!')
	#
	# 6. matches a string that has an a followed by two to three 'b'.
	#
	def text_match(text):
		patterns = 'ab{2,3}?'
		if re.search(patterns, text):
			return 'Found a match!'
		else:
			return('Not matched!')
	#
	# 7. find sequences of lowercase letters joined with a underscore.
	#
	def text_match(text):
		patterns = '^[a-z]+_[a-z]+$'
		if re.search(patterns, text):
			return 'Found a match!'
		else:
			return('Not matched!')
	# print(text_match("f_fadf"))
	#
	# 8. find sequences of one upper case letter followed by lower case letters.
	#
	def text_match(text):
		patterns = '[A-Z]{1}[a-z]'
		if re.search(patterns, text):
			return 'Found a match!'
		else:
			return('Not matched!')
	# print(text_match('ADFad'))

	# 9. matches a string that has an 'a' followed by anything, ending in 'b'.
	#
	def text_match(text):
		patterns = '^a*b$'
		if re.search(patterns, text):
			return 'Found a match!'
		else:
			return('Not matched!')
	# print(text_match('ADFad'))
	#
	# 10. matches a word at the beginning of a string.
	#
	def text_match(text):
		patterns = '^\w+'
		if re.search(patterns, text):
			return 'Found a match!'
		else:
			return('Not matched!')
	# print(text_match('The quick brown fox jumps over the lazy dog.'))
	#
	# 11. matches a word at end of string, with optional punctuation.
	#
	def text_match(text):
		patterns = '\w+\S*$'
		if re.search(patterns, text):
			return 'Found a match!'
		else:
			return('Not matched!')
	print(text_match('dog.'))
	print(text_match('dog'))

	#
	# # 12. matches a word containing 'z'.
	def text_match(text):
		patterns = '\w*z.\w*'
		if re.search(patterns, text):
			return 'Found a match!'
		else:
			return('Not matched!')
	# #
	# 13. t matches a word containing 'z', not start or end of the word.
	#
	#
	# 14. match a string that contains only upper and lowercase letters, numbers, and underscores.
	#
	#
	# 15. re a string will start with a specific number.
	#
	#
	# 16. remove leading zeros from an IP address.
	#
	#
	# 17. check for a number at the end of a string.
	#
	#
	# 18. search the numbers (0-9) of length between 1 to 3 in a given string.
	#
	# "Exercises number 1, 12, 13, and 345 are important"
	#
	#
	# 19. search some literals strings in a string.
	# Sample text : 'The quick brown fox jumps over the lazy dog.'
	# Searched words : 'fox', 'dog', 'horse'
	#
	#
	# 20. search a literals string in a string and also find the location within the original string where the pattern occurs.
	#
	# Sample text : 'The quick brown fox jumps over the lazy dog.'
	# Searched words : 'fox'
	#
	#
	# 21. find the substrings within a string.
	#
	# Sample text :
	#
	# 'Python exercises, PHP exercises, C# exercises'
	#
	# Pattern :
	#
	# 'exercises'
	#
	# Note: There are two instances of exercises in the input string.
	#
	#
	# 22. find the occurrence and position of the substrings within a string.
	#
	#
	# 23. replace whitespaces with an underscore and vice versa.
	#
	#
	# 24. extract year, month and date from a an url.
	#
	#
	# 25. convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
	#
	#
	# 26. match if two words from a list of words starting with letter 'P'.
	#
	#
	# 27. separate and print the numbers of a given string.
	#
	#
	# 28. find all words starting with 'a' or 'e' in a given string.
	#
	#
	# 29. separate and print the numbers and their position of a given string.
	#
	#
	# 30. abbreviate 'Road' as 'Rd.' in a given string.
	#
	#
	# 31. replace all occurrences of space, comma, or dot with a colon.
	#
	#
	# 32. replace maximum 2 occurrences of space, comma, or dot with a colon.
	#
	#
	# 33. find all five characters long word in a string.
	#
	#
	# 34. find all three, four, five characters long words in a string.
	#
	#
	# 35. find all words which are at least 4 characters long in a string.
	#
	#
	# 36. convert camel case string to snake case string.
	#
	#
	# 37. convert snake case string to camel case string.
	#
	#
	# 38. extract values between quotation marks of a string.
	#
	#
	# 39. remove multiple spaces in a string.
	#
	#
	# 40. remove all whitespaces from a string.
	#
	#
	# 41. remove everything except alphanumeric characters from a string.
	#
	#
	# 42. find urls in a string.
	#
	#
	# 43. split a string at uppercase letters.
	#
	#
	# 44. do a case-insensitive string replacement.
	#
	#
	# 45. remove the ANSI escape sequences from a string.
	#
	#
	# 46. find all adverbs and their positions in a given sentence.
	#
	# Sample text : "Clearly, he has no excuse for such behavior."
	#
	#
	# 47. split a string with multiple delimiters.
	#
	# Note : A delimiter is a sequence of one or more characters used to specify the boundary between separate, independent regions in plain text or other data streams. An example of a delimiter is the comma character, which acts as a field delimiter in a sequence of comma-separated values.
	#
	#
	# 48. check a decimal with a precision of 2.
	#
	#
	# 49. remove words from a string of length between 1 and a given number.
	#
	#
	# 50. remove the parenthesis area in a string.
	# Sample data : ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
	# Expected Output:
	# example
	# w3resource
	# github
	# stackoverflow
	#
	# 51. insert spaces between words starting with capital letters.
