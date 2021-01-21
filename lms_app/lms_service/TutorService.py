from lms.lms_app.lms_repository.TutorRepository import *


class TutorManagementService(metaclass=ABCMeta):
    @abstractmethod
    def register(self, model: RegisterTutorDto):
        """Register Student"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, tutor_id: int, model: EditTutorDto):
        """Edit Tutor"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListTutorDto]:
        """List Tutors"""
        raise NotImplementedError

    @abstractmethod
    def details(self, user_id: int) -> TutorDetailsDto:
        """Details of Tutor"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, tutor_id: int):
        """Delete Tutor"""
        raise NotImplementedError


class DefaultTutorManagementService(TutorManagementService):
    repository = TutorRepository

    def __init__(self, repository: TutorRepository):
        self.repository = repository

    def register(self, model: RegisterTutorDto):
        return self.repository.register(model)

    def edit(self, tutor_id: int, model: EditTutorDto):
        return self.repository.edit(tutor_id,model)

    def list(self) -> List[ListTutorDto]:
        return self.repository.list()

    def details(self, user_id: int) -> TutorDetailsDto:
        return self.repository.details(user_id)

    def delete(self, tutor_id: int):
        return self.repository.delete(tutor_id)