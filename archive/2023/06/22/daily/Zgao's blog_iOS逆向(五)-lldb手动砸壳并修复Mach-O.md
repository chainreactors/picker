---
title: iOS逆向(五)-lldb手动砸壳并修复Mach-O
url: https://zgao.top/ios%e9%80%86%e5%90%91%e4%ba%94-lldb%e6%89%8b%e5%8a%a8%e7%a0%b8%e5%a3%b3%e5%b9%b6%e4%bf%ae%e5%a4%8dmach-o/
source: Zgao's blog
date: 2023-06-22
fetch_date: 2025-10-04T11:44:14.865035
---

# iOS逆向(五)-lldb手动砸壳并修复Mach-O

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# iOS逆向(五)-lldb手动砸壳并修复Mach-O

* [首页](https://zgao.top)
* [iOS逆向(五)-lldb手动砸壳并修复Mach-O](https://zgao.top:443/ios%E9%80%86%E5%90%91%E4%BA%94-lldb%E6%89%8B%E5%8A%A8%E7%A0%B8%E5%A3%B3%E5%B9%B6%E4%BF%AE%E5%A4%8Dmach-o/)

[6月 21, 2023](https://zgao.top/2023/06/)

### iOS逆向(五)-lldb手动砸壳并修复Mach-O

作者 [Zgao](https://zgao.top/author/zgao/)
在[[逆向](https://zgao.top/category/%E9%80%86%E5%90%91/)](https://zgao.top/ios%E9%80%86%E5%90%91%E4%BA%94-lldb%E6%89%8B%E5%8A%A8%E7%A0%B8%E5%A3%B3%E5%B9%B6%E4%BF%AE%E5%A4%8Dmach-o/)

ios上一键脱壳的工具非常多，但原理基本都相同。都是运行app后从内存中dump出解密后的内容再重写回文件，替换原本的加密的二进制文件重新打包生成ipa，就完成了脱壳。

了解脱壳的原理，我们可以尝试使用手动脱壳，这样对ios的逆向理解也会更加深刻。

文章目录

[ ]

* [难度](#%E9%9A%BE%E5%BA%A6 "难度")
* [工具](#%E5%B7%A5%E5%85%B7 "工具")
  + [工具安装](#%E5%B7%A5%E5%85%B7%E5%AE%89%E8%A3%85 "工具安装")
    - [ipatool](#ipatool "ipatool")
    - [lldb和otool](#lldb%E5%92%8Cotool "lldb和otool")
    - [debugserver](#debugserver "debugserver")
* [手动砸壳过程](#%E6%89%8B%E5%8A%A8%E7%A0%B8%E5%A3%B3%E8%BF%87%E7%A8%8B "手动砸壳过程")
  + [ipatool下载ipa包](#ipatool%E4%B8%8B%E8%BD%BDipa%E5%8C%85 "ipatool下载ipa包")
  + [otool分析mach-o文件](#otool%E5%88%86%E6%9E%90mach-o%E6%96%87%E4%BB%B6 "otool分析mach-o文件")
  + [debugserver 监听端口](#debugserver_%E7%9B%91%E5%90%AC%E7%AB%AF%E5%8F%A3 "debugserver 监听端口")
  + [LLDB dump内存二进制文件](#LLDB_dump%E5%86%85%E5%AD%98%E4%BA%8C%E8%BF%9B%E5%88%B6%E6%96%87%E4%BB%B6 "LLDB dump内存二进制文件")
  + [修复Mach-O头部](#%E4%BF%AE%E5%A4%8DMach-O%E5%A4%B4%E9%83%A8 "修复Mach-O头部")

## 难度

★★☆☆☆

## 工具

* 越狱IOS 14.4
* ipatool
* otool
* lldb
* debugserver
* dd
* 010 editor

### 工具安装

#### ipatool

<https://github.com/majd/ipatool>

`ipatool`是一个命令行工具，可以在App Store上搜索 iOS 应用程序并下载应用程序包的副本，称为*ipa*文件。而使用ipatool下载的ipa文件是未经过砸壳，正好方便手动砸壳。

通过命令行安装，然后登录自己的AppStore的账号。

```
brew tap majd/repo
brew install ipatool
```

#### lldb和otool

LLDB全称Low Level Debugger ，是轻量级的高性能调试器，内置于Xcode。在macOS系统中，可以使用Xcode命令行工具来安装LLDB和otool。

```
xcode-select --install
```

#### debugserver

![](https://zgao.top/wp-content/uploads/2023/06/25092736-9cf5dbe0109051ba.webp)

LLDB和debugserver通信过程

在越狱设备上安装debugserver非常方便，直接在cydia商店搜索安装即可。

![](https://zgao.top/wp-content/uploads/2023/06/image-25.png)

## 手动砸壳过程

### ipatool下载ipa包

我们以某火锅app为例，使用ipatool搜索关键词找到对应的bundleID然后下载。

```
ipatool --format json search -l 5 海底捞
```

![](https://zgao.top/wp-content/uploads/2023/06/image-28-1024x725.png)

```
ipatool download -b app.haidilao.HaidilaoMobileDistribution --purchase
```

### otool分析mach-o文件

下载完成后先解压ipa包。

```
unzip app.haidilao.HaidilaoMobileDistribution_553115181_8.3.8.ipa -d haidilao
```

将ipa解压到haidilao的目录。

```
cd haidilao/Payload/HaiDiLao.app
```

其中与包名同名的文件就是要解密的二进制文件。

```
otool -arch arm64 -l ./HaiDiLao | grep -C5 LC_ENCRYPTION
```

![](https://zgao.top/wp-content/uploads/2023/06/image-26-1024x458.png)

每个字段的含义如下：

* `cmd`：这是load command的类型，表示这个load command包含了64位的加密信息。
* `cmdsize`：表示此load command的大小为24字节。
* `cryptoff`：表示加密数据在文件中开始的偏移量，单位是字节。表示加密数据从文件的16384字节处开始。
* `cryptsize`：表示加密数据的大小，单位是字节。表示加密数据的大小为31014912字节。
* `cryptid`：这是一个标志，表示文件是否被加密。如果`cryptid`的值为0，那么文件未被加密。
* `pad`：这是一个填充字段，用于保证数据对齐。

其中 `cryptoff` 和 `cryptsize` 就是文件的加密位置的起始偏移地址和大小。这两个值需要记下来，后面会用到。

### debugserver 监听端口

在ios设备上运行debugserver监听端口，这里我们用的usb数据线链接的iOS设备，就用iproxy转发端口映射。

```
//在mac上执行
iproxy 2222 22 &
iproxy 8888 8888 &
ssh root@127.0.0.1 -p2222

//在ios设备上执行
debugserver 127.0.0.1:8888 -a HaiDiLao
```

### LLDB dump内存二进制文件

```
process connect connect://127.0.0.1:8888
image list -f -o HaiDiLao
memory read 0x00000001047f8000+16384 -c 31014912 --force --binary -outfile ./HaiDiLaoDecrypted
```

![](https://zgao.top/wp-content/uploads/2023/06/image-27-1024x492.png)

利用memory命令从内存中dump出解密后的二进制数据，保存到文件。

```
image list -f -o HaiDiLao
[  0] /private/var/containers/Bundle/Application/B24DD689-8666-41FA-AC86-12B0689352A0/HaiDiLao.app/HaiDiLao 0x00000000047f8000(0x00000001047f8000)
```

需要注意的是这里不是获取ASLR的偏移量，而是要内存加载地址（0x00000001047f8000）。

### 修复Mach-O头部

因为dump出来的数据是没有Mach-O头部信息的，需要修复才能使用。这里采用最快捷的办法，将dump出来的数据重新写回到砸壳前的文件从而替换加密的数据。

```
dd if=./HaiDiLaoDecrypted of=./HaiDiLao bs=1 seek=16384 conv=notrunc
```

用dd命令将文件按照偏移量重新覆写回去。

![](https://zgao.top/wp-content/uploads/2023/06/image-29-1024x628.png)

这里用010 editor把Mach-o修改为cryptid重新修改为0。

```
zip -r haidilao.ipa haidilao/
```

使用zip命令重新打包回ipa文件，就完成手动砸壳了。

Post Views: 1,356

赞赏

![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114105.jpeg)微信赞赏![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114100.jpeg)支付宝赞赏

###### Zgao

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

### 发表评论 [取消回复](/ios%E9%80%86%E5%90%91%E4%BA%94-lldb%E6%89%8B%E5%8A%A8%E7%A0%B8%E5%A3%B3%E5%B9%B6%E4%BF%AE%E5%A4%8Dmach-o/#respond)

Δ

版权©2020 Author By : Zgao