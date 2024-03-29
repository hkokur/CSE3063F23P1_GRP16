package menus;

import java.util.ArrayList;
import java.util.Scanner;

import org.apache.log4j.Logger;

import models.Course;
import contollers.StudentController;
import models.Transcript;

public class StudentMenu {

    // Logger
    final static Logger logger = Logger.getLogger(StudentMenu.class);

    StudentController studentController;

    public StudentMenu(StudentController studentController) {
        this.studentController = studentController;
    }

    public StudentMenu() {
        this.studentController = new StudentController();
    }

    public void studentMenu() {
        logger.info("Student menu displayed");
        Scanner scanner = new Scanner(System.in);
        int choice = 0;
        while (choice != 6) {
            System.out.println("1-Add Course");
            System.out.println("2-Drop Course");
            System.out.println("3-Show Transcript");
            System.out.println("4-Show Selected Courses");
            System.out.println("5-Send Approval Request");
            System.out.println("6-Logout");
            System.out.print("Enter your choice: ");
            try {
                choice = scanner.nextInt();
                switch (choice) {
                    case 1:
                        CourseAdding();
                        break;
                    case 2:
                        CourseDropping();
                        break;
                    case 3:
                        showTranscript();
                        break;
                    case 4:
                        showSelectedCourses();
                        break;
                    case 5:
                        sendApprovalRequest();
                        break;
                    case 6:
                        menus.Menu.getInstance().setLoggedInUser(null);
                        menus.Menu.getInstance().LoginMenu();
                        break;
                    default:
                        System.out.println("Invalid choice");
                        break;
                }
            } catch (Exception e) {
                System.out.println("Invalid input type. Please try again.");
                scanner.nextLine();
            }
        }

    }

    public void CourseAdding() throws Exception {
        logger.info("Course adding menu displayed");
        showAvailableCourses();

        System.out.println("Enter the course you want to add");

        System.out.println("eg: 1,2,3");
        System.out.println("eg: * for all courses");
        System.out.println("eg: -1 to exit");
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();

        ArrayList<Course> courses = studentController.getAvailableCourses();
        ArrayList<Integer> selectedCourses = parseInput(input, courses);

        for (int i = 0; i < selectedCourses.size(); i++) {
            studentController.addCourse(courses.get(selectedCourses.get(i) - 1));
        }

    }

    public void CourseDropping() throws Exception {
        logger.info("Course dropping menu displayed");
        showSelectedCourses();

        System.out.println("Enter the course you want to drop");

        System.out.println("eg: 1,2,3");
        System.out.println("eg: * for all courses");
        System.out.println("eg: -1 to exit");
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();

        ArrayList<Course> courses = studentController.getSelectedCourses();
        ArrayList<Integer> selectedCourses = parseInput(input, courses);

        for (int i = selectedCourses.size() - 1; i >= 0; i--) {
            studentController.dropCourse(courses.get(selectedCourses.get(i) - 1));
        }
    }

    public void showSelectedCourses() {
        logger.info("Selected courses displayed");
        ArrayList<Course> courses = studentController.getSelectedCourses();
        System.out.println("Status: " + studentController.getStatus());
        System.out.println("=============Selected Courses=============");

        for (int i = 0; i < courses.size(); i++) {
            Course course = courses.get(i);
            System.out.println(i + 1 + "-" + course.getFullName() + " [" +
                    course.getShortName() + "]" + "(" + course.getCredit() + ")");
        }

        System.out.println("============================================");
    }

    public void showAvailableCourses() {
        logger.info("Available courses displayed");
        ArrayList<Course> courses = studentController.getAvailableCourses();

        System.out.println("=============Available Courses=============");

        for (int i = 0; i < courses.size(); i++) {
            Course course = courses.get(i);
            System.out.println(i + 1 + "-" + course.getFullName() + " [" +
                    course.getShortName() + "]" + "(" + course.getCredit() + ")");
        }

        System.out.println("============================================");
    }

    public void showTranscript() {
        logger.info("Transcript displayed");
        Transcript transcript = studentController.getTranscript();
        String grades = transcript.getGrades();

        System.out.println("=================Transcript==================");
        System.out.println(grades);
        System.out.println("=============================================");
    }

    public void sendApprovalRequest() {
        logger.info("Approval request sent");

        if (studentController.sendApprovalRequest()) {
            System.out.println("Approval request sent");
        } else {
            System.out.println("Approval request could not be sent");
        }
    }

    private ArrayList<Integer> parseInput(String input, ArrayList<Course> courses) throws Exception {

        // If input is * then return all indexes of courses
        // If input is -1 then return empty array
        // If input is 1,2,3 then return 1,2,3
        // If input is 1,2,3,4,5,6,7,8,9,10 then return 1,2,3,4,5,6,7,8,9,10
        // Else return empty array

        ArrayList<Integer> selectedCourses = new ArrayList<Integer>();

        if (input.equals("*")) {
            for (int i = 0; i < courses.size(); i++) {
                selectedCourses.add(i + 1);
            }
            return selectedCourses;
        } else if (input.equals("-1")) {
            return selectedCourses;
        } else {
            String[] inputArray = input.split(",");
            for (int i = 0; i < inputArray.length; i++) {

                try {
                    int index = Integer.parseInt(inputArray[i]);
                    if (index > 0 && index <= courses.size()) {
                        selectedCourses.add(index);
                    }
                } catch (Exception e) {
                    throw new Exception("Invalid input");
                }
            }

            return selectedCourses;
        }
    }

}
