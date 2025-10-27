---
title: 手把手教你写 hacking 脚本
url: https://mp.weixin.qq.com/s?__biz=MzI5MDQ2NjExOQ==&mid=2247498546&idx=1&sn=0c49e2038dde3e9fea5038751e11f806&chksm=ec1dcb1adb6a420c2b2e6699b80d8c8135ae52e0e11becf800b439b261f17f015caedda038b8&scene=58&subscene=0#rd
source: 信安之路
date: 2023-03-21
fetch_date: 2025-10-04T10:09:33.418202
---

# 手把手教你写 hacking 脚本

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sGfPWsuKAff8TArABiabOkDO1lUjQNeTTpicRbNxZQtZnrEl7xF91AojMfwWMGEN0UOOhA7vtCZzW5VMicXunooicg/0?wx_fmt=jpeg)

# 手把手教你写 hacking 脚本

原创

myh0st

信安之路

脚本开发能力是每一个安全从业者都必须掌握的，在未来的工作中，有非常多的场景用到脚本自动化，能自动化实现的一定不要手工来搞，比如日志分析、应急响应、渗透测试中都会用到脚本自动化。

近一个月在星球分享了二十节关于渗透自动化过程中编写的脚本，其中涉及多个 python 核心库的使用，比如 requests、re、socket、threading、queue、subprocess 等。

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAff8TArABiabOkDO1lUjQNeTT9LiaRPd7gkf6G3XwONPb8WlzBtiamh0h4IfNnMqg9zVLRW6wS4Zib0BnQ/640?wx_fmt=png)

脚本开发的学习，在有目标训练的情况下，可以很好的掌握，未来使用将近 40 天的时间训练自己的脚本开发能力，同时还可以掌握渗透测试的基本流程，是个不错的学习途径，课程规划如图。

**参与直播培训的小伙伴，在课程结束时，每人赠送一套补天、360公益的半自动漏洞提交系统一份，让你发现的漏洞，更方便提交，解放双手。**

实训计划：20230325 - 20230502，每隔一天上一节课，上课时间 晚 8 点 - 9 点，持续 近 40 天，录播会同步更新至知识星球

| 时间 | 课程内容 | 基础内容 | 核心功能 |
| --- | --- | --- | --- |
| 20230325 | python 基础介绍 | 环境安装，基本语法，系统常见库 | helloword |
| 20230327 | 补天注册厂商爬虫 | requests 库、re库、文件读写 | 分析补天平台获取厂商注册域名的方法 |
| 20230329 | 基于域名获取备案信息 | requests 库、re 库，文件读写 | 分析站长之家获取备案域名的方法 |
| 20230331 | 多平台获取高权重网站 | requests 库、re 库，文件读写 | 分析各个平台获取 top 网站的方法 |
| 20230402 | 海量域名批量查询权重 | requests 库，re 库，多线程，文件读写 | 分析爱站网权重查询的方法 |
| 20230404 | 域名被动收集 | requests 库，re 库，多线程 | 分析被动收集域名的方法 |
| 20230406 | 子域名枚举技术 | 基础库 | 基于第三方工具枚举子域名，如何提高准确率，以及对结果的解析 |
| 20230408 | 端口扫描 | 基础库 | 基于第三方工具做端口扫描，如何提高准确率并对结果进行解析 |
| 20230410 | 端口指纹识别 | socket 库，多线程 | 端口指纹识别的方法 |
| 20230412 | 网站验证活 | requests 库，多线程 | 基于网站响应内容，识别重复网站的方法 |
| 20230414 | 网站信息入库 | pymysql 库 | 数据库设计以及入库操作 |
| 20230416 | 网站内容获取 | requests 库，re 库 | 网站不同编码获取正确内容 |
| 20230418 | 基于网站内容实现指纹识别 | re 库，文件读写 | 网站指纹的提取与识别方法 |
| 20230420 | 基于指纹结果实现 POC 自动扫描 | requests 库，subprocess 库 | 常规系统 POC 分类 |
| 20230422 | 针对未识别出的系统实现通用 poc 扫描 | requests 库，subprocess 库 | 通用组件 POC 分类 |
| 20230424 | 调用第三方爬虫获取 url 并入库 | subprocess 库，pymysql 库 | url 去重方法 |
| 20230426 | 针对 GET 参数 URL 自动化漏扫 | requests 库，subprocess 库 | 获取 url 列表，调用 xray，上传结果 |
| 20230428 | 针对 POST 参数 URL 自动化漏扫 | requests 库 | 基于 xray 被动扫描，实现漏扫 |
| 20230430 | 网站备份扫描 | requests 库，多线程 | 备份文件名组合方式，验证备份存在的方法 |
| 20230502 | 课程总结与漏洞半自动提交系统交付 | 仅需填写漏洞复现的内容即可 | 补天、360 亿万守护计划两个平台的漏洞的半自动化提交 |

### 报名方式

定价 999/人，早鸟价 799/人，送：

* 价值 512 信安之路知识星球 一年
* 价值 128 的 成长平台账号一个，价值 512 的内部 文库 账号 一个
* 价值 256 的补天、360 公益漏洞半自动提交系统一套

添加微信 myh0st，或者扫描下面的二维码添加，支付 799 即可报名该课程，仅限前十名，超过十名，报名费恢复原价 999，先到先的，数量有限

![](https://mmbiz.qpic.cn/mmbiz_jpg/sGfPWsuKAfeCNvcOIWzcvvXEDpFSmCDsnAoLeo614ZYEetzBAcULQ8Do1M1CLHTicmR7dFUAZQMp2ia8DxOpbxqQ/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAff6G9jJ5AdPvZ0Fgia0Qm6X5X9Jkm8coDOxGE5UhriblyFP93bTgsDZKRib73zicNBGwibb2MPs9bXH4pA/0?wx_fmt=png)

信安之路

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAff6G9jJ5AdPvZ0Fgia0Qm6X5X9Jkm8coDOxGE5UhriblyFP93bTgsDZKRib73zicNBGwibb2MPs9bXH4pA/0?wx_fmt=png)

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