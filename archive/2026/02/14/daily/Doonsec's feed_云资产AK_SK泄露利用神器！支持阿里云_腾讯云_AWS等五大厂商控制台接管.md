---
title: 云资产AK/SK泄露利用神器！支持阿里云/腾讯云/AWS等五大厂商控制台接管
url: https://mp.weixin.qq.com/s/vC_J8Kt1QCEbpJsPJm0cTA
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:19:42.311647
---

# 云资产AK/SK泄露利用神器！支持阿里云/腾讯云/AWS等五大厂商控制台接管

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/L9cic5ql9ODwiaHViaN0yjpopMkgOCXu5r4L3pK4mCibjMk5m7ljLeINEeL6eibYF4ibnic7JBxseN4p8Lznf2hYRpZjqEz1A1U3G7CW3cp3hG5xoE/0?wx_fmt=jpeg)

# 云资产AK/SK泄露利用神器！支持阿里云/腾讯云/AWS等五大厂商控制台接管

原创

0xSecDebug
0xSecDebug

0xSecDebug

![]()

在小说阅读器中沉浸阅读

# cloudSec云安全-AK/SK泄露利用工具

>     请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除**。
>
> ***项目地址在文章底部哦***

* 注意：如果本地使用linux搭建，openjdk需要安装字体库，建议使用oraclejdk
* 前端采用vue3,基于buildadmin模板，后端springboot，原接口调用厂商的SDK
* 如果有BUG请提交issue
* ***提示：某些功能会对目标产品造成影响，如密钥对绑定，会导致重启，请慎重使用！！！***
* 另外权限信息获取目前只支持阿里云腾讯与,云服务器执行命令是通过agent来执行的，这个过程中还需要agent权限，光凭agent是否安装无法判断是否可以执行命令，因此为了保证命令执行准确性，扫描时会默认执行一次whoami

## 功能概览

| 厂商 | 产品 | 功能 | 备注 |
| --- | --- | --- | --- |
| 七牛云 | 云服务器 | 列出云服务器/绑定密钥对 | / |
| 云数据库 | / | / |  |
| 存储桶 | 列出文件/单文件下载链接生成/上传文件/导出存储桶所有文件列表 | 因为下载文件过多收费问题，所以改成了导出所有文件列表，然后通过文件名自己筛选即可，界面支持前缀搜索，支持1000条数据实时预览 |  |
| 控制台用户 | / | / |  |
| 华为云 | 列出云服务器 | 列出云服务器/绑定密钥对 | 密钥对操作需要重启服务器 |
| 云数据库 | 获取数据库资源/创建用户 | 不支持开通关闭外网访问，华为云数据库需要单独购买IP |  |
| 存储桶 | 列出文件/单文件下载链接生成/上传文件/导出存储桶所有文件列表 | 因为下载文件过多收费问题，所以改成了导出所有文件列表，然后通过文件名自己筛选即可，界面支持前缀搜索，支持1000条数据实时预览 |  |
| 控制台用户 | 创建控制台用户 | 默认继承父账号权限 |  |
| 阿里云 | 云服务器 | 列出云服务器/执行命令/绑定(还原)密钥对 | 密钥对操作需要重启服务器 |
| 云数据库 | 获取数据库资源/创建用户/开通或关闭外网访问 | 账号继承父账号权限 |  |
| 存储桶 | 列出文件/单文件下载链接生成/上传文件/导出存储桶所有文件列表 | 因为下载文件过多收费问题，所以改成了导出所有文件列表，然后通过文件名自己筛选即可，界面支持前缀搜索，支持1000条数据实时预览 |  |
| 控制台用户 | 创建控制台用户 | 默认管理员权限 |  |
| 腾讯云 | 云服务器 | 列出云服务器/执行命令/绑定(还原)密钥对 | 密钥对操作需要重启服务器 |
| 云数据库 | 获取数据库资源/创建用户/开通或关闭外网访问 | 账号继承父账号权限 |  |
| 集群 | 打开K8S APISERVER外部访问/获取kubeconfig/一键接管K8S | 默认开通外部访问会添加0.0.0.0/0的白名单 |  |
| 存储桶 | 列出文件/单文件下载链接生成/上传文件/导出存储桶所有文件列表 | 因为下载文件过多收费问题，所以改成了导出所有文件列表，然后通过文件名自己筛选即可，界面支持前缀搜索，支持1000条数据实时预览 |  |
| 控制台用户 | 创建控制台用户 | 默认父账号权限 |  |
| 亚马逊云 | 云服务器 | 列出云服务器 | / |
| 云数据库 | 列出数据库资源 | / |  |
| 存储桶 | 列出文件/单文件下载链接生成/上传文件/导出存储桶所有文件列表 | 因为下载文件过多收费问题，所以改成了导出所有文件列表，然后通过文件名自己筛选即可，界面支持前缀搜索，支持1000条数据实时预览 |  |
| 控制台用户 | 创建控制台用户 | 默认最高权限 |  |

## 使用方式

* 默认检测是10个线程

### 添加AK/SK

* 右边按钮对应key更新编辑，任务启动，控制台用户创建
* 添加后选择立即检测或手动执行任务
* 可选择更新时导出key
* 一键停止/启动所有任务 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODxeyqfbiac0Df64Vdic04kfmib5G2UkU9ysGd5iajsgYkCHgxjyyBuoeibbhFeWVCeWHichOc2c5YnMbjBtvMpUkTCpZs8YZWLqFJQDA/640?wx_fmt=png&from=appmsg)
* 权限信息 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODzB7a6Iu5SoBGUQnvQ7Nc1Sb29Tia5ibB9YrulN15a0kua69u8b2mYcrdEAqIricgEO4eWusC9whIeUAibkcDB3icdcibjtfkVIh8Tjc/640?wx_fmt=png&from=appmsg)

### 云服务器

* 对应命令执行，密钥对操作 ![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODx53znWOnfV8uTJnOsDenicOQRfp0BnA2CDjeTHdcGVU45S8gb4gibFFiajI5yX0kcTGEHxzqbKxTibO4P0as73ZSNTUz2TG6uIicV0/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODy7LBetmibzaaf5YKfAficfzgbAicaNbdwYkmQB6mUAqWjk2yiaD8pxZdAqNzejnFmxVvUVpg7ry5n8e5qMcgMmSNYo8NbicJPZHXEw/640?wx_fmt=png&from=appmsg)

### 存储桶

* 对应文件上传，导出文件列表（excel格式） ![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODyMP9rVsv52K9aqiaO8NVnnaFFuzmib2mE7TLYWwhicGy6CfZGmhRlIJVldu1oWucYCTqeMYzYgMcPRt7ALTvTetBQEWrQGrhicic7c/640?wx_fmt=png&from=appmsg)
* 点击上传然后选择文件列表，可预览1000条数据，点击下载可单独下载文件 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODzRFU1D5jNd6gbOZVPrdJibQtKRFx0wByiaR2Kko4c0AwOlTz0kt0Tak7PophcdhiaxuyplOM7Rsygia6VnruRp6a6MpD7rc3ypSP8/640?wx_fmt=png&from=appmsg)

### 集群相关

* 对应的是获取kubeconfig，打开公网apiserver权限，更新信息（主要是开启外网访问后存在一定延迟，需要隔一段时间手动获取外网端点信息） ![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODwjQQ1t23OX5uQa8kgWp4JS0gdAMVb6KFAYR21oEVuteUJ6RpR8B4ROUfbICeG3cONCb73asJ0MhYh8VTMejwnWGGD5iaUWHQ7k/640?wx_fmt=png&from=appmsg)

### 最后则是一键获取k8s权限，需要开通外网访问，点击后将会下载一个sh脚本，linux下执行后将本地安装kubectl连接该集群

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODxRy4siawHgFYD6yzxFneczs9Rm1eMMRkW9MOqwM0L5GZBNOtpDmpC3JmP6vzxuWyTyicLq0N7Osvho54b4usLnR5JzagK53ZtCo/640?wx_fmt=png&from=appmsg)

### 连接成功后将会执行kubectl get node，显示下面结果则代表成功

![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODxkhDNRcAEzPx2MgkPUyKZeGEYbMWcGnNtsfzQr31L6b4icicThSiatbr4GcSUyEspHiaSfyUcM0a2JxtxldZPEQe7ibcVrDYWVic6BY/640?wx_fmt=png&from=appmsg)

### 如果显示下面报错，请在sh脚本所在目录下执行

```
export KUBECONFIG=$(pwd)/kubeconfig
```

![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODyLGJ4llmZnPjSCDfcBbv3n7vXqjzy5Zvx4KsFUCWUrm69fHLs4Z8vzqgah7S1iaRicNtlUDGVClPz1uibRle07KiaM2udFflQOVJw/640?wx_fmt=png&from=appmsg)

### 成功后即可接管K8S

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODyKHZK8ibFvCvYznRBiaEtdWTEhnJibMDCtIUvrib3RSr8whOv5ALXnica2oia18wicO2YtYV6WvicbSDvKKmZFZFOUdC5g4AXV8UNyY6c/640?wx_fmt=png&from=appmsg)

### 控制台用户

* 创建的控制台用户将在这里显示 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODzRnib6SF8ORICIhbwAJicBakRfgOvBdjhuasslAB6AXujyA0Egew1Xq3QB5RBJfibZ5QswNT69OWasxDuEx5E2Anr5D2gib8cxoJY/640?wx_fmt=png&from=appmsg)

### 数据库

* 按钮对应打开/关闭外网，创建数据库账号 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODya26mWqNsaibjtauNEGtVrJ23DJZP6GNW1chlmT19mX6Ojz7Q5n1K3NfqgROmiaYGgV8Plib4iblK5Hrj9BUI1xiam05gMH3riaWZ8Y/640?wx_fmt=png&from=appmsg)

### 文件下载列表

* 此处对应导出存储桶的文件列表表格，状态成功后可下载 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODxAkvDKBDRKsUmuyuHWEOQQNhEAKQHJXicnbbZvN4qr4WYbx947zHqHVKpSPR3Rrel4w1dlK6sNJK03fzGzmwcwHC9hLtj71pf4/640?wx_fmt=png&from=appmsg)

### 导入key列表，为了更新不丢失key

![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODzy2mwNucsVfkCDMfDo4tntVbiaUDqugYib0SMJQicnRiaOanGCExVkkL1kgdvJZG9oaWtvOGWDMxkJyKtw9fh8ibVXbZw2Iz5WUcxU/640?wx_fmt=png&from=appmsg)

## 📖 项目地址

```
https://github.com/libaibaia/cloudSec
```

## 💻 威胁情报推送群

>   如果师傅们想要第一时间获取到**最新的威胁情报**，可以添加下面我创建的**钉钉漏洞威胁情报群**，便于师傅们可以及时获取最新的**IOC**。
>
>  如果师傅们想要获取**网络安全相关知识内容**，可以添加下面我创建的**网络安全全栈知识库**，便于师傅们的学习和使用：
>
>     覆盖渗透、安服、运营、代码审计、内网、移动、应急、工控、AI/LLM、数据、业务、情报、黑灰产、SOC、溯源、钓鱼、区块链等  方向，**内容还在持续整理中......**。

![img](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsGvpzTbNZamyJCmibbqwBWzgKUY4QqOTUNjibmmSiaNJibkPXMznRsC3eia8e4v7wcsibDepNqTft4aB2qw/640?wx_fmt=png&from=appmsg)![img](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsGvpzTbNZamyJCmibbqwBWzg8cDB2ibsdhJVnLBBlicLYjMtyTmOicUQbia7oIMS0Fia7uYtDrKXzULJVgQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnAqueibZX8s1IJDIlA8UJmu3uWsZUxqahoolciaqq65A30ia93jCyEwTLA/640?wx_fmt=gif&from=appmsg)

**点分享**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJniaq4LXsS43znk18DicsT6LtgMylx4w69DNNhsia1nyw4qEtEFnADmSLPg/640?wx_fmt=gif&from=appmsg)

**点收藏**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnev2xbu5ega5oFianDp0DBuVwibRZ8Ro1BGp4oxv0JOhDibNQzlSsku9ng/640?wx_fmt=gif&from=appmsg)

**点在看**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnwVncsEYvPhsCdoMYkI6PAHJQq4tEiaK3fcm3HGLialEMuMwKnnwwSibyA/640?wx_fmt=gif&from=appmsg)

**点点赞**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsGzSr4HnmUgiaibhvSicNIVAsdBq15vPEccY009wRZpHIJlvBl1ACks8gAYQYKicZwEKje2mMc1cia8ibGg/0?wx_fmt=png)

0xSecDebug

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsGzSr4HnmUgiaibhvSicNIVAsdBq15vPEccY009wRZpHIJlvBl1ACks8gAYQYKicZwEKje2mMc1cia8ibGg/0?wx_fmt=png)

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