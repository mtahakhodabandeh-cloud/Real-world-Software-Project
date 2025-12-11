import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("InlogPagina")
        self.setFixedSize(500, 400)
        self.setStyleSheet("background-color: #4CAF50;")

        self.bovenform = QLabel("Chem2Go", self)
        self.bovenform.setFixedSize(220, 80)
        self.bovenform.setVisible(True)
        self.bovenform.move(140, 30)
        self.bovenform.setStyleSheet("background-color: #137827; " \
        "border: 2px solid black; font-size: 32px; font-weight: bold; color: white;")
        self.bovenform.setAlignment(Qt.AlignCenter)

        self.LogoBea = QLabel(self)
        pixmap = QPixmap("LogoBea.png")
        pixmap = pixmap.scaled(100, 80)
        self.LogoBea.setPixmap(pixmap)
        self.LogoBea.setScaledContents(True)
        self.LogoBea.move(20, 20)

        self.inlog = QLabel("Vul uw inloggegevens in:", self)
        self.inlog.setFixedSize(250, 20)
        self.inlog.setVisible(True)
        self.inlog.move(130, 130)
        self.inlog.setStyleSheet("font-size: 18px; color: white; font-weight: bold;")

        self.gebruikersnaam = QLineEdit(self)
        self.gebruikersnaam.move(130, 165)
        self.gebruikersnaam.setFixedWidth(250)
        self.gebruikersnaam.setPlaceholderText("Gebruikersnaam")
        self.gebruikersnaam.setStyleSheet("font-size: 17px; color: white;")

        self.wachtwoord = QLineEdit(self)
        self.wachtwoord.setFixedWidth(250)
        self.wachtwoord.move(130, 200)
        self.wachtwoord.setPlaceholderText("Wachtwoord")
        self.wachtwoord.setEchoMode(QLineEdit.Password)
        self.wachtwoord.setStyleSheet("font-size: 17px; color: white;")

        self.announce = QLabel("", self)
        self.announce.setFixedSize(300, 30)
        self.announce.move(130, 270)
        self.announce.setVisible(False)
        self.announce.setStyleSheet("font-size: 15px; color: white;")

        self.verstuur = QPushButton("Verstuur", self)
        self.verstuur.move(140, 240)
        self.verstuur.setFixedSize(130, 30)
        self.verstuur.setStyleSheet("font-size: 14px; font-weight: bold; background-color: lightgray;")
        self.verstuur.clicked.connect(self.login)


    def login(self):
        if self.gebruikersnaam.text() != "" and self.wachtwoord.text() != "":
            if self.gebruikersnaam.text() == "user" and self.wachtwoord.text() == "pass":
                print("Welkom")
            elif self.gebruikersnaam.text() == "admin" and self.wachtwoord.text() == "pass":
                print("Welkom admin")
            else:
                self.announce.setText("Onjuiste inloggegevens.")
                self.announce.setVisible(True)
        else:
            self.announce.setText("Vul alle velden in.")
            self.announce.setVisible(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())