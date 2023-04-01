import sys
import csv

teacher_file = sys.argv[0]

def get_titles(file_name):
    '''takes a file and sorts it into different books (tuples)'''
    book_titles = []

    with open(file_name, encoding='utf8') as file:
        reader = csv.reader(file, delimiter = '|')
        for row in reader:
            book_titles.append(row[2])

    sorted_books = sorted(book_titles)
    my_titles = set(sorted_books)
    return my_titles

def read_books(file_name, title_name):
    '''takes a file and sorts it into different books (tuples)'''
    title_contents = []
    with open(file_name, encoding='utf8') as file:
        reader = csv.reader(file, delimiter = '|')
        for row in reader:
            if row[2] == title_name:
                title_contents.append((row[0], int(row[1])))

    sorted_book = [(line, num) for line, num in sorted(title_contents, key = lambda x: x[1])]
            
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

    #return (maximum_sentence)
    return (maximum_sentence, max_linenum)

def min_length(my_list):
    '''returns the minimum length of a list'''
    minimum_count = 0
    minimum_sentence = ''
    min_linenum = 0
    for row in my_list:
        sentence_length = len(row[0])

        if minimum_count == 0:
            minimum_count = sentence_length
            minimum_sentence = row[0]
            min_linenum =row[1]
        
        elif minimum_count == sentence_length:
            if min_linenum > row[1]:
                min_linenum =row[1]
                minimum_count = sentence_length
                minimum_sentence = row[0]
        
        elif sentence_length < minimum_count:
            minimum_count = sentence_length
            minimum_sentence = row[0]
            min_linenum =row[1]

    return (minimum_sentence, min_linenum)

def avg_length(my_list):
    '''returns the average of the length of a list'''
    avg_count = []
    for row in my_list:
        total_count = len(row[0])
        avg_count.append(total_count)
    total_avg = int(sum(avg_count) / len(avg_count))
    return total_avg

def write_summary_to_file(max, min, avg, title):
    '''writes the novel summary to a file'''
    with open('summary_novel.txt', 'a+', encoding = 'utf8') as file:
        file.write('{}\n'.format(title))
        file.write('Longest line ({}) : {}\n'.format(max[1], max[0]))
        file.write('Shortest line ({}): {}\n'.format(min[1], min[0]))
        file.write('Average length : {}\n\n'.format(avg))

def write_novel(list, title):
    '''writes the lines to a file with the whole book sorted'''
    with open('Novel_text.txt', 'a+', encoding = 'utf8') as file:
        file.write('{}\n'.format(title))
        for line in list:
            file.write('{}\n'.format(line[0]))
        file.write('-----\n')

def main():
   
    title_names = get_titles(sys.argv[1])

    for title in title_names:

        total_title = read_books(sys.argv[1], title)

        max = max_length(total_title)

        min = min_length(total_title)

        average = avg_length(total_title)

        summary = write_summary_to_file(max, min, average, title)

        novel = write_novel(total_title, title)
 
main()
