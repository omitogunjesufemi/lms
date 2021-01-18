from typing import Callable
from dependency_injector import providers, containers
from lms_app.lms_service.TutorService import *
from lms_app.lms_service.StudentService import *
from lms_app.lms_service.CourseService import *
from lms_app.lms_service.EnrollmentService import *
from lms_app.lms_service.AppointmentService import *
from lms_app.lms_service.AssessmentService import *
from lms_app.lms_service.QuestionService import *
from lms_app.lms_service.SittingService import *
from lms_app.lms_service.GradingServices import *


class Container(containers.DeclarativeContainer):
    # STUDENT SERVICE CONTROLLER
    student_repository: Callable[[], StudentRepository] = providers.Factory(
        DjangoORMStudentRepository
    )

    student_management_service: Callable[[], StudentManagementService] = providers.Factory(
        DefaultStudentManagementService,
        repository=student_repository
    )

    # TUTOR SERVICE CONTROLLER
    tutor_repository: Callable[[], TutorRepository] = providers.Factory(
        DjangoORMTutorRepository
    )
    tutor_management_service: Callable[[], TutorManagementService] = providers.Factory(
        DefaultTutorManagementService,
        repository=tutor_repository
    )

    # COURSE SERVICE CONTROLLER
    course_repository: Callable[[], CourseRepository] = providers.Factory(
        DjangoORMCourseRepository
    )
    course_management_service: Callable[[], CourseManagementService] = providers.Factory(
        DefaultCourseManagementService,
        repository=course_repository
    )

    # ENROLLMENT SERVICE CONTROLLER
    enroll_repository: Callable[[], EnrollmentRepository] = providers.Factory(
        DjangoORMEnrollmentRepository
    )
    enrollment_management_service: Callable[[], EnrollmentManagementService] = providers.Factory(
        DefaultEnrollmentManagementService,
        repository=enroll_repository
    )

    # APPOINTMENT SERVICE CONTROLLER
    appointment_repository: Callable[[], AppointmentRepository] = providers.Factory(
        DjangoORMAppointmentRepository
    )
    appointment_management_service: Callable[[], AppointmentManagementService] = providers.Factory(
        DefaultAppointmentManagementService,
        repository=appointment_repository
    )

    # ASSESSMENT SERVICE CONTROLLER
    assessment_repository: Callable[[], AssessmentRepository] = providers.Factory(
        DjangoORMAssessmentRepository
    )
    assessment_management_service: Callable[[], AssessmentManagementService] = providers.Factory(
        DefaultAssessmentManagementService,
        repository=assessment_repository
    )

    # QUESTION SERVICE CONTROLLER
    question_repository: Callable[[], QuestionRepository] = providers.Factory(
        DjangoORMQuestionRepository
    )
    question_management_service: Callable[[], QuestionManagementService] = providers.Factory(
        DefaultQuestionManagementService,
        repository=question_repository
    )

    # SITTING SERVICE CONTROLLER
    sitting_repository: Callable[[], SittingRepository] = providers.Factory(
        DjangoORMSittingRepository
    )
    sitting_management_service: Callable[[], SittingManagementService] = providers.Factory(
        DefaultSittingManagementService,
        repository=sitting_repository
    )

    # GRADING SERVICE CONTROLLER
    grading_repository: Callable[[], GradingRepository] = providers.Factory(
        DjangoORMGradingRepository
    )
    grading_management_service: Callable[[], GradingManagementService] = providers.Factory(
        DefaultGradingManagementService,
        repository=grading_repository
    )


service_controller = Container()
