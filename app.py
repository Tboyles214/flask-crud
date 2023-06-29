from flask import Flask, render_template
import psycopg2

url ="postgres://argskbfi:JPetNCnTcFwMA8GLWav8tsy6-DyDNqLv@mahmud.db.elephantsql.com/argskbfi"

conn = psycopg2.connect(url)



app = Flask(__name__)


#Route
@app.route("/")
#Route Handler

def root():
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users(username, email) Values('john_doe', 'john.doe@example.com') RETURNING (username, email);")
    conn.commit()
    rows = cursor.fetchall()
    print(rows)
    return render_template('home.html', users=users)


#Route
@app.route("/newuser")
#Route Handler

def newuser():
    return render_template('new_user.html')

#Route
@app.route("/submit")
#Route Handler

def newuser():
    return render_template('new_user.html')


