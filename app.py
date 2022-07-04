"""
UMGC - CMSC 495
Python Web Scraper Application - Aggregate Job Finder Application
By Autumn Capasso, Michael Galyen, Kacey Gambill, Anthony Washington, Eric Viera
"""

from flask import Flask, render_template

app = Flask(__name__)


# Establish route for homepage
@app.route("/home")
@app.route("/")
def homepage():
    """Replace <p> tag with html template for homepage - use render_template
       Directs user to homepage"""
    return "<p>Homepage</p>"


# Establish route for Job results page
@app.route("/jobs")
def job_search():
    """Replace <p> tag with html template for job search results- use render_template
       Directs user job search return results """
    return "<p>Job Search Results</p>"


# Establish route for Resume Results page
@app.route("/resume")
def resume_help():
    """Replace <p> tag with html template for resume help results - use render_template
       Directs user to resume return results """
    return "<p>Resumes Results</p>"


# Establish route for Interview Tips page
@app.route("/interview")
def interview_tips():
    """Replace <p> tag with html template for interview tips - use render_template
       Directs user to interview tips page """
    return "<p>Interview Tips</p>"


if __name__ == '__main__':
    app.run(debug=True)

