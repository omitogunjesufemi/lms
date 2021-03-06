from typing import Callable
from dependency_injector import providers, containers

from lms_app.lms_service.AdminService import *
from lms_app.lms_repository.ApplyRepository import DjangoORMApplyRepository
from lms_app.lms_repository.CommentRepository import DjangoORMCommentRepository
from lms_app.lms_service.ApplyService import *
from lms_app.lms_service.TutorService import *
from lms_app.lms_service.StudentService import *
from lms_app.lms_service.CourseService import *
from lms_app.lms_service.EnrollmentService import *
from lms_app.lms_service.AppointmentService import *
from lms_app.lms_service.AssessmentService import *
from lms_app.lms_service.QuestionService import *
from lms_app.lms_service.SittingService import *
from lms_app.lms_service.GradingServices import *
from lms_app.lms_service.CommentService import *


class Container(containers.DeclarativeContainer):
    # ADMIN SERVICE CONTROLLER
    admin_repository: Callable[[], AdminRepository] = providers.Factory(
        DjangoORMAdminRepository
    )

    admin_management_service: Callable[[], AdminManagementService] = providers.Factory(
        DefaultAdminManagementService,
        repository=admin_repository
    )

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

    # COMMENT SERVICE CONTROLLER
    comment_repository: Callable[[], CommentRepository] = providers.Factory(
        DjangoORMCommentRepository
    )
    comment_management_service: Callable[[], CommentManagementService] = providers.Factory(
        DefaultCommentManagementService,
        repository=comment_repository
    )

    # APPLICATION SERVICE CONTROLLER
    apply_repository: Callable[[], ApplyRepository] = providers.Factory(
        DjangoORMApplyRepository
    )
    apply_management_service: Callable[[], ApplyManagementService] = providers.Factory(
        DefaultApplyManagementService,
        repository=apply_repository
    )


service_controller = Container()
