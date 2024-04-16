import cv2

def resize_image_to_match(image_path_A, image_path_B):
    image_A = cv2.imread(image_path_A)
    image_B = cv2.imread(image_path_B)

    resized_image_A = cv2.resize(image_A, (image_B.shape[1], image_B.shape[0]))

    return resized_image_A

    # cv2.imshow('Resized Image A', resized_image_A)
    # # cv2.imwrite('resized_image_A.jpg', resized_image_A)  # 如果要保存调整后的图像A，取消注释该行并指定保存路径


# image_path_A = 'image_A.jpg'
# image_path_B = 'image_B.jpg'

# resize_image_to_match(image_path_A, image_path_B)