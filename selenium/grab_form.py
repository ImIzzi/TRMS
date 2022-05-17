from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


serv = Service("C:/Users/Admin/Desktop/Project 1/chromedriver.exe")
driver: WebDriver = webdriver.Chrome(service=serv)


def grab_form():

    # This will redirect to the employee form submission page
    driver.get("C:/Users/Admin/Desktop/Project 1/ClientSideProject1/HTMLCSS/GetEmployeeForm/GetFormEmployeeStatus.html")
    sleep(10)
    field: WebElement = driver.find_element(by=By.ID, value="idInput")
    field.send_keys("51")
    sleep(9)
    field: WebElement = driver.find_element(by=By.XPATH, value="/html/body/button[1]")
    field.click()
    sleep(25)

    driver.quit()


if __name__ == '__main__':
    grab_form()
