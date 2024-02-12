import logging
import time
from selenium.webdriver.common.by import By
from utilities.utils import Utils
from base.base_driver import BaseDriver


class SearchFlightResults(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.WARNING)

    def __int__(self, driver):
        super.__init__(driver)
        self.driver = driver


    # Locators
    FILTER_BY_1_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='1']"
    FILTER_BY_2_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='2']"
    FILTER_BY_NON_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='0']"
    SEARCH_FLIGHT_RESULTS = "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]"


    def get_filter_by_one_stop(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_1_STOP_ICON)

    def get_filter_by_two_stop(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_2_STOP_ICON)

    def get_filter_by_non_stop(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_NON_STOP_ICON)

    def get_search_flight_results(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.SEARCH_FLIGHT_RESULTS)

    def filter_flight_by_stop(self, by_Stop):
        if by_Stop == "1 Stop":
            self.get_filter_by_one_stop().click()
            self.log.warning("Selected Flight with 1 stop")
            time.sleep(2)
        elif by_Stop == "2 Stop":
            self.get_filter_by_two_stop().click()
            self.log.warning("Selected Flight with 2 stops")
            time.sleep(2)
        elif by_Stop == "Non Stop":
            self.get_filter_by_non_stop().click()
            self.log.warning("Selected Flight with Non stops")
            time.sleep(2)
        else:
            self.log.warning("Please provide a valid Stop detail")

