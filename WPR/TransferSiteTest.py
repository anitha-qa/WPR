from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from WPR.DBConnector import DBConnector_test
import time
import random

class transferSite_test():
    def Enviornment(self):
        global driver;
        global transfersitename;
        global transferSiteIdentifier;
        global increment;
        global increment1;
        driver = webdriver.Chrome('P://IT Transformation -Automation//WPR//WPR//ChromeDriver//chromedriver.exe')
        driver.implicitly_wait(1)
        driver.maximize_window()
        increment = random.randrange(0, 100000)
        increment1 = random.randrange(0, 100000)
        transfersitename = "e2e" + str(format(increment, '02'))
        transferSiteIdentifier = "e2e" + str(format(increment1, '02'))
        driver.get("https://qa-wpr.rxresourcesolutions.com/")
        print(driver.title)
        time.sleep(8)

    def addTransferSiteManual(self):
        driver.find_element_by_id("txtfacility").send_keys(' Sparrow Lansing  - 1193 ')
        driver.find_element_by_xpath("//*[@id = 'txtfacility']").click()
        facility_element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//span[text() = ' Sparrow Lansing  - 1193 ']"))
        )
        driver.execute_script("arguments[0].click();", facility_element)
        time.sleep(1)

        # Navigate to transfer site
        driver.find_element_by_xpath("//span[text() =' Data Management ']").click()
        time.sleep(3)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="cdk-overlay-1"]/div/div/span[3]/span/button'))
        )
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)

        #Send inputs for Automated Transfer Site
        '''driver.find_element_by_xpath('/html/body/app-root/div/div/mat-sidenav-container/mat-sidenav-content/main/div[2]/div/app-transfer-site/div[1]/div[2]/mat-card-actions/button').click()
        time.sleep(3)
        driver.find_element_by_id("ddlEntityId").click()
        
        time.sleep(3)
        element1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mat-option-517"]/span'))
                )
        time.sleep(3)
        driver.execute_script("arguments[0].click();", element1)
        
        driver.find_element_by_id('btnSave').click()'''

        #Add a Manual Site
        driver.find_element_by_xpath('/html/body/app-root/div/div/mat-sidenav-container/mat-sidenav-content/main/div[2]/div/app-transfer-site/div[1]/div[2]/mat-card-actions/button').click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[text()='Manual Site']/preceding-sibling::div[1]").click()
        driver.find_element_by_id('txtTransferSiteName').send_keys(transfersitename)
        driver.find_element_by_id("txtTransferSiteIdentifier").send_keys(transferSiteIdentifier)
        driver.find_element_by_id('btnSave').click()
        time.sleep(4)

    # Verify the data in Database
    def verifySiteInDatabase(self):
        print(transfersitename)
        return DBConnector_test.fetchSite(self, transfersitename)

    def test_closeWindow(self):
        driver.quit()



#Edit the Existing Transfir site

#driver.find_element_by_xpath('/html/body/app-root/div/div/mat-sidenav-container/mat-sidenav-content/main/div[2]/div/app-transfer-site/div[2]/form/div/div[1]/div[2]/mat-table/mat-row[3]/mat-cell[6]/span/button').click()
#driver.find_element_by_xpath('//*[@id="mat-checkbox-319"]/label/div').click()

