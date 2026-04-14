import sys
import math
from PyQt5.QtWidgets import (
    QApplication, QWidget, QGridLayout, QPushButton,
    QLineEdit, QTextEdit, QVBoxLayout, QLabel
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced Calculator")
        self.setGeometry(200, 200, 350, 450)
        self.expression = ""
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # Display
        self.display = QLineEdit()
        self.display.setFont(QFont("Arial", 20))
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setFixedHeight(50)
        main_layout.addWidget(self.display)

        # History Panel
        history_label = QLabel("History")
        history_label.setFont(QFont("Arial", 10, QFont.Bold))
        main_layout.addWidget(history_label)

        self.history = QTextEdit()
        self.history.setReadOnly(True)
        self.history.setFixedHeight(80)
        main_layout.addWidget(self.history)

        # Buttons Layout
        grid = QGridLayout()
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('%', 3, 2), ('+', 3, 3),
            ('√', 4, 0), ('x²', 4, 1), ('C', 4, 2), ('=', 4, 3)
        ]

        for text, row, col in buttons:
            button = QPushButton(text)
            button.setFont(QFont("Arial", 14))
            button.setFixedSize(70, 50)
            button.clicked.connect(self.on_button_click)
            grid.addWidget(button, row, col)

        main_layout.addLayout(grid)
        self.setLayout(main_layout)
        self.apply_styles()

    def apply_styles(self):
        """Apply simple styling for a modern look."""
        self.setStyleSheet("""
            QWidget {
                background-color: #2E3440;
                color: #ECEFF4;
            }
            QLineEdit {
                background-color: #3B4252;
                border: 2px solid #81A1C1;
                border-radius: 5px;
                padding: 5px;
                color: white;
            }
            QTextEdit {
                background-color: #3B4252;
                border-radius: 5px;
                color: white;
            }
            QPushButton {
                background-color: #5E81AC;
                border-radius: 5px;
                color: white;
            }
            QPushButton:hover {
                background-color: #81A1C1;
            }
            QPushButton:pressed {
                background-color: #4C566A;
            }
        """)

    def on_button_click(self):
        sender = self.sender().text()

        if sender == 'C':
            self.expression = ""
            self.display.setText("")
        elif sender == '=':
            self.calculate_result()
        elif sender == '√':
            self.expression = f"math.sqrt({self.expression})"
            self.display.setText("√(" + self.display.text() + ")")
        elif sender == 'x²':
            self.expression = f"({self.expression})**2"
            self.display.setText(self.display.text() + "²")
        else:
            self.expression += sender
            self.display.setText(self.display.text() + sender)

    def calculate_result(self):
        try:
            result = eval(self.expression)
            self.history.append(f"{self.display.text()} = {result}")
            self.display.setText(str(result))
            self.expression = str(result)
        except Exception:
            self.display.setText("Error")
            self.expression = ""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())