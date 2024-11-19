Feature: Create a student
    In order to create a university
    As a student
    I want to create a student

    Scenario: Create a student
        Given access to home page
        When I create a student "Jaque"
        Then the student "Jaque" should be created

    Scenario: Create a course
        Given access to home page
        When I create a course "mat"
        Then the course "mat" should be created

    Scenario: Subscribe student to course
        Given access to home page
        And I create a student "Jaque"
        And I create a course "mat"
        When I subscribe the student for the course
        Then the subscription should be done
    
    Scenario: create discipline without having 3 courses created
        Given access to home page
        And I create a student "Jaque"
        And I create a course "mat"
        When I add the discipline "calculus" to the course "1"
        Then the discipline should not be created

    Scenario: create discipline having 3 courses created
        Given access to home page
        And I create a student "Jaque"
        And I create a course "mat"
        And I create a course "port"
        And I create a course "geo"
        When I add the discipline "calculus" to the course "1"
        Then the discipline "calculus" should be created

    Scenario: Subscribe student in less than 3 disciplines
        Given access to home page
        And I create a student "Jaque"
        And I create a course "mat"
        And I create a course "port"
        And I create a course "geo"
        And I subscribe the student for the course
        And I add the discipline "calculus" to the course "1"
        And I add the discipline "portuguese" to the course "1"
        And I add the discipline "geography" to the course "1"
        When I subscribe the student "1" for the discipline "1"
        Then the subscription of the studente "Jaque" in the "1" discipline should be done
        And should be displayed a message indicating at least 3 required subjects

    Scenario: Subscribe student in more than 3 disciplines
        Given access to home page
        And I create a student "Jaque"
        And I create a course "mat"
        And I create a course "port"
        And I create a course "geo"
        And I subscribe the student for the course
        And I add the discipline "calculus" to the course "1"
        And I add the discipline "portuguese" to the course "1"
        And I add the discipline "geography" to the course "1"
        When I subscribe the student "1" for the discipline "1"
        And I subscribe the student "1" for the discipline "2"
        And I subscribe the student "1" for the discipline "3"
        And I add the discipline "history" to the course "1"
        And I subscribe the student "1" for the discipline "4"
        Then the subscription of the studente "Jaque" in the "4" discipline should be done