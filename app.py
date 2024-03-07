from flask import Flask, jsonify
import pymysql.cursors

app = Flask(__name__)

# Database connection information would be provided by Secretless Broker, hence no credentials here
DATABASE_HOST = 'localhost'
DATABASE_PORT = 3306
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_DB = 'sampledb'

def get_db_connection():
    connection = pymysql.connect(host=DATABASE_HOST,
                                 user=DATABASE_USER,
                                 password=DATABASE_PASSWORD,
                                 database=DATABASE_DB,
                                 cursorclass=pymysql.cursors.DictCursor,
                                 port=DATABASE_PORT)
    return connection

@app.route('/')
def index():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        cursor.close()
        connection.close()
        return jsonify({"db_version": version})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
