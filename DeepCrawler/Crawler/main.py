import threading
from .get_html import GetHTML
from queue import Queue
from .platforms import Platforms
import json
import os

class CRAWLER():
    def __init__(self,n_threads=4,saving_dir="./Results/"):
        # Constant Variables
        # Setup Variables
        self.platform = {} # list of platforms
        self.query = "" # list of query to search
        self.n_data = 0 # number of datasets(pages) to get
        self.n_threads = n_threads # Number of threads when crawling
        self.saving_dir = saving_dir

        self.isCrawling = False
        self.progress={}

    def set(self,query,n_data,platform):
        self.platform = platform  # list of platforms
        self.query = query  # list of query to search
        self.n_data = n_data  # number of datasets(pages) to get
        for key in self.platform.keys():
            self.progress[key] = 0 # 0 Data Collected so far fo each platform

    def crawling_process(self,task):
        platform = task["platform"] # Platform
        query = task["query"] # Query
        n_data = task["n_data"] # Number of Data Wanted
        page_num = 1

        scraper = GetHTML() # Create Get HTML and configure
        linkQueue = Queue()

        # If progress is smaller than number of data needed
        while self.progress[platform] < n_data:
            # If isCrawling is False stop
            if not self.isCrawling:
                scraper.browser.quit()
                break
            # If no link get link and put into linkQueue
            if linkQueue.empty():
                for link in scraper.get_post_links(
                        Platforms.toInt(platform),query,page_num):
                    linkQueue.put(link)
                page_num += 1

            # Get link from link Queue
            current_link = linkQueue.get()
            # Get Html
            current_html = scraper.get_html(Platforms.toInt(platform),current_link)
            self.saveFile(task,current_html)
            # Done Collection Data
            self.progress[platform] += 1

        print("Crawler Stopped")

    def crawl(self):
        threads = []
        task = self.generate_task()
        # Start Task
        for task in task:
            t = threading.Thread(target=self.crawling_process,args=(task,))
            threads.append(t)
            t.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

    def saveFile(self,task,text):
        curr_dir = self.saving_dir+task["query"]+"/"+task["platform"]
        if not os.path.isdir(curr_dir):
            os.makedirs(curr_dir)

        if os.path.exists(curr_dir+"/config.json"):
            with open(curr_dir+"/config.json") as json_file:
                config = json.load(json_file)
        else:
            config = {
                "task" : task,
                "index" : 1
            }
        print(config)
        file = open(curr_dir+"/"+str(config["index"]),"w")
        file.write(text)
        file.close()

        config["index"] += 1
        with open(curr_dir+"/config.json", 'w') as config_outfile:
            json.dump(config, config_outfile)

    # Main Run Method to activate crawler. Call this to Start Crawling
    def start(self):
        assert not self.isSettingValid(), "Invalid Setting"
        # Set isCrawling Indicator to True
        self.isCrawling = True
        # Do Crawling
        self.crawl()

    def stop(self):
        self.isCrawling = False

    def generate_task(self):
        task = []
        for keys in self.platform.keys():
            if self.platform[keys] == 1:
                task.append({"platform":keys,
                              "query":self.query,
                              "n_data":self.n_data})
        return task

    def isPlatformSet(self):
        isready = False
        for key in self.platform.keys():
            if self.platform[key] == 1:
                isready = True
                break
        return isready

    def isSettingValid(self):
        result = False
        # Check for invalid setting
        if self.query == "":
            result = True
        if self.n_data <= 0:
            result = True
        if not self.isPlatformSet():
            result = True
        return result
