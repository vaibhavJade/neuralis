import math
from abc import ABC, abstractmethod

# ==============================================================================
# 1. CLASS CREATION & 3. ENCAPSULATION
# ==============================================================================
class Student:
    """
    Base class representing a student.
    Demonstrates Encapsulation by making the age attribute private (__age).
    """
    def __init__(self, name: str, age: int, grade: str):
        self.name = name
        self.__age = age  # Private attribute (Encapsulation)
        self.grade = grade

    # Getter method for private attribute __age
    def get_age(self) -> int:
        return self.__age

    # Setter method for private attribute __age with validation
    def set_age(self, age: int) -> None:
        if age > 0:
            self.__age = age
        else:
            print("Error: Age must be a positive integer.")

    def display_info(self) -> None:
        """Displays student details."""
        print(f"Student Name: {self.name} | Age: {self.__age} | Grade: {self.grade}")


# ==============================================================================
# 2. INHERITANCE
# ==============================================================================
class HighSchoolStudent(Student):
    """
    Subclass inheriting from Student.
    Extends the base class with a grade_level attribute and overrides display_info().
    """
    def __init__(self, name: str, age: int, grade: str, grade_level: int):
        # Call parent constructor using super()
        super().__init__(name, age, grade)
        self.grade_level = grade_level

    # Override display_info method to include grade_level
    def display_info(self) -> None:
        print(
            f"High School Student: {self.name} | Age: {self.get_age()} | "
            f"Grade: {self.grade} | Grade Level: {self.grade_level}"
        )


# ==============================================================================
# 4. POLYMORPHISM
# ==============================================================================
def print_student_info(student: Student) -> None:
    """
    Polymorphic function that accepts an object of Student or any subclass
    (e.g., HighSchoolStudent) and dynamically calls its respective display_info().
    """
    student.display_info()


# ==============================================================================
# 5. ABSTRACTION
# ==============================================================================
class Shape(ABC):
    """
    Abstract Base Class representing a geometric shape.
    Enforces implementation of calculate_area in all derived subclasses.
    """
    @abstractmethod
    def calculate_area(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self) -> float:
        return math.pi * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height


# ==============================================================================
# TEST & VERIFICATION DRIVER
# ==============================================================================
if __name__ == "__main__":
    print("=== 1. Testing Class Creation & Encapsulation ===")
    s1 = Student(name="Alice", age=20, grade="A")
    s1.display_info()

    # Modify private attribute via setter
    print("\nUpdating age via setter (set_age)...")
    s1.set_age(21)
    print(f"Retrieved age via getter (get_age): {s1.get_age()}")
    s1.display_info()

    print("\n=== 2. Testing Inheritance ===")
    hs1 = HighSchoolStudent(name="Bob", age=16, grade="A+", grade_level=11)
    hs1.display_info()

    print("\n=== 3. Testing Polymorphism ===")
    print("Calling print_student_info() with Student object:")
    print_student_info(s1)

    print("Calling print_student_info() with HighSchoolStudent object:")
    print_student_info(hs1)

    print("\n=== 4. Testing Abstraction ===")
    circle = Circle(radius=5.0)
    rectangle = Rectangle(width=4.0, height=6.0)

    print(f"Circle Area (radius = 5.0): {circle.calculate_area():.2f}")
    print(f"Rectangle Area (4.0 x 6.0): {rectangle.calculate_area():.2f}")