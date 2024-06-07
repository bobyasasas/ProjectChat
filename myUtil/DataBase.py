import sqlite3


class Database:
    def __init__(self, db_name):
        """ 初始化数据库连接和游标 """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        """ 创建数据表 """
        column_definitions = ', '.join([f"{col_name} {col_type}" for col_name, col_type in columns.items()])
        create_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions})"
        self.cursor.execute(create_sql)
        self.conn.commit()
        print(f"Table {table_name} created.")

    def insert(self, table_name, data):
        """ 插入数据 """
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?' for _ in data])
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(sql, tuple(data.values()))
        self.conn.commit()

    def select(self, table_name, columns="*"):
        """ 查询数据 """
        sql = f"SELECT {columns} FROM {table_name}"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def update(self, table_name, data, conditions):
        """ 更新数据 """
        set_clause = ', '.join([f"{col} = ?" for col in data])
        cond_clause = ' AND '.join([f"{k} = ?" for k in conditions])
        sql = f"UPDATE {table_name} SET {set_clause} WHERE {cond_clause}"
        self.cursor.execute(sql, tuple(data.values()) + tuple(conditions.values()))
        self.conn.commit()

    def delete(self, table_name, conditions):
        """ 删除数据 """
        cond_clause = ' AND '.join([f"{k} = ?" for k in conditions])
        sql = f"DELETE FROM {table_name} WHERE {cond_clause}"
        self.cursor.execute(sql, tuple(conditions.values()))
        self.conn.commit()

    def close(self):
        """ 关闭数据库连接 """
        self.conn.close()
