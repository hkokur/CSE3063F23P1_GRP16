import unittest
from Course import Course
from TimeInterval import TimeInterval
from CourseSection import CourseSection 
from Lecturer import Lecturer



class CourseSectionTest(unittest.TestCase):
    def setUp(self):

        self.course = Course(short_name="CS101", full_name="Intro to CS", description="Introductory course", semester=1, credit=3, prerequisite=[])
        self.dates = [TimeInterval(start_time="9:00", end_time="11:00"), TimeInterval(start_time="13:00", end_time="15:00")]
        self.lecturer = Lecturer(username="lecturer_username", password="password", full_name="John Doe")

        self.course_section1 = CourseSection(
            course=self.course,
            dates=self.dates,
            section_name="Section A",
            lecturer=self.lecturer,
            quota=30,
            number_of_student=0,
            required_credit=150,
            type="Type A"
        )

        self.course_section2 = CourseSection(
            course=self.course,
            dates=self.dates,
            section_name="Section B",
            lecturer=self.lecturer,
            quota=25,
            number_of_student=0,
            required_credit=120,
            type="Type B"
        )

    def test_str_method(self):
        expected_str_output = (
            "---------\n"
            "Course Information\n"
            "Course Code: CS101\n"
            "Course Name: Intro to CS\n"
            "Description: Introductory course\n"
            "Prerequisite: \n"
            "Semester: 1\n"
            "Credit: 3\n"
            "Section Name: Section A\n"
            "Quota: 30\n"
            "Number of Student: 0\n"
            "Required Credit: 150\n"
            "Type: Type A\n"
            "Lecturer Name: John Doe\n"
            "Dates: 9:00 - 11:00, 13:00 - 15:00\n"
        )
        self.assertEqual(str(self.course_section1), expected_str_output)

    def test_eq_method(self):
        self.assertEqual(self.course_section1, self.course_section1)  
        self.assertNotEqual(self.course_section1, self.course_section2) 

    def test_number_of_student_setter_valid_value(self):
        self.course_section.number_of_student = 20
        self.assertEqual(self.course_section.number_of_student, 20)

    def test_number_of_student_setter_invalid_value(self):
        with self.assertRaises(ValueError):
            self.course_section.number_of_student = 40  

    def test_required_credit_setter_valid_value(self):
        self.course_section.required_credit = 100
        self.assertEqual(self.course_section.required_credit, 100)

    def test_required_credit_setter_invalid_value(self):
        with self.assertRaises(ValueError):
            self.course_section.required_credit = 250 


    def test_add_dates(self):
        new_date = TimeInterval(start_time="13:00", end_time="15:00")
        self.assertTrue(self.course_section.add_dates(new_date))
        self.assertIn(new_date, self.course_section.dates)  

        existing_date = TimeInterval(start_time="9:00", end_time="11:00")
        self.assertFalse(self.course_section.add_dates(existing_date))
        self.assertIn(existing_date, self.course_section.dates) 

    def test_remove_dates(self):
        existing_date = TimeInterval(start_time="9:00", end_time="11:00")
        self.assertTrue(self.course_section.remove_dates(existing_date))
        self.assertNotIn(existing_date, self.course_section.dates) 

        non_existing_date = TimeInterval(start_time="13:00", end_time="15:00")
        self.assertFalse(self.course_section.remove_dates(non_existing_date))

    def is_time_overlap(self, date: TimeInterval) -> bool:
        for d in self.__dates:
            if d.start_time < date.end_time and date.start_time < d.end_time:
                return True
        return False

    def check_overlap(self, course_section) -> bool:
        for d in course_section.dates:
            if self.is_time_overlap(d):
                return True
        return False
    
    def test_to_json(self):
        expected_json = {
            "shortName": self.course.short_name,
            "fullName": self.course.full_name,
            "description": self.course.description,
            "semester": 1,
            "credit": 3,
            "prerequisite": [],
            "dates": self.dates,
            "sectionName": "Section B",
            "lecturer": self.lecturer,  
            "quota": 30,
            "numberOfStudent": 0,
            "requiredCredit": 150,
            "type": "Type B"
        }
        result_json = self.course_section2.to_json()
        self.assertEqual(result_json, expected_json)


    def test_eq_method(self):
        self.assertEqual(self.course_section1, self.course_section1) 
        self.assertNotEqual(self.course_section1, self.course_section2)  

if __name__ == '__main__':
    unittest.main()
