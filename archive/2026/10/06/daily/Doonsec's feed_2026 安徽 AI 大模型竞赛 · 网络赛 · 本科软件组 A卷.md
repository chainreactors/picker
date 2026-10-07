---
title: 2026 安徽 AI 大模型竞赛 · 网络赛 · 本科软件组 A卷
url: https://mp.weixin.qq.com/s/Dpg7rjvRFQXiL7xeLb7UUA
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:51:08.863672
---

# 2026 安徽 AI 大模型竞赛 · 网络赛 · 本科软件组 A卷

# 2026 安徽 AI 大模型竞赛 · 网络赛 · 本科软件组 A卷

原创

識.
識.

0xNyx

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 第 1 部分：人工智能算力平台的使用（15分）— 纯操作

**本地操作**：装 Xshell / Xftp（解压"安装文件.zip"）。

**Xshell 连接**

**Xftp 上传**

**Linux 解压**（Xshell 中执行）：

```
cd /root/workspace
tar -zxvf Qwen3_5-0_8B.tar.gz
tar -zxvf Qwen3-Embedding-0_6B.tar.gz
ls-l Qwen3.5-0_8B/ Qwen3-Embedding-0_6B/
```

**截图**：①Xshell 登录成功；②Xftp 上传后 workspace；③解压命令及解压后文件。粘贴到答题卡第一部分。

## 第 2 部分：大模型离线部署的实现

### 2.1 安装第三方库

![](https://mmbiz.qpic.cn/mmbiz_png/icPMQgcMTD2fJ9qBYIUo6ay3ibLq4WcN0EY86ictMPiatfUUAJFia6sRc0wy6JfGOy73nZQlibbhpJBIYaZ4sOJ0A1fo51D7unqNVIWQg7IBlzSoM/640?wx_fmt=png&from=appmsg)

### 2.2 补全 Qwen\_model.py（两处填空）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icPMQgcMTD2fGick7NUiajPzl1JABAVJhAMzEGswlXdmeSWyvRH1bYQFicbKfic0b4exZVa2Wl9LOA98Iql1NnnkEUyL42G3Dyx75oSG3ZVreiamw/640?wx_fmt=png&from=appmsg)

### **答案**：填空① = 模型路径；填空② = `tokenizer(prmopt_text, return_tensors="pt").to(device)`运行后输入家乡名（如"阜南县"）即可对话。

### 2.3 Embedding 向量化（task2\_embedding.py）

![](https://mmbiz.qpic.cn/mmbiz_png/icPMQgcMTD2dUEZsmoyib0HBPzDkiajBv04WDNyJttgAjqGmsy67bFH6EAaUE4TNVxaXickDrmOSN14FicPaxxSFKQdic8lPXqNiayhfCAaWricM9v8/640?wx_fmt=png&from=appmsg)

## 第 3 部分：大模型提示词的设计（20分）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icPMQgcMTD2eFudUchXAzJFctmiaVyZfRvwxXY9iczy7aBn2dia43xDZ6SCWIYgBebj3qAXWtibwpgPKPUYWfqib3ib3hv0ksEyOm98ts7YuNvicQCU/640?wx_fmt=png&from=appmsg)

****预期输出**（输入题目样例后）：`{"反馈类型":"退货申请","涉及商品":"蓝牙耳机","问题描述":"使用三天后断连，左耳无声","期望处理":"退货"}`**

## 第 4 部分：RAG 智能问答系统的搭建

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icPMQgcMTD2dcevkPlmaaurRXpSLyickoiajmWLka1RCcB1iaKdOyMibApkjhExTCx1NQibUuXZu5xUMyvia3bGegPnFd7cPpR4m3RBCh0DGOKtEYs/640?wx_fmt=png&from=appmsg)

## **预期回答**：试卷第四部分是考查基于RAG技术的智能问答系统搭建，分值为25分。

## 第 5 部分：大模型的综合分析（20分）— 文档

## 秘密

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/icPMQgcMTD2ceTCkDez0Piat8aPQyHu06KEJDNNd4u19ZCweicJEoK4tnFV6nQBcXzmV90K7UTllfDM75weNK6tmntI3BhMrkMiaU9bg5ZiaL1EM/0?wx_fmt=png)

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