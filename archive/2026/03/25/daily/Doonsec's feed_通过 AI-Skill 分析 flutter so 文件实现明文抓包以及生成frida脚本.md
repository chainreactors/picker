---
title: 通过 AI-Skill 分析 flutter so 文件实现明文抓包以及生成frida脚本
url: https://mp.weixin.qq.com/s/mCO7Qu5fSQiS-0hOMGYj-g
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:26:29.541076
---

# 通过 AI-Skill 分析 flutter so 文件实现明文抓包以及生成frida脚本

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oQ0sWhcqsVnjK9yiaaArPlJutaox7y348y3ynXnTMvAelFCQFa7cpwyuhUzRMplI8LU7ROHEQrIkfFszqU8DAr0E9ibQ7vA1MVS7y79ylrGRU/0?wx_fmt=jpeg)

# 通过 AI-Skill 分析 flutter so 文件实现明文抓包以及生成frida脚本

原创

进击的HACK
进击的HACK

进击的HACK

![]()

在小说阅读器中沉浸阅读

> 字数 998，阅读大约需 5 分钟

## 前言

看了猿人学大佬的文章，
使⽤ AI 实现 最新版本 Flutter HTTPS 明⽂抓包
[https://mp.weixin.qq.com/s/Z6oinmOXl5ADu0bs8ZAXlw](https://mp.weixin.qq.com/s?__biz=MjM5NjE0NTY5OA==&mid=2448550192&idx=1&sn=881d7129c63834391ecbc0ee11c16fa3&scene=21#wechat_redirect)

自己也尝试复现了一下。用的是 TRAE + GLM5.0，分析 libflutter.so，也是成功实现了明文抓包。

猿人学大佬的提示词确实好。

本文在此的基础上，新增了 frida hook 的部分，以及如何用 stackplz 实现修改后的 ecapture 的抓包。并将其制作为 skill，放在了 github 项目中。

https://github.com/boqiqibo/Sec-Skills/tree/main/flutter-ssl-analysis

测试的 APK 来自：
https://github.com/ZSA233/android-reverse-examples/blob/main/003\_frida-analykit-static-linked-boringssl/samples/app-release.apk

## skill 使用

配置 MCP
参考之前的文章：[搭建 AI 逆向分析工具 IDA-Pro-MCP](https://mp.weixin.qq.com/s?__biz=MzkxNjMwNDUxNg==&mid=2247489651&idx=1&sn=796d8a013669dbc1ce4054314572bf49&scene=21#wechat_redirect)

![cdbe3ddf6493df58fe66e2676b06d181.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkoWel00LemLQeMricibMicgAq4OuyBPhOaMDq4sxrA66zhLdcJR9ThndyoEEcXOfoPicmjrgqwHqG1Xx3rjd4ueAmxPtWQbqTwfIA/640?from=appmsg "null")

cdbe3ddf6493df58fe66e2676b06d181.png

从项目中下载 skill，并放在大模型工具的 skills 目录下。

**获取 ssl\_write 和 ssl\_read**

```
/flutter-ssl-analysis 调用ida-pro-mcp分析libflutter.so
或者
/flutter-ssl-analysis Locating SSL_write/SSL_read Functions
```

![cadfa1eafedf0544871c7d44c266fa4c.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkIjxjVG02TBKZgce3009zJmJSTTu1XyqA2tYJuo1ic7PuzSTKD9uLoaBlkXWrrIBw0YvZy0wiccuTuw2iaz9SjYicM01x4JomTYVk/640?from=appmsg "null")

cadfa1eafedf0544871c7d44c266fa4c.png

生成 frida SSL bypass

```
/flutter-ssl-analysis SSL Bypass Script Generation
```

结果：
![32488c52cf1fd00d08b6b75e7053fb6d.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVmRSLbCJaaHeiazwia4MXvTCbcibvRSEpx9TOvDw0GWqc4Ifpbib17A8JweyKTwDHDKslr16wmSxd0zw6LH3SQpsNq37uaemQg3mNQ/640?from=appmsg "null")

32488c52cf1fd00d08b6b75e7053fb6d.png

## flutter hook ssl 校验

大模型提示词
中文原本：

```
调用mcp，搜索字符串ssl_client，获取存在该字符串的函数地址，返回该函数的前12Byte字节码，比如

var pattern = "ff 03 05 d1 fd 7b 0f a9 bc de 05 94 08 0a 80 52 48"
```

大模型增强后：

```
Use the Memory Control Panel (MCP) to perform a search for the string "ssl_client" within the target process memory space. Upon identifying all functions that contain this string, retrieve the memory address of each such function. For each identified function address, extract and return the first 12 bytes of the function's machine code. The output should be formatted as a hexadecimal string with space-separated bytes, following the example format: "ff 03 05 d1 fd 7b 0f a9 bc de 05 94".
```

结果：
![8ca5aa4c25c6f4220dbe601247de96bd.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVlakuBXEdo5q4EMdyENAFZuJ3fkCthLhlILJ07eRTXLpOsV19EicpicLPEINND4KnWxdssos9mo4BSe1tGWicQA7y3ibhuu0WJGpas/640?from=appmsg "null")

8ca5aa4c25c6f4220dbe601247de96bd.png

```
函数1
fe 4f bf a9 a1 d5 ff d0 21 28 1b 91

函数2
ff c3 01 d1 fd 7b 01 a9 fc 6f 02 a9
```

字节码没问题
![aecda5ebf78f7b0f14a5cdefff145aa8.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVnMbfqm8jcF9g6Cce79stvmCarkV4s7XrZfc68jO03vpwibn0oDxnvPA2LOic02LFUV5ic55DXR7mfbkk91AwkznX4bVD0RY0SUcc/640?from=appmsg "null")

aecda5ebf78f7b0f14a5cdefff145aa8.png

替换 Frida JS 当中的字节码

## 原本

使⽤ AI 实现 最新版本 Flutter HTTPS 明⽂抓包
[https://mp.weixin.qq.com/s/Z6oinmOXl5ADu0bs8ZAXlw](https://mp.weixin.qq.com/s?__biz=MjM5NjE0NTY5OA==&mid=2448550192&idx=1&sn=881d7129c63834391ecbc0ee11c16fa3&scene=21#wechat_redirect)

但是文章中的 ecapture 用的是修改后
https://github.com/Litt1eQ/ecapture

但 Litt1eQ 大佬并没有提供 release 版本，于是想着能不能用别的方法。

## Frida

flutter\_ssl\_hook.js
![7e9db5496a364c9ff8890f2ea3cef195.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVmD3IW3sIribtGBN7RQvrJeO0hpdlibACPWWCh8iarmLZgDg2BSnHaW1ibWS2LuHP3hYB4fTgZ95S6LOaHV2ziaRCCUfH0BPoia2422E/640?from=appmsg "null")

7e9db5496a364c9ff8890f2ea3cef195.png

```
// Frida 16 Hook libflutter.so SSL 读写 (指定内存地址)
const LIB_NAME = 'libflutter.so'

// 你提供的内存偏移地址
const SSL_WRITE_OFFSET = 0x7185a4
const SSL_READ_OFFSET = 0x717e60

function hookFlutterSSL() {
  // 等待libflutter.so加载完成
  const module = Process.getModuleByName(LIB_NAME)
  console.log('[+] 找到模块:', module.name, '基址:', module.base)

  // 计算真实内存地址 = 模块基址 + 偏移地址
  const sslWriteAddr = module.base.add(SSL_WRITE_OFFSET)
  const sslReadAddr = module.base.add(SSL_READ_OFFSET)
  console.log('[+] ssl_write 真实地址:', sslWriteAddr)
  console.log('[+] ssl_read 真实地址:', sslReadAddr)

  // --------------------------
  // Hook SSL_Write (发送请求)
  // --------------------------
  Interceptor.attach(sslWriteAddr, {
    onEnter: function (args) {
      try {
        // Flutter/boringssl 标准参数: (ssl, buf, len, ...)
        const buf = args[1] // 数据缓冲区指针
        const len = args[2].toInt32() // 数据长度

        if (len <= 0) return

        console.log('\n=====================================')
        console.log('【 FLUTTER SSL WRITE - 请求数据 】')
        console.log('长度:', len)
        console.log('数据(十六进制):', hexdump(buf, { length: len }))
        console.log('数据(字符串):\n', buf.readUtf8String(len))
        console.log('=====================================\n')
      } catch (e) {
        console.log('[-] ssl_write 读取失败:', e.message)
      }
    },
  })

  // --------------------------
  // Hook SSL_Read (接收响应)
  // --------------------------
  Interceptor.attach(sslReadAddr, {
    onEnter: function (args) {
      // 保存入参，用于onExit读取数据
      this.buf = args[1]
      this.lenPtr = args[2]
    },
    onLeave: function (retval) {
      try {
        // SSL_Read 返回实际读取的字节数
        const readLen = retval.toInt32()
        if (readLen <= 0) return

        console.log('\n=====================================')
        console.log('【 FLUTTER SSL READ - 响应数据 】')
        console.log('实际长度:', readLen)
        // console.log("数据(十六进制):", hexdump(this.buf, { length: readLen }));
        console.log('数据(字符串):\n', this.buf.readUtf8String(readLen))
        console.log('=====================================\n')
      } catch (e) {
        console.log('[-] ssl_read 读取失败:', e.message)
      }
    },
  })

  console.log('[+] Hook 完成！等待SSL数据...')
}

// 等待库加载完成后执行hook
setImmediate(hookFlutterSSL)
```

结果：
![2ffca4f09c58debc6953b2349a5d68ef.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVlqcOMm4ibITxPn1v3kPmXXRIbqSIDkbHCDNnLunv8voKHcZic6U4DdK769r0gnTiayOiaIbbxnLrvOkLXFv50B4clicxiabMCaJwI6k/640?from=appmsg "null")

2ffca4f09c58debc6953b2349a5d68ef.png

## stackplz

stackplz 读取 ssl\_write 比较简单，但读返回值比较复杂，我调试起来奇奇怪怪的，有的时候可以读到有时候又没办法

**单纯读请求包**

```
./stackplz -n com.frida_analykit.static_linked_boringssl \
-l libflutter.so \
-w 0x7085A4[ptr,buf:256] \
--color --dumphex
```

请求包
![78d4b95726a8fdf0ff1e2a93be03a2d5.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkXSQmOY2chpJjakQ7biaGicETV5eJBhqs7iaqic4IPjWRSuG1lalGhdBocd200G78Oxc9rI5PxVy7iamTbIEm4Tst82f3XuPM9ExAA/640?from=appmsg "null")

78d4b95726a8fdf0ff1e2a93be03a2d5.png

**关于响应包**
原本的，但是失败的命令

```
./stackplz -n com.frida_analykit.static_linked_boringssl \
-l libflutter.so \
-w 0x7085A4[ptr,buf:256] \
-w 0x707E60[ptr,buf:x1] \
 --color --dumphex
```

stackplz 打印堆栈 --stack，或者走 IDA 找引用
![50526d040ae8034d48f01c9d60c4f427.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVm3MZibps693iaWpZZ9z48ibBgSU7w8NKRQbkKDVlGMSdKfEXuEIDOcgjsxnVzFcfp3rSKcuw5daB0KdHQz9pxglIOBgeDraB6ndQ/640?from=appmsg "null")

50526d040ae8034d48f01c9d60c4f427.png

查看
![58922bb2a8789c02b2fccdfc7f0f62cb.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVk1NBPYYPYGtsOWxQ0mqy89esQHckMbVicWQOUf2pzqz3icWW0ZCeI6xDdbReia08LJEHLibh06zgTKVuoAEbJYxIViaEAyj8qBLia3Y/640?from=appmsg "null")

58922bb2a8789c02b2fccdfc7f0f62cb.png

0x839540 - 0x10000 = 0x829540

```
./stackplz -n com.frida_analykit.static_linked_boringssl \
-l libflutter.so \
-w 0x7085A4[ptr,buf:256] \
-w 0x829540[ptr,buf:x1] \
 --color  --dumphex
```

能在一堆打印的信息里发现返回值
![d091319af37c4a484a...