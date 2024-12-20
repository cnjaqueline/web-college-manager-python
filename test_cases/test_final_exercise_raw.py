# Generated by Selenium IDE
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pages.homePage import HomePage
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestDemo():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_demo(self):
    self.driver.get("https://tdd-detroid.onrender.com/")
    self.driver.set_window_size(1200, 740)

    home_page = HomePage(self.driver)

    home_page.wait_page_loaded()   
       
    home_page.add_student("douglas")
    assert (
      "INFO Added student id: 1, Name: douglas"
      in home_page.get_log_text(1)
    )

    home_page.add_course('mat')
    assert (
      "INFO Added course id: 1, Nome: mat"
      in home_page.get_log_text(1)
    )

    home_page.add_student_to_course("1", "1")
    assert (
      "INFO Student id 1 subscribed to course id 1"
      in home_page.get_log_text(1)
    )

    home_page.add_discipline_to_couse("mat", "1")
    assert (
      "FAIL Necessários 3 cursos para se criar a primeira matéria"
      in home_page.get_log_text(1)
    )
    
    home_page.add_course("port")

    home_page.add_course("geo")
    
    home_page.add_discipline_to_couse("mat")
    assert (
      "INFO Added discipline id: 1, Name: mat, Course: 1"
      in home_page.get_log_text(1)
    )
    home_page.add_discipline_to_couse("mat2")
    home_page.add_discipline_to_couse("mat3")

    home_page.subscribe_student_in_discipline("1", "1")
    assert (
      "WARN Aluno deve se inscrever em 3 materias no minimo"
      in home_page.get_log_text(1)
    )
    home_page.subscribe_student_in_discipline("2")
    home_page.subscribe_student_in_discipline("3")
    home_page.add_discipline_to_couse("mat4")
    home_page.subscribe_student_in_discipline("3")
    self.driver.close()



    