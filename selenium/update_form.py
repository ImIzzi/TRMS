from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


serv = Service("C:/Users/Admin/Desktop/Project 1/chromedriver.exe")
driver: WebDriver = webdriver.Chrome(service=serv)


def update_form():

    # This will redirect to the employee form submission page
    driver.get("C:/Users/Admin/Desktop/Project 1/ClientSideProject1/HTMLCSS/GetEmployeeForm/GetFormSup.html")
    sleep(10)
    field: WebElement = driver.find_element(by=By.ID, value="idInput")
    field.send_keys("51")
    sleep(9)
    field: WebElement = driver.find_element(by=By.XPATH, value="/html/body/button[1]")
    field.click()
    sleep(10)
    field: WebElement = driver.find_element(by=By.ID, value="rejectForm")
    field.send_keys("No")
    sleep(5)
    field: WebElement = driver.find_element(by=By.ID, value="dsupApproval")
    field.send_keys("Yes")
    field: WebElement = driver.find_element(by=By.ID, value="updateButton")
    field.click()
    sleep(10)

    driver.quit()


if __name__ == '__main__':
    update_form()