from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import config
import time
import sys

crawled_links = []
site_map = dict()

options = Options()
options.headless = True
driver = webdriver.Chrome(executable_path=config.CHROMEDRIVER_PATH, options=options)


def crawl_link(link):
    print(link)
    scraped_links = []
    driver.get(link)

    time.sleep(1)

    a_tags_in_html = driver.find_elements_by_xpath(config.XPATH_SELECTOR)

    for a_tag in a_tags_in_html:
        temp_link = str(a_tag.get_attribute(config.ATTRIBUTE_TO_EXTRACT))
        if config.DOMAIN_NAME in temp_link and temp_link not in scraped_links and not temp_link.startswith(config.DISALLOWED_PREFIX):
            scraped_links.append(temp_link)
            print(config.TAB_CHARACTER + temp_link)
        else:
            pass

    crawled_links.append(link)
    site_map[link] = scraped_links

    for scraped_link in scraped_links:
        if scraped_link not in crawled_links:
            crawl_link(scraped_link)


try:
    crawl_link(config.URL_TO_CRAWL)
    print(crawled_links)
    # print(site_map)
except:
    print(config.ERROR_MESSAGE_CRAWLING + sys.exc_info()[0])

driver.quit()
