---
title: 压缩包数据清洗最佳实践
url: https://zgao.top/%e5%8e%8b%e7%bc%a9%e5%8c%85%e6%95%b0%e6%8d%ae%e6%b8%85%e6%b4%97%e6%9c%80%e4%bd%b3%e5%ae%9e%e8%b7%b5/
source: Zgao's blog
date: 2025-03-01
fetch_date: 2025-10-06T21:56:05.570588
---

# 压缩包数据清洗最佳实践

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# 压缩包数据清洗最佳实践

* [首页](https://zgao.top)
* [压缩包数据清洗最佳实践](https://zgao.top:443/%E5%8E%8B%E7%BC%A9%E5%8C%85%E6%95%B0%E6%8D%AE%E6%B8%85%E6%B4%97%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5/)

[2月 28, 2025](https://zgao.top/2025/02/)

### 压缩包数据清洗最佳实践

作者 [Zgao](https://zgao.top/author/zgao/)
在[[安全运维](https://zgao.top/category/%E5%AE%89%E5%85%A8%E8%BF%90%E7%BB%B4/)](https://zgao.top/%E5%8E%8B%E7%BC%A9%E5%8C%85%E6%95%B0%E6%8D%AE%E6%B8%85%E6%B4%97%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5/)

常用的压缩包格式有zip，rar，7z这三类。一开始在处理这些压缩包时，采用的思路是直接用python封装的第三方模块如zipfile、rarfile、py7zr这些直接处理原始压缩文件。

如果只是处理几百兆的小文件，是没有任何问题，但对于几十G的压缩包效率极其低下，尤其针对不解压提取压缩包内部的文件内容的场景，一个rar的压缩包处理时长可能花费数十个小时。

本文针对压缩包清洗，花费大量时间研究。深入分析清洗数据的坑点，以及优化思路。

文章目录

[ ]

* [结论分析](#%E7%BB%93%E8%AE%BA%E5%88%86%E6%9E%90 "结论分析")
* [为什么不推荐使用rar和7z？](#%E4%B8%BA%E4%BB%80%E4%B9%88%E4%B8%8D%E6%8E%A8%E8%8D%90%E4%BD%BF%E7%94%A8rar%E5%92%8C7z%EF%BC%9F "为什么不推荐使用rar和7z？")
* [最佳实践](#%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5 "最佳实践")
* [RAR 分卷的处理](#RAR_%E5%88%86%E5%8D%B7%E7%9A%84%E5%A4%84%E7%90%86 "RAR 分卷的处理")
  + [处理单个rar分卷的问题？](#%E5%A4%84%E7%90%86%E5%8D%95%E4%B8%AArar%E5%88%86%E5%8D%B7%E7%9A%84%E9%97%AE%E9%A2%98%EF%BC%9F "处理单个rar分卷的问题？")

## 结论分析

在不解压清洗压缩包内部数据的场景下：

zip > rar > 7z

这个是基于压缩包的兼容性，压缩比，python模块封装程度，解析速度等因素，在大量实验场景下得出的结论。

## 为什么不推荐使用rar和7z？

分析python模块rarfile的底层源码，会发现这个模块底层实际是调用subprocess去执行unrar系统命令来操作压缩包内部的文件。

对于一个几十G的rar压缩包，内部的文件可能上百万个。逐一读取内部的文件进行解析，相当于要调用几百万次unrar命令，而且都是进程级的开销，效率太低了。

但是这并不能归结于rarfile，而是rar的压缩协议本身并不开源，rarfile只能是对系统unrar进行封装调用。而且unrar的命令行还存在bug，在代码兼容上浪费大量时间。

7z相对于zip和rar，出现的频率相对较少，在实际场景下调用py7zr还是存在很多兼容性的问题，比如zipfile和rarfile的调用接口是完全一致的，但是py7zr却有很大差异。这就导致代码适配异常艰难，投入产出也非常低。

## 最佳实践

最开始想在代码层面适配各种格式的压缩包，最后还是决定直接把其他的压缩包格式统一转换成zip。

这就涉及到必须要先统一解压再压缩的过程。

建议统一用7z命令行来解压rar、zip、7z文件，都是兼容的。

```
7z x archive.rar -o /tmp
```

zip也有多种压缩算法，但是针对于文本文件压缩比最高的是 lzma算法。

```
7z a -tzip -mm=lzma -mx=9 NEW_FILE.zip "FILE_DIR/*"
```

这样压缩出来的zip文件，会比用rar压缩出的体积更小。经测试不管是压缩比，还是兼容性方面都是非常不错。

代码就不放出来了，只是给出一些思路。

## RAR 分卷的处理

rar存在分卷的机制，但是用命令处理rar分卷有些特别的问题。

7z 命令会自动解压其他 part 文件。当使用 7z 命令解压一个 RAR 分卷的第一部分（通常是 .part1.rar 文件）时，7z 会自动识别并处理所有相关的分卷文件，只要它们都位于同一目录中并且命名符合惯例。

```
archive.part1.rar
archive.part2.rar
archive.part3.rar
archive.part4.rar
archive.part5.rar
```

只需要运行：

```
7z x archive.part1.rar
```

7z 会自动处理所有分卷并提取完整内容。不需要分别解压每个分卷文件。

1. 所有分卷文件必须位于同一目录中
2. 必须从第一个分卷（.part1.rar 或 .rar）开始解压
3. 所有分卷文件必须完整且未损坏
4. 文件命名必须一致（按照 .part1.rar, .part2.rar 或 .r00, .r01, .r02 等格式）

如果某个分卷缺失或损坏，解压过程会在到达该分卷时失败。

### 处理单个rar分卷的问题？

如果7z x archive.part3.rar 的话，是不是也会自动解压1和2？

* 如果解压 `archive.part1.rar`，7z 会找到并处理所有后续分卷（part2, part3等）
* 如果解压 `archive.part3.rar`，7z 只能访问从第三个分卷开始的数据，这通常只是完整归档的一个片段

但是7z 会自动识别并处理 part3 之后的所有分卷（如 part4、part5 等），前提是这些分卷存在且在同一目录中。

这就像是从一本书的第3章开始阅读，而没有前两章的内容，就将无法获得完整的信息。

所以使用7z命令本身没有直接支持只解压特定分卷的功能，因为7z（与大多数归档工具一样）将RAR分卷视为单个逻辑归档的组成部分。

用7z命令直接处理第一个rar文件，其他的都跳过即可。

Post Views: 412

赞赏

![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114105.jpeg)微信赞赏![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114100.jpeg)支付宝赞赏

###### Zgao

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

### 发表评论 [取消回复](/%E5%8E%8B%E7%BC%A9%E5%8C%85%E6%95%B0%E6%8D%AE%E6%B8%85%E6%B4%97%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5/#respond)

Δ

版权©2020 Author By : Zgao