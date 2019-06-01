#################################################
# Import Dependencies
#################################################
from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_mars

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape_all()
    mars.update({}, mars_data, upsert=True)
    return "Scraping Complete"


if __name__ == "__main__":
    app.run()
