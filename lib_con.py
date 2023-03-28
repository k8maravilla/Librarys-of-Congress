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
    sorted_book = sorted(my_book, key= lambda book: book[1])
    return sorted_book
        
books = create_books('data.txt')
print(books[0][1])
#finished_book = sort_by_lines(books[0])

#student_tuples = [
 #   ('john', 'A', 15),
  #  ('jane', 'B', 12),
   # ('dave', 'B', 10),
#]
#answer = sorted(student_tuples, key=lambda student: student[2])
#print(answer)

