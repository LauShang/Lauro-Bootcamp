# import necessary libraries
from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.scrape_mars_db

app = Flask(__name__)


@app.route("/")
def index():
    mars = list(db.mars.find())[0]
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    new_data = scrape_mars.scrape()
    db.mars.remove()
    db.mars.insert_one(new_data)
    mars = list(db.mars.find())[0]
    return render_template("index.html", mars=mars)


if __name__ == "__main__":
    app.run(debug=True)
