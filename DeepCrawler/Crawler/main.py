import threading
import time

class CRAWLER():
    def __init__(self,n_threads=4):
        # Constant Variables
        # Setup Variables
        self.platform = {} # list of platforms
        self.query = "" # list of query to search
        self.n_data = 0 # number of datasets(pages) to get
        self.n_threads = n_threads # Number of threads when crawling

        self.isCrawling = False

    def set(self,query,n_data,platform):
        self.platform = platform  # list of platforms
        self.query = query  # list of query to search
        self.n_data = n_data  # number of datasets(pages) to get

    def crawling_process(self,task):
        platform = task["platform"] # Platform
        query = task["query"] # Query
        n_data = task["n_data"] # Number of Data Wanted
        current_num = 1 # Current Data Number

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
                task.append([{"platform":keys,
                              "query":self.query,
                              "n_data":self.n_data}])
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
