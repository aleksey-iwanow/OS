from settings import *
from fl1.filebrowser import *
from snake import *

#rgb(83,184,35)

class Console(AppWidget):
    def start(self, ex):
        self.TITLE = " Терминал"
        super().start(ex, self)

        self.timer = QTimer()
        self.timer.setInterval(2555)
        self.timer.timeout.connect(self.timeStep)
        self.timer.start()

        self.pushButton = QPushButton(self.window)
        self.pushButton_2 = QPushButton(self.window)
        self.pushButton_3 = QPushButton(self.window)
        self.pushButton_4 = QPushButton(self.window)
        self.pushButtonEnter = QPushButton(self.window)
        self.lineEdit = QLineEdit(self.window)
        self.textEdit = QTextEdit(self.window)

        self.pushButton = QPushButton(self.window)
        self.label = QLabel(self.window)
        self.label_2 = QLabel(self.window)

        self.pushButtonEnter.show()
        self.pushButton.show()
        self.pushButton_2.show()
        self.pushButton_3.show()
        self.pushButton_4.show()
        self.lineEdit.show()
        self.textEdit.show()
        self.textEdit.setPlaceholderText("Hello ЁпTa")
        self.label.show()
        self.label_2.show()

        self.label.move(100, 10)
        self.label_2.move(10, 10)
        self.label.resize(1000, 31)
        self.label_2.resize(81, 31)
        self.textEdit.move(10, 40)
        self.pushButtonEnter.resize(60, 40)
        self.pushButtonEnter.setStyleSheet(style_but)

        self.pushButton_2.resize(60, 40)
        self.pushButton_2.setStyleSheet(style_but)

        self.pushButton_3.resize(60, 40)
        self.pushButton_3.setStyleSheet(style_but)

        self.pushButton_4.resize(60, 40)
        self.pushButton_4.setStyleSheet(style_but)

        self.pushButton.resize(60, 40)
        self.pushButton.setStyleSheet(style_but)
        self.pushButton.setText("Exit")

        self.pushButton.clicked.connect(self.close_nano)
        self.lineEdit.setStyleSheet(f"border: 2px solid #121C16; "
                                    f"background: rgb(0,0,0,0)")
        self.style_ = """border: none; background: rgb(0,0,0,0); """
        self.textEdit.setStyleSheet(self.style_)
        self.textEdit.setReadOnly(True)
        self.pushButton_2.clicked.connect(self.terminate_file)
        self.pushButton_4.clicked.connect(self.save_file)
        self.pushButton_3.clicked.connect(self.open_file_1)

        self.pushButton_4.hide()
        self.pushButton_3.hide()
        self.pushButton_2.hide()
        self.pushButton.hide()
        self.pushButtonEnter.clicked.connect(self.send_command)
        self.pushButtonEnter.setText('Esc')
        self.fl = ""
        self.nano_file = None
        self.fl_is_run = False
        self.function_set_txt = None
        self.pos_cur = None
        self.label.setText(f'┌{os.getcwd()}┐')
        self.set_cursor()
        self.text_main = f'''<span style="color:green;">НАЧАЛО РАБОТЫ!</span><br>'''

    # слот для таймера
    def timeStep(self):
        pass

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.send_command()

    def resizeEvent(self):
        self.textEdit.resize(self.WIDTH - 20, self.HEIGHT - 80)
        self.lineEdit.resize(self.WIDTH - 70, 40)
        self.lineEdit.move(10, self.HEIGHT - 40)
        self.pushButtonEnter.move(self.WIDTH - 60, self.HEIGHT - 40)
        self.pushButton_2.move(10, self.HEIGHT - 40)
        self.pushButton_3.move(70, self.HEIGHT - 40)
        self.pushButton_4.move(130, self.HEIGHT - 40)
        self.pushButton.move(190, self.HEIGHT - 40)

    def send_command(self):
        cp = os.getcwd()

        def set_txt(out=""):
            self.textEdit.setText(
                f'<div>{self.text_main}{titleFormat.format(cp + "~")} {command}<br><span style="background-color: #AB274F">#</span> {out if out else output}{darkgreenFormat.format(" ")}</div>')
            self.text_main = self.textEdit.toHtml()
            self.set_cursor()
            self.label.setText(f'┌{os.getcwd()}┐')

        if not self.function_set_txt:
            self.function_set_txt = set_txt

        command = self.lineEdit.text()
        if not command:
            return
        output = ""
        fcm = command.split()[0]
        fcms = command.split()[0].split('.')
        arg = command[len(fcm) + 1:]

        ch = "<font color=rgb(0,0,0,0)>&nbsp;</font>"
        path_ = ''

        if fcm in commands:
            if fcm == commands['cd'][0]:
                try:
                    os.chdir(arg if ":" in arg else (os.getcwd() + '\\' + arg))
                    output = os.getcwd()
                except Exception as ex:
                    output += errorFormat.format(ex)
            if fcm == commands['system'][0]:
                try:
                    data = subprocess.check_output(arg)
                    print(data.decode(encoding='ascii'))

                except Exception as ex:
                    output += errorFormat.format(ex)
            elif fcm == commands['clear'][0]:
                self.text_main = ''
                output = 'Консоль очищена.'
            elif fcm == commands['nano'][0]:
                try:
                    path_ = arg if ":" in arg else (os.getcwd() + '\\' + arg)

                except Exception as ex:
                    output += errorFormat.format(ex)
            elif fcms[0] == commands['ls'][0]:
                onlyfiles = ''
                if len(fcms) > 1:
                    if fcms[1] == 'DIRS':
                        onlyfiles = [f for f in listdir(cp) if not os.path.isfile(os.path.join(cp, f))]
                    elif fcms[1] == 'FILES':
                        onlyfiles = [f for f in listdir(cp) if os.path.isfile(os.path.join(cp, f))]
                else:
                    # if os.path.isfile(os.path.join(cp, f))
                    onlyfiles = [f for f in listdir(cp)]

                output = f",{ch * 2}".join(onlyfiles)
            elif fcm == commands['help'][0]:
                try:
                    for i in commands:
                        name = f"{i}:"
                        ln = 20 - len(name)
                        output += '<br>' + f'{validFormat.format(name)}{ln * ch}{darkgreenFormat.format(commands[i][1])}</span>'
                except Exception as ex:
                    output += errorFormat.format(ex)
            elif fcm == commands['systeminfo'][0]:
                inf = json.loads(get_system_info())

                for i in inf:
                    name = f"{i}:"
                    ln = 20 - len(name)
                    output += f'<br>{validFormat.format(name)}{ln * ch}{darkgreenFormat.format(inf[i])}</span>'

        else:
            output = warningFormat.format("Команда не обнаружена! (help - список команд)")

        if path_:
            ex = self.active_nano(path_)
            if ex:
                set_txt(ex)
        else:
            set_txt()

        count = len(self.textEdit.toPlainText().split("\n"))
        self.label_2.setText(f'┌{count}┐')

    def active_nano(self, pt):
        try:
            self.nano_file = pt
            self.open_file(pt)
            self.textEdit.setReadOnly(False)
            self.lineEdit.hide()
            self.pushButtonEnter.hide()
            self.pushButton_4.show()
            self.pushButton_3.show()
            self.pushButton_2.show()
            self.pushButton.show()
            self.label_2.show()
            return ""
        except Exception as ex:
            print(ex)
            return errorFormat.format(ex)

    def close_nano(self):
        self.textEdit.setReadOnly(True)
        self.lineEdit.show()
        self.pushButtonEnter.show()
        self.pushButton_4.hide()
        self.pushButton_3.hide()
        self.pushButton_2.hide()
        self.pushButton.hide()
        self.label_2.hide()
        self.function_set_txt("nano exit")
        return ""

    def set_cursor(self):
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.textEdit.setTextCursor(cursor)

    def run_file(self):
        if self.fl:
            self.fl_is_run = True
            os.system(f'python {self.fl}')

    def open_file_1(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         "Выбрать файл",
                                                         ".",
                                                         "Text Files(*.txt);;Python File(*.py);;All Files(*)")
        if filename.strip():
            self.open_file(filename)

    def save_file(self):
        filename, ok = QFileDialog.getSaveFileName(self,
                                                   "Сохранить файл",
                                                   ".",
                                                   "All Files(*.*)")
        if ok:
            with open(filename, 'w', encoding="utf-8") as fl:
                fl.write(self.textEdit.toPlainText())

    def terminate_file(self):
        if self.fl_is_run:
            self.fl_is_run = False
            ext_proc = sp.Popen(['python', self.fl.split('\\')[-1]])
            sp.Popen.terminate(ext_proc)

    def update_nano(self, file_):
        with open(file_, 'r', encoding="utf-8") as fl__:
            tx = fl__.read()

            self.textEdit.setPlainText(tx)
            ht = self.textEdit.toHtml()

            is_code = False
            for h in ht.split():
                if h.startswith('text-indent:0px;">'):
                    is_code = True
                if is_code:
                    h2 = h.replace("if", validFormat.format("if"))
                    ht = ht.replace(h, h2)

                if h.endswith('</p>'):
                    is_code = False

            self.textEdit.setText(f'{ht}')
            count = len(tx.split("\n"))
            self.label_2.setText(f'┌{count}┐')

    def open_file(self, file_):
        fl = sys.argv[0]
        fl = fl.replace('/', '\\')
        nm = file_.split("\\")[-1]
        self.fl = ""
        if file_ != fl:
            if file_.endswith('.py') or file_.endswith('.pyr'):
                self.fl = file_
            self.label.setText(f'┌{nm}┐')

            self.update_nano(file_)
        self.set_cursor()


class Calculator(AppWidget):
    def start(self, ex):
        self.TITLE = " Калькулятор"
        super().start(ex, self)
        self.app.resize(360, 385)
        self.app.setMinimumSize(360,385)
        self.app.setMaximumSize(360,385)
        # calling method
        self.UiComponents()

        # method for widgets

    def resizeEvent(self):
        pass

    def keyPressEvent(self, event):
        pass


    def UiComponents(self):
        # creating a label
        self.label = QLabel(self.window)

        # setting geometry to the label
        self.label.setGeometry(5, 5, 350, 70)
        self.label.show()
        # creating label multi line
        self.label.setWordWrap(True)

        # setting style sheet to the label
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 4px solid rgb(83,184,35);"
                                 "background : rgb(0,0,0,0);"
                                 "}")

        # setting alignment to the label
        self.label.setAlignment(Qt.AlignRight)

        # setting font
        self.label.setFont(QFont('Arial', 15))

        # adding number button to the screen
        # creating a push button
        push1 = QPushButton("1", self.window)
        push1.show()
        # setting geometry
        push1.setGeometry(5, 150, 80, 40)
        push1.setStyleSheet(style_but)
        # creating a push button
        push2 = QPushButton("2", self.window)
        push2.show()
        push2.setStyleSheet(style_but)
        # setting geometry
        push2.setGeometry(95, 150, 80, 40)

        # creating a push button
        push3 = QPushButton("3", self.window)
        push3.show()
        push3.setStyleSheet(style_but)
        push3.setGeometry(185, 150, 80, 40)

        push4 = QPushButton("4", self.window)
        push4.show()
        push4.setStyleSheet(style_but)
        push4.setGeometry(5, 200, 80, 40)

        push5 = QPushButton("5", self.window)
        push5.show()
        push5.setStyleSheet(style_but)
        push5.setGeometry(95, 200, 80, 40)

        push6 = QPushButton("5", self.window)
        push6.show()
        push6.setStyleSheet(style_but)
        push6.setGeometry(185, 200, 80, 40)

        push7 = QPushButton("7", self.window)
        push7.show()
        push7.setStyleSheet(style_but)
        push7.setGeometry(5, 250, 80, 40)

        push8 = QPushButton("8", self.window)
        push8.show()
        push8.setStyleSheet(style_but)
        push8.setGeometry(95, 250, 80, 40)

        push9 = QPushButton("9", self.window)
        push9.show()
        push9.setStyleSheet(style_but)
        push9.setGeometry(185, 250, 80, 40)

        push0 = QPushButton("0", self.window)
        push0.show()
        push0.setStyleSheet(style_but)
        push0.setGeometry(5, 300, 80, 40)

        # adding operator push button
        # creating push button
        push_equal = QPushButton("=", self.window)
        push_equal.show()
        push_equal.setStyleSheet(style_but)
        push_equal.setGeometry(275, 300, 80, 40)

        # adding equal button a color effect
        c_effect = QGraphicsColorizeEffect()
        c_effect.setColor(Qt.blue)
        push_equal.setGraphicsEffect(c_effect)

        # creating push button
        push_plus = QPushButton("+", self.window)
        push_plus.show()
        push_plus.setStyleSheet(style_but)
        push_plus.setGeometry(275, 250, 80, 40)

        # creating push button
        push_minus = QPushButton("-", self.window)
        push_minus.show()
        push_minus.setStyleSheet(style_but)
        push_minus.setGeometry(275, 200, 80, 40)

        push_mul = QPushButton("*", self.window)
        push_mul.show()
        push_mul.setStyleSheet(style_but)
        push_mul.setGeometry(275, 150, 80, 40)

        push_div = QPushButton("/", self.window)
        push_div.show()
        push_div.setStyleSheet(style_but)
        push_div.setGeometry(185, 300, 80, 40)

        push_point = QPushButton(".", self.window)
        push_point.show()
        push_point.setStyleSheet(style_but)
        push_point.setGeometry(95, 300, 80, 40)

        push_clear = QPushButton("Clear", self.window)
        push_clear.setGeometry(5, 100, 200, 40)
        push_clear.show()
        push_clear.setStyleSheet(style_but)
        push_del = QPushButton("Del", self.window)
        push_del.setGeometry(210, 100, 145, 40)
        push_del.show()
        push_del.setStyleSheet(style_but)

        push_minus.clicked.connect(self.action_minus)
        push_equal.clicked.connect(self.action_equal)
        push0.clicked.connect(self.action0)
        push1.clicked.connect(self.action1)
        push2.clicked.connect(self.action2)
        push3.clicked.connect(self.action3)
        push4.clicked.connect(self.action4)
        push5.clicked.connect(self.action5)
        push6.clicked.connect(self.action6)
        push7.clicked.connect(self.action7)
        push8.clicked.connect(self.action8)
        push9.clicked.connect(self.action9)
        push_div.clicked.connect(self.action_div)
        push_mul.clicked.connect(self.action_mul)
        push_plus.clicked.connect(self.action_plus)
        push_point.clicked.connect(self.action_point)
        push_clear.clicked.connect(self.action_clear)
        push_del.clicked.connect(self.action_del)


    def action_equal(self):
        # get the label text
        equation = self.label.text()

        try:
            # getting the ans
            ans = eval(equation)

            # setting text to the label
            self.label.setText(str(ans))

        except:
            # setting text to the label
            self.label.setText("Wrong Input")


    def action_plus(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " + ")


    def action_minus(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " - ")


    def action_div(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " / ")


    def action_mul(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " * ")


    def action_point(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + ".")


    def action0(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "0")


    def action1(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "1")


    def action2(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "2")


    def action3(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "3")


    def action4(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "4")


    def action5(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "5")


    def action6(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "6")


    def action7(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "7")


    def action8(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "8")


    def action9(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "9")


    def action_clear(self):
        # clearing the label text
        self.label.setText("")


    def action_del(self):
        # clearing a single digit
        text = self.label.text()
        print(text[:len(text) - 1])
        self.label.setText(text[:len(text) - 1])


class Browser(AppWidget):
    def start(self, ex):
        self.TITLE = " Браузер"
        super().start(ex, self)
        self.win = FrameWeb()
        self.app.setMinimumSize(1166, 568)
        self.win.move(0, 0)
        self.win.setParent(self.window)
        self.win.show()

    def resizeEvent(self):
        self.win.resize(self.window.size())

    def keyPressEvent(self, event):
        pass


class FileManager(AppWidget):
    def start(self, ex):
        self.TITLE = " Файловый менеджер"
        super().start(ex, self)
        self.win = FileManagerWidget()
        self.app.setMinimumSize(1166, 568)
        self.win.move(0, 0)
        self.win.setParent(self.window)
        self.win.show()

    def resizeEvent(self):
        self.win.resize(self.window.size())

    def keyPressEvent(self, event):
        pass


class SystemMessage(AppWidget):
    def __init__(self, size, text):
        self.SIZE = size
        self.TEXT = text

    def start(self, ex):
        self.TITLE = " Сообщение"
        super().start(ex, self, self.SIZE.width(), self.SIZE.height())
        self.ex = ex
        self.app.setMinimumSize(self.SIZE)
        self.app.setMaximumSize(self.SIZE)
        self.label = QLabel(self.window)
        self.label.show()
        self.resizeEvent()
        self.label.setText(self.TEXT)

    def resizeEvent(self):
        self.label.move(10, 0)
        self.label.resize(self.WIDTH - 10, self.HEIGHT)

    def keyPressEvent(self, event):
        pass


class Snake1(AppWidget):

    def start(self, ex):
        self.TITLE = " Змейка"
        self.SIZE = QSize(1000, 700)
        super().start(ex, self, self.SIZE.width(), self.SIZE.height())
        self.ex = ex
        self.app.setMinimumSize(self.SIZE)
        self.app.setMaximumSize(self.SIZE)
        launch_game = SnakeGame()
        launch_game.show()
        self.resizeEvent()

    def resizeEvent(self):
        pass

    def keyPressEvent(self, event):
        pass



class FrameWeb(QFrame):
    def __init__(self):
        super().__init__()

        self.CreateApp()

    def CreateApp(self):
        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # Create Tab
        self.tabbar = QTabBar(movable=True, tabsClosable=True)
        self.tabbar.tabCloseRequested.connect(self.CloseTab)
        self.tabbar.tabBarClicked.connect(self.SwitchTab)
        # set the current index of tab bar that tell the tabbar which tab is active
        self.tabbar.setCurrentIndex(0)  # initialize with active tab bar
        self.tabbar.setDrawBase(False)

        self.shortcutNewTab = QShortcut(QKeySequence("Ctrl+T"), self)
        self.shortcutNewTab.activated.connect(self.AddTab)

        self.shortcutReload = QShortcut(QKeySequence("Ctrl+R"), self)
        self.shortcutReload.activated.connect(self.ReloadPage)

        #Keep track of tabs and corresponding tab content
        self.tabCount = 0
        self.tabs =[] #contains every widget that belong to a tab; tab object


        # Create AddressBar
        self.Toolbar = QWidget()
        self.Toolbar.setObjectName("Toolbar")
        self.ToolbarLayout = QHBoxLayout()
        self.addressbar = AddressBar()
        self.AddTabButton = QPushButton("+")

        #Connect AddressBar + button Signals
        self.addressbar.returnPressed.connect(self.BrowseTo)
        self.AddTabButton.clicked.connect(self.AddTab)  # connect AddTabButton to method def AddTab(self):

        #Set Toolbar Buttons
        self.BackButton = QPushButton("<")
        self.BackButton.clicked.connect(self.GoBack)

        self.ForwardButton = QPushButton(">")
        self.ForwardButton.clicked.connect(self.GoForward)

        self.ReloadButton = QPushButton("R")
        self.ReloadButton.clicked.connect(self.ReloadPage)


        #Build toolbar
        self.Toolbar.setLayout(self.ToolbarLayout)
        self.ToolbarLayout.addWidget(self.BackButton)
        self.ToolbarLayout.addWidget(self.ForwardButton)
        self.ToolbarLayout.addWidget(self.ReloadButton)
        self.ToolbarLayout.addWidget(self.addressbar)
        self.ToolbarLayout.addWidget(self.AddTabButton)

        #set main view
        self.container = QWidget()
        self.container.layout = QStackedLayout()
        self.container.setLayout(self.container.layout) #tell QWidget() to use QStackedLayout()

        #stacked layout
        self.layout.addWidget(self.tabbar)
        self.layout.addWidget(self.Toolbar)
        self.layout.addWidget(self.container)


        self.setLayout(self.layout)

        #calling AddTab so there is always a tab active
        self.AddTab()

        self.show()

    def CloseTab(self, i):
        self.tabbar.removeTab(i)

    def AddTab(self):
        i = self.tabCount

        #Set self.tab<#> = QWidget
        self.tabs.append(QWidget()) #add stuff to self.tablist
        self.tabs[i].layout = QVBoxLayout() #modify the widget which access QWidget, can be treated as same QWidget b/c it's targeting QWidget
        self.tabs[i].layout.setContentsMargins(0, 0, 0, 0)




        #For tab switching
        self.tabs[i].setObjectName("tab" + str(i))

        #Create webview within the tabs top level widget
        self.tabs[i].content = QWebEngineView()
        self.tabs[i].content.load(QUrl.fromUserInput("http://google.com"))

        #self.tabs[i].content1 = QWebEngineView()
        #self.tabs[i].content1.load(QUrl.fromUserInput("http://google.com"))

        self.tabs[i].content.titleChanged.connect(lambda: self.SetTabContent(i, "title"))
        self.tabs[i].content.iconChanged.connect(lambda: self.SetTabContent(i,"icon"))
        self.tabs[i].content.urlChanged.connect(lambda: self.SetTabContent(i, "url"))

        #Add widget to tab .layout
        self.tabs[i].layout.addWidget(self.tabs[i].content)
        #self.tabs[i].splitview = QSplitter()
        #self.tabs[i].splitview.setOrientation(Qt.Vertical)
        #self.tabs[i].layout.addWidget(self.tabs[i].splitview)

        #self.tabs[i].splitview.addWidget(self.tabs[i].content)
        #self.tabs[i].splitview.addWidget(self.tabs[i].content1)

        #Set tabLayout to .layout
        self.tabs[i].setLayout(self.tabs[i].layout)

        #Add and set new tabs content to the stack widget
        self.container.layout.addWidget(self.tabs[i])
        self.container.layout.setCurrentWidget(self.tabs[i])

        #Create tab on tabbar, representing this tab,
        #Set tabData to tab<#> So it knows what self.tabs[#] it needs to control
        self.tabbar.addTab("New Tab")
        #tell tab what object name it should control
        self.tabbar.setTabData(i, {"object": "tab" + str(i), "initial": i})


        self.tabbar.setCurrentIndex(i)

        #increase tab count
        self.tabCount += 1

    def SetAddressBar(self, i):
        # Get the current tabs index, and set the address bar to its title.toString()
        tab = self.tabbar.tabData(i)["object"]
        if self.findChild(QWidget, tab).content == True:
            url = QUrl(self.findChild(QWidget, tab).content.url()).toString()
            self.AddressBar.setText(url)

    def SwitchTab(self, i):
        #Switch to tab, get currents tabs tabData ("tab0") and find object with that name
        if self.tabbar.tabData(i):
            tab = self.tabbar.tabData(i)["object"]
            self.container.layout.setCurrentWidget(self.findChild(QWidget, tab))
            self.SetAddressBar(i)
            print(self.tabs[i].content.nativeParentWidget())


    def BrowseTo(self):
        txt = self.addressbar.text()
        print(txt)

        #getting the index of current tab, set the tab to that index, and
        i = self.tabbar.currentIndex()
        tab = self.tabbar.tabData(i)["object"]
        web_view = self.findChild(QWidget, tab).content


        if "http" not in txt:
            if "." not in txt:
                url = "https://www.google.com/search?q=" + txt
            else:
                url = "http://" + txt
        else:
            url = txt

        web_view.load(QUrl.fromUserInput(url))

    def SetTabContent(self, i, type):
        '''
            self.tabs[i].objectName = tab1
            self.tabbar.tabData(i)["object"] = tab1
        '''
        tab_name  = self.tabs[i].objectName()
        #tab1

        count = 0
        running = True
        '''
        #create a SetAddressBar method
        current_tab = self.tabbar.tabData(self.tabbar.currentIndex())["object"]

        if current_tab == tab_name and type == "url":
            new_url = self.findChild(QWidget, tab_name).content.url().toString()
            self.addressbar.setText(new_url)
            return False
        '''


        while running:
            tab_data_name = self.tabbar.tabData(count)

            if count >= 99:
                running = False

            if tab_name  == tab_data_name["object"]:
                if type == "title":
                    newTitle = self.findChild(QWidget, tab_name).content.title()
                    self.tabbar.setTabText(count,newTitle)
                elif type == "icon":
                    newIcon = self.findChild(QWidget, tab_name).content.icon()
                    self.tabbar.setTabIcon(count, newIcon)
                running = False
            else:
                count += 1


    def GoBack(self):
        activeIndex = self.tabbar.currentIndex()
        tab_name = self.tabbar.tabData(activeIndex)["object"]
        tab_content = self.findChild(QWidget, tab_name).content

        tab_content.back()

    def GoForward(self):
        activeIndex = self.tabbar.currentIndex()
        tab_name = self.tabbar.tabData(activeIndex)["object"]
        tab_content = self.findChild(QWidget, tab_name).content

        tab_content.forward()

    def ReloadPage(self):
        activeIndex = self.tabbar.currentIndex()
        tab_name = self.tabbar.tabData(activeIndex)["object"]
        tab_content = self.findChild(QWidget, tab_name).content

        tab_content.reload()