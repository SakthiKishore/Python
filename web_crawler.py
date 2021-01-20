import requests
from bs4 import BeautifulSoup
import time
import concurrent.futures

class Crawl():
    def __init__(self, url):
        self.url = url
    
    def get_local_links(self):

        """Returns the links belonging to the same domain(first party) present on the page""" 

        local_links = set()
        with requests.Session() as req: 
            html_text = req.get(self.url).text
            soup = BeautifulSoup(html_text, 'html.parser')
            for link in soup.find_all('a', href=True):
                anchor_tag = link.get('href')
                if anchor_tag.startswith('/'):
                    local = self.url + anchor_tag
                    local_links.add(local)   
                else:
                    continue
        list_local_links = list(local_links)
        print('====' * 30)
        print(f'Found {len(list_local_links)} same domain pages at ==> {self.url}. Details below')
        print('====' * 30)
        return list_local_links

    def get_all_links(self, url):

        """Returns all the links (1st + 3rd party) present on the page"""     

        with requests.Session() as req: 
            html_text = req.get(url).text
            soup = BeautifulSoup(html_text, 'html.parser')
            every_link = set()
            for link in soup.find_all('a', href=True):
                anchor_tag = link.get('href')
                if anchor_tag.startswith('/'):
                    local_link = url + anchor_tag
                    every_link.add(local_link)   
                elif anchor_tag.startswith('#'):
                    continue
                else:
                    every_link.add(anchor_tag)
            list_every_link = list(every_link)
        list_every_link = '\n'.join(list_every_link)  
        result = f'\n ================================================ \n "{url}" has the following links : \n ================================================ \n\n {list_every_link}'
        return result
    
    def quick(self, urls):

        """Uses Multithreading to call get_all_links() function for all URLs in the input list""" 

        with concurrent.futures.ThreadPoolExecutor() as executor:
            final = [executor.submit(self.get_all_links, u) for u in urls]
            for i in concurrent.futures.as_completed(final):
                print(i.result())


if __name__ == "__main__":
    start_time = time.time()
    website = Crawl("https://monzo.com")
    page_links = website.get_local_links()
    website.quick(page_links)
    print(f"\n\nFinished in {time.time() - start_time} seconds")
