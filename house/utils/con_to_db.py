from pymysql import connect, OperationalError

USERNAME = 'root'
PASSWORD = 'root'
HOST = 'localhost'
PORT = 3306
DATABASE = 'house'

def query_data(sql_str):
    conn = None
    cur = None
    try:
        # 连接数据库
        conn = connect(user=USERNAME, password=PASSWORD, host=HOST, port=PORT, database=DATABASE)

        # 获取游标对象cursor
        cur = conn.cursor()

        # 使用游标对象来执行SQL语句
        cur.execute(sql_str)

        # 获取查询结果
        result = cur.fetchall()

        # 对于查询操作，不需要commit，直接返回结果
        return result

    except Exception as e:
        print(f"数据库查询出错：{e}")
        # 可以选择重新抛出异常，让上层处理
        raise

    finally:
        # 安全关闭游标和连接
        if cur:
            cur.close()
        if conn:
            conn.close()