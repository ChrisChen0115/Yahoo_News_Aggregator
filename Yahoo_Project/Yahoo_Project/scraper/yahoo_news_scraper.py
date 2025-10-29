from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

def yahoo_scraper():
    service =  Service(executable_path='D:/chromedriver-win64/chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.get("https://tw.news.yahoo.com/")
    time.sleep(3)

    # find target ul
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    target_ul = soup.find("ul", class_="H(100%) D(ib) Mstart(24px) W(32.7%)")
    
    if target_ul:
        articles = target_ul.select("li[class*='Pos(r)']")
        news_list = []
        # get news titles and links
        for t in articles:
            title_tag = t.find("a")
            if not title_tag:
                continue
            title = title_tag.text.strip()
            link = title_tag["href"]

            # get published time
            published_at = ""
            try:
                driver.get(link)
                time.sleep(3)

                inner_soup = BeautifulSoup(driver.page_source, 'html.parser')
                time_element = inner_soup.find("time")
                if time_element:
                    published_at = time_element.text.strip()
                else:
                    published_at = "Publish time not found."
            
            except Exception as e:
                print(f'Error message : {e}')

            # avoid duplicate news
            if t not in news_list:
                news_list.append({
                "title" : title,
                "link" : link,
                "published_at" : published_at
            })
    
    driver.quit()
    return news_list