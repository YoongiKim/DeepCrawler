from DeepCrawler.Crawler import CRAWLER

class SAMPLER():
    def __init__(self):
        # Initialize Sampler
        self.crawler = CRAWLER(['NaverBlog','Google'],['햄버거래시피','샐러드래시피'],10,5)
        self.crawler.run()