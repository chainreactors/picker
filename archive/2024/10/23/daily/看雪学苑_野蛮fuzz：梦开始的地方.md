---
title: 野蛮fuzz：梦开始的地方
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458578912&idx=2&sn=816a4aeedfd3e1eef7d17deea7fa9681&chksm=b18ddf6a86fa567c9b9bcde9916d481dba67cb7b23a9d53e88aa5c10a949cb0fa77aeaed8c6a&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-10-23
fetch_date: 2025-10-06T18:52:43.644676
---

# 野蛮fuzz：梦开始的地方

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EBegp1g8icpID4s0Iq8zYMHrsRibGcVzzoj2icwmHBFYEZSKUFuUKAf6JzicjXpLUm9JWGkU2cMeWH0w/0?wx_fmt=jpeg)

# 野蛮fuzz：梦开始的地方

pureGavin【译】

看雪学苑

# 介绍

在过去的几个月里，我一直在被动地吸收大量与模糊测试相关的材料，因为我主要尝试将我的 Windows 利用技能从菜鸟级别提升到略微高级的水平，我发现它非常有趣。在这篇文章中，我将向你展示如何创建一个非常简单的变异模糊测试器，并希望我们能用它在一些开源项目中找到一些崩溃。

我们将要创建的模糊测试器是通过跟随@gynvael在YouTube 上的模糊测试教程来实现的。我之前不知道 Gynvael 有视频流，现在我有了更多的内容可以添加到永无止境的观看/阅读列表中。

我还必须提到Brandon Faulk的模糊测试视频流非常棒。我大约不理解 Brandon 所说的 99% 的内容，但这些视频流非常吸引人。我个人最喜欢的是他对`calc.exe`和`c-tags`的模糊测试。他还有一个非常棒的模糊测试概念介绍视频：NYU Fuzzing Talk。

# 选择一个目标

我想找到一个用 C 或 C++ 编写并从文件中解析数据的二进制文件。我首先接触到的是解析图像中 Exif 数据的二进制文件。我们还希望选择一个几乎没有安全隐患的目标，因为我会实时发布这些发现。

根据`https://www.media.mit.edu/pia/Research/deepview/exif.html`的描述：基本上，Exif 文件格式与 JPEG 文件格式相同。Exif 根据 JPEG 规范将一些图像/数码相机信息数据和缩略图图像插入到 JPEG 中。因此，你可以像查看普通 JPEG 图像文件一样，通过符合 JPEG 规范的互联网浏览器/图片查看器/照片修饰软件等查看 Exif 格式图像文件。

所以，Exif 根据 JPEG 规范将元数据类型信息插入到图像中，并且有很多程序/工具可以解析这些数据。

# 开始

我们将使用 Python3 构建一个基本的变异模糊测试器，它会微妙地（或不那么微妙地）修改有效的包含 Exif 的 JPEG，并将其提供给解析器，希望引发崩溃。我们还将在 x86 Kali Linux 发行版上进行操作。

首先，我们需要一个有效的包含 Exif 的 JPEG。谷歌搜索“带有 Exif 的样本 JPEG”会将我们引导到这个仓库。我将使用`Canon_40D.jpg`图像进行测试。

## 了解 JPEG 和 EXIF 规范

在我们开始随便在 Sublime Text 中编写 Python 之前，让我们先花点时间了解 JPEG 和 Exif 规范，这样我们可以避免一些更明显的陷阱，比如将图像损坏到解析器不尝试解析它并浪费宝贵的模糊测试周期。

从之前引用的规范概述中可以知道，所有 JPEG 图像都以字节值`0xFFD8`开头，以字节值`0xFFD9`结尾。这前几个字节被称为“magic bytes”。这使得在 \*Nix 系统上可以直接进行文件类型识别。

```
root@kali:~# file Canon_40D.jpg
Canon_40D.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 72x72, segment length 16, Exif Standard: [TIFF image data, little-endian, direntries=11, manufacturer=Canon, model=Canon EOS 40D, orientation=upper-left, xresolution=166, yresolution=174, resolutionunit=2, software=GIMP 2.4.5, datetime=2008:07:31 10:38:11, GPS-Data], baseline, precision 8, 100x68, components 3
```

我们可以去掉`.jpg`扩展名，得到相同的输出。

```
root@kali:~# file Canon
Canon: JPEG image data, JFIF standard 1.01, resolution (DPI), density 72x72, segment length 16, Exif Standard: [TIFF image data, little-endian, direntries=11, manufacturer=Canon, model=Canon EOS 40D, orientation=upper-left, xresolution=166, yresolution=174, resolutionunit=2, software=GIMP 2.4.5, datetime=2008:07:31 10:38:11, GPS-Data], baseline, precision 8, 100x68, components 3
```

如果我们对图像进行十六进制转储，可以看到第一个和最后一个字节实际上是`0xFFD8`和`0xFFD9`。

```
root@kali:~# hexdump Canon
0000000 d8ff e0ff 1000 464a 4649 0100 0101 4800
------SNIP------
0001f10 5aed 5158 d9ff
```

在规范概述中，另一个有趣的信息是“标记”以 0xFF 开头。有几个已知的静态标记，例如：

◆“图像开始”（SOI）标记：`0xFFD8`

◆APP1 标记：`0xFFE1`

◆通用标记：`0xFFXX`

◆“图像结束”（EOI）标记：`0xFFD9`

由于我们不想更改图像长度或文件类型，让我们尽量保持 SOI 和 EOI 标记不变。例如，我们不希望在图像中间插入`0xFFD9`，因为这会截断图像或导致解析器以非崩溃的方式出现异常。“非崩溃”是一个真实的词。此外，这样的做法可能是错误的，也许我们应该随机地在字节流中插入 EOI 标记？让我们看看。

## 启动我们的模糊测试器

我们首先需要做的是从我们要用作“有效”输入样本的 JPEG 中提取所有字节，当然我们会对其进行变异。

我们的代码将如下开始：

```
#!/usr/bin/env python3
import sys

# read bytes from our valid JPEG and return them in a mutable bytearray
def get_bytes(filename):

    f = open(filename, "rb").read()

    return bytearray(f)

if len(sys.argv) < 2:
    print("Usage: JPEGfuzz.py <valid_jpg>")

else:
    filename = sys.argv[1]
    data = get_bytes(filename)
```

如果我们想看看这些数据的样子，可以打印数组中的前 10 个左右的字节值，看看我们将如何与它们交互。我们可以临时添加类似以下的代码：

```
else:
    filename = sys.argv[1]
    data = get_bytes(filename)
    counter = 0
    for x in data:
        if counter < 10:
            print(x)
        counter += 1
```

运行这段代码显示我们在处理整齐转换的十进制整数，这让我觉得一切都变得更加容易。

```
root@kali:~# python3 fuzzer.py Canon_40D.jpg
255
216
255
224
0
16
74
70
73
70
```

让我们快速验证一下是否可以从我们的字节数组创建一个新的有效 JPEG 文件。我们会将这个函数添加到代码中并运行它。

```
def create_new(data):    f = open("mutated.jpg", "wb+")
    f.write(data)
    f.close()
```

现在我们在目录中有了一个`mutated.jpg`文件，让我们对两个文件进行哈希处理，看看它们是否匹配。

```
root@kali:~# shasum Canon_40D.jpg mutated.jpg
c3d98686223ad69ea29c811aaab35d343ff1ae9e  Canon_40D.jpg
c3d98686223ad69ea29c811aaab35d343ff1ae9e  mutated.jpg
```

太棒了，我们有两个相同的文件。现在我们可以在创建`mutated.jpg`之前开始变异数据了。

### 变异

我们将保持我们的模糊测试器相对简单，并只实现两种不同的变异方法。这些方法是：

◆位翻转

◆用 Gynvael 的“Magic Numbers”覆盖字节序列

让我们从位翻转开始。`255`（或`0xFF`）在二进制中是`11111111`，如果我们随机翻转这个数字中的一个位，例如在索引号 2 处，我们会得到`11011111`。这个新数字将是`223`或`0xDF`。

我不完全确定这种变异方法与从`0`到`255`随机选择一个值并用它覆盖一个随机字节有多大的不同。我的直觉告诉我，位翻转与随机用任意字节覆盖字节非常相似。

让我们假设我们只想在 1% 的字节中翻转一个位。我们可以在 Python 中通过以下方式得到这个数字：

```
num_of_flips = int((len(data) - 4) * .01)
```

我们希望从 bytearray 的长度中减去 4，因为我们不希望计算数组中的前 2 个字节或最后 2 个字节，因为它们是 SOI 和 EOI 标记，我们希望保持这些标记不变。

接下来，我们需要随机选择这么多的索引，并针对这些索引进行位翻转。我们将创建一个可以更改的可能索引范围，然后选择`num_of_flips`个索引进行随机位翻转。

```
indexes = range(4, (len(data) - 4))

chosen_indexes = []

# iterate selecting indexes until we've hit our num_of_flips number
counter = 0
while counter < num_of_flips:
    chosen_indexes.append(random.choice(indexes))
    counter += 1
```

让我们在脚本中添加`import random`，并添加这些调试打印语句，以确保一切正常工作。

```
print("Number of indexes chosen: " + str(len(chosen_indexes)))
print("Indexes chosen: " + str(chosen_indexes))
```

我们现在的函数看起来像这样：

```
def bit_flip(data):

    num_of_flips = int((len(data) - 4) * .01)

    indexes = range(4, (len(data) - 4))

    chosen_indexes = []

    # iterate selecting indexes until we've hit our num_of_flips number
    counter = 0
    while counter < num_of_flips:
        chosen_indexes.append(random.choice(indexes))
        counter += 1

    print("Number of indexes chosen: " + str(len(chosen_indexes)))
    print("Indexes chosen: " + str(chosen_indexes))
```

如果我们运行这个函数，我们会得到一个预期的漂亮输出：

```
root@kali:~# python3 fuzzer.py Canon_40D.jpg
Number of indexes chosen: 79
Indexes chosen: [6580, 930, 6849, 6007, 5020, 33, 474, 4051, 7722, 5393, 3540, 54, 5290, 2106, 2544, 1786, 5969, 5211, 2256, 510, 7147, 3370, 625, 5845, 2082, 2451, 7500, 3672, 2736, 2462, 5395, 7942, 2392, 1201, 3274, 7629, 5119, 1977, 2986, 7590, 1633, 4598, 1834, 445, 481, 7823, 7708, 6840, 1596, 5212, 4277, 3894, 2860, 2912, 6755, 3557, 3535, 3745, 1780, 252, 6128, 7187, 500, 1051, 4372, 5138, 3305, 872, 6258, 2136, 3486, 5600, 651, 1624, 4368, 7076, 1802, 2335, 3553]
```

接下来我们需要实际对这些索引处的字节进行变异。我们需要对它们进行位翻转。我选择了一种非常简单的方法来实现这一点，您可以自由实现自己的解决方案。我们将把这些索引处的字节转换为二进制字符串，并填充它们，使其长度为 8 位。让我们添加这段代码，看看我在说什么。我们将把字节值（记住是十进制的）转换为二进制字符串，然后如果长度小于 8 位，则用前导零填充。最后一行是用于调试的临时打印语句。

```
for x in chosen_indexes:
        current = data[x]
        current = (bin(current).replace("0b",""))
        current = "0" * (8 - len(current)) + current
```

如您所见，我们得到了漂亮的二进制数字字符串输出。

```
root@kali:~# python3 fuzzer.py Canon_40D.jpg
10100110
10111110
10010010
00110000
01110001
00110101
00110010
-----SNIP-----
```

现在对于每一个，我们将随机选择一个索引并翻转它。以第一个`10100110`为例，如果选择索引 0，我们有一个`1`，我们将其翻转为`0`。

最后要考虑的是，这些是字符串而不是整数。所以我们需要做的最后一件事是将翻转后的二进制字符串转换为整数。

我们将创建一个空列表，将每个数字添加到列表中，翻转我们随机选择的数字，然后从所有列表成员构造一个新的字符串。（我们必须使用这个中间列表步骤，因为字符串是不可变的）。最后，我们将其转换为整数，并将数据返回到我们的`create_new()`函数，以创建一个新的 JPEG。

我们的脚本现在总体上看起来是这样的：

```
#!/usr/bin/env python3

import sys
import random

# read bytes from our valid JPEG and return them in a mutable bytearray
def get_bytes(filename):

    f = open(filename, "rb").read()

    return bytearray(f)

def bit_flip(data):

    num_of_flips = int((len(data) - 4) * .01)

    indexes = range(4, (len(data) - 4))

    chosen_indexes = []

    # iterate selecting indexes until we've hit our num_of_flips number
    counter = 0
    while counter < num_of_flips:
        chosen_indexes.append(random.choice(indexes))
        counter += 1

    for x in chosen_indexes:
        current = data[x]
        current = (bin(current).replace("0b",""))
        current = "0" * (8 - len(current)) + current

        indexes = range(0,8)

        picked_index = random.choice(indexes)

        new_number = []

        # our new_number list now has all the digits, example: ['1', '0', '1', '0', '1', '0', '1', '0']
        for i in current:
            new_number.append(i)

        # if the number at our randomly selected index is a 1, make it a 0, and vice versa
        if new_number[picked_index] == "1":
            new_number[picked_index] = "0"
        else:
            new_number[picked_index] = "1"

        # create our new bin...