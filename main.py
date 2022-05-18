import psycopg2 

connection = psycopg2.connect('dbname=example') 

cursor = connection.cursor() 

cursor.execute ('''
    CREATE TABLE table1 (
        id INTEGER PRIMARY KEY,  
        description VARCHAR NOT NULL, 
        completed BOOLEAN NOT NULL DEFAULT False
    ); 
''') 

cursor.execute (''' 
    INSERT INTO table1 (id, decription, completed) VALUES (1,'question one',True); 
''') 

cursor.commit()
connection.close() 

cursor.stop() 