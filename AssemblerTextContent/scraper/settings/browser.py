from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



def get_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito");
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    return options



class Browser:

    def get_browser():
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        return browser
