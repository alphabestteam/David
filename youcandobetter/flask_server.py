from flask import Flask, request, jsonify, Response
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'mysqldb'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'usersDB'
mysql = MySQL(app)


def table_exists(cur, table_name):
    cur.execute(f'''SHOW TABLES LIKE '{table_name}' ''')
    if cur.fetchone():
        return True
    return False


def create_table(cur, table_name, columns):
    cur.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} ({columns})''')


@app.route("/users", methods=["POST", "GET"])
def handle_users():
    cur = mysql.connection.cursor()
    if not table_exists(cur, "users"):
        create_table(cur, "users", "id INTEGER PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255)")

    if request.method == "POST":
        try:
            data_json = request.get_json()
            user_name = str(data_json["name"])
            cur.execute('''INSERT INTO users (name) VALUES (%s)''', (user_name,))
            mysql.connection.commit()
            cur.close()
        except Exception as e:
            return Response(str(e), status=400)
        return Response(f"User {user_name} was successfully added to the database with the id {cur.lastrowid}.", status=201)
    else:
        cur.execute('''SELECT name FROM users''')
        rv = cur.fetchall()
        cur.close()
        return jsonify(rv)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)
