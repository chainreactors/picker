---
title: 网安工具30天通（第6期）｜Netcat：网络瑞士军刀，反弹Shell必备
url: https://mp.weixin.qq.com/s/i-QqQ-C9yxhy9R0JqbpC7w
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:21:02.892159
---

# 网安工具30天通（第6期）｜Netcat：网络瑞士军刀，反弹Shell必备

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Vs6KsYlvMyMDr1hd2q5icPvSSYjgAYLkMHLGEZlhEHE04zm9XMOZDO72szbB45snacBCMVnfIaHCelzfVksOJF3ZjchDXh61S85nWsLuFiajI/0?wx_fmt=jpeg)

# 网安工具30天通（第6期）｜Netcat：网络瑞士军刀，反弹Shell必备

原创

点击关注👉
点击关注👉

网络安全学习室

![]()

在小说阅读器中沉浸阅读

## 一、工具核心定位

Netcat 简称 **nc**，被称为「**网络瑞士军刀**」。

体积小、功能强、几乎所有系统都自带，是 CTF、渗透、内网环境里**最基础、最隐蔽、最离不开**的小工具。

核心用途：

* 端口探测
* 监听端口、接收反弹 Shell
* 文件传输
* 简单后门 & 反弹连接
* 内网不出网机器的通信桥梁

---

## 二、实战必用命令（直接背）

### 1. 监听端口（等反弹 Shell 最常用） ![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6TNjmVTAr7pIRcJotHKiaxCqgcjQwa3OjfmNFzHZg54ibyMmRgyrJ8Hxbj71tEQuAuN5y9RJ6Y9sQ7Z75GIialteNNkrmb6pbXvoQgTAyLICavw/640?wx_fmt=svg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Vs6KsYlvMyOdRphswQibicv1k2greJiaqBLrbGPAvrpDVst3NHvicSQ4c56cGWibGF9M5HtBq0XSxOiaz9Cd9RjJn3YWvS5hOhSpd8hCftk7EWDJ4/640?wx_fmt=png&from=appmsg)

### 2. 连接目标端口（探测服务） ![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7EvRM1B9NzNYgxwGcjx3svhKpibMea9uFiav6LJ2Atd1flZUH3tKtD8mtk5xanBdmbiaxQcFo5Vn59ARSVyn3VuXsuM9PuFZ6sbkuJvhN8ro58A/640?wx_fmt=svg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vs6KsYlvMyMFPPPssjOMxJBzLPjMGFbKo96qlzJ91KmDLtU2v01fjVQeRLCHC2RyxGk2jOa5718uia6gvb5ucjoOpHPEETOzKrwib6sxYfnXU/640?wx_fmt=png&from=appmsg)

### 3. 发送文件 ![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4TpzqzYMcTS5fUWUESiaFUNexmhzoRUPiaxvIcHwSnM06X66F2OicibOYLuRNwfNtrXzDsBmnOugXLSNXZ7icdKPy58M2Il20AxQ1G6fFmmE3hX0Q/640?wx_fmt=svg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vs6KsYlvMyOSrOlib6ib2x093DwwichgqY7o1OpvQePlulxPpYFQKfGjQyJpfENelwk44xpGa8NfcM72jnB7usTcR19oojc39jRdccicN4xhr8E/640?wx_fmt=png&from=appmsg)

### 4. Linux 经典反弹 Shell ![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7XicmNlEhvCWrQiaFURicfcTOfH6db6c5G3P0bzARQIRruEMTzjKZNadibtDCTqiceupcwkNWEuwK8yegv3xUSicnaK90WhUIcMCgZKLAt2B1MVSSg/640?wx_fmt=svg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vs6KsYlvMyPtEVhRsgTytMBlgunjORsr3y1eqlUQ11Ns0397ibqpgTvVpPtvFKskcKFJABV8CCcibevf8Nm62hZj1zBek4ichWE1dlj6ib5icSc4/640?wx_fmt=png&from=appmsg)

---

## 三、经典CTF真题实战

### 真题名称：最简单的内网后门 ![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4B23ibuoWdyQDSlicpxJTia3IWvLmGhhI5s0Y8LIeBEXqtFowqMsaRdjl0Js0AfbB6QXPQ1lyq1tLTmokPMz8xrp9Ff8g62LEfCmhjasPWjOpqw/640?wx_fmt=svg&from=appmsg)

### 靶机信息 ![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4hadh5YbWqcOkS57hHuJ0xPbklG2erVpWRWhOvET48IRslgS4ibTtsibHQepibRaibkZibC4sCFK2Driczw3elNeRX7FI4qHh6iaBrCnmxb9t9wyC8A/640?wx_fmt=svg&from=appmsg)

* 开放端口：80、22、9999
* 网站存在文件上传漏洞，上传了一句话脚本
* 目标：拿到反弹 Shell → 读取 flag

---

## 四、完整解题流程

### 步骤1：本地开启监听 ![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7qgQtWfbs8k3OR2uG9kRCWVibN7jV7k8vFtxM8VdU2QvFaaqRvFpsIVWOtYV5ggNz98CK2CqRibsqdlrDj5vNfG1e163NhblRqLNqVBIia6gWoQ/640?wx_fmt=svg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vs6KsYlvMyN88k3X51JibBlo3JBX4pIs0Nia1Mh45paTE4os8eefCaECXoyr2rBKQL5ic8SRmD7ZgR6YBWJYQgBYrw9FRicvvEiac47NYe9hCGZs/640?wx_fmt=png&from=appmsg)

### 步骤2：在靶机执行反弹命令 ![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM74qWtbVa3ibQMibG0r0X4K3eUPdHzbqd1LGwRBAxMAvnAr4SD7f7hITJz3z8icvqydAQDERMF9VHSoY8XiaSvzbLRgxqVLR8ibwZhCsyG42iaYqEOA/640?wx_fmt=svg&from=appmsg)

通过文件上传 / 命令执行 运行：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vs6KsYlvMyOa659pRLPn1opiaTmZuoWfAKdUtOPibQtm3icPnEmIdCxM3HyOsaoqSMdrKmRDjU35btIsGwEWHia7U4ia9IGbcOxItJzCBWZ98RsI/640?wx_fmt=png&from=appmsg)

### 步骤3：成功拿到 Shell ![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6pbCyFEyRViat66x74JJcabIZ3T5sXu9JZvdVSJibgLq2e4huG5vEyxRQyqoDWVMJ1VWe4icXO38h2M4eOud0meDnZQwzw4sO48ib43hxNvW1Z0A/640?wx_fmt=svg&from=appmsg)

监听端立刻获得靶机权限：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vs6KsYlvMyP1B60Unutwjaia0l0CicZrYs0FEhttroiajDjk7d6ia4msfiboszVP4Gh7yXKNPuxdSRibnAf4ebXLzesVqGxJOTYCzG0kPDnXViac3Y/640?wx_fmt=png&from=appmsg)

### 步骤4：提权并获取 flag ![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6oVwIzBVP2x6huK8AWoeibbiceFL79dHqAzUXlibJNdqzoVU6nPmCibIECicmEQqBKOFugiaYrojW1nITtA2k1uelibibbGicH5PuEpW2tDcIvejNCEQQ/640?wx_fmt=svg&from=appmsg)

flag：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vs6KsYlvMyMIicwGhibDyaZUuEhJsDT1q3NJxbv1RqLCFINuJuKIFqhaESZfkoORptb3Jn5qMZ1ERiaQGzTh9xAQMsib2w67AJHG2A19Uictp6M8/640?wx_fmt=png&from=appmsg)

---

## 五、实战复盘

1. **nc 是反弹 Shell 最基础工具**，不会 nc 就等于不会内网渗透
2. 很多不出网、低权限机器，**只能靠 nc 回弹**
3. 实战中经常遇到：没有 bash、没有 python，**只有 nc 能用**
4. 监听命令 `nc -lvnp 端口` 是所有渗透人员肌肉记忆

---

## 六、福利领取：全系列资料合集

为了感谢大家的一路跟随，整理了 **「200节攻防教程资源包」**这是我整理的精华内容，覆盖网安所有核心知识点，后台回复“学习”即可获取：

全套学习资源，可以点击文末阅读原文领取200节攻防教程

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/iaLzURuoralYx8yXB4LvFH5iaWSZLQIibIy0cjSua3jS1U4ibv8YxBJtIbq5qiahPnPyjH1eicWEbpedhFmOLmYozvFA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=17)

---

## 下期预告（第7期）

**sqlmap：全自动SQL注入神器**

一键脱库、查库、查表、查字段，CTF Web题神器

真题：《最常见的注入点》

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralYfTVkr1yhiasbN03K2QuRu04rw6cCa7lx8kbE5uGoeTArEW3nCoRN0Y8dQDQjrCtTycTCjUxGmicvw/0?wx_fmt=png)

网络安全学习室

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralYfTVkr1yhiasbN03K2QuRu04rw6cCa7lx8kbE5uGoeTArEW3nCoRN0Y8dQDQjrCtTycTCjUxGmicvw/0?wx_fmt=png)

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