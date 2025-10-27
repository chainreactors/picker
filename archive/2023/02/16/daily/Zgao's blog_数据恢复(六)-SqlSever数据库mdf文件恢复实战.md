---
title: 数据恢复(六)-SqlSever数据库mdf文件恢复实战
url: https://zgao.top/%e6%95%b0%e6%8d%ae%e6%81%a2%e5%a4%8d%e5%85%ad-sqlsever%e6%95%b0%e6%8d%ae%e5%ba%93mdf%e6%96%87%e4%bb%b6%e6%81%a2%e5%a4%8d%e5%ae%9e%e6%88%98/
source: Zgao's blog
date: 2023-02-16
fetch_date: 2025-10-04T06:43:15.240583
---

# 数据恢复(六)-SqlSever数据库mdf文件恢复实战

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# 数据恢复(六)-SqlSever数据库mdf文件恢复实战

* [首页](https://zgao.top)
* [数据恢复(六)-SqlSever数据库mdf文件恢复实战](https://zgao.top:443/%E6%95%B0%E6%8D%AE%E6%81%A2%E5%A4%8D%E5%85%AD-sqlsever%E6%95%B0%E6%8D%AE%E5%BA%93mdf%E6%96%87%E4%BB%B6%E6%81%A2%E5%A4%8D%E5%AE%9E%E6%88%98/)

[2月 15, 2023](https://zgao.top/2023/02/)

### 数据恢复(六)-SqlSever数据库mdf文件恢复实战

作者 [Zgao](https://zgao.top/author/zgao/)
在[[数据恢复](https://zgao.top/category/%E6%95%B0%E6%8D%AE%E6%81%A2%E5%A4%8D/)](https://zgao.top/%E6%95%B0%E6%8D%AE%E6%81%A2%E5%A4%8D%E5%85%AD-sqlsever%E6%95%B0%E6%8D%AE%E5%BA%93mdf%E6%96%87%E4%BB%B6%E6%81%A2%E5%A4%8D%E5%AE%9E%E6%88%98/)

> 某客户系统文件被勒索后，通过分析发现文件的头部全0填充了256kb。但是文件的主体内容还在，也就意味着可以通过数据恢复的方式进行文件修复。本文通过对mdf文件进行修复，成功帮客户成功恢复几个G的数据库，最大程度上降低损失。
>
> 案例背景

文章目录

[ ]

* [实验环境](#%E5%AE%9E%E9%AA%8C%E7%8E%AF%E5%A2%83 "实验环境")
* [勒索数据库文件分析](#%E5%8B%92%E7%B4%A2%E6%95%B0%E6%8D%AE%E5%BA%93%E6%96%87%E4%BB%B6%E5%88%86%E6%9E%90 "勒索数据库文件分析")
* [mdf修复过程](#mdf%E4%BF%AE%E5%A4%8D%E8%BF%87%E7%A8%8B "mdf修复过程")
* [导入SQLserver重新生成mdf文件](#%E5%AF%BC%E5%85%A5SQLserver%E9%87%8D%E6%96%B0%E7%94%9F%E6%88%90mdf%E6%96%87%E4%BB%B6 "导入SQLserver重新生成mdf文件")

## 实验环境

* 腾讯云 4核8G CVM
* SQLserver 2016
* Stellar Phoenix SQL Database Repair

## 勒索数据库文件分析

![](https://zgao.top/wp-content/uploads/2023/02/image-26-1024x682.png)

winhex直接跳转到偏移量3FFFF，后面部分仍为文件原内容。

## mdf修复过程

注意：要想将修复后的数据再导出为mdf文件需要先安装MSSQL数据

下载数据库修复工具后，解压打开运行ssr.exe。

![](https://zgao.top/wp-content/uploads/2023/02/image-27-1024x575.png)

选择待修复的mdf文件，如果是勒索的文件需要把后缀名改为mdf。

![](https://zgao.top/wp-content/uploads/2023/02/image-28-1024x699.png)

根据原本的数据库版本进行选择。

![](https://zgao.top/wp-content/uploads/2023/02/image-29.png)

修复完成后根据提示进行保存。如果mdf文件很大，则修复时间可能长达数小时。

![](https://zgao.top/wp-content/uploads/2023/02/image-30-1024x758.png)

预览恢复后的数据库表。

![](https://zgao.top/wp-content/uploads/2023/02/image-31-1024x439.png)

## 导入SQLserver重新生成mdf文件

选择本地搭建的SQLserver数据库（实测该版本不支持远程数据库）。

![](https://zgao.top/wp-content/uploads/2023/02/image-32.png)

连接成功后会将数据重新写入数据库。

![](https://zgao.top/wp-content/uploads/2023/02/image-33.png)

![](https://zgao.top/wp-content/uploads/2023/02/image-34-1024x598.png)

mdf成功修复完成！

经校验比对大部分的表均完全恢复完成，仅丢失很少数据。

Post Views: 1,451

赞赏

![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114105.jpeg)微信赞赏![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114100.jpeg)支付宝赞赏

###### Zgao

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

### 目前为止有一条评论

###### http://tupalo.com/en/users/4167854 发布于8:02 下午 - 5月 9, 2023

Thanks for the interesting and up to date information.

[回复](https://zgao.top/%E6%95%B0%E6%8D%AE%E6%81%A2%E5%A4%8D%E5%85%AD-sqlsever%E6%95%B0%E6%8D%AE%E5%BA%93mdf%E6%96%87%E4%BB%B6%E6%81%A2%E5%A4%8D%E5%AE%9E%E6%88%98/?replytocom=5287#respond)

### 发表评论 [取消回复](/%E6%95%B0%E6%8D%AE%E6%81%A2%E5%A4%8D%E5%85%AD-sqlsever%E6%95%B0%E6%8D%AE%E5%BA%93mdf%E6%96%87%E4%BB%B6%E6%81%A2%E5%A4%8D%E5%AE%9E%E6%88%98/#respond)

Δ

版权©2020 Author By : Zgao