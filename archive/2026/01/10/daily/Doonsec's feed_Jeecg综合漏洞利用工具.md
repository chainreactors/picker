---
title: Jeecg综合漏洞利用工具
url: https://mp.weixin.qq.com/s/ECGxZ46xSlwXJ-LSXwCoVA
source: Doonsec's feed
date: 2026-01-10
fetch_date: 2026-01-11T03:39:28.614965
---

# Jeecg综合漏洞利用工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/XZByrJJ6uUweTDYunX7L5UJMVricbpnaqTQGzM3f5rWOXxd91amGb0j4ibD4hqib0Zs44ricIsDRK5NQNCSzfick4dw/0?wx_fmt=jpeg)

# Jeecg综合漏洞利用工具

W小哥

![]()

在小说阅读器中沉浸阅读

# Jeecg综合漏洞利用工具

jeecg综合漏洞利用工具，程序采用javafx开发，环境JDK 1.8 声明：仅用于授权测试，用户滥用造成的一切后果和作者无关 请遵守法律法规！ 漏洞收录如下：

jeecg-boot queryFieldBySql远程命令执行漏洞

jeecg-boot testConnection远程命令执行漏洞

JeecgBoot jmreport/loadTableData SSTI模板注入漏洞

jeecg-boot-queryTableData-sqli注入漏洞

jeecg-boot-getDictItemsByTable-sqli注入漏洞

Jeecg-Boot qurestSql-SQL注入漏洞

jeecg-boot commonController 任意文件上传漏洞

Jeecg-boot JMREPORT任意文件上传漏洞

jeecg-boot-querySysUser信息泄露漏洞

jeecg-boot-checkOnlyUser信息泄露漏洞

Jeecg-boot-httptrace信息泄露漏洞

jeecg-boot-任意文件下载漏洞

jeecg-boot-jeecgFormDemoController漏洞

jeecg-boot-v2 P3 Biz Chat任意文件读取漏洞

jeecg-boot-v2 sys/duplicate/check注入漏洞

jeecg-boot-v2 AviatorScript表达式注入漏洞

# 功能介绍

Jeecg综合漏洞利用工具集成了多模块漏洞利用，包括一键漏洞检测，单独选择模块检测，cmdshell模块，文件上传模块，批量检测模块等v3.0版本内置的标准库外，在检测模块加入了okhttp的三方库，支持https网站检测，以及优化了基于jeecg queryUser漏洞的接口测试

一键检测模块，选择模块

jeecg-boot queryFieldBySql远程命令执行漏洞

jeecg-boot testConnection远程命令执行漏洞

JeecgBoot jmreport/loadTableData SSTI模板注入漏洞

jeecg-boot-queryTableData-sqli注入漏洞

jeecg-boot-getDictItemsByTable-sqli注入漏洞

Jeecg-Boot qurestSql-SQL注入漏洞

jeecg-boot commonController 任意文件上传漏洞

Jeecg-boot JMREPORT任意文件上传漏洞

jeecg-boot-querySysUser信息泄露漏洞

jeecg-boot-checkOnlyUser信息泄露漏洞

Jeecg-boot-httptrace信息泄露漏洞

接口测试模块：

jeecg-boot-querySysUser信息泄露漏洞

jeecg-boot-checkOnlyUser信息泄露漏洞

cmdshell模块：

jeecg-boot queryFieldBySql远程命令执行漏洞

jeecg-boot testConnection远程命令执行漏洞

JeecgBoot jmreport/loadTableData SSTI模板注入漏洞

文件上传模块:

jeecg-boot commonController 任意文件上传漏洞

Jeecg-boot JMREPORT任意文件上传漏洞

批量检测模块：

jeecg-boot queryFieldBySql远程命令执行漏洞

jeecg-boot testConnection远程命令执行漏洞

JeecgBoot jmreport/loadTableData SSTI模板注入漏洞

jeecg-boot-queryTableData-sqli注入漏洞

jeecg-boot-getDictItemsByTable-sqli注入漏洞

Jeecg-Boot qurestSql-SQL注入漏洞

# 功能使用

默认模块可一键扫描所有漏洞

![](https://mmbiz.qpic.cn/mmbiz_png/XZByrJJ6uUweTDYunX7L5UJMVricbpnaqhVFrQmMzMEfNXUonOajmvmbshBXXOM1bBEjicS6j0TBoxLTg8VJiasdQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/XZByrJJ6uUweTDYunX7L5UJMVricbpnaqSagDF8sE366C0TYma4Ydbkh25YYHQggZbZTmtX4kP2NB5w3nYDe2YA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/XZByrJJ6uUweTDYunX7L5UJMVricbpnaqd2qic1DKPwV8gGiaLn1dicRfNNpVUl6k97e4uvBL2xTtjbywVWBmqhBkA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_jpg/XZByrJJ6uUweTDYunX7L5UJMVricbpnaq1eTJW9C3ibdPopHWRFzEyLicTWOiclvq3mLs9HrOxGacQX0Z58XPibpx1A/640?wx_fmt=jpeg)

选择模块可单独选择你要检测的漏洞

cmdshel模块

如存在jeecg-boot queryFieldBySql远程命令执行漏洞

选择cmd模块的jeecg-boot queryFieldBySql远程命令执行漏洞

输入你要执行的命令即可

![](https://mmbiz.qpic.cn/mmbiz_png/XZByrJJ6uUweTDYunX7L5UJMVricbpnaqOhr05GItL5GRvfCEqzNfoRX44sqMZEsplDicdeExvSIqG6bSib6emFcA/640?wx_fmt=png)

文件上传模块：

![](https://mmbiz.qpic.cn/mmbiz_jpg/XZByrJJ6uUweTDYunX7L5UJMVricbpnaqTXicnhqFvzPcGh7nBYRERmJIClSzBFFoZibApzIzdvZ9mjzC5sHdnHcA/640?wx_fmt=jpeg)

如存在jeecg-boot jmreport任意文件上传漏洞

![](https://mmbiz.qpic.cn/mmbiz_png/XZByrJJ6uUweTDYunX7L5UJMVricbpnaq7qKoWtQhDWVKXBNaXH3WnZia0WHZJxj9OwkictJvE1dJW3nDp5HRmf0g/640?wx_fmt=png)

shell不再内置，支持用户自定义上传，输入你的shell代码，文件名，点击上传即可

![](https://mmbiz.qpic.cn/mmbiz_png/XZByrJJ6uUweTDYunX7L5UJMVricbpnaq2yjleoiclER6ESZmDv0jNxZDQvSX2SLVhF7BkE4JcoSKrI2wsJGEticQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/XZByrJJ6uUweTDYunX7L5UJMVricbpnaqSIM0DibicCeBD7d3rgXKBJUw6Nz5SEOdWc3fe48icYyVYBtYQZvbTE9kg/640?wx_fmt=png)

批量检测模块：

下载jeecgExploitss jar程序，本地新建文本urls.txt

选择你要检测的模块，点击检测，即可开始批量检测

批量检测，默认只输出存在漏洞的网站

后续根据版本优化再添加其他的批量检测模块

![](https://mmbiz.qpic.cn/mmbiz_png/XZByrJJ6uUweTDYunX7L5UJMVricbpnaquib4ab50ic5g1Ke3xEUJJGvrKZLLlYW8iaFWWO9vDI99FuU58nLTpiaIfg/640?wx_fmt=png)

关注公众号回复“20260108”获取工具地址。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/XZByrJJ6uUzKsSv7UficCMvNU3C1Khiayp4iabicKicKVePCZbMlUKFfStk6mX3Hpf6kh5Zl6vcUoOqGcELngiazX8rg/0?wx_fmt=png)

W小哥

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/XZByrJJ6uUzKsSv7UficCMvNU3C1Khiayp4iabicKicKVePCZbMlUKFfStk6mX3Hpf6kh5Zl6vcUoOqGcELngiazX8rg/0?wx_fmt=png)

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