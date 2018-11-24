class CRAWLER():
    def __init__(self,platform,query,num):
        # Constant Variables
        # TODO Change this when adding platform
        self.validplatforms = ['NaverBlog','Google']
        # Setup Variables
        self.platform = platform # list of platforms
        self.query = query # list of query to search
        self.num = num # number of datasets(pages) to get

        # Platform validation check
        assert self.platformValidation_check(self.platform), 'Platform list contains invalid platform names'

    def run(self):
        # Start Crawling
        print('Crawler Run')
        print('Query:{}||Platform:{}||NumberofData:{}'.format(self.query,self.platform,self.num))

    def platformValidation_check(self,platform):
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