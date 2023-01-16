import cv2
import matplotlib.pyplot as plt
import numpy as np


def grey(image):
    # grayscale
    image = np.asarray(image)
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


# Gaussian Blur
def gauss(image):
    return cv2.GaussianBlur(image, (5, 5), 0)


def canny(image):
    edges = cv2.Canny(image, 50, 150)
    return edges


def region(image):
    height, width = image.shape

    triangle = np.array([
        [(100, height), (475, 325), (width, height)]
    ])
    # siyah
    mask = np.zeros_like(image)
    # mask
    mask = cv2.fillPoly(mask, triangle, 255)
    mask = cv2.bitwise_and(image, mask)
    return mask


def display_lines(image, lines):
    lines_image = np.zeros_like(image)

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line

            cv2.line(lines_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
    return lines_image


def average(image, lines):
    left = []
    right = []
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)

            parameters = np.polyfit((x1, x2), (y1, y2), 1)
            slope = parameters[0]
            y_int = parameters[1]

            if slope < 0:
                left.append((slope, y_int))
            else:
                right.append((slope, y_int))

    # column average
    right_avg = np.average(np.array(right), axis=0)
    left_avg = np.average(np.array(left), axis=0)
    # lines based on average
    left_line = make_points(image, left_avg)
    right_line = make_points(image, right_avg)
    return np.array([left_line, right_line])


def make_points(image, average):
    print(average)
    slope, y_int = average
    y1 = image.shape[0]
    y2 = int(y1 * (3 / 5))
    # biraz da math
    x1 = int((y1 - y_int) // slope)
    x2 = int((y2 - y_int) // slope)
    return np.array([x1, y1, x2, y2])


cap = cv2.VideoCapture('road.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('frame', gray)

    copy = np.copy(gray)
    edges = cv2.Canny(copy, 10, 125, 1)
    isolated = region(edges)
    cv2.imshow("edges", edges)
    cv2.imshow("isolated", isolated)
    cv2.waitKey(0)

    lines = cv2.HoughLinesP(isolated, 2, np.pi / 180, 100, np.array([]), minLineLength=40, maxLineGap=5)
    averaged_lines = average(copy, lines)
    cv2.imshow("avar", averaged_lines)
    black_lines = display_lines(copy, averaged_lines)

    lanes = cv2.addWeighted(copy, 0.8, black_lines, 1, 1)
    cv2.imshow("lanes", lanes)
    cv2.waitKey(0)

    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
