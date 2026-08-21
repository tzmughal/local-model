import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt Calculator")
        self.setGeometry(100, 100, 300, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.display = QPushButton("0", minimumHeight=50)
        self.display.setEnabled(False)
        self.layout.addWidget(self.display)

        # Add buttons here
        for i in range(1, 10):
            button = QPushButton(str(i))
            button.clicked.connect(lambda value=i: self.on_button_click(value))
            self.layout.addWidget(button)

        zero_button = QPushButton("0")
        zero_button.clicked.connect(lambda: self.on_button_click(0))
        self.layout.addWidget(zero_button)

        # Add other buttons as needed

    def on_button_click(self, value):
        current_text = self.display.text()
        if current_text == "0":
            self.display.setText(str(value))
        else:
            self.display.setText(current_text + str(value))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())