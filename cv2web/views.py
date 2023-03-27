from django.http import StreamingHttpResponse
from django.shortcuts import render
import cv2

# Create your views here.


def index(request):
    return render(request, 'cv2web/index.html')


def stream():
    cap = cv2.VideoCapture('3.mp4')

    while True:
        ret, frame = cap.read()
        ret, jpeg = cv2.imencode('.jpg', frame)
        if not ret:
            print("Error: failed to capture image")
            break

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()


def video_feed(request):
    return StreamingHttpResponse(stream(), content_type='multipart/x-mixed-replace; boundary=frame')