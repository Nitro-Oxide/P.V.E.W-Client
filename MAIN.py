import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import Functions
import config
from PyQt5.QtWidgets import QMessageBox
class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PVEW: Environment Viewer")
        self.setLayout(qtw.QVBoxLayout())
        PVEW_label = qtw.QLabel("PVEW")
        PVEW_label.setFont(qtg.QFont('Black Hans Sans', 30))
        self.layout().addWidget(PVEW_label)

        entry = qtw.QLineEdit()
        entry.setObjectName("Email_Grabber")
        entry.setText("Enter Your Email")
        self.layout().addWidget(entry)

        button = qtw.QPushButton("Confirm", clicked = lambda: Button_Press())
        button_demo = qtw.QPushButton("Notificaion Demonstration", clicked = lambda: Demo_Press())
        self.layout().addWidget(button)
        self.layout().addWidget(button_demo)
        self.show()
        
        def Demo_Press():
            print("Button works")
        
            demo = QMessageBox()
            demo.setWindowTitle("Notification")
            demo.setText("This is a notification demo")
            demo.exec_()
        
        def Button_Press():
            button.setText("Refresh")
            curr = Functions.Air_Quality()
            post_label = qtw.QLabel(f""""
            Wind Speed: {config.data_ws},{Functions.check_wind(entry.text)}
            Temperature: {config.data_temp - 273} centigrade, {Functions.check_temp(entry.text)}
            Rain: {config.data_rf}%, {Functions.check_rain(entry.text)}
            Air Quality: {curr.check_air(entry.text)}
                                    """)
            self.layout().addWidget(post_label)
            

            
app = qtw.QApplication([])
mw = MainWindow()

app.exec_()