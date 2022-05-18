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

cursor.execute('DROP TABLE IF EXISTS table1;')

cursor.execute (''' 
    INSERT INTO table1 (id, description, completed) VALUES (%s,%s,%s); 
''', 
    (1,'question one', True)
)  

cursor.execute ('''
   INTSERT INTO table1 (id,description,completed) VALUES (%(id)s,%(description)s,%(completed)s);
''', 
    {
        'id': 1, 
        'description': 'question two', 
        'completed': False 
    }
)

cursor.commit()
connection.close() 

cursor.stop() 