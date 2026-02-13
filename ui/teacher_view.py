# ui/teacher_view.py
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget

class TeacherView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Panel de Docente - MVP")
        self.resize(520, 320)
        
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        
        self._label = QLabel("Bienvenido al Portal de Docentes", alignment=Qt.AlignCenter)
        self._label.setStyleSheet("font-size: 22px; font-weight: bold; color: #388e3c;")
        
        self._info_label = QLabel(
            "Aquí podrás gestionar calificaciones, asistencia y materiales de clase.",
            alignment=Qt.AlignCenter
        )
        self._info_label.setStyleSheet("font-size: 14px; margin-top: 20px;")
        
        layout.addStretch(1)
        layout.addWidget(self._label)
        layout.addWidget(self._info_label)
        layout.addStretch(2)
        
        self.setCentralWidget(central_widget)

    def set_welcome(self, user: str):
        self._label.setText(f"Bienvenido, Profesor(a) {user}")
