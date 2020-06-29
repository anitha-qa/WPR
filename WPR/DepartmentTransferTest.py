from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from WPR.DBConnector import DBConnector_test
import time
import random

class department_transfer_test():

    def Enviornment(self):
        global driver
        global increment1
        global increment2
        global increment3
        global increment4
        global tdn1
        global tdn2
        global deptNameIdentifier1
        global deptNameIdentifier2

        increment1 = random.randrange(0, 100000)
        increment2 = random.randrange(0, 100000)
        increment3 = random.randrange(100001, 200000)
        increment4 = random.randrange(200001, 300000)
        tdn1 = "e2e" + str(format(increment1, '02'))
        deptNameIdentifier1 = "e2e" + str(format(increment2, '02'))
        tdn2 = "e2e" + str(format(increment3, '02'))
        deptNameIdentifier2 = "e2e" + str(format(increment4, '02'))
        driver = webdriver.Chrome('P://IT Transformation -Automation//WPR//WPR//ChromeDriver//chromedriver.exe')
        driver.implicitly_wait(3)
        driver.maximize_window()

        #Open the application
        driver.get("https://qa-wpr.rxresourcesolutions.com/")

        print(driver.title)

    # Add a transfer department
    def Data_Transfer_Depart(self):
        global driver
        time.sleep(5)
        #driver.find_element_by_id("txtfacility").send_keys('Access Rx Pharmacy  - 8184')
        driver.find_element_by_id("txtfacility").send_keys(' Sparrow Lansing  - 1193 ')
        driver.find_element_by_xpath("//*[@id = 'txtfacility']").click()
        facility_element = WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, "//span[text() = ' Sparrow Lansing  - 1193 ']"))
                )
        driver.execute_script("arguments[0].click();", facility_element)
        time.sleep(1)

        driver.find_element_by_xpath("//span[text() =' Data Management ']").click()
        time.sleep(3)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button//span[text() ='Transfer Department']"))
        )
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        #time.sleep(5)

        #Add a Department ID
        driver.find_element_by_id('btnAdd').click()
        time.sleep(2)

        #Enter Random values in department transfer window
        #increment = random.randrange(0, 100000)
        #increment1 = random.randrange(0, 100000)
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/mat-dialog-container/app-transfer-department-dialog/form/div[1]/div/div/div/div/div/div/div[1]/div/div/mat-form-field/div/div[1]/div[3]/input').send_keys(tdn1)
        #time.sleep(3)

        print(deptNameIdentifier1)
        driver.find_element_by_id("txTransferDepartmentIdentifier").send_keys(deptNameIdentifier1)
        #time.sleep(3)
        saveelement = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="mat-dialog-0"]/app-transfer-department-dialog/form/div[2]/mat-card-actions[1]/button/span'))
            )
        driver.execute_script("arguments[0].click();", saveelement)


        #Select the second Facility
        #time.sleep(3)
        driver.find_element_by_id("txtfacility").clear()
        #time.sleep(3)
        driver.find_element_by_xpath("//*[@id = 'txtfacility']").click()
        #time.sleep(3)
        facility_element = WebDriverWait(driver, 15).until(
                    #EC.presence_of_element_located((By.XPATH, "//span[text() = ' Cedar Ridge Hospital  - 0423 ']"))
                    EC.presence_of_element_located((By.XPATH, "//span[text() = ' Behavioral Hospital of Bellaire  - 0455 ']"))
                )
        driver.execute_script("arguments[0].click();", facility_element)
        time.sleep(1)

        #Add a Department ID

        driver.find_element_by_id('btnAdd').click()

        #increment = random.randrange(100001, 200000)
        #increment1 = random.randrange(200001, 300000)

        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/mat-dialog-container/app-transfer-department-dialog/form/div[1]/div/div/div/div/div/div/div[1]/div/div/mat-form-field/div/div[1]/div[3]/input').send_keys(tdn2)
        print("deptName3"+tdn2)
        driver.find_element_by_id("txTransferDepartmentIdentifier").send_keys(deptNameIdentifier2)
        print("deptName2" + deptNameIdentifier2)
        driver.find_element_by_id('btnSave').click()

    #Verify the data in Database
    def verifyDeptNameInDatabase(self):
        print("tdn1"+tdn1)
        return DBConnector_test.fetchDepartment(self, tdn1)

    #edit the existing department
    def Edit_Transfer_Site(self):
        global driver
        time.sleep(2)
        driver.find_element_by_id('btnEdit').click()
        time.sleep(2)
        driver.find_element_by_id('txtTransferDepartmentIdentifier').clear()
        time.sleep(2)
        driver.find_element_by_id('txtTransferDepartmentIdentifier').send_keys("e2e" + str(format(increment3, '02')))
        driver.find_element_by_id('btnSave').click()

    def Verify_Dupulicate_values(self):
        global driver
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id = 'btnEdit']//*[text()='edit']").click()
        time.sleep(2)
        driver.find_element_by_id('btnAdd').click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id = 'btnSave']//*[text()=' Save ']").click()
        time.sleep(3)
        warning_message=driver.find_element_by_xpath("//div[@class = 'cdk-overlay-pane']//span").text
        print(warning_message)
        return warning_message

    def test_closeWindow(self):
        driver.quit()


