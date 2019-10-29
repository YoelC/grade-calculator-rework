from PyQt5 import QtCore, QtGui, QtWidgets


# Not so dark
color1 = '#5a6175'

# Dark
color2 = '#69718a'

# Darker
color3 = '#7a84a1'

# Darkest
color4 = '#464b5c'

# Most Dark
color5 = '#575e73'

# Fonts
font_color = '#e6ebff'
dark_font_color = '#e6ebff'

# Intermediate Dark?
color6 = '#67708a'


class Tab1(QtWidgets.QWidget):
    def __init__(self, grade_type):
        super(Tab1, self).__init__()

        self.grade_type = grade_type

        self.grades = {

        }
        self.max_grades = 1
        self.average = 'succ'

        self.resize(800, 350)
        self.gridLayout = QtWidgets.QGridLayout(self)

        self.gradeLabel = QtWidgets.QLabel()
        self.gradeLabel.setText(f'{self.grade_type} not set')
        self.gradeLabel.setAlignment(QtCore.Qt.AlignHCenter)

        self.addGradeSpinBox = QtWidgets.QDoubleSpinBox()
        self.addGradeSpinBox.setMaximum(9999.99)
        self.addGradeButton = QtWidgets.QPushButton()
        self.addGradeButton.setText('Add Grade')
        self.addGradeButton.clicked.connect(lambda: self.add_grade(self.addGradeSpinBox.value()))

        self.averageGradeSpinBox = QtWidgets.QDoubleSpinBox()
        self.averageGradeSpinBox.setMaximum(9999.99)

        self.averageGradeButton = QtWidgets.QPushButton()
        self.averageGradeButton.setText('Set Average Grade')
        self.averageGradeButton.clicked.connect(self.average_grade)

        self.clearGradeButton = QtWidgets.QPushButton()
        self.clearGradeButton.setText('Clear Grades')
        self.clearGradeButton.clicked.connect(self.clear_grades)

        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollAreaGroupBox = QtWidgets.QGroupBox()
        self.scrollAreaGroupBoxLayout = QtWidgets.QGridLayout()
        self.scrollAreaGroupBox.setLayout(self.scrollAreaGroupBoxLayout)

        self.scrollArea.setWidget(self.scrollAreaGroupBox)
        self.scrollArea.setWidgetResizable(True)

        self.spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        # Add Widgets
        self.gridLayout.addWidget(self.addGradeSpinBox, 1, 0)
        self.gridLayout.addItem(self.spacerItem, 2, 0)
        self.gridLayout.addItem(self.spacerItem1, 3, 0)
        self.gridLayout.addWidget(self.averageGradeSpinBox, 5, 0)
        self.gridLayout.addWidget(self.averageGradeButton, 4, 0)
        self.gridLayout.addWidget(self.scrollArea, 0, 2, 8, 1)
        self.gridLayout.addWidget(self.addGradeButton, 0, 0)
        self.gridLayout.addItem(self.spacerItem3, 6, 0)
        self.gridLayout.addWidget(self.clearGradeButton, 7, 0)
        self.gridLayout.addWidget(self.gradeLabel, 8, 0, 1, 3)
        self.scrollAreaGroupBoxLayout.addItem(self.spacerItem2, 0, 0)
        self.setLayout(self.gridLayout)

        # Stylesheets
        self.addGradeButton.setStyleSheet(f'''
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
        ''')

        self.averageGradeButton.setStyleSheet(f'''
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
        ''')

        self.clearGradeButton.setStyleSheet(f'''
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
        ''')

        self.addGradeSpinBox.setStyleSheet(f'''
        QDoubleSpinBox{{
        border: 10px solid {color2};
        background-color: {color2};
        color: {dark_font_color};
        font-size: 15px;
        }}

        QDoubleSpinBox::up-button{{
        border none;
        background-color: {color2};
        }}
        
        QDoubleSpinBox::down-button{{
        border: none;
        background-color: {color2};
        }}
        ''')

        self.averageGradeSpinBox.setStyleSheet(f'''
        QDoubleSpinBox{{
        border: 10px solid {color2};
        background-color: {color2};
        color: {dark_font_color};
        font-size: 15px;

        }}

        QDoubleSpinBox::up-button{{
        border none;
        background-color: {color2};
        }}

        QDoubleSpinBox::down-button{{
        border: none;
        background-color: {color2}

        }}
        ''')

        self.scrollArea.setStyleSheet(f'''
        *{{
        background-color: {color2};
        border: 5px solid {color2};
        }}
        
        QScrollBar:vertical {{
        background: {color3}; 
        }}

        QScrollBar::handle:vertical{{
        background-color: {color4};
        padding: 10px;
        border-radius: 8px
        }}

        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
        background: none;
        }}

        QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {{
        border-color: {color4};
        background-color: {color4};
        }}

        QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {{
        border: 2px solid grey;
        width: 3px;
        height: 3px;
        background: white;
        }}

        
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
        height: 0px;
        }}



        
        ''')

        self.gradeLabel.setStyleSheet(f'''
        background-color: {color4};
        width: 256px;
        height: 64px;
        padding: 20px;
        font-size: 20px;
        color: {font_color};
        
        ''')

        self.button_style = f'''QPushButton:!hover{{
        background-color: {color5};
        width: 256px;
        height: 32px;
        font-size: 15px;
        color: {dark_font_color}
        }}

        QPushButton:hover{{
        background-color: {color4};
        width: 256px;
        height: 32px;
        font-size: 15px;
        color: {font_color}
        }}'''

        self.setStyleSheet(f'''
       *{{
        font: Segoe UI
        }}''')

    def add_grade(self, value, number=0):
        i = 0
        while True:
            if f'gradeButton{i}' not in self.grades:
                self.grades[f'gradeButton{i}'] = QtWidgets.QPushButton()
                self.grades[f'gradeButton{i}'].setText(str(value))
                self.grades[f'gradeButton{i}'].clicked.connect(lambda: self.clicked_grade(i))
                self.grades[f'gradeButton{i}'].setStyleSheet(self.button_style)

                if number == 0:
                    self.update_grades()
                break
            i += 1

    def update_grades(self):
        for grade, i in zip(self.grades, range(len(self.grades))):
            self.scrollAreaGroupBoxLayout.addWidget(self.grades[grade], i + 1, 0)

        if len(self.grades) != 0:
            self.average = 0
            for grade in self.grades:
                self.average += float(self.grades[grade].text())

            self.average /= len(self.grades)
            self.average = round(self.average, 2)
        else:
            self.average = 'succ'

        if len(self.grades) > self.max_grades:
            self.max_grades = len(self.grades)

        if self.average != 'succ':
            self.averageGradeSpinBox.setValue(self.average)
            self.gradeLabel.setText(f'Your average grade in {self.grade_type} is {self.average}')
        else:
            self.averageGradeSpinBox.setValue(0)
            self.gradeLabel.setText(f'{self.grade_type} not set')

    def clicked_grade(self, i):
        if f'gradeButton{i}' in self.grades:
            self.scrollAreaGroupBoxLayout.removeWidget(self.grades[f'gradeButton{i}'])
            self.grades[f'gradeButton{i}'].deleteLater()
            del self.grades[f'gradeButton{i}']
            self.update_grades()

    def clear_grades(self, number=0):
        for i in range(self.max_grades):
            if f'gradeButton{i}' in self.grades:
                self.scrollAreaGroupBoxLayout.removeWidget(self.grades[f'gradeButton{i}'])
                self.grades[f'gradeButton{i}'].deleteLater()
                del self.grades[f'gradeButton{i}']
        if number == 0:
            self.update_grades()

            self.averageGradeSpinBox.setValue(0)
            self.addGradeSpinBox.setValue(0)

    def average_grade(self):
        self.clear_grades(-1)
        self.add_grade(self.averageGradeSpinBox.value(), -1)
        self.update_grades()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Tab1()
    ui.show()
    sys.exit(app.exec_())
