# core/app_shell.py
from PyQt5.QtWidgets import QStackedWidget
from ui.login_view import LoginView
from ui.main_view import MainView
from ui.student_view import StudentView
from ui.teacher_view import TeacherView
from services.auth_service import AuthService
from presenters.login_presenter import LoginPresenter

class AppShell(QStackedWidget):
    PAGE_LOGIN = 0
    PAGE_ADMIN = 1
    PAGE_STUDENT = 2
    PAGE_TEACHER = 3

    def __init__(self):
        super().__init__()

        self.login_view = LoginView()
        self.admin_view = MainView()
        self.student_view = StudentView()
        self.teacher_view = TeacherView()

        self.auth_service = AuthService()
        
        self.login_presenter = LoginPresenter(
            view=self.login_view,
            auth=self.auth_service,
            on_success=self._go_to_view
        )
        self.addWidget(self.login_view)
        self.addWidget(self.admin_view)
        self.addWidget(self.student_view)
        self.addWidget(self.teacher_view)
        self.setCurrentIndex(self.PAGE_LOGIN)
        self.setWindowTitle("PyQt5 - MVP Multi-Rol")
        self.resize(640, 400)

    def _go_to_view(self, username: str, user_type: str):
        if user_type == "admin":
            self.admin_view.set_welcome(username)
            self.setCurrentIndex(self.PAGE_ADMIN)
        elif user_type == "alumno":
            self.student_view.set_welcome(username)
            self.setCurrentIndex(self.PAGE_STUDENT)
        elif user_type == "maestro":
            self.teacher_view.set_welcome(username)
            self.setCurrentIndex(self.PAGE_TEACHER)
