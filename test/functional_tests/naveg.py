from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ROOT_PATH = Path(__file__).parent.parent.parent
CHROMEDRIVER_NAME = 'chromedriver'
CHROMEDRIVER_PATH = ROOT_PATH / 'utils' / CHROMEDRIVER_NAME



def make_chrome_browser(*options):
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)
    # headless para não abrir - roda em segundo plano
    chrome_options.add_argument('--headless')
    chrome_service = Service(executable_path=CHROMEDRIVER_PATH)
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return browser


if __name__ == '__main__':
    
    # browser = make_chrome_browser('--headless')
    browser = make_chrome_browser()
    browser.get('https://www.enedino.com.br/')
    sleep(5)
    browser.quit()
