import numpy as np
import cv2

def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def compute_lbp_pixel(img, x, y):
    center = img[x, y]
    pattern = 0
    patterns = []
    for i, j in [(1, 0), (1, 1), (0, 1), (-1, 1),
                 (-1, 0), (-1, -1), (0, -1), (1, -1)]:
        if img[x + i, y + j] >= center:
            patterns.append(1)
        else:
            patterns.append(0)
    for i in range(len(patterns)):
        pattern += patterns[i] * (2 ** i)
    return pattern

def compute_lbp_image(img):
    lbp_img = np.zeros_like(img)
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            lbp_img[i, j] = compute_lbp_pixel(img, i, j)
    return lbp_img

def compute_histogram(lbp_img):
    hist = np.zeros(256, dtype=np.uint8)
    for i in range(lbp_img.shape[0]):
        for j in range(lbp_img.shape[1]):
            hist[lbp_img[i, j]] += 1
    return hist

def lbp_feature_vector(image):
    gray_img = grayscale(image)
    lbp_img = compute_lbp_image(gray_img)
    hist = compute_histogram(lbp_img)
    return hist.flatten()

# Example usage:
image = cv2.imread('data')
feature_vector = lbp_feature_vector(image)
print(feature_vector)
