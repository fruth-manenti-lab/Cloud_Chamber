import cv2

img = cv2.imread('/Users/parakhkotwani/Downloads/Particle-Identification-System-in-Cloud-Chamber-Using-YoloV5-main/images/train/cloudchamber1.png')

if img is None:
    print("Error: Image not found or path is incorrect.")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    thresh = cv2.adaptiveThreshold(
        blurred, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        11, 2)

    cv2.imshow('Enhanced Particle Tracks', thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
