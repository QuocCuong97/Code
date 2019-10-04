def creat_database():
    mariahost = input('MariaDB Host (localhost): ')
    if mariahost == '':
        mariahost == 'localhost'
    mariadb = input('New MariaDB Name: ')
    mariauser = input('New MariaDB User: ')
    mariapass = input('Password: ')

creat_database