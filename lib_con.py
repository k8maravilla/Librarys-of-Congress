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
        return dict(woo_list), dict(ttl_list), dict(alg_list)

def sort_by_lines(my_book):
    '''Takes a book and sorts it in ascending order by the line number'''
    my_dictionary = dict(my_book)
    my_values = list(my_dictionary.values())
    sorted_val = sorted(my_values)
    #sorted_book = [(line, num) for line, num in sorted(my_book, key = lambda x: x[1])]
    #sorted_book = dict(sorted(my_book, key= lambda x: (x[0], x[1])))
    return sorted_val
        
books = create_books('data.txt')
finished_book = sort_by_lines(books[0])
print(finished_book)

