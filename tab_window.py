from PyQt5 import QtCore, QtGui, QtWidgets
from tabs.tab1 import Tab1
from tabs.tab2 import Tab2

# Not so dark
color1 = '#5a6175'

# Dark
color2 = '#4b5162'

# Darker
color3 = '#4e5463'

# Darkest
color4 = '#383c4a'

# Most Dark
color5 = '#191b21'

# Fonts
font_color = '#e6ebff'
dark_font_color = '#777f96'

# Intermediate Dark?
color6 = '#434859'


button_style = f'''
QPushButton:!hover{{
background-color: #b3322e;
width: 32px;
height: 64px;
font-size: 25px;
color: {font_color}
}}

QPushButton:hover{{
background-color: #9e2e2c;
width: 32px;
height: 64px;
font-size: 25px;
color: {font_color}
}}

QPushButton:pressed{{
background-color: #691d1b;
width: 32px;
height: 64px;
font-size: 25px;
color: {font_color}

}}'''


class Main(QtWidgets.QWidget):
    def __init__(self):
        super(Main, self).__init__()

        self.tab1 = Tab1('F1')
        self.tab2 = Tab1('F2')
        self.tab3 = Tab1('Summative')
        self.tab4 = Tab1('Semestral')
        self.tab5 = Tab2()

        self.oldPos = self.pos()

        self.available = QtWidgets.QDesktopWidget().availableGeometry().getRect()
        self.fullscreened = True

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setContentsMargins(0, 0, 0, 0)

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        # Left side
        self.leftGroupBox = QtWidgets.QGroupBox()
        self.leftGroupBox.setContentsMargins(0, 0, 0, 0)
        self.leftGridLayout = QtWidgets.QGridLayout(self.leftGroupBox)
        self.leftGridLayout.setContentsMargins(0, 0, 0, 0)
        self.leftGridLayout.setSpacing(0)

        self.gradeTypeLabel = QtWidgets.QLabel()
        self.gradeTypeLabel.setText('GRADE TYPE')
        self.gradeTypeLabel.setAlignment(QtCore.Qt.AlignLeft)

        self.gradeLabel = QtWidgets.QLabel()
        self.gradeLabel.setText('FINAL GRADES')
        self.gradeLabel.setAlignment(QtCore.Qt.AlignLeft)

        self.tabButton0 = QtWidgets.QPushButton()
        self.tabButton0.setText('F1')
        self.tabButton0.clicked.connect(lambda: self.update_tab_stylesheets(0))

        self.tabButton0_clear = QtWidgets.QPushButton()
        self.tabButton0_clear.setText('')
        self.tabButton0_clear.clicked.connect(self.tab1.clear_grades)

        self.tabButton1 = QtWidgets.QPushButton()
        self.tabButton1.setText('F2')
        self.tabButton1.clicked.connect(lambda: self.update_tab_stylesheets(1))

        self.tabButton1_clear = QtWidgets.QPushButton()
        self.tabButton1_clear.setText('')
        self.tabButton1_clear.clicked.connect(self.tab2.clear_grades)

        self.tabButton2 = QtWidgets.QPushButton()
        self.tabButton2.setText('SUMMATIVE')
        self.tabButton2.clicked.connect(lambda: self.update_tab_stylesheets(2))

        self.tabButton2_clear = QtWidgets.QPushButton()
        self.tabButton2_clear.setText('')
        self.tabButton2_clear.clicked.connect(self.tab3.clear_grades)

        self.tabButton3 = QtWidgets.QPushButton()
        self.tabButton3.setText('SEMESTRAL')
        self.tabButton3.clicked.connect(lambda: self.update_tab_stylesheets(3))

        self.tabButton3_clear = QtWidgets.QPushButton()
        self.tabButton3_clear.setText('')
        self.tabButton3_clear.clicked.connect(self.tab4.clear_grades)

        self.tabButton4 = QtWidgets.QPushButton()
        self.tabButton4.setText('TOTAL GRADE')
        self.tabButton4.clicked.connect(lambda: self.update_tab_stylesheets(4))

        self.verticalSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        # Top
        self.topGroupBox = QtWidgets.QGroupBox()
        self.topGridLayout = QtWidgets.QGridLayout(self.topGroupBox)
        self.topGridLayout.setSpacing(0)
        self.topGridLayout.setContentsMargins(0, 0, 0, 0)

        # Top Upper
        self.topGroupBox_1 = QtWidgets.QGroupBox()
        self.topGroupBox_1.setContentsMargins(0, 0, 0, 0)
        self.topGridLayout_1 = QtWidgets.QGridLayout(self.topGroupBox_1)
        self.topGridLayout.setSpacing(0)
        self.topGridLayout_1.setContentsMargins(0, 0, 0, 0)
        self.topGridLayout_1.setSpacing(25)

        # Quit Button
        self.quitButton = QtWidgets.QLabel()
        self.quitButton.setPixmap(QtGui.QPixmap('close_button.png').scaled(26, 26))
        self.quitButton.mousePressEvent = self.quit_application
        self.quitButton.setAlignment(QtCore.Qt.AlignVCenter)

        # Maximize Button
        self.maximizeButton = QtWidgets.QLabel()
        self.maximizeButton.setPixmap(QtGui.QPixmap('maximize_button.png').scaled(23, 23))
        self.maximizeButton.mousePressEvent = self.maximize
        self.maximizeButton.mouseReleaseEvent = self.maximize_release
        self.maximizeButton.setAlignment(QtCore.Qt.AlignVCenter)

        # Minimize Button
        self.minimizeButton = QtWidgets.QLabel()
        self.minimizeButton.setPixmap(QtGui.QPixmap('minimize_button.png').scaled(26, 26))
        self.minimizeButton.mousePressEvent = self.minimize
        self.minimizeButton.setAlignment(QtCore.Qt.AlignVCenter)

        self.spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.topGroupBox_1.mousePressEvent = self.mousePressMoveEvent
        self.topGroupBox_1.mouseMoveEvent = self.mouseMoveMoveEvent

        # Top Lower
        self.topGroupBox_2 = QtWidgets.QGroupBox()

        # Icon
        self.iconGroupBox = QtWidgets.QGroupBox()
        self.iconGridLayout = QtWidgets.QGridLayout(self.iconGroupBox)
        self.iconGridLayout.setSpacing(0)
        self.iconGridLayout.setContentsMargins(0, 0, 0, 0)

        # Icon Upper
        self.iconGroupBox_1 = QtWidgets.QGroupBox()
        self.iconGridLayout_1 = QtWidgets.QGridLayout(self.iconGroupBox_1)
        self.iconGridLayout_1.setSpacing(0)
        self.iconGridLayout_1.setContentsMargins(0, 0, 0, 0)
        self.placeholderButton = QtWidgets.QLabel()
        self.placeholderButton.setPixmap(QtGui.QPixmap('empty.png').scaled(26, 26))
        self.placeholderButton.setAlignment(QtCore.Qt.AlignLeft)

        self.iconGroupBox_1.mousePressEvent = self.mousePressMoveEvent
        self.iconGroupBox_1.mouseMoveEvent = self.mouseMoveMoveEvent

        # Icon Lower
        self.iconGroupBox_2 = QtWidgets.QGroupBox()

        # Content (IMPORTANT)
        self.contentGroupBox = QtWidgets.QGroupBox()
        self.contentGroupBox.setContentsMargins(0, 0, 0, 0)
        self.contentGridLayout = QtWidgets.QGridLayout(self.contentGroupBox)
        self.contentGridLayout.setContentsMargins(0, 0, 0, 0)
        self.contentGridLayout.setSpacing(0)

        self.tabWidget = QtWidgets.QTabWidget()
        self.tabWidget.currentChanged.connect(self.tab_changed)

        self.tabWidget.addTab(self.tab1, 'F1')
        self.tabWidget.addTab(self.tab2, 'F2')
        self.tabWidget.addTab(self.tab3, 'Summative')
        self.tabWidget.addTab(self.tab4, 'Semestral')
        self.tabWidget.addTab(self.tab5, 'Total Grade')

        # Add Widgets
        self.gridLayout.addWidget(self.leftGroupBox, 1, 0, 9, 1)

        self.leftGridLayout.addWidget(self.gradeTypeLabel, 0, 0)
        self.leftGridLayout.addWidget(self.tabButton0, 1, 0)
        self.leftGridLayout.addWidget(self.tabButton0_clear, 1, 1)
        self.leftGridLayout.addWidget(self.tabButton1, 2, 0)
        self.leftGridLayout.addWidget(self.tabButton1_clear, 2, 1)
        self.leftGridLayout.addWidget(self.tabButton2, 3, 0)
        self.leftGridLayout.addWidget(self.tabButton2_clear, 3, 1)
        self.leftGridLayout.addWidget(self.tabButton3, 4, 0)
        self.leftGridLayout.addWidget(self.tabButton3_clear, 4, 1)
        self.leftGridLayout.addItem(self.verticalSpacer, 5, 0)
        self.leftGridLayout.addWidget(self.gradeLabel, 6, 0)
        self.leftGridLayout.addWidget(self.tabButton4, 7, 0)

        self.topGridLayout_1.addWidget(self.quitButton, 0, 3)
        self.topGridLayout_1.addWidget(self.maximizeButton, 0, 2)
        self.topGridLayout_1.addWidget(self.minimizeButton, 0, 1)
        self.topGridLayout_1.addItem(self.spacer, 0, 0)
        self.topGridLayout.addWidget(self.topGroupBox_1, 0, 0, 2, 0)
        self.topGridLayout.addWidget(self.topGroupBox_2, 2, 0, 4, 0)
        self.gridLayout.addWidget(self.topGroupBox, 0, 1, 1, 7)
        self.iconGridLayout.addWidget(self.iconGroupBox_1, 0, 0, 2, 0)
        self.iconGridLayout.addWidget(self.iconGroupBox_2, 2, 0, 4, 0)
        self.iconGridLayout_1.addWidget(self.placeholderButton, 0, 1)
        self.gridLayout.addWidget(self.iconGroupBox, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.contentGroupBox, 1, 1, 9, 7)
        self.contentGridLayout.addWidget(self.tabWidget, 0, 0)

        # Stylesheets
        self.leftGroupBox.setStyleSheet(f'''
        background-color: {color3};
        border: none
        ''')

        self.topGroupBox.setStyleSheet(f'''
        background-color: {color1};
        border: none
        ''')
        self.topGroupBox_1.setStyleSheet(f'''
        background-color: {color5};
        border: none
        ''')
        self.iconGroupBox.setStyleSheet(f'''
        background-color: {color3};
        border: none
        ''')
        self.iconGroupBox_1.setStyleSheet(f'''
        background-color: {color5};
        border: none
        ''')
        self.contentGroupBox.setStyleSheet(f'''
        background-color: {color1};
        border: none
        ''')
        self.tabButton0_clear.setStyleSheet(button_style)
        self.tabButton1_clear.setStyleSheet(button_style)
        self.tabButton2_clear.setStyleSheet(button_style)
        self.tabButton3_clear.setStyleSheet(button_style)

        self.tabWidget.setStyleSheet(f'''
        QTabWidget QTabBar::tab{{
        height: 0px;
        width: 0px;
        border: none
        }}
    
        QTabWidget::pane{{
        border: none
        }}
        ''')

        self.update_tab_stylesheets(0)

        subtitle_stylesheet = (f'''
        font-size: 15px;
        font-weight: 900;
        padding-top: 20px;
        padding-bottom: 5px;
        color: {dark_font_color}
        ''')

        self.gradeTypeLabel.setStyleSheet(subtitle_stylesheet)
        self.gradeLabel.setStyleSheet(subtitle_stylesheet)

        self.setStyleSheet(f'''
        *{{
        font-family: Segoe UI
        }}
        ''')

        self.maximize_release('')

    def tab_changed(self, i):
        pass

    def update_tab_stylesheets(self, number):

        self.tabWidget.setCurrentIndex(number)

        not_selected_stylesheet = f'''
        QPushButton:!hover{{
        background-color: {color3};
        width: 256px;
        height: 64px;
        font-size: 20px;
        color: {font_color}
        }}

        QPushButton:hover{{
        background-color: {color6};
        width: 256px;
        height: 64px;
        font-size: 20px;
        color: {font_color}
        }}
        '''
        selected_stylesheet = f'''
        QPushButton:!hover{{
        background-color: {color4};
        width: 256px;
        height: 64px;
        font-size: 20px;
        color: {font_color}
        }}

        QPushButton:hover{{
        background-color: {color4};
        width: 256px;
        height: 64px;
        font-size: 20px;
        color: {font_color}
        }}
        '''

        button1_not_selected_stylesheet = f'''
        QPushButton:!hover{{
        background-color: {color3};
        width: 256px;
        height: 64px;
        font-size: 20px;
        color: {font_color}
        }}

        QPushButton:hover{{
        background-color: {color6};
        width: 256px;
        height: 64px;
        font-size: 20px;
        color: {font_color}
        }}
        '''

        button1_selected_stylesheet = f'''
        QPushButton:!hover{{
        background-color: {color4};
        width: 256px;
        height: 64px;
        font-size: 20px;
        color: {font_color}
        }}

        QPushButton:hover{{
        background-color: {color4};
        width: 256px;
        height: 64px;
        font-size: 20px;
        color: {font_color}
        }}
        '''

        if self.tabWidget.currentIndex() == 0:
            self.tabButton0.setStyleSheet(button1_selected_stylesheet)
        else:
            self.tabButton0.setStyleSheet(button1_not_selected_stylesheet)

        if self.tabWidget.currentIndex() == 1:
            self.tabButton1.setStyleSheet(selected_stylesheet)
        else:
            self.tabButton1.setStyleSheet(not_selected_stylesheet)

        if self.tabWidget.currentIndex() == 2:
            self.tabButton2.setStyleSheet(selected_stylesheet)
        else:
            self.tabButton2.setStyleSheet(not_selected_stylesheet)

        if self.tabWidget.currentIndex() == 3:
            self.tabButton3.setStyleSheet(selected_stylesheet)
        else:
            self.tabButton3.setStyleSheet(not_selected_stylesheet)

        if self.tabWidget.currentIndex() == 4:
            self.tabButton4.setStyleSheet(selected_stylesheet)
        else:
            self.tabButton4.setStyleSheet(not_selected_stylesheet)

    def quit_application(self, event):
        app.quit()

    def minimize(self, event):
        self.showMinimized()

    def maximize(self, event):
        pass

    def maximize_release(self, event):
        if self.fullscreened:
            self.fullscreened = False
            self.resize(round(self.available[2] / 1.5), round(self.available[3] / 1.5))
            self.move(QtWidgets.QDesktopWidget().availableGeometry().topLeft())

        else:
            self.fullscreened = True
            self.setGeometry(self.available[0], self.available[1], self.available[2], self.available[3])
            self.move(QtWidgets.QDesktopWidget().availableGeometry().topLeft())

    def mousePressMoveEvent(self, event):
        if not self.fullscreened:
            self.oldPos = event.globalPos()

    def mouseMoveMoveEvent(self, event):
        if not self.fullscreened:
            delta = QtCore.QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())
