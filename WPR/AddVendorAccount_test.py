from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from WPR.DBConnector import DBConnector_test
import time
class AddVendorAccount_test():
    # To setup driver and launch the application
    def test_setup(self):
        global driver
        global vendorName
        global accountName
        global updatedSiteOfCare
        global updatedAccountName
        vendorName = "Baxter"
        accountName = "TestVenMar911"
        updatedSiteOfCare = "Physician Clinic"
        updatedAccountName = "WAC"
        driver = webdriver.Chrome('P://IT Transformation -Automation//WPR//WPR//ChromeDriver//chromedriver.exe')
        driver.implicitly_wait(3)
        driver.maximize_window()

        # Open the application
        driver.get("https://qa-wpr.rxresourcesolutions.com")
        print(driver.title)
        print("welcome")
        time.sleep(15)

    #Verify the data in Database
    def verifyAccountNumberInDatabase(self):
        return DBConnector_test.fetchVendorAccountNumber(self, accountName)

    #To add vendor account
    def test_addVendor(self):
        # Select the facility
        driver.find_element_by_xpath("//*[@id = 'txtfacility']").click()
        time.sleep(1)
        driver.find_element_by_id("txtfacility").send_keys(' Sparrow Lansing  - 1193 ')
        driver.find_element_by_xpath("//*[@id = 'txtfacility']").click()
        facility_element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//span[text() = ' Sparrow Lansing  - 1193 ']"))
        )
        driver.execute_script("arguments[0].click();", facility_element)
        time.sleep(3)

        # Navigate to Vendor Account
        driver.find_element_by_xpath("//span[text() =' Data Management ']").click()
        time.sleep(3)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button//span[text() ='Vendor Account']"))
        )
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)

        #Click on Vendor Account Button
        driver.find_element_by_xpath("//span[text() = ' VENDOR ACCOUNT ']").click()

        # Select Vendor by Clicking on row in table
        time.sleep(2)
        table = driver.find_element_by_xpath("//td[text() = ' "+vendorName+" ']/following-sibling::td[4]//button")
        table.click()
        numberofElement = driver.find_elements(By.XPATH, "//*[contains(text(), ' ("+vendorName+" ')]").__sizeof__() > 0
        print(numberofElement)

        # Enter Account name
        time.sleep(2)
        driver.find_element_by_xpath(
            "//*[text() = 'Account']/ancestor::div[@class = 'mat-form-field-infix']//input").click()
        driver.find_element_by_xpath(
            "//*[text() = 'Account']/ancestor::div[@class = 'mat-form-field-infix']//input").send_keys(accountName)

        # Select "Account type"
        time.sleep(2)
        driver.find_element_by_xpath(
            "//*[text() = 'Account Type ']/ancestor::div[@class = 'mat-form-field-infix']//input").click()
        driver.find_element_by_xpath(
            "//*[text() = 'Account Type ']/ancestor::div[@class = 'mat-form-field-infix']//input").send_keys("340B")
        driver.find_element_by_xpath("//span[@class ='mat-option-text']").click()

        # select "Site of Care"
        time.sleep(2)
        driver.find_element_by_xpath(
            "//*[text() = 'Site of Care ']/ancestor::div[@class = 'mat-form-field-infix']//input").click()
        driver.find_element_by_xpath(
            "//*[text() = 'Site of Care ']/ancestor::div[@class = 'mat-form-field-infix']//input").send_keys(
            "Acute Care")
        driver.find_element_by_xpath("//span[@class ='mat-option-text']").click()
        time.sleep(2)

        # Click save button
        driver.find_element_by_xpath("//div[@class='ng-star-inserted']//button//*[text()=' Save ']").click()
        time.sleep(2)

    #To verify Account added or not
    def test_VerifyAddedAccount(self, accountName):
        accountNameIsPresent = driver.find_element_by_xpath("//*[text() = ' " + accountName + " ']/following-sibling::*[6]/button").is_displayed()
        print(accountNameIsPresent)
        return accountNameIsPresent

    #Verify the data in Database
    def verifyAccountNumberInDatabase(self):
        return DBConnector_test.fetchVendorAccountNumber(self, accountName)

    #To edit Vendor Account
    def test_EditVendor(self):
        # Edit the Account
        driver.find_element_by_xpath("//*[text() = ' "+accountName+" ']/following-sibling::*[6]/button").click()
        time.sleep(5)
        editElement = driver.find_elements_by_xpath("//button[contains(@class,'shortButton')]")
        editElement[0].click()

        # Edit "Account type"
        time.sleep(2)
        driver.find_element_by_xpath(
            "//*[text() = 'Account Type ']/ancestor::div[@class = 'mat-form-field-infix']//input").click()
        driver.find_element_by_xpath(
            "//*[text() = 'Account Type ']/ancestor::div[@class = 'mat-form-field-infix']//input").clear()
        driver.find_element_by_xpath(
            "//*[text() = 'Account Type ']/ancestor::div[@class = 'mat-form-field-infix']//input").send_keys("WAC")
        driver.find_element_by_xpath("//span[@class ='mat-option-text']").click()

        # Edit "Site of Care"
        time.sleep(2)
        driver.find_element_by_xpath(
            "//*[text() = 'Site of Care ']/ancestor::div[@class = 'mat-form-field-infix']//input").click()
        driver.find_element_by_xpath(
            "//*[text() = 'Site of Care ']/ancestor::div[@class = 'mat-form-field-infix']//input").send_keys(
            "Physician Clinic")
        driver.find_element_by_xpath("//span[@class ='mat-option-text']").click()
        time.sleep(2)

        # Save edited account
        time.sleep(2)
        driver.find_element_by_xpath("//button[contains(@class,'mat-raised-button')]//span[text() = ' Save ']").click()

    #To verify Edited Account
    def test_verifyEditedAccount(self, accountName):
        time.sleep(5)
        actualAcctType = driver.find_element_by_xpath(
            "//*[text() = ' " + accountName + " ']/following-sibling::*[1]").text
        print(actualAcctType)
        return actualAcctType

    #To delete vendor account
    def test_DeleteVendor(self):
        # Delete the Account
        time.sleep(5)
        driver.find_element_by_xpath("//*[text() = ' "+accountName+" ']/following-sibling::*[6]/button").click()
        time.sleep(5)
        deleteElement = driver.find_elements_by_xpath("//button[contains(@class,'shortButton')]")
        deleteElement[1].click()
        time.sleep(2)
        driver.find_element_by_xpath("//span[text() = 'Yes, Delete it']").click()

    #To Verify Deleted Account
    def test_verifyDeleteAccount(self, accountName):
            time.sleep(3)
            #driver.find_element_by_xpath("//*[text() = ' " + accountName + " ']")
            try:
                isaccountpresent = driver.find_element_by_xpath("//*[text() = ' " + accountName + " ']").is_displayed()
                return isaccountpresent
            except NoSuchElementException as e:
                isaccountpresent = False
                print("Exception occured", e)
                return isaccountpresent

    def test_closeWindow(self):
        driver.quit()



