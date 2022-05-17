from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


serv = Service("C:/Users/Admin/Desktop/Project 1/chromedriver.exe")
driver: WebDriver = webdriver.Chrome(service=serv)


def submit_form():

    # This will redirect to the employee form submission page
    driver.get("file:///C:/Users/Admin/Desktop/Project%201/ClientSideProject1/HTMLCSS/EmployeeForm/EmployeeForm2.html")
    sleep(10)
    field: WebElement = driver.find_element(by=By.ID, value="fname")
    field.send_keys("Selenium")
    sleep(2)
    field: WebElement = driver.find_element(by=By.ID, value="lname")
    field.send_keys("Test")
    sleep(2)
    field: WebElement = driver.find_element(by=By.ID, value="eventDate")
    field.send_keys("05/12/2022")
    sleep(2)
    field: WebElement = driver.find_element(by=By.ID, value="eventTime")
    field.send_keys("10:00AM")
    sleep(2)
    field: WebElement = driver.find_element(by=By.ID, value="location")
    field.send_keys("Texas")
    sleep(2)
    field: WebElement = driver.find_element(by=By.ID, value="description")
    field.send_keys("University Course")
    sleep(2)
    field: WebElement = driver.find_element(by=By.ID, value="cost")
    field.send_keys("5000")
    sleep(2)
    field: WebElement = driver.find_element(by=By.ID, value="gradingFormat")
    field.send_keys("txt")
    sleep(2)
    field: WebElement = driver.find_element(by=By.ID, value="typeOfEvent")
    field.send_keys("Course")
    sleep(2)
    field: WebElement = driver.find_element(by=By.ID, value="employeeId")
    field.send_keys("51")
    sleep(2)
    field: WebElement = driver.find_element(by=By.ID, value="finalGrade")
    field.send_keys("A")
    sleep(2)
    field: WebElement = driver.find_element(by=By.ID, value="workJust")
    field.send_keys("Benefit Work Role")
    sleep(5)
    field: WebElement = driver.find_element(by=By.ID, value="submitButton")
    field.click()
    sleep(10)

    driver.quit()


if __name__ == '__main__':
    submit_form()
