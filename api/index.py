import os
import psycopg2
from flask import Flask, render_template
import json
from flask_cors import CORS, cross_origin


app = Flask(__name__)
# DB_NAME = "oscar_db"
# DB_USER = "oscar_user"
# DB_PASS = "12345"
# DB_HOST = "localhost"
DB_PORT = "5432"


DB_URL="postgres://default:FcVuaDQ1lR2j@ep-spring-meadow-154032-pooler.ap-southeast-1.postgres.vercel-storage.com:5432/verceldb"
POSTGRES_PRISMA_URL="postgres://default:FcVuaDQ1lR2j@ep-spring-meadow-154032-pooler.ap-southeast-1.postgres.vercel-storage.com:5432/verceldb?pgbouncer=true&connect_timeout=15"
POSTGRES_URL_NON_POOLING="postgres://default:FcVuaDQ1lR2j@ep-spring-meadow-154032.ap-southeast-1.postgres.vercel-storage.com:5432/verceldb"
DB_USER="default"
DB_HOST="ep-spring-meadow-154032-pooler.ap-southeast-1.postgres.vercel-storage.com"
DB_PASS="FcVuaDQ1lR2j"
DB_NAME="verceldb"





def get_db_connection():
    connect = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    return connect


@app.route('/')
@app.route('/<string:year>')
@cross_origin()
def home(year="2023"):
    conn = get_db_connection()
    cur=conn.cursor()
    if (year.isdigit()==False):
        year = 2023
    elif(year.isdigit()==True and (len(year)<3 or len(year)>5)):
        year = 2023
    else:
        year = str(year)
    cur.execute("SELECT * FROM oscar_data WHERE YEAR = {};".format(year))
    d_a_t_a = cur.fetchall()

    cur.close()
    conn.close()
    winner_list = ''
    for i in d_a_t_a:
        winner_list = json.loads(str(i[2]))



    return winner_list





if __name__ == "__main__":
    app.run(debug=True)
