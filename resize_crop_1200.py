import os
from PIL import Image

def crop_images_in_folder(input_folder, output_folder, target_width=1600, target_height=1200):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp')): 
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            image = Image.open(input_path)

            width, height = image.size

            top = (height - target_height) // 2
            bottom = top + target_height

            cropped_image = image.crop((0, top, width, bottom))

            cropped_image.save(output_path)

if __name__ == "__main__":
    input_folder = "dataset/NH_O_DENSE_HAZE_more_resize/inc_bic_sr"  # 替换为实际的输入文件夹路径
    output_folder = "dataset/NH_O_DENSE_HAZE_more_resize/inc_bic_sr_crop"  # 替换为实际的输出文件夹路径

    crop_images_in_folder(input_folder, output_folder)
