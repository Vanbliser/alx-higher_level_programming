#!/usr/bin/python3


"""a script that lists all states from the database hbtn_0e_0_usa"""


if __name__ == '__main__':
    import MySQLdb

    from sys import argv

    uname = argv[1]
    passd = argv[2]
    db_n = argv[3]
    str_q = argv[4]
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=uname,
                           passwd=passd,
                           db=db_n,
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE `name` LIKE '{}' ORDER BY id ASC"
                .format(str_q))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
