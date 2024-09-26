import sys
import random
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PySide6.QtGui import QIcon, QPixmap, QFont
from PySide6.QtCore import Qt, QSize

class NumberGuessingGame(QWidget):
    def __init__(self):
        super().__init__()

        self.target_number = random.randint(1, 100)
        self.attempts = 0

        # Set window icon
        self.setWindowIcon(QIcon("C:/Users/Amrutha/Documents/GitHub/Number_guessing/Number_guessing_game/icon.ico"))

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Num Flex")
        self.setFixedSize(500, 400)  # Set fixed window size

        # Create widgets
        self.label_logo = QLabel(self)
        pixmap = QPixmap("C:/Users/Amrutha/Documents/GitHub/Number_guessing/Number_guessing_game/logo.png")
        pixmap = pixmap.scaled(QSize(100, 100), Qt.AspectRatioMode.KeepAspectRatio)
        self.label_logo.setPixmap(pixmap)
        self.label_logo.setFixedSize(pixmap.size())

        self.label_instruction = QLabel("Guess a number between 1 and 100:")
        self.label_instruction.setFont(QFont("Open Sans", 14, QFont.Bold))
        self.label_instruction.setStyleSheet("color: #333;")

        self.input_guess = QLineEdit()
        self.input_guess.setPlaceholderText("Enter your guess")
        self.input_guess.setFont(QFont("Open Sans", 12))
        self.input_guess.setStyleSheet("padding: 10px; border: 2px solid #3498db; border-radius: 5px;")

        self.button_submit = QPushButton("Submit Guess")
        self.button_submit.setFont(QFont("Open Sans", 12, QFont.Bold))
        self.button_submit.setStyleSheet("background-color: #3498db; color: white; padding: 10px; border: none; border-radius: 5px;")

        self.button_reset = QPushButton("Reset Game")
        self.button_reset.setFont(QFont("Open Sans", 12, QFont.Bold))
        self.button_reset.setStyleSheet("background-color: #f1c40f; color: white; padding: 10px; border: none; border-radius: 5px;")

        self.label_feedback = QLabel("")
        self.label_feedback.setFont(QFont("Open Sans", 12))
        self.label_feedback.setStyleSheet("color: #FF0000;")
        self.label_feedback.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_number_display = QLabel("")
        self.label_number_display.setFont(QFont("Open Sans", 24, QFont.Bold))
        self.label_number_display.setStyleSheet("color: #3498db;")
        self.label_number_display.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Set layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)  # Add spacing around the layout

        logo_layout = QHBoxLayout()
        logo_layout.addWidget(self.label_logo)
        logo_layout.addStretch()
        main_layout.addLayout(logo_layout)

        main_layout.addWidget(self.label_instruction)
        main_layout.addWidget(self.input_guess)
        
        # Layout for number display and feedback
        central_layout = QVBoxLayout()
        central_layout.addWidget(self.label_number_display)
        central_layout.addWidget(self.label_feedback)
        central_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        central_layout.setContentsMargins(0, 20, 0, 20)  # Add spacing around number display and feedback
        main_layout.addLayout(central_layout)

        # Layout for buttons at the bottom
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.button_submit)
        button_layout.addWidget(self.button_reset)
        button_layout.setSpacing(10)
        button_layout.setContentsMargins(0, 0, 0, 10)  # Add bottom margin
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        # Connect the button click events to the functions
        self.button_submit.clicked.connect(self.check_guess)
        self.button_reset.clicked.connect(self.reset_game)

    def check_guess(self):
        try:
            guess = int(self.input_guess.text())
            self.attempts += 1

            if guess > 100 or guess < 1:
                self.label_feedback.setText("Oops!! The number you guessed is out of range.")
                self.label_number_display.setText("")
            elif guess > self.target_number:
                self.label_feedback.setText("Oops!! The number you guessed is too high. Try again.")
                self.label_number_display.setText(f"{guess}")
            elif guess < self.target_number:
                self.label_feedback.setText("Oops!! The number you guessed is too low. Try again.")
                self.label_number_display.setText(f"{guess}")
            else:
                self.label_feedback.setText("")
                self.label_number_display.setText(f"{self.target_number}")
                QMessageBox.information(self, "Congratulations!", 
                                        f"You guessed the number {self.target_number} in {self.attempts} attempts.")
                
                # Comment out or remove reset_game() call from here to allow for manual reset
                # self.reset_game()

        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid number.")

    def reset_game(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.input_guess.clear()
        self.label_feedback.setText("")
        self.label_number_display.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = NumberGuessingGame()
    window.show()

    sys.exit(app.exec())
