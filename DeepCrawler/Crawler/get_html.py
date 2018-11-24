import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from urllib.parse import quote
from Crawler.platforms import Platforms
import platform
import os
import sys

class GetHTML:
    def __init__(self):
        executable = ''

        if platform.system() == 'Windows':
            print('Detected OS : Windows')
            executable = './chromedriver/chromedriver_win.exe'
        elif platform.system() == 'Linux':
            print('Detected OS : Linux')
            executable = './chromedriver/chromedriver_linux'
        elif platform.system() == 'Darwin':
            print('Detected OS : Darwin')
            executable = './chromedriver/chromedriver_mac'
        else:
            assert False, 'Unknown OS Type'

        print(executable)
        self.browser = webdriver.Chrome(executable)

    def get_post_links(self, platform, keyword, page_num):
        keyword_encode = quote(keyword)

        if platform == Platforms.GOOGLE:
            pass

        elif platform == Platforms.NAVER_BLOG:
            link = "https://section.blog.naver.com/Search/Post.nhn?pageNo={}&rangeType=ALL&orderBy=sim&keyword={}" \
                .format(page_num, keyword_encode)

            self.browser.get(link)

        time.sleep(1)

        elem = self.browser.find_element_by_tag_name("body")

        posts = self.browser.find_elements(By.XPATH, '//a[@class="desc_inner"]')

        links = []

        for post in posts:
            links.append(post.get_attribute("href"))

        return links

    def get_html(self, platform, post_link):
        self.browser.get(post_link)
        time.sleep(1)

        if platform == Platforms.GOOGLE:
            pass

        elif platform == Platforms.NAVER_BLOG:
            frame = self.browser.find_element(By.XPATH, '//iframe[@id="mainFrame"]')

            for i in range(60):
                frame.send_keys(Keys.PAGE_DOWN)
                time.sleep(0.2)

            htmls = self.browser.find_elements_by_tag_name('html')
            print(htmls[-1].get_attribute('innerHTML'))

if __name__ == '__main__':
    get_html = GetHTML()
    links = get_html.get_post_links(Platforms.NAVER_BLOG, '김밥', 1)

    get_html.get_html(Platforms.NAVER_BLOG, links[0])
