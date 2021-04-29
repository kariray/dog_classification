from PIL import Image
import os
# Reference : https://note.nkmk.me/en/python-pillow-add-margin-expand-canvas/

def resizing():
    dir_path = 'archive/images'
    dir_names = os.listdir(dir_path)
    for dir_name in dir_names :
        if dir_name != ".DS_Store" :
            file_path = f"{dir_path}/{dir_name}"
            file_names = os.listdir(file_path)
            for file_name in file_names :
                img = Image.open(f"archive/images/{dir_name}/{file_name}")
                rgb_img = img.convert("RGB")
                img_new = change2square(rgb_img, (0, 0, 0)).resize((256, 256))
                new_dir = f"dog_resize/{dir_name}"
                if not os.path.isdir(new_dir):
                    os.mkdir(new_dir)
                img_new.save(f"{new_dir}/{file_name}", quality = 95)


# img_resize = img.resize((256, 256))
# img_resize.save('dog_resize/resize2.jpg')

def change2square(pill_img, background_color):
    width, height = pill_img.size
    if width == height:
        return pill_img
    elif width> height :
        result = Image.new(pill_img.mode, (width, width), background_color)
        result.paste(pill_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pill_img.mode, (height, height), background_color)
        result.paste(pill_img, ((height - width) // 2, 0))
        return result

resizing()


