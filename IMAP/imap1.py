#!/usr/bin/env python3

from email.mime.multipart import MIMEMultipart
from PyQt5.Qt import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from email.mime.text import MIMEText
import smtplib
import sys


class window(QWidget):

	def __init__(self):
		super().__init__()

		self.text = QLabel(
				"your username,password, target , message and subject(username is without @gmail.com. but write @gmail.com for target")
		self.user = QLineEdit()
		self.passw = QLineEdit()
		self.passw.setEchoMode(QLineEdit.Password)
		self.target = QLineEdit()
		self.message = QLineEdit()
		self.subject = QLineEdit()
		self.button = QPushButton("Send")

		v_box = QVBoxLayout()
		v_box.addWidget(self.user)
		v_box.addWidget(self.passw)
		v_box.addStretch()
		v_box.addWidget(self.target)
		v_box.addWidget(self.message)
		v_box.addWidget(self.subject)
		v_box.addStretch()
		v_box.addWidget(self.button)
		v_box.addWidget(self.text)
		self.setLayout(v_box)
		self.setWindowTitle("Deneme")
		self.button.clicked.connect(lambda: self.func(
				self.user, self.passw, self.target, self.message, self.subject))

		self.show()

	def func(self, user, passw, target, message, subject):
		mes = MIMEMultipart()
		mes["From"] = "Me"
		mes["To"] = target.text()
		mes["Subject"] = subject.text()

		body = MIMEText(message.text(), "plain")
		mes.attach(body)

		try:
			mail = smtplib.SMTP("smtp.gmail.com", 587)
			mail.ehlo()
			mail.starttls()
			mail.login(user.text(), passw.text())
			mail.sendmail(mes["from"], mes["To"], mes.as_string())
			mail.close()
		except:
			sys.stderr.write("Failed....")
			sys.stderr.flush()


app = QApplication(sys.argv)

objectt = window()


sys.exit(app.exec_())
