
---

# Real-Time Facial Emotion Detection

## Description

This project implements a real-time facial emotion detection system using OpenCV, DeepFace, and PyQt5. The application captures live video feed from the camera, detects faces, analyzes the dominant emotion in each face using DeepFace, and displays the results on the screen. It also provides statistics of the detected emotions.

## Features

- Real-time face detection and emotion analysis.
- Displays the detected emotions on the video feed.
- Shows statistical distribution of detected emotions.
- User-friendly graphical interface with PyQt5.
- Start and stop camera feed with a single button click.
- Display emotion statistics in a bar chart.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/mohsenakhavan/Percentage-of-Facial-Emotions.git
    cd emotion-detector
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**
    ```bash
    python main.py
    ```

## Usage

- **Start Button:** Starts the camera feed and begins emotion detection.
- **Stop Button:** Stops the camera feed.
- **Show Stats Button:** Displays a bar chart with the percentage distribution of detected emotions.

## Dependencies

- OpenCV
- DeepFace
- PyQt5
- Matplotlib
- Numpy

## License

This project is licensed under the MIT License.

---

# تشخیص حالات چهره به صورت لحظه‌ای

## توضیحات

این پروژه یک سیستم تشخیص حالات چهره به صورت لحظه‌ای با استفاده از OpenCV، DeepFace و PyQt5 پیاده‌سازی می‌کند. این برنامه فید ویدیویی زنده از دوربین را ضبط می‌کند، چهره‌ها را تشخیص می‌دهد، احساس غالب در هر چهره را با استفاده از DeepFace تجزیه و تحلیل می‌کند و نتایج را روی صفحه نمایش می‌دهد. همچنین آمار حالات تشخیص داده شده را فراهم می‌کند.

## ویژگی‌ها

- تشخیص چهره و تجزیه و تحلیل احساسات به صورت لحظه‌ای.
- نمایش حالات تشخیص داده شده روی فید ویدیویی.
- نمایش توزیع آماری حالات تشخیص داده شده.
- رابط کاربری کاربرپسند با PyQt5.
- شروع و توقف فید دوربین با یک کلیک.
- نمایش آمار حالات در نمودار میله‌ای.

## نصب

1. **کلون کردن مخزن:**
    ```bash
    git clone https://github.com/mohsenakhavan/Percentage-of-Facial-Emotions.git
    cd emotion-detector
    ```

2. **ایجاد و فعال‌سازی محیط مجازی:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # در ویندوز: venv\Scripts\activate
    ```

3. **نصب بسته‌های مورد نیاز:**
    ```bash
    pip install -r requirements.txt
    ```

4. **اجرای برنامه:**
    ```bash
    python main.py
    ```

## استفاده

- **دکمه شروع:** شروع فید دوربین و شروع تشخیص احساسات.
- **دکمه توقف:** توقف فید دوربین.
- **دکمه نمایش آمار:** نمایش نمودار میله‌ای با توزیع درصدی حالات تشخیص داده شده.

## وابستگی‌ها

- OpenCV
- DeepFace
- PyQt5
- Matplotlib
- Numpy


## مجوز

این پروژه تحت مجوز MIT قرار دارد.

---

