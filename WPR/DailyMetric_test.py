from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class DailyMetric_test():
    def test_setup(self):
        global driver
        driver = webdriver.Chrome('P://IT Transformation -Automation//WPR//WPR//ChromeDriver//chromedriver.exe')
        driver.implicitly_wait(3)
        driver.maximize_window()
        time.sleep(2)
        # Open the application
        driver.get("https://qa-wpr.rxresourcesolutions.com/")
        print(driver.title)
        time.sleep(7)

    def test_primaryMetric(self):
        facility_click = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id = 'txtfacility']"))
        )
        driver.execute_script("arguments[0].click();", facility_click)
        driver.find_element_by_id("txtfacility").send_keys(' Sparrow Lansing  - 1193 ')
        driver.find_element_by_xpath("//*[@id = 'txtfacility']").click()
        facility_element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//span[text() = ' Sparrow Lansing  - 1193 ']"))
        )
        driver.execute_script("arguments[0].click();", facility_element)
        time.sleep(2)

        # Navigate to Daily Metric
        driver.find_element_by_xpath("//span[text() =' Data Management ']").click()
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button//span[text() ='Daily Metric']"))
        )
        driver.execute_script("arguments[0].click();", element)
        time.sleep(2)

        emptyprimarytext = driver.find_element_by_xpath("//*[@id = 'mat-select-0']").text
        print(emptyprimarytext)

        #Select Primary Metric
        driver.find_element_by_xpath("//span[text() = 'Patient Days (actual - excluding newborns) - PD']").click()
        time.sleep(3)
        primaryMetric_element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//span[text() = ' Patient Days (actual - excluding newborns) - PD ']"))
        )
        driver.execute_script("arguments[0].click();", primaryMetric_element)
        time.sleep(2)
        driver.find_element_by_xpath("//*[text()=' Customize Primary Description']").click()
        time.sleep(4)
        driver.find_element_by_xpath("//span/label/*[text() = 'WPR Primary Custom Description']//ancestor::div/input").send_keys("descp1")
        driver.find_element_by_xpath("//*[text() = 'Adjust Primary Metric']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[text() = 'With Carveout ']").click()
        time.sleep(2)

    # Select secondary Metric
    def test_secondaryMetric(self):

        driver.find_element_by_xpath("//*[text()='Use Secondary Metric ']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//span[text()='Adjust Secondary Metric']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[text() = 'With Carveout ']/preceding-sibling::div").click()
        time.sleep(1)
        driver.find_element_by_xpath("//span[text() = 'Combine with Primary during Process Month End']").click()
        time.sleep(2)

        driver.find_element_by_xpath("//span[text()=' Update Daily Metric ']").click()
        time.sleep(2)

    # Assertion
    # verify PrimaryMetric
    def test_verifyPrimaryMetric(Self):
        driver.get("https://qa-wpr.rxresourcesolutions.com/")
        print(driver.title)
        time.sleep(7)

        driver.find_element_by_xpath("//*[@id = 'txtfacility']").click()
        driver.find_element_by_id("txtfacility").send_keys(' Sparrow Lansing  - 1193 ')
        driver.find_element_by_xpath("//*[@id = 'txtfacility']").click()
        facility_element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//span[text() = ' Sparrow Lansing  - 1193 ']"))
        )
        driver.execute_script("arguments[0].click();", facility_element)
        time.sleep(2)

        # Navigate to Daily Metric
        driver.find_element_by_xpath("//span[text() =' Data Management ']").click()
        element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//button//span[text() ='Daily Metric']"))
        )
        driver.execute_script("arguments[0].click();", element)
        time.sleep(2)

        # To Get primary metric
        primarymetric = driver.find_element_by_xpath("//*[@id = 'mat-select-0']").text
        print(primarymetric)
        return primarymetric

    # To Get secondary metric
    def test_verifySecondaryMetric(Self):
        # secondarymetric = driver.find_element_by_xpath("//*[@id ='mat-select-1']").text
        secondarymetric = driver.find_element_by_xpath("//*[text()='CMI Total Hospital - CMI']/ancestor::div[3]").text
        print(secondarymetric)
        return secondarymetric

        # To check custom secondary Desc
        customCheckboxIsSelected = driver.find_element_by_xpath("//*[@id='mat-checkbox-5-input']").is_selected()
        print(customCheckboxIsSelected)
        time.sleep(2)

        # To get secondary Desc
        primaryCustomDesc = driver.find_element_by_xpath("//input[@id='mat-input-4']").text
        print(primaryCustomDesc)

    #Reset PrimaryMetric
    def test_primaryMetricReset(self):
        facility_click = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id = 'txtfacility']"))
        )
        driver.execute_script("arguments[0].click();", facility_click)
        driver.find_element_by_xpath("//*[@id = 'txtfacility']").click()
        facility_element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//span[text() = ' Sparrow Lansing  - 1193 ']"))
        )
        driver.execute_script("arguments[0].click();", facility_element)
        time.sleep(2)

        # Navigate to Daily Metric
        driver.find_element_by_xpath("//span[text() =' Data Management ']").click()
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button//span[text() ='Daily Metric']"))
        )
        driver.execute_script("arguments[0].click();", element)
        time.sleep(2)

        emptyprimarytext = driver.find_element_by_xpath("//*[@id = 'mat-select-0']").text
        print(emptyprimarytext)

        driver.find_element_by_xpath("//*[text()=' Customize Primary Description']").click()
        time.sleep(4)

        driver.find_element_by_xpath("//*[text() = 'Adjust Primary Metric']").click()
        time.sleep(2)


    #Reset secondary Metric
    def test_secondaryMetricReset(self):
        time.sleep(2)
        driver.find_element_by_xpath("//*[text()='Use Secondary Metric ']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//span[text()=' Update Daily Metric ']").click()

     # To check custom Primary Desc
    def test_verifyCustomizePrimaryDescrption(Self):
        customCheckboxIsSelected = driver.find_element_by_xpath("//*[@id='mat-checkbox-2-input']").is_selected()
        print(customCheckboxIsSelected)
        time.sleep(2)

        #To get Primary Desc
        primaryCustomDesc = driver.find_element_by_xpath("//input[@id='mat-input-3']").text
        print(primaryCustomDesc)

    # To Check Adjust Primary Metric
    def test_verifyAdjustPrimaryMetric(Self):
        adjustPrimaryMetric = driver.find_element_by_xpath("//*[@id = 'mat-checkbox-3-input']").is_selected()
        print(adjustPrimaryMetric)
        time.sleep(1)
        return adjustPrimaryMetric

    # To Check Primary With Carveout
    def test_verifyPrimaryWithCarveout(Self):

        primaryWithCarveout = driver.find_element_by_xpath("//*[@id = 'mat-checkbox-6-input']").is_selected()
        print(primaryWithCarveout)
        return primaryWithCarveout



    def test_verifyAdjustSecondaryMetric(Self):
        #To Check Adjust secondary Metric
        adjustSecondaryMetric = driver.find_element_by_xpath("//*[@id = 'mat-checkbox-5-input']").is_selected()
        print(adjustSecondaryMetric)
        time.sleep(1)
        return adjustSecondaryMetric

    def test_verifysecondaryWithCarveout(Self):
        #To Check secondary With Carveout
        secondaryWithCarveout = driver.find_element_by_xpath("//*[@id = 'mat-checkbox-7-input']").is_selected()
        print(secondaryWithCarveout)
        return secondaryWithCarveout

    def test_closeWindow(self):
        driver.quit()

