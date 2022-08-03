import pytest
import time
import WebScraper

link = "https://www.linkedin.com/jobs/search/?geoId=107024810&keywords=software%20engineer&location=Everett%2C%20Washington%2C%20United%20States"

##########****** Functional tests ******#############

# Test scrape_url function
def test_scrape_url_type():
    scrape_test = WebScraper.scrape_url(link)
    assert type(scrape_test) == dict

# Test scrape_url function
def test_scrape_url_dict_not_empty():
    scrape_test = WebScraper.scrape_url(link)
    assert len(scrape_test) != 0

# Test text function for return type
def test_text_function_for_return_type():
    text_test_value = WebScraper.text(link)
    assert type(text_test_value) == dict

##########****** Performance tests ******#############

# Test performance of text function
def test_text_function_performance():
    start = time.time()
    WebScraper.text(link)
    end = time.time()
    performance_time = start - end
    assert performance_time < .01

# Test performance of scrape_url function
def test_scrape_url_function_performance():
    start = time.time()
    WebScraper.scrape_url(link)
    end = time.time()
    performance_time = start - end
    assert performance_time < .01

# Test pefformance of main function
def test_main_performance():
    start = time.time()
    WebScraper.main()
    end = time.time()
    performance_time = start - end
    assert performance_time < .01