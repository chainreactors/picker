---
title: 面向APP/Web 加解密逆向分析的工具
url: https://mp.weixin.qq.com/s/YBKCGTC5CIBUo0_cux5vWg
source: Doonsec's feed
date: 2026-07-06
fetch_date: 2026-07-07T06:00:47.780642
---

# 面向APP/Web 加解密逆向分析的工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oQ0sWhcqsVlgdQgpSqMQ7l3o1dNkNRicDneG0gygByehGhbTOQrKHuicMZpibXuBOu9yNQMMt8gwOYmMew1fuSg3uXYBCG5NvPAoHavMpgxouY/0?wx_fmt=jpeg)

# 面向APP/Web 加解密逆向分析的工具

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 285，阅读大约需 2 分钟

## 前言

面向 APP/Web 加解密逆向分析、渗透测试人员的可视化解密框架

项目地址：https://github.com/CuriousLearnerDev/CipherBridge

在 APP 逆向、安全测试和接口联调过程中，经常会遇到：

* • 请求体经过 AES / DES / SM4 等加密
* • 参数或请求头带有 MD5 / SHA256 / HMAC 等签名
* • Burp Suite 抓到的全是密文，无法直接改包重放

## 核心特性

* • AI 自动生成 mitmdump 插件代码
* • 可视化配置 AES / DES / 3DES / SM4 / RSA 等加解密流程
* • Burp Suite 双向加解密桥接
* • 支持扩展自定义 Python 函数
* • 浏览器 Hook + AI 自动分析生成脚本
* • 内置加解密测试工具
* • 自动识别 Base64 / Hex / JWT 等编码
* • 项目导入导出（`.cbproj.zip`）
* • 深色 / 浅色主题切换
* • 支持 Windows / macOS / Linux

## 环境要求

* • Python 3.10+
* • Windows / macOS / Linux

## 安装

```
# 克隆仓库后进入目录
git clone https://github.com/CuriousLearnerDev/CipherBridge.git
cd CipherBridge

pip install -r requirements.txt

# AI 自动化分析使用浏览器采集时需要（可选）
playwright install chromium
```

启动 GUI：

```
python gui.py
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVnZaZeoHXsDO84uaI7X5qIFp4nPu7v2o0x1E2FusV30bs4WZToDP0Jp6cqhhywsEZEicBRiaU9k3AUFsziauFdWbmP1ACywI6snYU/640?wx_fmt=png&from=appmsg)

dc761a642446d41536c67e2635f6dddc.png

## 总结

项目地址：https://github.com/CuriousLearnerDev/CipherBridge

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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