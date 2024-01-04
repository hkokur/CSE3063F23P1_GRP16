from datetime import datetime

class TimeInterval:
    def __init__(self, start_time, end_time, day_of_week=None):
        self.start_time = start_time
        self.end_time = end_time
        self.day_of_week = day_of_week

    def get_start_time(self):
        return self.start_time

    def set_start_time(self, start):
        self.start_time = start

    def get_end_time(self):
        return self.end_time

    def set_end_time(self, end):
        self.end_time = end

    def get_day_of_week(self):
        return self.day_of_week

    def set_day_of_week(self, day):
        self.day_of_week = day

    def get_total_time_in_minutes(self):
        try:
            # Convert start and end time to datetime objects(HH:mm)
            start = datetime.strptime(self.start_time, "%H:%M")
            end = datetime.strptime(self.end_time, "%H:%M")

            # Get difference between start and end time in minutes
            difference = (end - start).seconds // 60

            return difference
        except ValueError as e:
            print(e)
            raise e

    def get_time_interval_info(self):
        return f"TimeInterval{{startTime={self.start_time}, endTime={self.end_time}, dayOfWeek={self.day_of_week}}}"

    def is_overlapping(self, time_interval):
        try:
            # Convert start and end time to datetime objects(HH:mm)
            start = datetime.strptime(self.start_time, "%H:%M")
            end = datetime.strptime(self.end_time, "%H:%M")

            # Convert start and end time of the other TimeInterval to datetime objects(HH:mm)
            start2 = datetime.strptime(time_interval.get_start_time(), "%H:%M")
            end2 = datetime.strptime(time_interval.get_end_time(), "%H:%M")

            # Check if the time intervals are overlapping
            if start < start2 < end or start < end2 < end or start2 <= start and end2 >= end:
                return True
            else:
                return False
        except ValueError as e:
            print(e)
            raise e
