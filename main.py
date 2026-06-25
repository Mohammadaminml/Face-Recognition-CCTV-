import cv2
import face_recognition
import os

# ایجاد پوشه برای ذخیره چهره‌ها
if not os.path.exists("faces"):
    os.makedirs("faces")

# تابع برای ذخیره چهره
def save_face(face_image, count):
    filename = f"faces/face_{count}.jpg"
    cv2.imwrite(filename, face_image)
    print(f"Face saved as {filename}")

# تنظیمات دوربین مداربسته
video_capture = cv2.VideoCapture(0)  # در اینجا از وب‌کم پیش‌فرض استفاده می‌شود، برای دوربین دیگر آی‌پی یا شناسه مناسب را وارد کنید
face_count = 0  # شمارنده تعداد چهره‌ها

while True:
    # گرفتن فریم از ویدیو
    ret, frame = video_capture.read()
    if not ret:
        break

    # تغییر رنگ تصویر به RGB برای تشخیص بهتر چهره‌ها
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # شناسایی مکان‌های چهره‌ها در تصویر
    face_locations = face_recognition.face_locations(rgb_frame)

    # رسم مستطیل دور چهره‌های شناسایی شده
    for (top, right, bottom, left) in face_locations:
        # جدا کردن چهره از تصویر اصلی
        face_image = frame[top:bottom, left:right]
        # ذخیره چهره
        save_face(face_image, face_count)
        face_count += 1

        # رسم مستطیل روی فریم اصلی
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    # نمایش فریم با مستطیل‌های شناسایی شده
    cv2.imshow("Video", frame)

    # خروج با کلید 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# آزادسازی دوربین و بستن تمام پنجره‌ها
video_capture.release()
cv2.destroyAllWindows()