

class Scraper:
    def __init__(self, browser):
        self.browser = browser



def SeleniumTest():
    # url = settings.BASE_LINK_REDDIT_AITAH
    # scraper_browser = Scraper(Browser.get_browser()).browser
    xpath = "/html/body/shreddit-app/dsa-transparency-modal-provider/div/div[1]/div/main/shreddit-post/div[2]/div"
    # scraper_browser.get(url)
    # firstQuestion = scraper_browser.find_element("xpath",xpath).text
    # print(firstQuestion)
    # scraper_browser.close()