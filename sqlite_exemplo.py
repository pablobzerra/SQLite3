import sqlite3
file = 'teste.db'
class sqlfile:
        global file
        def maker(tabela, id, name, user, passwd):
                c = sqlite3.connect(str(file))
                app = c.cursor()
                
                #CRIAR UMA TABELA
                app.execute(f'''CREATE TABLE {tabela} (id numeric, name text, usuario text, pass text)''')
                
                #INSERIR DADOS NA TABELA
                app.execute(f'''INSERT INTO {tabela} VALUES ("{str(id)}", "{str(name)}", "{str(user)}", "{str(passwd)}")''')
                
                #SALVA & FECHAR
                c.commit()
                c.close()
                print('[ SQLFILE ] --> TABELA CRIADA!!')

        def insert(tabela, id, name, user, passwd):
            #try:
            c = sqlite3.connect(file)
            app = c.cursor()
            
            #INSERIR DADOS NA TABELA
            sql = f'''INSERT INTO {tabela} VALUES ("{id}", "{name}", "{user}", "{passwd}")'''
            app.execute(sql)

            c.commit()
            c.close()
            print('[ SQLFILE ] --> dados foi adicionado a tabela!!')

        def update(tabela, id, name, user, passwd):
                c = sqlite3.connect(file)
                app = c.cursor()
                
                #ATUALIZAR UM DADO ESPECIFICO NA TABELA
                app.execute(f'''UPDATE {tabela} set name = "{name}", usuario = "{user}", pass = "{passwd}" where id = {id}''')

                c.commit()
                c.close()
                print('[ SQLFILE ] --> Tabela atualizada')

        def getData(dados):
                c = sqlite3.connect(file)
                app = c.cursor()
                
                #PUXAR DADOS DA TABELA
                app.execute(f'''SELECT * FROM {dados}''')
                tabelas = app.fetchall()

                for tabela in tabelas:
                        print(tabela)