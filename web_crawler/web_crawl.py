#!/usr/bin/env python3

"""
Author : Sakthi Kishore <sendtokishore.3@gmail.com>
Purpose: Scrape website to return various types of links present

"""

import requests
from bs4 import BeautifulSoup
import time
import concurrent.futures


class Crawl():

    def get_local_links(self, url):

        """
        Takes in a url and returns the links belonging to the same domain(first party) present on the page
        
        Args:
            url (str): This is the website name(eg: http://google.com)
           
        Returns: 
            set : A set of URLs belonging to same domain

        """ 

        local_links = set()
        with requests.Session() as req: 
            html_text = req.get(url).text
            soup = BeautifulSoup(html_text, 'html.parser')
            for link in soup.find_all('a', href=True):
                anchor_tag = link.get('href')
                if anchor_tag.startswith(('/', '#')):
                    local = url + anchor_tag
                    local_links.add(local)
        print('====' * 30)
        print(f'Found {len(local_links)} same domain pages at ==> {url}. Details below')
        print('====' * 30)
        return local_links

    def get_all_links(self, url):

        """
        Takes in a url and returns all links (1st + 3rd party) present on the page
        
        Args:
            url (str): This is a single url of one of the pages of the website 
                        (eg: http://google.com/careers or http://google.com/aboutus)

        Returns:
            list : returns a formatted string which includes all the links present on the page   

        """     

        with requests.Session() as req: 
            html_text = req.get(url).text
            soup = BeautifulSoup(html_text, 'html.parser')
            every_link = []
            for link in soup.find_all('a', href=True):
                anchor_tag = link.get('href')
                if anchor_tag.startswith(('/', '#')):
                    local_link = "https://monzo.com" + anchor_tag
                    every_link.append(local_link)   
                else:
                    every_link.append(anchor_tag)
        list_every_link = '\n'.join(every_link)  
        result = f'================================================ \n"{url}" has the following links : \n================================================ \n\n{list_every_link}'
        return result
    
    def quick_get(self, urls):

        """
        Uses Multithreading to call get_all_links() function for all URLs in the input list and prints 
        the result for each URL as soon as the thread on which the request URL was running gets completed.
        
        Args:
            urls (list): List of local URLs returned from get_local_links()
        
        Returns:
            prints out the formatted string containing links returned from get_all_links()
        
        """ 
        with concurrent.futures.ThreadPoolExecutor() as executor:
            final = [executor.submit(self.get_all_links, u) for u in urls]
            for i in concurrent.futures.as_completed(final):
                print(i.result())


if __name__ == "__main__":

    start_time = time.time()
    website = Crawl()
    page_links = website.get_local_links("https://monzo.com")
    website.quick_get(page_links)
    print(f"\nFinished in {time.time() - start_time} seconds")

    