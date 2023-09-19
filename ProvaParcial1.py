import mysql.connector

con = mysql.connector.connect(host='localhost', database='pp_1', user='root', password='root')

tabela_job = """
    CREATE TABLE IF NOT EXISTS job(
        job_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50), 
        description VARCHAR(200)
        )
"""

tabela_employee = """
 CREATE TABLE IF NOT EXISTS employee (
        employee_id INT NOT NULL AUTO_INCREMENT,
        job_id INT NOT NULL,
        name VARCHAR(100) NOT NULL,
        birthday DATE NOT NULL,
        salary FLOAT(10,2) NOT NULL,
        department VARCHAR(100) NOT NULL,
    PRIMARY KEY (employeeID),
        FOREIGN KEY (job_id)
        REFERENCES job (job_id)
        )
"""

tabela_job_history = """
  CREATE TABLE IF NOT EXISTS job_history (
        job_history_id INT NOT NULL AUTO_INCREMENT,
        title VARCHAR(100) NOT NULL,
        start_date DATE NOT NULL,
        end_date DATE NOT NULL,
        salary FLOAT(10,2) NOT NULL,
        job VARCHAR(100) NOT NULL,
        employee_id INT NOT NULL,
    PRIMARY KEY (job_history_id),
        FOREIGN KEY (employee_id)
        REFERENCES employee (employee_id)
    )
"""

cursor = con.cursor()

cursor.execute(tabela_job)
cursor.execute(tabela_employee)
cursor.execute(tabela_job_history)

inicio = int(input("Digite 1 para acessar o banco e 2 para encerrar: "))

while inicio == 1:

    menu = int(input("Digite 1 para tabela job, 2 para tabela employee e 3 para tabela job_history: "))

    if menu == 1: 

        func = int(input("Digite 1 para inserir, 2 para deletar, 3 para atualizar e 4 para listar: "))
            
        if func == 1:

            x = int(input("Digite o id do trabalho: "))
            y = input("Digite o nome do trabalho: ")
            z = input("Digite a descrição do trabalho: ")

            cursor.execute('INSERT INTO job (job_id, name, description) VALUES (%s, %s, %s)', (x, y, z))
        
        elif func == 2:

            x = input("Digite o id do trabalho que será excluido: ")

            cursor.execute("DELETE FROM job_history WHERE employee_id IN (SELECT employee_id FROM employee WHERE job_id = " + x +")")
            cursor.execute("DELETE FROM employee WHERE job_id = " + x)  
            cursor.execute("DELETE FROM job WHERE job_id = "+ x)
          

        elif func == 3:
        
            x = int(input("Digite o id do trabalho: "))
            y = input("Digite o nome do trabalho: ")
            z = input("Digite a descrição do trabalho: ")
        
            cursor.execute('UPDATE job SET name = %s, description = %s WHERE job_id = %s', (y, z, x))

        elif func == 4:

            cursor.execute('SELECT * FROM job LEFT JOIN employee ON job.job_id = employee.job_id LEFT JOIN job_history ON employee.employee_id = job_history.employee_id')

            for job in cursor.fetchall():
                print(job)

    elif menu == 2:

        func = int(input("Digite 1 para inserir, 2 para deletar, 3 para atualizar e 4 para listar: "))

        if func == 1:   
        
            x = int(input("Digite o id do empregado: "))
            y = input("Digite o nome do empregado: ")
            z = input("Digite a data de nascimento do empregado(yyyy-mm--dd): ")
            w = float(input("Digite o salario do empregado: "))
            v = input("Digite o departamento do empregado: ")
            u = int(input("Digite o id do trabalho: "))

            cursor.execute('INSERT INTO employee (employee_id, name, birthdate, salary, department, job_id) VALUES (%s, %s, %s, %s, %s, %s)', (x, y, z, w, v, u))
        elif func == 2:
                
         x = input("Digite o id do empregado: ")

         cursor.execute('DELETE FROM job_history WHERE employee_id = ' + x)
         cursor.execute('DELETE FROM employee WHERE employee_id = ' + x)

        elif func == 3:

            x = int(input("Digite o id do empregado: "))
            y = input("Digite o nome do empregado: ")
            z = input("Digite a data de nascimento do empregado(yyyy-mm--dd): ")
            w = float(input("Digite o salario do empregado: "))
            v = input("Digite o departamento do empregado: ")
            u = int(input("Digite o id do trabalho: "))

            cursor.execute('UPDATE employee SET name = %s, birthdate = %s, salary = %s, department = %s, job_id = %s WHERE employee_id = %s', (y, z, w, v, u, x))
       
        elif func == 4:

            cursor.execute('SELECT * FROM employee LEFT JOIN job_history ON employee.employee_id = job_history.employee_id')

            for employee in cursor.fetchall():
                print(employee)

    elif menu == 3:

            func = int(input("Digite 1 para inserir, 2 para deletar, 3 para atualizar e 4 para listar: "))

            if func == 1:   
                
                x = int(input("Digite o id do histórico: "))
                x1 = input("Digite o título: ")
                y = input("Digite a data de inicio do histórico(yyyy-mm--dd): ")
                z = input("Digite a data de fim do histórico(yyyy-mm--dd): ")
                w = float(input("Digite o salario do histórico: "))
                v = input("Digite o trabalho do histórico: ")
                u = int(input("Digite o id do empregado: "))

                cursor.execute('INSERT INTO job_history (job_history_id, title, start_date, end_date, salary, job, employee_id) VALUES (%s, %s, %s, %s, %s, %s, %s)', (x, x1, y, z, w, v, u))
               
            elif func == 2:
                    
                x = input("Digite o id do histórico: ")
                cursor.execute('DELETE FROM job_history WHERE job_history_id = ' + x)

            elif func == 3:

                x = int(input("Digite o id do histórico: "))
                x1 = input("Digite o título: ")
                y = input("Digite a data de inicio do histórico(yyyy-mm--dd): ")
                z = input("Digite a data de fim do histórico(yyyy-mm--dd): ")
                w = float(input("Digite o salario do histórico: "))
                v = input("Digite o trabalho do histórico: ")
                u = int(input("Digite o id do empregado: "))

                cursor.execute('UPDATE job_history SET title = %s, start_date = %s, end_date = %s, salary = %s, job = %s, employee_id = %s WHERE job_history_id = %s', (x1, y, z, w, v, u, x))
            elif func == 4:

                cursor.execute('SELECT * FROM job_history')

                for job_history in cursor.fetchall():
                    print(job_history)
    con.commit()

    inicio = int(input("Digite 1 para acessar o banco e 2 para encerrar: "))

