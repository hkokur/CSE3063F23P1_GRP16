import java.util.ArrayList;

public class Student extends Person {
    private String address;
    private String phoneNumber;
    private int semester;
    private int entranceYear;
    private String status;
    private ArrayList<Course> selectedCourses;
    private Transcript transcript;

    public Student(String personName, String personSurname, String username, String password,
            String address, String phoneNumber, int studentYear, int entranceYear, String status,
            ArrayList<Course> selectedCourses,
            Transcript transcript) {
        super(personName, personSurname, username, password);
        this.address = address;
        this.phoneNumber = phoneNumber;
        this.entranceYear = entranceYear;
        this.selectedCourses = selectedCourses;
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

    public String getStatus() {
        return this.status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public ArrayList<Course> getSelectedCourses() {
        return selectedCourses;
    }

    public void setCourses(ArrayList<Course> courses) {
        this.selectedCourses = courses;
    }

    public String getFullName() {
        return this.getPersonName() + " " + this.getPersonSurname();
    }

    public void setSelectedCourses(ArrayList<Course> selectedCourses) {
        this.selectedCourses = selectedCourses;
    }

    public Transcript getTranscript() {
        return this.transcript;
    }

    public void setTranscript(Transcript transcript) {
        this.transcript = transcript;
    }

    public boolean addCourse(Course course){
        return this.selectedCourses.add(course);

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


    // Function for checking if the student's year is suitable for the course.
    public boolean checkYear(Course course) {

        String courseShortName = course.getShortName();
        int courseYear = parseYearFromShortName(courseShortName);

        // If the student's year is suitable for the course, return true.
        // If the student's year is not suitable for the course, return false.
        if (this.getEntranceYear() >= courseYear) {
            return true;
        } else {
            return false;
        }
    }

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
            if (!checkStudentAlreadyAddedTheCourse(course)
                    && checkPrerequisite(course)
                    && checkYear(course) && isUntaken(course)) {
                availableCourses.add(course);
            }
        }
        return availableCourses;
    }

    private boolean studentCanTakeCourse(Course course) {
        if (checkStudentAlreadySelectedCourse(course) == false &&
                checkPrerequisite(course) == true &&
                checkSemesterOfCourse(course) == true &&
                checkStudentPassedCourse(course) == false) {
            return true;
        }

        else {
            return false;
        }
    }

    public ArrayList<Course> getAllCourses() {
        ArrayList<Course> allCourses = new ArrayList<Course>();

        Json json = new Json();
        allCourses.addAll(json.readMandatoryCourses());
        allCourses.addAll(json.readTechnicalElectiveCourse());
        allCourses.addAll(json.readNonTechnicalElectiveCourses());

        return allCourses;
    }

    public String getWarnings() {

        String warningString = "";

        if (checkCreditLimit() == false) {
            warningString += "========Student has exceeded the credit limit.=========\n";
            warningString += "Total credit: " + getTotalCreditOfSelectedCourses() + "\n";
            warningString += "Max credit: 30\n";
            warningString += "========================================================\n";
        }

        // TODO: revise this function after merge
        if (checkOverlappingCourses().size() > 0) {
            warningString += "========Student has overlapping courses.=========\n";
            for (ArrayList<Course> overlappingCourses : checkOverlappingCourses()) {
                for (Course course : overlappingCourses) {
                    warningString += course.getFullName() + " (" + course.getShortName() + "), ";
                }
                warningString += "\n";
            }
            warningString += "========================================================\n";
        }

        return warningString;
    }
    public int getTotalCredit(){
        int sum = 0;
        for(int i = 0;i<selectedCourses.size();i++){
            sum+=selectedCourses.get(i).getCredit();
        }
        return sum;
    }  

    public boolean dropCourse(Course course){
        for(int i = 0;i<this.getSelectedCourses().size();i++){
            if(this.getSelectedCourses().get(i).getShortName().equals(course.getShortName())){
                this.getSelectedCourses().remove(course);
                return true;
            }
        }
        return false;
    }
    private int getTotalCreditOfSelectedCourses() {
        int totalCredit = 0;

        for (Course course : selectedCourses) {
            totalCredit += course.getCredit();
        }

        return totalCredit;
    }

    // Returns true if the student has less than max credit
    public boolean checkCreditLimit() {
        if (getTotalCreditOfSelectedCourses() > 30) {
            return false;
        }

        else {
            return true;
        }
    }

    // Returns true if the student has already selected the course
    public boolean checkStudentAlreadySelectedCourse(Course course) {
        // Check if the course's short name is in the selected courses
        for (Course selectedCourse : selectedCourses) {
            if (selectedCourse.getShortName().equals(course.getShortName())) {
                return true;
            }
        }
        return false;
    }


    // Returns true if the student passed the prerequisite courses
    public boolean checkPrerequisite(Course course) {
        if (course.getPrerequisite() == null) {
            return true;
        }

        else {
            for (String prerequisite : course.getPrerequisite()) {
                if (checkStudentPassedCourseWithShortName(prerequisite) == false) {
                    return false;
                }
            }

            return true;
        }
    }

    // Returns true if student has greater or equal semester than the course
    public boolean checkSemesterOfCourse(Course course) {
        if (course.getSemester() <= this.semester) {
            return true;
        } else {
            return false;
        }
    }

    // Returns true if the course is in the transcript(student has taken the course
    // before and passed)
    public boolean checkStudentPassedCourse(Course course) {
        for (Grade grade : transcript.getGradeList()) {
            if (grade.getCourse().getShortName().equals(course.getShortName()) && grade.getGrade() != "FF") {
                return true;
            }
        }

        return false;
    }

    public boolean checkStudentPassedCourseWithShortName(String courseShortName) {
        for (Grade grade : transcript.getGradeList()) {
            if (grade.getCourse().getShortName().equals(courseShortName) && grade.getGrade() != "FF") {
                return true;
            }
        }

        return false;
    }

    public ArrayList<ArrayList<Course>> checkOverlappingCourses() {
        ArrayList<ArrayList<Course>> overlapingCourses = new ArrayList<ArrayList<Course>>();

        ArrayList<Course> allCourseSections = getSelectedCourses();

        for (int i = 0; i < allCourseSections.size(); i++) {

            Course course1 = allCourseSections.get(i);
            ArrayList<TimeInterval> dates1 = new ArrayList<>();

            for (int j = i + 1; j < allCourseSections.size(); j++) {

                Course course2 = allCourseSections.get(j);
                ArrayList<TimeInterval> dates2 = new ArrayList<>();

                if (allCourseSections.get(i) instanceof MandatoryCourse) {
                    course1 = (MandatoryCourse) allCourseSections.get(i);
                    dates1 = ((MandatoryCourse) allCourseSections.get(i)).getDates();
                } else if (allCourseSections.get(i) instanceof TechnicalElectiveCourse) {
                    course1 = (TechnicalElectiveCourse) allCourseSections.get(i);
                    dates1 = ((TechnicalElectiveCourse) allCourseSections.get(i)).getDates();
                } else if (allCourseSections.get(i) instanceof NonTechnicalElectiveCourse) {
                    course1 = (NonTechnicalElectiveCourse) allCourseSections.get(i);
                    dates1 = ((NonTechnicalElectiveCourse) allCourseSections.get(i)).getDates();
                }
                if (allCourseSections.get(j) instanceof MandatoryCourse) {
                    course2 = (MandatoryCourse) allCourseSections.get(i);
                    dates2 = ((MandatoryCourse) allCourseSections.get(i)).getDates();
                } else if (allCourseSections.get(j) instanceof TechnicalElectiveCourse) {
                    course2 = (TechnicalElectiveCourse) allCourseSections.get(i);
                    dates2 = ((TechnicalElectiveCourse) allCourseSections.get(i)).getDates();
                } else if (allCourseSections.get(j) instanceof NonTechnicalElectiveCourse) {
                    course2 = (NonTechnicalElectiveCourse) allCourseSections.get(i);
                    dates2 = ((NonTechnicalElectiveCourse) allCourseSections.get(i)).getDates();
                }

                for (int x = 0; x < dates1.size(); x++) {
                    if (dates2.contains(dates1.get(x))) {
                        ArrayList<Course> overlapingCourse = new ArrayList<Course>();
                        overlapingCourse.add(course1);
                        overlapingCourse.add(course2);
                        overlapingCourses.add(overlapingCourse);
                    }
                }
            }
        }

        return overlapingCourses;
    }
}
