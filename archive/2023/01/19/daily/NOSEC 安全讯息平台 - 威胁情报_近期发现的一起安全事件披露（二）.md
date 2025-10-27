---
title: 近期发现的一起安全事件披露（二）
url: https://nosec.org/home/detail/5057.html
source: NOSEC 安全讯息平台 - 威胁情报
date: 2023-01-19
fetch_date: 2025-10-04T04:17:26.395209
---

# 近期发现的一起安全事件披露（二）

[![](https://nosec.org/home/image/logo.png)](/)

[登录/注册](https://nosec.org/home/caslogin)

[投稿](https://nosec.org/home/caslogin)

[首页](/home/index)
[威胁情报](/home/index/threaten.html)
[安全动态](/home/index/security.html)
[漏洞预警](/home/index/hole.html)

数据泄露

* [新闻浏览](/home/index/leakage.html)
* [图表统计](/home/index/graphshtml)

[专题报告](/home/index/speech.html)
[技术分析](/home/index/skill.html)
[安全工具](/home/index/tool.html)

# 近期发现的一起安全事件披露（二）

![](https://nosec.org/home/image/headImg.png)ddddddd9  996天前

![paper.jpg](/avatar/uploads/attach/image/d886aa897cfbd1c6554ad683792325e9/paper.jpg)

要更像一个猎人；

对内像一个猎人一样探察自己部落的弱点/风险点，然后进行修补，使其更加坚固；

对外像一个猎人一样，察找正在攻击我方部落或者正准备攻击己方部落的对手。

作者：dn9ie@零妖实验室

# 事件摘要

在前段时间，白帽汇发现并披露了一起针对国内的黑客团伙攻击事件，该攻击活动的事件前情请查看：“近期发现的一起安全事件披露 <https://nosec.org/home/detail/5054.html>”

1. 该攻击团伙使用位于香港地区的VPS和有道云笔记托管恶意程序，早期样本托管服务器充当过C2角色；
2. 在论坛或群组相关站点投放向日葵、迈克菲、影音播放、TG图标的downloader程序；
3. 经过测试在本地虚拟机运行结合virustotal情报，国内常用的终端杀毒产品，腾讯电脑管家、火绒个人版、360杀毒+卫士，在最新版情况下依然无法有效检测出全部白加黑恶意程序；downloader程序少数国内厂商可以部分报毒检出。
4. 通过VT和微步结合对比，攻击者使用的样本国内安全厂商相对于国外厂商目前无法有效检出，国内样本累计和威胁情报相对于国外存在一定延迟；

全国各地区与已发现恶意域名通信DNS请求数据分布如下：

![](data:image/png;base64...)

数据来源：Netlab@360 统计日期：2022.11.03--2023.01.18

特征分析

| Domains | IP address |
| --- | --- |
| microsoftdefender.luckfafa.com | 127.0.0.1 / 210.56.54.12 |
| wpsupdate.luckfafa.com | 14.192.67.187 |
| googleupdate.luckfafa.com | 45.116.161.95 |

攻击者使用的早期样本中托管服务器和C2为同一个域名，均在中国香港地区；逐渐的改为使用有道云笔托管恶意程序；

1. 中国香港地区服务器；
2. 有道云笔记托管恶意程序
3. 图片后缀，带密码保护的压缩包文件；
4. 针对国内终端安全软件制作并且持续更新的恶意程序；

**亮点一：使用有道云笔记托管绕过网络检测，避免IP、域名信誉度问题；**

**亮点二：将密码保护的含有恶意程序的压缩包修改为jpg后缀，绕过流量沙箱，同时增加了溯源难度；**

## 受害者特征

* 使用向日葵国内远程控制软件、杀毒软件、破解软件、TG通讯软件，具备以上软件使用习惯的用户一般为企业内的技术、运维、开发人员；
* 根据上述，我们推断这是一起目前仍持续活跃的，针对中国企业技术人员，推测攻击者目的为入侵中国企业内网获取控制权，窃取企业信息和数据的攻击活动；

  # 国内免杀

  ![微步-no.png](/avatar/uploads/attach/image/8ae2fbb96c757264fe80c81628096cdb/微步-no.png)![no-360-2.png](/avatar/uploads/attach/image/e409c4b47ae61185af8d3c7beeece8e5/no-360-2.png)![火绒-no.png](/avatar/uploads/attach/image/bd70dd8ade4d3592577181e1d9fd1677/火绒-no.png)![qq.png](/avatar/uploads/attach/image/0adb66a7acd96f48a2d6f2553d7492d6/qq.png)

  白程序

  ![白程序.png](/avatar/uploads/attach/image/c47ce93bf5cc1ee7471b8ac32bde131b/白程序.png)

  ```
    c81b31f8986cc40ff2d31c3bafd7abdf275826ccb5859eba8d927144e38bc7f3.exe
    数字签名:ASUSTeK COMPUTER INC.

    075f5bdab9194969a0c1e57c2f3e7a341d261f7d0ce252c3e9bf7856f5dd0ba4.exe
    数字签名:China Mobile Group Guangdong Co., Ltd. Mobile Internet Branch
  ```

  ## 释放恶意程序

  ![第一波攻击.png](/avatar/uploads/attach/image/e86b58a408cc99ed7cf4666e159b2762/第一波攻击.png)

downloader：`057e908cd15f95a9768989c0455ae9a24a65c46a5022f5fa1adfe7c7a8a4b6a7.exe`

VT 首次上传时间 2022-11-04 18:05:40 UTC

VT 检出率：31/72

VT中无国内厂商检出

本地测试中腾讯电脑管家检出

```
C:\Program Files\timo\ASUA.exe
 c81b31f8986cc40ff2d31c3bafd7abdf275826ccb5859eba8d927144e38bc7f3

C:\Program Files\timo\ATKEX.dll
ff6557980fac2ca2905eab34746eab8dde4aca4f8870e6c21a0d472969885542

C:\Program Files\timo\debug.dump
9adaaef0ec5d51f3936432d6ac17a3234496c8d4c5fcfec1c036601d676c736c

C:\Program Files\timo\logo.png
deda3dea72ddc36d6899c7bd9711e88831dd5521d9ecf38a28b3df554d4a32cf
```

## VPS托管恶意程序

![第二波攻击.png](/avatar/uploads/attach/image/35e28eebeae4fd0464826dca1dc1f3ac/第二波攻击.png)

downloader：`c5402f8882960bb73a0fd7b1b4badcb12ca96791c189b430cc234fbd2965aa34.exe`

VT 首次上传时间 2022-11-30 17:20:26 UTC

VT检出率：37/72

VT中国内厂商alibaba 、sangfor深信服检出 其余无

本地测试中 腾讯电脑管家 、火绒个人版 、360卫士 + 杀毒 均无检出

```
C:\Users\Public\Videos\EY7Gtwy\8zghB_8\Console.exe
SHA256:075f5bdab9194969a0c1e57c2f3e7a341d261f7d0ce252c3e9bf7856f5dd0ba4

C:\Users\Public\Videos\EY7Gtwy\8zghB_8\Foundation.dll
SHA256:ca686789e96eae34d486a372b1b5e586500a4182b33f718a514742e9f0265ebe

ZP.log
SHA256:2584fca73c9e414327f23d18b161ddabec47c40f07fa3a9f01143b21df3e77ff
```

## YoudaoNote托管程序

![第三波攻击.png](/avatar/uploads/attach/image/9e6d30f9e850e836d148fe6edf4196c3/第三波攻击.png)

downloader：`2bc6170db3ec76a75bac1cb8b063c204c58a8a05a60a480476fd8d30dd3a7b12`

VT 检出率：15/67

VT中国内厂商腾讯检出、alibaba检出，其余无

上传时间：2023.01.03

微步无该样本

将木马程序添加到含有密码的压缩包修改文件后缀为`Z.jpg`的形式存储在有道云笔记；

有道云笔记托管的恶意程序

<http://note.youdao.com/yws/api/personal/file/WEB720a08468a011e3e33d62419914dae5c?method=download&inline=true&shareKey=9fffc94ecccab53a2f9329114662f576>

有道笔记中压缩包SHA256：

7964f1f4714a96331b672882b0531560093162664a028dbfb2d4600dfaf7479c Z.jpg

![密码保护的压缩包.png](/avatar/uploads/attach/image/5cf0df235acdfc805dfe8fbc66cb899d/密码保护的压缩包.png)

```
Console.exe SHA256：075f5bdab9194969a0c1e57c2f3e7a341d261f7d0ce252c3e9bf7856f5dd0ba4mnZP.log
m
n
ZP.log
```

## VT中公开样本

`33fc06ce07dcb94336f2f4897a52f0da0cc62d47b8814803304a4a2a6ea2045c`

VT检出率：40/71 VT中国内无厂商报毒

`9c205ac413192f5c8d8c409620e8f3707f354897df89427fe540f480bac4c760`

VT检出率：27/71 VT中国厂商内腾讯报毒，其余无

# IOCs

microsoftdefender.luckfafa.com| 127.0.0.1 210.56.54.12 | HK

wpsupdate.luckfafa.com | 14.192.67.187 | HK

googleupdate.luckfafa.com | 45.116.161.95 | HK

057e908cd15f95a9768989c0455ae9a24a65c46a5022f5fa1adfe7c7a8a4b6a7

c81b31f8986cc40ff2d31c3bafd7abdf275826ccb5859eba8d927144e38bc7f3

ff6557980fac2ca2905eab34746eab8dde4aca4f8870e6c21a0d472969885542

9adaaef0ec5d51f3936432d6ac17a3234496c8d4c5fcfec1c036601d676c736c

deda3dea72ddc36d6899c7bd9711e88831dd5521d9ecf38a28b3df554d4a32cf

c5402f8882960bb73a0fd7b1b4badcb12ca96791c189b430cc234fbd2965aa34

075f5bdab9194969a0c1e57c2f3e7a341d261f7d0ce252c3e9bf7856f5dd0ba4

ca686789e96eae34d486a372b1b5e586500a4182b33f718a514742e9f0265ebe

2584fca73c9e414327f23d18b161ddabec47c40f07fa3a9f01143b21df3e77ff

2bc6170db3ec76a75bac1cb8b063c204c58a8a05a60a480476fd8d30dd3a7b12

7964f1f4714a96331b672882b0531560093162664a028dbfb2d4600dfaf7479c

075f5bdab9194969a0c1e57c2f3e7a341d261f7d0ce252c3e9bf7856f5dd0ba4

[上一篇：
最佳实践：仿冒站点一键自动化拓线（修订版......](/home/detail/5056.html)
[下一篇：
最佳实践：如何固化IP画像流程](/home/detail/5058.html)

浏览: 56228
评论: 0

![](https://nosec.org/home/image/weibo.png)

#### 最新评论

![](/home/image/loading.gif)
评论正在提交，请稍等...

昵称

邮箱

已有账号，[登录](/home/caslogin)评论

提交评论

[x]  有人回复邮件通知我

![](https://nosec.org/home/image/code.png)

## 相关推荐

[枣庄市教育局被黑](/home/detail/1382.html "枣庄市教育局被黑")

[有黑客在twitter煽动DDos攻击全...](/home/detail/2068.html "有黑客在twitter煽动DDos攻击全球银行")

[利用FOFA做些有趣的事](/home/detail/1858.html "利用FOFA做些有趣的事")

[【转】SQLite 被曝存在漏洞，数...](/home/detail/2070.html "【转】SQLite 被曝存在漏洞，数千应用受影响")

[华顺信安漏洞简报2025年7月10日](/home/detail/5893.html "华顺信安漏洞简报2025年7月10日")

## 热门文章

×

#### 分享到微信朋友圈

![](https://nosec.org/home/image/logo.png)

友情链接：[FOFA](https://fofa.info) [FOEYE](http://www.baimaohui.net/foeye) [BAIMAOHUI](http://baimaohui.net) [安全客](https://www.anquanke.com) [i春秋](https://www.ichunqiu.com)
[指尖安全](https://www.secfree.com)
[2021上海网络安全博览会](http://www.sins-expo.com)

nosec.org All Rights Reserved [京ICP备15042518号-2](http://beian.miit.gov.cn)