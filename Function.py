
import mysql.connector as m
con=m.connect(host='localhost',
              user='root',
              passwd='mysql',
              db='library')



def abk():  #addbook
    bcode=input('Enter the book Code--->')
    bname=input('Enter the book name--->')
    author=input("Enter author's name--->")
    
    status=input('Enter Status i.e. Available/Issued--->')
    c=con.cursor()
    q1="insert into books(bcode,bname,author,status) values('{}','{}','{}','{}')" . format(bcode,bname,author,status)
    c.execute(q1)
    con.commit()

def rbk():  #removebook
    bcode=input("Enter the book's code--->")
    q1="delete from books where bcode='{}'" . format(bcode)
    c=con.cursor()
    c.execute(q1)
    con.commit()

def vab():  #view all books
    c=con.cursor()
    q1="select * from books"
    c.execute(q1)
    for i in c:
        print(i)
    con.commit()

def vaba(): #view all available books
    c=con.cursor()
    q1="select * from books where status='Available'"
    c.execute(q1)
    for i in c:
        print(i)
    con.commit()

def ibk():  #issue book
    bcode=input('Enter the Code of the Book you want to Issue--->')
    ib=input('Enter your registered name--->')
    c=con.cursor()
    q1="update books set issued_by='{}',status='Issued' where bcode='{}'" . format(ib,bcode)
    c.execute(q1)
    con.commit()

def rtb():  #return book
    bcode=input('Enter the Code of the Book you want to Return--->')
    c=con.cursor()
    q1="update books set issued_by is NULL,status='Available' where bcode='{}'" . format(bcode)
    c.execute(q1)
    con.commit()

def search(): #search
    print('''Search BY:
    1.Book Code
    2.Book Name
    3.Author Name''')
    ch=input('Enter any one option--->')
    c=con.cursor()
    while ch not in('1','2','3'):
        print('Please select a valid option')
        ch= input('Please select anyone option---> ')
    if int(ch)==1:
        bcode=input('Enter the Code of the Book you want to search--->')
        q1="select * from books where bcode='{}'" . format(bcode)
    elif int(ch)==2:
        bname=input('Enter the Name of the Book you want to Search--->')
        q1="select * from books where bname like  '%{}%' " . format(bname)
    elif int(ch)==3:
        aname=input("Enter the name of the author whose books you want to search--->")
        q1="select * from books where author like  '%{}%' " . format(aname)
    c.execute(q1)
    for i in c:
        print(i)
    con.commit()




    
