import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class HomePage():
  def __init__(self, driver):
    self._driver = driver
  
  def wait_page_loaded(self):
    elements = self._driver.find_elements(By.CSS_SELECTOR, ".smooth")       
    while len(elements) > 0:            
      elements = self._driver.find_elements(By.CSS_SELECTOR, ".smooth")            
      time.sleep(1) 

  def subscribe_student_in_discipline(self, course_id, student_id=None):
    if student_id:
      self._driver.find_element(By.ID, "subscribe-student-id").click()
      self._driver.find_element(By.ID, "subscribe-student-id").clear()
      self._driver.find_element(By.ID, "subscribe-student-id").send_keys(student_id)
    self._driver.find_element(By.ID, "subscribe-discipline-id").click()
    self._driver.find_element(By.ID, "subscribe-discipline-id").clear()
    self._driver.find_element(By.ID, "subscribe-discipline-id").send_keys(course_id)
    self._driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(6) > #course-btn").click()
    self._driver.find_element(By.CSS_SELECTOR, ".py-p:nth-child(1)").click()

  def add_discipline_to_couse(self, name, course_id=None):
      self._driver.find_element(By.ID, "discipline-nome").click()
      self._driver.find_element(By.ID, "discipline-nome").clear()
      self._driver.find_element(By.ID, "discipline-nome").send_keys(name)
      if course_id:
        self._driver.find_element(By.ID, "course-discipline-id").click()
        self._driver.find_element(By.ID, "course-discipline-id").clear()
        self._driver.find_element(By.ID, "course-discipline-id").send_keys(course_id)
      self._driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(5) > #course-btn").click()

  def add_student_to_course(self, student_id, course_id):
      self._driver.find_element(By.ID, "student-id").click()
      self._driver.find_element(By.ID, "student-id").send_keys(student_id)
      self._driver.find_element(By.ID, "course-id").click()
      self._driver.find_element(By.ID, "course-id").send_keys(course_id)
      self._driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > #course-btn").click()

  def add_course(self, name):
      self._driver.find_element(By.ID, "course-nome").click()
      self._driver.find_element(By.ID, "course-nome").clear()
      self._driver.find_element(By.ID, "course-nome").send_keys(name)
      self._driver.find_element(By.ID, "course-btn").click()

  def add_student(self, name):
    self._driver.find_element(By.ID, "student-nome").click()
    self._driver.find_element(By.ID, "student-nome").send_keys(name)
    self._driver.find_element(By.ID, "student-btn").click()

  def get_log_text(self, index):
    return self._driver.find_element(By.CSS_SELECTOR, f".py-p:nth-child({index})").text