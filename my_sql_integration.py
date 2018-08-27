import pymysql
print("imported my_sql_integration")

def search_in_mysql(sql_querry_string):
    """Returns a list of lists"""
    conn = pymysql.connect(
        host='DELETED',
        user='DELETED',
        password='DELETED',
        db='DELETED'
        )
    a = conn.cursor()
    a.execute(sql_querry_string)
    requested_querry = a.fetchall() # outputs a tuple/list
    return requested_querry
    # will give a list of list
    # the index of outer list gives info of a particular customer

def address_of_user(sql_list, index_of_list):
    """[6] = Street Address, [7] = City, [8] = ON, [9] = ZIP, [10] = Canada"""
    Ontario = "ON"
    Canada = "Canada"
    particular_client = sql_list[index_of_list]
    address_of_client = (
        particular_client[6],
        particular_client[7],
        Ontario,
        particular_client[9],
        Canada)
    return """{}""".format(address_of_client)
    # the input is the list from the search_in_mysql function above
    # the index_of_list variable gives info of a particular customer

def attraction_type_digit(sql_list, index_of_list):
    """_"""
    particular_client = sql_list[index_of_list]
    #print(particular_client)
    attraction_type = particular_client[-5]
    return """{}""".format(attraction_type)
    # will give output as a string
    # the output will be a single digit

def write_abb_course_date_price_students(listx, first_ever_price):
    float_int_current = float(int(listx[13]))
    float_int_first_ever = float(int(first_ever_price))
    ratio_floats = float_int_current / float_int_first_ever * 100
    stringx = "{}, {}, {}, {}, {}".format(listx[2], listx[1], listx[4], ratio_floats, listx[16])
    # 2 = location, 1 = Coure_name, 4 = Date, 13 = Price, 16 = Students
    file_path = '/Users/timur01/Desktop/B_Intelligence/prices_students.py'
    newdatafile = open(file_path, 'a')
    newdatafile.write('\n')
    newdatafile.write('%r' % (stringx))

def f_location_abb(sql_querry):
    dict_of_loc_abb = {}
    list_of_loc_abb = []
    loc_abb_search = search_in_mysql(sql_querry) # list of lists
    for index, item in enumerate(loc_abb_search):
        dict_of_loc_abb[item[2]] = dict_of_loc_abb.get(item, 0) + 1
    for key, value in dict_of_loc_abb.items():
        list_of_loc_abb.insert(0, key)
    return list_of_loc_abb
    # location_abb_querry = 'SELECT * from courses'

def request_courses_in_location(list_of_course_abb, list_of_loc_abb):
    for index, item in enumerate(list_of_loc_abb):
        for idx, itm in enumerate(list_of_course_abb):
            sqL_format = "SELECT * from courses WHERE location_id = \'{}\' and course_name_id = \'{}\' order by start_date;".format(item, itm)
            list_of_requested_items = search_in_mysql(sqL_format)
            i = 0
            while i < len(list_of_requested_items):
                write_abb_course_date_price_students(list_of_requested_items[i], int(list_of_requested_items[0][13]))
                print(list_of_requested_items[i])
                i += 1

def f_course_abb(sql_querry):
    list_of_abbs = []
    dict_of_abbs = {}
    non_repeat_list = []
    course_names_search = search_in_mysql(sql_querry) # list of lists
    for index, item in enumerate(course_names_search):
        list_of_abbs.insert(0, item[1])
    for index, item in enumerate(list_of_abbs):
        dict_of_abbs[item] = dict_of_abbs.get(item, 0) + 1
    for key, value in dict_of_abbs.items():
        non_repeat_list.insert(0, key)
    return non_repeat_list
    # course_names_querry = 'SELECT * from course_names'

def customers_in(sql_querry):
    list_of_specific_customers = []
    list_of_customers = search_in_mysql(sql_querry)
    for index, item in enumerate(list_of_customers):
        list_of_specific_customers.insert(0, address_of_user(list_of_customers, index))
    return list_of_specific_customers

def all_course_dates(sql_querry):
    list_of_all_dates = []
    sql_output = search_in_mysql(sql_querry)
    print("total entries %d" % (len(sql_output)))
    for index, item in enumerate(sql_output):
        if item[4] in list_of_all_dates:
            pass
            #print("passed %r" % (item[4]))
        else:
            list_of_all_dates.insert(-1, item[4])
            #print("added %r to the list" % (item[4]))
    if None in list_of_all_dates:
        list_of_all_dates.remove(None)
    else:
        pass
    return(list_of_all_dates)

course_abbreviations = ('D1', 'SB', 'Y1', 'W1', 'B1', 'J2', 'H1', 'RH', 'H2',
    'MB', 'F5', 'F4', 'F3', 'F2', 'F1', 'ET', 'CS', 'AS', 'PJ', 'T1', 'EC',
    'EA', 'AJ', 'R3', 'R2', 'R1', 'P1', 'P2', 'RJ', 'Z1', 'NT', 'C1', 'C2',
    'RL', 'RC', 'RB', 'RA', 'PC', 'A1', 'NC', 'NA', 'G1', 'G2', 'PR', 'GR',
    'JA', 'M1', 'HW', 'S1', 'S2', 'JT', 'WD')

def specific_course_income(course_abb, location_abb):
    sql_querry = """select * from courses
    where course_name_id = '%s' and location_id = '%s'
    order by start_date;""" % (course_abb, location_abb)
    sql_output = search_in_mysql(sql_querry)
    list_of_dates = []
    for index1, item1 in enumerate(sql_output):
        if item1[4] not in list_of_dates:
            list_of_dates.insert(-1, item1[4])
        elif item1[4] in list_of_dates:
            pass
        else:
            pass
    print("the sql_output list is %s ling" % (len(sql_output)))
    print("the list of dates is %s long" % len(list_of_dates))
    for index2, item2 in enumerate(list_of_dates):
        if item2 is None:
            pass
        else:
            new_sql_querry = """select * from courses
            where course_name_id = '%s' and location_id = '%s' and start_date = '%s'
            order by start_date;""" % (course_abb, location_abb, item2)
            refined_sql_search = search_in_mysql(new_sql_querry)
            if len(refined_sql_search) == 1:
                for index3, item3 in enumerate(refined_sql_search):
                    income = int(item3[13]) * int(item3[16])
                    print("%s, %s, %s, %d" % (location_abb, course_abb, item2, income))
            elif len(refined_sql_search) > 1:
                #print ("%s querry has %d results" % (item2, len(refined_sql_search)))
                income_list = []
                for index4, item4 in enumerate(refined_sql_search):
                    income = int(item4[13]) * int(item4[16])
                    income_list.insert(0, income)
                #print(income_list)
                avg_income = sum(income_list)/len(income_list)
                print("%s, %s, %s, %d" % (location_abb, course_abb, item2, avg_income))
            else:
                pass

def write_excel_format(centre, date, string):
    file_path = '/Users/timur01/Desktop/centres.csv'#B_Intelligence/centress.csv'
    newdatafile = open(file_path, 'a')
    newdatafile.write('\n')
    newdatafile.write('%s, %s, %s' % (centre, date, string))

def specific_centre_income(centre):
    print("looking through courses offered at %s" % (centre))
    for idx, itm in enumerate(course_abbreviations):
        print(idx, itm)
    for index0, date_x in enumerate(ordered_list_of_dates):
        print("searching %s" % (date_x))
        sql_querry = """select * from courses
        where location_id = '%s' and start_date = '%s';""" % (centre, date_x)
        sql_output = search_in_mysql(sql_querry)
        print("A %s has %d results" % (date_x, len(sql_output)))
        if len(sql_output) == 0:
            pass
        elif len(sql_output) == 1:
            print("B the only result is %s" % (sql_output[0][1]))
            dummy_list = [77777, 77777, 77777, 77777, 77777, 77777, 77777,
            77777, 77777, 77777, 77777, 77777, 77777, 77777, 77777, 77777,
            77777, 77777, 77777, 77777, 77777, 77777, 77777, 77777, 77777,
            77777, 77777, 77777, 77777, 77777, 77777, 77777, 77777, 77777,
            77777, 77777, 77777, 77777, 77777, 77777, 77777, 77777, 77777,
            77777, 77777, 77777, 77777, 77777, 77777, 77777, 77777, 77777,]
            for index1, item1 in enumerate(sql_output):
                yincome = int(item1[13]) * int(item1[16])
                int_position_in_string = course_abbreviations.index(item1[1])
                dummy_list[int_position_in_string] = yincome
                print("C the course is %s amount is %d and position is %d" % (item1[1], yincome, int_position_in_string))
                print("(the price is %d and # of students is %d)" % (item1[13], item1[16]))
            write_excel_format(centre, date_x, dummy_list)
        elif len(sql_output) > 1: # if there are multiple courses
            coursesx = []
            dummy_list = [77777, 77777, 77777, 77777, 77777, 77777, 77777,
            77777, 77777, 77777, 77777, 77777, 77777, 77777, 77777, 77777,
            77777, 77777, 77777, 77777, 77777, 77777, 77777, 77777, 77777,
            77777, 77777, 77777, 77777, 77777, 77777, 77777, 77777, 77777,
            77777, 77777, 77777, 77777, 77777, 77777, 77777, 77777, 77777,
            77777, 77777, 77777, 77777, 77777, 77777, 77777, 77777, 77777,]
            for index2, item2 in enumerate(sql_output):
                if item2[1] not in coursesx:
                    coursesx.insert(-1, item2[1])
                else:
                    pass
            print("D and out of %d results, there are %d unique courses" % (len(sql_output), len(coursesx)))
            if len(coursesx) == 1: # if there are multiple courses but they are of the same kind
                print("E The only available course is: %s" % (coursesx[0]))
                zincome_list = []
                for index3, item3 in enumerate(sql_output):
                    zincome = int(item3[13]) * int(item3[16])
                    zincome_list.insert(-1, zincome)
                    print("(the price is %d and # students is %d)" % (item3[13], item3[16]))
                average_income = sum(zincome_list)#/len(zincome_list) # average distorts the picture
                zint_position_in_string = course_abbreviations.index(coursesx[0])
                dummy_list[zint_position_in_string] = average_income
                print("F the course is %s average_amount is %d and position is %d" % (coursesx[0], average_income, zint_position_in_string))
                write_excel_format(centre, date_x, dummy_list)
            elif len(coursesx) > 1: # if there are multiple courses but of different kind
                print("G The availble courses are: %s" % (coursesx))
                for index4, item4 in enumerate(coursesx):
                    new_search_q = """select * from courses
                    where location_id = '%s' and start_date = '%s' and course_name_id = '%s';""" % (centre, date_x, item4)
                    print("H searching for %s" % (item4))
                    refined_search = search_in_mysql(new_search_q) # make a new search for a specic course
                    if len(refined_search) == 1:
                        print("I the course %s had only 1 result" % (refined_search[0][1]))
                        xincome_list = []
                        for index5, item5 in enumerate(refined_search):
                            xincome = int(item5[13]) * int(item5[16])
                            xincome_list.insert(-1, xincome)
                            print("(the price is %d and # of students is %d)" % (item5[13], item5[16]))
                        xavg_income = sum(xincome_list)#/len(xincome_list)#average distorts
                        pos = course_abbreviations.index(item4)
                        dummy_list[pos] = xavg_income
                        print("J the course is %s amount is %d and position is %d" % (refined_search[0][1], xavg_income, pos))
                        print("K Inserting amount %d course %s into %s position" % (xavg_income, item4, pos))
                    elif len(refined_search) > 1:
                        print("L the course %s had %d results" % (item4, len(refined_search)))
                        cincome_list = []
                        for index6, item6 in enumerate(refined_search):
                            cincome = int(item6[13]) * int(item6[16])
                            cincome_list.insert(-1, cincome)
                            print("(the price is %d and # students is %d)" % (item6[13], item6[16]))
                        cavg_income = sum(cincome_list)#/len(cincome_list)#average distorts
                        cpos = course_abbreviations.index(item4)
                        dummy_list[cpos] = cavg_income
                        print("M Inserting average amount %d course %s into %s position" % (cavg_income, item4, cpos))
                    else:
                        pass
                write_excel_format(centre, date_x, dummy_list)
            else:
                pass
        else:
            pass

def demo_code(abc):
    locales = ['MP', 'HG', 'GM', 'HM', 'TH', 'PG', 'WS', 'MW', 'AP', 'BT',
    'ST', 'DC', 'BH', 'MM', 'CN', 'SM', 'RB', 'BG', 'GW']
    for index, item in enumerate(locales):
        specific_centre_income(item)
        print("FINISHED WITH %s" % (item))

jxd = demo_code('abc')

course_dates_querry = 'SELECT * from courses WHERE start_date >\'\' order by start_date;'
ordered_list_of_dates = all_course_dates(course_dates_querry)
print(ordered_list_of_dates)
