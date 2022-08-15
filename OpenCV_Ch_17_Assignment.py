# # Assignment: Stacking Images Horizontally When Their Sizes are Different

# ### Step 01 - Import Libraries
# import cv2 as cv
# import numpy as np

# ### Reading the Images
# img1 = cv.imread("Resources/birds.jpg")
# img2 = cv.imread("Resources/garden.png")

# ### Displaying the Images
# cv.imshow("Birds", img1)
# cv.imshow("Garden", img2)
# cv.imwrite("bir.png", img1)
# cv.imwrite("gar.png", img2)

# # Here, it can be seen that both images have different sizes. Now, we are going to concatenate them Horizontally

# # define a function for vertically concatenating images of different widths 
# def hconcat_resize_min(im_list, interpolation=cv.INTER_CUBIC):
#     h_min = min(im.shape[0] for im in im_list)
#     im_list_resize = [cv.resize(im, (int(im.shape[1] * h_min / im.shape[0]), h_min), interpolation=interpolation)
#                       for im in im_list]
#     return cv.hconcat(im_list_resize)

# im_h_resize = hconcat_resize_min([img1, img2])
# cv.imshow('h_concat.jpg', im_h_resize)
# cv.imwrite("horizontally_stacked.png", im_h_resize)
# cv.waitKey(0)
# cv.destroyAllWindows()
