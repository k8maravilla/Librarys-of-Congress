import sys
import csv

teacher_file = sys.argv[0]

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

def max_length(my_list):
    '''returns the max length of a sentence'''
    maximum_count = 0
    max_linenum = 0
    maximum_sentence = ''

    for row in my_list:
        sentence_length = len(row[0])

        if maximum_count == 0:
            maximum_count = sentence_length
            maximum_sentence = row[0]
            max_linenum = row[1]

        elif maximum_count == sentence_length:
            if max_linenum < row[1]:
                max_linenum = row[1]
                maximum_sentence = row[0]
                maximum_count = sentence_length

        elif sentence_length > maximum_count:
            maximum_count = sentence_length
            maximum_sentence = row[0],row[1]
            max_linenum = row[1]

    return maximum_sentence

def min_length(my_list):
    '''returns the minimum length of a list'''
    minimum_count = 0
    minimum_sentence = ''
    min_linenum = 0
    for row in my_list:
        sentence_length = len(row[0])

        if minimum_count == 0:
            minimum_count = sentence_length
            minimum_sentence = row[0], row[1]
            min_linenum =row[1]
        
        elif minimum_count == sentence_length:
            if min_linenum > row[1]:
                min_linenum =row[1]
                minimum_count = sentence_length
                minimum_sentence = row[0], row[1]
        
        elif sentence_length < minimum_count:
            minimum_count = sentence_length
            minimum_sentence = row[0], row[1]
            min_linenum =row[1]

    return minimum_sentence

def avg_length(my_list):
    '''returns the average of the length of a list'''
    avg_count = []
    for row in my_list:
        total_count = len(row[0])
        avg_count.append(total_count)
    total_avg = int(sum(avg_count) / len(avg_count))
    return total_avg

def write_summary_to_file(summary, book_name):
    '''writes the novel summary to a file'''
    with open('summary_novel.txt', 'a+', encoding = 'utf8') as f:
        f.write('{}\n'.format(book_name))
        f.write('Longest line ({}) : {}\n'.format(summary[1][1], summary[1][0]))
        f.write('Shortest line ({}): {}\n'.format(summary[0][1], summary[0][0]))
        f.write('Average length : {}\n\n'.format(summary[2]))

def write_novel(sorted_lin, book_name):
    '''writes the lines to a file with the whole book sorted'''
    with open('Novel_text.txt', 'a+', encoding = 'utf8') as file:
        file.write('{}\n'.format(book_name))
        for line in sorted_lin:
            file.write('{}\n'.format(line))
        file.write('-----\n')

def main():
    '''executes all code'''
    #ttl output
    ttl_book = read_books('book_data.txt', 'TTL')

    ttl_sorted = sort_by_lines(ttl_book)

    ttl_answer = min_max_avg_length(ttl_sorted)

    write_summary_to_file(ttl_answer, 'TTL')

    write_novel(ttl_sorted, 'TTL')

    #woo output
    woo_book = read_books('book_data.txt', 'WOO')

    woo_sorted = sort_by_lines(woo_book)

    woo_answer = min_max_avg_length(woo_sorted)

    write_summary_to_file(woo_answer, 'WOO')

    write_novel(woo_sorted, 'WOO')

    #alg output
    alg_book = read_books('book_data.txt', 'ALG')

    alg_sorted = sort_by_lines(alg_book)

    alg_answer = min_max_avg_length(alg_sorted)

    write_summary_to_file(alg_answer, "ALG")

    write_novel(alg_sorted, 'ALG')

#woo_book = read_books('book_data.txt', 'WOO')
#woo_sorted = sort_by_lines(woo_book)
#max_answer = max_length(woo_sorted)
#min_answer = min_length(woo_sorted)
#avg_answer = avg_length(woo_sorted)
#print(max_answer)
#print(min_answer)
#print(avg_answer)

my_list = [('hello worlddsafdas', int('10')), ('hello wiplddsafdas', int('9')), ('goodbye', int('7')), ('Idunnow', int('5'))]

answer = min_length(my_list)
print(answer)

