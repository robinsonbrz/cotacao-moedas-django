import time
from test.functional_tests.naveg import make_chrome_browser

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By


class Cotacao_moeda_funcional_test(StaticLiveServerTestCase):
    def sleep(self, seconds=5):
        time.sleep(seconds)

    def test_the_test(self):
        make_chrome_browser()
        browser = make_chrome_browser()
        browser.get(self.live_server_url)
        self.sleep(3)
        body = browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('Campo moeda vazio', body.text)
        browser.quit()



