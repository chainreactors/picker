---
title: MultiPar – 大文件备份与传输必备：「永不损坏」的数据[Win]
url: https://buaq.net/go-146531.html
source: unSafe.sh - 不安全
date: 2023-01-24
fetch_date: 2025-10-04T04:37:05.707906
---

# MultiPar – 大文件备份与传输必备：「永不损坏」的数据[Win]

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/8be0f29b7960ca6ac41ec6e9d81300b5.jpg)

MultiPar – 大文件备份与传输必备：「永不损坏」的数据[Win]

*2023-1-23 14:36:6
Author: [www.appinn.com(查看原文)](/jump-146531.htm)
阅读量:50
收藏*

---

**MultiPar** 是一款奇偶效验文件工具（Parchive tool），用来为文件、文件夹创建校验块，当文件损坏时，只要损坏占比小于创建时的冗余度，就可以完全恢复源文件。非常适合在大文件备份、传输大量数据时使用，以节省时间。@[Appinn](https://www.appinn.com/multipar-parchive-tool/)

![MultiPar - 大文件备份与传输必备：「永不损坏」的数据[Win]](https://static1.appinn.com/images/202301/multipar-parchive-tool.jpg!o "MultiPar - 大文件备份与传输必备：「永不损坏」的数据[Win] 1")

来自[**发现频道**](https://meta.appinn.net/c/faxian/10)，@**jerrylus** 同学的推荐，原文：<https://meta.appinn.net/t/topic/39807>

## MultiPar – 创建冗余校验块，恢复受损文件

MultiPar 可以为文件/文件夹创建校验块，在原文件损坏时，只要损坏占比小于创建时的冗余度，就可以完全恢复源文件。

### 背景、原理和应用场景

在网络上下载资源时，验证文件的校验和（checksum）是一个好习惯，不仅能避免从恶意来源下载到假冒的文件，也可以及早发现文件在传输过程中出现的错误。但校验和不一致只能告诉我们文件的完整性被破坏了，除了重新下载一次，似乎也没有什么其他选项（尽管有时不一致的可能只是几个 bit）。

WinRAR 中的“恢复记录”功能，为这个烦人的问题提出了一种简单的解决方案。只需要把文件打包成 RAR，勾上“启用恢复记录”，再设定下冗余度参数，得到的文件就会自带校验数据。即使传输过程中出了错，也可以用校验数据恢复。

“恢复记录”实际上是基于 Reed–Solomon 码实现的。通过这种编码方式，可以将原始数据分成 N 块，再计算 M 个校验块。发生文件损坏时，只要损坏块数小于校验块数量，就可以将原数据恢复。敏锐的读者会问，如果校验块损坏了呢？但不用担心，损坏的校验块也可以用原始数据的完好部分和其他完好的校验块重建。（注：这里对算法细节有较大简化）

可以想到，除了快速重建损坏的下载文件，校验块在许多其他场景下也有用途。日常生活中的一个常见备份策略是将文件复制多份，但即使是本地的文件传输也有可能出现比特翻转，导致副本和源文件不一致。对于如音频、视频这类文件来说可能还好，最多影响一两帧的播放，但其他对文件完整性要求极高的情况下（例如游戏存档），这个问题可能尤为致命。而如果先创建校验块，再同时复制原文件和校验块，就能极大减少因复制过程中出错导致副本不可用的可能性。

RAR 是个闭源格式，而开源世界中也早有开发者基于 Reed–Solomon 码实现了具有相同功能的开源存档格式： Parchive。本次介绍的 MultiPar 就是Windows 平台的一个 Parchive 创建工具。

## MultiPar : Parchive tool

项目地址：[Github](https://github.com/Yutaka-Sawada/MultiPar)

**适用：**

* 备份、下载场景
* 幅度较小的文件破坏

**不适用：**

* 大规模文件修改（例如视频重编码）

### 演示

假设我有一个文件夹，里面有一些十分重要的文件：

![MultiPar - 大文件备份与传输必备：「永不损坏」的数据[Win] 1](https://meta-cdn1.appinn.com/uploads/default/original/3X/c/f/cf49c898efd89a13705e48709dad00035fa22100.png "MultiPar - 大文件备份与传输必备：「永不损坏」的数据[Win] 2")

打开 MultiPar 将文件拖入，创建校验块。这里选择了 20% 的冗余度，也可以根据自己的需要调整。（图中可以看到，原始文件总共有 2038 个分块，本次会创建 408 个校验块）

![MultiPar - 大文件备份与传输必备：「永不损坏」的数据[Win] 2](https://meta-cdn1.appinn.com/uploads/default/original/3X/6/5/651e270e2014b62132bd9a110c5a1a1f0471f722.png "MultiPar - 大文件备份与传输必备：「永不损坏」的数据[Win] 3")

完成后，文件夹下会多出校验块文件。（其中第一个较小的是索引/目录文件，第二个较大的是真正的校验块文件。依据设置可能会有多个。）

![MultiPar - 大文件备份与传输必备：「永不损坏」的数据[Win] 3](https://meta-cdn1.appinn.com/uploads/default/original/3X/d/0/d02ff32bd611dbbba44f6cf00a31edf9906aef7a.png "MultiPar - 大文件备份与传输必备：「永不损坏」的数据[Win] 4")

现在对文件进行一些破坏：

1. 用记事本打开视频，随机删除一小段。（模拟传输过程中的不稳定）
2. 用 PowerPoint 打开文档，删除一页幻灯片。（模拟手残）
3. 打开压缩包，删除压缩包中的一个文件夹。（模拟手残）
4. 重命名照片文件。（模拟无心之失）

随便点击一个 .par2 文件，打开 **MultiPar**，尝试进行文件恢复。

可以看到前 3 个文件被标记为破损（文件内容变更，影响完整性），最后一个被标记为缺失（重命名后的文件显示“文件名不对应”）。下方显示“可以用 22 个分块进行恢复”，而我们总共一共有 408 个校验块，因此可以正常恢复。

![MultiPar - 大文件备份与传输必备：「永不损坏」的数据[Win] 4](https://meta-cdn1.appinn.com/uploads/default/original/3X/f/2/f2ffe1c36916408002d5d1b9902418acfd070ba6.png "MultiPar - 大文件备份与传输必备：「永不损坏」的数据[Win] 5")

点击右下角修复按钮，所有文件恢复如初。（3 个被破坏的文件显示“修复成功”，最后一个被重命名的文件显示“还原成功”）

---

文章来源: https://www.appinn.com/multipar-parchive-tool/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)