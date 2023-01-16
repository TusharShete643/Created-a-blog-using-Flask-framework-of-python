import pymysql as p

def connect():
    return p.connect(host='localhost',user='root',password='',database='authordt',port=3306)

def addauthordetails(t):
    con=connect()
    cur=con.cursor()
    sql='insert into info values(%s,%s,%s,%s)'
    cur.execute(sql,t)
    con.commit()
    con.close()

def checklgau(t):
    con=connect()
    cur=con.cursor()
    sql='select email,password from info where email=%s'
    cur.execute(sql,t[0])
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def select():
    con=connect()
    sql='select * from info'
    cr=con.cursor()
    cr.execute(sql)
    elist=cr.fetchall()
    con.commit()
    con.close()
    return elist


