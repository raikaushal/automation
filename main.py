import time
from src.utils import Utils
from src.web_driver import WebDriver
from src.automation import Automation


def main():
    """Entrypoint Function"""
    # create chrome driver instance
    web_driver = WebDriver()
    driver = web_driver.get_driver()

    # utility function
    utils = Utils()

    # ceate automation instance
    automation = Automation(driver)

    # login to page using crdentials
    automation.login()

    # read excel to get ration card data
    rc_data_list = utils.read_excel()

    # iterate through each row
    for rc_data in rc_data_list:
        member_found = automation.search_member(rc_data)
        if not member_found:
            continue
        automation.switch_to_next_window()
        automation.check_for_member_with_no_adhaar()
        automation.proceed_for_upload_file_and_deletion(rc_data)
        time.sleep(2)
        automation.close_current_window()
        time.sleep(2)


if __name__ == "__main__":
    main()
