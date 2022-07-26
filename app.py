"""
UMGC - CMSC 495
Python Web Scraper Application - Aggregate Job Finder Application
By Autumn Capasso, Michael Galyen, Kacey Gambill, Anthony Washington, Eric Viera
"""
import WebScraper
from flask import Flask, render_template, request

app = Flask(__name__)

# example
#scrape_list = {
#        "scrape_site": "google",
#        "links": [
#            "http://google.com",
#            "http://facebook.com",
#            "http://linkedin.com"
#            ]
#        }


# Establish route for homepage
@app.route("/home")
@app.route("/")
def homepage():
    return render_template('index.html')



# Establish route for Job results page
@app.route("/jobs", methods = ['POST', 'GET'])
def job_search():
    if request.method == 'GET':
        # array of sites to search for information
        options = ['https://www.dice.com/jobs?q=software%20engineering&countryCode=US&radius=30&radiusUnit=mi&page=1&pageSize=20&language=en&eid=S2Q_', 'https://www.linkedin.com/jobs/search/?geoId=107024810&keywords=software%20engineer&location=Everett%2C%20Washington%2C%20United%20States']
        return render_template('jobs.html',request='GET', url='jobs', options=options)
    if request.method == 'POST':
        result = request.form['link']
        job_results = WebScraper.scrape_url(result)
        return render_template('jobs.html', table_header=job_results['scrape_site'], table_data=job_results['links'])


# Establish route for Resume Results page
@app.route("/resume", methods = ['POST', 'GET'])
def resume_help():
    if request.method == 'GET':
        # array of sites to search for information
        options = ["https://www.freecodecamp.org/news/tag/resume"]
        return render_template(
                'resume.html',
                request='GET',
                url='resume',
                options=options
                )
    if request.method == 'POST':
        result = request.form['link']
        resume_results  = WebScraper.links(result)
        return render_template(
                'resume.html',
                url = '/resume',
                table_header="Resume Tips",
                table_data=resume_results
                )


# Establish route for Interview Tips page
@app.route("/interview", methods = ['POST', 'GET'])
def interview_tips():
    if request.method == 'GET':
        # array of sites to search for information
        options = ["https://www.freecodecamp.org/news/tag/interview"]
        return render_template(
                'interview.html',
                request='GET',
                url='interview',
                options=options
                )
    if request.method == 'POST':
        result = request.form['link']
        interview_results  = WebScraper.links(result)
        return render_template(
                'interview.html',
                url = '/interview',
                table_header="Interview Tips",
                table_data=interview_results
                )


if __name__ == '__main__':
    app.run(debug=True)

