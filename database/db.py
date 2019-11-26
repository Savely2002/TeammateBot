import psycopg2

def sqlite3_simple_example_create_db():
    #Открытие или создание базы данных
    con = sqlite3.connect('E:\IT Jump Pro\teammate\teammate\database\Inf_Users.db')
    #Создание объекта курсора
    cur = con.cursor()
    #Создаем таблицу если её не существует
    cur.execute('CREATE TABLE IF NOT EXISTS core_fes(Аккаунт Steam, '
                                                    'Аккаунт Discord, '
                                                    'Информация о пользователе)')
    #Добавляем данные в таблицу
    cur.execute('INSERT INTO core_fes VALUES(Profile.SteamId, Profile.DiscordId, abc)') #В скобках должна быть информация
    #Сохраняем изменения в таблице
    con.commit()
    cur.close() #Удаляем курсор
    con.close() #Разрываем соединение с базой данных
