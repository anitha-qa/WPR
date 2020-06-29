#import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import XLUtils

driver = webdriver.Chrome('P://IT Transformation -Automation//WPR//WPR//ChromeDriver//chromedriver.exe')

driver.implicitly_wait(1)
driver.maximize_window()

#Open the application
#driver.get("http://webqa01:4204/")
driver.get("https://qa-wpr.rxresourcesolutions.com/")
print(driver.title)

def getRowCount(file,DepartmentTransfer) :
    workbook = openpyxl.load_workbook(file)
    sheet = workbook.get_sheet_by_name(DepartmentTransfer)
    return (sheet.max_row)

def getcolumnCount(file,DepartmentTransfer) :
    workbook = openpyxl.load_workbook(file)
    sheet = workbook.get_sheet_by_name(DepartmentTransfer)
    return (sheet.max_column)

def readData(file,DepartmentTransfer,rownum,columno) :
    workbook = openpyxl.load_workbook(file)
    sheet = workbook.get_sheet_by_name(DepartmentTransfer)
    return sheet.cell(row=rownum, column=columno).value

def writeData(file,DepartmentTransfer,rownum,columno,data) :
    workbook = openpyxl.load_workbook(file)
    sheet = workbook.get_sheet_by_name(DepartmentTransfer)
    return sheet.cell(row=rownum, column=columno).value
    workbook.save(file)

    # Calling Xcel File
    # path = "P://IT Transformation -Automation//WPR//WPR//WPR- DDT Excel file//DepartmentTransfer.xlsx"

    # Calling the Function from the XLUtils

    # rows = XLUtils.getRowCount(path,'DepartmentTransfer.xlsx')
    # for r in range(2,rows+1) :
    #   DepartmentID = XLUtils.readData(path,"DepartmentTransfer.xlsx",r,1)
    #  DepartmentIdentifier = XLUtils.readData(path, "DepartmentTransfer.xlsx", r, 2)

    # Validation for existing department
    for x in range(0, 3):
        driver.find_element_by_id("mat-input-5").send_keys("zxzx")
        driver.find_element_by_id("mat-input-6").click()
        numberofElement = driver.find_elements(By.XPATH, "//*[contains(text(), ' Already Exists. ')]").__sizeof__() > 0
        print(numberofElement)
        driver.find_element_by_id("mat-input-5").clear()
        driver.find_element_by_id("mat-input-6").clear()
        if not numberofElement:
            break
    driver.find_element_by_id("mat-input-5").clear()
    driver.find_element_by_id("mat-input-5").send_keys("zxzx1")
    driver.find_element_by_id("mat-input-6").click()