import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


public class SystemController {
    private Person loggedInUser;
    private ArrayList<Course> courses;
    private ArrayList<Lecturer> lecturers;
    private ArrayList<CourseSection> courseSections;
    private ArrayList<Student> students;
    private ArrayList<Advisor> advisors;
    private Json json;
    SystemController() {
        json = new Json();
        courses = json.getCourses();
        lecturers = json.getLecturers();
        courseSections = json.getCourseSections();
        students = json.getStudents();
        advisors = json.getAdvisors();

    }

    public SystemController(Person loggedInUser) {
        this.loggedInUser = loggedInUser;
    }

    public Person getLoggedInUser() {
        return loggedInUser;
    }

    public ArrayList<CourseSection> getCourseSectionList() {
        return courseSections;
    }

    public ArrayList<Advisor> getAdvisorList() {
        return advisors;
    }

    public ArrayList<Lecturer> getLecturerList() {
        return lecturers;
    }

    public boolean Authenticate(String username, String password) {
        // Check if username and password are correct
        // If correct, set loggedInUser to the correct user
        // If incorrect, throw an error
        for (int i = 0; i < students.size(); i++) {
            if (students.get(i).getUsername().equals(username) && students.get(i).getPassword().equals(password)) {
                this.loggedInUser = students.get(i);
            }
        }
        for (int i = 0; i < lecturers.size(); i++) {
            if (lecturers.get(i).getUsername().equals(username) && lecturers.get(i).getPassword().equals(password)) {
                this.loggedInUser = lecturers.get(i);
            }
        }
        for (int i = 0; i < advisors.size(); i++) {
            if (advisors.get(i).getUsername().equals(username) && advisors.get(i).getPassword().equals(password)) {
                this.loggedInUser = advisors.get(i);
            }
        }
        if (this.loggedInUser == null) {
            return false;
        }
        return true;
    }

    public String getMenu() {
        String_Constants StringConstants = new String_Constants();
        if (loggedInUser instanceof Student) {
            return StringConstants.STUDENT_MENU_OPTIONS;
        } else if (loggedInUser instanceof Advisor) {
            return StringConstants.ADVISOR_MENU_OPTIONS;
        } else if (loggedInUser instanceof Lecturer) {
            return StringConstants.LECTURER_MENU_OPTIONS;
        } else {
            return "Error: Invalid user type.";
        }
    }

    public ArrayList<Course> requestCourses() {
        // Return a list of courses for the logged in user
        return null;
    }

    public String viewCourses() {
        // ArrayList<Course> courses = requestCourses();
        ArrayList<Course> courses = new ArrayList<Course>(
                List.of(
                        new Course("CS101", "Introduction to Computer Science",
                                "This course is an introduction to computer science."),
                        new Course("CS102", "Introduction to Programming",
                                "This course is an introduction to programming.")));

        String courseList = "";
        for (Course course : courses) {
            courseList += course.getShortName() + " - " + course.getFullName() + "\n";
        }
        return courseList;
    }

    public void printAvailableCourses(Student student) {
        for (int i = 0; i < courses.size(); i++) {
            ArrayList<Grade> studentCoursesTaken = student.getTranscript().getGradeList();
            int j = 0;
            for (; j < studentCoursesTaken.size(); j++) {
                if (studentCoursesTaken.get(j).getCourse().getFullName().equals(courses.get(i).getFullName())) {
                    break;
                }
            }
            if (j == studentCoursesTaken.size()) {
                System.out.println(courses.get(i).getFullName());

            }
        }
    }

    public void printLecturerCourses(Lecturer lecturer) {
        for (int i = 0; i < courses.size(); i++) {
            List<Course> lecturerCourses = lecturer.getCourses();
            int j = 0;
            for (; j < lecturerCourses.size(); j++) {
                if (lecturerCourses.get(j).getShortName().equals(courses.get(i).getShortName())) {
                    System.out.println(lecturerCourses.get(j).getFullName());
                }
            }
        }
    }

    public void printLecturerStudents(Lecturer lecturer) {
        for (int i = 0; i < students.size(); i++) {
            List<Course> lecturerCourses = lecturer.getCourses();
            for (int j = 0; j < students.get(i).getCourses().size(); j++) {
                for (int k = 0; k < lecturerCourses.size(); k++) {
                    System.out.println("Lecturer Course: " + lecturerCourses.get(k).getFullName());
                    System.out.println("Student Course: " + students.get(i).getCourses().get(j).getFullName());
                    if (lecturerCourses.get(k)
                            .equals(students.get(i).getCourses().get(j))) {
                        System.out.println(students.get(i).getCourses().get(k).getFullName());
                    }
                }
            }
        }
    }

    public void printLecturerStudentsGrades(Lecturer lecturer) {
        for (int i = 0; i < courseSections.size(); i++) {

        }
    }


    public void printAvailableCourses(Student student, ArrayList<CourseSection> untakenCourses){
        
        int courseOrder = 1;
        for(int i = 0;i<courseSections.size();i++){
            CourseSection courseSection = courseSections.get(i);
            ArrayList<Grade> studentCoursesTaken = student.getTranscript().getGradeList();
            int j = 0;
            for(;j<studentCoursesTaken.size();j++){
                if(studentCoursesTaken.get(j).getCourse().getFullName().equals(courseSection.getFullName())){
                    break;
                }
            }
            if(j==studentCoursesTaken.size()){
                
                untakenCourses.add(courseSections.get(i));
                System.out.println(courseOrder+". "+courseSection.getFullName()+" "+courseSection.getSectionName()+" "+courseSection.getShortName());
                courseOrder++;
            }
        }
    }

    // Applying the course operation
    public void applyCourse(Student student, CourseSection courseSection){
        System.out.println(courseSection.getFullName());
        student.getCourses().add(courseSection);
        json.updateStudents();
        json.updateParametes();

    }

    public boolean checkPrerequisite(){
        return true;
    }

    // Accepting or rejecting the course application.

    // Displaying the information of the advisor. It may be more specific depending
    // on request type

    // Possible scenarios

    // Sending the chosen courses to advisor. It will add these courses to the lsit
    // temporarily.
    // Depdending on the action of the advisor, course will stay in the list or not.

    // Deleting the target courses.

    // Displaying the information of the student. It may be more specific depending
    // on request type

    /*
     * public void sendCourses(Course course){
     * student.getCourses().add(course);
     * 
     * // Student list will be inserted to the json file(to the corresponding course
     * list of the student in json file) for the necessary fields.
     * }
     * 
     * public void deleteCourses(Course course){
     * // Similar approach with sendCourses is intended.
     * }
     */
}
