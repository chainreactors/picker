---
title: 数据恢复(八)-PDF文件修复实战
url: https://zgao.top/%e6%95%b0%e6%8d%ae%e6%81%a2%e5%a4%8d%e5%85%ab-pdf%e6%96%87%e4%bb%b6%e4%bf%ae%e5%a4%8d%e5%ae%9e%e6%88%98/
source: Zgao's blog
date: 2023-02-17
fetch_date: 2025-10-04T06:50:35.862368
---

# 数据恢复(八)-PDF文件修复实战

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# 数据恢复(八)-PDF文件修复实战

* [首页](https://zgao.top)
* [数据恢复(八)-PDF文件修复实战](https://zgao.top:443/%E6%95%B0%E6%8D%AE%E6%81%A2%E5%A4%8D%E5%85%AB-pdf%E6%96%87%E4%BB%B6%E4%BF%AE%E5%A4%8D%E5%AE%9E%E6%88%98/)

[2月 16, 2023](https://zgao.top/2023/02/)

### 数据恢复(八)-PDF文件修复实战

作者 [Zgao](https://zgao.top/author/zgao/)
在[[数据恢复](https://zgao.top/category/%E6%95%B0%E6%8D%AE%E6%81%A2%E5%A4%8D/)](https://zgao.top/%E6%95%B0%E6%8D%AE%E6%81%A2%E5%A4%8D%E5%85%AB-pdf%E6%96%87%E4%BB%B6%E4%BF%AE%E5%A4%8D%E5%AE%9E%E6%88%98/)

上一篇文章中对PDF文件结构进行分析，那么实战中遇到PDF损坏的情况该如何进行手工或工具修复？

文章目录

[ ]

* [案例背景分析](#%E6%A1%88%E4%BE%8B%E8%83%8C%E6%99%AF%E5%88%86%E6%9E%90 "案例背景分析")
* [PDF文件修复思路](#PDF%E6%96%87%E4%BB%B6%E4%BF%AE%E5%A4%8D%E6%80%9D%E8%B7%AF "PDF文件修复思路")
* [PDF修复工具](#PDF%E4%BF%AE%E5%A4%8D%E5%B7%A5%E5%85%B7 "PDF修复工具")
* [PDF手工修复](#PDF%E6%89%8B%E5%B7%A5%E4%BF%AE%E5%A4%8D "PDF手工修复")
  + [foremost提取PDF图片文件](#foremost%E6%8F%90%E5%8F%96PDF%E5%9B%BE%E7%89%87%E6%96%87%E4%BB%B6 "foremost提取PDF图片文件")

## 案例背景分析

和《[数据恢复(六)-SqlSever数据库mdf文件恢复实战](https://zgao.top/%E6%95%B0%E6%8D%AE%E6%81%A2%E5%A4%8D%E5%85%AD-sqlsever%E6%95%B0%E6%8D%AE%E5%BA%93mdf%E6%96%87%E4%BB%B6%E6%81%A2%E5%A4%8D%E5%AE%9E%E6%88%98/)》是同样的勒索场景，PDF文件头尾均丢失了256kb的数据。

![](https://zgao.top/wp-content/uploads/2023/02/image-40-1024x293.png)

文件头

![](https://zgao.top/wp-content/uploads/2023/02/image-42-1024x248.png)

文件尾，xref表已经完全丢失

根据上面的情况分析PDF丢失了哪部分数据？

* PDF文件头
* 文件头后面的部分对象obj
* xref之前的部分对象obj
* 交叉引用表xref
* 文件尾trailer

为什么强调丢失部分对象obj？因为对象obj是PDF的主体部分。

![](https://zgao.top/wp-content/uploads/2023/02/image-43-1024x458.png)

第一个完整的obj编号为26，说明在此之前已经丢失了26个obj对象了（从0开始）。

![](https://zgao.top/wp-content/uploads/2023/02/image-44-1024x454.png)

这就意味着，我们最多也就只能恢复pdf文件中的81-26=55个完整的obj。

别担心obj数量太少，没法恢复出来什么数据。比如有的obj是一个图片，数据量占比实则很大。

## PDF文件修复思路

按照上面的情况，相当于PDF文件的文件头、xref表、trailer完全丢失。只剩下大部分的obj。

此时只能扫描PDF所有的obj，重新排序计算obj的偏移地址，生成xref交叉引用表和trailer。

## PDF修复工具

我对市面上常见的PDF修复工具都进行了测试，发现有三款工具能达到恢复效果。

* [在线修复PDF文件 – iLovePDF](https://www.ilovepdf.com/zh-cn/repair-pdf)
* PDF Recovery Toolbox
* SysInfoTools PDF Repair

这里以PDF Recovery Toolbox工具为例，导入受损的PDF文件。

![](https://zgao.top/wp-content/uploads/2023/02/image-45-1024x499.png)
![](https://zgao.top/wp-content/uploads/2023/02/image-46-1024x417.png)

工具会扫描PDF的所有内容重新生成完整的PDF文件。

![](https://zgao.top/wp-content/uploads/2023/02/image-47-1024x431.png)

但是工具的缺点是不支持批量PDF损坏文件修复。

## PDF手工修复

以图片类型的PDF为例进行分析。

![](https://zgao.top/wp-content/uploads/2023/02/image-50-1024x411.png)

可以通过写代码obj特征提取pdf中的图片内容，这里就不贴代码了，可以自行实现。

### foremost提取PDF图片文件

也可以用到foremost。思路很简单，因为PDF文件本身的obj就是嵌入的其他文件，所以其他格式的文件在PDF中还是原样保存的。

```
apt-get install foremost -y
```

这里可以把PDF看做一个raw二进制文件，从中提取图片文件。

```
foremost -t jpg -i damaged_file.pdf -v
```

![](https://zgao.top/wp-content/uploads/2023/02/image-48-1024x992.png)
![](https://zgao.top/wp-content/uploads/2023/02/image-49-1024x603.png)

从损坏的pdf文件中提取所有图片文件，再把所有的图片合并到一个新的PDF即可完成修复。

Post Views: 1,583

赞赏

![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114105.jpeg)微信赞赏![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114100.jpeg)支付宝赞赏

###### Zgao

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

### 发表评论 [取消回复](/%E6%95%B0%E6%8D%AE%E6%81%A2%E5%A4%8D%E5%85%AB-pdf%E6%96%87%E4%BB%B6%E4%BF%AE%E5%A4%8D%E5%AE%9E%E6%88%98/#respond)

Δ

版权©2020 Author By : Zgao