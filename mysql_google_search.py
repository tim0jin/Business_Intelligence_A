import Distance_Search
import my_sql_integration as my_sql_i
import sys
sys.path.append('/Users/timur01/Desktop/B_Intelligence/analytics/')
import competitor_locations as cl

locations = [
    '7600 Kennedy Rd, Markham, ON L3R 9S5',
    '3201 Bur Oak Ave, Markham, ON L6B 0T2',
    '7755 Bayview Ave., Thornhill, ON L3T 7R3',
    '501 Clark Ave. West, Thornhill, ON L4J 4E5',
    '1441 Clark Avenue West, Thornhill, ON L4J 7R4',
    '10190 Keele St., Maple, ON L6A 1R7',
    '9201 Islington Ave., Woodbridge, ON L4L 1A7',
    ]

def write_to_7600(string):
    file_path = '/Users/timur01/Desktop/B_Intelligence/locations/7600.py'
    newdatafile = open(file_path, 'a')
    newdatafile.write('\n')
    newdatafile.write('%r' % (string[1]))

def write_to_3201(string):
    file_path = '/Users/timur01/Desktop/B_Intelligence/locations/3201.py'
    newdatafile = open(file_path, 'a')
    newdatafile.write('\n')
    newdatafile.write('%r' % (string[1]))

def write_to_7755(string):
    file_path = '/Users/timur01/Desktop/B_Intelligence/locations/7755.py'
    newdatafile = open(file_path, 'a')
    newdatafile.write('\n')
    newdatafile.write('%r' % (string[1]))

def write_to_501(string):
    file_path = '/Users/timur01/Desktop/B_Intelligence/locations/501.py'
    newdatafile = open(file_path, 'a')
    newdatafile.write('\n')
    newdatafile.write('%r' % (string[1]))

def write_to_1441(string):
    file_path = '/Users/timur01/Desktop/B_Intelligence/locations/1441.py'
    newdatafile = open(file_path, 'a')
    newdatafile.write('\n')
    newdatafile.write('%r' % (string[1]))
def write_to_10190(string):
    file_path = '/Users/timur01/Desktop/B_Intelligence/locations/10190.py'
    newdatafile = open(file_path, 'a')
    newdatafile.write('\n')
    newdatafile.write('%r' % (string[1]))

def write_to_9201(string):
    file_path = '/Users/timur01/Desktop/B_Intelligence/locations/9201.py'
    newdatafile = open(file_path, 'a')
    newdatafile.write('\n')
    newdatafile.write('%r' % (string[1]))

def write_to_attraction(string):
    file_path = '/Users/timur01/Desktop/B_Intelligence/analytics/attraction.py'
    newdatafile = open(file_path, 'a')
    newdatafile.write('\n')
    newdatafile.write('%r' % (string))

def search_write(customer_address):
    dist = Distance_Search.smallest_distance(
        customer_address,
        locations)
    print(dist)
    if dist[0].startswith('7600'):
        write_to_7600(dist)
        print("wrote to 7600")
    elif dist[0].startswith('3201'):
        write_to_3201(dist)
        print("wrote to 3201")
    elif dist[0].startswith('7755'):
        write_to_7755(dist)
        print("wrote to 7755")
    elif dist[0].startswith('501'):
        write_to_501(dist)
        print("wrote to 501")
    elif dist[0].startswith('1441'):
        write_to_1441(dist)
        print("wrote to 1441")
    elif dist[0].startswith('10190'):
        write_to_10190(dist)
        print("wrote to 10190")
    elif dist[0].startswith('9201'):
        write_to_9201(dist)
        print("wrote to 9201")
    else:
        pass

def multiple_customers_s_w(start_index, end_index):
    i = start_index
    while i < end_index:
        addr = my_sql_i.address_of_user(my_sql_i.search_in_mysql(sql_querry), i)
        print(addr)
        search_write(addr)
        i += 1

def attraction_write(start_index, end_index):
    print("wrote to attraction")
    ar = []
    i = start_index
    while i < end_index:
        attr = my_sql_i.attraction_type_digit(my_sql_i.search_in_mysql(sql_attraction_search), i)
        ar.insert(i, "{}".format(attr))
        i += 1
    print(ar)
    write_to_attraction(ar)

wooodbrige_people_querry = 'SELECT * from users WHERE town = \'Woodbridge\';'
nz = my_sql_i.customers_in(wooodbrige_people_querry)
print(len(nz))
