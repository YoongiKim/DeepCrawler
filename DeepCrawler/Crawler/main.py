from . import collectData
from multiprocessing import Pool

class CRAWLER():
    def __init__(self,platform,query,n_data,n_thread=4):
        # Constant Variables
        # TODO Change this when adding platform
        self.validplatforms = ['NaverBlog','Google']
        # Setup Variables
        self.platform = platform # list of platforms
        self.query = query # list of query to search
        self.n_data = n_data # number of datasets(pages) to get
        self.n_thread = n_thread # number of threads

        # Platform validation check
        assert self.platformValidity_check(self.platform), 'Platform list contains invalid platform names'
                
        # Store crawled data (number of platform,number of data for each platform)
        self.result = {}
        for p in self.platform:
            self.result[p] = []

    def download(self,task):
        # TODO download process
        print(task)

    # Main Run Method to activate crawler. Call this to Start Crawling
    def run(self):
        print('Query:{}||Platform:{}||data_num:{}||thread_num:{}'.format(self.query,self.platform,self.n_data,self.n_thread))
        # Start Crawling with MultiProcess
        pool = Pool(self.n_thread)
        # TODO pass proper iterable task
        pool.map_async(self.download,[1,2,3,4])
        pool.close()
        pool.join()

    # Return if platform list is valid or not
    def platformValidity_check(self,platform):
        validity = True
        for p in platform:
            for v in self.validplatforms:
                temp = False
                if p == v:
                    temp = True
                    break
            if temp == False:
                validity = False
                break
        return validity