# Form implementation generated from reading ui file 'InHoaDon.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import Dataconnection
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from XuatBaoCao import Print_File

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_InHoaDon(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(593, 774)
        self.frame = QtWidgets.QFrame(parent=Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 591, 41))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.btnPrint = QtWidgets.QPushButton(parent=self.frame)
        self.btnPrint.setGeometry(QtCore.QRect(370, 10, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnPrint.setFont(font)
        self.btnPrint.setObjectName("btnPrint")
        self.btnPrint.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnExit = QtWidgets.QPushButton(parent=self.frame)
        self.btnExit.setGeometry(QtCore.QRect(470, 10, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnExit.setFont(font)
        self.btnExit.setObjectName("btnExit")
        self.btnExit.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnTimKiem = QtWidgets.QPushButton(parent=self.frame)
        self.btnTimKiem.setGeometry(QtCore.QRect(260, 10, 91, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnTimKiem.setFont(font)
        self.btnTimKiem.setObjectName("btnTimKiem")
        self.btnTimKiem.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.txtMaHoaDon = QtWidgets.QTextEdit(parent=self.frame)
        self.txtMaHoaDon.setGeometry(QtCore.QRect(120, 10, 104, 21))
        self.txtMaHoaDon.setObjectName("txtMaHoaDon")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(parent=Dialog)
        self.frame_2.setGeometry(QtCore.QRect(30, 80, 531, 601))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(180, 30, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tableViewHoaDonThanhToan = QtWidgets.QTableView(parent=self.frame_2)
        self.tableViewHoaDonThanhToan.setGeometry(QtCore.QRect(20, 100, 491, 211))
        self.tableViewHoaDonThanhToan.setObjectName("tableViewHoaDonThanhToan")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(70, 360, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txtTien = QtWidgets.QLabel(parent=self.frame_2)
        self.txtTien.setGeometry(QtCore.QRect(230, 360, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.txtTien.setFont(font)
        self.txtTien.setObjectName("txtTien")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(360, 360, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(50, 470, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(350, 470, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(270, 430, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        # 
        self.btnExit.clicked.connect(Dialog.close)
        self.btnTimKiem.clicked.connect(self.searchChiTietHoaDon)
        self.btnPrint.clicked.connect(lambda:Print_File(self.tableViewHoaDonThanhToan,self.txtTien, [self.label_6,self.label_7,self.label_8]))
        self.ChiTiet_table()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "In Hóa Đơn"))
        self.btnPrint.setText(_translate("Dialog", "PRINT"))
        self.btnExit.setText(_translate("Dialog", "EXIT"))
        self.btnTimKiem.setText(_translate("Dialog", "Tìm Hóa Đơn"))
        self.label.setText(_translate("Dialog", "Mã Hóa Đơn"))
        self.label_2.setText(_translate("Dialog", "HÓA ĐƠN THANH TOÁN"))
        self.label_3.setText(_translate("Dialog", "Thành Tiền"))
        self.txtTien.setText(_translate("Dialog", "0.0"))
        self.label_5.setText(_translate("Dialog", "$"))
        self.label_6.setText(_translate("Dialog", "Khách Hàng"))
        self.label_7.setText(_translate("Dialog", "Người Bán Hàng"))
        self.label_8.setText(_translate("Dialog", "Hà Nội ....Ngày ...Tháng  ...Năm 2024"))
    
    def ChiTiet_table(self):
        self.ChiTiet = QStandardItemModel()
        self.tableViewHoaDonThanhToan.setModel(self.ChiTiet)
        
        header = self.tableViewHoaDonThanhToan.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

    
    def searchChiTietHoaDon(self):
        # Get the MaSP from the search text box
        ma_hd = self.txtMaHoaDon.toPlainText().strip()
        connection = Dataconnection.connectdatabase()
        if connection:
            cursor = connection.cursor()
            # ........
            query = "SELECT TenSP,SoLuong,GiaBan  FROM ChiTietHoaDon WHERE MaHD = %s"
            cursor.execute(query, (ma_hd,))
            results = cursor.fetchall()
            # ........
            query_total = "SELECT TongTien FROM HoaDon WHERE MaHD = %s"
            cursor.execute(query_total, (ma_hd,))
            result_total = cursor.fetchone()
            cursor.close()
            connection.close()

            # Update the model with the results
            self.ChiTiet.clear()
            if results:  
                headers = [  'TenSP', 'SoLuong', 'GiaBan']   
                self.ChiTiet.setHorizontalHeaderLabels(headers)
                
                for row in results:
                    items = [QtGui.QStandardItem(str(field)) for field in row]
                    self.ChiTiet.appendRow(items)
            else:
                self.ChiTiet.setHorizontalHeaderLabels(['Không có mã sản phẩm nào >'])
            
            self.resizeColumns()

            # Show tổng tiền 
            if result_total:
                self.txtTien.setText(str(result_total[0]))
            else:
                self.txtTien.setText("0.0")

    def resizeColumns(self):
        self.tableViewHoaDonThanhToan.resizeColumnsToContents()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_InHoaDon()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
