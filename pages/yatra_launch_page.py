import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pages.search_flights_results import SearchFlightResults
from base.base_driver import BaseDriver
from utilities.utils import Utils


class LaunchPage(BaseDriver):
    log = Utils.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD = "//input[@id='BE_flight_arrival_city']"
    GOING_TO_FIELD_LIST = "//div[@class='viewport']//div[1]/li"
    SELECT_DATE_FIELD = "//input[@id='BE_flight_origin_date']"
    ALL_DATES_FIELD = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    SEARCH_BUTTON = "//input[@value='Search Flights']"


    def getdepartFromField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DEPART_FROM_FIELD)

    def enterdepartFromLocation(self, departlocation):
        self.getdepartFromField().click()
        self.getdepartFromField().send_keys(departlocation)
        self.getdepartFromField().send_keys(Keys.ENTER)


    def getgoingtoField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GOING_TO_FIELD)

    def getgoingtoResults(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.GOING_TO_FIELD_LIST)


    def enterdeparttoLocation(self, goingtolocation):
        self.getgoingtoField().click()
        self.log.info("Clicked on Going to")
        time.sleep(3)
        self.getgoingtoField().send_keys(goingtolocation)
        self.log.info("Typed Text into going to Field Successfully")
        time.sleep(2)
        search_results = self.getgoingtoResults()
        for results in search_results:
            self.log.info(results.text)
            if goingtolocation in results.text:
                results.click()
                time.sleep(4)
                break


    def getDepatureDateField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SELECT_DATE_FIELD)

    def getAllDatesField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ALL_DATES_FIELD)


    def enterDepartureDate(self, departdate):
        self.getDepatureDateField().click()
        alldates_ = self.getAllDatesField().find_elements(By.XPATH, self.ALL_DATES_FIELD)
        for date in alldates_:
            if date.get_attribute("data-date") == departdate:
                date.click()
                break

    def getSearchButton(self):
        return self.driver.find_element(By.XPATH, self.SEARCH_BUTTON)

    def clickSearchButton(self):
        self.getSearchButton().click()
        time.sleep(4)


    def searchFlights(self, departfromlocation, goingtolocation, departdate):
        self.enterdepartFromLocation(departfromlocation)
        self.enterdeparttoLocation(goingtolocation)
        self.enterDepartureDate(departdate)
        self.clickSearchButton()
        search_flights_result = SearchFlightResults(self.driver)
        return search_flights_result
