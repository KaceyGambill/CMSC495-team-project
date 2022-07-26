import unittest
import time
import WebScraper
import app

class WebScraperTests(unittest.TestCase):
    '''
    This class will test the WebScraper functions
    '''

    # Test scrape_url function
    def test_scrape_url_type(self):
        scrape_test = WebScraper.scrape_url("https://www.linkedin.com/jobs/search/?geoId=107024810&keywords=software%20engineer&location=Everett%2C%20Washington%2C%20United%20States")
        self.assertEqual(type(scrape_test), dict,
                            'wrong size after resize')

    # Test scrape_url function
    def test_scrape_url_dict_not_empty(self):
        scrape_test = WebScraper.scrape_url("https://www.linkedin.com/jobs/search/?geoId=107024810&keywords=software%20engineer&location=Everett%2C%20Washington%2C%20United%20States")
        self.assertNotEqual(len(scrape_test), 0,
                            'wrong size after resize')

    # Test main function
    def test_main_performance(self):
        start = time.time()
        WebScraper.main()
        end = time.time()
        performance_time = start - end
        self.assertLess(performance_time, .01, 'Test failed because it took too long')

    # Test scrape_url function for perfomance
    def test_scrape_url_dict_not_empty_performance(self):
        start = time.time()
        WebScraper.test_scrape_url_dict_not_empty()
        end = time.time()
        performance_time = start - end
        self.assertLess(performance_time, .01, 'Test failed because it took too long')

