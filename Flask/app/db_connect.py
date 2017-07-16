from app import app
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask_mysqldb import MySQL 

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ViaSafe'
mysql = MySQL(app)

@app.route('/databasetest')
def index():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT countryname FROM countries''')
	rv = cur.fetchall()
	return str(rv)
