import os
from PIL import Image

# 输入文件夹和输出文件夹路径
# 输入文件夹和输出文件夹路径
input_folder = 'dataset/NH_O_DENSE_HAZE_more_resize/conclusion_use_RE_3000_19_4350'
output_folder = 'dataset/NH_O_DENSE_HAZE_more_resize/inc_bic/conclusion_use_RE_3000_19_4350'

# 指定上采样比例
scale_factor = 4

# 创建输出文件夹
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的图像文件
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp')):  # 只处理图像文件
        input_image_path = os.path.join(input_folder, filename)
        output_image_path = os.path.join(output_folder, filename)

        # 打开图像
        input_image = Image.open(input_image_path)

        # 获取原图像的尺寸
        original_width, original_height = input_image.size

        # 设置目标尺寸为原来的4倍
        target_width = original_width * scale_factor
        target_height = original_height * scale_factor

        # 使用双三次插值进行上采样
        upsampled_image = input_image.resize((target_width, target_height), resample=Image.BICUBIC)

        # 保存上采样后的图像到输出文件夹
        upsampled_image.save(output_image_path)

print("上采样完成！")
