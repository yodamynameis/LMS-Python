from Function import *
import mysql.connector as m
con=m.connect(host='localhost',
              user='root',
              passwd='mysql',
              db='library')
while True:
    print('''#####UTOPIA LIBRARY#####
    1. Admin options
    2. Reader Options
    3. Search
    4. View books
    5. Exit''')
    ch=input('Please enter any one option--->')

    while ch not in('1','2','3','4','5'):
        print('Please select a valid option')
        ch= input('Please select anyone option---> ')
    if int(ch)==1:
        p=input('Enter Admin Password--->')
        if p=='utopia@123':
            print('''          Admin options
1. Add Book
2. Remove Book''')
            ch=input('Please enter any one option--->')
            while ch not in ('1','2'):
                print('Please select a valid option')
                ch=input('Please enter any one option--->')
            if int(ch)==1:
                abk()
            elif int(ch)==2:
                rbk()
        else:
            print('Enter correct Password')
    elif int(ch)==2:
        print('''Reader Option
        1. Issue book
        2. Return book''')
        ch=input('Please enter any one option--->')
        while ch not in ('1','2'):
            print('Please select a valid option')
            ch=input('Please enter any one option--->')
        if int(ch)==1:
            ibk()
        elif int(ch)==2:
            rtb()
        
    elif int(ch)==3:
        print('search')
        search()
    elif int(ch)==4:
        print('''view books
        1. View all Books
        2. View all available Books''')
        ch=input('Please enter any one option--->')
        while ch not in ('1','2'):
            print('Please select a valid option')
            ch=input('Please enter any one option--->')
        if int(ch)==1:
            vab()
        elif int(ch)==2:
            vaba()
    elif int(ch)==5:
        print('BYE BYE! thanks for visiting')
        exit()
