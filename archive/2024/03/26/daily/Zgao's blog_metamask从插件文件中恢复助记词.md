---
title: metamask从插件文件中恢复助记词
url: https://zgao.top/metamask%e4%bb%8e%e6%8f%92%e4%bb%b6%e6%96%87%e4%bb%b6%e4%b8%ad%e6%81%a2%e5%a4%8d%e5%8a%a9%e8%ae%b0%e8%af%8d/
source: Zgao's blog
date: 2024-03-26
fetch_date: 2025-10-04T12:09:01.301415
---

# metamask从插件文件中恢复助记词

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# MetaMask从插件文件中恢复助记词

* [首页](https://zgao.top)
* [MetaMask从插件文件中恢复助记词](https://zgao.top:443/metamask%E4%BB%8E%E6%8F%92%E4%BB%B6%E6%96%87%E4%BB%B6%E4%B8%AD%E6%81%A2%E5%A4%8D%E5%8A%A9%E8%AE%B0%E8%AF%8D/)

[3月 25, 2024](https://zgao.top/2024/03/)

### MetaMask从插件文件中恢复助记词

作者 [Zgao](https://zgao.top/author/zgao/)
在[[web3](https://zgao.top/category/web3/)](https://zgao.top/metamask%E4%BB%8E%E6%8F%92%E4%BB%B6%E6%96%87%E4%BB%B6%E4%B8%AD%E6%81%A2%E5%A4%8D%E5%8A%A9%E8%AE%B0%E8%AF%8D/)

![](https://zgao.top/wp-content/uploads/2024/03/image-43-1024x1024.png)

上周研究了一下如何从小狐狸的插件文件中恢复助记词。结合官方描述是在知道密码的前提下，可以从插件文件中提取vault字段在官方提供的解密页面进行恢复。

<https://metamask.github.io/vault-decryptor/>

文章目录

[ ]

* [插件目录](#%E6%8F%92%E4%BB%B6%E7%9B%AE%E5%BD%95 "插件目录")
* [获取vault](#%E8%8E%B7%E5%8F%96vault "获取vault")
* [解密助记词](#%E8%A7%A3%E5%AF%86%E5%8A%A9%E8%AE%B0%E8%AF%8D "解密助记词")
* [hashcat字典爆破](#hashcat%E5%AD%97%E5%85%B8%E7%88%86%E7%A0%B4 "hashcat字典爆破")
  + [钱包hash格式转化](#%E9%92%B1%E5%8C%85hash%E6%A0%BC%E5%BC%8F%E8%BD%AC%E5%8C%96 "钱包hash格式转化")
  + [下载metamask最新加密算法的hashcat模块](#%E4%B8%8B%E8%BD%BDmetamask%E6%9C%80%E6%96%B0%E5%8A%A0%E5%AF%86%E7%AE%97%E6%B3%95%E7%9A%84hashcat%E6%A8%A1%E5%9D%97 "下载metamask最新加密算法的hashcat模块")
  + [字典枚举](#%E5%AD%97%E5%85%B8%E6%9E%9A%E4%B8%BE "字典枚举")

## 插件目录

以Chrome为例，小狐狸插件配置文件目录为：

```
C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\
```

注意：插件源码和配置文件并不在同一个目录下。插件的ID可以在chrome://extensions中看到。

![](https://zgao.top/wp-content/uploads/2024/03/image-41-1024x637.png)
![](https://zgao.top/wp-content/uploads/2024/03/image-39-1024x422.png)

## 获取vault

这里的ldb文件是Google的leveldb数据库文件，需要用特定的方式打开。而在log文件中也能找到加密后的vault，直接用记事本打开搜索KeyringController。

![](https://zgao.top/wp-content/uploads/2024/03/image-40-1024x434.png)

复制vault对应完整的json。

## 解密助记词

![](https://zgao.top/wp-content/uploads/2024/03/image-42-1024x532.png)

## hashcat字典爆破

### 钱包hash格式转化

<https://github.com/hashcat/hashcat/blob/master/tools/metamask2hashcat.py>

暴力破解之前需要将格式转换为hashcat支持的格式。使用上面的脚本进行转换。

```
python3 /root/Downloads/metamask2hashcat.py --vault wallet | tee wallet.hash
```

![](https://zgao.top/wp-content/uploads/2024/03/image-44-1024x395.png)

### 下载metamask最新加密算法的hashcat模块

由于metamask变更过几次钱包的加密算法，所以hashcat以前的26600、26610模块都已经过时了。前一个月有大佬更新了最新的metamask模块，需要在github下载导入hashcat的modules模块。

[https://github.com/flyinginsect271/MetamaskHashcatModule](https://github.com/flyinginsect271/MetamaskHashcatModule?tab=readme-ov-file)

![](https://zgao.top/wp-content/uploads/2024/03/image-45-1024x747.png)

下载后解压，如果用的Windows就导入dll文件，Linux就导入so文件。

如果用的kali，默认模块路径为：

```
/usr/share/hashcat/modules
```

![](https://zgao.top/wp-content/uploads/2024/03/image-46-1024x409.png)

### 字典枚举

```
hashcat -a 0 -m 26650  wallet.hash rockyou.txt
```

![](https://zgao.top/wp-content/uploads/2024/03/image-47-789x1024.png)

钱包密码能否破解成功还是取决于你的密码字典中是否包含有正确的密码。

Post Views: 1,841

赞赏

![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114105.jpeg)微信赞赏![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114100.jpeg)支付宝赞赏

###### Zgao

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

### 发表评论 [取消回复](/metamask%E4%BB%8E%E6%8F%92%E4%BB%B6%E6%96%87%E4%BB%B6%E4%B8%AD%E6%81%A2%E5%A4%8D%E5%8A%A9%E8%AE%B0%E8%AF%8D/#respond)

Δ

版权©2020 Author By : Zgao