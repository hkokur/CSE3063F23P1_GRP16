import java.util.ArrayList;
import java.util.Scanner;

public class Menu {
    
    private Person loggedInUser;
    private Json json = new Json();
    private ArrayList<Course> courses = json.readCourses();
    private ArrayList<Lecturer> lecturers = json.readLecturers();
    private ArrayList<Student> students = json.readStudents();
    private ArrayList<Advisor> advisors = json.readAdvisors();
    SystemController systemController = new SystemController();
    String_Constants StringConstants = new String_Constants();
    Scanner scanner = new Scanner(System.in);

    public Person getLoggedInUser() {
        return loggedInUser;
    }

    public void setLoggedInUser(Person loggedInUser) {
        this.loggedInUser = loggedInUser;
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

    public void Menu() {
        Scanner loginScanner = new Scanner(System.in);
        while (systemController.getLoggedInUser() == null) {
            System.out.println(StringConstants.WELCOME_MESSAGE);
            System.out.println(StringConstants.LOGIN_MESSAGE);
            System.out.print(StringConstants.USERNAME_MESSAGE);
            String username = loginScanner.nextLine();
            System.out.print(StringConstants.PASSWORD_MESSAGE);
            String password = loginScanner.nextLine();
            // If the username and password are correct, authenticate the user and set the
            // logged in user
            boolean isLogged = Authenticate(username, password);
            if (isLogged) {
                System.out.println(StringConstants.LOGIN_SUCCESSFUL_MESSAGE);
            } else {
                System.out.println(StringConstants.LOGIN_UNSUCCESSFUL_MESSAGE);
            }
            System.out.println();
        }

        // System.out.println(systemController.getMenu());
        // int selection = scanner.nextInt();

        if (getLoggedInUser() instanceof Student) {
            studentMenu();
        } else if (getLoggedInUser()instanceof Advisor) {
            advisorMenu();
        } else if (getLoggedInUser() instanceof Lecturer) {
            lecturerMenu();
        }

    }

    public void studentMenu() {
        Student student = (Student) getLoggedInUser();
        StudentController studentController = new StudentController(student);
        System.out.println(systemController.getMenu());
        int selection = scanner.nextInt();
        if (selection == 1) {
            studentController.CourseAdding();
            if (i == -1)
                studentMenu();
            else {
                try {
                    systemController.applyCourse(student, availableCourses.get(i - 1));
                } catch (Exception e) {
                    System.out.println(StringConstants.INVALID_OPTION_MESSAGE);
                }
            }
        } else if (selection == 2) {
            studentController.showTranscript();
        } else if (selection == 3) {
            systemController.setLoggedInUser(null);
        }

        else if (selection == 4) {
            studentController.showSelectedCourses();
        }

        if (systemController.getLoggedInUser() == null) {
            Menu();
        } else {
            studentMenu();
        }

    }

    public void advisorMenu() {

        System.out.println(systemController.getMenu());
        int selection = scanner.nextInt();

        Advisor advisor = (Advisor) systemController.getLoggedInUser();

        if (selection == 1) {
            System.out.println("Which student do you want to go on?");

            for (int j = 0; j < advisor.getStudents().size(); j++) {
                System.out.println((j + 1) + "- " + advisor.getStudents().get(j).getFullName());
            }
            int studentSelection = scanner.nextInt();
            System.out.println(
                    "List of courses for student " + advisor.getStudents().get(studentSelection - 1).getFullName());

            ArrayList<CourseSection> coursesOfStudent = advisor.getStudents().get(studentSelection - 1)
                    .getCourses();
            for (int i = 0; i < coursesOfStudent.size(); i++) {
                CourseSection courseSection = coursesOfStudent.get(i);
                System.out.println(courseSection.getFullName() + " " +
                        courseSection.getSectionName()
                        + " " + courseSection.getShortName());
            }

            System.out.println("1-Approve selections\n2-Reject selections");
            int decision = scanner.nextInt();

            if (decision == 1) {
                // System.out.println(advisor.getStudents().get(studentSelection -
                // 1).getApproved());
                // advisor.getStudents().get(studentSelection - 1).setApproved(true);
                systemController.approveCourse(advisor, studentSelection);
                // System.out.println(advisor.getStudents().get(studentSelection -
                // 1).getApproved());
            } else if (decision == 2) {
                systemController.rejectCourse(advisor, studentSelection);
                // advisor.getStudents().get(studentSelection - 1).clearCourses();
            }

        } else if (selection == 2) {
            System.out.println("Which student do you want to go on?");

            for (int j = 0; j < advisor.getStudents().size(); j++) {
                System.out.println((j + 1) + "- " + advisor.getStudents().get(j).getFullName());
            }
            int studentSelection = scanner.nextInt();

            advisor.getStudents().get(studentSelection - 1).printTranscriptInfo();
        } else if (selection == 3) {
            systemController.setLoggedInUser(null);
        }

        if (systemController.getLoggedInUser() == null) {
            Menu();
        } else {
            advisorMenu();
        }

    }

    public void lecturerMenu() {

        System.out.println(systemController.getMenu());
        int selection = scanner.nextInt();

        Lecturer lecturer = (Lecturer) systemController.getLoggedInUser();

        if (selection == 1) {
            Scanner input = new Scanner(System.in);
            System.out.print("Give ShortName: ");
            String shortName = input.nextLine();
            System.out.print("Give FullName: ");
            String fullName = input.nextLine();
            System.out.print("Description: ");
            String description = input.nextLine();
            Course course = new Course(shortName, fullName, description, "");
            lecturer.addCourse(course);
            systemController.getCourses().add(course);
            systemController.save();

        } else if (selection == 2) {
            systemController.setLoggedInUser(null);
        }

        if (systemController.getLoggedInUser() == null) {
            Menu();
        } else {
            lecturerMenu();
        }

    }

}