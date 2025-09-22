from stats import *
import sys

def get_book_text(filepath):
	with open(filepath, "r") as f:
		book = f.read()
	return book



def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book = get_book_text(sys.argv[1])
	words = count_words(book)
	symbole = count_symbols(book)
	sorted_l = sort_dict(symbole)
	print(f"Found {words} total words")
	for liste in sorted_l:
		if liste["char"].isalpha():
			print(f"{liste["char"]}: {liste["num"]}")

main()