from sqlite3 import connect


def connect():
    __DB_OBJ = connect('./data.db')
    __CUR_OBJ = __DB_OBJ.cursor()

    return (__DB_OBJ, __CUR_OBJ)


def run_querry(query: str) -> None:
    __DB_OBJ, __CUR_OBJ = connect()
    try:
        __CUR_OBJ.execute(query)
    except:
        __DB_OBJ.rollback()
        __DB_OBJ.close()
        return
    __DB_OBJ.commit()
    __DB_OBJ.close()


def get_data(query: str) -> list:
    __DB_OBJ, __CUR_OBJ = connect()
    try:
        __CUR_OBJ.execute(query)
        data = __CUR_OBJ.fetchall()
    except:
        __DB_OBJ.rollback()
        __DB_OBJ.close()
        return
    __DB_OBJ.commit()
    __DB_OBJ.close()
    return data
