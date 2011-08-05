'''
Created on Aug 2, 2011

@author: luis
'''

from __future__ import with_statement    
from com.ziclix.python.sql import zxJDBC

jdbc_url = "jdbc:hsqldb:mem"
username = "SA"
password = ""
driver = "org.hsqldb.jdbcDriver"

def hypersonic_test():

    stmt = "create table python_implementations (id integer, python_implementation varchar(50), current_version varchar(10))"
    
    # obtain a connection using the with-statment
    with zxJDBC.connect(jdbc_url, username, password, driver) as conn:
        with conn:
            with conn.cursor() as c:
                c.execute(stmt)
                stmt = "insert into PYTHON_IMPLEMENTATIONS values (?, ?, ?)"
                c.executemany(stmt, [1,'Jython','2.5.2'])
                c.executemany(stmt, [2,'CPython','3.1.1'])
                c.executemany(stmt, [3,'IronPython','2.0.2'])
                c.executemany(stmt, [4,'PyPy','1.1'])
                
                c.execute("select * from python_implementations")
                print(c.rowcount)
                print(c.fetchall())

if __name__ == '__main__':
    hypersonic_test()
    
    