import csv

def create_books(file_name):
    '''takes a file and sorts it into different books (tuples)'''
    woo_list = []
    ttl_list = []
    alg_list = []
    with open(file_name, encoding='utf8') as file:
        reader = csv.reader(file, delimiter = '|')
        print(reader)
        for row in reader:
            if row[2] == 'WOO':
                woo_list.append((row[0], row[1]))
            elif row[2] == 'TTL':
                ttl_list.append((row[0], row[1]))
            else:
                alg_list.append((row[0], row[1]))
        return tuple(woo_list) + tuple(ttl_list) + tuple(alg_list)
            

            #print(row[0], row[1], row[2])
        
books = create_books('data.txt')

