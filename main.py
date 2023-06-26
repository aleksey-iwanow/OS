from PyQt5.QtWidgets import QLayout

from apps import *
from main_ui import Ui_MainWindow

STYLE = """
QHeaderView::section { background-color: rgb(83,184,35); color: rgb(0,0,0); border: 2px solid rgb(0,0,0) }
QTreeView {border: 2px solid rgb(0,0,0)}

QListWidget::item:pressed,QListWidget::item:selected{background-color:rgb(83,184,35); color: rgb(0,0,0)}
QTreeView::item:pressed,QTreeView::item:selected{background-color:rgb(83,184,35); color: rgb(0,0,0)}

QMainWindow{
    background-color: rgb(0,0,0);
    
}

QPushButton
{
	background-color: rgb(51,101,45);
	border: 2px solid rgb(46,197,38);
	color: rgb(255,255,255)
}

QPushButton:hover
{
	background-color: rgb(34,80,33);
	color: rgb(255,255,255)
}

QLineEdit::text:selected
{
	background-color: rgb(55,185,141,190);
	color: rgb(255,255,255)
}

QTabWidget::pane
{
    border: 1px;
    background-color: rgba(102, 126, 120, 190);
    color: rgb(255, 255, 255)
}

QTabBar::tab
{
	background-color: rgb(142, 146, 140, 190);
	color: rgb(255, 255, 255)
}

QTabBar::tab:selected
{
	background-color: rgb(102, 126, 120, 190);
	color: rgb(255, 255, 255)
}

QTabBar::tab:hover
{
	background-color: rgb(82, 106, 100, 190);
	color: rgb(255, 255, 255)
}

QMenu
{
	background-color: rgb(16, 45, 35, 90);
     color: #37B98D;
	
	font: 9pt "OCR A Extended";
}

QCheckBox::indicator
{
	width: 22px;
	height: 22px;
	background-color: #77D4C5;
	border: 2px solid #27685D;
}
QCheckBox::indicator:checked
{
	image: url(images/icon-check.png);
}
QCheckBox::indicator:hover
{
	border: 2px solid black;
}

QLineEdit:hover{
	border: 2px solid black;
}
QLineEdit{
	border: 2px solid #27685D;
	background-color: #77D4C5;
}
"""
button_with_icon_style = """QPushButton#title
{   
    border: 2px solid color black;
	background-color: rgb(0,0,0,0);
}

QPushButton#title:hover
{
    border: 2px solid color black;
	background-color: rgb(0,0,0,60);
}"""
button_exit_style = """QPushButton#title
{   
    border: 2px solid color black;
	background-color: rgb(0,0,0,0);
}

QPushButton#title:hover
{
    border: 2px solid color black;
	background-color: rgb(152, 0 ,0);
}"""


class Wifi(QFrame):
    def __init__(self, *args, **kwargs):
        self.win = args[0]

        super().__init__(*args, **kwargs)
        self.hide()
        self.resize(450, 700)
        self.move(self.win.width() - self.width(), self.win.HEIGHT_T)
        self.setStyleSheet('QFrame{background-color: rgb(0,0,0); border: 4px solid rgb(83,184,35); font: 28px "CatV 6X12 9";}'
                           'QListWidget{background-color: rgb(0,0,0); color:rgb(83,184,35)}'
                           'QLabel{border: none}')
        self.label_ = QLabel(self)
        self.label_.resize(120,120)
        self.label_.move(20,5)
        self.movie = QMovie("img/loader.gif")
        self.movie.setScaledSize(self.label_.size())
        self.label_.setMovie(self.movie)
        self.movie.start()

    def open(self):
        self.move(self.win.width() - self.width(), self.win.HEIGHT_T)


class Menu(QFrame):
    def __init__(self, icons, *args, **kwargs):
        self.win = args[0]
        self.i_cns, self.i_calc, self.i_web, self.i_fl = [i for i in icons]
        super().__init__(*args, **kwargs)
        self.hide()
        self.resize(500, 700)
        self.move(0, self.win.HEIGHT_T)
        self.setStyleSheet('QFrame{background-color: rgb(0,0,0); border: 4px solid rgb(83,184,35); font: 28px "CatV 6X12 9";}'
                           'QListWidget{background-color: rgb(0,0,0); color:rgb(83,184,35)}')
        self.list_apps = [App("Калькулятор", self.i_calc), App("Терминал", self.i_cns), App("Браузер", self.i_web), App("Файловый менеджер", self.i_fl), App("Змейка", self.i_fl)]
        self.listWidgetApps = QListWidget(self)
        self.listWidgetApps.resize(self.width(), self.height())

    def open(self):
        self.update_list_widget()

    def open_app(self):
        index = self.listWidgetApps.currentIndex().row()
        ap = None
        if self.list_apps[index].name == "Терминал":
            self.win.open_app(Console())
        elif self.list_apps[index].name == "Калькулятор":
            self.win.open_app(Calculator())
        elif self.list_apps[index].name == "Браузер":
            self.win.open_app(Browser())
        elif self.list_apps[index].name == "Файловый менеджер":
            self.win.open_app(FileManager())
        elif self.list_apps[index].name == "Змейка":
            self.win.open_app(Snake1())

    def update_list_widget(self):
        self.listWidgetApps.clear()

        for a in self.list_apps:
            item = QListWidgetItem()
            item.setText(a.name)
            item.setIcon(a.icon)
            self.listWidgetApps.addItem(item)

        self.listWidgetApps.clicked.connect(self.open_app)


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        #uic.loadUi('main_ui.ui', self)

        # icons
        self.icon_exit = QIcon(QPixmap("img/icon_exit.png"))
        self.icon_close = QIcon(QPixmap("img/icon_close.png"))
        self.icon_menu = QIcon(QPixmap("img/icon_menu.png"))
        self.icon_browser = QIcon(QPixmap("img/icon_browser.png"))
        self.icon_browser_green = QIcon(QPixmap("img/icon_browser_green.png"))
        self.icon_calc_green = QIcon(QPixmap("img/icon_calc_green.png"))
        self.icon_console_green = QIcon(QPixmap("img/icon_console_green.png"))
        self.icon_calc = QIcon(QPixmap("img/icon_calc.png"))
        self.icon_console = QIcon(QPixmap("img/icon_console.png"))
        self.icon_wifi = QIcon(QPixmap("img/icon_wifi.png"))
        self.icon_file_manager_green = QIcon(QPixmap("img/icon_file_manager_green.png"))
        self.icon_file_manager = QIcon(QPixmap("img/icon_file_manager.png"))
        # x
        self.layout = QWidget(self)
        self.layout.move(0, 0)
        self.layout.resize(self.size())
        self.layout.show()

        self.apps = []
        self.current_time = None
        self.HEIGHT_T = 50
        self.font_title = QFont("CatV 6x12 9")
        self.font_title.setPointSize(22)
        self.setStyleSheet(STYLE)

        self.menu_ = Menu([self.icon_console_green,
                          self.icon_calc_green,
                           self.icon_browser_green,
                           self.icon_file_manager_green], self)

        self.wifi_ = Wifi(self)

        self.panel_up = QWidget(self)
        self.panel_up.resize(self.width(), self.HEIGHT_T)
        self.panel_up.move(0, 0)
        self.panel_up.setStyleSheet("background-color: rgb(83,184,35)")

        self.time_label = QLabel(self.panel_up)
        self.time_label.resize(200, self.HEIGHT_T)
        self.time_label.setStyleSheet('color: rgb(0,0,0)')
        self.time_label.setFont(self.font_title)

        self.temp_label = QLabel(self.panel_up)
        self.temp_label.resize(200, self.HEIGHT_T)
        self.temp_label.setStyleSheet('color: rgb(0,0,0)')
        self.temp_label.setFont(self.font_title)

        self.button_exit = QPushButton(self.panel_up)
        self.button_exit.clicked.connect(lambda: sys.exit(app.exec_()))
        self.button_exit.setIcon(self.icon_exit)
        self.button_exit.setObjectName('title')
        self.button_exit.setIconSize(QSize(self.HEIGHT_T - 10, self.HEIGHT_T - 10))
        self.button_exit.resize(self.HEIGHT_T + 2, self.HEIGHT_T + 2)
        self.button_exit.move(0, 0)
        self.button_exit.setStyleSheet(button_exit_style)

        self.button_menu = QPushButton(self.panel_up)
        self.button_menu.clicked.connect(self.open_menu)
        self.button_menu.setIcon(self.icon_menu)
        self.button_menu.setObjectName('title')
        self.button_menu.setIconSize(QSize(self.HEIGHT_T - 10, self.HEIGHT_T - 10))
        self.button_menu.resize(self.HEIGHT_T + 2, self.HEIGHT_T + 2)
        self.button_menu.move(self.HEIGHT_T, 0)
        self.button_menu.setStyleSheet(button_with_icon_style)

        self.button_console = QPushButton(self.panel_up)
        self.button_console.setObjectName('title')
        self.button_console.clicked.connect(lambda: self.open_app(Console()))
        self.button_console.setIcon(self.icon_console)
        self.button_console.setIconSize(QSize(self.HEIGHT_T, self.HEIGHT_T))
        self.button_console.resize(self.HEIGHT_T + 2, self.HEIGHT_T + 2)
        self.button_console.move(self.HEIGHT_T * 2, 0)
        self.button_console.setStyleSheet(button_with_icon_style)

        self.button_web = QPushButton(self.panel_up)
        self.button_web.setObjectName('title')
        self.button_web.clicked.connect(lambda: self.open_app(Browser()))
        self.button_web.setIcon(self.icon_browser)
        self.button_web.setIconSize(QSize(self.HEIGHT_T - 5, self.HEIGHT_T - 5))
        self.button_web.resize(self.HEIGHT_T + 2, self.HEIGHT_T + 2)
        self.button_web.move(self.HEIGHT_T * 3, 0)
        self.button_web.setStyleSheet(button_with_icon_style)

        self.button_wifi = QPushButton(self.panel_up)
        self.button_wifi.setObjectName('title')
        self.button_wifi.clicked.connect(self.open_wifi)
        self.button_wifi.setIcon(self.icon_wifi)
        self.button_wifi.setIconSize(QSize(self.HEIGHT_T - 5, self.HEIGHT_T - 5))
        self.button_wifi.resize(self.HEIGHT_T + 2, self.HEIGHT_T + 2)
        self.button_wifi.move(self.width() - self.time_label.width(), 0)
        self.button_wifi.setStyleSheet(button_with_icon_style)

        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.timer_event)
        self.timer.start()

        self.timer2 = QTimer()
        self.timer2.setInterval(1000)
        self.timer2.timeout.connect(self.timer_event_sec)
        self.timer2.start()

        self.open_app(SystemMessage(QSize(500, 100), "Это Leha OS! Добро пожаловать!"))

    def open_app(self, ap):
        ap.start(self)
        for a in self.apps:
            if a.app.pos() == ap.app.pos():
                ap.app.move(a.app.x() + 10, a.app.y() + 10)
        self.apps.append(ap)

    def mouseMoveEvent(self, event):
        x, y = event.x(), event.y()
        apps_copy = [a for a in self.apps]
        apps_copy.reverse()
        for app in apps_copy:
            app.move(x, y)

    def mousePressEvent(self, event):
        x, y = event.x(), event.y()
        apps_copy = [a for a in self.apps]
        apps_copy.reverse()
        for ap in apps_copy:
            if ap.app.x() <= x <= ap.app.x() + ap.app.width() and ap.app.y() <= y <= ap.app.y() + ap.title.height():
                for a in self.apps:
                    a.app.setParent(self.layout)
                    a.app.show()
                ap.down()
                break


    def resizeEvent(self, event):
        self.layout.resize(self.size())
        self.panel_up.resize(self.width(), self.HEIGHT_T)
        self.time_label.move(self.panel_up.width() - self.time_label.width(), 0)
        self.temp_label.move(self.panel_up.width() - self.time_label.width() - self.temp_label.width(), 0)
        self.button_wifi.move(self.width() - self.time_label.width() - self.button_wifi.width() - 10, 0)

    def keyPressEvent(self, event):
        for ap in self.apps:
            ap.keyPressEvent(event)

    def timer_event(self):
        self.current_time = datetime.now().strftime("%H:%M:%S")
        self.time_label.setText(f'{self.current_time}')
        for ap in self.apps:
            ap.resizeAppEvent()
        self.unsetCursor()

    def timer_event_sec(self):
        pass
        # self.temp_label.setText(self.get_temp())

    def get_temp(self):
        gpus = GPUtil.getGPUs()
        gpu_temperature = f"{gpus[0].temperature}°C"
        return gpu_temperature

    def open_menu(self):
        if self.menu_.isHidden():
            self.menu_.show()
            self.menu_.open()
        else:
            self.menu_.hide()

    def open_wifi(self):
        if self.wifi_.isHidden():
            self.wifi_.show()
            self.wifi_.open()
        else:
            self.wifi_.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.setWindowFlags(Qt.ToolTip)
    ex.show()
    user32 = ctypes.windll.user32
    scz = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    ex.showMaximized()

    sys.exit(app.exec_())
