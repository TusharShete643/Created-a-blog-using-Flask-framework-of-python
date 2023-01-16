import pymysql as p

def connect():
    return p.connect(host='localhost',user='root',password='',database='blogpost',port=3306)

def addnewblog(t):
    con=connect()
    cur=con.cursor()
    sql='insert into blog values(%s,%s,%s)'
    cur.execute(sql,t)
    con.commit()
    con.close()

def view():
    con=connect()
    cur=con.cursor()
    sql='select * from blog'
    cur.execute(sql)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data