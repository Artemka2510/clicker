import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QProgressBar, QMessageBox
from PyQt5.QtCore import QTimer
class ClickerGame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Кликер")
        self.score, self.energy, self.progress = 0, 5, 0
        self.score_goal, self.max_energy, self.max_progress = 50, 5, 100
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.recover_energy)
        self.timer.start(1000)
        self.init_ui()
    def init_ui(self):
        self.layout = QVBoxLayout()
        self.score_label = QLabel(f"Счет: {self.score}")
        self.energy_bar = QProgressBar(maximum=self.max_energy, value=self.energy)
        self.progress_bar = QProgressBar(maximum=self.max_progress, value=self.progress)
        self.click_button = QPushButton("Клик!")
        self.click_button.clicked.connect(self.increase_score)
        self.layout.addWidget(self.score_label)
        self.layout.addWidget(QLabel("Энергия:"))
        self.layout.addWidget(self.energy_bar)
        self.layout.addWidget(QLabel("Прогресс:"))
        self.layout.addWidget(self.progress_bar)
        self.layout.addWidget(self.click_button)
        self.setLayout(self.layout)
    def increase_score(self):
        if self.energy > 0:
            self.score += 1
            self.energy -= 1
            self.progress += 5
            self.score_label.setText(f"Счет: {self.score}")
            self.energy_bar.setValue(self.energy)
            self.progress_bar.setValue(self.progress)
            if self.score >= self.score_goal:
                QMessageBox.information(self, "Победа", "Вы достигли цели!")
                self.reset_game()
            else:
                QMessageBox.warning(self, "Энергия исчерпана", "Подождите восстановления энергии!")
    def recover_energy(self):
        if self.energy < self.max_energy:
            self.energy += 1
            self.energy_bar.setValue(self.energy)
    def reset_game(self):
        self.score, self.energy, self.progress = 0, self.max_energy, 0
        self.score_label.setText(f"Счет: {self.score}")
        self.energy_bar.setValue(self.energy)
        self.progress_bar.setValue(self.progress)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = ClickerGame()
    game.show()
    sys.exit(app.exec_())