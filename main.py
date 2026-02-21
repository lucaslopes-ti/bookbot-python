from stats import get_num_words, get_num_characters, sort_characters
import sys

def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	text = get_book_text(sys.argv[1])
	num_words = get_num_words(text)
	print(f"Found {num_words} total words")

	char_counts = get_num_characters(text)
	sorted_chars = sort_characters(char_counts)
	
	for item in sorted_chars:
		if not item["char"].isalpha():
			continue
		print(f"{item['char']}: {item['num']}")

main()
