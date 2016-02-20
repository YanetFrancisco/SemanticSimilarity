import text_processing
import metrics


from PyQt4 import QtCore, QtGui


class TabDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(TabDialog, self).__init__(parent)

        tabWidget = QtGui.QTabWidget()
        gt = GeneralTab()
        tabWidget.addTab(gt, "General")
        pt = PermissionsTab()
        tabWidget.addTab(pt, "Distancias")
        at = ApplicationsTab(gt.path_text1, gt.text2, pt.apps)
        tabWidget.addTab(at, "Resultados")

        buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel)

        buttonBox.accepted.connect(at.resultados)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(tabWidget)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Similaridad Textual")


class GeneralTab(QtGui.QWidget):
    def __init__(self, parent=None):
        super(GeneralTab, self).__init__(parent)

        self.path_text1 = []
        self.text2 = []

        fileNameLabel = QtGui.QLabel("Texto 1:")
        self.directoryComboBox = self.createComboBox(QtCore.QDir.currentPath())

        fileNameLabel1 = QtGui.QLabel("Texto 2:")
        self.directoryComboBox1 = self.createComboBox(QtCore.QDir.currentPath())


        browseButton = self.createButton("&Browse...", self.browse)
        browseButton2 = self.createButton("&Browse...", self.browse1)

        # ok = QtGui.QPushButton("OK")
        browseButton.clicked.connect(self.text)
        browseButton2.clicked.connect(self.text)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(fileNameLabel)
        mainLayout.addWidget(self.directoryComboBox)
        mainLayout.addWidget(browseButton)
        mainLayout.addWidget(fileNameLabel1)
        mainLayout.addWidget(self.directoryComboBox1)
        mainLayout.addWidget(browseButton2, 5)
        otherlayout = QtGui.QVBoxLayout()
        # otherlayout.addWidget(ok)
        mainLayout.addLayout(otherlayout, 0)
        mainLayout.addStretch(1)
        self.setLayout(mainLayout)

    def text(self):
        self.path_text1.append(self.directoryComboBox.currentText())
        self.text2.append(self.directoryComboBox1.currentText())

    def createComboBox(self, text=""):
        comboBox = QtGui.QComboBox()
        comboBox.setEditable(True)
        comboBox.addItem(text)
        comboBox.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Preferred)
        return comboBox

    def browse(self):
        directory = QtGui.QFileDialog.getOpenFileName(self, "Find Files",
                QtCore.QDir.currentPath())

        if directory:
            if self.directoryComboBox.findText(directory) == -1:
                self.directoryComboBox.addItem(directory)

            self.directoryComboBox.setCurrentIndex(self.directoryComboBox.findText(directory))

    def browse1(self):
        directory = QtGui.QFileDialog.getOpenFileName(self, "Find Files",
                QtCore.QDir.currentPath())

        if directory:
            if self.directoryComboBox1.findText(directory) == -1:
                self.directoryComboBox1.addItem(directory)

            self.directoryComboBox1.setCurrentIndex(self.directoryComboBox1.findText(directory))

    def createButton(self, text, member):
        button = QtGui.QPushButton(text)
        button.clicked.connect(member)
        return button


class PermissionsTab(QtGui.QWidget):
    def __init__(self, parent=None):
        super(PermissionsTab, self).__init__(parent)

        self.apps = []
        permissionsGroup = QtGui.QGroupBox("Sintacticas")

        binary = QtGui.QCheckBox("Binary")
        binary.toggled.connect(self.check1)
        hamming = QtGui.QCheckBox("Hamming")
        hamming.toggled.connect(self.check2)
        masi = QtGui.QCheckBox("MASI")
        masi.toggled.connect(self.check3)
        jaccard = QtGui.QCheckBox("Jaccard")
        jaccard.toggled.connect(self.check4)
        levenshtein = QtGui.QCheckBox("Levenshtein")
        levenshtein.toggled.connect(self.check5)

        ownerGroup = QtGui.QGroupBox("Semantica")
        wordNet = QtGui.QCheckBox("WordNet")
        wordNet.toggled.connect(self.check6)


        permissionsLayout = QtGui.QVBoxLayout()
        permissionsLayout.addWidget(binary)
        permissionsLayout.addWidget(hamming)
        permissionsLayout.addWidget(masi)
        permissionsLayout.addWidget(jaccard)
        permissionsLayout.addWidget(levenshtein)
        permissionsGroup.setLayout(permissionsLayout)

        ownerLayout = QtGui.QVBoxLayout()
        ownerLayout.addWidget(wordNet)
        ownerGroup.setLayout(ownerLayout)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(permissionsGroup)
        mainLayout.addWidget(ownerGroup)
        mainLayout.addStretch(1)
        self.setLayout(mainLayout)

    def check1(self):
        if not 1 in self.apps:
            self.apps.append(1)
        else:
            self.apps.remove(1)

    def check2(self):
        if not 2 in self.apps:
            self.apps.append(2)
        else:
            self.apps.remove(2)

    def check3(self):
        if not 3 in self.apps:
            self.apps.append(3)
        else:
            self.apps.remove(3)

    def check4(self):
        if not 4 in self.apps:
            self.apps.append(4)
        else:
            self.apps.remove(4)

    def check5(self):
        if not 5 in self.apps:
            self.apps.append(5)
        else:
            self.apps.remove(5)

    def check6(self):
        if not 6 in self.apps:
            self.apps.append(6)
        else:
            self.apps.remove(6)


class ApplicationsTab(QtGui.QWidget):
    def __init__(self, text1, text2, apps, parent=None):
        super(ApplicationsTab, self).__init__(parent)

        self.text1 = text1
        self.text2 = text2
        self.applications = []

        self.apps = apps
        topLabel = QtGui.QLabel("Resultados:")
        # topButton = QtGui.QPushButton('Resultados')
        # topButton.clicked.connect(self.resultados)

        applicationsListBox = QtGui.QListWidget()


        # for i in range(1, 31):
        #     self.applications.append("Application %d" % i)

        applicationsListBox.insertItems(0, self.applications)

        layout = QtGui.QGridLayout()
        layout.addWidget(topLabel, 0, 0)
        # layout.addWidget(topButton, 0, 1)
        layout.addWidget(applicationsListBox)
        self.setLayout(layout)

    def resultados(self):
        self.text1 = to_path(self.text1)
        self.text2 = to_path(self.text2)
        print(self.text2)
        print(self.text1)
        for a in self.apps:
            if a == 1:
                self.applications.append('binary_distance: ' + str(text_processing.sintactic_similarity_with_class(self.text1, self.text2, metrics.binary_distance)))
            if a == 2:
                self.applications.append('hamming_distance: ' + str(text_processing.sintactic_similarity_with_class(self.text1, self.text2, metrics.hamming_distance)))
            if a == 3:
                self.applications.append('masi_distance: ' + str(text_processing.sintactic_similarity(self.text1, self.text2, metrics.masi_distance)))
            if a == 4:
                self.applications.append('jaccard_distance: ' + str(text_processing.sintactic_similarity_with_class(self.text1, self.text2, metrics.jaccard_distance)))
            if a == 5:
                self.applications.append('levenshtein_distance: ' + str(text_processing.sintactic_similarity_with_class(self.text1, self.text2, metrics.levenshtein_distance)))
            if a == 6:
                self.applications.append('wordnet_distance: ' + str(text_processing.semantic_similarity(self.text1, self.text2)))


def to_path(path):
    new_path = ''
    for p in path[-1]:
        if p == "/":
            new_path += '\\'
        else:
            new_path += p
    return new_path

if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)

    tabdialog = TabDialog()
    sys.exit(tabdialog.exec_())
