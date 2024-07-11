import cv2
import numpy as np
from deepface import DeepFace
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QImage, QPixmap

class EmotionDetector:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.emotions = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
        self.emotion_counts = {emotion: 0 for emotion in self.emotions}

    def detect_emotion(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            roi = frame[y:y+h, x:x+w]
            try:
                result = DeepFace.analyze(roi, actions=['emotion'], enforce_detection=False)
                emotion = result[0]['dominant_emotion']
                self.emotion_counts[emotion] += 1
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                cv2.putText(frame, emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
            except:
                pass

        return frame

    def get_emotion_stats(self):
        total = sum(self.emotion_counts.values())
        if total == 0:
            return {emotion: 0 for emotion in self.emotions}
        return {emotion: count / total * 100 for emotion, count in self.emotion_counts.items()}

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("تشخیص حالات چهره")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #f0f0f0;")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QHBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.camera_label = QLabel()
        self.camera_label.setStyleSheet("border: 2px solid #3498db; border-radius: 10px;")
        self.layout.addWidget(self.camera_label, 2)

        self.right_layout = QVBoxLayout()
        self.layout.addLayout(self.right_layout, 1)

        self.start_button = QPushButton("شروع")
        self.start_button.clicked.connect(self.start_camera)
        self.start_button.setStyleSheet("QPushButton {background-color: #2ecc71; color: white; border-radius: 5px; padding: 10px;}"
                                        "QPushButton:hover {background-color: #27ae60;}")
        self.right_layout.addWidget(self.start_button)

        self.stats_button = QPushButton("نمایش آمار")
        self.stats_button.clicked.connect(self.show_stats)
        self.stats_button.setStyleSheet("QPushButton {background-color: #3498db; color: white; border-radius: 5px; padding: 10px;}"
                                        "QPushButton:hover {background-color: #2980b9;}")
        self.right_layout.addWidget(self.stats_button)

        self.emotion_detector = EmotionDetector()
        self.camera = cv2.VideoCapture(0)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

    def start_camera(self):
        if self.timer.isActive():
            self.timer.stop()
            self.start_button.setText("شروع")
            self.start_button.setStyleSheet("QPushButton {background-color: #2ecc71; color: white; border-radius: 5px; padding: 10px;}"
                                            "QPushButton:hover {background-color: #27ae60;}")
        else:
            self.timer.start(30)
            self.start_button.setText("توقف")
            self.start_button.setStyleSheet("QPushButton {background-color: #e74c3c; color: white; border-radius: 5px; padding: 10px;}"
                                            "QPushButton:hover {background-color: #c0392b;}")

    def update_frame(self):
        ret, frame = self.camera.read()
        if ret:
            frame = self.emotion_detector.detect_emotion(frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            q_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            self.camera_label.setPixmap(QPixmap.fromImage(q_image))

    def show_stats(self):
        stats = self.emotion_detector.get_emotion_stats()
        plt.figure(figsize=(10, 6))
        plt.bar(stats.keys(), stats.values())
        plt.title('Percentage of Facial Emotions')
        plt.xlabel('Emotions')
        plt.ylabel('Percentage')
        plt.show()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()