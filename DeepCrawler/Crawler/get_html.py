import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from urllib.parse import quote
from Crawler.platforms import Platforms

def get_post_links(platform, keyword, page_num):
    browser = webdriver.Chrome()

    keyword_encode = quote(keyword)

    if platform == Platforms.GOOGLE:
        pass

    elif platform == Platforms.NAVER_BLOG:
        link = "https://section.blog.naver.com/Search/Post.nhn?pageNo={}&rangeType=ALL&orderBy=sim&keyword={}"\
            .format(page_num, keyword_encode)

        browser.get(link)

    time.sleep(1)

    elem = browser.find_element_by_tag_name("body")

    posts = browser.find_elements(By.XPATH, '//a[@class="desc_inner"]')

    links = []

    for post in posts:
        links.append(post.get_attribute("href"))

    browser.close()

    return links

def get_html(platform, post_link):
    browser = webdriver.Chrome()
    browser.get(post_link)
    time.sleep(1)

    elem = browser.find_element(By.XPATH, '//iframe[@id="mainFrame"]')

    if platform == Platforms.GOOGLE:
        pass

    elif platform == Platforms.NAVER_BLOG:
        for i in range(60):
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.2)

    print(elem)

if __name__ == '__main__':
    links = get_post_links(Platforms.NAVER_BLOG, '김밥', 1)

    get_html(Platforms.NAVER_BLOG, links[0])
