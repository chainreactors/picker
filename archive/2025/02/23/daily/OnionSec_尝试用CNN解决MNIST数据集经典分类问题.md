---
title: 尝试用CNN解决MNIST数据集经典分类问题
url: https://mp.weixin.qq.com/s?__biz=MzUyMTUwMzI3Ng==&mid=2247485571&idx=1&sn=d51aa8f4c841386d80202428a0d598e9&chksm=f9db5fc0ceacd6d6020bfec410b7da56966bcd99054d26546fb65e0c320876a9ffa2fb2cbf99&scene=58&subscene=0#rd
source: OnionSec
date: 2025-02-23
fetch_date: 2025-10-06T20:37:18.037657
---

# 尝试用CNN解决MNIST数据集经典分类问题

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dib9GLOoSY0goUMY2myz52nqibiaRWUGrKTut3k10mSCbC9z7Ub7bm4JiciachQn7tHEpibIKBAU7jciathLOJTzHrzJw/0?wx_fmt=jpeg)

# 尝试用CNN解决MNIST数据集经典分类问题

原创

jishuzhain

OnionSec

MNIST 数据集对应的任务是手写数字识别，属于图像分类任务。具体是对0~9 的手写数字分类，能够达到接近人脑的图像识别能力。这次选择CNN算法进行小实验，卷积神经网络已经被证明对图像类任务是合适的。

MNIST 数据集在下载时已经预先划分好了训练集和测试集：

训练集（train=True）包含 60000 张手写数字图片，用于模型训练。

测试集（train=False）包含 10000 张图片，用于模型评估。

思路是根据经验首先确定模型的架构，从最简单的网络结构开始。第二步使用超参数优化 (Hyperparameter Optimization)，以下训练的代码使用 Optuna 进行超参数优化，Optuna 是一个流行的库，用于高效的超参数优化。同时还利用了数据增强策略，例如对训练数据新增数据增强：随机旋转10度和随机平移（最大10%的图像移动）。主要是让模型“见到”更多数据，提升能力。

最终训练模型（代码1）得到的最佳超参数如下：

conv1\_out\_channels：第一个卷积层的输出通道数（特征图的数量）。88

conv2\_out\_channels：第二个卷积层的输出通道数。237

fc1\_out\_features：全连接层的输入特征数（即第一层全连接层的输出特征数）。389

Best hyperparameters: {'conv1\_out\_channels': 88, 'conv2\_out\_channels': 237, 'fc1\_out\_features': 389}

Training final model with best hyperparameters...

Epoch 1, Loss: 0.2567, Accuracy: 91.88%

Epoch 2, Loss: 0.0815, Accuracy: 97.48%

Epoch 3, Loss: 0.0653, Accuracy: 97.95%

Epoch 4, Loss: 0.0557, Accuracy: 98.26%

Epoch 5, Loss: 0.0508, Accuracy: 98.46%

Final test accuracy with best hyperparameters: 99.03%

Best model saved as best\_deep\_cnn\_model.pth

示例代码1如下：

|  |
| --- |
| ``` import torch import torch.nn as nn import torch.optim as optim import torchvision import torchvision.transforms as transforms import optuna from torch.utils.data import DataLoader   # --------------------------- # 数据增强与预处理 # ---------------------------   # 对训练数据新增数据增强：随机旋转10度和随机平移（最大10%的图像移动） train_transform = transforms.Compose([     transforms.RandomRotation(10),                # 随机旋转10度     transforms.RandomAffine(degrees=0, translate=(0.1, 0.1)),  # 随机平移     transforms.ToTensor(),     transforms.Normalize((0.5,), (0.5,)) ])   # 测试数据只做标准化 transform = transforms.Compose([     transforms.ToTensor(),     transforms.Normalize((0.5,), (0.5,)) ])   # 数据加载：训练集使用数据增强，测试集不使用 trainset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=train_transform) testset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)   trainloader = DataLoader(trainset, batch_size=64, shuffle=True) testloader = DataLoader(testset, batch_size=64, shuffle=False)     # --------------------------------------------- # 定义具有深度卷积层的网络结构 # --------------------------------------------- class DeepCNN(nn.Module):     def __init__(self, conv_layers, fc_layers):         """         构造深度卷积神经网络         conv_layers：包含卷积层输出通道数的列表         fc_layers：包含全连接层神经元数量的列表         """         super(DeepCNN, self).__init__()           # 构建卷积层         self.conv_layers = nn.ModuleList()         in_channels = 1         for out_channels in conv_layers:             self.conv_layers.append(nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1))             in_channels = out_channels           # 计算卷积层和池化层输出的尺寸         self._calculate_conv_output_size()           # 构建全连接层         self.fc_layers = nn.ModuleList()         self.fc_layers.append(nn.Linear(self.conv_output_size, fc_layers[0]))         for i in range(1, len(fc_layers)):             self.fc_layers.append(nn.Linear(fc_layers[i - 1], fc_layers[i]))         self.fc_layers.append(nn.Linear(fc_layers[-1], 10))  # 输出层，10个类别（MNIST）       def _calculate_conv_output_size(self):         # 假设输入尺寸为 28x28（MNIST）         dummy_input = torch.zeros(1, 1, 28, 28)  # 1个样本，1个通道，28x28的图像         x = dummy_input           # 逐层通过卷积和池化层计算输出尺寸         for conv in self.conv_layers:             x = torch.relu(conv(x))             x = torch.max_pool2d(x, 2)  # 2x2 池化           # 计算最终展平后的大小         self.conv_output_size = x.view(1, -1).size(1)  # 展平后尺寸大小       def forward(self, x):         # 卷积层和池化层         for conv in self.conv_layers:             x = torch.relu(conv(x))             x = torch.max_pool2d(x, 2)           # 展平         x = x.view(x.size(0), -1)           # 全连接层         for fc in self.fc_layers[:-1]:             x = torch.relu(fc(x))         x = self.fc_layers[-1](x)  # 最后一层全连接输出         return x     # --------------------------------------------- # 定义训练函数 # --------------------------------------------- def train_model(model, trainloader, testloader, epochs=5):     criterion = nn.CrossEntropyLoss()     optimizer = optim.Adam(model.parameters(), lr=0.001)     device = torch.device("cuda" if torch.cuda.is_available() else "cpu")     model.to(device)       for epoch in range(epochs):         model.train()         running_loss = 0.0         correct = 0         total = 0         for images, labels in trainloader:             images, labels = images.to(device), labels.to(device)             optimizer.zero_grad()             outputs = model(images)             loss = criterion(outputs, labels)             loss.backward()             optimizer.step()             running_loss += loss.item()             _, predicted = torch.max(outputs, 1)             total += labels.size(0)             correct += (predicted == labels).sum().item()           accuracy = 100 * correct / total         print(f"Epoch {epoch + 1}, Loss: {running_loss / len(trainloader):.4f}, Accuracy: {accuracy:.2f}%")       # 测试阶段     model.eval()     correct = 0     total = 0     with torch.no_grad():         for images, labels in testloader:             images, labels = images.to(device), labels.to(device)             outputs = model(images)             _, predicted = torch.max(outputs, 1)             total += labels.size(0)             correct += (predicted == labels).sum().item()       test_accuracy = 100 * correct / total     return test_accuracy     # --------------------------------------------- # 定义 Optuna 的目标函数来优化超参数 # --------------------------------------------- def objective(trial):     # 选择卷积层的数量和每个卷积层的输出通道数     conv_layers = [trial.suggest_int('conv1_out_channels', 32, 128),                    trial.suggest_int('conv2_out_channels', 64, 256)]       # 选择全连接层的神经元数量     fc_layers = [trial.suggest_int('fc1_out_features', 128, 512)]       # 创建模型     model = DeepCNN(conv_layers, fc_layers)       # 训练并返回在测试集上的准确率     accuracy = train_model(model, trainloader, testloader)     return accuracy     # --------------------------------------------- # 使用 Optuna 进行超参数优化 # --------------------------------------------- study = optuna.create_study(direction='maximize')  # 目标是最大化准确率 study.optimize(objective, n_trials=10)  # 进行 10 次实验，尝试不同的超参数   print(f"Best hyperparameters: {study.best_params}")   # 利用最佳参数构造模型，并进行最终训练 best_conv_layers = [study.best_params['conv1_out_channels'], study.best_params['conv2_out_channels']] best_fc_layers = [study.best_params['fc1_out_features']] best_model = DeepCNN(best_conv_layers, best_fc_layers)   print("Training final model with best hyperparameters...") final_test_accuracy = train_model(best_model, trainloader, testloader, epochs=5) print(f"Final test accuracy with best hyperparameters: {final_test_accuracy:.2f}%")   # 保存最终模型到本地 torch.save(best_model.state_dict(), "best_deep_cnn_model.pth") print("Best model saved as best_deep_cnn_model.pth") ``` |

代码2利用最佳的超参数，对模型进行全面评估。

|  |
| --- |
| ``` import torch import torch.nn as nn import torch.optim as optim import torchvision import torchvision.transforms as transforms import optuna  # 如果后续需要使用该工具进行超参数优化 import numpy as np  import matplotlib.pyplot as plt import seaborn as sns  from sklearn.metrics import (precision_recall_fscore_support,                              roc_auc_score,                              confusion_matrix,                              classification_report,                              cohen_kappa_score,                              balanced_accuracy_score,                              roc_curve, auc) from sklearn.preprocessing import label_binarize import os  # --------------------------- # 数据增强与预处理 # ---------------------------  # 对训练数据新增数据增强：随机旋转10度和随机平移（最大10%的图像移动） train_transform = transforms.Compose([     transforms.RandomRotation(10),                # 随机旋转10度     transforms.RandomAffine(de...