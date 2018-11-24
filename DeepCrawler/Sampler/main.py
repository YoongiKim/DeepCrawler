from Crawler import CRAWLER

class SAMPLER():
    def __init__(self):
        # Initialize Sampler
        self.crawler = CRAWLER(['NaverBlog'],['래시피'],3)
        self.crawler.run()