from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_mars 

app = Flask(__name__)

#Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/missionToMars"
mongo = PyMongo(app)


@app.route("/")
def index():
    destination_data = mongo.db.collection.find_one()
    return render_template("index.html", mars_data=destination_data)

@app.route("/scrape")
def scraper():
    # run scrape function 
    mars_data = scrape_mars.scrape()

    # insert the scraped data
    mongo.db.collection.insert_one(mars_data)

    #REDIRECT TO THE homepage
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)