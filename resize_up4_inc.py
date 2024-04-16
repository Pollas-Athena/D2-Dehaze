import os
import cv2

# 输入文件夹和输出文件夹路径
input_folder = 'dataset/NH_O_DENSE_HAZE_more_resize/conclusion_use_RE_3000_19_4350'
output_folder = 'dataset/NH_O_DENSE_HAZE_more_resize/inc/conclusion_use_RE_3000_19_4350'

# 上采样比例
scale_factor = 4


if not os.path.exists(output_folder):
    os.makedirs(output_folder)


for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp')):

        input_image_path = os.path.join(input_folder, filename)
        original_image = cv2.imread(input_image_path)

        upsampled_image = cv2.resize(original_image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)

        output_image_path = os.path.join(output_folder, f'upsampled_{filename}')

        cv2.imwrite(output_image_path, upsampled_image)

print("上采样完成。")
