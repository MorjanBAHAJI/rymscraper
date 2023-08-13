import logging
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import random
logger = logging.getLogger(__name__)


class RymBrowser(webdriver.Firefox):
    def __init__(self, headless=True):
        logger.debug("Starting Selenium Browser : headless = %s", headless)
        self.options = Options()
        if headless:
            self.options.add_argument('-headless')

        webdriver.Firefox.__init__(self, options=self.options)

    def restart(self):
        self.quit()
        webdriver.Firefox.__init__(self, options=self.options)

    def get_url(self, url):
        logger.debug("get_url(browser, %s)", url)
        while True:
            self.get(str(url))
            class_to_click_on = [
                {"class": "as-oil__btn-optin", "id": None, "num_clicks": 1},  # cookie bar
                {"class":"fc-cta-consent", "id": None, "num_clicks":1},  # consent popup
                {"class": "view_more", "id": "view_more_new_releases_all", "num_clicks": 4}
            ]
            for class_button in class_to_click_on:
                for num_clicks in range(class_button["num_clicks"]):
                    sleep_t = round(random.uniform(0.2, 1.0),2)
                    logger.debug(f"Sleep for {sleep_t} seconds")
                    time.sleep(sleep_t)
                    elements = self.find_elements(By.CLASS_NAME, class_button["class"])
                    if len(elements)==1:
                        logger.debug(f"{class_button['class']} found. Clicking on it.")
                        elements[0].click()
                    elif len(elements)==0:
                        logger.debug(f"{class_button['class']} cannot be found")
                    else:
                        elements=[el for el in elements if el.get_attribute("id")==class_button["id"]]
                        if len(elements)==0:
                            logger.debug(f"{class_button['class']} found, but corresponding id: {class_button['id']} cannot be found..")
                        elif len(elements)==1:
                            logger.debug(f"{class_button['class']} found with corresponding id: {class_button['id']} . Clicking on it.")
                            elements[0].click()
                        else:
                            logger.debug(f"{class_button['class']} found with corresponding id: {class_button['id']}, but multiple elements...click ignored")

            if len(self.find_elements(By.CLASS_NAME, "disco_expand_section_link")) > 0:
                try:
                    for index, link in enumerate(
                        self.find_elements(By.CLASS_NAME, "disco_expand_section_link")
                    ):
                        self.execute_script(
                            f"document.getElementsByClassName('disco_expand_section_link')[{index}].scrollIntoView(true);"
                        )
                        link.click()
                        time.sleep(0.2)
                except Exception as e:
                    logger.debug('No "Show all" links found : %s.', e)
            # Test if IP is banned.
            if self.is_ip_banned():
                self.quit()
                raise Exception("IP banned from rym. Can't do any requests to the website. Exiting.")
            # Test if browser is rate-limited.
            if self.is_rate_limited():
                logger.error("Rate-limit detected. Restarting browser.")
                self.restart()
            else:
                break
        return

    def get_soup(self):
        return BeautifulSoup(self.page_source, "html.parser")

    def is_ip_banned(self):
        logger.debug("soup.title : %s", self.get_soup().title)
        return self.get_soup().title.text.strip() == "IP blocked"

    def is_rate_limited(self):
        return self.get_soup().find("form", {"id": "sec_verify"})
