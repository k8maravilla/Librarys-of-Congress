import csv

def create_books(file_name):
    '''takes a file and sorts it into different books (tuples)'''
    woo_list = []
    ttl_list = []
    alg_list = []
    with open(file_name, encoding='utf8') as file:
        reader = csv.reader(file, delimiter = '|')
        for row in reader:
            if row[2] == 'WOO':
                woo_list.append((row[0], row[1]))
            elif row[2] == 'TTL':
                ttl_list.append((row[0], row[1]))
            else:
                alg_list.append((row[0], row[1]))
        return tuple((woo_list, ttl_list, alg_list)) 

def sort_by_lines(my_book):
    '''Takes a book and sorts it in ascending order by the line number'''
    #sorted_book = tuple(sorted(my_book, key= lambda book: book[1]))
    #sorted_book = [(line, num) for line, num in sorted(my_book, key = lambda x: x[1])]
    sorted_book = dict(sorted(my_book, key= lambda x: (x[0], x[1])))
    return sorted_book
        
books = create_books('data.txt')
finished_book = sort_by_lines(books[0])
print(finished_book)

#orders = {
#	'cappuccino': 54,
#	'latte': 56,
#	'espresso': 72,
#	'americano': 48,
#	'cortado': 41
#}

#[print(key, value) for (key, value) in sorted(orders.items(), key=lambda x: x[1])]
