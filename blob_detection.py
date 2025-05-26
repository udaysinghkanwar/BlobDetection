import cv2
import numpy as np

# 1. Load the original color image (not grayscale!)
color_img = cv2.imread("TestImage2.png", cv2.IMREAD_COLOR)

# 2. Convert to HSV and threshold out the green pixels
hsv   = cv2.cvtColor(color_img, cv2.COLOR_BGR2HSV)
lower = np.array([48,  12,  0])   # tweak H,S,V mins
upper = np.array([82, 255, 255])   # tweak H,S,V maxes
mask  = cv2.inRange(hsv, lower, upper)  # green→255, everything else→0

cv2.imshow("Mask 1", mask)
# (Optional) clean up noise / fill holes
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
mask   = cv2.morphologyEx(mask, cv2.MORPH_OPEN,  kernel)
mask   = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Mask", mask)

# 3. Set up your blob detector to look for bright blobs (white regions in mask)
params = cv2.SimpleBlobDetector_Params()
params.minThreshold = 0
params.maxThreshold = 255
"""
These are the parameters that can be fine tuned to get the best results for our use case.

params.filterByArea        = True
params.minArea             = 10
params.filterByCircularity = True
params.minCircularity      = 0.1
params.filterByConvexity   = True
params.minConvexity        = 0.87
params.filterByInertia     = True
params.minInertiaRatio     = 0.01
"""

params.filterByArea        = False
params.filterByCircularity = False
params.filterByConvexity   = False
params.filterByInertia     = False

params.filterByColor       = True
params.blobColor           = 255   # ← we want white blobs in our mask

detector = cv2.SimpleBlobDetector_create(params)

# 4. Detect on the mask, not the raw grayscale
keypoints   = detector.detect(mask)
coordinates = cv2.KeyPoint_convert(keypoints)

print(keypoints)
print("Co‐ordinates of the green blobs:", coordinates)

# 5. Draw those keypoints back on the original color image
output = cv2.drawKeypoints(
    color_img, 
    keypoints, 
    np.array([]), 
    (0, 0, 255),                         # red circles
    cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)

cv2.imshow("Green Blobs Detected", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
