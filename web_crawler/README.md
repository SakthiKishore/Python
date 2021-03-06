# Web Crawler

Web Crawler is a Python script for scraping websites and listing out the links present on each page of the website.

## Contents

1. ### `web_crawl.py`

For a given website, this script first finds all the pages present in the website belonging to the same domain. It then visits each of those pages and prints out the page visited and all the links present in that page.

2. ### `test_web_crawl.py`

Unittests to check 

* If the files need to run the test are present.
* If the function to return ONLY the local links works as expected
* If the function to return ALL the links works as expected

3. ### `fake_response.txt`

Contains a sample of http response with a few //a//href tags in text format. Used as mock input for unittest get requests.

4. ### `output_from_fn.txt`

File to write the output returned by the called function

5. ### `expected.txt`

File contains expected function output. Used to compare with the output returned from the function.

## Installation

**Mac OS X**: A version of Python is already installed.  
**Windows**: You will need to install one of Python 3.x versions available at [python.org](http://www.python.org/getit/).

## Dependencies

The script requires the following Python packages and libraries to be imported to run successfully.

* requests

* beautifulsoup4 (bs4)

* time

* concurrent.futures

* unittest

* requests_mock

* os


## General usage information

1. Download the ZIP package and unzip it.
2. 
 * The script will run by simply typing `python ` followed by the file name of the script, e.g. `python web_crawler.py`.
 * If the script is in a different directory from which you are trying to run it, you will need to provide the full path to the script’s file, e.g. `python /Users/myself/foldername/web_crawler.py`.
