---
title: AI风控之伪造视频检测
url: https://forum.butian.net/share/3131
source: 奇安信攻防社区
date: 2024-07-23
fetch_date: 2025-10-06T17:38:27.030629
---

# AI风控之伪造视频检测

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### AI风控之伪造视频检测

* [安全工具](https://forum.butian.net/topic/53)

Deepfake技术是一种利用人工智能深度学习算法生成虚假内容的手段。通过训练模型识别和模仿特定人物的面部特征、声音甚至行为方式，Deepfake可以合成出极为逼真的虚假视频或音频。这种技术的关键在于其高度的欺骗性，使得辨别真伪变得异常困难。

前言
==
Deepfake技术是一种利用人工智能深度学习算法生成虚假内容的手段。通过训练模型识别和模仿特定人物的面部特征、声音甚至行为方式，Deepfake可以合成出极为逼真的虚假视频或音频。这种技术的关键在于其高度的欺骗性，使得辨别真伪变得异常困难。
Deepfake伪造视频对社会的影响是多方面的。它严重侵犯了个人隐私权，通过伪造他人形象进行不实传播，给被伪造者带来名誉损害和精神压力。Deepfake在政治领域的影响尤为显著，它可以被用来制造假新闻，篡改公众对事件的看法，甚至影响选举结果。此外，Deepfake还可能被用于商业欺诈，通过伪造高管访谈等手段误导投资者，造成经济损失。
![image-20240621093621443.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-db2406954dd06c76d45b2f4168768693d84520d0.png)
![image-20240621093344359.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-19fcb5b2700d85655bc0fc1d9269eebcf26a4bd6.png)
因此在风控等场合下如何有效对deepfake伪造视频进行有效鉴伪就是急需解决的事情。本文就来分享一个简单有效的方案。
背景知识
====
在实战之前，我们先来补一下背景知识
deepfake
--------
Deepfake技术的核心原理是利用生成对抗网络（GAN）或卷积神经网络（CNN）等算法将目标对象的面部“嫁接”到被模仿对象上。由于视频是连续的图片组成，因此只需要把每一张图片中的脸替换，就能得到变脸的新视频。具体而言，首先将模仿对象的视频逐帧转化成大量图片，然后将目标模仿对象面部替换成目标对象面部。最后，将替换完成的图片重新合成为假视频，而深度学习技术可以使这一过程实现自动化。
![image-20240621093749221.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-9e4ee14d767192b933879e7a29d8e3d1f6829a12.png)
脸部交换是一种常见的类型。最流行的包含假视频和真实视频的数据库是FaceForensics++。该数据集中的假视频是使用计算机图形学（FaceSwap）和深度学习方法（DeepFake FaceSwap）制作的。FaceSwap应用程序是用Python编写的，它使用面部对齐、高斯-牛顿优化和图像混合技术，将摄像头看到的人脸与提供图像中的人脸进行交换。DeepFake FaceSwap方法基于两个具有共享编码器的自动编码器，分别训练重建源脸和目标脸的训练图像。目标序列中的人脸被替换为在源视频或图像集中观察到的人脸。使用人脸检测器裁剪并对齐图像。为了创建假图像，应用源脸的训练编码器和解码器到目标脸上。然后，自动编码器的输出与图像的其余部分使用泊松图像编辑进行混合。具体效果如下所示
![image-20240621093812803.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-a404e1342398ab02efbb2b86eff00300920cc5c5.png)
也可以实现表情操纵，包括修改面部的属性，例如头发或皮肤的颜色、年龄、性别，以及使面部表现出高兴、悲伤或愤怒的表情。最流行的例子是最近推出的FaceApp移动应用程序。这些方法大多数采用生成对抗网络（GANs）进行图像到图像的转换。下图就是一个示例
![image-20240621094052345.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-17fe2981827f7236997cf9ba33a949828ec73987.png)
如下就是其中用到的StarGAN的结构
![image-20240621094126012.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-03316d667b9d2545032f4ad29747f51e7ac542e5.png)
StarGAN由鉴别器D和生成器G组成。鉴别器试图预测输入图像是假的还是真实的，并将真实图像分类到其对应的域。生成器接受图像和目标域标签作为输入，并生成一个假图像。目标域标签在空间上复制并与输入图像连接。然后，生成器试图根据原始域标签从假图像重构出原始图像。最后，生成器G努力生成与真实图像无法区分且能够被鉴别器分类为目标域的图像。
实战
==
数据分析
----
首先统计我们目前手头的给定文件夹中的训练样本和测试样本的数量
```php
DATA\_FOLDER = 'deepfake'
TRAIN\_SAMPLE\_FOLDER = 'train\_sample\_videos'
TEST\_FOLDER = 'test\_videos'
print(f"Train samples: {len(os.listdir(os.path.join(DATA\_FOLDER, TRAIN\_SAMPLE\_FOLDER)))}")
print(f"Test samples: {len(os.listdir(os.path.join(DATA\_FOLDER, TEST\_FOLDER)))}")
```
1. `DATA\_FOLDER = '../input/deepfake-detection-challenge'`：定义一个变量`DATA\_FOLDER`，其值为字符串`'../input/deepfake-detection-challenge'`。这个值表示数据集的根目录。
2. `TRAIN\_SAMPLE\_FOLDER = 'train\_sample\_videos'`：定义一个变量`TRAIN\_SAMPLE\_FOLDER`，其值为字符串`'train\_sample\_videos'`。这个值表示存储训练样本视频的子目录名称。
3. `TEST\_FOLDER = 'test\_videos'`：定义一个变量`TEST\_FOLDER`，其值为字符串`'test\_videos'`。这个值表示存储测试样本视频的子目录名称。
4. `print(f"Train samples: {len(os.listdir(os.path.join(DATA\_FOLDER, TRAIN\_SAMPLE\_FOLDER)))}")`：这行代码首先使用`os.path.join()`函数将`DATA\_FOLDER`和`TRAIN\_SAMPLE\_FOLDER`两个变量的值拼接起来，得到训练样本视频的绝对路径。然后使用`os.listdir()`函数获取该路径下的所有文件和子目录列表。最后，使用`len()`函数计算列表的长度，即训练样本的数量，并通过格式化字符串（f-string）在控制台输出结果。
5. `print(f"Test samples: {len(os.listdir(os.path.join(DATA\_FOLDER, TEST\_FOLDER)))}")`：这行代码的逻辑与第4行代码类似，只是将`TRAIN\_SAMPLE\_FOLDER`替换为`TEST\_FOLDER`，用于计算并输出测试样本的数量。
执行后如下所示
![image-20240621090623957.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-a37077e342ad04452c72cc21f595599debdf8a4b.png)
读取训练样本的元数据信息，并将其存储在一个Pandas DataFrame中
```php
train\_sample\_metadata = pd.read\_json('../input/deepfake-detection-challenge/train\_sample\_videos/metadata.json').T
train\_sample\_metadata.head()：
```
1. `train\_sample\_metadata = pd.read\_json('../input/deepfake-detection-challenge/train\_sample\_videos/metadata.json').T`：这行代码使用Pandas库的`read\_json()`函数从指定的JSON文件中读取数据。文件路径是`'../input/deepfake-detection-challenge/train\_sample\_videos/metadata.json'`，这是训练样本视频元数据的存储位置。`.T`操作是对读取到的DataFrame进行转置，使得原本的列名成为索引。
2. `train\_sample\_metadata.head()`：这行代码调用Pandas DataFrame的`head()`方法，显示DataFrame的前几行（默认为前5行）。这有助于查看元数据的大致结构和内容。
从JSON文件中读取训练样本的元数据信息，并将其存储在一个Pandas DataFrame中。接着，它会显示这个DataFrame的前几行，以便我们查看元数据的结构和内容
```php
train\_sample\_metadata = pd.read\_json('deepfake/train\_sample\_videos/metadata.json').T
train\_sample\_metadata.head()
```
执行后如下所示
![image-20240621090927991.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-a5f070a18a244e36ed3308a017cce99a2489fd4d.png)
对训练样本的标签进行分组统计，并绘制一个柱状图来展示训练集中各个标签的分布情况
```php
train\_sample\_metadata.groupby('label')['label'].count().plot(figsize=(15, 5), kind='bar', title='Distribution of Labels in the Training Set')
plt.show()
```
执行后如下所示
![image-20240621091014551.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-908091e220a7a13845264a83f1c3e957a6dc7db7.png)
```php
train\_sample\_metadata.shape
```
`train\_sample\_metadata.shape` 是一个Pandas DataFrame属性，它返回一个包含两个元素的元组，分别表示DataFrame的行数和列数。在这个例子中，`train\_sample\_metadata` 是从训练样本的元数据JSON文件中读取的数据。
从训练样本的元数据中随机选取3个标签为'FAKE'的样本，并获取它们的索引（即文件名）
```php
fake\_train\_sample\_video = list(train\_sample\_metadata.loc[train\_sample\_metadata.label=='FAKE'].sample(3).index)
fake\_train\_sample\_video
```
执行后如下所示
![image-20240621091142557.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-38edb7e7764e4532e3fbffecf12def139d8c520d.png)
定义一个名为`display\_image\_from\_video`的函数，它接受一个参数`video\_path`，表示视频文件的路径。函数的目的是从给定的视频中捕获一帧图像，并在matplotlib图中显示该图像
```php
def display\_image\_from\_video(video\_path):
capture\_image = cv2.VideoCapture(video\_path)
ret, frame = capture\_image.read()
fig = plt.figure(figsize=(10,10))
ax = fig.add\_subplot(111)
frame = cv2.cvtColor(frame, cv2.COLOR\_BGR2RGB)
ax.imshow(frame)
```
![image-20240621091236527.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-e6e21d1957e21ce593fdf16ef3a5fe7ad7985245.png)
执行后如下所示
![image-20240621091258723.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-4d9fd9838ac877ac13b4eb4516bb371087f6bb11.png)
以上是伪造的视频，再来看看真实的视频
![image-20240621091356682.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-e28f3f8438f19df981599d4d40541f835fc4a41b.png)
执行后如下所示
![image-20240621091417585.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-83d1e8e22c03d7488794a98492bcbd06195722da.png)
以上就是真实的视频
统计训练样本元数据中'original'列的值的出现次数，并显示出现次数最多的前5个值
```php
train\_sample\_metadata['original'].value\_counts()[0:5]
```
定义一个名为`display\_image\_from\_video\_list`的函数，它接受两个参数：`video\_path\_list`（一个包含视频文件名的列表）和`video\_folder`（视频文件所在的文件夹，默认值为`TRAIN\_SAMPLE\_FOLDER`）。函数的目的是遍历给定的视频文件名列表，从每个视频中捕获一帧图像，并在matplotlib图中显示这些图像
```php
def display\_image\_from\_video\_list(video\_path\_list, video\_folder=TRAIN\_SAMPLE\_FOLDER):
plt.figure()
fig, ax = plt.subplots(2,3,figsize=(16,8))
for i, video\_file in enumerate(video\_path\_list[0:6]):
video\_path = os.path.join(DATA\_FOLDER, video\_folder,video\_file)
capture\_image = cv2.VideoCapture(video\_path)
ret, frame = capture\_image.read()
frame = cv2.cvtColor(frame, cv2.COLOR\_BGR2RGB)
ax[i//3, i%3].imshow(frame)
ax[i//3, i%3].set\_title(f"Video: {video\_file}")
ax[i//3, i%3].axis('on')
```
首先从训练样本的元数据中...