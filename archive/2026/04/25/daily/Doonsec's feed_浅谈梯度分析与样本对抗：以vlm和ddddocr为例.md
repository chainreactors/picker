---
title: 浅谈梯度分析与样本对抗：以vlm和ddddocr为例
url: https://mp.weixin.qq.com/s/5cYB87tv_eUyeL4WLWi9cw
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T04:56:55.166851
---

# 浅谈梯度分析与样本对抗：以vlm和ddddocr为例

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K2oLCedic85Fmn4iaPhoZe0ibbkWpjibY2V78hu1pVG1hJTFqW3EeDtJmzibUTchUrtnQJemyxiahFpwkQPU7qdmlbr8iaLibySgIfnkkc/0?wx_fmt=jpeg)

# 浅谈梯度分析与样本对抗：以vlm和ddddocr为例

the\_hs
the\_hs

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 早在2018年，便有学者（https://arxiv.org/abs/1808.07945）发现可以通过仅修改几个像素来干扰模型对输入的预测。

作为一篇社区博客，本文将谈论如何**构造**验证码，而不是如何解决验证码，以避免不必要的副面影响（构造验证码来保护在线业务几乎总是有利于保护网络安全环境的）。请勿恶意构造其他数据，或利用类似方法做对抗性滤波，避免对他人服务产生影响。

**验证码识别器的原理**

在开始谈论对抗性验证码构造前，我们必须了解验证码识别器的原理。

绝大多数的人工智能识别器，从ResNet到Yolo，都是基于卷积层的。卷积层是网络的核心，其运算并非数学严格定义上的卷积，而是互相关运算。给定一个二维输入张量X，其维度为高度H和宽度W，卷积核K为一个大小为kH乘以kW的张量。输出特征图矩阵中的每一个元素Y(i, j)是通过卷积核在输入图像上的滑动窗口内进行逐元素相乘并求和得到的。从数学角度看，这可以表示为在每一个空间位置上，输入局部区域向量与卷积核权值向量的内积再加上偏置项。

由于同一个卷积核在整个输入空间上滑动，这种权值共享极大减少了参数数量，并利用了图像统计属性的局部平稳性。在卷积操作之后，通常会施加一个非线性激活函数，最常用的是修正线性单元ReLU，即函数f(x)等于max(0, x)。

引入非线性的目的是为了使网络能够拟合复杂的非线性函数，否则多层线性卷积层在数学上等价于单层线性变换，将失去深层结构的表达能力。

这里，为了更教育意义，我们这里先自己训练一个甚至有一点过度简化（只有数字识别、没有位置检测和分割功能）的验证码识别器。在产业中，这一步可以直接替换为使用攻击者使用的模型进行防御。

我们先对mnist数据集进行一些简单的扰动，代码如下：

```
# img is 28x28 numpy array, uint8

# Random shift -2 to 2
shift_x, shift_y = random.randint(-2, 2), random.randint(-2, 2)
M1 = np.float32([[1, 0, shift_x], [0, 1, shift_y]])
img = cv2.warpAffine(img, M1, (28, 28), borderValue=0)

# Random scale -> resize and crop/pad to 28x28
# Target size within 26x30 to 30x26
t_width = random.randint(26, 30)
t_height = 56 - t_width  # keeping sum around 56, matching 26x30 ~ 30x26 boundaries
if t_width == 28:
    t_height = 28
else:
    t_height = random.randint(26, 30)

img = cv2.resize(img, (t_width, t_height))

# Pad or crop to 28x28
canvas = np.zeros((28, 28), dtype=np.uint8)
start_y = max((t_height - 28) // 2, 0)
start_x = max((t_width - 28) // 2, 0)

c_start_y = max((28 - t_height) // 2, 0)
c_start_x = max((28 - t_width) // 2, 0)

copy_h = min(28, t_height)
copy_w = min(28, t_width)

canvas[c_start_y:c_start_y + copy_h, c_start_x:c_start_x + copy_w] = img[start_y:start_y + copy_h, start_x:start_x + copy_w]
img = canvas

angle = random.uniform(-20, 20)
M2 = cv2.getRotationMatrix2D((14, 14), angle, 1.0)
img = cv2.warpAffine(img, M2, (28, 28), borderValue=0)

# Add 10 random noise pixels
for _ in range(10):
    nx, ny = random.randint(0, 27), random.randint(0, 27)
    img[ny, nx] = random.choice([0, 255])

return img.astype(np.float32) / 255.0
```

效果如图所示：

![图片描述](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K1dic3mDS6vvazY9lvMLYCfibibsJRdW3jjYj2PmichnRLzWewp2sibUKc5B337yCGEfx8jxZQsj18stX8xF1ePJyLShegsWHKXibfhA/640?wx_fmt=other&from=appmsg)

很多传统的验证码生成器就到此为止了（生成随机干扰点和线）。必须指出，尽管在今天看来，这种扰动是毫无意义的（任何合理的OCR都能无视这种扰动），但是它可以避免我们接下来的构建的识别器过度简单，从而不能正确地反应其他识别器的弱点。

**验证码识别器的构建**

我们可以随手（嗯，真的是随手，根本没怎么调优）设计一个CNN网络，比如说如图所示：

![图片描述](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K3VjOdPJicl3OZJEMhM0hz4oDeRd91fKfM7qe8YNQibLV1yrCJk2IgkmfX23jAyMGMrEN7OU8v9E8BosUOaLlKBBzflfajkktt0g/640?wx_fmt=other&from=appmsg)![]()

代码如下：

```
class SimpleCNN(nn.Module):
def __init__(self):
super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3, padding=1)
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)
        self.fc1 = nn.Linear(32 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, 10)

def forward(self, x):
        x = self.pool(self.relu(self.conv1(x)))
        x = self.pool(self.relu(self.conv2(x)))
        x = x.view(-1, 32 * 7 * 7)
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
return x
```

并画上那么几秒钟进行一个简单的训练。五秒钟后，尽管模型的准确率只有95%，并且没有分割等功能，但是已经足够我们下一步使用了。

```
Epoch 20/20, Loss:0.0017
Time elapsed:5.03 seconds
Test Accuracy:95.10%
```

##

**对抗性样本的构造**

构造对抗性样本有很多种不同的方法，这里展示一种笔者前日设计的方法（https://openaccess.thecvf.com/content/ICCV2025/html/Gao\_FastJSMA\_Accelerating\_Jacobian-based\_Saliency\_Map\_Attacks\_through\_Gradient\_Decoupling\_ICCV\_2025\_paper.html）的变种：取预测中高置信度的部分作为优化目标，进行逐点干扰。这里，为了确保不被滤波器滤除，同时没有benchmark需求，我们选择随机构造扰动幅度，代码如下：

```
img_adv = img_tensor.clone().detach().requires_grad_(True)
# A
T = set()
for step in range(50):
if img_adv.grad is not None:
        img_adv.grad.zero_()
    output = model(img_adv)
    model.zero_grad()
    output[0, target_class].backward(retain_graph=True)
    grad_target = img_adv.grad.clone()
    img_adv.grad.zero_()
    output[0, source_class].backward()
    grad_source = img_adv.grad.clone()
    D = (0.5 * grad_target - grad_source).squeeze()
    D_flat = D.view(-1)
for t_idx in T:
        D_flat[t_idx] = -float('inf')
    max_idx = torch.argmax(D_flat).item()
    T.add(max_idx)
# B
    magnitude = random.uniform(0.3, 0.6)
    direction = torch.sign(D_flat[max_idx]).item()
if direction == 0:
        direction = 1
with torch.no_grad():
        flat_img = img_adv.view(-1)
        flat_img[max_idx] += direction * magnitude
# C
        flat_img.clamp_(0, 1)
    img_adv.requires_grad_(True)
```

上述代码中A处是为了避免重复修改相同像素，B处是刚才提到的随机扰动，C处是为了避免生成的值不再是图像；这些点比较琐碎，但不正确的实现还是会导致效果不对。g+与g-的混合因子、试探方式与paper中存在微小出入，是为了更好地适配ddddocr进行的工程优化。那么就大功告成。

**效果测试**

4339

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K1IXbpjL7CicHz7W2lWR7tldClnP69fNvL9IHXyBg6iaxGeIuGMQzaNibJokbRVEE8Lm9KibB5Gvyl5pjiacWWlVvWppm4sBZytSywo/640?wx_fmt=other&from=appmsg)![]()

ddddocr-数字模式：识别失败

![图片描述](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K1LrDGJYbCcMkOnO9fbibrwsL9c2xJbtCW6B0D75yQKCKBxlRWPbTZbHcVlJs2sdwUuF5nWKDrmojtClplF0qOkn4Fon2icW9EH8/640?wx_fmt=other&from=appmsg)![]()

几个常见的vlm： 7984 9339 4239

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K0iaykpAyLywZoV2YDHB2kNj9dT5JpaHHq9J3icBOAYPVrlibhaz2g3tViaA22sPibkgYNs35qymOKPOUSAzSp8icrsfia0fkCBYXCB4k/640?wx_fmt=other&from=appmsg)![]()

ddddocr-全量模式：y33g

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K0HW10m3AYAoNCDqhiczFhR7SicORnSDP9ZxqkHdKDPHPS6ReicGLrZiaa03YamBkHGJqjKrX2scwCkPGWeUEIqbZcFAmibnXD4dz8E/640?wx_fmt=other&from=appmsg)![]()

PaddleOCR-VL: 936.9

![图片描述](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K3VVBkZIM1DlibqRibUh62TqlKgyuqNr7doNxhetOJrnda1ia36MBiax6GFr7AOFXHyGTRxo0BOEX9JQz4gqY4fAGIkLY2Ezm2BHm4/640?wx_fmt=other&from=appmsg)![]()

因此可以认为我们的验证码对于常见的机器学习方法拥有足够的抵抗力。

**总结**

本文所展示的对抗性样本构造方法，其唯一目的在于学术探讨及网络安全防御应用，旨在通过提升验证码的抗 AI 识别能力，帮助开发者更好地保护在线业务免受恶意自动化程序的攻击。

请勿将本文涉及的技术、代码或逻辑用于任何非法或违背道德的行为，包括但不限于样本投毒、恶意绕过他人的安全防御系统或干扰正常网络服务。在进行任何相关实验或应用时，请确保严格遵守《生成式人工智能服务管理暂行办法》及所在地区的相关法律法规。技术的使用应始终保持在合法、合规且符合伦理的框架内。

##

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K3eoscLLQIicV1ia8pMAef15GGEcqp8UgrcHSibmV7CXLMl4MxIzs1Lnpl6OPicj3Jbey8Urd8lgWERKEiarx9MTDmslxBL7r0icdyD8/640?wx_fmt=png&from=appmsg)

看雪ID：the\_hs

https://bbs.kanxue.com/user-home-994475.htm

\*本文为看雪论坛优秀文章，由 the\_hs 原创，转载请注明来自看雪社区

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K2qcLqpRmOMibeYwDybhCLLIjdNicUibsZsCmf4IQWHhSkZ8vaFGSPmKKNcSdD8ansPXR7U0ricmvGqBM3XEmciazwVm1V3Lq4qvQbE/640?wx_fmt=jpeg&from=appmsg)![]()![]()![]()![]()

# 往期推荐

[安卓逆向基础知识之frida Hook](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458612348&idx=1&sn=9b1f49187644981e264882dedfde45f9&scene=21#wechat_redirect)

[2025 强网杯和强网拟态部分题解](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458612341&idx=1&sn=08f4b531105ec2b3a44360f66169db05&scene=21#wechat_redirect)

[在逆向分析方面-unidbg真的适合 MCP 吗？](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458612340&idx=1&sn=0c799826addbc96801752a6c70938bf1&scene=21#wechat_redirect)

[AI静态分析，内核模块隐藏 Frida 特征，绕过linker私有结构遍历崩溃链](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458612335&idx=1&sn=ca23336eef45a4993cc6e5b191e62a61&scene=21#wechat_redirect)

[某安全so库深度解析](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458612118&idx=2&sn=47fe8a55e77b2ca8f2f8d73c9a9d99d0&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Hice1nuesdoDZjYQzRMv9tpvJW9icibkZBj9PNBzyQ4d4JFoAKxdnPqHWpMPQfNysVmcL1dtRqU7VyQ/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_...