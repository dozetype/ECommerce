import mysql

def get_list(cursor, table):
    cursor.execute(f"SELECT * FROM {table};")
    return cursor.fetchall()

def search(cursor, col, table, condition):
    try:
        cursor.execute(f"SELECT {col} FROM {table} WHERE {condition};")
        results = cursor.fetchall()
        return results

    except Exception as e:
        print(e)
        return None
