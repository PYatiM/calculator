import math
from PyQt5.QtWidgets import (
    QWidget, QGridLayout, QPushButton, QLineEdit,
    QTextEdit, QVBoxLayout, QLabel, QHBoxLayout, QFileDialog
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from styles import DARK_THEME, LIGHT_THEME
from history_manager import HistoryManager


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced Scientific Calculator")
        self.setGeometry(200, 200, 420, 600)

        self.expression = ""
        self.memory = 0
        self.is_dark = True
        self.history_manager = HistoryManager()

        self.init_ui()
        self.load_history()
        self.apply_theme()

    # ---------- UI Setup ----------
    def init_ui(self):
        main_layout = QVBoxLayout()

        # Display
        self.display = QLineEdit()
        self.display.setFont(QFont("Arial", 20))
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(60)
        main_layout.addWidget(self.display)

        # History
        main_layout.addWidget(QLabel("History"))
        self.history = QTextEdit()
        self.history.setReadOnly(True)
        self.history.setFixedHeight(120)
        main_layout.addWidget(self.history)

        # Top Controls
        top_layout = QHBoxLayout()
        export_btn = QPushButton("Export History")
        export_btn.clicked.connect(self.export_history)
        theme_btn = QPushButton("Toggle Theme")
        theme_btn.clicked.connect(self.toggle_theme)
        top_layout.addWidget(export_btn)
        top_layout.addWidget(theme_btn)
        main_layout.addLayout(top_layout)

        # Buttons
        grid = QGridLayout()
        buttons = [
            ('MC',0,0),('MR',0,1),('M+',0,2),('M-',0,3),('C',0,4),
            ('7',1,0),('8',1,1),('9',1,2),('/',1,3),('√',1,4),
            ('4',2,0),('5',2,1),('6',2,2),('*',2,3),('x²',2,4),
            ('1',3,0),('2',3,1),('3',3,2),('-',3,3),('^',3,4),
            ('0',4,0),('.',4,1),('π',4,2),('+',4,3),('=',4,4),
            ('sin',5,0),('cos',5,1),('tan',5,2),('log',5,3),('ln',5,4),
        ]

        for text, row, col in buttons:
            btn = QPushButton(text)
            btn.setFont(QFont("Arial", 12))
            btn.setFixedSize(70, 50)
            btn.clicked.connect(self.on_button_click)
            grid.addWidget(btn, row, col)

        main_layout.addLayout(grid)
        self.setLayout(main_layout)

    # ---------- Theme Handling ----------
    def apply_theme(self):
        self.setStyleSheet(DARK_THEME if self.is_dark else LIGHT_THEME)

    def toggle_theme(self):
        self.is_dark = not self.is_dark
        self.apply_theme()

    # ---------- History ----------
    def load_history(self):
        for item in self.history_manager.load_history():
            self.history.append(item)

    def export_history(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Export History", "", "Text Files (*.txt)"
        )
        if file_path:
            with open(file_path, "w") as f:
                f.write(self.history.toPlainText())

    # ---------- Button Logic ----------
    def on_button_click(self):
        text = self.sender().text()

        if text == 'C':
            self.expression = ""
            self.display.clear()
        elif text == '=':
            self.calculate()
        elif text == '√':
            self.expression = f"math.sqrt({self.expression})"
            self.display.setText(f"√({self.display.text()})")
        elif text == 'x²':
            self.expression = f"({self.expression})**2"
            self.display.setText(self.display.text() + "²")
        elif text == '^':
            self.expression += "**"
            self.display.setText(self.display.text() + "^")
        elif text in ['sin','cos','tan','log','ln']:
            func_map = {
                'sin': 'math.sin',
                'cos': 'math.cos',
                'tan': 'math.tan',
                'log': 'math.log10',
                'ln': 'math.log'
            }
            self.expression = f"{func_map[text]}({self.expression})"
            self.display.setText(f"{text}({self.display.text()})")
        elif text == 'π':
            self.expression += str(math.pi)
            self.display.setText(self.display.text() + "π")
        elif text == 'MC':
            self.memory = 0
        elif text == 'MR':
            self.expression += str(self.memory)
            self.display.setText(self.display.text() + str(self.memory))
        elif text == 'M+':
            self.memory += float(self.display.text() or 0)
        elif text == 'M-':
            self.memory -= float(self.display.text() or 0)
        else:
            self.expression += text
            self.display.setText(self.display.text() + text)

    # ---------- Calculation ----------
    def calculate(self):
        try:
            result = eval(self.expression, {"__builtins__": None}, {"math": math})
            entry = f"{self.display.text()} = {result}"
            self.history.append(entry)
            self.history_manager.save_entry(entry)
            self.display.setText(str(result))
            self.expression = str(result)
        except Exception:
            self.display.setText("Error")
            self.expression = ""

    # ---------- Keyboard Support ----------
    def keyPressEvent(self, event):
        key = event.text()
        if key in "0123456789+-*/.^":
            self.expression += key
            self.display.setText(self.display.text() + key)
        elif event.key() in (Qt.Key_Return, Qt.Key_Enter):
            self.calculate()
        elif event.key() == Qt.Key_Backspace:
            self.expression = self.expression[:-1]
            self.display.setText(self.display.text()[:-1])