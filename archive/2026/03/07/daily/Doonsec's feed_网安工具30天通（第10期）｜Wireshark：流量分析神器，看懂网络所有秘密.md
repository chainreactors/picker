---
title: 网安工具30天通（第10期）｜Wireshark：流量分析神器，看懂网络所有秘密
url: https://mp.weixin.qq.com/s/K9rwNoL-_6dRaV-7MBp8CQ
source: Doonsec's feed
date: 2026-03-07
fetch_date: 2026-03-08T04:04:30.046439
---

# 网安工具30天通（第10期）｜Wireshark：流量分析神器，看懂网络所有秘密

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Vs6KsYlvMyNrSp79XGd2Ymto8XiaiamGbib4drdLpE2qxqVUibReqibia1wIic7nZCk7G8jic5t8ugSuZqE3ZGkeGTpz33SIDqCZLPCy8eXTogatSBY/0?wx_fmt=jpeg)

# 网安工具30天通（第10期）｜Wireshark：流量分析神器，看懂网络所有秘密

原创

点击关注👉
点击关注👉

网络安全学习室

![]()

在小说阅读器中沉浸阅读

## 一、工具核心定位

**Wireshark** 是全球最主流的**网络流量抓包与分析工具**，被称为“网络世界的显微镜”。

不管是排查网络故障、分析攻击行为、找回明文密码，还是 CTF 流量题、护网溯源，它都是必备神器。

核心用途：

* 抓取网卡所有进出流量
* 过滤 HTTP、HTTPS、DNS、FTP、Telnet 等协议
* 查看数据包原文、定位敏感信息
* 分析攻击行为：端口扫描、暴力破解、注入攻击
* 流量取证、溯源分析

---

## 二、最实用基础操作（新手直接照做）

### 1. 开始抓包 ![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4Vnn5ia95AteynFFMu2MQ9zIeNnRibQgIXWb0t1kl20Lm6EJoG0OYQ3AmpNnngAPTB9LJ890LaebNKF4UpBicgQIwPWlQshApEaOibGISR3ricPJg/640?wx_fmt=svg&from=appmsg)

* 选择网卡 → 点击**鲨鱼鳍图标**开始抓包
* 访问网页/执行操作 → 流量自动被捕获

### 2. 最常用过滤语句 ![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5dMaEiaunfkiaFicpibFfohsaWcVFLm7HhPpdcdOEoGCEibo1z6Gds6V4pXP8ZlW8KTmETg996BB4ibVlLy7lT2Th5sVHH9UZJIzqDtCE0gCNLCTiag/640?wx_fmt=svg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Vs6KsYlvMyNu9O3yEWtwe6Lb2FCqzXBo1cPjBzsO2Iq05TRh8NYicSA7NNL8czECruc8tE9ibKVfmfoicwD2JsEON0Mic1fobJT6ibccbDylA5WM/640?wx_fmt=png&from=appmsg)

### 3. 快速找账号密码 ![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6QTpq9YklcXiasQF0kicqEiakINRUEBseBcXLIu9tV11nZP3e7IyCBuMY6TAcrRIea7uQjZibJNIhYZY7DRw9bzevqVCKbfs4556TekLPsDE9Ykw/640?wx_fmt=svg&from=appmsg)

* 过滤 `http` 或 `ftp`
* 追踪流：**右键 → Follow → HTTP Stream**
* 直接看到明文账号、密码、Cookie

---

## 三、本期CTF真题实战

### 真题名称：流量里藏着的密码 ![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7Cic64yo2q5KWRmSHV1J28pNgiaNsm6LwNRQYAkqq8lRiaX5zdr2qRibj3CLrsiaB5jcfuOCicKkSn02JzlO1vpKFEs2ia7cEyQeMNV68ACjO68HJ1g/640?wx_fmt=svg&from=appmsg)

### 靶机信息 ![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6K2eJ5M8f1fct6Ubm1O2Awy8dNLs2AVayWH1V1ibayDwMCLxvNdSU55ZRj9m8OgrBt0GSPtXJfwywdcBVGG3LwL3Xn9PzOovpGsARG9EOQpqA/640?wx_fmt=svg&from=appmsg)

* 提供一个流量包：`capture.pcap`
* 目标：从流量包中找到账号密码，拿到 flag
* 考点：Wireshark 基础过滤、追踪流、信息提取

---

## 四、完整解题流程

### 步骤1：打开流量包 ![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7tSq6aZXeDq4Ys7rsxicWQ0mJUkUhAmzdB1IDKngrpFMFuUUJLGlVN3hxeYbkx3ibZCJrd3B43sCxscsURhrmurYELibNHljfUs74WZr78GLPicA/640?wx_fmt=svg&from=appmsg)

用 Wireshark 打开 `capture.pcap`。

### 步骤2：过滤 HTTP 流量 ![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4VMsicDje7u2c7HzyZ2yt0Fkt8sg3ajOl07Enk8XALY9PYamGovm1TkRf6Ltgu7fjhLdoWY2HaUYA9cZX3hia5K4XYsEMibyYTAcrrr7SwtkoTQ/640?wx_fmt=svg&from=appmsg)

输入过滤器：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vs6KsYlvMyPY1d0fox6ax6oTrsnbt27N1xRpEKN8vIibibXyouYBoS3jEvf8HBfUic1EyOrMADpcTXMKLibhEkQwWtmvHPeccAkAgMJmz9dsWng/640?wx_fmt=png&from=appmsg)

### 步骤3：找到登录请求 ![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5Pr7rJJbpBX1ic9AsDmNoOzeI3Paywv2UhLxaTT692fdXq3ibfticEyyju1C5v3yUEx98ruiacfR5ZXaP7hkKLzIuugBnUfATpeY3KygYunTXTog/640?wx_fmt=svg&from=appmsg)

找到一个 `POST /login.php` 的包。

### 步骤4：追踪HTTP流 ![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4OZh67yKBxeA9eukBoPltHBBGD2SlcsM5vphUH6XiaibCTyz4X7pORluL6AD29FTicnTzDZYx2EqJiacoLz9v7hgxF7WwkVCLKwzmmwqJIBxGT3Q/640?wx_fmt=svg&from=appmsg)

右键 → Follow → HTTP Stream

直接看到明文提交内容：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vs6KsYlvMyNUIbbxJj1LFwhgZQxibxf4Ud3icEM7gkFeHrGsMGIfN27xvSicXibgbfd6IkdGIYDXib4McgUKmcd1Kib0B8fGGZfB5fibqQaetwPfuc/640?wx_fmt=png&from=appmsg)

### 步骤5：得到flag ![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM41JIFZf3u6BQV2Wgj9g6UamsQtVptPxRZFuibRQxHTlxqftfXhfVZmGuBvqGbD8jBVPZRrBbjBqSbXECZdBarfDDWRKjFwjiar9xzohsgvqbLg/640?wx_fmt=svg&from=appmsg)

根据题目提示，输入账号密码即可获得：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vs6KsYlvMyOib2Jo9q0IP184yzZ4c2Y05nzS1A991jQIMia7AesDOdOHp2lPib8jiaiak7VRePXjic5PEoykyVL3N9icO9zy0bXuA4BHnKJqv2fcso/640?wx_fmt=png&from=appmsg)

---

## 五、实战复盘（新手必看）

1. **CTF流量题 90% 都是送分题**：基本就是过滤+追踪流
2. **HTTP、FTP、Telnet 都是明文传输**，账号密码一抓一个准
3. 实战中：黑客扫描、肉鸡外联、数据外传，都能在流量里现形
4. 学会 Wireshark，你就拥有了“看清网络底层”的能力

---

## 六、福利领取：全系列资料合集

为了感谢大家的一路跟随，整理了 **「200节攻防教程资源包」**这是我整理的精华内容，覆盖网安所有核心知识点，后台回复“学习”即可获取：

全套学习资源，可以点击文末阅读原文领取200节攻防教程

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/iaLzURuoralYx8yXB4LvFH5iaWSZLQIibIy0cjSua3jS1U4ibv8YxBJtIbq5qiahPnPyjH1eicWEbpedhFmOLmYozvFA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=17)

---

## 下期预告（第11期）

**John the Ripper：密码破解之王**

破解压缩包、系统密码、哈希密文，CTF 密码题必备神器。

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