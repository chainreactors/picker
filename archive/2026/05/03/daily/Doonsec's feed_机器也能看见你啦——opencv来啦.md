---
title: 机器也能看见你啦——opencv来啦
url: https://mp.weixin.qq.com/s/hmWpputbR4AKQlqP18W_Wg
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:27:16.337434
---

# 机器也能看见你啦——opencv来啦

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/njicUbJnVlIxopyx9XS8dEtOPDQBLJxweaecBf0FPNLtKWRLcPe364Z2mFBEoyWeHpibU1tkMCVRZb9cDvBvCSnJ0tr1nzMPNllTVZgHnVKibc/0?wx_fmt=jpeg)

# 机器也能看见你啦——opencv来啦

原创

书中自有代码来
书中自有代码来

书中自有代码来

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 一、什么是OpenCV

OpenCV（Open Source Computer Vision Library）是一个基于开源发行的跨平台计算机视觉与机器学习软件库。它最初由英特尔于1999年发起建立，如今由庞大的全球开发者社区共同维护。OpenCV以C++为核心编写，同时提供了Python、Java等多种语言的接口，能够无缝运行在Windows、Linux、macOS、Android及iOS等主流操作系统上。该库轻量级且高效，内置了500多个涵盖图像处理、视频分析、目标检测及深度学习推理的通用算法。作为计算机视觉领域的“瑞士军刀”，它被广泛应用于自动驾驶、人脸识别、工业质检及医疗影像分析等前沿领域。

# 二、常用函数和方法

## 图像输入

```
img = cv2.imread(filename, flags)
```

> 这是 OpenCV 中最基础的函数之一，用于从指定的文件路径加载图片数据并转换为 NumPy 数组。如果文件路径错误或格式不支持，函数会返回 `None`。它常用于程序启动时加载需要处理的原始素材。

| 参数名 | 说明 |
| --- | --- |
| `filename` | 要读取的文件完整路径（字符串）。 |
| `flags` | 读取标志，指定读取图像的颜色模式（默认为 `cv2.IMREAD_COLOR`）。 |

* **支持格式**

  : `.bmp`, `.dib`, `.jpeg`, `.jpg`, `.jpe`, `.jp2`, `.png`, `.webp`, `.pbm`, `.pgm`, `.ppm`, `.pxm`, `.pnm`, `.tiff`, `.tif`
* **Flags**

  :

+ `cv2.IMREAD_COLOR`

  (1): 转为 3 通道（默认）。
+ `cv2.IMREAD_GRAYSCALE`

  (0): 单通道灰度。
+ `cv2.IMREAD_UNCHANGED`

  (-1): 原样读取（包含 Alpha 通道）。
+ `cv2.IMREAD_ANYDEPTH`

  (2): 返回 16/32 位图，否则转为 8 位。
+ `cv2.IMREAD_ANYCOLOR`

  (4): 读取任意颜色。

## 图像显示

```
cv2.imshow(winname, mat)
```

> 在一个弹出窗口中显示加载或处理后的图像。该函数通常与 `cv2.waitKey()` 配合使用，否则窗口会一闪而过。它主要用于代码调试阶段，帮助开发者直观地查看图像处理的中间结果或最终效果。

| 参数名 | 说明 |
| --- | --- |
| `winname` | 显示窗口的名称（字符串）。 |
| `mat` | 要显示的图像数据（NumPy 数组）。 |

## 按键等待

```
cv2.waitKey(delay)
```

> 用于绑定键盘事件并控制图像窗口的显示时长。如果 `delay` 设为 0，程序会无限期等待用户按下任意键；如果设为正整数（如 1000），则窗口会显示 1000 毫秒。它常紧接在 `cv2.imshow()` 之后，防止窗口瞬间关闭。

| 参数名 | 说明 |
| --- | --- |
| `delay` | 等待时间（单位：毫秒）。0 表示无限等待。 |

## 关闭窗口

```
cv2.destroyAllWindows()
```

> 销毁（关闭）所有由 OpenCV 创建的显示窗口，并释放相关的窗口资源。通常放在脚本的最后，或者在用户按下特定退出键后执行，用于清理运行环境。

| 参数名 | 说明 |
| --- | --- |
| 无 | 该函数不需要传入参数。 |

## 图像保存

```
retval = cv2.imwrite(filename, img[, params])
```

> 将处理后的图像数据保存到本地磁盘。函数会根据文件名的后缀（如 `.jpg` 或 `.png`）自动选择编码格式。常用于保存算法处理后的结果图、截图或转换格式后的图片。

| 参数名 | 说明 |
| --- | --- |
| `filename` | 保存的文件路径及名称（需包含后缀）。 |
| `img` | 要保存的图像数据。 |
| `params` | 特定格式的编码参数（可选），如压缩质量。 |

* `retval`

  : 布尔类型，保存成功返回 `True`。
* `params`

  : 针对特定格式的参数。

+ `cv2.IMWRITE_JPEG_QUALITY`

  : JPEG 质量 (0-100)，默认 95。
+ `cv2.IMWRITE_WEBP_QUALITY`

  : WEBP 质量 (0-100)，默认 95。
+ `cv2.IMWRITE_PNG_COMPRESSION`

  : PNG 压缩级别 (0-9)，默认 3。

## 图像加法 (像素求和)

```
result = cv2.add(img1, img2)
```

> 将两张图像的对应像素值进行相加。与 NumPy 的加法不同，OpenCV 的 `add` 是**饱和运算**，即当结果超过 255 时会取 255（白色），而不是取模溢出。常用于图像亮度增强或简单的图像融合。

| 参数名 | 说明 |
| --- | --- |
| `img1` | 第一张输入图像（需与 img2 大小、类型一致）。 |
| `img2` | 第二张输入图像。 |

* 两张图片大小必须一致。
* 这是饱和运算（超过 255 取 255），不同于 NumPy 的模运算。

## 图像混合 (加权加法)

```
dst = cv2.addWeighted(img1, alpha, img2, beta, gamma)
```

> 按照指定的权重（透明度）将两张图像进行融合。公式为 `dst = img1 * alpha + img2 * beta + gamma`。常用于制作水印、图像过渡特效，或者将两张不同曝光的照片合成一张高动态范围（HDR）图像。

| 参数名 | 说明 |
| --- | --- |
| `img1` | 第一张输入图像。 |
| `alpha` | 第一张图像的权重（透明度）。 |
| `img2` | 第二张输入图像。 |
| `beta` | 第二张图像的权重。 |
| `gamma` | 加到总和上的标量值（通常设为 0，用于调节亮度）。 |

## 调整大小\缩放

```
img_resized = cv2.resize(img, dsize, fx, fy, interpolation)
```

> 改变图像的尺寸（放大或缩小）。在深度学习中，常用于将输入图片统一缩放到模型要求的固定尺寸（如 224x224）；在日常处理中，可用于生成缩略图或放大查看细节。

| 参数名 | 说明 |
| --- | --- |
| `img` | 原始输入图像。 |
| `dsize` | 输出图像的尺寸元组 `(宽, 高)`。 |
| `fx` , `fy` | 沿 x 轴和 y 轴缩放的比例因子（若 dsize 为 0 则生效）。 |
| `interpolation` | 插值方法，如 `cv2.INTER_LINEAR`（默认）、`cv2.INTER_AREA`（缩小推荐）。 |

* **常见插值方法**

  :

+ `cv2.INTER_LINEAR`

  : 双线性插值（默认）。
+ `cv2.INTER_NEAREST`

  : 最近邻插值。
+ `cv2.INTER_AREA`

  : 像素区域重采样（适合图像缩小）。
+ `cv2.INTER_CUBIC`

  : 双三次插值。
+ `cv2.INTER_LANCZOS4`

  : Lanczos 插值（8x8 邻域）。

## 图像平移

```
img_shift = cv2.warpAffine(img, M, dsize, flags, borderMode, borderValue)
```

> 将图像在平面内沿水平或垂直方向移动指定的距离。常用于数据增强（增加训练数据的多样性）或图像校正（如将画面中的物体移动到中心位置）。

| 参数名 | 说明 |
| --- | --- |
| `img` | 输入图像。 |
| `M` | 2x3 的变换矩阵，例如 `np.float32([[1, 0, tx], [0, 1, ty]])`，其中 tx, ty 为偏移量。 |
| `dsize` | 输出图像的大小 `(宽, 高)`。 |
| `flags` | 插值方法的组合（如 `cv2.INTER_LINEAR`）。 |
| `borderMode` | 边界像素模式（如 `cv2.BORDER_CONSTANT`）。 |
| `borderValue` | 边界填充值（当 `borderMode` 为 `cv2.BORDER_CONSTANT` 时使用）。 |

## 图像旋转

```
img_rot = cv2.warpAffine(img, M, dsize, flags, borderMode, borderValue)
```

> 根据给定的变换矩阵对图像进行旋转。通常与 `cv2.getRotationMatrix2D` 配合使用，用于图像矫正（如文档扫描后的摆正）或数据增强。

| 参数名 | 说明 |
| --- | --- |
| `img` | 输入图像。 |
| `M` | 由 `getRotationMatrix2D` 生成的 2x3 旋转矩阵。 |
| `dsize` | 输出图像的大小。 |
| `flags` | 插值方法的组合。 |
| `borderMode` | 边界像素模式。 |
| `borderValue` | 边界填充值。 |

## 获取旋转矩阵

```
M = cv2.getRotationMatrix2D(center, angle, scale)
```

> 这是一个辅助函数，用于生成图像旋转所需的 2x3 变换矩阵。它根据指定的中心点、角度和缩放比例计算出矩阵，供 `cv2.warpAffine` 使用。

| 参数名 | 说明 |
| --- | --- |
| `center` | 旋转中心点的坐标 `(x, y)`。 |
| `angle` | 旋转角度（正值表示逆时针旋转）。 |
| `scale` | 各向同性的缩放比例（1.0 表示不缩放）。 |

## 颜色空间转换

```
img_cvt = cv2.cvtColor(img, code, dstCn)
```

> 将图像从一种颜色空间转换到另一种。最常见的用途是将彩色图像转为灰度图（用于边缘检测等算法），或者转为 HSV 空间（用于基于颜色的物体追踪和分割）。

| 参数名 | 说明 |
| --- | --- |
| `img` | 输入图像。 |
| `code` | 颜色转换代码，如 `cv2.COLOR_BGR2GRAY`。 |
| `dstCn` | 目标图像的通道数（默认从 `code` 自动推导）。 |

* `code`

  : 转换标志。

+ `cv2.COLOR_BGR2GRAY`

  : BGR 转灰度。
+ `cv2.COLOR_BGR2HSV`

  : BGR 转 HSV。
+ `cv2.COLOR_BGR2RGB`

  : BGR 转 RGB。

## 图像二值化 (全局阈值)

```
retval, dst = cv2.threshold(src, thresh, maxval, type)
```

> 将灰度图像转换为只有黑白两色的二值图像。如果像素值大于阈值则设为最大值（白），否则设为 0（黑）。常用于 OCR 文字识别前的预处理，或提取物体的轮廓。

| 参数名 | 说明 |
| --- | --- |
| `src` | 输入图像（通常为灰度图）。 |
| `thresh` | 阈值。 |
| `maxval` | 超过阈值时赋予的最大值（通常为 255）。 |
| `type` | 阈值类型（如 `cv2.THRESH_BINARY`）。 |

* `retval`

  : 实际使用的阈值（在 Otsu 算法中有效）。
* `type`

  :

+ `cv2.THRESH_BINARY`

  : 二值化。
+ `cv2.THRESH_BINARY_INV`

  : 反二值化。
+ `cv2.THRESH_TRUNC`

  : 截断。
+ `cv2.THRESH_TOZERO`

  : 低于阈值置零。
+ `cv2.THRESH_TOZERO_INV`

  : 高于阈值置零。

## 自适应阈值

```
dst = cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)
```

> 针对光照不均匀的图像进行二值化。它不是使用全局阈值，而是计算每个像素邻域的局部阈值。常用于处理阴影严重或光照变化大的文档扫描图。

| 参数名 | 说明 |
| --- | --- |
| `src` | 输入灰度图像。 |
| `maxValue` | 赋予满足条件的像素的最大值。 |
| `adaptiveMethod` | 自适应方法（均值或高斯加权）。 |
| `thresholdType` | 阈值类型（必须是二值化或反二值化）。 |
| `blockSize` | 计算阈值的邻域大小（如 11）。 |
| `C` | 从均值或加权均值中减去的常数。 |

* `adaptiveMethod`

  :

+ `cv2.ADAPTIVE_THRESH_MEAN_C`

  : 邻域均值。
+ `cv2.ADAPTIVE_THRESH_GAUSSIAN_C`

  : 邻域高斯加权和。

## 图像腐蚀

```
dst = cv2.erode(src, kernel, anchor, iterations, borderType, borderValue)
```

> 形态学操作之一，用卷积核扫描图像，只有当核内所有像素都为前景（白色）时，中心像素才保留。作用是“腐蚀”掉物体的边缘，常用于去除图像中的小白点噪声，或分离粘连的物体。

| 参数名 | 说明 |
| --- | --- |
| `src` | 输入图像。 |
| `kernel` | 卷积核（结构元素），如 `np.ones((5,5), np.uint8)`。 |
| `anchor` | 锚点位置，默认为 `(-1, -1)` 即核中心。 |
| `iterations` | 迭代次数，即执行腐蚀的次数。 |
| `borderType` | 边界像素模式。 |
| `borderValue` | 边界填充值。 |

* 作用: 使边界向内部侵蚀，消除噪点。

## 图像膨胀

```
dst = cv2.dilate(src, kernel, anchor, iterations, borderType, borderValue)
```

> 与腐蚀相反，只要卷积核覆盖的区域内有一个像素为前景，中心像素就设为前景。作用是扩大物体的白色区域，常用于填补物体内部的小黑洞，或连接断裂的线条。

| 参数名 | 说明 |
| --- | --- |
| `src` | 输入图像。 |
| `kernel` | 卷积核。 |
| `anchor` | 锚点位置。 |
| `iterations` | 迭代次数。 |
| `borderType` | 边界像素模式。 |
| `borderValue` | 边界填充值。 |

* 作用: 使边界向外部扩张。

## 开运算

```
dst = cv2.morphologyEx(src, cv2.MORPH_OPEN, kernel)
```

> 先腐蚀后膨胀的操作。它能有效去除图像外部的小噪点（小白点），同时基本保持原物体的大小和形状不变。常用于二值图像的去噪预处理。

| 参数名 | 说明 |
| --- | --- |
| `src` | 输入图像。 |
| `cv2.MORPH_OPEN` | 形态学操作类型标志。 |
| `kernel` | 卷积核。 |

* 先腐蚀，后膨胀。用于去除噪点。

## 闭运算

```
dst = cv2.morphologyEx(src, cv2.MORPH_CLOSE, kernel)
```

> 先膨胀后腐蚀的操作。它能填充物体内部的小黑洞或前景物体上的小孔，也可以连接邻近的断裂处。常用于修复有缺损的文字或图案。

| 参数名 | 说明 |
| --- | --- |
| `src` | 输入图像。 |
| `cv2.MORPH_CLOSE` | 形态学操作类型标志。 |
| `kernel` | 卷积核。 |

* 先膨胀，后腐蚀。用于填充空洞。

## 梯度运算

```
dst = cv2.morphologyEx(src, cv2.MORPH_GRADIENT, kernel)
```

> 膨胀图与腐蚀图之差。该操作会保留物体的边缘轮廓，去除内部填充，结果看起来像物体的轮廓素描。常用于提取物体的边缘信息。

| 参数名 | 说明 |
| --- | --- |
| `src` | 输入图像。 |
| `cv2.MORPH_GRADIENT` | 形态学操作类型标志。 |
| `kernel` | 卷积核。 |

* 膨胀图与腐蚀图之差，提取边缘。

## 顶帽运算

```
dst = cv2.morphologyEx(src, cv2.MORPH_TOPHAT, kernel)
```

> 原始图像与开运算结果之差。因为开运算会去除细小的亮斑，所以顶帽运算的结果就是这些被去除的亮斑。常用于分离比邻近点亮一些的斑块，或进行不均匀光照下的背景提取。

| 参数名 | 说明 |
| --- | --- |
| `src` | 输入图像。 |
| `cv2.MORPH_TOPHAT` | 形态学操作类型标志。 |
|...