
import java.util.ArrayList;
import java.util.List;

public class Lecturer extends Staff {
    public Lecturer(String personName, String personSurname, String username, String password,
            String reputation, ArrayList<TimeInterval> officeHours, int salary, String employmentStatus,
            List<Course> courses) {
        super(personName, personSurname, username, password, reputation, officeHours, salary,
                employmentStatus);
        this.courses = courses;
    }

    public Lecturer(String personName, String personSurname, String usrename, String password) {

    }

    public Lecturer() {
        
    }

    private List<Course> courses;

    public List<Course> getCourses() {
        return courses;
    }

    public boolean addCourse(Course course) {
        return courses.add(course);
    }

    public boolean removeCourse(Course course) {
        return courses.remove(course);
    }
}
