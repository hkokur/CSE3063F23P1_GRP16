from typing import List

from Lecturer import Lecturer
from TimeInterval import TimeInterval

class SectionInterface:
    def is_technical(self) -> bool:
        pass

    def is_mandatory(self) -> bool:
        pass

    def set_dates(self, dates: List[TimeInterval.TimeInterval]):
        pass

    def get_dates(self) -> List[TimeInterval.TimeInterval]:
        pass

    def add_date(self, date: TimeInterval) -> bool:
        pass

    def remove_date(self, date: TimeInterval) -> bool:
        pass

    def get_section_name(self) -> str:
        pass

    def set_section_name(self, section_name: str):
        pass

    def get_lecturer(self) -> Lecturer:
        pass

    def set_lecturer(self, lecturer: Lecturer):
        pass

    def get_quota(self) -> int:
        pass

    def set_quota(self, quota: int):
        pass
