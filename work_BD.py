import sqlite3


class BDManager():
    'class по работе с базой данных проектов'
    conn = sqlite3.connect('DB.db', check_same_thread=False)
    sql = conn.cursor()

    @classmethod
    def create_table(cls) -> None:
        'создание таблицы и столбцов базы данных'
        cls.sql.execute('''CREATE TABLE IF NOT EXISTS projects(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    date TEXT,
                    comment TEXT,
                    work_in TEXT)
                    ''')
        cls.conn.commit()

    def insert_data(self, data: list) -> None:
        'добавление данных в таблицу в формате list'
        self.sql.execute('INSERT INTO projects(name, date, comment, work_in) values(?, ?, ?, ?)', data)
        self.conn.commit()
        print('Данные добавлены')

    def drop_data(self, id_project: int) -> None:
        'удаление данных из таблицы по id'
        if type(id_project) == int:
            self.sql.execute(f'DELETE FROM projects WHERE id = {id_project}')
            self.conn.commit()
            print('Данные удалены')
        else:
            print('Ошибка ввода id')

    def select_data_all(self) -> dict:
        'получение всех данных таблицы'
        datas = self.sql.execute('SELECT * FROM projects')
        for data in datas:
            D = {1: data[1], 2: data[3], 3: data[4]}
            yield D
