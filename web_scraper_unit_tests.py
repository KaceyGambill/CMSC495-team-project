import unittest
import time
import WebScraper
import app

class WebScraperTests(unittest.TestCase):

    def test_scrape_url_type(self):
        scrape_test = WebScraper.scrape_url("https://www.linkedin.com/jobs/search/?geoId=107024810&keywords=software%20engineer&location=Everett%2C%20Washington%2C%20United%20States")
        self.assertEqual(type(scrape_test), dict,
                            'wrong size after resize')

    def test_scrape_url_dict_not_empty(self):
        scrape_test = WebScraper.scrape_url("https://www.linkedin.com/jobs/search/?geoId=107024810&keywords=software%20engineer&location=Everett%2C%20Washington%2C%20United%20States")
        self.assertNotEqual(len(scrape_test), 0,
                            'wrong size after resize')

    def test_main_performance(self):
        start = time.time()
        WebScraper.main()
        end = time.time()
        performance_time = start - end
        self.assertLess(performance_time, .01, 'Test failed because it took too long')

class faskAppTests(unittest.TestCase):

    def test_job_search_performance(self):
        start = time.time()
        app.job_search()
        end = time.time()
        performance_time = start - end
        self.assertLess(performance_time, .01, 'Testing job_search failed because it took too long')

    def test_resume_help_performance(self):
        start = time.time()
        app.resume_help()
        end = time.time()
        performance_time = start - end
        self.assertLess(performance_time, .01, 'Testing resume_help failed because it took too long')

    def test_interview_tips_performance(self):
        start = time.time()
        app.interview_tips()
        end = time.time()
        performance_time = start - end
        self.assertLess(performance_time, .01, 'Testing interview_tips failed because it took too long')