def get_num_words(text):
        words = text.split()
        return len(words)

def get_num_characters(text):
	char_counts = {}

	for char in text.lower():
		if char in char_counts:
			char_counts[char] += 1
		else:
			char_counts[char] = 1
	return char_counts

def sort_characters(char_dict):
	chars_list = []

	for char, count in char_dict.items():
		chars_list.append({
			"char": char,
			"num": count
		})

	def sort_on(dict_item):
		return dict_item["num"]

	chars_list.sort(reverse=True, key=sort_on)

	return chars_list
