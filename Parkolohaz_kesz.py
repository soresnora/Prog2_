from PyQt5 import QtCore, QtGui, QtWidgets
import Class as cl

class Ui_Belepteto_rendszer(object):
    adatok=[]
    abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
    szam = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def setupUi(self, Belepteto_rendszer):
        Belepteto_rendszer.setObjectName("Belepteto_rendszer")
        Belepteto_rendszer.resize(482, 600)
        self.centralwidget = QtWidgets.QWidget(Belepteto_rendszer)
        self.centralwidget.setObjectName("centralwidget")
        self.marka = QtWidgets.QLineEdit(self.centralwidget)
        self.marka.setGeometry(QtCore.QRect(150, 20, 251, 31))
        self.marka.setObjectName("marka")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 91, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 91, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 91, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 60, 91, 31))
        self.label_5.setObjectName("label_5")
        self.engedelyezve = QtWidgets.QCheckBox(self.centralwidget)
        self.engedelyezve.setGeometry(QtCore.QRect(150, 230, 125, 51))
        self.engedelyezve.setObjectName("engedelyezve")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 240, 91, 31))
        self.label_6.setObjectName("label_6")
        self.szin = QtWidgets.QLineEdit(self.centralwidget)
        self.szin.setGeometry(QtCore.QRect(150, 150, 251, 31))
        self.szin.setObjectName("szin")
        self.rendszam = QtWidgets.QLineEdit(self.centralwidget)
        self.rendszam.setGeometry(QtCore.QRect(150, 190, 251, 31))
        self.rendszam.setObjectName("rendszam")
        self.tipus = QtWidgets.QLineEdit(self.centralwidget)
        self.tipus.setGeometry(QtCore.QRect(150, 60, 251, 31))
        self.tipus.setObjectName("tipus")
        self.uzemanyag = QtWidgets.QComboBox(self.centralwidget)
        self.uzemanyag.setGeometry(QtCore.QRect(150, 100, 251, 31))
        self.uzemanyag.setObjectName("uzemanyag")
        self.uzemanyag.addItem("")
        self.uzemanyag.addItem("")
        self.uzemanyag.addItem("")
        self.uzemanyag.addItem("")
        self.felvesz = QtWidgets.QPushButton(self.centralwidget)
        self.felvesz.setGeometry(QtCore.QRect(30, 300, 93, 28))
        self.felvesz.setObjectName("felvesz")
        self.modosit = QtWidgets.QPushButton(self.centralwidget)
        self.modosit.setGeometry(QtCore.QRect(250, 300, 93, 28))
        self.modosit.setObjectName("modosit")
        self.torol = QtWidgets.QPushButton(self.centralwidget)
        self.torol.setGeometry(QtCore.QRect(360, 300, 93, 28))
        self.torol.setObjectName("torol")
        self.torol_2 = QtWidgets.QPushButton(self.centralwidget)
        self.torol_2.setGeometry(QtCore.QRect(140, 300, 93, 28))
        self.torol_2.setObjectName("torol_2")
        self.kijelzo = QtWidgets.QListWidget(self.centralwidget)
        self.kijelzo.setEnabled(True)
        self.kijelzo.setGeometry(QtCore.QRect(10, 340, 461, 201))
        self.kijelzo.setObjectName("kijelzo")
        Belepteto_rendszer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Belepteto_rendszer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 482, 26))
        self.menubar.setObjectName("menubar")
        Belepteto_rendszer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Belepteto_rendszer)
        self.statusbar.setObjectName("statusbar")
        Belepteto_rendszer.setStatusBar(self.statusbar)


        self.retranslateUi(Belepteto_rendszer)
        QtCore.QMetaObject.connectSlotsByName(Belepteto_rendszer)

        self.felvesz.clicked.connect(self.felveszfv)
        self.torol_2.clicked.connect(self.szerkesztfv)
        self.torol.clicked.connect(self.torolfv)
        self.modosit.clicked.connect(self.modositfv)

    def retranslateUi(self, Belepteto_rendszer):
        _translate = QtCore.QCoreApplication.translate
        Belepteto_rendszer.setWindowTitle(_translate("Belepteto_rendszer", "Belepteto_rendszer"))
        self.label.setText(_translate("Belepteto_rendszer", "Márka:"))
        self.label_2.setText(_translate("Belepteto_rendszer", "Üzemanyag:"))
        self.label_3.setText(_translate("Belepteto_rendszer", "Rendszám:"))
        self.label_4.setText(_translate("Belepteto_rendszer", "Szín:"))
        self.label_5.setText(_translate("Belepteto_rendszer", "Típus:"))
        self.engedelyezve.setText(_translate("Belepteto_rendszer", "Engedélyezve"))
        self.label_6.setText(_translate("Belepteto_rendszer", "Engedély:"))
        self.uzemanyag.setItemText(0, _translate("Belepteto_rendszer", "Benzin"))
        self.uzemanyag.setItemText(1, _translate("Belepteto_rendszer", "Diesel"))
        self.uzemanyag.setItemText(2, _translate("Belepteto_rendszer", "Elektromos"))
        self.uzemanyag.setItemText(3, _translate("Belepteto_rendszer", "LPG"))
        self.felvesz.setText(_translate("Belepteto_rendszer", "Felvesz"))
        self.modosit.setText(_translate("Belepteto_rendszer", "Modosít"))
        self.torol.setText(_translate("Belepteto_rendszer", "Töröl"))
        self.torol_2.setText(_translate("Belepteto_rendszer", "Szerkeszt"))
        self.rendszam.setText(_translate("Belepteto_rendszer","ABC123"))
        self.beolvas()


    def felveszfv(self):
        try:
            marka=self.marka.text()
            tipus=self.tipus.text()
            uzemanyag=self.uzemanyag.currentText()
            szin=self.szin.text()
            rendszam=self.rendszam.text()
            engedelyezve=self.engedelyezve.isChecked()

            if len(marka)==0:
                raise cl.HianyzoAdat('márka')
            if len(tipus)==0:
                raise cl.HianyzoAdat('típus')
            if len(szin)==0:
                raise cl.HianyzoAdat('szín')
            if len(rendszam)==0:
                raise cl.HianyzoAdat('rendszám')
            if rendszam == 'ABC123':
                raise cl.RendszamHiba()
            if len(rendszam)!=6:
                raise cl.RendszamFormatumHiba()
            if rendszam[0:1] not in self.abc:
                raise cl.RendszamFormatumHiba()
            if rendszam[1:2] not in self.abc:
                raise cl.RendszamFormatumHiba()
            if rendszam[2:3] not in self.abc:
                raise cl.RendszamFormatumHiba()
            if rendszam[3:4] not in self.szam:
                raise cl.RendszamFormatumHiba()
            if rendszam[4:5] not in self.szam:
                raise cl.RendszamFormatumHiba()
            if rendszam[5:6] not in self.szam:
                raise cl.RendszamFormatumHiba()


            uj_auto=cl.Auto(marka,tipus,uzemanyag,szin,rendszam,engedelyezve)
            if uj_auto not in self.adatok:
                self.adatok.append(uj_auto)
                self.adatok.sort()
                self.mentes()
                self.kijelzo.clear()

                for i in self.adatok:
                    self.kijelzo.addItem(i.__str__())
                    if not i.getEngedely():
                        self.kijelzo.item(self.kijelzo.count() - 1).setBackground(QtCore.Qt.red)
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Figyelmeztetés!')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText('Ez az autó már szerepel a listában!')
                msg.exec()


        except cl.HianyzoAdat as ha:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Figyelmeztetés')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText(ha.__str__())
            msg.exec()


        except cl.RendszamHiba:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Figyelmeztetés')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Az alapértelmezett rendszámot írja át!")
            msg.exec()


        except cl.RendszamFormatumHiba:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Figyelmeztetés')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("A rendszámot a mintaformátumnak megfelelően adja meg!  (pl: ABC123)")
            msg.exec()


    def szerkesztfv(self,adat):
        if not self.kijelzo.currentItem():
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Figyelmeztetés")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Ki kell választanod egy autót a listából!")
            msg.exec()
        else:
            adat=self.kijelzo.currentItem()
            tmp = adat.text()
            tmp = tmp.split(' ')
            rendsz = tmp[1]
            for i in self.adatok:
                if rendsz == i.getRendszam():
                    self.marka.setText(i.getMarka())
                    self.tipus.setText(i.getTipus())
                    self.uzemanyag.setCurrentText(i.getUzemanyag())
                    self.szin.setText(i.getSzin())
                    self.rendszam.setText(i.getRendszam())
                    self.engedelyezve.setChecked(i.getEngedely())
                    self.rendszam.setReadOnly(True)


    def torolfv(self):
        if not self.kijelzo.currentItem():
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Figyelmeztetés")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Ki kell választanod egy autót a listából!")
            msg.exec()
        else:
            adat=self.kijelzo.currentItem()
            tmp = adat.text()
            tmp = tmp.split(' ')
            rendsz = tmp[1]
            for i in self.adatok:
                if rendsz == i.getRendszam():
                    self.adatok.remove(i)
                    self.mentes()
                    self.kijelzo.clear()

                    for j in self.adatok:
                        self.kijelzo.addItem(j.__str__())
                        if not j.getEngedely():
                            self.kijelzo.item(self.kijelzo.count() - 1).setBackground(QtCore.Qt.red)



    def modositfv(self):
        marka = self.marka.text()
        tipus = self.tipus.text()
        uzemanyag = self.uzemanyag.currentText()
        szin = self.szin.text()
        rendszam = self.rendszam.text()
        engedelyezve = self.engedelyezve.isChecked()

        for i in self.adatok:
            if i.getRendszam()==rendszam:
                i.setMarka(marka)
                i.setTipus(tipus)
                i.setUzemanyag(uzemanyag)
                i.setSzin(szin)
                i.setRendszam(rendszam)
                i.setEngedely(engedelyezve)
                self.mentes()
                self.kijelzo.clear()

                for j in self.adatok:
                    self.kijelzo.addItem(j.__str__())
                    if not j.getEngedely():
                        self.kijelzo.item(self.kijelzo.count() - 1).setBackground(QtCore.Qt.red)


    def mentes(self):
        adatb = open("adatbazis.txt","w")
        for i in self.adatok:
            print('{};{};{};{};{};{}\n'.format(i.getMarka(),i.getTipus(),i.getUzemanyag(),i.getSzin(),i.getRendszam(),i.getEngedely()),file=adatb)
        adatb.close()

    def beolvas(self):
        try:
            adatb = open('adatbazis.txt', 'r')
            for i in adatb:
                if i.count(';') == 5:
                    tmp = i.split(';')
                    self.adatok.append(cl.Auto(tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], tmp[5][:-1]=='True'))
            adatb.close()
            for j in self.adatok:
                self.kijelzo.addItem(j.__str__())
                if not j.getEngedely():
                    self.kijelzo.item(self.kijelzo.count() - 1).setBackground(QtCore.Qt.red)
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Belepteto_rendszer = QtWidgets.QMainWindow()
    ui = Ui_Belepteto_rendszer()
    ui.setupUi(Belepteto_rendszer)
    Belepteto_rendszer.show()
    sys.exit(app.exec_())
