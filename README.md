# 🧮 Advanced Scientific Calculator (PyQt5)

A modern and intermediate-level desktop calculator application built using **PyQt5**.  
This project demonstrates GUI development, modular design, and safe evaluation of mathematical expressions.

## ✨ Features

- 🧮 Basic arithmetic operations (+, −, ×, ÷)
- 🔬 Scientific functions (sin, cos, tan, log, ln, √, power)
- 💾 Memory operations (MC, MR, M+, M−)
- 📜 Persistent calculation history
- 🌗 Light and Dark theme switching
- 📤 Export history to a text file
- ⌨️ Keyboard input support
- 🛡️ Safe expression evaluation
- 🧩 Modular and maintainable code structure

## 📁 Project Structure
calculator_app/
├── main.py # Application entry point
├── calculator.py # GUI and controller logic
├── history_manager.py # Handles persistent history
├── styles.py # Light and dark themes


## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/advanced-calculator.git
   cd advanced-calculator

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt

3. Run the application
    
    ```bash
    python main.py

## 🛠️ Technologies Used
    Python 3
    PyQt5 – GUI framework
    Math Module – Scientific computations
    File Handling – Persistent history storage

## 📦 Packaging 

    To create a standalone executable:

    ```bash
    pip install pyinstaller
    pyinstaller --onefile --windowed main.py