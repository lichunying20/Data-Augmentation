from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt

# 定义数据增强变换
transform = transforms.Compose([
    transforms.RandomResizedCrop(256, scale=(0.5, 0.5), ratio=(1.0, 1.0)),
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.RandomRotation(degrees=(-10, 10)),
    transforms.ToTensor(),
])

# 加载训练集图片和验证集图片
train_image = Image.open(r'D:\GitHub_test\classification-basic-sample\data\train\train\cat.jpg')
val_image = Image.open(r'D:\GitHub_test\classification-basic-sample\data\val\val\dog.jpg')

# 对训练集图片和验证集图片进行增广
augmented_train_image = transform(train_image)
augmented_val_image = transform(val_image)

# 显示增广后的图片
fig, axs = plt.subplots(1, 2)
axs[0].imshow(augmented_train_image.permute(1, 2, 0))
axs[1].imshow(augmented_val_image.permute(1, 2, 0))
plt.show()