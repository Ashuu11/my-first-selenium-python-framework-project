import pytest
from utilities.utils import Utils
from pages.yatra_launch_page import LaunchPage
import softest
from ddt import ddt, data, unpack, file_data


@pytest.mark.usefixtures("setUp")
@ddt
class TestSearchAndVerifyFilter(softest.TestCase):
    log = Utils.custom_logger()

    @pytest.fixture(autouse=True)
    def class_setUp(self):
        self.lp = LaunchPage(self.driver)
        self.ut = Utils()

    # @data(("New Delhi", "BBI", "24/02/2024", "1 Stop"), ("Mumbai", "CCU", "28/02/2024", "2 Stop"))
    # @unpack
    @file_data("../testdata/test_data.json")
    # @file_data("../testdata/test_data.yaml")
    # @data(*Utils.read_from_excel("C:\\Python-Selenium\\LearnPyTest\\TestFrrameworkDemo\\testdata\\tdataexcel.xlsx", "Sheet1"))
    # @unpack
    # @data(*Utils.read_from_csv("C:\\Python-Selenium\\LearnPyTest\\TestFrrameworkDemo\\testdata\\test_datacsv.csv"))
    # @unpack
    def test_search_flights_1_stop(self, goingfrom, goingto, departdate, stops):
        search_flight_results = self.lp.searchFlights(goingfrom, goingto, departdate)
        self.lp.page_scroll()
        search_flight_results.filter_flight_by_stop(stops)
        all_stops1 = search_flight_results.get_search_flight_results()
        self.log.info(len(all_stops1))
        self.ut.assertListItem(all_stops1, stops)
