from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import csv
from openpyxl import load_workbook

import xlrd


workbook = xlrd.open_workbook("GSTLudhianaData.xlsx")
sheet = workbook.sheet_by_name("Ludhiana GSTN")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.mastersindia.co/gst-number-search-and-gstin-verification/")


rowcount = sheet.nrows
# Get number of columns with data in each row
colcount = sheet.ncols

# Reading Excel to fetch GST Number
for curr_row in range(2, rowcount, 1):
    for curr_col in range(3, 4, 1):
        # Read the data in the current cell
        gstNumber = sheet.cell_value(curr_row, curr_col)
        srNo = sheet.cell_value(curr_row, curr_col-2)
        print(srNo, gstNumber)
        
        gstInput = driver.find_element_by_class_name("inputbox")
        gstInput.send_keys(gstNumber)  # data is GST Number
        driver.find_element_by_id("gstin-search-buton").click()

        # Table to Excel conceverions starts
        table = driver.find_element_by_css_selector(".table-responsive")
        with open(r'LudhianaGST.csv', 'a', newline='') as csvfile:
            wr = csv.writer(csvfile)
            for row in table.find_elements_by_css_selector('tbody'):
                gstList = [
                    d.text for d in row.find_elements_by_css_selector('td')]
                gstList.insert(0, srNo)
                wr.writerow(gstList)
        # Table to Excel conceverions Ends

        # clearing input field to enter gst again
        driver.find_element_by_class_name("inputbox").clear()
