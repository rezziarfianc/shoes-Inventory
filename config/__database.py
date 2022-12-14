import mysql.connector

db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "",
  database = "sepatu"
)

if db.is_connected():
  def con():
    return db