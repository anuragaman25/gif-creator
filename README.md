# 🎞️ GIF Creator using Python

![GIF Preview](https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif)

## 🚀 Project Overview

This **GIF Creator** project allows you to generate animated GIFs from multiple images using **Python**. You can combine multiple images into a smooth animation in just a few lines of code! 🎨✨

## 📌 Features
✅ Converts multiple images into a GIF  
✅ Customizable GIF duration and looping  
✅ Simple and efficient Python script  
✅ Uses `imageio` and `PIL` for image processing  
✅ Resizes images to avoid errors due to mismatched sizes  

---

## 🛠️ Installation & Setup

### **1️⃣ Clone this Repository**
```sh
git clone https://github.com/anuragaman25/gif-creator.git
cd gif-creator
```

### **2️⃣ Install Required Dependencies**
Make sure you have Python **3.10+** installed. Then, install the required libraries:
```sh
pip install imageio pillow numpy
```

### **3️⃣ Add Your Images**
Place your images (`.png` or `.jpg`) inside the project folder.

---

## 🎨 Usage

### **Run the script**
```sh
python create_gif.py
```

### **Customize the GIF**
Modify `create_gif.py` to adjust settings:
- **`duration=500`** (Time per frame in milliseconds)
- **`loop=0`** (Set to `0` for infinite loop, or a specific number for limited loops)

---

## 📷 Sample Code

```python
import imageio.v3 as iio
from PIL import Image
import numpy as np

def resize_images(image_files, target_size=(500, 500)):
    resized_images = []
    for file in image_files:
        img = Image.open(file)
        img = img.resize(target_size)
        img_array = np.array(img)
        resized_images.append(img_array)
    return resized_images

def create_gif(image_files, output_name='output.gif', duration=500, loop=0):
    images = resize_images(image_files)
    iio.imwrite(output_name, images, duration=duration, loop=loop)
    print(f"GIF saved as {output_name}")

filenames = ['image1.png', 'image2.png', 'image3.png']
create_gif(filenames, 'my_animation.gif', duration=500, loop=0)
```

---

## 📩 Contribution
🙌 Contributions are welcome! If you have suggestions or improvements:
1. Fork this repo 🍴
2. Create a new branch 🌿
3. Make your changes 🛠
4. Submit a pull request 📩

---

## 📜 License
This project is open-source and available under the **MIT License**.

📌 **Developed with ❤️ by [Anurag Aman](https://github.com/anuragaman25)** 🚀

