
public interface Section {
    
    public boolean isTechnical();
    public boolean isMandatory();
    public void setDates(TimeInterval timeInterval);
    public boolean addDate(TimeInterval timeInterval);
    public boolean removeDate(TimeInterval timeInterval);
    public String getSectionName();
    public void setSectionName(String sectionName);
    public Lecturer getLecturer();
    public void setLecturer(Lecturer lecturer);
    public int getQuota();
    public void setQuota(int quota);
}
