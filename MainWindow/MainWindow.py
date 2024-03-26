from PySide6.QtWidgets import QWidget,QMainWindow,QMessageBox,QFileDialog,QAbstractItemView
from .MainWindow_ui import Ui_MainWindow
from exif import Image

class MyWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        ui=Ui_MainWindow()
        ui.setupUi(self)

        # 槽函数

        # 导入图片
        def MesClick():
            paths = QFileDialog.getOpenFileNames(QMainWindow(), "选择文件", "./", "Image files (*.png *.jpg *.rw2)")[0]
            if len(paths) >= 20:
                QMessageBox.critical(self, "错误", "最大数量不得超过20！")
            else:
                ui.imageList.addItems(paths)
                ui.imageList.setSelectionMode(QAbstractItemView.ExtendedSelection)

        # 显示exif
        def ShowExif():
            f=open(ui.imageList.currentItem().text(),'rb')
            tags= Image(f)
            f.close()
            ui.exifList.clear()
            ui.exifList.addItem("厂商："+tags.Make)
            ui.exifList.addItem("型号："+tags.Model)
            ui.exifList.addItem("镜头："+tags.get("lens_model"))
            ui.exifList.addItem("焦距："+str(tags.focal_length)+"mm")
            ui.exifList.addItem("35mm焦距："+str(tags.focal_length_in_35mm_film)+"mm")
            ui.exifList.addItem("闪光灯："+str(tags.flash.flash_fired))


        # 信号处理
        ui.pushButton.clicked.connect(MesClick)
        ui.imageList.clicked.connect(ShowExif)