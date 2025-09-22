def count_words(book):
	book_split = book.split()
	count = 0
	for word in book_split:
		count += 1
	return count

def sort_on(items):
    return items["num"]

def count_symbols(book):
	book = book.lower()
	symbols = dict()
	for symbol in book:
		if symbol in symbols:
			symbols[symbol] += 1
		else:
			symbols[symbol] = 1
	return symbols

def sort_dict(old_dict):
	new_list = list()
	for key in old_dict:
		new_dict = dict()
		new_dict["char"] = key
		new_dict["num"] = old_dict[key]
		new_list.append(new_dict)
	new_list.sort(reverse=True, key=sort_on) 
	return new_list