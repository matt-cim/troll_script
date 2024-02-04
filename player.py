import numpy as np
import cv2 as cv
from multiprocessing import Process

PROCESSES = 20

def play_video():
    cap = cv.VideoCapture(r"C:\Users\Example_User\Videos\video.mp4")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Video length expired\n")
            break

        cv.namedWindow("window", cv.WND_PROP_FULLSCREEN)
        cv.setWindowProperty("window", cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)

        cv.imshow("window", frame)

        if cv.waitKey(1) == ord('!'): # pressing ! terminates, need this condition for some reason
            break

    # done
    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    ps = []
    for i in range(PROCESSES):
        p = Process(target = play_video)
        p.start()
        ps.append(p)
    for p in ps:
        p.join()