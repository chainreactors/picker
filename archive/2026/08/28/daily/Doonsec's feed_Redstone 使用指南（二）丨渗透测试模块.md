---
title: Redstone 使用指南（二）丨渗透测试模块
url: https://mp.weixin.qq.com/s/9aK9ki7fgmwcz0Gq20RJxg
source: Doonsec's feed
date: 2026-08-28
fetch_date: 2026-08-29T08:27:47.287537
---

# Redstone 使用指南（二）丨渗透测试模块

# Redstone 使用指南（二）丨渗透测试模块

永恒之锋实验室
永恒之锋实验室

Eonian Sharp

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# Redstone 使用指南（二）丨渗透测试模块

本篇介绍渗透测试模块。该模块是 Redstone 的综合作业台，集成 ESP 端口扫描引擎与 ESD Web 指纹识别引擎，共含扫描视图、终端视图、接口分析、敏感信息、引擎配置、指纹配置、扩展配置、可视化视图、锈化之路、安全隐私十个子页面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vj6VUMJMyibp0OI8oCGbvzObyBkAad3cQxVS6Rd83WbTiaiakUGjpkpHN6So8xp3WRJhiczThFfHiaic6LPSE5MoL113wAtYGh1MGEt2ibFmmLSibts/640?wx_fmt=png&from=appmsg)

初次使用，建议选择一个数据存储位置

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vj6VUMJMyibrbtzhc9SU6pklPTnLFD36pbbnziawQK8FVzeNmQvZV8C4DtET1RRN6GoW1cCnkFm4ibpujJia9RHkbUacsBFmPY1uPIWcxEiaTXFo/640?wx_fmt=png&from=appmsg)

## 一、扫描引擎

引擎安装与配置见：[Redstone 使用指南（一）丨安装配置与界面导览](https://mp.weixin.qq.com/s?__biz=Mzg3NzUyMTM0NA==&mid=2247488776&idx=2&sn=3ab113408b87520e5fa78cebd4368d6e&scene=21#wechat_redirect)

• ESP：端口扫描。支持智能扫描模式、服务指纹识别、HTTP/SOCKS5 代理，以及降低检测风险的 Pulse 间歇式扫描模式。结果输出端口、服务、指纹。

• ESD：Web 指纹识别。支持 JS 分析、响应体获取、路径爆破与登录验证配置。结果输出 URL、状态码、标题、指纹。

## 二、扫描任务基本流程

1. 在「引擎配置」中确认 ESP 与 ESD 路径有效

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vj6VUMJMyibrNyFCmzR4p6yIcvmvibYmloQNoANu8va6Jy33HSHELjB1YOHg6ZM0jKnGxAvAx5n5KUngSgSSS3BNEicGonSYSciciaA7teZHouDY/640?wx_fmt=png&from=appmsg)

2. 在「扫描视图」新建任务

![](https://mmbiz.qpic.cn/mmbiz_png/Vj6VUMJMyibqOLMibqPnLZsUgwWD2kpwckA3dG9ibWUlrjWOONPajsicdm923bNKAiaQrcSiaSLSpBQ8f2GlxKYT1ptibkTOTuET5vdzuY6yjmu62Y/640?wx_fmt=png&from=appmsg)

3. 录入目标，按需添加自定义请求头

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vj6VUMJMyibqPhSgfSC064X7XicvESN1mTZklyjeUcUclcsad6Ivt8iarL0ib0xvEqk74G3nArRP9vlNCEFmlkia2uI1ksBhBQTjxbUpicZ5NWRoE/640?wx_fmt=png&from=appmsg)

4. 选择是否开启 ESP 到 ESD 的自动联动

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vj6VUMJMyibqCM2nypFDUy8LCrQxmeicEN2V61mowJBnt3EujMKA252kDunt9tmRFxx25CEBk09u4Ay2qbJYYV6amvia8xibAFlmwZXb0nSiaboo/640?wx_fmt=png&from=appmsg)

5. 开始执行

6. 在结果区依次查看 ESP 结果、HTTP 入口列表、ESD 结果

7. 按需导出 XLSX 留档

![](https://mmbiz.qpic.cn/mmbiz_png/Vj6VUMJMyibr6aU4fkAEqBaWjVzhmIGGubuyZyVPL32U5JpFvbo0xnkV05XbTZtMKc3wUlQfUnxoux9sLMy5dtJ6qdSlhc3In5MOsbAqQMWw/640?wx_fmt=png&from=appmsg)

若只需快速确认 Web 入口，可重点关注 HTTP 入口列表。任务较多时，建议以任务名与标签标记区分优先级。

## 三、接口分析

ESD 扫描的 JS 文件将被自动提取为 API 路由，按目标域名分组、以树状结构展示。路由可发送至重放神器（按住 Ctrl 或 Cmd 点击路由可快速发送），也可整批发送至字典管理，沉淀为路径爆破字典。

### ESD接口实验室

所有扫描过的接口都被沉淀到实验室进行分析，可通过研究接口的特性和规律整理成字典，可以说是越积累越宝贵

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vj6VUMJMyibp11PQQL8mgDv2aOmnhHevjXe6KIvLVlpwS6ibKaAGjZYON6JQFl5QAMvtpkfyVs0UibicKlqzFYibReRricO6wQXjZD3VsGiaqDtcYY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vj6VUMJMyiboB8W9ib8MmeIrvp6CVXeJeAQGlheE37KECcib1lryaQtmo7Via3G3Uib9K6tB9om1BnxuuxclqDBmibicx5SldsvZODxXteDnkNSNR8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vj6VUMJMyiboLwkZqU2KibEH4jW3NtsKkYbLCNPYcaibYE8FBtic3cq28IUrQmxciaJ5Kx3CtkXF5XwvI0cHIu1VIU6rjicB6dPdCrVeVF2ft5cEw/640?wx_fmt=png&from=appmsg)

## 四、敏感信息

敏感信息页自动汇总 ESD 结果中的手机号、身份证号、银行卡号、邮箱、GitHub Token、ICP 备案号等内容，分为资产、敏感信息、开发、汇总四个子视图，可按目标逐项排查。提取结果需人工复核。

![](https://mmbiz.qpic.cn/mmbiz_png/Vj6VUMJMyibrCAAibO7seia3MOjTrLEZPJpQYFb8JzwaSCJ27v3rUlXQ1nlPh63wwj56jeibjvfMCgfX4zyjarAMT3at85Fj1gCWOUycF6HwELA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Vj6VUMJMyiboHibX7hhGJACuiarIBmUtVkKNWib4ia9XNYG4Y9ibT4agvHetu9RHibyHwPDxdMetXYB3PicoBiceGEcOohz4ibCYKsjicg3paQyrGXZ7J0/640?wx_fmt=png&from=appmsg)

## 五、远程节点

配置远程 Agent 节点后，ESP/ESD 任务可下发至节点执行，进度经 WebSocket 实时回传，本地与远程结果保持一致。

（本章不展开节点相关介绍，内容将放置高级进阶篇。）

## 五、指纹配置

ESP兼容社区大部分指纹格式，因为ES是Rust系武器库，所以也特别推荐使用开源的Rust项目的指纹项目 —— ObserverWard

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vj6VUMJMyiboCZC2vBpgSabIEuBcwIHRUpYQHJgOMNgrwhUS62EyFGicqvsFNwagow75E3KFvxVJmBmBNJ6QQT2wyUnPFc7av2QGOOEc97Ib0/640?wx_fmt=png&from=appmsg)

使用后，可识别大部分指纹，ESP最求精简指纹库，留下高价值指纹，和自定义自己发现的指纹，并预留一个验证窗口，会对目标进行top端口扫描，内置了--save-port参数，目标如果携带端口，那么这个端口会被追加到端口列表中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vj6VUMJMyibpOFO5V6ibJz6JZjDRiaRIt6k2dLaXyPlibNLyvrnHceQkNhn9Sr823eMLznrGA11hhJvtwdPsRMYG9GUCjTbgkEPfHX77ndYjCXE/640?wx_fmt=png&from=appmsg)

## 六、终端视图

终端视图主要用来管理复杂的命令行任务，以及SSH远程管理

例如我们需要精细化使用一些参数时，一些复杂的命令行工具时

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vj6VUMJMyibp9Exib0cq3Q5qreqehIRZc0ABEo0msH2pibmmphYJ1fQmJ02n8fy5D4N1RmdDqgDPon7ia21xmkjgNnqPmuk8ibPbKicvsO1zzONGo/640?wx_fmt=png&from=appmsg)

除此之外，我们可以配置SSH服务器快速连接，对服务器进行管理

打开引擎配置 - 终端管理 配置服务器以及常用命令

![](https://mmbiz.qpic.cn/mmbiz_png/Vj6VUMJMyiboJ4pO2Y3iasAu15mhUaqQ13v9AibxsBdibhPQOmwgoDQ3dAtqDNWCzmNDnKLRdIrVOk890k3S3CJMeFhkFMGuFeSgsACPhw01srY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Vj6VUMJMyibo6AJPMalUZuPGamZfibp2SjLX4rwBlFDIWhiauHmMibaRphAUSeKkFgT9eTUMVxqpe6Jtuekbqc9S4nFZhX9ZfGPy2uAzqgf5kiaA/640?wx_fmt=png&from=appmsg)

配置后即可快速打开服务器播放常用命令

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vj6VUMJMyibqXIYRtO0sdUg99sF42nibTEMF9gmJBjhGictBF0jYF8wcia4QNpqKic8H4eluAoUibJF5QzuXpzE4tWN2wJdEFrIPAI1bMMf2iaaOTM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Vj6VUMJMyibpLbmeickjQd9ypMd9BIb8mjrSu1V4Nj7w6AdEzuqedcwpMqKzPy6CTQzbmDuNm4diaicgtgHkshPCanyaSa9z8ibUp6t62Cz236Uw/640?wx_fmt=png&from=appmsg)

当然，我们还能进行文件管理，上传下载文件编辑等操作

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vj6VUMJMyibqSbSEf8icRKCw83TjR6icadicCIzeGrKHaicGUnlmY4Psrc8eCxkdwr7I7cGztsiae96mGsuZFo3BAgUGBjyRM1e2BjeSQJUkvedU8/640?wx_fmt=png&from=appmsg)

两种方式都可以打开

![](https://mmbiz.qpic.cn/mmbiz_png/Vj6VUMJMyiboEibXnmvFdjaQtrwEBguOMuumsh3L7ezMEGoHn6EspJNdrn6pjguqzbibANOjbfFoAFCGBnjialcC0Mhjaksibx0JAshiaphku1ub0/640?wx_fmt=png&from=appmsg)

当然，可以3视图，边运行命令，边看文件，并进行文件编辑

![](https://mmbiz.qpic.cn/mmbiz_png/Vj6VUMJMyibpcINgDVIlPbZiccAq4YY2S6oFTyfJMC7ouQlRU0ETbwWfwR1zxibUePN61JJuQKoWYwaKO8ticZpSDQQhSwyxiciau8spo7mL2FLTY/640?wx_fmt=png&from=appmsg)

有时候，我们忘记了一些命令，或者工具不知道怎么用，可直接唤出AI助手

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vj6VUMJMyibraYLS2NSuiabdg4MrdclmtAlZGps0zuRicbKOEKcnSKicN7ktQto5gRBaVuRGYfNLwsRf741Mr9vNHCMXJa7pBHXB8j8uuVG4TkU/640?wx_fmt=png&from=appmsg)

AI可获取到终端的响应，并给出回答

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vj6VUMJMyibrTCLGCFuvBxeQX4xv33CbGE2tN4pbbNdtr7yEOPqxf3jqPZQn2icJN2cKkDhGSTqbWTGk9DfrPTpdicbJSGOryppDz0rDWiaAuew/640?wx_fmt=png&from=appmsg)

## 七、本地环境演示案例

### 环境一：CmsWing 搭建

环境搭建，本环境以CmsWing为例演示基本的目录扫描发现后台以及对后台进行爆破：

* 项目地址： https://github.com/arterli/CmsWing
* 准备phpstudy简易开启mysql数据库，按照命令进行启动

修改数据库 /config/sequelize.js

```
{
  dialect: 'mysql',
  host: '127.0.0.1',
  port: 3306,
  database: 'cmswing2',
  username: 'cmswing2',
  password: 'cmswing2',
}
```

修改成你自己的数据库，先创建数据库，然后把数据库配置文件的信息修改成你实际的数据库信息。

启动项目

```
$ npm i
$ npm run dev
$ open http://localhost:7001/
```

启动项目后会自动生成表结构，和初始化信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vj6VUMJMyibpCPQmC5xhU4jf6yMNd4Oddn4yBZBAoXkF9m6QuUY53icstfa0HoUyzibfs6OvBFmZ8yx53tHmV9DuKxl7ibK1mDqqb618zo3tUAU/640?wx_fmt=png&from=appmsg)

开启环境

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vj6VUMJMyibqJMfL3HhLqTVM4qflLTlYdaDKOXB8SANhAeD8hVHMLHDricnEFMDYXMxFzeP1p15DrFQxogUNBN2hj1y8Merv1ibIaDnpZzKEDg/640?wx_fmt=png&from=appmsg)

后台地址：http://localhost:7001/admin账号：admin 密码：123456

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vj6VUMJMyibrtibpewibUQfvUp4fI9HkMkX1c7MJSubRHfib77yL8MbUtT81icCCcV5o8xPEtD2ehDoZhjx8PFfciajOdXjvia2DpLddyUoAFMkklk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vj6VUMJMyibp1ibKrkUGl8QTMepTjGYvYSBicNgW5IKm9lr4tmgwEwGoVnicciaT9kXxnHZNVz8G1Zuic4TkCnXhgLaRQkb86DUFcb6ibt9icGh5FEM/640?wx_fmt=png&from=appmsg)

验证没有问题。

### 环境二：Ruoyi 搭建

环境搭建，本环境以Ruoyi为例演示基本的JS发现后台以及对接口的分析：

* 项目地址：https://github.com/yangzongzhuan/RuoYi
* 准备Kali Parrot用脚本快速安装搭建

![](https://mmbiz.qpic.cn/mmbiz_png/Vj6VUMJMyibrb6KLxRyeh09fwfQW9XbNOo9iac29mTIJPuIYpgRt3IsGFCP7BWIAfU5MpBbZuBpkqAUXbJkW320iaCT3Z2oIkz7g8Sv0NPnShs/640?wx_fmt=png&from=appmsg)

启动后端

![](https://mmbiz.qpic.cn/mmbiz_png/Vj6VUMJMyiboY6jibhFrrFTXxOFVqxibMBT2zNXmL63uialWUiaP1icCQ4xVdoWGAx3NsvzsliaknI7enuricza37icOlXyR8gdodaLOaibXIf1WbWRa4/640?wx_fmt=png&from=appmsg)

启动前端

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vj6VUMJMyiboIId7lukYSAicXWrHHBG5NRQfm1A99x08cFjDSsf1z70ZHr0qYd1IFbYdYfcZfdoIicM5ekJmh8QrNY8wGWkldu5l31QtMrUicCY/640?wx_fmt=png&from=appmsg)

访问

访问地址:       http://<IP>:8888   (本机则 http://localh...