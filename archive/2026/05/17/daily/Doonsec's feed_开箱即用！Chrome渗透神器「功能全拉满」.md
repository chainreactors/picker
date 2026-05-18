---
title: 开箱即用！Chrome渗透神器「功能全拉满」
url: https://mp.weixin.qq.com/s/vWzN2Fd7FYY0kpPydt8Nsw
source: Doonsec's feed
date: 2026-05-17
fetch_date: 2026-05-18T06:10:18.056178
---

# 开箱即用！Chrome渗透神器「功能全拉满」

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/HqolA1dQic6ibVOwD0YicGb5K17cwUWtbIB69WEVfW88JjEuaIa4q5zbReeIhrbUB3h8CQFsWZ8NIyrPs1Eh2ia5MkJtwr15kSZaBic4Q49iaTq7s/0?wx_fmt=jpeg)

# 开箱即用！Chrome渗透神器「功能全拉满」

EdinLyle
EdinLyle

HACK之道

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

介绍

*黄油曲奇是一款集成化渗透测试浏览器插件，专为安全测试人员和开发者设计。它提供了丰富的安全测试工具，包括信息收集、信息提取、XSS 测试、SQL 注入测试、端点安全扫描、云存储检测、Shodan 主机信息查询以及多种辅助工具，帮助用户快速识别和评估 Web 应用的安全漏洞。*

*该插件集成了 8 大核心功能模块，覆盖了 Web 应用渗透测试的各个方面。通过直观的用户界面和强大的功能，黄油曲奇使安全测试变得简单高效，即使是非专业安全人员也能轻松操作。*

## 功能特性

![](https://mmbiz.qpic.cn/mmbiz_png/HqolA1dQic6ib6esH1OSW050HcGj1nO0SMjUAicU53x3pUia8qI6YYM1JXiaVNyHiaMlVs8UCPDOKPwypG7ycn5qaGjc7UPNUzicqalGJtZTYpaHXg/640?wx_fmt=png&from=appmsg)

## 系统要求

* **浏览器：Chrome 88+ 或 Edge 88+**
* **操作系统：Windows、macOS、Linux**
* **权限要求：需要以下浏览器权限**

+ activeTab
+ scripting
+ webRequest
+ cookies
+ contentSettings
+ declarativeNetRequest
+ storage
+ tabs
+ contextMenus
+ downloads
+ <all\_urls>（主机权限）

## 工具使用

### 信息收集

信息收集功能中的 Fuzz 扫描部分的扫描字典，师傅们可以自行收集和使用自己的常用字典或者添加内容，在插件的 data/ 目录下自行修改即可。

![image-20260402015008036](https://mmbiz.qpic.cn/mmbiz_png/HqolA1dQic6ibNo5MHF5IK5xcib92UdnenianibicsIwoVA3icns9kficYP2HDrFkJhg4vYHdCSsUDsMYPZol3C27EQRQ8oBToOYx5HZ2PjFk51T9nI/640?wx_fmt=png&from=appmsg)

![image-20260425185854923](https://mmbiz.qpic.cn/mmbiz_png/HqolA1dQic69siauSkkzKE8AdvSCNA2a4d7JMmkgPRibbH0cFDbicLfFfWRJwF9zgMvdDEog4yiakRQtXt4ianClS7sAZ1icsJaSGRKBSKCf3IAdnk/640?wx_fmt=png&from=appmsg)

### 信息提取

![image-20260425185808471](https://mmbiz.qpic.cn/sz_mmbiz_png/HqolA1dQic6ic16qdicumc3eG7SfXyRp4q4CJEwfclZrjibGfbicXNIibYZY6mtuibEs5DtZicWXQjWjUHdAichagKewPCsyU8uGQnhQ4fmPn27pwHmI/640?wx_fmt=png&from=appmsg)

自定义正则提取例如：

id = ""

```
\bid=["'][^"']+["']
```

## ![image-20260402013821029](https://mmbiz.qpic.cn/sz_mmbiz_png/HqolA1dQic69LZv1En5YVoGicWajH9EH7aTXsh88bxqUTshfARqNibDXKRwsNDb1sRJjtHjrP76LJ62TEbRBsIFgTu1fBHeNCaEibpVaCGicFiclg/640?wx_fmt=png&from=appmsg)![]()

### XSS 测试

## ![image-20260425185727200](https://mmbiz.qpic.cn/mmbiz_png/HqolA1dQic6icJBXaA6eqBEIzZicxKuWd28k7f0fa2GPdn7XkrIPaIdQ8MZQpNwTJfTxGnlWVH5rUB696PaNn1e5sGVP79Fiag1AcNNFkW4Lufs/640?wx_fmt=png&from=appmsg)![]()

### SQL 注入

![image-20260425190329813](https://mmbiz.qpic.cn/sz_mmbiz_png/HqolA1dQic6ibenZcSdG3zJDZx72LqCjvu9xDETob1aEZSMlzQQeO0AWAdupPZZw1p6S79QS0VLoPe64pWZkxR8WxO5csOUt5NUr27QSmfyy8/640?wx_fmt=png&from=appmsg)![]()

### 端点安全扫描

![image-20260425185930411](https://mmbiz.qpic.cn/sz_mmbiz_png/HqolA1dQic69E4jRepIm2Po9Lw4GpgXxWXctOYwh6XUMgdMmvyNicvnxvraqDtgh77ZfJgbfVUHpkowFFGCE0VWzuloynJzT3xtnJicEiamEDqc/640?wx_fmt=png&from=appmsg)![]()

### 云存储检测

![image-20260425190255255](https://mmbiz.qpic.cn/sz_mmbiz_png/HqolA1dQic6ibIOPl0HfnmAjGAyfGLicOZGsHCuzdsF7KKtfufvWLyEtkiblluBa7jdJhbS7N1AEe8W6RssPA7ZDN10MO0ha6K5PnRjgbjoibHZg/640?wx_fmt=png&from=appmsg)![]()

### Shodan

![image-20260425190213618](https://mmbiz.qpic.cn/sz_mmbiz_png/HqolA1dQic69ficC6cfoWibg4Qicn6JCon8gORwQ50TicbTcKQSUhUGiczphcGMtSE6Tcf0dZGOW5WUF98h62TJ0NfY80ZadViateLJ5DBsV7gYiaR4/640?wx_fmt=png&from=appmsg)![]()

### 辅助工具

Vue 未授权快速检测

JAVASCRIPT

批量 URL 打开工具

![image-20260425185625815](https://mmbiz.qpic.cn/mmbiz_png/HqolA1dQic6ib8gmt42wfRIibcRunYcKBrqgMBJicv5VTFdyBlJQZhO5fqHeydaezhIKcHBqlTvlibgI6CQ18oqQLZI5GzNbSnh58xyt8sqG2vCM/640?wx_fmt=png&from=appmsg)![]()

## 快速开始

### 安装方法

1. 克隆或下载项目到本地
2. 打开 Chrome 浏览器，进入扩展管理页面（chrome://extensions/）
3. 开启开发者模式
4. 点击"加载已解压的扩展程序"
5. 选择项目目录
6. 扩展将自动安装并在浏览器工具栏显示

### 首次使用

1. 在目标网站上点击扩展图标
2. 选择需要使用的功能模块
3. 根据界面提示进行操作
4. 查看结果并导出报告（如果需要）

项目地址

https://github.com/EdinLyle/Butter\_Cookie

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GzdTGmQpRic1orFibqtmBJd06F33KoWTM6qEUAG7ZbwicA5MhTqx9stelHv8cMgibthiahUBTtgbPgn3ia2bYLpBElTQ/0?wx_fmt=png)

HACK之道

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GzdTGmQpRic1orFibqtmBJd06F33KoWTM6qEUAG7ZbwicA5MhTqx9stelHv8cMgibthiahUBTtgbPgn3ia2bYLpBElTQ/0?wx_fmt=png)

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