import cv2
import numpy as np

# Load the image
image = cv2.imread('C:\\Users\\ADMIN\\Pictures\\wallpaper\\anya.jpeg')

# Define the transformation matrix
# For an affine transformation, you need a 2x3 transformation matrix.
# This matrix can perform translations, rotations, scaling, and shearing.
# Here, we will perform a simple translation.
# Let's translate the image by 100 pixels to the right and 50 pixels down.
tx = 100
ty = 50
M = np.float32([[1, 0, tx], [0, 1, ty]])

# Apply the affine transformation using warpAffine function
# The third argument is the size of the output image.
# We'll keep it the same size as the input image for simplicity.
transformed_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

# Display the original and transformed images
cv2.imshow('Original Image', image)
cv2.imshow('Transformed Image', transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
