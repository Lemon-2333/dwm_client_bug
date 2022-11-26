from PyQt5 import QtCore, QtGui, QtWidgets
import item, main_ui  # ui文件
import sys, time


class Windows(QtWidgets.QMainWindow, main_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.testButton.clicked.connect(self.add)
        self.listWidget.verticalScrollBar().valueChanged.connect(self.up)

    def add(self):
        test = add_widget()
        a = QtWidgets.QListWidgetItem()
        a.setSizeHint(QtCore.QSize(350, 510))
        self.listWidget.addItem(a)
        self.listWidget.setItemWidget(a, test)
    def up(self ):
        print(self.listWidget.verticalScrollBar().value())
        if self.listWidget.verticalScrollBar().value() >= self.listWidget.verticalScrollBar().maximum() :
            self.add()


class add_widget(QtWidgets.QWidget, item.Ui_Form):
    def __init__(self):
        super(add_widget, self).__init__()
        self.setupUi(self)
        self.show()

    def up(self, i):
        pass

def main():
    windows.show()
    pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    windows = Windows()
    main()
    sys.exit(app.exec_())
