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
        
        self._label = QLabel("Bienvenido, has iniciado sesión correctamente.", alignment=Qt.AlignCenter)
        
        layout.addWidget(self._label)
        
        self.setCentralWidget(central_widget)

    def set_welcome(self, user: str):
        self._label.setText(f"Bienvenido, {user}. ¡Sesión iniciada!")
