---
title: Swift 逆向——授人以鱼不如授人以渔
url: https://mp.weixin.qq.com/s/M2IR_WdWWKTOGhMkXDPH7w
source: Doonsec's feed
date: 2026-01-16
fetch_date: 2026-01-17T03:25:58.493390
---

# Swift 逆向——授人以鱼不如授人以渔

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EhX3LXAfz6BiaBJjnTttFFFHYXGWxX8gkcC4KghYn9Eic3ibbt0RBaTqNLLZfOZc3ZgrQGiaibqNiazPag/0?wx_fmt=jpeg)

# Swift 逆向——授人以鱼不如授人以渔

αβγδεξπ
αβγδεξπ

看雪学苑

![]()

在小说阅读器中沉浸阅读

**01**

**Swift String 底层原理**

# Swift 源码地址https://github.com/swiftlang/swift/tree/main/stdlib/public/core

Mems 工具下载地址

https://github.com/CoderMJLee/Mems/tree/master

笔者将从 Swift String 的底层原理切入，循序渐进地带大家走进 Swift 逆向的世界，逐步理解其核心逻辑与实践思路。

## 空字符串

首先打开 XCode 创建一个 Swift 项目，然后在入口类的构造函数中添加如下代码，并且点击 序号 15 打上断点。

![QQ_1765422459209](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EhX3LXAfz6BiaBJjnTttFFFnN0UBZzzT9DIHTTRc3cLrPqm7avcjWSnevQcdsRfYiaIcw6MqicRywwA/640?wx_fmt=png&from=appmsg)

随后点击运行，会自动卡在断点处，然后点击步过

![QQ_1765422562768](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EhX3LXAfz6BiaBJjnTttFFFxvGfFJn8UY7WSxhGRtkKDPxAT24dHic17L5oNiay8Ms81CCXaWLTMoAg/640?wx_fmt=png&from=appmsg)![]()![]()

随后可以看到 Swift String 的内部结构了。

![QQ_1765422605874](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EhX3LXAfz6BiaBJjnTttFFFOILPj6GA18C8jeIrJ6T7Q4XHxnSLX2hWrdL2xbLabqylynz6TOiaeDg/640?wx_fmt=png&from=appmsg)![]()![]()

接下来打开 Swift 源码

### （1）在 String.swift 中检索 "struct String"

![QQ_1765419592151](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EhX3LXAfz6BiaBJjnTttFFFBIiaU1m9VLemRkQhZDibzu3GQsZ61xWdzUYwYb2KymwHzOgo6hBWY3Yw/640?wx_fmt=png&from=appmsg)![]()![]()

可以看到`String`结构体的构造函数中接收了一个`_StringGuts`对象，继续跟进`_StringGuts`结构体

### （2）在 StringGuts.swift 中检索 "\_StringGuts"

![QQ_1765419705917](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EhX3LXAfz6BiaBJjnTttFFF2RvSiaeFnbvBUbuGvDXt2yictia1RJIaicS1KetW5ey0OWrKdicZC6QZSzQ/640?wx_fmt=png&from=appmsg)![]()![]()

阅读源码后可以发现`_StringGuts`结构体的构造函数接收了一个`_StringObject`对象，并且这个`_StringObject`对象是通过传入`empty`参数进行构造的，所以等会可以检索**"init(empty"**来定位`_StringObject`的构造函数。

### （3）在 StringObject.swift 中检索 "init(empty"

![QQ_1765419759238](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EhX3LXAfz6BiaBJjnTttFFFgPBhETRKFKfdnr85bqqUoBIoViaoPmYNbQUicfKTVBd7K6vdvayoGRBw/640?wx_fmt=png&from=appmsg)![]()![]()

该私有构造函数中，根据不同平台的**指针位宽**（64/32/16 位）适配空字符串的底层内存布局，保证空字符串在所有平台下的内存表示一致。

**（3.1）`_pointerBitWidth`编译条件**

`_pointerBitWidth(_64)`：Swift 编译器内置的私有编译标记，判断当前平台是否为**64 位架构**（如 arm64/iOS、x86\_64/macOS）；

`_pointerBitWidth(_32)`/`_16`：对应 32 位 / 16 位架构（极少用，如老旧的 armv7 设备、嵌入式平台）；

**（3.2）64 位下的代码逻辑**

```
self._countAndFlagsBits = 0
self._object = Builtin.valueToBridgeObject(Nibbles.emptyString._value)
```

先明确 Swift`String`的底层核心字段

| 字段 | 作用 |
| --- | --- |
| `_countAndFlagsBits` | 存储字符串长度 + 标志位（如是否为小字符串、是否 ASCII 编码），64 位下占 8 字节 |
| `_object` | 指向字符串底层存储的桥接对象指针（64 位下占 8 字节，对应 C++ 的`void*`） |

`_countAndFlagsBits = 0`：空字符串长度为 0，所有标志位清零；

`Builtin.valueToBridgeObject`：Swift 内置（Builtin）函数，将「空字符串的静态内存地址」转换为桥接对象指针（`_object`）；

`Nibbles.emptyString`：Swift 标准库中预定义的「空字符串常量」（全局唯一，避免重复创建空字符串实例，类比 C++ 的`std::string::empty()`优化）。

`Nibbles`是个枚举，源码中给它加了多个`extension`。进一步查看源码可以看到`Nibbles.emptyString`，调用方法：`small(isASCII: Bool)`

![QQ_1765436959302](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EhX3LXAfz6BiaBJjnTttFFF6bDutSwsjymtA80mZx4ibcwE9pmSGm5uibw6domyeMfX9rmvtRqET6ww/640?wx_fmt=png&from=appmsg)![]()![]()

通过调试也可以发现存储的地址是`0xe000000000000000`

![QQ_1765422773012](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EhX3LXAfz6BiaBJjnTttFFFEEx4VSCcx0egiahibd6Wp3NmuTxPdSXzjChricqs2owbhshT5psoerEqg/640?wx_fmt=png&from=appmsg)![]()![]()

**64 位平台设计逻辑**

空字符串无需动态分配内存，直接复用全局唯一的`emptyString`静态地址，`_object`指向该地址，`_countAndFlagsBits`置 0，实现极致的内存效率（无堆分配）。

**（3.3）32 位下的代码逻辑**

在`StringObject.swift`文件下检索`init(count:`，可以看到 32 位下调用的构造函数，因为通常是 64位，故 32位不做分析，感兴趣的可以自行了解。

![QQ_1765420132253](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EhX3LXAfz6BiaBJjnTttFFFMwdtAlT6SS2nJEbIXlEFIibgQYjrGQddiboIQFDAVsHHprRolSmEo1aw/640?wx_fmt=png&from=appmsg)![]()![]()

### （4）小结

经过上面的分析，可以知道一个字符串变量至少占用了16字节。用`MemoryLayout`工具进行验证也确实是16个字节。

![QQ_1765437667976](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EhX3LXAfz6BiaBJjnTttFFFpbmqERohia1N7AibuBUoU9RhYy0T66VSTGsQxEPIefS8hdT9ldNIsLicA/640?wx_fmt=png&from=appmsg)![]()![]()

## 非空字符串

### 小字符串

已知字符串变量至少占用 16个字节，那么在内存中是什么样的呢？

### （1）查看小字符串的内存

首先前往[Mems]下载 或者直接从Mems.zip中解压得到  Mems.swift 文件，然后导入到项目中，最后键入下面的代码。

```
func show<T>(val: inout T) {
print("-------------- \(type(of: val)) --------------")
print("变量的地址:", Mems.ptr(ofVal: &val))
print("变量的内存:", Mems.memStr(ofVal: &val))
print("变量的大小:", Mems.size(ofVal: &val))
print("")
}

func show<T>(ref: T) {
print("-------------- \(type(of: ref)) --------------")
print("对象的地址:", Mems.ptr(ofRef: ref))
print("对象的内存:", Mems.memStr(ofRef: ref))
print("对象的大小:", Mems.size(ofRef: ref))
print("")
}

@main
struct SwiftDemoApp: App {

init(){
var str ="1"
print("字符串："\(str)"")
print("字符串所占字节数：\(MemoryLayout.size(ofValue: str))")
        show(val: &str)
    }

var body: some Scene {
WindowGroup {
ContentView()
        }
    }
}
```

上面的程序运行后可以得到下面的结果

![QQ_1765439113226](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EhX3LXAfz6BiaBJjnTttFFFW1ZxH1jpAYAcUC9V872LDHIeQF1aIicRp3cPlahVF4Lr9tibLxdpSEHA/640?wx_fmt=png&from=appmsg)![]()![]()

### （2）进一步验证

空字符串的`_object = 0xe000000000000000`，字符串 "1" 的`_object = 0xe100000000000000`，据此可合理推测，`e`后四位的十六进制数值用于存储小字符串的长度，接下来将对此展开进一步验证。

查看字符串 "123" 的内存

![QQ_1765439779485](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EhX3LXAfz6BiaBJjnTttFFFiaYYLLRhSkglwpjfRK21ct1micKbV1sRA6pU9TfegFwGucRSnAqWyX2g/640?wx_fmt=png&from=appmsg)![]()![]()

查看字符串 "0123456789ABCDE" 的内存

![QQ_1765439849837](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EhX3LXAfz6BiaBJjnTttFFF5f3AJh9qalhYZVicibYrL0QJGicqctxVvicyfHkd05Mq4ibCx9kicCLcc96g/640?wx_fmt=png&from=appmsg)![]()![]()

查看字符串 "0123456789ABCDEF" 的内存

![QQ_1765440096654](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EhX3LXAfz6BiaBJjnTttFFFia8NGfkIBTVVvbE90lGhFDibCYNloUibZJwl0ibMcCRlmmgkicrXDVC7R0A/640?wx_fmt=png&from=appmsg)![]()![]()

###

### （3）小结

字符串长度小于 16 时，e 后的4位用于表示字符串长度，并且字符串内容存储在另外 15 个字节中。

### 大字符串

### （1）查看大字符串的内存

![QQ_1765442903546](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EhX3LXAfz6BiaBJjnTttFFF8xDAKxiaxlVUcS7IMVAAugQYPCbBzYzYlF098OpqntRej1xqcI14U0A/640?wx_fmt=png&from=appmsg)![]()![]()

### （2）进一步验证

通过对比`"0123456789ABCDEFG"`与`"0123456789ABCDEF"`的内存数据可推测，字符串长度不再存储于`_object`中，而是由`_countAndFlagsBits`字段存储；而`_object`中记录的地址偏移`0x20`后，即为字符串的实际内存地址。

查看字符串 "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" 的内存。

![QQ_1765443276529](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EhX3LXAfz6BiaBJjnTttFFF9iaZKNkR9HGZr1hIQYqRaQCxbCRBCbdKJE6jmk6lXwYs7HOuiazda1dw/640?wx_fmt=png&from=appmsg)![]()![]()

查看字符串 "泥嚎，我正在分析 swift string！" 的内存

![QQ_1765443744257](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EhX3LXAfz6BiaBJjnTttFFFtUaBw4uj35jaT5RkFmocfvozRgWAktzmNiaibUtXw3vHeatw5XyzfMDA/640?wx_fmt=png&from=appmsg)![]()![]()

![QQ_1765443697548](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EhX3LXAfz6BiaBJjnTttFFFV5GWoEeMvUGicYI40zMWNRc9OiavmVgV05bk4aH4geTFkbxwKN2JGiasw/640?wx_fmt=png&from=appmsg)![]()![]()

### （3）小结

大字符串的`_object`存储的是字符串的内存地址，偏移 0x20 就可以读取到字符串内容。

**0****2**

**测试环境**

测试环境分为**[ Swift 源码 ]**、**[ 项目源码 ]**和 一个**[ IPA 文件 ]**，Swift 源码和项目源码用来理解 Swift 底层结构，ipa 文件用来辅助分析。

## 项目源码

[SwiftDemo.zip]

## IPA 安装

连接上**iPhone**，打开**爱思助手**，然后按照下面的步骤操作。当然，如果你有**巨魔**，就可以跳过这个地方了。

![QQ_1765961203314](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EhX3LXAfz6BiaBJjnTttFFF8yx6Lv0My6rVRdsZk99PZEVcVIKY9ao1ibKy6kWrMQyBPuPwWq3rGQQ/640?wx_fmt=png&from=appmsg)![]()![]()

![QQ_1765961890582](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EhX3LXAfz6BiaBJjnTttFFFDiaRrAOvjbl4HvibNTX9jc5JxKHdmfAzebvKyBAKfnCLUXLJIrPiamAhQ/640?wx_fmt=png&from=appmsg)![]()![]()

![QQ_1765961991857](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EhX3LXAfz6BiaBJjnTttFFFwJ9dNPjb4GQIhAMl8jyDtoaYyic2JA98M7E6EpFdQRWFlWLMX0taxZg/640?wx_fmt=png&from=appmsg)![]()![]()

**03**

**工具：函数符号还原**

IDA 中 Swift 函数符号是经过特殊处理的，形如`_$s10Foundation4UUIDV10uuidStringSSvg`和`_$sSS21_builtinStringLiteral17utf8CodeUnitCount7isASCIISSBp_BwBi1_tcfC`这种，前者看起来还相对明了，后者看起来就稍微费劲点，此时可以使用`xcrun swift-demangle`命令进行函数符号还原即可。

首先了解一下什么是`xcrun`。`...