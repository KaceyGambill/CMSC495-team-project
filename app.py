"""
UMGC - CMSC 495
Python Web Scraper Application - Aggregate Job Finder Application
By Autumn Capasso, Michael Galyen, Kacey Gambill, Anthony Washington, Eric Viera
"""
import WebScraper
from flask import Flask, render_template

app = Flask(__name__)

# example
scrape_list = {
        "scrape_site": "google",
        "links": [
            "http://google.com",
            "http://facebook.com",
            "http://linkedin.com"
            ]
        }


# Establish route for homepage
@app.route("/home")
@app.route("/")
def homepage():
    return render_template('index.html', table_header=scrape_list['scrape_site'], table_data=scrape_list['links'])



# Establish route for Job results page
@app.route("/jobs")
def job_search():
    job_results = WebScraper.scrape_url("https://www.dice.com/jobs?q=software%20engineering&countryCode=US&radius=30&radiusUnit=mi&page=1&pageSize=20&language=en&eid=S2Q_")
    return render_template('jobs.html', table_header=job_results['scrape_site'], table_data=job_results['links'])


# Establish route for Resume Results page
@app.route("/resume")
def resume_help():
    return render_template('resume.html', table_header=scrape_list['scrape_site'], table_data=scrape_list['links'])


# Establish route for Interview Tips page
@app.route("/interview")
def interview_tips():
    return render_template('interview.html', table_header=scrape_list['scrape_site'], table_data=scrape_list['links'])


if __name__ == '__main__':
    app.run(debug=True)

