"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

- Abstraction:
    You can hide details that you don't need to know. You can just call a method 
    without knowing the full extent of the information that makes it work.

- Encapsulation:
    The data lives close to its functionality; for example you can bundle a 
    function(method) in a class and only use it with instances of that class.

- Polymorphysm: 
    You can adapt the code to the type of data you are taking in. Child classes 
    can change their methods and attributes to more accurately structure/contain 
    the data in it, even though child classes inherit these from their parent class.

2. What is a class?
    A class is a data structure used to implement user-defined objects. You can 
    create a parent class that inherits from an object, then create child classes 
    that inherit attributes and methods from the parent class. This allows for 
    code-reusability, customization and minimizes redundacy overall.

3. What is an instance attribute?
    An attribute that belongs to the instance (not the class).

4. What is a method?
    A method is a function defined inside a class that always takes at least one 
    parameter (self).

5. What is an instance in object orientation?
    An instance is a version (object) created from a specified class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

    A class attribute is a requirement that is specified in the class. An instance 
    attribute is something that is added to the instance and does not exist in the 
    class that the instance derives from.

    For example:

    class Flower(object):
        def __init__(self):
            self.color = "Pink" <---- class attribute

    ranunculus = Flower() <------ instance
    ranunculus.species = "ranunculus" <------ instance attribute

The ranunculus.species attribute does not exist in the class, just in that specific instance.

"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """A parent class created for a student that requires 3 attributes to instantiate: first name, last name and address."""
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """ A parent class for questions and answers."""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """ Method prints a question, takes in user input and evaluates if it's correct."""

        prompt = raw_input(self.question + " > ").lower()
        if prompt == self.correct_answer:
            return True
        else:
            return False


class Exam(object):
    """A parent class for an exam. Requires exam name to instantiate"""

    questions = []

    def __init__(self, name):
        self.name = name


    def add_question(self, question, correct_answer):
        """ Adds question and answer to exam."""

        question = Question( question, correct_answer)
        self.questions.append(question)

    def administer(self):
        """Administers all questions and returns user's score"""

        # There's a bug here where it returns a score of 1 even though all 
        # questions are answered correctly. I couldn't figure out why. Perhaps 
        # the issue is with the ask_and_evaluate() method? Not sure :/

        score = 0

        for question in self.questions:
            if Question.ask_and_evaluate(question) is True:
                score += 1
        return score

class Quiz(Exam):
    number_questions = len(Exam.questions)

    def administer(self):
        """ Inherits from parent class Exam and creates a Quiz."""

        # I thought that having it inherit from Exam would simplify things. However, I 
        # couldn't get super to work on the administer function in the Quiz class,
        # which is why I copied/pasted the same here to override it from the Exam class.

        # After testing, it returns a pass/fail like it should, but just like the 
        # parent's administer() method, I think the score variable is not updating 
        # correctly, which means this might be returning incorrect pass/fail marks.

        score = 0

        for question in self.questions:
            if Question.ask_and_evaluate(question):
                score += 1

        if score >= self.number_questions/2.0:
            return "Pass"
        else:
            return "Fail"

def take_test(exam_instance, student_instance):
    """Takes in exam and student as parameters, administers exam and returns student's score"""

    exam_given = Exam.administer(exam_instance)
    return exam_given


def example():
    """ Creates a class and student instance."""

    """ Added some questions to the exam and administered exam for the student."""

    # This mostly works except that score is not updating correctly. It returns 
    # a score of 1 when all questions are answered correctly.

    new_exam = Exam('midterm')
    new_exam.add_question("What is the method for adding an element to a set?", ".add()")
    new_exam.add_question("Who is the author of Python?", "Guido Van Rossum")
    new_exam.add_question("What is Python named after?", "Monty Python")
    
    student_taking_exam = Student("Ada", "Lovelace", "123 Alongtimeago st")

    return take_test(new_exam, student_taking_exam)

if __name__ == '__main__':
    print example()

