import psycopg2; 

connection  = psycopg2.connect('dbname=exercise1') 

cursor = connection.cursor() 

cursor.execute (''' 
    CREATE TABLE table1 (
        id INTEGER PRIMARY KEY, 
        comments VARCHAR NOT NULL 
    ); 
''') 

cursor.execute ('''
    INSERT INTO table1 (id,comments) VALUES (1,'it is halfway done'); 
''') 

cursor.commit() 
cursor.close() 

cursor.stop() 

