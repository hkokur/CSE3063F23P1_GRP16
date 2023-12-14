
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
public class Advisor extends Staff {

    private List<Student> students;

    public Advisor(String personName, String personSurname, String username, String password,
            String reputation, ArrayList<TimeInterval> officeHours, int salary, String employmentStatus,
            List<Student> students) {
        super(personName, personSurname, username, password, reputation, officeHours, salary,
                employmentStatus);
        this.students = students;
    }

    public Advisor() {
        
    }

    public void printTranscriptInfo() {
        System.out.println("STUDENT TRANSCRIPT");
        System.out.println("-------------------------------------------------");
        System.out.println();
    }

    public void setStudents(List<Student> students) {
        this.students = students;
    }

    public List<Student> getStudents() {
        return this.students;
    }


    public boolean addStudent(Student student){
        return students.add(student);
    }
    public boolean deleteStudent(Student student){
        return students.remove(student);
    }

    public ArrayList<Course> getCombinedCourses(Student student){
        
        ArrayList<Course> availableCourses = new ArrayList<>();
        availableCourses.addAll(student.getAvailableCourses());
        availableCourses.addAll(student.getSelectedCourses());
        return availableCourses;
    }
    public boolean approveStudent(Student student){
        
        ArrayList<Course> selectedCourses = student.getSelectedCourses();
        Scanner input = new Scanner(System.in);
        int operation = 0;
        while (operation != 1 || operation != 2) {
            System.out.println("Please select the approval type:");
            System.out.println("1. Approve whole");
            System.out.println("2. Approve one by one");
            System.out.println("3. Skip");
            operation = input.nextInt();
            if(operation != 1 || operation != 2){
                System.out.println("Please select one of the operations showcased.\n");
            }
            else if(operation==1){   
                if(student.getTotalCredit()>40){
                    student.getWarnings(1); // It requests the first warning shooting out.
                }
                else{
                    student.setStatus("Approved");
                }   
            }
            else if(operation==2){
                int i = 0;
                int approvalStatus  = 0;
                while(i<student.getSelectedCourses().size()){
                    System.out.println("Do you approve the course "+student.getSelectedCourses().get(i).getFullName()+"?(1: approve, 0: reject, -1: skip)");
                    approvalStatus = input.nextInt();
                    if(approvalStatus==1){
                        i++;
                    }
                    else if(approvalStatus==0){
                        Course targetCourse = student.getAvailableCourses().get(i);
                        student.getSelectedCourses().remove(targetCourse);
                    }
                    else if(approvalStatus!=-1)
                        System.out.println("Please type one of the options showcased.\n");
                }
                student.setStatus("Approved");
            }
            else if(operation==3){
                student.setStatus("Pending");
                return false;
            }
        }
        for(int i = 0;i<selectedCourses.size();i++){
            
            System.out.println("Do you approve the course")
        }
        return true;
    }

    public boolean rejectStudent(Student student){
        student.getSelectedCourses().clear();
        student.setStatus("Rejected");
        return 0;
    }

}
