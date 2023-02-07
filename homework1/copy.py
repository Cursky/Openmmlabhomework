import os

train_txt = '../train.txt'
val_txt = '../val.txt'

# 创建所有类别的文件夹
classes = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']
for cls in classes:
    os.makedirs(f'train/{cls}', exist_ok=True)
    os.makedirs(f'val/{cls}', exist_ok=True)

# 复制 train.txt 中的图像到对应的文件夹
with open(train_txt, 'r') as f:
    for line in f:
        img_path, label = line.strip().split()
        label = classes[int(label)]
        dest = f'train/{label}/{os.path.basename(img_path)}'
        os.system(f'cp {img_path} {dest}')

# 复制 val.txt 中的图像到对应的文件夹
with open(val_txt, 'r') as f:
    for line in f:
        img_path, label = line.strip().split()
        label = classes[int(label)]
        dest = f'val/{label}/{os.path.basename(img_path)}'
        os.system(f'cp {img_path} {dest}')
