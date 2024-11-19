from time import sleep
from behave import *
from selenium import webdriver
from pages.homePage import HomePage

@given(u'access to home page')
def step_impl(context):
    driver = webdriver.Chrome()
    driver.get("https://tdd-detroid.onrender.com/")
    driver.set_window_size(1200, 740)
    context.homepage = HomePage(driver)
    context.homepage.wait_page_loaded()


@step(u'I create a student "{student_name}"')
def step_impl(context, student_name):
    hp = context.homepage
    hp.add_student(student_name)
    

@then(u'the student "{student_name}" should be created')
def step_impl(context, student_name):
    hp = context.homepage
    assert (
      f"INFO Added student id: 1, Name: {student_name}"
      in hp.get_log_text(1)
    )


@step(u'I create a course "{course_name}"')
def step_impl(context, course_name):
    hp = context.homepage
    hp.add_course(course_name)


@then(u'the course "{course_name}" should be created')
def step_impl(context, course_name):
    hp = context.homepage
    assert (
      f"INFO Added course id: 1, Nome: {course_name}"
      in hp.get_log_text(1)
    )

@step(u'I subscribe the student for the course')
def step_impl(context):
    hp = context.homepage
    hp.add_student_to_course("1", "1")


@then(u'the subscription should be done')
def step_impl(context):
    hp = context.homepage
    assert (
      "INFO Student id 1 subscribed to course id 1"
      in hp.get_log_text(1)
    )

@when(u'I add the discipline "{discipline_name}" to the course "1"')
def step_impl(context, discipline_name):
    hp = context.homepage
    hp.add_discipline_to_couse(discipline_name, "1")


@then(u'the discipline should not be created')
def step_impl(context):
    hp = context.homepage
    assert (
      "FAIL Necessários 3 cursos para se criar a primeira matéria"
      in hp.get_log_text(1)
    )

@then(u'the discipline "{discipline_name}" should be created')
def step_impl(context, discipline_name):
    hp = context.homepage
    assert (
      f"INFO Added discipline id: 1, Name: {discipline_name}, Course: 1"
      in hp.get_log_text(1)
    )

@given(u'I add the discipline "{discipline_name}" to the course "{course_id}"')
def step_impl(context, discipline_name, course_id):
    hp = context.homepage
    hp.add_discipline_to_couse(discipline_name, course_id)

@step(u'I subscribe the student "{student_id}" for the discipline "{discipline_id}"')
def step_impl(context, student_id, discipline_id):
    hp = context.homepage
    hp.subscribe_student_in_discipline(discipline_id, student_id)

@then(u'the subscription of the studente "{student_name}" in the "{discipline_id}" discipline should be done')
def step_impl(context, student_name, discipline_id):
    hp = context.homepage
    discipline_id = int(discipline_id)
    if discipline_id >= 3:
        index = 1
    else:
        index = 2
    assert (
      f"INFO Student id 1, Name {student_name} subscribed to discipline id {discipline_id}"
      in hp.get_log_text(index)
    )
    
@then(u'should be displayed a message indicating at least 3 required subjects')
def step_impl(context):
    hp = context.homepage
    assert (
      "WARN Aluno deve se inscrever em 3 materias no minimo"
      in hp.get_log_text(1)
    )