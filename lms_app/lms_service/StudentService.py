from lms_app.lms_repository.StudentRepository import *


class StudentManagementService(metaclass=ABCMeta):
    @abstractmethod
    def register(self, model: RegisterStudentDto):
        """Register Student"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, student_id: int, model: EditStudentDto):
        """Edit Student"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListStudentDto]:
        """List Student"""
        raise NotImplementedError

    @abstractmethod
    def list_student_for_course(self, course_id) -> List[ListStudentDto]:
        """List Student"""
        raise NotImplementedError

    @abstractmethod
    def details(self, user_id: int) -> StudentDetailsDto:
        """Details of Student"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, student_id: int):
        """Delete Student"""
        raise NotImplementedError


class DefaultStudentManagementService(StudentManagementService):
    repository = StudentRepository

    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def register(self, model: RegisterStudentDto):
        return self.repository.register(model)

    def edit(self, student_id: int, model: EditStudentDto):
        return self.repository.edit(student_id, model)

    def list(self) -> List[ListStudentDto]:
        return self.repository.list()

    def list_student_for_course(self, course_id) -> List[ListStudentDto]:
        return self.repository.list_student_for_course(course_id)

    def details(self, user_id: int) -> StudentDetailsDto:
        return self.repository.details(user_id)

    def delete(self, student_id: int):
        return self.repository.delete(student_id)