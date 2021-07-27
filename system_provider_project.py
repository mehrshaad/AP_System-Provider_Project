import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import css
import pics_rc
import func
import func_2
import func_3
try:
    from pynotifier import Notification
except:
    import subprocess  # gg
    subprocess.call(['pip', 'install', 'win10toast'])
    subprocess.call(['pip', 'install', 'py-notifier'])
    from pynotifier import Notification

signed_up = False  # age true bood ejaze estefade az app dare
moshtari = None  # age false bood yani moshtari nist (khadamatie)
username = ''


def sendNotification(Text, Title='System Provider Application', Duration=3):
    try:
        Notification(
            title='System Provider Application',
            description=Text,
            icon_path='./images/icon.ico',
            duration=Duration,
        ).send()
    except:
        print(Text[::-1])


class Controller:

    def __init__(self):
        self.welcome = Ui_Welcome()
        self.menu = Ui_menu()
        self.login = Ui_Login()
        self.su_moshtari = Ui_SignUpMoshtari()
        self.su_khadamat = Ui_SignUpKhadamat()
        self.su_khadamat2 = Ui_SignUpKhadamat2()
        self.omor_mali = Ui_omor_mali()
        self.hazf = Ui_hazf()
        self.eshterak = Ui_printEshterak()
        self.sefaresh = Ui_request_for_work()
        self.sod = Ui_sod()

    def show_welcome(self):
        self.welcome.setupUi(self.welcome.window)
        self.welcome.window.show()

    def show_main(self):
        self.welcome.window.close()
        self.menu.setupUi(self.menu.window)
        self.menu.window.show()

    def show_login(self):
        self.menu.window.close()
        self.login.setupUi(self.login.window)
        self.login.window.show()

    def show_eshterak(self):
        global signed_up, moshtari
        if signed_up and moshtari:
            self.eshterak.setupUi(self.eshterak.window)
            self.eshterak.window.show()
        elif not moshtari:
            sendNotification('فقط برای افراد مشتری')
        else:
            sendNotification('شما هنوز وارد نشدید')

    def show_hazf(self):
        global signed_up, moshtari
        if signed_up and not moshtari:
            self.hazf.setupUi(self.hazf.window)
            self.hazf.window.show()
        elif moshtari:
            sendNotification('فقط برای افراد خدماتی')
        else:
            sendNotification('شما هنوز وارد نشدید')

    def show_sod(self):
        self.sod = Ui_sod()
        self.sod.setupUi(self.sod.window)
        self.sod.window.show()

    def close_eshterak(self):
        self.eshterak.window.close()

    def close_hazf(self):
        self.hazf.window.close()

    def from_menu_to_su_moshtari(self):
        self.menu.window.close()
        self.su_moshtari.setupUi(self.su_moshtari.window)
        self.su_moshtari.window.show()

    def from_menu_to_su_khadamat(self):
        self.menu.window.close()
        self.su_khadamat.setupUi(self.su_khadamat.window)
        self.su_khadamat.window.show()

    def from_menu_to_omor_mali(self):
        self.menu.window.close()
        self.omor_mali.setupUi(self.omor_mali.window)
        self.omor_mali.window.show()

    def from_menu_to_sefaresh(self):
        global signed_up, moshtari
        if signed_up and moshtari:
            self.menu.window.close()
            self.sefaresh.setupUi(self.sefaresh.window)
            self.sefaresh.window.show()
        else:
            sendNotification('فقط برای افراد مشتری')

    def from_moshtari_to_menu(self):
        self.su_moshtari.window.close()
        self.menu.setupUi(self.menu.window)
        self.menu.window.show()

    def from_khadamat_to_menu(self):
        self.su_khadamat.window.close()
        self.menu.setupUi(self.menu.window)
        self.menu.window.show()

    def from_khadamat2_to_menu(self):
        self.su_khadamat2.window.close()
        self.menu.setupUi(self.menu.window)
        self.menu.window.show()

    def from_login_to_menu(self):
        self.login.window.close()
        self.menu.setupUi(self.menu.window)
        self.menu.window.show()

    def from_khadamat_to_khadamat2(self):
        self.su_khadamat.window.close()
        self.su_khadamat2.setupUi(self.su_khadamat2.window)
        self.su_khadamat2.window.show()

    def from_khadamat2_to_khadamat(self):
        self.su_khadamat2.window.close()
        self.su_khadamat.setupUi(self.su_khadamat.window)
        self.su_khadamat.window.show()

    def from_omor_mali_to_menu(self):
        self.omor_mali.window.close()
        self.menu.setupUi(self.menu.window)
        self.menu.window.show()

    def sefaresh_to_menu(self):
        self.sefaresh.window.close()
        self.menu.setupUi(self.menu.window)
        self.menu.window.show()


class Ui_Welcome(object):
    def __init__(self):
        self.window = QtWidgets.QMainWindow()

    def setupUi(self, Welcome):
        self.key = False
        Welcome.setObjectName("Welcome")
        Welcome.resize(800, 600)
        Welcome.setMinimumSize(QtCore.QSize(800, 600))
        Welcome.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(24)
        Welcome.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/background/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Welcome.setWindowIcon(icon)
        Welcome.setStyleSheet("")
        self.progressBar = QtWidgets.QProgressBar(Welcome)
        self.progressBar.setGeometry(QtCore.QRect(10, 570, 781, 23))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(1)
        self.progressBarTime = 25
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(True)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.timer = QTimer()
        self.timer.timeout.connect(self.load)
        self.timer.start(self.progressBarTime)
        self.temp1Label = QtWidgets.QLabel(Welcome)
        self.temp1Label.setGeometry(QtCore.QRect(490, 540, 291, 31))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(18)
        self.temp1Label.setFont(font)
        self.temp1Label.setStyleSheet("color:white;")
        self.temp1Label.setObjectName("temp1Label")
        self.bgWelcome = QtWidgets.QLabel(Welcome)
        self.bgWelcome.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.bgWelcome.setMinimumSize(QtCore.QSize(800, 600))
        self.bgWelcome.setMaximumSize(QtCore.QSize(800, 600))
        self.bgWelcome.setText("")
        self.bgWelcome.setPixmap(QtGui.QPixmap(":/background/leaf_blur.jpg"))
        self.bgWelcome.setObjectName("bgWelcome")
        self.temp2Label = QtWidgets.QLabel(Welcome)
        self.temp2Label.setGeometry(QtCore.QRect(100, 20, 601, 81))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.temp2Label.setFont(font)
        self.temp2Label.setStyleSheet(css.welcome)
        self.temp2Label.setAlignment(QtCore.Qt.AlignCenter)
        self.temp2Label.setObjectName("temp2Label")
        self.bgWelcome.raise_()
        self.progressBar.raise_()
        self.temp1Label.raise_()
        self.temp2Label.raise_()
        self.retranslateUi(Welcome)
        QtCore.QMetaObject.connectSlotsByName(Welcome)

    def retranslateUi(self, Welcome):
        _translate = QtCore.QCoreApplication.translate
        Welcome.setWindowTitle(_translate("Welcome", "Form"))
        self.temp1Label.setText(_translate("Welcome", "در حال خواندن داده ها"))
        self.temp2Label.setText(_translate("Welcome", "خوش آمدید"))

    def load(self):
        value = self.progressBar.value()
        if value < 100:
            value = value + 1
            self.progressBar.setValue(value)
        else:
            self.timer.stop()
            self.switchMenu()

    def switchMenu(self):
        Page.show_main()


class Ui_menu(object):
    def __init__(self):
        self.window = QtWidgets.QMainWindow()

    def setupUi(self, menu):
        global moshtari, signed_up
        self.menu = QtWidgets.QLabel(menu)
        self.menu.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.menu.setMinimumSize(QtCore.QSize(800, 600))
        self.menu.setMaximumSize(QtCore.QSize(800, 600))
        self.menu.setText("")
        self.menu.setPixmap(QtGui.QPixmap("./images/8.jpg"))
        self.menu.setObjectName("omor_mali")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/background/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        menu.setWindowIcon(icon)
        menu.setObjectName("omor_malli")
        menu.resize(800, 600)
        menu.setMinimumSize(QtCore.QSize(800, 600))
        menu.setMaximumSize(QtCore.QSize(800, 600))
        menu.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(menu)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(120, 100, 587, 391))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hazfoezafe = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(22)
        self.hazfoezafe.setFont(font)
        self.hazfoezafe.setStyleSheet(css.menu_button)
        self.hazfoezafe.clicked.connect(self.switchto__hazf)
        self.hazfoezafe.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.hazfoezafe.setObjectName("hazfoezafe")
        self.verticalLayout.addWidget(self.hazfoezafe)
        self.eshterak = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(22)
        self.eshterak.setFont(font)
        self.eshterak.clicked.connect(self.switchto__Ui_printEshterak)
        self.eshterak.setStyleSheet(css.menu_button)
        self.eshterak.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.eshterak.setObjectName("eshterak")
        self.verticalLayout.addWidget(self.eshterak)
        self.khadamat = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(22)
        self.khadamat.setFont(font)
        self.khadamat.setStyleSheet(css.menu_button)
        self.khadamat.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.khadamat.setObjectName("khadamat")
        self.verticalLayout.addWidget(self.khadamat)
        self.omor_mali = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(22)
        self.omor_mali.setFont(font)
        self.omor_mali.setStyleSheet(css.menu_button)
        self.omor_mali.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.omor_mali.setObjectName("omor_mali")
        self.verticalLayout.addWidget(self.omor_mali)
        self.khoroj = QtWidgets.QPushButton(self.centralwidget)
        self.khoroj.setGeometry(QtCore.QRect(120, 510, 151, 41))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(22)
        self.khoroj.setFont(font)
        self.khoroj.setStyleSheet(css.menu_exit_button)
        self.khoroj.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.khoroj.setObjectName("menu")
        self.khoroj.clicked.connect(self.exit)
        # self.pushButton_2 = QtWidgets.QLabel(menu) #mituni text ino center koni? text align nabod? na ba qt on kar nkrd
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)  # khob mehrshad ye kari kon mokhtasatesho jabeja kon hmmm
        self.pushButton_2.setGeometry(QtCore.QRect(310, 20, 191, 41))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(22)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet('color:red; background-color:lightblue;border:0px;border-radius:10px')
        menu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(menu)
        self.menubar.setObjectName("menubar")
        self.menubar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        if not signed_up:
            self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
            self.menu_2 = QtWidgets.QMenu(self.menubar)
            self.menu_2.setObjectName("menu_2")
            self.menu_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            menu.setMenuBar(self.menubar)
            self.statusbar = QtWidgets.QStatusBar(menu)
            self.statusbar.setObjectName("statusbar")
            menu.setStatusBar(self.statusbar)
            self.action = QtWidgets.QAction(menu)
            self.action.setObjectName("action")
            # link to login page
            self.action.triggered.connect(self.switchto__login)
            self.action_2 = QtWidgets.QAction(menu)
            self.action_2.triggered.connect(self.switchto__signup_moshtari)
            self.action_2.setObjectName("action_2")
            self.action_3 = QtWidgets.QAction(menu)
            self.action_3.triggered.connect(self.switchto__signup_khadamati)
            self.action_3.setObjectName("action_3")
            self.menu_2.addAction(self.action)
            self.menu_2.addAction(self.action_2)
            self.menu_2.addAction(self.action_3)
            self.menubar.addAction(self.menu_2.menuAction())
        else:
            self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 0))
        self.retranslateUi(menu)
        QtCore.QMetaObject.connectSlotsByName(menu)

        self.omor_mali.clicked.connect(self.switchto__pop_sod)
        self.khadamat.clicked.connect(self.switchto__Ui_request_for_work)

    def exit(self):
        sys.exit()

    def retranslateUi(self, menu):
        global signed_up, moshtari, username
        _translate = QtCore.QCoreApplication.translate
        menu.setWindowTitle(_translate("menu", "منو"))
        self.hazfoezafe.setText(_translate("menu", "حذف و اضافه نیروی خدماتی ( ویژه کارکنان )"))
        self.eshterak.setText(_translate("menu", "درخواست برای شماره اشتراک ( ویژه مشتریان )"))
        self.khadamat.setText(_translate("menu", "ثبت خدمات انجام شده"))
        self.omor_mali.setText(_translate("menu", "گزارش سود"))
        self.khoroj.setText(_translate("menu", "خروج از برنامه"))
        self.pushButton_2.setAccessibleDescription(_translate("menu", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        if not signed_up:
            self.pushButton_2.setText(_translate("menu", "به منو خوش آمدید"))
            self.menu_2.setTitle(_translate("menu", "ورود"))
            self.action.setText(_translate("menu", "ورود به پنل"))
            self.action_2.setText(_translate("menu", "ثبت نام به عنوان مشتری"))
            self.action_3.setText(_translate("menu", "ثبت نام به عنوان نیروی خدماتی"))
        elif moshtari:
            self.pushButton_2.setText(_translate("menu", f"خوش آمدید {func.get_name(username)}"))
        else:
            self.pushButton_2.setText(_translate("menu", f"خوش آمدید {func_2.get_name(username)}"))

    def switchto__login(self):
        Page.show_login()

    def switchto__signup_moshtari(self):
        Page.from_menu_to_su_moshtari()

    def switchto__signup_khadamati(self):
        Page.from_menu_to_su_khadamat()

    def switchto__pop_sod(self):
        Page.show_sod()

    def switchto__hazf(self):
        Page.show_hazf()

    def switchto__Ui_printEshterak(self):
        Page.show_eshterak()

    def switchto__Ui_request_for_work(self):  # kiyan ino seda kon
        Page.from_menu_to_sefaresh()


class Ui_Login(object):
    def __init__(self):
        self.window = QtWidgets.QMainWindow()

    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(800, 600)
        Login.setMinimumSize(QtCore.QSize(800, 600))
        Login.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        Login.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/background/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login.setWindowIcon(icon)
        Login.setLayoutDirection(QtCore.Qt.RightToLeft)
        Login.setAutoFillBackground(False)
        Login.setStyleSheet("sign_up{\nbackground-color:black;\n}")
        self.MainLabelLogin = QtWidgets.QLabel(Login)
        self.MainLabelLogin.setGeometry(QtCore.QRect(175, 20, 450, 61))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.MainLabelLogin.setFont(font)
        self.MainLabelLogin.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.MainLabelLogin.setStyleSheet(css.sign_up_main_label)
        self.MainLabelLogin.setTextFormat(QtCore.Qt.PlainText)
        self.MainLabelLogin.setAlignment(QtCore.Qt.AlignCenter)
        self.MainLabelLogin.setObjectName("MainLabelLogin")
        self.BgLogin = QtWidgets.QLabel(Login)
        self.BgLogin.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.BgLogin.setMinimumSize(QtCore.QSize(800, 600))
        self.BgLogin.setMaximumSize(QtCore.QSize(800, 600))
        self.BgLogin.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.BgLogin.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.BgLogin.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.BgLogin.setText("")
        self.BgLogin.setPixmap(QtGui.QPixmap(":/background/sky_blur.jpg"))
        self.BgLogin.setWordWrap(False)
        self.BgLogin.setObjectName("BgLogin")
        self.ButtonNextLogin = QtWidgets.QPushButton(Login)
        self.ButtonNextLogin.setGeometry(QtCore.QRect(290, 510, 220, 51))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(34)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ButtonNextLogin.setFont(font)
        self.ButtonNextLogin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonNextLogin.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.ButtonNextLogin.setAutoFillBackground(False)
        self.ButtonNextLogin.setStyleSheet(css.button_false)
        self.ButtonNextLogin.setCheckable(False)
        self.ButtonNextLogin.setAutoExclusive(False)
        self.ButtonNextLogin.setAutoDefault(False)
        self.ButtonNextLogin.setDefault(False)
        self.ButtonNextLogin.setFlat(False)
        self.ButtonNextLogin.setObjectName("ButtonNextLogin")
        self.ButtonBackLogin = QtWidgets.QPushButton(Login)
        self.ButtonBackLogin.setGeometry(QtCore.QRect(20, 20, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonBackLogin.setFont(font)
        self.ButtonBackLogin.clicked.connect(self.switchto__menu)
        self.ButtonBackLogin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonBackLogin.setStyleSheet(css.back_button)
        self.ButtonBackLogin.setObjectName("ButtonBackLogin")
        self.BgLogin_2 = QtWidgets.QLabel(Login)
        self.BgLogin_2.setGeometry(QtCore.QRect(110, 50, 580, 530))
        self.BgLogin_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0.119318, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(82, 82, 82, 255));\n"
                                     "border-radius: 26px;")
        self.BgLogin_2.setText("")
        self.BgLogin_2.setObjectName("BgLogin_2")
        self.PassLineEditLogin = QtWidgets.QLineEdit(Login)
        self.PassLineEditLogin.setGeometry(QtCore.QRect(190, 430, 431, 61))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.PassLineEditLogin.setFont(font)
        self.PassLineEditLogin.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PassLineEditLogin.setStyleSheet(css.line_edit_false)
        self.PassLineEditLogin.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.PassLineEditLogin.setMaxLength(16)
        self.PassLineEditLogin.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PassLineEditLogin.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.PassLineEditLogin.setDragEnabled(True)
        self.PassLineEditLogin.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.PassLineEditLogin.setClearButtonEnabled(True)
        self.PassLineEditLogin.setObjectName("PassLineEditLogin")
        self.UserLineEditLogin = QtWidgets.QLineEdit(Login)
        self.UserLineEditLogin.setGeometry(QtCore.QRect(190, 260, 431, 61))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.UserLineEditLogin.setFont(font)
        self.UserLineEditLogin.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.UserLineEditLogin.setStyleSheet(css.line_edit_basic)
        self.UserLineEditLogin.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.UserLineEditLogin.setMaxLength(25)
        self.UserLineEditLogin.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.UserLineEditLogin.setDragEnabled(True)
        self.UserLineEditLogin.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.UserLineEditLogin.setClearButtonEnabled(True)
        self.UserLineEditLogin.setObjectName("UserLineEditLogin")
        self.UserLabelLogin = QtWidgets.QLabel(Login)
        self.UserLabelLogin.setGeometry(QtCore.QRect(280, 180, 381, 61))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.UserLabelLogin.setFont(font)
        self.UserLabelLogin.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.UserLabelLogin.setAutoFillBackground(False)
        self.UserLabelLogin.setStyleSheet(css.login_labels)
        self.UserLabelLogin.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.UserLabelLogin.setObjectName("UserLabelLogin")
        self.PassLabelLogin = QtWidgets.QLabel(Login)
        self.PassLabelLogin.setGeometry(QtCore.QRect(280, 350, 381, 61))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.PassLabelLogin.setFont(font)
        self.PassLabelLogin.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.PassLabelLogin.setAutoFillBackground(False)
        self.PassLabelLogin.setStyleSheet(css.login_labels)
        self.PassLabelLogin.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.PassLabelLogin.setObjectName("PassLabelLogin")
        self.radioButton = QtWidgets.QRadioButton(Login)
        self.radioButton.setGeometry(QtCore.QRect(325, 100, 151, 41))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(25)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("color:white;")
        self.radioButton.setIconSize(QtCore.QSize(22, 22))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.temp1label = QtWidgets.QLabel(Login)
        self.temp1label.setGeometry(QtCore.QRect(140, 100, 521, 51))
        self.temp1label.setStyleSheet(css.login_labels)
        self.temp1label.setText("")
        self.temp1label.setObjectName("temp1label")
        self.BgLogin.raise_()
        self.ButtonBackLogin.raise_()
        self.BgLogin_2.raise_()
        self.ButtonNextLogin.raise_()
        self.MainLabelLogin.raise_()
        self.PassLineEditLogin.raise_()
        self.UserLineEditLogin.raise_()
        self.UserLabelLogin.raise_()
        self.PassLabelLogin.raise_()
        self.temp1label.raise_()
        self.radioButton.raise_()

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)
        Login.setTabOrder(self.UserLineEditLogin, self.PassLineEditLogin)
        Login.setTabOrder(self.PassLineEditLogin, self.ButtonNextLogin)
        Login.setTabOrder(self.ButtonNextLogin, self.ButtonBackLogin)

        self.usernameKey = False
        self.passwordKey = False
        self.radioKey = True
        self.UserLineEditLogin.textChanged.connect(self.checkLogin)
        self.PassLineEditLogin.textChanged.connect(self.checkLogin)
        self.ButtonNextLogin.clicked.connect(self.otherButtonStuff)
        self.radioButton.toggled.connect(lambda: self.checkRadioButton(self.radioButton))
        self.radioButton.toggled.connect(lambda: self.checkLogin())

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Sign Up Form"))
        self.MainLabelLogin.setText(_translate("Login", "صفحه ورود"))
        self.ButtonNextLogin.setText(_translate("Login", "ورود"))
        self.ButtonBackLogin.setText(_translate("Login", "<"))
        self.PassLineEditLogin.setPlaceholderText(_translate("Login", " حداقل8 کاراکتر"))
        self.UserLineEditLogin.setPlaceholderText(_translate("Login", " حداکثر25 کاراکتر"))
        self.UserLabelLogin.setText(_translate("Login", "  شماره اشتراک یا نام کاربری:"))
        self.PassLabelLogin.setText(_translate("Login", "  رمز عبور:"))
        self.radioButton.setText(_translate("Login", "مشتری هستم"))

    def checkLogin(self):
        pas = self.PassLineEditLogin
        user = self.UserLineEditLogin

        if self.radioKey:
            self.usernameKey, self.passwordKey = func_2.check_login(str(user.text()), str(pas.text()))
        else:
            self.usernameKey, self.passwordKey = func.check_login(str(user.text()), str(pas.text()))

        if self.usernameKey:
            user.setStyleSheet(css.line_edit_correct)
        else:
            user.setStyleSheet(css.line_edit_false)

        if self.usernameKey and self.passwordKey:
            pas.setStyleSheet(css.line_edit_correct)
            self.ButtonNextLogin.setStyleSheet(css.button_true)
        else:
            pas.setStyleSheet(css.line_edit_false)
            self.ButtonNextLogin.setStyleSheet(css.button_false)

    def checkRadioButton(self, radioButt):
        if radioButt.isChecked() == True:
            self.radioKey = True
        else:
            self.radioKey = False

    def checkLineEdit(self):
        obj = self.UserLineEditLogin
        if len(str(obj.text())) > 2:
            obj.setStyleSheet(css.line_edit_correct)
            self.usernameKey = True
        else:
            obj.setStyleSheet(css.line_edit_false)
            self.usernameKey = False

    def otherButtonStuff(self):
        global signed_up, moshtari, username
        if self.usernameKey and self.passwordKey:
            if self.radioKey:
                sendNotification(f'سلام {func_2.get_name(str(self.UserLineEditLogin.text()))}')
                moshtari = True
                signed_up = True
                username = str(self.UserLineEditLogin.text())
            else:
                sendNotification(f'سلام {func.get_name(str(self.UserLineEditLogin.text()))}')
                moshtari = False
                signed_up = True
                username = str(self.UserLineEditLogin.text())
            Page.from_login_to_menu()

    def switchto__menu(self):
        Page.from_login_to_menu()


class Ui_hazf(object):
    def __init__(self):
        self.window = QtWidgets.QMainWindow()

    def setupUi(self, hazf):
        hazf.setObjectName("hazf")
        hazf.resize(250, 200)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/background/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        hazf.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(hazf)
        self.label.setGeometry(QtCore.QRect(26, 40, 201, 41))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 16pt \"B Badr\";")
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(hazf)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 100, 231, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.yes = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.yes.setObjectName("yes")
        self.horizontalLayout.addWidget(self.yes)
        self.no = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.no.setObjectName("no")
        self.horizontalLayout.addWidget(self.no)

        self.retranslateUi(hazf)
        QtCore.QMetaObject.connectSlotsByName(hazf)

        self.yes.clicked.connect(self.datahazf)
        self.no.clicked.connect(self.closeWindow)

    def retranslateUi(self, hazf):
        _translate = QtCore.QCoreApplication.translate
        hazf.setWindowTitle(_translate("hazf", "حذف نیروی خدماتی"))
        self.label.setText(_translate("hazf", "آیا از حذف خود اطمینان دارید؟!"))
        self.yes.setText(_translate("hazf", "بله"))
        self.no.setText(_translate("hazf", "خیر"))

    def datahazf(self):
        global username
        func.del_row(username)

    def closeWindow(self):
        Page.close_hazf()


class Ui_printEshterak(object):
    def __init__(self):
        self.window = QtWidgets.QMainWindow()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(320, 240)
        Form.setMinimumSize(QtCore.QSize(320, 240))
        Form.setMaximumSize(QtCore.QSize(320, 240))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/background/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(200, 10, 111, 221))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(13)
        self.verticalLayoutWidget.setFont(font)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 191, 221))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(13)
        self.verticalLayoutWidget_2.setFont(font)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(13)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        global username
        self.information = func_2.hamash(username)
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form", "نام:"))
        self.label_7.setText(_translate("Form", "نام خانوادگی:"))
        self.label_8.setText(_translate("Form", "شماره تماس:"))
        self.label_10.setText(_translate("Form", "شماره اشتراک:"))
        self.label_9.setText(_translate("Form", "نام کاربری:"))
        self.label_11.setText(_translate("Form", "رمز عبور:"))
        self.label.setText(_translate("Form", f"{self.information[1]}"))
        self.label_2.setText(_translate("Form", f"{self.information[2]}"))
        self.label_3.setText(_translate("Form", f"0{self.information[3]}"))
        self.label_4.setText(_translate("Form", f"{self.information[0]}"))
        self.label_5.setText(_translate("Form", f"{self.information[4]}"))
        self.label_12.setText(_translate("Form", f"{self.information[5]}"))


class Ui_SignUpMoshtari(object):
    def __init__(self):
        self.window = QtWidgets.QMainWindow()

    def setupUi(self, SignUpMoshtari):
        SignUpMoshtari.setObjectName("SignUpMoshtari")
        SignUpMoshtari.resize(800, 600)
        SignUpMoshtari.setMinimumSize(QtCore.QSize(800, 600))
        SignUpMoshtari.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        SignUpMoshtari.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/background/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SignUpMoshtari.setWindowIcon(icon)
        SignUpMoshtari.setLayoutDirection(QtCore.Qt.RightToLeft)
        SignUpMoshtari.setAutoFillBackground(False)
        SignUpMoshtari.setStyleSheet("sign_up{\n"
                                     "background-color:black;\n"
                                     "}")
        self.MainLabelMoshtari = QtWidgets.QLabel(SignUpMoshtari)
        self.MainLabelMoshtari.setGeometry(QtCore.QRect(175, 20, 450, 61))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.MainLabelMoshtari.setFont(font)
        self.MainLabelMoshtari.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.MainLabelMoshtari.setStyleSheet(css.sign_up_main_label)
        self.MainLabelMoshtari.setTextFormat(QtCore.Qt.PlainText)
        self.MainLabelMoshtari.setAlignment(QtCore.Qt.AlignCenter)
        self.MainLabelMoshtari.setObjectName("MainLabelMoshtari")
        self.NameLabelMoshtari = QtWidgets.QLabel(SignUpMoshtari)
        self.NameLabelMoshtari.setGeometry(QtCore.QRect(540, 110, 191, 61))
        self.NameLabelMoshtari.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.NameLabelMoshtari.setStyleSheet(css.sign_up_small_labels)
        self.NameLabelMoshtari.setAlignment(QtCore.Qt.AlignCenter)
        self.NameLabelMoshtari.setObjectName("NameLabelMoshtari")
        self.BgMoshtari = QtWidgets.QLabel(SignUpMoshtari)
        self.BgMoshtari.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.BgMoshtari.setMinimumSize(QtCore.QSize(800, 600))
        self.BgMoshtari.setMaximumSize(QtCore.QSize(800, 600))
        self.BgMoshtari.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.BgMoshtari.setStyleSheet("")
        self.BgMoshtari.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.BgMoshtari.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.BgMoshtari.setText("")
        self.BgMoshtari.setPixmap(QtGui.QPixmap(":/background/desert2_blur.jpg"))
        self.BgMoshtari.setWordWrap(False)
        self.BgMoshtari.setObjectName("BgMoshtari")
        self.NameLineEditMoshtari = QtWidgets.QLineEdit(SignUpMoshtari)
        self.NameLineEditMoshtari.setGeometry(QtCore.QRect(70, 110, 431, 61))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.NameLineEditMoshtari.setFont(font)
        self.NameLineEditMoshtari.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.NameLineEditMoshtari.setStyleSheet(css.line_edit_basic)
        self.NameLineEditMoshtari.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.NameLineEditMoshtari.setMaxLength(15)
        self.NameLineEditMoshtari.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.NameLineEditMoshtari.setDragEnabled(True)
        self.NameLineEditMoshtari.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.NameLineEditMoshtari.setClearButtonEnabled(True)
        self.NameLineEditMoshtari.setObjectName("NameLineEditMoshtari")
        self.FamilyLineEditMoshtari = QtWidgets.QLineEdit(SignUpMoshtari)
        self.FamilyLineEditMoshtari.setGeometry(QtCore.QRect(70, 190, 431, 61))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.FamilyLineEditMoshtari.setFont(font)
        self.FamilyLineEditMoshtari.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.FamilyLineEditMoshtari.setStyleSheet(css.line_edit_basic)
        self.FamilyLineEditMoshtari.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.FamilyLineEditMoshtari.setMaxLength(20)
        self.FamilyLineEditMoshtari.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.FamilyLineEditMoshtari.setDragEnabled(True)
        self.FamilyLineEditMoshtari.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.FamilyLineEditMoshtari.setClearButtonEnabled(True)
        self.FamilyLineEditMoshtari.setObjectName("FamilyLineEditMoshtari")
        self.ButtonNextMoshtari = QtWidgets.QPushButton(SignUpMoshtari)
        self.ButtonNextMoshtari.setGeometry(QtCore.QRect(290, 519, 220, 71))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(34)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ButtonNextMoshtari.setFont(font)
        self.ButtonNextMoshtari.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.ButtonNextMoshtari.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.ButtonNextMoshtari.setAutoFillBackground(False)
        self.ButtonNextMoshtari.setStyleSheet(css.button_invisible)
        self.ButtonNextMoshtari.setCheckable(False)
        self.ButtonNextMoshtari.setAutoExclusive(False)
        self.ButtonNextMoshtari.setAutoDefault(False)
        self.ButtonNextMoshtari.setDefault(False)
        self.ButtonNextMoshtari.setFlat(False)
        self.ButtonNextMoshtari.setObjectName("ButtonNextMoshtari")
        self.ButtonMoshtari = QtWidgets.QPushButton(SignUpMoshtari)
        # linking to menu page
        self.ButtonMoshtari.clicked.connect(self.switchto__menu)
        self.ButtonMoshtari.setGeometry(QtCore.QRect(20, 20, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonMoshtari.setFont(font)
        self.ButtonMoshtari.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonMoshtari.setStyleSheet(css.back_button)
        self.ButtonMoshtari.setObjectName("ButtonMoshtari")
        self.FamilyLabelMoshtari = QtWidgets.QLabel(SignUpMoshtari)
        self.FamilyLabelMoshtari.setGeometry(QtCore.QRect(540, 190, 191, 61))
        self.FamilyLabelMoshtari.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.FamilyLabelMoshtari.setStyleSheet(css.sign_up_small_labels)
        self.FamilyLabelMoshtari.setAlignment(QtCore.Qt.AlignCenter)
        self.FamilyLabelMoshtari.setObjectName("FamilyLabelMoshtari")
        self.PhoneLabelMoshtari = QtWidgets.QLabel(SignUpMoshtari)
        self.PhoneLabelMoshtari.setGeometry(QtCore.QRect(540, 270, 191, 61))
        self.PhoneLabelMoshtari.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.PhoneLabelMoshtari.setStyleSheet(css.sign_up_small_labels)
        self.PhoneLabelMoshtari.setAlignment(QtCore.Qt.AlignCenter)
        self.PhoneLabelMoshtari.setObjectName("PhoneLabelMoshtari")
        self.PhoneLineEditMoshtari = QtWidgets.QLineEdit(SignUpMoshtari)
        self.PhoneLineEditMoshtari.setGeometry(QtCore.QRect(70, 270, 431, 61))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.PhoneLineEditMoshtari.setFont(font)
        self.PhoneLineEditMoshtari.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PhoneLineEditMoshtari.setStyleSheet(css.line_edit_basic)
        self.PhoneLineEditMoshtari.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.PhoneLineEditMoshtari.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.PhoneLineEditMoshtari.setMaxLength(11)
        self.PhoneLineEditMoshtari.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.PhoneLineEditMoshtari.setDragEnabled(True)
        self.PhoneLineEditMoshtari.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.PhoneLineEditMoshtari.setClearButtonEnabled(True)
        self.PhoneLineEditMoshtari.setObjectName("PhoneLineEditMoshtari")
        self.PassLabelMoshtari = QtWidgets.QLabel(SignUpMoshtari)
        self.PassLabelMoshtari.setGeometry(QtCore.QRect(540, 430, 191, 61))
        self.PassLabelMoshtari.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.PassLabelMoshtari.setStyleSheet(css.sign_up_small_labels)
        self.PassLabelMoshtari.setAlignment(QtCore.Qt.AlignCenter)
        self.PassLabelMoshtari.setObjectName("PassLabelMoshtari")
        self.PassLineEditMoshtari = QtWidgets.QLineEdit(SignUpMoshtari)
        self.PassLineEditMoshtari.setGeometry(QtCore.QRect(70, 430, 431, 61))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.PassLineEditMoshtari.setFont(font)
        self.PassLineEditMoshtari.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PassLineEditMoshtari.setStyleSheet(css.line_edit_false)
        self.PassLineEditMoshtari.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.PassLineEditMoshtari.setMaxLength(16)
        self.PassLineEditMoshtari.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.PassLineEditMoshtari.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.PassLineEditMoshtari.setDragEnabled(True)
        self.PassLineEditMoshtari.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.PassLineEditMoshtari.setClearButtonEnabled(True)
        self.PassLineEditMoshtari.setObjectName("PassLineEditMoshtari")
        self.UserLabelMoshtari = QtWidgets.QLabel(SignUpMoshtari)
        self.UserLabelMoshtari.setGeometry(QtCore.QRect(540, 350, 191, 61))
        self.UserLabelMoshtari.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.UserLabelMoshtari.setStyleSheet(css.sign_up_small_labels)
        self.UserLabelMoshtari.setAlignment(QtCore.Qt.AlignCenter)
        self.UserLabelMoshtari.setObjectName("UserLabelMoshtari")
        self.UserLineEditMoshtari = QtWidgets.QLineEdit(SignUpMoshtari)
        self.UserLineEditMoshtari.setGeometry(QtCore.QRect(70, 350, 431, 61))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.UserLineEditMoshtari.setFont(font)
        self.UserLineEditMoshtari.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.UserLineEditMoshtari.setStyleSheet(css.line_edit_basic)
        self.UserLineEditMoshtari.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.UserLineEditMoshtari.setInputMethodHints(QtCore.Qt.ImhLatinOnly)
        self.UserLineEditMoshtari.setMaxLength(15)
        self.UserLineEditMoshtari.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.UserLineEditMoshtari.setDragEnabled(True)
        self.UserLineEditMoshtari.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.UserLineEditMoshtari.setClearButtonEnabled(True)
        self.UserLineEditMoshtari.setObjectName("UserLineEditMoshtari")
        self.BgMoshtari.raise_()
        self.MainLabelMoshtari.raise_()
        self.NameLabelMoshtari.raise_()
        self.NameLineEditMoshtari.raise_()
        self.FamilyLineEditMoshtari.raise_()
        self.ButtonNextMoshtari.raise_()
        self.ButtonMoshtari.raise_()
        self.FamilyLabelMoshtari.raise_()
        self.PhoneLabelMoshtari.raise_()
        self.PhoneLineEditMoshtari.raise_()
        self.PassLabelMoshtari.raise_()
        self.PassLineEditMoshtari.raise_()
        self.UserLabelMoshtari.raise_()
        self.UserLineEditMoshtari.raise_()

        self.retranslateUi(SignUpMoshtari)
        QtCore.QMetaObject.connectSlotsByName(SignUpMoshtari)
        SignUpMoshtari.setTabOrder(self.NameLineEditMoshtari, self.FamilyLineEditMoshtari)
        SignUpMoshtari.setTabOrder(self.FamilyLineEditMoshtari, self.PhoneLineEditMoshtari)
        SignUpMoshtari.setTabOrder(self.PhoneLineEditMoshtari, self.UserLineEditMoshtari)
        SignUpMoshtari.setTabOrder(self.UserLineEditMoshtari, self.PassLineEditMoshtari)
        SignUpMoshtari.setTabOrder(self.PassLineEditMoshtari, self.ButtonNextMoshtari)
        SignUpMoshtari.setTabOrder(self.ButtonNextMoshtari, self.ButtonMoshtari)

        self.nameKey = False
        self.familyKey = False
        self.phoneKey = False
        self.userKey = False
        self.passKey = False
        self.buttonKey = False
        self.NameLineEditMoshtari.textChanged.connect(self.checkLineEdit)
        self.FamilyLineEditMoshtari.textChanged.connect(self.checkLineEdit)
        self.PhoneLineEditMoshtari.textChanged.connect(self.checkLineEdit)
        self.UserLineEditMoshtari.textChanged.connect(self.checkLineEdit)
        self.PassLineEditMoshtari.textChanged.connect(self.checkLineEdit)
        self.ButtonNextMoshtari.clicked.connect(self.sendData)

    def retranslateUi(self, SignUpMoshtari):
        _translate = QtCore.QCoreApplication.translate
        SignUpMoshtari.setWindowTitle(_translate("SignUpMoshtari", "Sign Up Form"))
        self.MainLabelMoshtari.setText(_translate("SignUpMoshtari", "صفحه ثبت نام مشتری"))
        self.NameLabelMoshtari.setText(_translate("SignUpMoshtari", "نام:"))
        self.NameLineEditMoshtari.setPlaceholderText(_translate("SignUpMoshtari", " نام (حداکثر15 کاراکتر)"))
        self.FamilyLineEditMoshtari.setPlaceholderText(_translate("SignUpMoshtari", " نام خانوادگی (حداکثر20 کاراکتر)"))
        self.ButtonNextMoshtari.setText(_translate("SignUpMoshtari", "ثبت نام"))
        self.ButtonMoshtari.setText(_translate("SignUpMoshtari", "<"))
        self.FamilyLabelMoshtari.setText(_translate("SignUpMoshtari", "نام خانوادگی:"))
        self.PhoneLabelMoshtari.setText(_translate("SignUpMoshtari", "شماره تماس:"))
        self.PhoneLineEditMoshtari.setPlaceholderText(_translate("SignUpMoshtari", " مثال: 09123456789"))
        self.PassLabelMoshtari.setText(_translate("SignUpMoshtari", "رمز عبور:"))
        self.PassLineEditMoshtari.setPlaceholderText(_translate("SignUpMoshtari", " حداقل8 کاراکتر"))
        self.UserLabelMoshtari.setText(_translate("SignUpMoshtari", "نام کاربری:"))
        self.UserLineEditMoshtari.setPlaceholderText(_translate("SignUpMoshtari", " حداقل3 کاراکتر (لاتین)"))

    def checkLineEdit(self):
        name = self.NameLineEditMoshtari
        family = self.FamilyLineEditMoshtari
        phone = self.PhoneLineEditMoshtari
        user = self.UserLineEditMoshtari
        pas = self.PassLineEditMoshtari
        if len(str(name.text())) > 2:
            name.setStyleSheet(css.line_edit_correct)
            self.nameKey = True
        else:
            name.setStyleSheet(css.line_edit_false)
            self.nameKey = False

        if len(str(family.text())) > 2:
            family.setStyleSheet(css.line_edit_correct)
            self.familyKey = True
        else:
            family.setStyleSheet(css.line_edit_false)
            self.familyKey = False

        if len(str(phone.text())) > 10 and str(phone.text()).isdigit() and str(phone.text())[:2] == '09':
            phone.setStyleSheet(css.line_edit_correct)
            self.phoneKey = True
        else:
            phone.setStyleSheet(css.line_edit_false)
            self.phoneKey = False

        if len(str(user.text())) > 2 and str(user.text()).isascii() and str(user.text()) not in func_2.print_data("USERNAME"):
            user.setStyleSheet(css.line_edit_correct)
            self.userKey = True
        else:
            user.setStyleSheet(css.line_edit_false)
            self.userKey = False

        if len(str(pas.text())) > 7 and str(user.text()).isascii():
            pas.setStyleSheet(css.line_edit_correct)
            self.passKey = True
        else:
            pas.setStyleSheet(css.line_edit_false)
            self.passKey = False

        if self.passKey and self.userKey and self.phoneKey and self.nameKey and self.familyKey:
            self.ButtonNextMoshtari.setStyleSheet(css.button_active)
            self.ButtonNextMoshtari.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.buttonKey = True
        else:
            self.ButtonNextMoshtari.setStyleSheet(css.button_invisible)
            self.ButtonNextMoshtari.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
            self.buttonKey = False

    def sendData(self):
        if self.buttonKey:
            name = self.NameLineEditMoshtari
            family = self.FamilyLineEditMoshtari
            phone = self.PhoneLineEditMoshtari
            user = self.UserLineEditMoshtari
            pas = self.PassLineEditMoshtari
            func_2.insert(str(name.text()), str(family.text()), str(phone.text()), str(user.text()), str(pas.text()))
            sendNotification('ثبت نام با موفقیت انجام شد')
            self.switchto__menu()

    def switchto__menu(self):
        Page.from_moshtari_to_menu()


class Ui_SignUpKhadamat(object):
    def __init__(self):
        self.window = QtWidgets.QMainWindow()

    def setupUi(self, SignUpKhadamat):
        SignUpKhadamat.setObjectName("SignUpKhadamat")
        SignUpKhadamat.resize(800, 600)
        SignUpKhadamat.setMinimumSize(QtCore.QSize(800, 600))
        SignUpKhadamat.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        SignUpKhadamat.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/background/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SignUpKhadamat.setWindowIcon(icon)
        SignUpKhadamat.setLayoutDirection(QtCore.Qt.RightToLeft)
        SignUpKhadamat.setAutoFillBackground(False)
        SignUpKhadamat.setStyleSheet("sign_up{\n"
                                     "background-color:black;\n"
                                     "}")
        self.MainLabelKhadamat = QtWidgets.QLabel(SignUpKhadamat)
        self.MainLabelKhadamat.setGeometry(QtCore.QRect(175, 20, 450, 61))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.MainLabelKhadamat.setFont(font)
        self.MainLabelKhadamat.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.MainLabelKhadamat.setStyleSheet(css.sign_up_main_label)
        self.MainLabelKhadamat.setTextFormat(QtCore.Qt.PlainText)
        self.MainLabelKhadamat.setAlignment(QtCore.Qt.AlignCenter)
        self.MainLabelKhadamat.setObjectName("MainLabelKhadamat")
        self.NameLabelKhadamat = QtWidgets.QLabel(SignUpKhadamat)
        self.NameLabelKhadamat.setGeometry(QtCore.QRect(540, 110, 191, 61))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.NameLabelKhadamat.setFont(font)
        self.NameLabelKhadamat.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.NameLabelKhadamat.setAutoFillBackground(False)
        self.NameLabelKhadamat.setStyleSheet(css.sign_up_small_labels)
        self.NameLabelKhadamat.setAlignment(QtCore.Qt.AlignCenter)
        self.NameLabelKhadamat.setObjectName("NameLabelKhadamat")
        self.FamilyLabelKhadamat = QtWidgets.QLabel(SignUpKhadamat)
        self.FamilyLabelKhadamat.setGeometry(QtCore.QRect(540, 190, 191, 61))
        self.FamilyLabelKhadamat.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.FamilyLabelKhadamat.setStyleSheet(css.sign_up_small_labels)
        self.FamilyLabelKhadamat.setAlignment(QtCore.Qt.AlignCenter)
        self.FamilyLabelKhadamat.setObjectName("FamilyLabelKhadamat")
        self.TavanaiLabelKhadamat = QtWidgets.QLabel(SignUpKhadamat)
        self.TavanaiLabelKhadamat.setGeometry(QtCore.QRect(410, 270, 321, 61))
        self.TavanaiLabelKhadamat.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.TavanaiLabelKhadamat.setStyleSheet(css.sign_up_small_labels)
        self.TavanaiLabelKhadamat.setAlignment(QtCore.Qt.AlignCenter)
        self.TavanaiLabelKhadamat.setObjectName("TavanaiLabelKhadamat")
        self.BgKhadamat = QtWidgets.QLabel(SignUpKhadamat)
        self.BgKhadamat.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.BgKhadamat.setMinimumSize(QtCore.QSize(800, 600))
        self.BgKhadamat.setMaximumSize(QtCore.QSize(800, 600))
        self.BgKhadamat.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.BgKhadamat.setStyleSheet("")
        self.BgKhadamat.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.BgKhadamat.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.BgKhadamat.setText("")
        self.BgKhadamat.setPixmap(QtGui.QPixmap(":/background/desert_blur.jpg"))
        self.BgKhadamat.setWordWrap(False)
        self.BgKhadamat.setObjectName("BgKhadamat")
        self.NameLineEditKhadamat = QtWidgets.QLineEdit(SignUpKhadamat)
        self.NameLineEditKhadamat.setGeometry(QtCore.QRect(70, 110, 431, 61))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.NameLineEditKhadamat.setFont(font)
        self.NameLineEditKhadamat.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.NameLineEditKhadamat.setStyleSheet(css.line_edit_basic)
        self.NameLineEditKhadamat.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.NameLineEditKhadamat.setMaxLength(15)
        self.NameLineEditKhadamat.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.NameLineEditKhadamat.setDragEnabled(True)
        self.NameLineEditKhadamat.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.NameLineEditKhadamat.setClearButtonEnabled(True)
        self.NameLineEditKhadamat.setObjectName("NameLineEditKhadamat")
        self.FamilyLineEditKhadamat = QtWidgets.QLineEdit(SignUpKhadamat)
        self.FamilyLineEditKhadamat.setGeometry(QtCore.QRect(70, 190, 431, 61))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.FamilyLineEditKhadamat.setFont(font)
        self.FamilyLineEditKhadamat.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.FamilyLineEditKhadamat.setStyleSheet(css.line_edit_basic)
        self.FamilyLineEditKhadamat.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.FamilyLineEditKhadamat.setMaxLength(20)
        self.FamilyLineEditKhadamat.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.FamilyLineEditKhadamat.setDragEnabled(True)
        self.FamilyLineEditKhadamat.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.FamilyLineEditKhadamat.setClearButtonEnabled(True)
        self.FamilyLineEditKhadamat.setObjectName("FamilyLineEditKhadamat")
        self.KhadamatLineEditKhadamat2 = QtWidgets.QLineEdit(SignUpKhadamat)
        self.KhadamatLineEditKhadamat2.setGeometry(QtCore.QRect(410, 355, 321, 61))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.KhadamatLineEditKhadamat2.setFont(font)
        self.KhadamatLineEditKhadamat2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.KhadamatLineEditKhadamat2.setStyleSheet(css.line_edit_basic)
        self.KhadamatLineEditKhadamat2.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.KhadamatLineEditKhadamat2.setMaxLength(20)
        self.KhadamatLineEditKhadamat2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.KhadamatLineEditKhadamat2.setDragEnabled(True)
        self.KhadamatLineEditKhadamat2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.KhadamatLineEditKhadamat2.setClearButtonEnabled(True)
        self.KhadamatLineEditKhadamat2.setObjectName("KhadamatLineEditKhadamat2")
        self.KhadamatLineEditKhadamat3 = QtWidgets.QLineEdit(SignUpKhadamat)
        self.KhadamatLineEditKhadamat3.setGeometry(QtCore.QRect(70, 355, 321, 61))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.KhadamatLineEditKhadamat3.setFont(font)
        self.KhadamatLineEditKhadamat3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.KhadamatLineEditKhadamat3.setStyleSheet(css.line_edit_basic)
        self.KhadamatLineEditKhadamat3.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.KhadamatLineEditKhadamat3.setMaxLength(20)
        self.KhadamatLineEditKhadamat3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.KhadamatLineEditKhadamat3.setDragEnabled(True)
        self.KhadamatLineEditKhadamat3.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.KhadamatLineEditKhadamat3.setClearButtonEnabled(True)
        self.KhadamatLineEditKhadamat3.setObjectName("KhadamatLineEditKhadamat3")
        self.KhadamatLineEditKhadamat4 = QtWidgets.QLineEdit(SignUpKhadamat)
        self.KhadamatLineEditKhadamat4.setGeometry(QtCore.QRect(410, 440, 321, 61))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.KhadamatLineEditKhadamat4.setFont(font)
        self.KhadamatLineEditKhadamat4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.KhadamatLineEditKhadamat4.setStyleSheet(css.line_edit_basic)
        self.KhadamatLineEditKhadamat4.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.KhadamatLineEditKhadamat4.setMaxLength(20)
        self.KhadamatLineEditKhadamat4.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.KhadamatLineEditKhadamat4.setDragEnabled(True)
        self.KhadamatLineEditKhadamat4.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.KhadamatLineEditKhadamat4.setClearButtonEnabled(True)
        self.KhadamatLineEditKhadamat4.setObjectName("KhadamatLineEditKhadamat4")
        self.KhadamatLineEditKhadamat5 = QtWidgets.QLineEdit(SignUpKhadamat)
        self.KhadamatLineEditKhadamat5.setGeometry(QtCore.QRect(70, 440, 321, 61))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.KhadamatLineEditKhadamat5.setFont(font)
        self.KhadamatLineEditKhadamat5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.KhadamatLineEditKhadamat5.setStyleSheet(css.line_edit_basic)
        self.KhadamatLineEditKhadamat5.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.KhadamatLineEditKhadamat5.setMaxLength(20)
        self.KhadamatLineEditKhadamat5.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.KhadamatLineEditKhadamat5.setDragEnabled(True)
        self.KhadamatLineEditKhadamat5.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.KhadamatLineEditKhadamat5.setClearButtonEnabled(True)
        self.KhadamatLineEditKhadamat5.setObjectName("KhadamatLineEditKhadamat5")
        self.KhadamatLineEditKhadamat = QtWidgets.QLineEdit(SignUpKhadamat)
        self.KhadamatLineEditKhadamat.setGeometry(QtCore.QRect(70, 270, 321, 61))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.KhadamatLineEditKhadamat.setFont(font)
        self.KhadamatLineEditKhadamat.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.KhadamatLineEditKhadamat.setStyleSheet(css.line_edit_basic)
        self.KhadamatLineEditKhadamat.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.KhadamatLineEditKhadamat.setMaxLength(20)
        self.KhadamatLineEditKhadamat.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.KhadamatLineEditKhadamat.setDragEnabled(True)
        self.KhadamatLineEditKhadamat.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.KhadamatLineEditKhadamat.setClearButtonEnabled(True)
        self.KhadamatLineEditKhadamat.setObjectName("KhadamatLineEditKhadamat")
        self.ButtonNextKhadamat = QtWidgets.QPushButton(SignUpKhadamat)
        self.ButtonNextKhadamat.setGeometry(QtCore.QRect(290, 520, 220, 70))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(45)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ButtonNextKhadamat.setFont(font)
        self.ButtonNextKhadamat.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.ButtonNextKhadamat.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.ButtonNextKhadamat.setAutoFillBackground(False)
        self.ButtonNextKhadamat.setStyleSheet(css.button_invisible)
        self.ButtonNextKhadamat.setCheckable(False)
        self.ButtonNextKhadamat.setAutoExclusive(False)
        self.ButtonNextKhadamat.setAutoDefault(False)
        self.ButtonNextKhadamat.setDefault(False)
        self.ButtonNextKhadamat.setFlat(False)
        self.ButtonNextKhadamat.setObjectName("ButtonNextKhadamat")
        self.ImportantThingsLabel = QtWidgets.QLabel(SignUpKhadamat)
        self.ImportantThingsLabel.setGeometry(QtCore.QRect(26, 100, 51, 231))
        font = QtGui.QFont()
        font.setFamily("NanumGothic")
        font.setPointSize(50)
        self.ImportantThingsLabel.setFont(font)
        self.ImportantThingsLabel.setStyleSheet("color:red;")
        self.ImportantThingsLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.ImportantThingsLabel.setObjectName("ImportantThingsLabel")
        self.ButtonBackKhadamat = QtWidgets.QPushButton(SignUpKhadamat)
        self.ButtonBackKhadamat.setGeometry(QtCore.QRect(20, 20, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonBackKhadamat.setFont(font)
        self.ButtonBackKhadamat.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonBackKhadamat.setStyleSheet(css.back_button)
        self.ButtonBackKhadamat.clicked.connect(self.switchto__menu)
        self.ButtonBackKhadamat.setObjectName("ButtonBackKhadamat")
        self.BgKhadamat.raise_()
        self.MainLabelKhadamat.raise_()
        self.NameLabelKhadamat.raise_()
        self.FamilyLabelKhadamat.raise_()
        self.TavanaiLabelKhadamat.raise_()
        self.NameLineEditKhadamat.raise_()
        self.FamilyLineEditKhadamat.raise_()
        self.KhadamatLineEditKhadamat2.raise_()
        self.KhadamatLineEditKhadamat3.raise_()
        self.KhadamatLineEditKhadamat4.raise_()
        self.KhadamatLineEditKhadamat5.raise_()
        self.KhadamatLineEditKhadamat.raise_()
        self.ButtonNextKhadamat.raise_()
        self.ImportantThingsLabel.raise_()
        self.ButtonBackKhadamat.raise_()

        self.retranslateUi(SignUpKhadamat)
        QtCore.QMetaObject.connectSlotsByName(SignUpKhadamat)
        SignUpKhadamat.setTabOrder(self.NameLineEditKhadamat, self.FamilyLineEditKhadamat)
        SignUpKhadamat.setTabOrder(self.FamilyLineEditKhadamat, self.KhadamatLineEditKhadamat)
        SignUpKhadamat.setTabOrder(self.KhadamatLineEditKhadamat, self.KhadamatLineEditKhadamat2)
        SignUpKhadamat.setTabOrder(self.KhadamatLineEditKhadamat2, self.KhadamatLineEditKhadamat3)
        SignUpKhadamat.setTabOrder(self.KhadamatLineEditKhadamat3, self.KhadamatLineEditKhadamat4)
        SignUpKhadamat.setTabOrder(self.KhadamatLineEditKhadamat4, self.KhadamatLineEditKhadamat5)
        SignUpKhadamat.setTabOrder(self.KhadamatLineEditKhadamat5, self.ButtonNextKhadamat)
        SignUpKhadamat.setTabOrder(self.ButtonNextKhadamat, self.ButtonBackKhadamat)

        self.nameKey = False
        self.familyKey = False
        self.tavanaiKey = [False, False, False, False, False]
        self.buttonKey = False
        self.NameLineEditKhadamat.textChanged.connect(self.checkLineEdit)
        self.FamilyLineEditKhadamat.textChanged.connect(self.checkLineEdit)
        self.KhadamatLineEditKhadamat.textChanged.connect(self.checkLineEdit)
        self.KhadamatLineEditKhadamat2.textChanged.connect(self.checkLineEdit)
        self.KhadamatLineEditKhadamat3.textChanged.connect(self.checkLineEdit)
        self.KhadamatLineEditKhadamat4.textChanged.connect(self.checkLineEdit)
        self.KhadamatLineEditKhadamat5.textChanged.connect(self.checkLineEdit)
        self.ButtonNextKhadamat.clicked.connect(self.sendData)

    def retranslateUi(self, SignUpKhadamat):
        _translate = QtCore.QCoreApplication.translate
        SignUpKhadamat.setWindowTitle(_translate("SignUpKhadamat", "Sign Up Form"))
        self.MainLabelKhadamat.setText(_translate("SignUpKhadamat", "صفحه ثبت نام نیروی خدماتی"))
        self.NameLabelKhadamat.setText(_translate("SignUpKhadamat", "نام:"))
        self.FamilyLabelKhadamat.setText(_translate("SignUpKhadamat", "نام خانوادگی:"))
        self.TavanaiLabelKhadamat.setText(_translate("SignUpKhadamat", "توانایی‌ها (خدمات):"))
        self.NameLineEditKhadamat.setPlaceholderText(_translate("SignUpKhadamat", " نام (حداکثر15 کاراکتر)"))
        self.FamilyLineEditKhadamat.setPlaceholderText(_translate("SignUpKhadamat", " نام خانوادگی (حداکثر20 کاراکتر)"))
        self.KhadamatLineEditKhadamat2.setPlaceholderText(_translate("SignUpKhadamat", " می‌توانید خالی بگذارید!"))
        self.KhadamatLineEditKhadamat3.setPlaceholderText(_translate("SignUpKhadamat", " می‌توانید خالی بگذارید!"))
        self.KhadamatLineEditKhadamat4.setPlaceholderText(_translate("SignUpKhadamat", " می‌توانید خالی بگذارید!"))
        self.KhadamatLineEditKhadamat5.setPlaceholderText(_translate("SignUpKhadamat", " می‌توانید خالی بگذارید!"))
        self.KhadamatLineEditKhadamat.setPlaceholderText(_translate("SignUpKhadamat", " مثال: تعویض ویندوز"))
        self.ButtonNextKhadamat.setText(_translate("SignUpKhadamat", "بعدی"))
        self.ImportantThingsLabel.setText(_translate("SignUpKhadamat", "*\n"
                                                     "*\n"
                                                     "*"))
        self.ButtonBackKhadamat.setText(_translate("SignUpKhadamat", "<"))

    def checkLineEdit(self):
        name = self.NameLineEditKhadamat
        family = self.FamilyLineEditKhadamat
        tavanai = [self.KhadamatLineEditKhadamat, self.KhadamatLineEditKhadamat2,
                   self.KhadamatLineEditKhadamat3, self.KhadamatLineEditKhadamat4, self.KhadamatLineEditKhadamat5]
        if len(str(name.text())) > 2:
            name.setStyleSheet(css.line_edit_correct)
            self.nameKey = True
        else:
            name.setStyleSheet(css.line_edit_false)
            self.nameKey = False

        if len(str(family.text())) > 2:
            family.setStyleSheet(css.line_edit_correct)
            self.familyKey = True
        else:
            family.setStyleSheet(css.line_edit_false)
            self.familyKey = False

        for le, key in zip(tavanai, range(len(self.tavanaiKey))):
            if len(str(le.text())) > 2:
                le.setStyleSheet(css.line_edit_correct)
                self.tavanaiKey[key] = True
            elif self.KhadamatLineEditKhadamat == le:
                le.setStyleSheet(css.line_edit_false)
                self.tavanaiKey[key] = False
            else:
                le.setStyleSheet(css.line_edit_basic)
                self.tavanaiKey[key] = False

        if self.tavanaiKey[0] and self.familyKey and self.nameKey:
            self.ButtonNextKhadamat.setStyleSheet(css.button_active)
            self.ButtonNextKhadamat.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.buttonKey = True
        else:
            self.ButtonNextKhadamat.setStyleSheet(css.button_invisible)
            self.ButtonNextKhadamat.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
            self.buttonKey = False

    def sendData(self):
        if self.buttonKey:
            name = str(self.NameLineEditKhadamat.text())
            family = str(self.FamilyLineEditKhadamat.text())
            tavanai = [str(self.KhadamatLineEditKhadamat.text()), str(self.KhadamatLineEditKhadamat2.text()),
                       str(self.KhadamatLineEditKhadamat3.text()), str(self.KhadamatLineEditKhadamat4.text()),
                       str(self.KhadamatLineEditKhadamat5.text())]

            func.data_temp([name, family, tavanai[0], tavanai[1], tavanai[2], tavanai[3], tavanai[4]])
            sendNotification('ادامه ثبت نام در صفحه بعد')
            Page.from_khadamat_to_khadamat2()

    def switchto__menu(self):
        Page.from_khadamat_to_menu()


class Ui_SignUpKhadamat2(object):
    def __init__(self):
        self.window = QtWidgets.QMainWindow()

    def setupUi(self, SignUpKhadamat2):
        SignUpKhadamat2.setObjectName("SignUpKhadamat2")
        SignUpKhadamat2.resize(800, 600)
        SignUpKhadamat2.setMinimumSize(QtCore.QSize(800, 600))
        SignUpKhadamat2.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        SignUpKhadamat2.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/background/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SignUpKhadamat2.setWindowIcon(icon)
        SignUpKhadamat2.setLayoutDirection(QtCore.Qt.RightToLeft)
        SignUpKhadamat2.setAutoFillBackground(False)
        SignUpKhadamat2.setStyleSheet("sign_up{\nbackground-color:black;\n}")
        self.SexLabelKhadamat2 = QtWidgets.QLabel(SignUpKhadamat2)
        self.SexLabelKhadamat2.setGeometry(QtCore.QRect(540, 110, 191, 61))
        self.SexLabelKhadamat2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.SexLabelKhadamat2.setStyleSheet(css.sign_up_small_labels)
        self.SexLabelKhadamat2.setAlignment(QtCore.Qt.AlignCenter)
        self.SexLabelKhadamat2.setObjectName("SexLabelKhadamat2")
        self.BgKhadamat2 = QtWidgets.QLabel(SignUpKhadamat2)
        self.BgKhadamat2.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.BgKhadamat2.setMinimumSize(QtCore.QSize(800, 600))
        self.BgKhadamat2.setMaximumSize(QtCore.QSize(800, 600))
        self.BgKhadamat2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.BgKhadamat2.setStyleSheet("")
        self.BgKhadamat2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.BgKhadamat2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.BgKhadamat2.setText("")
        self.BgKhadamat2.setPixmap(QtGui.QPixmap(":/background/desert_blur.jpg"))
        self.BgKhadamat2.setWordWrap(False)
        self.BgKhadamat2.setObjectName("BgKhadamat2")
        self.EmailLineEditKhadamat2 = QtWidgets.QLineEdit(SignUpKhadamat2)
        self.EmailLineEditKhadamat2.setGeometry(QtCore.QRect(70, 190, 431, 61))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.EmailLineEditKhadamat2.setFont(font)
        self.EmailLineEditKhadamat2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.EmailLineEditKhadamat2.setStyleSheet(css.line_edit_basic)
        self.EmailLineEditKhadamat2.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.EmailLineEditKhadamat2.setMaxLength(40)
        self.EmailLineEditKhadamat2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.EmailLineEditKhadamat2.setDragEnabled(True)
        self.EmailLineEditKhadamat2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.EmailLineEditKhadamat2.setClearButtonEnabled(True)
        self.EmailLineEditKhadamat2.setObjectName("EmailLineEditKhadamat2")
        self.ButtonNextKhadamat2 = QtWidgets.QPushButton(SignUpKhadamat2)
        self.ButtonNextKhadamat2.setGeometry(QtCore.QRect(290, 519, 220, 71))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(34)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ButtonNextKhadamat2.setFont(font)
        self.ButtonNextKhadamat2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.ButtonNextKhadamat2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.ButtonNextKhadamat2.setAutoFillBackground(False)
        self.ButtonNextKhadamat2.setStyleSheet(css.button_invisible)
        self.ButtonNextKhadamat2.setCheckable(False)
        self.ButtonNextKhadamat2.setAutoExclusive(False)
        self.ButtonNextKhadamat2.setAutoDefault(False)
        self.ButtonNextKhadamat2.setDefault(False)
        self.ButtonNextKhadamat2.setFlat(False)
        self.ButtonNextKhadamat2.setObjectName("ButtonNextKhadamat2")
        self.ButtonKhadamat2 = QtWidgets.QPushButton(SignUpKhadamat2)
        self.ButtonKhadamat2.setGeometry(QtCore.QRect(20, 20, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonKhadamat2.setFont(font)
        self.ButtonKhadamat2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonKhadamat2.setStyleSheet(css.back_button)
        self.ButtonKhadamat2.clicked.connect(self.switchto__signup_khadamati)
        self.ButtonKhadamat2.setObjectName("ButtonKhadamat2")
        self.EmailLabelKhadamat2 = QtWidgets.QLabel(SignUpKhadamat2)
        self.EmailLabelKhadamat2.setGeometry(QtCore.QRect(540, 190, 191, 61))
        self.EmailLabelKhadamat2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.EmailLabelKhadamat2.setStyleSheet(css.sign_up_small_labels)
        self.EmailLabelKhadamat2.setAlignment(QtCore.Qt.AlignCenter)
        self.EmailLabelKhadamat2.setObjectName("EmailLabelKhadamat2")
        self.PhoneLabelKhadamat2 = QtWidgets.QLabel(SignUpKhadamat2)
        self.PhoneLabelKhadamat2.setGeometry(QtCore.QRect(540, 270, 191, 61))
        self.PhoneLabelKhadamat2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.PhoneLabelKhadamat2.setStyleSheet(css.sign_up_small_labels)
        self.PhoneLabelKhadamat2.setAlignment(QtCore.Qt.AlignCenter)
        self.PhoneLabelKhadamat2.setObjectName("PhoneLabelKhadamat2")
        self.PhoneLineEditKhadamat2 = QtWidgets.QLineEdit(SignUpKhadamat2)
        self.PhoneLineEditKhadamat2.setGeometry(QtCore.QRect(70, 270, 431, 61))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.PhoneLineEditKhadamat2.setFont(font)
        self.PhoneLineEditKhadamat2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PhoneLineEditKhadamat2.setStyleSheet(css.line_edit_basic)
        self.PhoneLineEditKhadamat2.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.PhoneLineEditKhadamat2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly | QtCore.Qt.ImhFormattedNumbersOnly)
        self.PhoneLineEditKhadamat2.setMaxLength(11)
        self.PhoneLineEditKhadamat2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.PhoneLineEditKhadamat2.setDragEnabled(True)
        self.PhoneLineEditKhadamat2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.PhoneLineEditKhadamat2.setClearButtonEnabled(True)
        self.PhoneLineEditKhadamat2.setObjectName("PhoneLineEditKhadamat2")
        self.PassLabelKhadamat2 = QtWidgets.QLabel(SignUpKhadamat2)
        self.PassLabelKhadamat2.setGeometry(QtCore.QRect(540, 430, 191, 61))
        self.PassLabelKhadamat2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.PassLabelKhadamat2.setStyleSheet(css.sign_up_small_labels)
        self.PassLabelKhadamat2.setAlignment(QtCore.Qt.AlignCenter)
        self.PassLabelKhadamat2.setObjectName("PassLabelKhadamat2")
        self.PassLineEditKhadamat2 = QtWidgets.QLineEdit(SignUpKhadamat2)
        self.PassLineEditKhadamat2.setGeometry(QtCore.QRect(70, 430, 431, 61))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.PassLineEditKhadamat2.setFont(font)
        self.PassLineEditKhadamat2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PassLineEditKhadamat2.setStyleSheet(css.line_edit_basic)
        self.PassLineEditKhadamat2.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.PassLineEditKhadamat2.setMaxLength(16)
        self.PassLineEditKhadamat2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PassLineEditKhadamat2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.PassLineEditKhadamat2.setDragEnabled(True)
        self.PassLineEditKhadamat2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.PassLineEditKhadamat2.setClearButtonEnabled(True)
        self.PassLineEditKhadamat2.setObjectName("PassLineEditKhadamat2")
        self.MainLabelKhadamat2 = QtWidgets.QLabel(SignUpKhadamat2)
        self.MainLabelKhadamat2.setGeometry(QtCore.QRect(175, 20, 450, 61))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.MainLabelKhadamat2.setFont(font)
        self.MainLabelKhadamat2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.MainLabelKhadamat2.setStyleSheet(css.sign_up_main_label)
        self.MainLabelKhadamat2.setTextFormat(QtCore.Qt.PlainText)
        self.MainLabelKhadamat2.setAlignment(QtCore.Qt.AlignCenter)
        self.MainLabelKhadamat2.setObjectName("MainLabelKhadamat2")
        self.UserLineEditKhadamat2 = QtWidgets.QLineEdit(SignUpKhadamat2)
        self.UserLineEditKhadamat2.setGeometry(QtCore.QRect(70, 350, 431, 61))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.UserLineEditKhadamat2.setFont(font)
        self.UserLineEditKhadamat2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.UserLineEditKhadamat2.setStyleSheet(css.line_edit_basic)
        self.UserLineEditKhadamat2.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.UserLineEditKhadamat2.setInputMethodHints(QtCore.Qt.ImhLatinOnly)
        self.UserLineEditKhadamat2.setMaxLength(15)
        self.UserLineEditKhadamat2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.UserLineEditKhadamat2.setDragEnabled(True)
        self.UserLineEditKhadamat2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.UserLineEditKhadamat2.setClearButtonEnabled(True)
        self.UserLineEditKhadamat2.setObjectName("UserLineEditKhadamat2")
        self.UserLabelKhadamat2 = QtWidgets.QLabel(SignUpKhadamat2)
        self.UserLabelKhadamat2.setGeometry(QtCore.QRect(540, 350, 191, 61))
        self.UserLabelKhadamat2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.UserLabelKhadamat2.setStyleSheet(css.sign_up_small_labels)
        self.UserLabelKhadamat2.setAlignment(QtCore.Qt.AlignCenter)
        self.UserLabelKhadamat2.setObjectName("UserLabelKhadamat2")
        self.FemaleradioButton = QtWidgets.QRadioButton(SignUpKhadamat2)
        self.FemaleradioButton.setGeometry(QtCore.QRect(290, 110, 151, 61))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(39)
        self.FemaleradioButton.setFont(font)
        self.FemaleradioButton.setStyleSheet("color:black;")
        self.FemaleradioButton.setIconSize(QtCore.QSize(22, 22))
        self.FemaleradioButton.setChecked(False)
        self.FemaleradioButton.setObjectName("FemaleradioButton")
        self.MaleradioButton = QtWidgets.QRadioButton(SignUpKhadamat2)
        self.MaleradioButton.setGeometry(QtCore.QRect(90, 110, 151, 61))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(39)
        self.MaleradioButton.setFont(font)
        self.MaleradioButton.setStyleSheet("color:black;")
        self.MaleradioButton.setIconSize(QtCore.QSize(22, 22))
        self.MaleradioButton.setChecked(True)
        self.MaleradioButton.setObjectName("MaleradioButton")
        self.tmpLabel = QtWidgets.QLabel(SignUpKhadamat2)
        self.tmpLabel.setGeometry(QtCore.QRect(70, 110, 431, 61))
        self.tmpLabel.setStyleSheet("text-align: center;\nborder:3px solid white;\nborder-radius: 15px;\n"
                                    "background-color: white;\ncolor:white;")
        self.tmpLabel.setText("")
        self.tmpLabel.setObjectName("tmpLabel")
        self.BgKhadamat2.raise_()
        self.SexLabelKhadamat2.raise_()
        self.EmailLineEditKhadamat2.raise_()
        self.ButtonNextKhadamat2.raise_()
        self.ButtonKhadamat2.raise_()
        self.EmailLabelKhadamat2.raise_()
        self.PhoneLabelKhadamat2.raise_()
        self.PhoneLineEditKhadamat2.raise_()
        self.PassLabelKhadamat2.raise_()
        self.PassLineEditKhadamat2.raise_()
        self.MainLabelKhadamat2.raise_()
        self.UserLineEditKhadamat2.raise_()
        self.UserLabelKhadamat2.raise_()
        self.tmpLabel.raise_()
        self.FemaleradioButton.raise_()
        self.MaleradioButton.raise_()

        self.retranslateUi(SignUpKhadamat2)
        QtCore.QMetaObject.connectSlotsByName(SignUpKhadamat2)
        SignUpKhadamat2.setTabOrder(self.FemaleradioButton, self.MaleradioButton)
        SignUpKhadamat2.setTabOrder(self.MaleradioButton, self.EmailLineEditKhadamat2)
        SignUpKhadamat2.setTabOrder(self.EmailLineEditKhadamat2, self.PhoneLineEditKhadamat2)
        SignUpKhadamat2.setTabOrder(self.PhoneLineEditKhadamat2, self.UserLineEditKhadamat2)
        SignUpKhadamat2.setTabOrder(self.UserLineEditKhadamat2, self.PassLineEditKhadamat2)
        SignUpKhadamat2.setTabOrder(self.PassLineEditKhadamat2, self.ButtonNextKhadamat2)
        SignUpKhadamat2.setTabOrder(self.ButtonNextKhadamat2, self.ButtonKhadamat2)

        self.phoneKey = False
        self.userKey = False
        self.passKey = False
        self.buttonKey = False
        self.UserLineEditKhadamat2.textChanged.connect(self.checkLineEdit)
        self.PassLineEditKhadamat2.textChanged.connect(self.checkLineEdit)
        self.PhoneLineEditKhadamat2.textChanged.connect(self.checkLineEdit)
        self.EmailLineEditKhadamat2.textChanged.connect(self.checkLineEdit)
        self.ButtonNextKhadamat2.clicked.connect(self.sendData)

    def retranslateUi(self, SignUpKhadamat2):
        _translate = QtCore.QCoreApplication.translate
        SignUpKhadamat2.setWindowTitle(_translate("SignUpKhadamat2", "Sign Up Form"))
        self.SexLabelKhadamat2.setText(_translate("SignUpKhadamat2", "جنسیت:"))
        self.EmailLineEditKhadamat2.setPlaceholderText(_translate("SignUpKhadamat2", " مثال: email@gmail.com"))
        self.ButtonNextKhadamat2.setText(_translate("SignUpKhadamat2", "ثبت نام"))
        self.ButtonKhadamat2.setText(_translate("SignUpKhadamat2", "<"))
        self.EmailLabelKhadamat2.setText(_translate("SignUpKhadamat2", "ایمیل:"))
        self.PhoneLabelKhadamat2.setText(_translate("SignUpKhadamat2", "شماره تماس:"))
        self.PhoneLineEditKhadamat2.setPlaceholderText(_translate("SignUpKhadamat2", " مثال: 09123456789"))
        self.PassLabelKhadamat2.setText(_translate("SignUpKhadamat2", "رمز عبور:"))
        self.PassLineEditKhadamat2.setPlaceholderText(_translate("SignUpKhadamat2", " حداقل8 کاراکتر"))
        self.MainLabelKhadamat2.setText(_translate("SignUpKhadamat2", "صفحه ثبت نام نیروی خدماتی"))
        self.UserLineEditKhadamat2.setPlaceholderText(_translate("SignUpKhadamat2", " حداقل3 کاراکتر (لاتین)"))
        self.UserLabelKhadamat2.setText(_translate("SignUpKhadamat2", "نام کاربری:"))
        self.FemaleradioButton.setText(_translate("SignUpKhadamat2", "زن "))
        self.MaleradioButton.setText(_translate("SignUpKhadamat2", " مرد "))

    def checkLineEdit(self):
        user = self.UserLineEditKhadamat2
        pas = self.PassLineEditKhadamat2
        phone = self.PhoneLineEditKhadamat2
        email = self.EmailLineEditKhadamat2

        if len(str(user.text())) > 2 and str(user.text()).isascii() and str(user.text()) not in func.print_data("USERNAME"):
            user.setStyleSheet(css.line_edit_correct)
            self.userKey = True
        else:
            user.setStyleSheet(css.line_edit_false)
            self.userKey = False

        if len(str(pas.text())) > 7 and str(user.text()).isascii():
            pas.setStyleSheet(css.line_edit_correct)
            self.passKey = True
        else:
            pas.setStyleSheet(css.line_edit_false)
            self.passKey = False

        if len(str(phone.text())) > 10 and str(phone.text()).isdigit() and str(phone.text())[:2] == '09':
            phone.setStyleSheet(css.line_edit_correct)
            self.phoneKey = True
        else:
            phone.setStyleSheet(css.line_edit_false)
            self.phoneKey = False

        if len(str(email.text())) > 2 and str(email.text()).isascii() and '@' in str(email.text()):
            email.setStyleSheet(css.line_edit_correct)
        else:
            email.setStyleSheet(css.line_edit_false)

        if self.passKey and self.userKey and self.phoneKey:
            self.ButtonNextKhadamat2.setStyleSheet(css.button_active)
            self.ButtonNextKhadamat2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.buttonKey = True
        else:
            self.ButtonNextKhadamat2.setStyleSheet(css.button_invisible)
            self.ButtonNextKhadamat2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
            self.buttonKey = False

    def sendData(self):
        if self.buttonKey:
            user = str(self.UserLineEditKhadamat2.text())
            pas = str(self.PassLineEditKhadamat2.text())
            phone = str(self.PhoneLineEditKhadamat2.text())
            email = str(self.EmailLineEditKhadamat2.text())
            func.insert(phonenumber=phone, username=user, password=pas)
            sendNotification('ثبت نام با موفقیت انجام شد')
            # kiyan inja bayad bre page baad (menu) # be roye cheshm :) | (: oftad
            self.switchto__menu()

    def switchto__signup_khadamati(self):
        Page.from_khadamat2_to_khadamat()

    def switchto__menu(self):
        Page.from_khadamat2_to_menu()


class Ui_omor_mali(object):
    def __init__(self):
        self.window = QtWidgets.QMainWindow()

    def setupUi(self, omor_mali):
        self.omor_mali = QtWidgets.QLabel(omor_mali)
        self.omor_mali.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.omor_mali.setMinimumSize(QtCore.QSize(800, 600))
        self.omor_mali.setMaximumSize(QtCore.QSize(800, 600))
        self.omor_mali.setText("")
        self.omor_mali.setPixmap(QtGui.QPixmap("./images/1.jpg"))
        self.omor_mali.setObjectName("omor_mali")
        omor_mali.setObjectName("omor_malli")
        omor_mali.resize(800, 600)
        omor_mali.setMinimumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/background/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        omor_mali.setWindowIcon(icon)
        self.welcome_text = QtWidgets.QTextBrowser(omor_mali)
        self.welcome_text.setGeometry(QtCore.QRect(200, 90, 391, 51))
        self.welcome_text.setStyleSheet("font: 20pt \"B Badr\";\nbackground-color:\"#B8860B\";\nborder-radius: 20px;")
        self.welcome_text.setObjectName("welcome_text")
        self.pushButton = QtWidgets.QPushButton(omor_mali)
        self.pushButton.setGeometry(QtCore.QRect(110, 260, 571, 51))
        self.pushButton.setStyleSheet("font: 20pt \"B Badr\";\nbackground-color:\"#B8860B\";\nborder-radius: 20px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(omor_mali)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 20, 101, 41))
        self.pushButton_2.setStyleSheet("QPushButton {\nbackground-color:\"#B8860B\";\ncolor: white; \nborder: 1px solid rgb(0, 0, 210);\n"
                                        "border-radius: 50px;\nfont-size:30px;\n}\nQPushButton:pressed {\nbackground-color:rgb(0, 85, 255);\n"
                                        "}\nQPushButton:hover{\ncolor:rgb(216, 216, 216);\n}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(omor_mali)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 340, 531, 51))
        self.pushButton_3.setStyleSheet("font: 20pt \"B Badr\";\nbackground-color:\"#B8860B\";\nborder-radius: 20px;\n")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(omor_mali)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 410, 551, 51))
        self.pushButton_4.setStyleSheet("font: 20pt \"B Badr\";\nbackground-color:\"#B8860B\";\nborder-radius: 20px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(omor_mali)
        self.pushButton_5.setGeometry(QtCore.QRect(490, 480, 191, 41))
        self.pushButton_5.setStyleSheet("font: 20pt \"B Badr\";\nbackground-color:\"#B8860B\";\nborder-radius: 20px;")
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.clicked.connect(self.switchto__pop_sod)
        self.retranslateUi(omor_mali)
        QtCore.QMetaObject.connectSlotsByName(omor_mali)
        self.pushButton_2.clicked.connect(self.switchto__menu)

    def retranslateUi(self, omor_mali):
        _translate = QtCore.QCoreApplication.translate
        omor_mali.setWindowTitle(_translate("omor_mali", "بخش امور مالی"))
        self.welcome_text.setToolTip(_translate("omor_mali", "<html><head/><body><p><br/></p></body></html>"))
        self.welcome_text.setHtml(_translate("omor_mali", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'B Badr\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
                                             "<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:22pt;\">به صفحه امور مالی خوش آمدید</span></p></body></html>"))
        self.pushButton.setText(_translate("omor_mali", "برای دیدن گزارش کارکرد نیرو های خدماتی شرکت اینجا را کلیک کنید"))
        self.pushButton_2.setText(_translate("omor_mali", "<"))
        self.pushButton_3.setText(_translate("omor_mali", "برای دیدن درخواست های مشتری های شرکت اینجا را کلیک کنید"))
        self.pushButton_4.setText(_translate("omor_mali", "برای دیدن عملکرد خدمات عرضه شده به مشتریان اینجا را کلیک کنید"))
        self.pushButton_5.setText(_translate("omor_mali", "گزارش سود شرکت"))

    def switchto__menu(self):
        Page.from_omor_mali_to_menu()

    def switchto__pop_sod(self):
        Page.show_sod()


class Ui_request_for_work(object):
    def __init__(self):
        self.window = QtWidgets.QMainWindow()

    def setupUi(self, menu):
        self.menu = QtWidgets.QLabel(menu)
        self.menu.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.menu.setMinimumSize(QtCore.QSize(800, 600))
        self.menu.setMaximumSize(QtCore.QSize(800, 600))
        self.menu.setText("")
        self.menu.setPixmap(QtGui.QPixmap("./images/13.jpg"))
        self.menu.setObjectName("menu")
        menu.setObjectName("menu")
        menu.resize(800, 600)
        menu.setMinimumSize(QtCore.QSize(800, 600))
        menu.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/background/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        menu.setWindowIcon(icon)
        self.ability = QtWidgets.QComboBox(menu)
        self.ability.setGeometry(QtCore.QRect(180, 190, 271, 41))
        self.ability.setMaxVisibleItems(10)
        self.ability.setIconSize(QtCore.QSize(16, 16))
        self.ability.setObjectName("ability")
        self.ability.setStyleSheet("font: 20 14pt \"B Badr\";border-radius:5px;")
        self.back = QtWidgets.QPushButton(menu)
        self.back.setGeometry(QtCore.QRect(50, 30, 81, 51))
        self.back.setStyleSheet("font-size:20px;\nbackground-color:rgba(0,170,255,0.7);\ncolor:white;\nborder-radius:10px;")
        self.back.setObjectName("back")
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label = QtWidgets.QLabel(menu)
        self.label.setGeometry(QtCore.QRect(530, 180, 211, 61))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(menu)
        self.label_2.setGeometry(QtCore.QRect(480, 270, 271, 61))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.ability_2 = QtWidgets.QComboBox(menu)
        self.ability_2.setGeometry(QtCore.QRect(180, 280, 271, 41))
        self.ability_2.setMaxVisibleItems(10)
        self.ability_2.setIconSize(QtCore.QSize(16, 16))
        self.ability_2.setObjectName("ability_2")
        self.ability_2.setStyleSheet("font: 20 14pt \"B Badr\";border-radius:5px;")
        self.lineEdit = QtWidgets.QLineEdit(menu)
        self.lineEdit.setGeometry(QtCore.QRect(180, 360, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet(css.line_edit_request_false)
        self.label_3 = QtWidgets.QLabel(menu)
        self.label_3.setGeometry(QtCore.QRect(540, 350, 191, 71))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 18pt \"B Badr\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(menu)
        self.label_4.setGeometry(QtCore.QRect(540, 430, 201, 61))
        font = QtGui.QFont()
        font.setFamily("B Badr")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.sabt = QtWidgets.QPushButton(menu)
        self.sabt.setGeometry(QtCore.QRect(100, 510, 171, 41))
        self.sabt.setStyleSheet("font: 22pt \"B Badr\";\nbackground-color:rgba(0,170,255,0.7);\ncolor:white;\nborder-radius:10px;")
        self.sabt.setObjectName("sabt")
        self.sabt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.retranslateUi(menu)
        QtCore.QMetaObject.connectSlotsByName(menu)
        self.key = False
        self.addAbility()
        self.back.clicked.connect(self.switchto__menu)
        self.lineEdit.textChanged.connect(self.checkLineEdit)
        self.ability.currentIndexChanged.connect(self.removeFromComboBox)
        self.ability.activated[str].connect(self.addToComboBox)
        self.sabt.clicked.connect(self.done)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "صفحه درخواست کار"))
        self.back.setText(_translate("Form", "<"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">انتخاب کار</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">انتخاب نیروی خدماتی</span></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("Form", "100000 <"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\"font-size:34px; font-weight:800;\">قیمت (ریال)</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">تاریخ انجام کار</span></p></body></html>"))
        self.sabt.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt;\">ثبت</span></p></body></html>"))
        self.sabt.setWhatsThis(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt;\">ثبت</span></p></body></html>"))
        self.sabt.setText(_translate("Form", "انجام"))

    def addAbility(self):
        for i in func.print_ability():
            if str(i).strip() == '':
                continue
            self.ability.addItems([i])

    def checkLineEdit(self):
        obj = self.lineEdit
        if len(str(obj.text())) > 5 and str(obj.text()).isdigit():
            obj.setStyleSheet(css.line_edit_request_correct)
            self.key = True
        else:
            obj.setStyleSheet(css.line_edit_request_false)
            self.key = False

    def done(self):
        box = self.ability
        box2 = self.ability_2
        if self.key and str(box2.currentText()).strip() != '':
            money = int(self.lineEdit.text())
            func_3.insert(money)  # vahid
            self.switchto__menu()
            sendNotification('ثبت با موفقیت انجام شد')
        else:
            sendNotification('تمام موارد را کامل کنید')

    def addToComboBox(self, ability='تعویض ویندوز'):
        box = self.ability_2
        for i in func.print_hamal(ability):
            box.addItems([i])

    def removeFromComboBox(self):
        box = self.ability_2
        box.clear()

    def switchto__menu(self):
        Page.sefaresh_to_menu()


class Ui_sod(object):
    def __init__(self):
        self.window = QtWidgets.QMainWindow()

    def setupUi(self, sod):
        sod.setObjectName("sod")
        sod.resize(450, 275)
        sod.setMinimumSize(QtCore.QSize(450, 275))
        sod.setMaximumSize(QtCore.QSize(450, 275))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/background/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        sod.setWindowIcon(icon)
        self.verticalLayoutWidget = QtWidgets.QWidget(sod)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 10, 381, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("font: 22pt \"B Badr\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(sod)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(40, 160, 151, 61))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.print_sod = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.print_sod.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.print_sod.setText(str(func_3.sum_sood()))  # label for ((sod))
        self.print_sod.setAlignment(QtCore.Qt.AlignCenter)
        self.print_sod.setObjectName("print_sod")
        self.verticalLayout_2.addWidget(self.print_sod)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(sod)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(220, 170, 199, 36))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setStyleSheet("font: 14pt \"B Badr\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)

        self.retranslateUi(sod)
        QtCore.QMetaObject.connectSlotsByName(sod)

    def retranslateUi(self, sod):
        _translate = QtCore.QCoreApplication.translate
        sod.setWindowTitle(_translate("sod", "محاسبه سود شرکت"))
        self.label.setText(_translate("sod", "به بخش میزان سود شرکت خوش آمدید."))
        self.label_2.setText(_translate("sod", "میزان سود شرکت تا امروز ( ریال ):"))


app = QtWidgets.QApplication(sys.argv)
Page = Controller()
Page.show_welcome()
sys.exit(app.exec_())
