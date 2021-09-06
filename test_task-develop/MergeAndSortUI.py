import sys
import pandas as pd
from PyQt5.QtWidgets import *


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Объединение и сортировка")
        self.setGeometry(50,50,450,650)
        self.setStyleSheet("QWidget{"
"background-color: rgb(65, 102, 245);\n" "}")
        self.UI()


    def UI(self):
        self.Address1 = QLineEdit(self)
        self.Address1.setGeometry(50,50, 350, 40)
        self.Address1.setStyleSheet("QWidget{"
"background-color: rgb(255, 255, 255);\n" "}")
        self.Address1.setPlaceholderText("Введите адрес первой таблицы Excel")

        self.Address2 = QLineEdit(self)
        self.Address2.setGeometry(50,100, 350 ,40)
        self.Address2.setStyleSheet("QWidget{"
"background-color: rgb(255, 255, 255);\n" "}")
        self.Address2.setPlaceholderText("Введите адрес второй таблицы Excel")

        mergeButton = QPushButton("Объединить и сортировать по дате", self)
        mergeButton.setGeometry(75, 200, 300, 100)
        mergeButton.setStyleSheet("QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(246, 250, 5);\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"font: 100 12pt \"Arial\" ;\n"
"}\n"
"QPushButton:hover{\n"
"color:rgb(0, 0, 05);\n"
"background-color: rgb(245, 169, 17);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"color:rgb(0, 0, 0);\n"
"background-color: rgb(255, 148, 164);\n"
"}")

        mergeButton.clicked.connect(self.mergeAndSort)

        self.columnToRemove = QLineEdit(self)
        self.columnToRemove.setPlaceholderText("Вставьте название колонки для удаления")
        self.columnToRemove.setGeometry(50, 350,350,40)
        self.columnToRemove.setStyleSheet("QWidget{"
                                    "background-color: rgb(255, 255, 255);\n" "}")

        self.columnSortBy = QLineEdit(self)
        self.columnSortBy.setPlaceholderText("Вставьте название колонки для сортировки")
        self.columnSortBy.setGeometry(50, 450,350,40)
        self.columnSortBy.setStyleSheet("QWidget{"
                                    "background-color: rgb(255, 255, 255);\n" "}")

        self.removeCheckBox = QCheckBox("Удалить колонку", self)
        self.removeCheckBox.setGeometry(75, 400, 300, 40)
        self.removeCheckBox.setStyleSheet("QWidget{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(246, 250, 5);\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"font: 100 12pt \"Arial\" ;\n"
"}\n")

        self.sortCheckBox = QCheckBox("Сортировать по колонке", self)
        self.sortCheckBox.move(75, 500)
        self.sortCheckBox.setStyleSheet("QWidget{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(246, 250, 5);\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"font: 100 12pt \"Arial\" ;\n"
"}\n")

        self.rowLimit = QLineEdit(self)
        self.rowLimit.setPlaceholderText("Вставьте ограничение на количество строк")
        self.rowLimit.setGeometry(50, 550, 350, 40)
        self.rowLimit.setStyleSheet("QWidget{"
                                          "background-color: rgb(255, 255, 255);\n" "}")

        limitButton = QPushButton("Ввести лимит", self)
        limitButton.setGeometry(75, 600, 300, 40)
        limitButton.setStyleSheet("QPushButton{\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "background-color: rgb(246, 250, 5);\n"
                                  "border-style:outset;\n"
                                  "border-radius:10px;\n"
                                  "font: 100 12pt \"Arial\" ;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "color:rgb(0, 0, 05);\n"
                                  "background-color: rgb(245, 169, 17);\n"
                                  "border-radius:5px;\n"
                                  "}\n"
                                  "QPushButton:pressed{\n"
                                  "color:rgb(0, 0, 0);\n"
                                  "background-color: rgb(255, 148, 164);\n"
                                  "}")

        limitButton.clicked.connect(self.limit)

        self.show()

    def mergeAndSort(self):
        address1 = self.Address1.text()
        address1 = address1.replace('\\', '/')
        address2 = self.Address2.text()
        address2 = address2.replace('\\', '/')

        df1 = pd.read_excel(address1)
        df2 = pd.read_excel(address2)

        ffj = [df1, df2]
        join = pd.concat(ffj)
        join = join.sort_values(by="Дата")
        join.to_excel("third_table.xlsx", index=False)

    def limit(self):
        pass


def main():
    App = QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()