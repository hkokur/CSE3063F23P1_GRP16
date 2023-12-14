
import java.util.ArrayList;

public class Student extends Person {
    private String address;
    private String phoneNumber;
    private int semester;
    private int entranceYear;
<<<<<<< HEAD
    private String status;
    private ArrayList<Course> courses;
    private Transcript transcript;

    public Student(String personName, String personSurname, String username, String password,
            String address, String phoneNumber, int studentYear, int entranceYear, String status,
            ArrayList<Course> courses,
            Transcript transcript) {
        super(personName, personSurname, username, password);
        this.address = address;
        this.phoneNumber = phoneNumber;
        this.studentYear = studentYear;
        this.entranceYear = entranceYear;
        this.courses = courses;
        this.transcript = transcript;
        this.status = status;
    }

    public Student(String personName, String personSurname, String username, String password) {

    }

    public Student() {

    }

    public void printTranscriptInfo() {
        System.out.println("STUDENT TRANSCRIPT");
        System.out.println("-------------------------------------------------");
        System.out.println(transcript.getGrades());
    }

=======
    private String status; // waiting, approved, rejected, finished, available
    private ArrayList<Course> selectedCourses;
    private Transcript transcript;

>>>>>>> 7f49d5ed85e4b624f6ddc60902887c9f8b6eafef
    public String getAddress() {
        return this.address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getPhoneNumber() {
        return this.phoneNumber;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public int getSemester() {
        return this.semester;
    }

    public void setSemester(int semester) {
        this.semester = semester;
    }

    public int getEntranceYear() {
        return this.entranceYear;
    }

    public void setEntranceYear(int entranceYear) {
        this.entranceYear = entranceYear;
    }

<<<<<<< HEAD
    public boolean getStatus() {
        return this.getStatus();
=======
    public String getStatus() {
        return this.status;
>>>>>>> 7f49d5ed85e4b624f6ddc60902887c9f8b6eafef
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public ArrayList<Course> getSelectedCourses() {
<<<<<<< HEAD
        return courses;
    }

    public void setCourses(ArrayList<Course> courses) {
        this.courses = courses;
    }

    public void clearCourses() {
        this.courses = new ArrayList<Course>();
    }

    public String getFullName() {
        return this.getPersonName() + " " + this.getPersonSurname();
=======
        return this.selectedCourses;
    }

    public void setSelectedCourses(ArrayList<Course> selectedCourses) {
        this.selectedCourses = selectedCourses;
>>>>>>> 7f49d5ed85e4b624f6ddc60902887c9f8b6eafef
    }

    public Transcript getTranscript() {
        return this.transcript;
    }

    public void setTranscript(Transcript transcript) {
        this.transcript = transcript;
    }

<<<<<<< HEAD
    public void addCourse(Course course){
        this.courses.add(course);

    }


    // Function for checking if the student has already added the course.
    public boolean checkStudentAlreadyAddedTheCourse(Course course) {
        ArrayList<Course> courses = this.getSelectedCourses();
        for (int i = 0; i < courses.size(); i++) {
            if (courses.get(i).getShortName().equals(course.getShortName())) {
                return true;
            }
        }
        return false;
    }

     // If the student has taken the prerequisite course, it will return true.
     public boolean checkPrerequisite(Course course) {
        ArrayList<Grade> grades = this.getTranscript().getGradeList();
        // If there are no prerequisites, return true.
        if (course.getPrerequisite().size()==0) {
            return true;
        }

        // If there are prerequisites, check if the student has taken the prerequisite
        // course.
        else {
            // Check if the student has taken the prerequisite course. If the student has
            // taken the course, return true.
            // If the student has not taken the course, return false.
            // If the student has taken the course but failed, return false.
            for (int i = 0; i < grades.size(); i++) {
                ArrayList<String> prerequisites = course.getPrerequisite();
                for(int j = 0;j<prerequisites.size();j++){
                    if (grades.get(i).getCourse().getShortName().equals(prerequisites.get(j))
                        && !grades.get(i).getGrade().equals("FF")) {
                        return true;
                    }
                }
            }
            return false;
        }
    }

    // Function for checking if the student's year is suitable for the course.
    public boolean checkYear(Course course) {

        String courseShortName = course.getShortName();
        int courseYear = parseYearFromShortName(courseShortName);

        // If the student's year is suitable for the course, return true.
        // If the student's year is not suitable for the course, return false.
        if (this.getStudentYear() >= courseYear) {
            return true;
        } else {
=======
    public Student(String name, String surname, String id, String password, String address, String phoneNumber,
            int semester, int entranceYear, String status, ArrayList<Course> selectedCourses, Transcript transcript) {
        super(name, surname, id, password);
        this.address = address;
        this.phoneNumber = phoneNumber;
        this.semester = semester;
        this.entranceYear = entranceYear;
        this.status = status;
        this.selectedCourses = selectedCourses;
        this.transcript = transcript;
    }

    public Student() {
        super();
        this.address = "";
        this.phoneNumber = "";
        this.semester = 0;
        this.entranceYear = 0;
        this.status = "";
        this.selectedCourses = new ArrayList<Course>();
        this.transcript = new Transcript();
    }

    // Adding a course to the selected courses of the student
    public boolean addCourse(Course course) {
        try {
            selectedCourses.add(course);
            return true;
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
            return false;
        }

    }

    public boolean dropCourse(Course course) {
        try {
            selectedCourses.remove(course);
            return true;
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
>>>>>>> 7f49d5ed85e4b624f6ddc60902887c9f8b6eafef
            return false;
        }
    }

<<<<<<< HEAD
    // Function for parsing the year from the course short name.
    public int parseYearFromShortName(String courseShortName) {
        // Find first number in string
        int i = 0;
        while (!Character.isDigit(courseShortName.charAt(i))) {
            i++;
        }
        // Return courseShortName.charAt(i) as an int
        return Character.getNumericValue(courseShortName.charAt(i));
    }

    public boolean isUntaken(Course course) {
        ArrayList<Grade> studentCoursesTaken = this.getTranscript().getGradeList();

        for(int i = 0;i<studentCoursesTaken.size();i++){
            if(studentCoursesTaken.get(i).getCourse().getFullName().equals(course.getFullName()))
                return false;
        }           
       
        return true;
    }

    public ArrayList<Course> getAvailableCourses() {
        ArrayList<Course> availableCourses = new ArrayList<Course>();
        Json json = new Json();
        ArrayList<Course> courses = json.readCourses();
        // From the course section list
        for (int i = 0; i < courses.size(); i++) {
            Course course = courses.get(i);
            if (checkStudentAlreadyAddedTheCourse(course) == false
                    && checkPrerequisite(course) == true
                    && checkYear(course) == true && isUntaken(course)) {
                availableCourses.add(course);
            }
        }
        return availableCourses;
    }

    public String getWarnings(int warningCount){
        if(warningCount==1){
            return "Maximum credit exceeded.";
        }
        return "";
    }
    public int getTotalCredit(){
        int sum = 0;
        for(int i = 0;i<courses.size();i++){
            sum+=courses.get(i).getCredit();
        }
        return sum;
    }   

=======
    public ArrayList<Course> getAvailableCourses() {
        ArrayList<Course> availableCourses = new ArrayList<Course>();

        ArrayList<Course> allCourseSections = getAllCourses();
        for (Course course : allCourseSections) {
            if (checkStudentAlreadySelectedCourse(course) == false &&
                    checkPrerequisite(course) == true &&
                    checkSemesterOfCourse(course) == true) {
                availableCourses.add(course);
            }
        }

        return availableCourses;
    }

    public ArrayList<Course> getAllCourses() {

        Json json = new Json();
        ArrayList<CourseSection> allCourseSections = json.readCourseSections();
        ArrayList<Course> allCourses = new ArrayList<Course>();

        allCourses.addAll(allCourseSections);
        return allCourses;
    }

    public String getWarnings() {

        return "";
    }

    public int getTotalCredit() {

        return 0;
    }

    public boolean checkCredits() {
        return false;
    }

    public boolean checkStudentAlreadySelectedCourse(Course course) {
        return false;
    }

    public boolean checkPrerequisite(Course course) {
        return false;
    }

    public boolean checkSemesterOfCourse(Course course) {
        return false;
    }

    // Returns true if the course is in the transcript(student has taken the course
    // before and passed)
    private boolean checkCourseInTranscript(Course course) {
        for (Grade grade : transcript.getGradeList()) {
            if (grade.getCourse() == course) {
                return true;
            }
        }

        return false;
    }

    public boolean sendCoursesForApproval() {
        return false;
    }

    public ArrayList<ArrayList<Course>> checkOverlappingCourses() {
        return new ArrayList<ArrayList<Course>>();
    }

    // + addCourse(course: Course): boolean
    // + dropCourse(course: Course): boolean
    // - dropCourse(course: Course): boolean
    // + getSelectedCourse():
    // + getAvailableCourses():
    // + getAllCourses():
    // + getWarnings(): String
    // - getTotalCredit(): int
    // - checkCredits(): boolean
    // - checkStudentAlreadySelectedCourse(course: Course): boolean
    // - checkPrerequisite(course: Course): boolean
    // - checkSemesterOfCourse(course: Course): boolean
    // + sendCoursesForApproval(): boolean
    // + checkOver1apingCourses(): ArrayList<ArrayList<Course>>
>>>>>>> 7f49d5ed85e4b624f6ddc60902887c9f8b6eafef
}
