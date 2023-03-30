import csv

def read_books(file_name, book_name):
    '''takes a file and sorts it into different books (tuples)'''
    book_list = []
    
    with open(file_name, encoding='utf8') as file:
        reader = csv.reader(file, delimiter = '|')
        for row in reader:
            if row[2] == book_name:
                book_list.append((row[0], int(row[1])))
            
        return book_list

def sort_by_lines(my_book):
    '''Takes a book and sorts it in ascending order by the line number'''
    sorted_book = [(line, num) for line, num in sorted(my_book, key = lambda x: x[1])]
    return sorted_book

def minimum_length(my_list):
    '''this function looks at the lines of the book and tells which line is the shortest'''
    minimum_count = 0
    minimum_sentence = ''
    avg_count = []
    for row in my_list:
        min_count = len(row[0])
        avg_count.append(min_count)
        if minimum_count == 0:
            minimum_count = min_count
            minimum_sentence = row[0]
        elif min_count < minimum_count:
            minimum_count = min_count
            minimum_sentence = row[0]
    total_avg = int(sum(avg_count) / len(avg_count))
    return minimum_count, minimum_sentence, total_avg

def maximum_length(my_list):
    '''takes a list and returns the biggest line in the list'''
    maximum_count = 0
    maximum_sentence = ''
    for row in my_list:
        max_count = len(row[0])
        if maximum_count == 0:
            maximum_count = max_count
            maximum_sentence = row[0]
        elif max_count > maximum_count:
            maximum_count = max_count
            maximum_sentence = row[0]
    return maximum_count, maximum_sentence

ttl_book = read_books('data.txt', 'TTL')
woo_book = read_books('data.txt', 'WOO')
alg_book = read_books('data.txt', 'ALG')

answer = sort_by_lines(woo_book)
short_answer = minimum_length(answer)
long_answer = maximum_length(answer)
print(short_answer)
print(long_answer)
