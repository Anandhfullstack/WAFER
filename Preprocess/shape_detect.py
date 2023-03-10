import cv2


class shaper():
    def __init__(self):
        pass

    def detect(self, contour):
        image_shape="unidentified"
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.04 * peri, True)

        if len(approx) == 3:
            shape = "triangle"
        elif len(approx) == 4:
            # compute the bounding box of the contour and use the
            # bounding box to compute the aspect ratio
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)

            # a square will have an aspect ratio that is approximately
            # equal to one, otherwise, the shape is a rectangle
            image_shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"

            # if the shape is a pentagon, it will have 5 vertices
        elif len(approx) == 5:
            image_shape = "pentagon"

            # otherwise, we assume the shape is a circle
        else:
            image_shape = "circle"

    # return the name of the shape
        return image_shape