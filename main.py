from ultralytics import YOLO
from window import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog
from PyQt5.QtMultimedia import QMediaContent
from PyQt5.QtCore import QUrl, QTimer
import cv2
import threading


class Program(QMainWindow):

    def __init__ (self):
        super().__init__()
        self.userInterface = Ui_Dialog()
        self.userInterface.setupUi(self)
        self.setWindowTitle("KUŞ YUVASI BUL")
        self.setFixedSize(1184,601)
        self.setWindowFlag(False)
      
        #self.setWindowIcon()


        self.path = None
        self.filename = None
        self.model_path = "best.pt"
        self.total_frames=1
        self.frame_counter=1
        self.local_flag = False
        self.url_flag = False

        self.conf_val = 50

        self.timer= None
        self.progress_rate=0

        self.Texts = []

        self.buttons = [
            self.userInterface.pushButton,
            self.userInterface.pushButton_2
        ]

        self.graphics = [
            self.userInterface.media_player,
            self.userInterface.video_widget
        ]

        self.labels = [
            self.userInterface.label,
            self.userInterface.label_2
        ]

        self.radio_buttons = [
            self.userInterface.radioButton_1,
            self.userInterface.radioButton_2
        ]

        self.progress = [
            self.userInterface.progess_bar
        ]

        self.sliders = [
            self.userInterface.horizontalSlider
        ]


        self.moves()



    def model_yukle(self):
        
        self.model_path, _ = QFileDialog.getOpenFileName(self, "modl Dosyası Seç", "", "model dosyaları(v8) (*.pt)")

    def slider(self):
        self.labels[0].setText("dogruluk esigi")
        self.sliders[0].setValue(self.conf_val)
        self.labels[1].setText(str(self.conf_val))
        self.sliders[0].setMaximum(100)
        self.sliders[0].setMinimum(0)
        self.sliders[0].actionTriggered.connect(self.slider_update)


    def slider_update(self):

        self.conf_val = self.sliders[0].value()
        self.labels[1].setText(str(self.conf_val))

    def moves(self):
        self.slider()
        self.radio_button_select()
        self.buttons[0].clicked.connect(self.open_media)
        self.buttons[1].clicked.connect(self.model_yukle)
        



    def radio_button_select(self):
        
        if self.radio_buttons[0].isChecked():
            self.local_flag = True
            self.url_flag = False
        
        elif self.radio_buttons[1].isChecked():
            self.local_flag = True
            self.url_flag = False

        
        else:
            self.labels[0].setText("bir işaretleme yapın..")
            self.local_flag = False
            self.url_flag = False


    def model(self):

        model = YOLO(self.model_path)

        #fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        #output_path = os.path.join(os.getcwd(), 'videos', 'output.mp4')
        #out = cv2.VideoWriter(output_path, fourcc, 60.0, (640, 480))
                
        cap = cv2.VideoCapture(self.path)
        self.total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.frame_counter=1
        cap.release()

        results = model(self.path, stream=True, save=True, conf=(self.conf_val/100))
        for res in results:
            self.frame_counter+=1
            self.progress_rate = ((int(self.frame_counter)/int(self.total_frames))*100)


        """
        while cap.isOpened():
            
            success, frame = cap.read()
            #results = model(frame, conf=0.5)

            for result in results:
               
                result.show()

                annotated_frame = results[0].plot()
                
                #cv2.imshow("YOLOv8 ile Kus yuvasi", annotated_frame)
                self.frame_counter+=1
                #cv2.imshow("frame", annotated_frame)
                
                
                #out.write(annotated_frame)
                self.progress_rate = (int(self.frame_counter)/int(self.total_frames))*100

            else:
                break

        cap.release()
        #out.release()
        cv2.destroyAllWindows()
        """


    def image_control(self):

        model = YOLO(self.model_path)

        model.predict(self.path, save=True, show=True, conf=(self.conf_val/100))


    def showVideo(self):

        if self.path != '':
            self.graphics[0].setMedia(QMediaContent(QUrl.fromLocalFile(self.path)))
            self.graphics[0].play()
        
    def open_media(self):
        
        if self.radio_buttons[0].isChecked():
            self.radio_button_select()
            self.path, self.filename = QFileDialog.getOpenFileName(self, "resim Dosyası Seç", "", "resim Dosyaları (*.png *.jpeg *.jpg)")
            self.image_control()

        elif self.radio_buttons[1].isChecked():
            self.radio_button_select()

            thred1 = threading.Thread(target=self.model)
            self.path, self.filename = QFileDialog.getOpenFileName(self, "Video Dosyası Seç", "", "Video Dosyaları (*.mp4 *.avi *.mkv)")
            self.showVideo()
            thred1.start()
            self.start_progress()

        else:
            self.radio_button_select()
            self.labels[0].setText("hatali islem")


    def start_progress(self):
        self.progress[0].setValue(0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(1000)

    def update_progress(self):

        if int(self.frame_counter) < int(self.total_frames) and int(self.frame_counter) != 0:
            self.progress[0].setValue(int(self.progress_rate))
        else :
            self.timer.stop()
        


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    prog = Program()
    prog.show()
    sys.exit(app.exec_())