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


main()



