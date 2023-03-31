
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

def min_max_avg_length(my_list):
    '''this function looks at the lines of the book and tells which line is the shortest'''
    minimum_count = 0
    minimum_sentence = ''
    maximum_count = 0
    maximum_sentence = ''
    avg_count = []

    for row in my_list:
        min_count = len(row[0])
        max_count = len(row[0])
        avg_count.append(min_count)
        avg_count.append(max_count)

        if minimum_count == 0:
            minimum_count = min_count
            maximum_count = max_count
            minimum_sentence = row[0], row[1]
            maximum_sentence = row[0], row[1]

        elif min_count < minimum_count:
            minimum_count = min_count
            minimum_sentence = row[0], row[1]

        elif max_count > maximum_count:
            maximum_count = max_count
            maximum_sentence = row[0],row[1]

    total_avg = int(sum(avg_count) / len(avg_count))
    return minimum_sentence, maximum_sentence, total_avg



def write_summary_to_file(file_name, file_name2, summary, novel):
    '''writes the novel summary to a file'''
    with open(file_name, 'w', encoding = 'utf8') as f, open(file_name2,'w', encoding = 'utf8') as file:
        #summary file writing
        f.write('Longest line ({}) : {}\n'.format(summary[1][1], summary[1][0]))
        f.write('Shortest line ({}): {}\n'.format(summary[0][1], summary[0][0]))
        f.write('Average length : {}'.format(summary[2]))

        #novel file writing
        file.write()


ttl_book = read_books('data.txt', 'TTL')
woo_book = read_books('data.txt', 'WOO')
alg_book = read_books('data.txt', 'ALG')

answer = sort_by_lines(woo_book)
short_answer = min_max_avg_length(answer)
write_summary_to_file('summary_novel.txt', short_answer)
