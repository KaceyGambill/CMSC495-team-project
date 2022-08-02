import pytest
import time
import WebScraper

# Test scrape_url function
def test_scrape_url_type():
        scrape_test = WebScraper.scrape_url("https://www.linkedin.com/jobs/search/?geoId=107024810&keywords=software%20engineer&location=Everett%2C%20Washington%2C%20United%20States")
        assert type(scrape_test) == dict

# Test scrape_url function
def test_scrape_url_dict_not_empty():
    scrape_test = WebScraper.scrape_url("https://www.linkedin.com/jobs/search/?geoId=107024810&keywords=software%20engineer&location=Everett%2C%20Washington%2C%20United%20States")
    assert len(scrape_test) != 0

# Test main function
    def test_main_performance(self):
        start = time.time()
        WebScraper.main()
        end = time.time()
        performance_time = start - end
        assert performance_time < .01