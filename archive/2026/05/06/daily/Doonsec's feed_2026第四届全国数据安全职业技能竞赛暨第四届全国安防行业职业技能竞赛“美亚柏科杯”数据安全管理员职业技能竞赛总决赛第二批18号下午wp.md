---
title: 2026第四届全国数据安全职业技能竞赛暨第四届全国安防行业职业技能竞赛“美亚柏科杯”数据安全管理员职业技能竞赛总决赛第二批18号下午wp
url: https://mp.weixin.qq.com/s/-aokqaJajF8ka7Poj6a2DQ
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:32:50.799316
---

# 2026第四届全国数据安全职业技能竞赛暨第四届全国安防行业职业技能竞赛“美亚柏科杯”数据安全管理员职业技能竞赛总决赛第二批18号下午wp

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5wuTuicCVRBGHRSFpwXoldX29SQXRJWqU1NanPtg4lLvnR6lCbqic9uz4bbBtLTprwvnSsAxBFEdrib3eJrGI3lZ5E7dyQJ3MUy6x6IJibfT4d4/0?wx_fmt=jpeg)

# 2026第四届全国数据安全职业技能竞赛暨第四届全国安防行业职业技能竞赛“美亚柏科杯”数据安全管理员职业技能竞赛总决赛第二批18号下午wp

原创

一把梭安全
一把梭安全

一把梭安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

数据安全

数据校验(50分)

题目描述：某安全运营中心的安全研究员，日常运维时捕获到奇怪的流量，研究员分析发现，这属于某种私有的视频监控传输协议。设备日志显示，存在大量“完整性校验错误”，导致数据包被丢弃。安全研究员从废弃项目文档资料中获取未知版本的协议头文件，请结合算法以及机制，分析提供信息，提取出隐藏数据并提交。

## 解题思路

### 第 1 步：分析头文件

`HIK_SECURE_V1.h` 提供了所有关键信息：

```
#define PROTOCOL_MAGIC "HIK_SECURE_V1"
#define KEY_SEED_TEMPLATE "%s|%s|%s"      // Seed Format: MAGIC | SERIAL | DATE
// Algo: SHA-256 (Truncate to 16 bytes for AES-128)

// Cipher: AES-128-GCM
#define GCM_IV_LEN  12
#define GCM_TAG_LEN 16

// AAD Format: "FRAME:<Sequence_ID>"
#define AAD_PREFIX "FRAME:"

// JSON Schema: { seq, ts, iv (hex), tag (hex), data (hex) }
```

总结出来：

* 算法：**AES-128-GCM**
* 密钥：`SHA256("HIK_SECURE_V1" | SERIAL | DATE)[:16]`
* AAD：`"FRAME:<seq>"` 字符串
* 传输格式：JSON 文本

### 第 2 步：从注册包提取密钥材料

Wireshark 打开 pcap，第 1 个包是明文 JSON 注册包：

```
{
  "msg_type": "DEVICE_REGISTER",
  "protocol": "HIK_SECURE_V1",
  "device_info": {
    "serial_no": "IPC_X7_8848",
    "firmware_ver": "20251225",
    "model": "HK-Vision-X7"
  },
  "status": "ONLINE"
}
```

得到密钥派生三要素：

```
proto = "HIK_SECURE_V1"
sn    = "IPC_X7_8848"
date  = "20251225"
key   = SHA256("HIK_SECURE_V1|IPC_X7_8848|20251225")[:16]
      = de6d6027334237b3cf81a55756fe84c5
```

### 第 3 步：识别隐写包

总共 200 个加密视频包，扫一遍 `data` 字段长度：

* 正常视频帧：100~200 字节左右
* **异常包：`data` 仅 1 字节** ← 共 55 个

55 个异常包就是攻击者注入的隐写包，每包用 1 字节传输 1 个 ASCII 字符。

### 第 4 步：解密提取 flag

按 `seq` 升序，对 55 个隐写包逐个 AES-GCM 解密。

**关键点**：所有 55 个包的 GCM tag 验证全部**失败**——这正是题目里"完整性校验错误"的来源。攻击者注入隐写包时没有计算正确的 tag，设备验证失败后丢弃。但我们作为攻击分析者，可以**跳过 tag 验证**，仅用 `key + nonce + AAD` 还原明文。

把 55 个包解密出的 1 字节按 seq 顺序拼起来即得 flag。

SECRET\_TOKEN\_INFO{019b4a35-5d81-7073-bc07-e5b91e3ac63d}

数据隐藏(40分)

题目描述：某安防监控中心3号摄像头的RTSP视频流遭劫持，安全团队已捕获流量包surveillance.pcap。分析发现监控画面中拍到了可疑车辆，需通过技术手段还原视频并识别车牌号。经检测，该视频流采用RTP协议传输H.264编码数据，使用FU-A分片模式，且视频数据经过简单异或加密（密钥0xAA）。请从Wireshark中导出RTP负载（含12字节头）为二进制文件，该文件中的RTP包长度固定为1412字节（12字节头+1400字节负载）。请编写脚本解密视频数据，重组H.264 NALU并添加起始码0x00000001，最终生成可播放的MP4文件，从中找出可疑车辆的车牌号（格式示例：苏A888888）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5wuTuicCVRBGWBgB1g1P7jHicicKaUH4ic3VDTYhAnQW02zSyxIYWjn28qHtB7pCBM0gNwiaWjs7j2oCd360U8iaSpo0JnBicWyxUL0byLMM8CGe9E/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/5wuTuicCVRBGcqXiarkzZVVRKzm3wG8bJzQjwojvXnd31sS9BIoic6wLlwH40t3uTzC4B44q5xM6fSTZ7yhTCRhicPAezZDYZT7hiber2gQAO3Lo/640?wx_fmt=png&from=appmsg)

导出payload

然后进行xor

![](https://mmbiz.qpic.cn/mmbiz_png/5wuTuicCVRBG9gGDYkuNkvb3278po5oXmRTqzXpEKhnMicdzH85LoxHJYfR6rLqWmTpketmgPMzCS2a5OpxicGRMSImSMnIAicTRo75fjaZVUfk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5wuTuicCVRBGp13nYfZPIgWKXdo53u269II7x4tN8B0O1fu5L25MzgRj2w9aqCYX72ObePYFIlRYI2X9eo4ICZKibTKw3hew2pO5ERiaDpUIcI/640?wx_fmt=png&from=appmsg)

答案  京A598550

数据分析

 溯源分析

【题目1】日志分析某安防平台的运维人员在日常巡查的时候，发现平台的流量监控设备出现异常告警，他立即关闭的平台的业务并导出相关日志文件，请你分析日志文件，找出黑客的IP和攻击方式。【答案标准】

请你提交黑客的IP地址和攻击方式并提交

例：黑客的IP地址为192.168.1.1，攻击方式为文件上传，则最终提交192.168.1.1\_文件上传

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5wuTuicCVRBEVM48uxr5HqRDOnRrhfkR4hSKDSOSwID7OGCXxzCnIyMiaZ1Ln5wzvYeS3icwcIIJ7V6y8R9xmGyE40YypbLuia1f87icXLDb7ozE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/5wuTuicCVRBGQGNMbOjCic0tgGBNiatIKmsjrSoTAat6ib2NOfffAa2ryOicSskMQ6hDtqk6wqJSB2bXLLD7ibnlXzWyDBYYsQoUV9WSa46W2x8fg/640?wx_fmt=png&from=appmsg)

答案  213.54.123.103\_SQL注入

【题目2】内存分析

运维人员在分析完日志后，将系统的内存信息保存了下来，以便后续的溯源工作。请你分析内存文件，找出黑客放置的挖矿程序。

【答案标准】

请你分析附件中的内存，找出黑客放置的挖矿程序，提交挖矿程序的全名

例：挖矿程序名称为wakuang.exe，则最终提交wakuang.exe

![](https://mmbiz.qpic.cn/mmbiz_png/5wuTuicCVRBGicEtOZYMQicWra51gs1RZjKBmRCdV1MMiaM4YGrLJNIeaD170pCTZEfiaRneQtib0S1kgleWYfnF4EXTyTMWia0O9DaAR9CkkdV17U/640?wx_fmt=png&from=appmsg)

答案  winlogon.exe

【题目3】溯源取证

请你分析上题中发现的挖矿程序，找出黑客的矿池域并作为答案提交

【答案标准】

请你根据上题中找到的挖矿程序，继续进行内存分析，找出黑客挖矿的矿池域名并提交

例：黑客的矿池域名为aaa.com，则最终提交aaa.com

![](https://mmbiz.qpic.cn/mmbiz_png/5wuTuicCVRBExDodHk2vL1GXqspUpjpyb6REKfPZ9znJJX5LU4iciamuNksraGsWyGSddIY8Xiaf89QTkiblDxm00peT2T3Swnh0odLG7cpiaSzdU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/5wuTuicCVRBFT8FxR8YhxW6tiauUerGYeaO13Jr7A1UXOOPH94bTicA4S1LVDp0SxUJeFLLibMDKWK2tbiahyfy617WYO2ZmH3trVal2icnPInjzQ/640?wx_fmt=png&from=appmsg)

答案  pool.supportxmr.com

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/ia8fjTFQuYh9TzoFJXukO3SPRHgDqtX98JkqXmZslibicapMtIia8sKyxFCQIHj5cZ07wJsXutfAI36ibD4FlN8b0XA/0?wx_fmt=png)

一把梭安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ia8fjTFQuYh9TzoFJXukO3SPRHgDqtX98JkqXmZslibicapMtIia8sKyxFCQIHj5cZ07wJsXutfAI36ibD4FlN8b0XA/0?wx_fmt=png)

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