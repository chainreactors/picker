---
title: Azure 在线文本转语音（99%真人声音）
url: https://blog.upx8.com/4377
source: 黑海洋 - WIKI
date: 2024-11-03
fetch_date: 2025-10-06T19:15:38.776830
---

# Azure 在线文本转语音（99%真人声音）

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Azure 在线文本转语音（99%真人声音）

发布时间:
2024-11-02

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
27450

# TTS Azure Web

TTS Azure Web 是一个 Azure 文本转语音（TTS）网页应用。通过语音合成标记语言 (SSML) 对输出语音结果微调，可以在本地运行或使用你的 Azure Key 一键部署。

TTS Azure Web is an Azure Text-to-Speech (TTS) web application. It allows you to run it locally or deploy it with a single click using your Azure Key.

主要特性：

* 支持选择语音、语言、风格和角色
* 支持语速、语调、音量的调节
* 支持输出音频下载
* 本地和云端一键部署。
* 支持导入/导出 SSML 配置

该项目适合那些希望在体验 Azure TTS 全功能的同时最小化设置工作的用户。

在线演示： [https://tts.femoon.top/cn](https://blog.upx8.com/go/aHR0cHM6Ly90dHMuZmVtb29uLnRvcC9jbg)

## 入门指南

获取你的 API 密钥

* 需要一张 VISA 卡
* 访问 [Microsoft Azure 文本转语音](https://blog.upx8.com/go/aHR0cHM6Ly9henVyZS5taWNyb3NvZnQuY29tL3poLWNuL3Byb2R1Y3RzL2FpLXNlcnZpY2VzL3RleHQtdG8tc3BlZWNo) 并点击“免费试用文本转语音”
* 访问 [Azure AI services](https://blog.upx8.com/go/aHR0cHM6Ly9wb3J0YWwuYXp1cmUuY29tLyN2aWV3L01pY3Jvc29mdF9BenVyZV9Qcm9qZWN0T3hmb3JkL0NvZ25pdGl2ZVNlcnZpY2VzSHViL34vU3BlZWNoU2VydmljZXM)
* 在“语音服务”块中，点击“创建”
* 创建成功后，在语音服务旁边将列出一个区域和两个订阅 Key 。你只需一个 Key 及其对应的区域

具体可以参考 [Bob](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3JpcHBlcmhlL0JvYg) 官方申请 Azure TTS 的[图文教程](https://blog.upx8.com/go/aHR0cHM6Ly9ib2J0cmFuc2xhdGUuY29tL3NlcnZpY2UvdHRzL21pY3Jvc29mdC5odG1s)，流程只需要到**获取完密钥**就可以了。

## 在 Vercel 上一键部署

[![使用 Vercel 部署](https://camo.githubusercontent.com/20bea215d35a4e28f2c92ea5b657d006b087687486858a40de2922a4636301ab/68747470733a2f2f76657263656c2e636f6d2f627574746f6e)](https://blog.upx8.com/go/aHR0cHM6Ly92ZXJjZWwuY29tL25ldy9jbG9uZT9yZXBvc2l0b3J5LXVybD1odHRwcyUzQSUyRiUyRmdpdGh1Yi5jb20lMkZGZW1vb24lMkZ0dHMtYXp1cmUtd2ViJmVudj1TUEVFQ0hfS0VZJmVudj1TUEVFQ0hfUkVHSU9OJnByb2plY3QtbmFtZT10dHMtYXp1cmUtd2ViJnJlcG9zaXRvcnktbmFtZT10dHMtYXp1cmUtd2Vi)

## 在本地一键部署

```
# 安装 yarn
npm i -g yarn
# 安装依赖
yarn
# 构建生产环境
yarn build
# 运行生产环境服务
yarn start
```

## 开发

在开始开发之前，必须在项目根目录创建一个新的 `.env.local` 文件，并输入你的 Azure Key 和对应的地区：

```
# 你的 Azure Key (必填)
SPEECH_KEY=your_azure_key
# 你的 Azure 地区 (必填)
SPEECH_REGION=your_azure_region
# 输入框最大长度限制 (可选)
NEXT_PUBLIC_MAX_INPUT_LENGTH=4000
```

本地运行开发服务器：

```
# 安装 yarn
npm i -g yarn
# 安装依赖
yarn
# 运行服务器
yarn dev
```

使用浏览器打开 [http://localhost:3000](https://blog.upx8.com/go/aHR0cDovL2xvY2FsaG9zdDozMDAwLw) 查看结果。

项目地址：[https://github.com/Femoon/tts-azure-web](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL0ZlbW9vbi90dHMtYXp1cmUtd2Vi)

[取消回复](https://blog.upx8.com/4377#respond-post-4377)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")