# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Admin\Desktop\GUI\afm_processor\afm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import matplotlib
import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt,exp
from copy import copy
from PIL import Image
from PIL import ImageFilter
from PyQt5 import QtCore, QtGui, QtWidgets
from skimage.filters import median
from skimage.io import imread, imsave
from skimage.morphology import disk
import skimage.metrics
from skimage import  img_as_ubyte, img_as_float
image_path = "C:\\Users\\Admin\\Desktop\\GUI\\afm_processor\\images\\"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        '''Define path and names for color/grayscale original/preproceed image for convinient use'''
        self.fileName = None
        self.image = None
        self.color_image = None
        self.imname = None

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 779)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.SearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton.setGeometry(QtCore.QRect(10, 10, 91, 21))
        self.SearchButton.setObjectName("Search")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 60, 141, 271))
        self.groupBox.setObjectName("groupBox")

        self.FreqFiltrationButton = QtWidgets.QPushButton(self.groupBox)
        self.FreqFiltrationButton.setGeometry(QtCore.QRect(0, 10, 141, 61))
        self.FreqFiltrationButton.setObjectName("FreqFiltrationButton")

        self.MedianBlurButton = QtWidgets.QPushButton(self.groupBox)
        self.MedianBlurButton.setGeometry(QtCore.QRect(0, 70, 141, 51))
        self.MedianBlurButton.setObjectName("MedianBlurButton")

        self.ImageLevelingButton = QtWidgets.QPushButton(self.groupBox)
        self.ImageLevelingButton.setGeometry(QtCore.QRect(0, 120, 141, 51))
        self.ImageLevelingButton.setObjectName("ImageLevelingButton")

        self.LightSourseButton = QtWidgets.QPushButton(self.groupBox)
        self.LightSourseButton.setGeometry(QtCore.QRect(0, 170, 141, 51))
        self.LightSourseButton.setObjectName("LightSourseButton")

        self.AddSharpnessButton = QtWidgets.QPushButton(self.groupBox)
        self.AddSharpnessButton.setGeometry(QtCore.QRect(0, 220, 141, 51))
        self.AddSharpnessButton.setObjectName("AddSharpnessButton")

        self.labelOriginal = QtWidgets.QLabel(self.centralwidget)
        self.labelOriginal.setGeometry(QtCore.QRect(200, 80, 431, 351))
        self.labelOriginal.setFrameShape(QtWidgets.QFrame.Box)
        self.labelOriginal.setText("")
        self.labelOriginal.setObjectName("labelOriginal")

        self.labelProcessed = QtWidgets.QLabel(self.centralwidget)
        self.labelProcessed.setGeometry(QtCore.QRect(650, 80,  431, 351))
        self.labelProcessed.setFrameShape(QtWidgets.QFrame.Box)
        self.labelProcessed.setText("")
        self.labelProcessed.setObjectName("labelProcessed")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(410, 510, 681, 211))
        self.listWidget.setObjectName("listWidget")

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 460, 141, 271))
        self.groupBox_2.setObjectName("groupBox_2")

        self.PsnrButton = QtWidgets.QPushButton(self.groupBox_2)
        self.PsnrButton.setGeometry(QtCore.QRect(0, 10, 141, 61))
        self.PsnrButton.setObjectName("PsnrButton")

        self.MinkovskyButton = QtWidgets.QPushButton(self.groupBox_2)
        self.MinkovskyButton.setGeometry(QtCore.QRect(0, 70, 141, 51))
        self.MinkovskyButton.setObjectName("MinkovskyButton")

        self.SSIMbutton = QtWidgets.QPushButton(self.groupBox_2)
        self.SSIMbutton.setGeometry(QtCore.QRect(0, 120, 141, 51))
        self.SSIMbutton.setObjectName("SSIMbutton")

        self.MeanDiffButton = QtWidgets.QPushButton(self.groupBox_2)
        self.MeanDiffButton.setGeometry(QtCore.QRect(0, 170, 141, 51))
        self.MeanDiffButton.setObjectName("MeanDiffButton")

        self.MaximumDiffButton = QtWidgets.QPushButton(self.groupBox_2)
        self.MaximumDiffButton.setGeometry(QtCore.QRect(0, 220, 141, 51))
        self.MaximumDiffButton.setObjectName("MaximumDiffButton")

        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(190, 460, 141, 171))
        self.groupBox_3.setObjectName("groupBox_3")

        self.SharpnessButton = QtWidgets.QPushButton(self.groupBox_3)
        self.SharpnessButton.setGeometry(QtCore.QRect(0, 10, 141, 61))
        self.SharpnessButton.setObjectName("SharpnessButton")

        self.ContrastButton = QtWidgets.QPushButton(self.groupBox_3)
        self.ContrastButton.setGeometry(QtCore.QRect(0, 70, 141, 51))
        self.ContrastButton.setObjectName("ContrastButton")

        self.LightSharpnessButton = QtWidgets.QPushButton(self.groupBox_3)
        self.LightSharpnessButton.setGeometry(QtCore.QRect(0, 120, 141, 51))
        self.LightSharpnessButton.setObjectName("LightSharpnessButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.SearchButton.clicked.connect(self.setImage)
        self.MedianBlurButton.clicked.connect(self.median_blur)
        self.LightSourseButton.clicked.connect(self.add_light_sourse)
        self.FreqFiltrationButton.clicked.connect(self.use_Furier)
        self.ImageLevelingButton.clicked.connect(self.plot_substraction)
        self.AddSharpnessButton.clicked.connect(self.add_sharpness)
        self.SSIMbutton.clicked.connect(self.SSIM_evaluation)
        self.PsnrButton.clicked.connect(self.PSNR_evaluation)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SearchButton.setText(_translate("MainWindow", "Поиск "))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.FreqFiltrationButton.setText(_translate("MainWindow", "Частотная фильтрация "))
        self.MedianBlurButton.setText(_translate("MainWindow", "Медианная фильтрация"))
        self.ImageLevelingButton.setText(_translate("MainWindow", "Вычитание подложки"))
        self.LightSourseButton.setText(_translate("MainWindow", "Подсветка"))
        self.AddSharpnessButton.setText(_translate("MainWindow", "Увеличение резкости"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Эталонная оценка"))
        self.PsnrButton.setText(_translate("MainWindow", "ПОСШ"))
        self.MinkovskyButton.setText(_translate("MainWindow", "Норма Минковского"))
        self.SSIMbutton.setText(_translate("MainWindow", "SSIM"))
        self.MeanDiffButton.setText(_translate("MainWindow", "Средняя разность"))
        self.MaximumDiffButton.setText(_translate("MainWindow", "Максимальная разность"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Безэталонная оценка"))
        self.SharpnessButton.setText(_translate("MainWindow", "Оценка резкости"))
        self.ContrastButton.setText(_translate("MainWindow", "Оценка контраста "))
        self.LightSharpnessButton.setText(_translate("MainWindow", "Оценка яркости и резкости"))

    def setImage(self,):
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp)")
        print(self.fileName)
        if self.fileName: 
            pixmap = QtGui.QPixmap(self.fileName)
            pixmap = pixmap.scaled(self.labelOriginal.width(), self.labelOriginal.height(), QtCore.Qt.KeepAspectRatio,QtCore.Qt.FastTransformation)
            self.labelOriginal.setPixmap(pixmap)
            self.labelOriginal.setAlignment(QtCore.Qt.AlignCenter)
            self.image = copy(imread(self.fileName,as_gray=True))
            self.color_image = copy(cv2.imread(self.fileName,0))

    def median_blur(self,):
        blur_img = median(self.image,disk(5))
        imname = 'median.png'
        imsave(f'{image_path}{imname}',blur_img)
        self.show_image(imname)
    
    def add_light_sourse(self,):
        new_image = self.light_sourse(self.image)
        self.imname = 'light.png'
        imsave(f'{image_path}{self.imname}',new_image)
        self.show_image(self.imname)
    
    def light_sourse(self, image, cmap='gray', ve=10,):
        ls = matplotlib.colors.LightSource(azdeg=350, altdeg=30)
        return ls.hillshade(image, vert_exag=ve)

    def show_image(self,image_name,):
        image = image_path + image_name
        pixmap = QtGui.QPixmap(image)
        pixmap = pixmap.scaled(self.labelProcessed.width(), self.labelProcessed.height(), QtCore.Qt.KeepAspectRatio,QtCore.Qt.FastTransformation)
        self.labelProcessed.setPixmap(pixmap)
        self.labelProcessed.setAlignment(QtCore.Qt.AlignCenter)

    def distance(self,point1,point2,):
        return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

    def Fourier_filterLP(self,D0,imgShape):
        base = np.zeros(imgShape[:2])
        rows, cols = imgShape[:2]
        center = (rows/2,cols/2)
        for x in range(cols):
            for y in range(rows):
                if self.distance((y,x),center) < D0:
                    base[y,x] = 1
        return base
    
    def use_Furier(self,):
        spectrum = np.fft.fft2(self.image)
        shape = self.image.shape
        centralized_spectrum = np.fft.fftshift(spectrum)
        low_pass_center = centralized_spectrum * self.Fourier_filterLP(80,shape)
        low_pass = np.fft.ifftshift(low_pass_center)
        filtered_image = np.fft.ifft2(low_pass)
        self.imname = 'fft_filter.png'
        plt.imsave(f'{image_path}{self.imname}',np.abs(filtered_image),cmap='gray')
        self.show_image(self.imname)

    def plot_substraction(self,):
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(4,4))
        cl1 = clahe.apply(self.color_image)
        self.imname = 'plot_sbstr.png'
        plt.imsave(f'{image_path}{self.imname}',cl1,cmap='gray')
        self.show_image(self.imname)

    def add_sharpness(self,):
        image = Image.fromarray(self.color_image.astype('uint8'))
        new_image = image.filter(ImageFilter.UnsharpMask(radius=2, percent=100))
        f_image = img_as_float(new_image)
        self.imname = 'sharpness.png'
        imsave(f'{image_path}{self.imname}',f_image)
        self.show_image(self.imname)

    def SSIM_evaluation(self,):
        origin_img = cv2.imread(self.fileName,0)
        proceed_img = cv2.imread(f"{image_path}{self.imname}",0)
        answer = skimage.metrics.structural_similarity(origin_img,proceed_img)
        self.listWidget.addItem(f"Значение метода структурного подобия равно {answer}")

    def PSNR_evaluation(self,):
        origin_img = cv2.imread(self.fileName,0)
        proceed_img = cv2.imread(f"{image_path}{self.imname}",0)
        answer = skimage.metrics.peak_signal_noise_ratio(origin_img,proceed_img)
        self.listWidget.addItem(f"Отношение сигнал-шум равно  {answer}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
