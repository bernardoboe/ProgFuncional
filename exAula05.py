import mysql.connector

con = mysql.connector.connect(host='localhost', database='ex_CRUD', user='root', password='root')

tabela_author= """
    CREATE TABLE IF NOT EXISTS author(
        author_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50)
    )
"""

tabela_post = """
    CREATE TABLE IF NOT EXISTS post(
        post_id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(50), created DATE, author_id INT,
        FOREIGN KEY (author_id) REFERENCES Author(author_id)
    )
"""

cursor = con.cursor()

cursor.execute(tabela_author)
cursor.execute(tabela_post)

inicio = int(input("Digite 1 para acessar o banco e 2 para encerrar: "))

while inicio == 1:

    menu = int(input("Digite 1 para tabela autor e 2 para tabela post: "))

    if menu == 1: 

        func = int(input("Digite 1 para inserir, 2 para deletar, 3 para atualizar e 4 para listar: "))
            
        if func == 1:

            x = int(input("Digite o id do autor: "))
            y = input("Digite o nome do autor: ")

            cursor.execute('INSERT INTO author (author_id, name) VALUES (%s, %s)', (x, y))
        
        elif func == 2:

            x = input("Digite o id do autor que será excluido: ")

            cursor.execute('DELETE FROM post WHERE author_id = ' + x)
            cursor.execute('DELETE FROM author WHERE author_id = ' + x)
          

        elif func == 3:
        
            x = int(input("Digite o id do autor: "))
            y = input("Digite o nome do autor: ")
        
            cursor.execute('UPDATE author SET name = %s WHERE author_id = %s', (y, x))

        elif func == 4:

            cursor.execute('SELECT * FROM author')

            for author in cursor.fetchall():
                print(author)

    elif menu == 2:

        func = int(input("Digite 1 para inserir, 2 para deletar, 3 para atualizar e 4 para listar: "))

        if func == 1:   
        
            x = int(input("Digite o id do post: "))
            y = input("Digite o titulo do post: ")
            z = input("Digite a data de criação do post(yyyy-mm--dd): ")
            w = int(input("Digite o id do autor: "))
    
            cursor.execute('INSERT INTO post (post_id, title, created, author_id) VALUES (%s, %s, %s, %s)', (x, y, z, w))

        elif func == 2:
                
            x = input("Digite o id do post: ")

        
            cursor.execute('DELETE FROM post WHERE post_id = '+ x)


        elif func == 3:

            x = int(input("Digite o id do post: "))
            y = input("Digite o titulo do post: ")
            z = input("Digite a data de criação do post(yyyy-mm--dd): ")
            w = int(input("Digite o id do autor: "))

            cursor.execute('UPDATE post SET title = %s, created = %s, author_id = %s WHERE post_id = %s', (y, z, w, x))

        elif func == 4:

            cursor.execute('SELECT * FROM post')

            for post in cursor.fetchall():
                print(post)

    con.commit()

    inicio = int(input("Digite 1 para acessar o banco e 2 para encerrar: "))



