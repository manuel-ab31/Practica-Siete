# ui/student_view.py
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget

class StudentView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Panel de Estudiante - MVP")
        self.resize(520, 320)
        
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        
        self._label = QLabel("Bienvenido al Portal de Estudiantes", alignment=Qt.AlignCenter)
        self._label.setStyleSheet("font-size: 22px; font-weight: bold; color: #1976d2;")
        
        self._info_label = QLabel(
            "Aquí podrás consultar tus calificaciones, horarios y materias.",
            alignment=Qt.AlignCenter
        )
        self._info_label.setStyleSheet("font-size: 14px; margin-top: 20px;")
        
        layout.addStretch(1)
        layout.addWidget(self._label)
        layout.addWidget(self._info_label)
        layout.addStretch(2)
        
        self.setCentralWidget(central_widget)

    def set_welcome(self, user: str):
        self._label.setText(f"Bienvenido, {user}")
