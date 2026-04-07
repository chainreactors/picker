---
title: Universal-POC Validator || 万能POC验证器
url: https://mp.weixin.qq.com/s/H0-ogtipSCBX0iHpzu4QRg
source: Doonsec's feed
date: 2026-04-06
fetch_date: 2026-04-07T04:28:57.564959
---

# Universal-POC Validator || 万能POC验证器

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/XwvIIOgh4ZHT1TYLWzNcZ4ymHicsVUhcNBnMMrHI1zdz0XxYoklPjicgpvWsVkRdISVqfZibNQKqt4dXvQzSCZ3Y6JSkZ0xaibhX4A134g7Ny5s/0?wx_fmt=jpeg)

# Universal-POC Validator || 万能POC验证器

原创

aqwzaa 万知安全
aqwzaa 万知安全

安全wz啊

![]()

在小说阅读器中沉浸阅读

**工具获取**

回复:POC

免责声明

本工具仅用于安全测试和漏洞验证，使用本工具必须遵守相关法律法规。使用者应在获得授权的情况下使用，禁止用于任何非法活动。作者不对使用本工具产生的任何后果负责。

前言

在攻防演练、众测等实战场景中，n-day 漏洞的快速、批量验证是提升效率的关键。传统方案需针对 Xray、Nuclei 、Yakit等框架编写适配 POC，流程繁琐、响应滞后。Universal-POC-Validator（万能 POC 验证器）以原生 HTTP 数据包解析为核心，无需二次开发，支持直接复用各类 POC，搭配批量验证能力与极简 Web 界面，开箱即用，可高效完成漏洞快速验证，为安全从业者提供通用、高效的漏洞验证工具。

适配场景:盒子上榜，新洞速刷，edu通杀rank，通用型漏洞nday批量验证

本工具是对此前[长篇-Redis从入门到进阶](https://mp.weixin.qq.com/s?__biz=MzkzNTk3NzE3NA==&mid=2247484224&idx=1&sn=78bbbfd5b90393744f1553766544df73&scene=21#wechat_redirect)文章的补充

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XwvIIOgh4ZET6ibRcCuWDF6mQZSRPg4ib4ud7SAHbkyZubhbPgdvjORdfosTeo9ML1mCpWCufRTVRXrrcxibicNyuy6gmlGqMIZ46ZvlicicibibxEg/640?wx_fmt=png&from=appmsg)

简绍

Universal-POC Validator

万能POC验证器

**Universal-POC Validator** 是一款专业的安全测试工具，由公众号「安全wz啊」开发，用于漏洞验证和POC（概念验证）测试。

该工具采用本地服务+网页界面的架构，提供了直观、高效的漏洞验证体验，特别适合安全测试人员和渗透测试工程师使用。

## 功能特性

* ✅ **本地服务自动启动**：双击即可运行，无需复杂配置
* ✅ **自动打开网页界面**：友好的用户界面，操作简单直观
* ✅ **Burp Suite 代理集成**：所有流量自动转发到Burp Suite，便于分析和调试
* ✅ **智能POC解析**：支持多种格式的POC数据包解析
* ✅ **单文件运行**：无需安装Python环境，携带方便
* ✅ **跨平台兼容**：在Windows系统上运行稳定

## 技术架构

* **网络**：本地HTTP服务（127.0.0.1:6880）
* **代理**：Burp Suite 集成（127.0.0.1:8080）

## 使用方法

### 1. 启动程序

双击 `Universal-POC validator.exe` 文件即可启动程序。

### 2. 程序运行流程

1. **启动阶段**：程序自动启动本地服务器
2. **界面打开**：自动打开浏览器显示操作界面
3. **配置检查**：自动检测Burp Suite代理连接
4. **测试执行**：用户输入目标和POC后执行测试
5. **结果展示**：实时显示测试结果和响应内容

### 3. 配置 Burp Suite

1. 启动 Burp Suite
2. 在Proxy选项卡中，确保监听地址为 `127.0.0.1:8080`
3. 确保Intercept功能已开启（如需查看请求详情）
4. 无需其他特殊配置，工具会自动使用该代理

### 4. 基本操作步骤

1. **输入目标地址**：在"目标IP"输入框中填写目标服务器地址
2. **粘贴POC数据包**：在"POC数据包"文本框中粘贴完整的HTTP请求数据包
3. **点击测试**：点击"测试"按钮执行验证
4. **查看结果**：在"测试结果"区域查看响应内容和状态
5. **分析流量**：在Burp Suite中查看完整的请求和响应详情

## 运行截图

### 主界面

![](https://mmbiz.qpic.cn/mmbiz_png/XwvIIOgh4ZFiajxMJk24XqIZwvibVd3FBTHmAc3bU87DIqiaYvJcRujickXibOoCvSCjWUVGb13wlwDVhvyqLpibTm7ZLwibuQHbP7m8CY0tPgmcaE/640?wx_fmt=png&from=appmsg)

### 操作界面

**漏洞数据包示例**：

经过测试某网站存在任意文件读取漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XwvIIOgh4ZEcDMiadHxK4JbGxsicnVbYxwum2IDq954ibicrbOQE9RJey2C7B6yplmswRrq9rOwueTXZU21ibIia5n91hkpFkxQuxibGuqNrPhWEtA/640?wx_fmt=png&from=appmsg)

**指纹识别结果**：

通过查找指纹得到

![](https://mmbiz.qpic.cn/mmbiz_png/XwvIIOgh4ZHicOQVPNybtCWPnZLAanT0rr8PJvuK5a8zOZ0XZmVpbFjs1L3P0icqBAQmZZdfhAqhcyf5b6tE2fuLsZwrO5WVAUkapp0vvdwFk/640?wx_fmt=png&from=appmsg)

**测试配置**：

将请求数据包和目标IP进行添加

![](https://mmbiz.qpic.cn/mmbiz_png/XwvIIOgh4ZGJicjfZx3omNzu0ibibtGpFx2chia2rLxAsicSc17pPCUe1wPibg4jHV7MNiaD3n8QcLZl0TOZMvj7e3lM4rgEp91axfzPWNPMjjtibN0/640?wx_fmt=png&from=appmsg)

### 测试结果

![](https://mmbiz.qpic.cn/mmbiz_png/XwvIIOgh4ZFicKJbpj9EYQucHZnAsEEscTxbhtWxiaw631ofpyac79X5hv8eyyDQ6F8YjX0R1YjTMKRqYqoJn8ZSUcfQI8yJpmicfWzsZ5bdWg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/XwvIIOgh4ZEx6xvdyQsEHnvvUXu3mibE5pJMP3Y4ZZ4cM0eia7OqroTesRP79CzfpHyR0eAxMLicTeLuJBkJJcx7WKqLoF65YcEpiaWo1Nf8faA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XwvIIOgh4ZFTNWjDFOTtP6NRExK56v5CwzazAFBHAj5jVRV4U4F9SK2PBqC9X88BuHgcoqicaK1kvhA8fib084bOB6AiafibL3bMU5nDVbq9ia4o/640?wx_fmt=png&from=appmsg)

## 常见问题与解决方案

### 1. 程序启动失败

* **原因**：端口 6880 被占用
* **解决方案**：关闭占用该端口的程序，或重启电脑后再试

### 2. 无法连接Burp Suite

* **原因**：Burp Suite 未启动或端口配置错误
* **解决方案**：确保Burp Suite已启动并监听 127.0.0.1:8080

### 3. 测试无响应

* **原因**：目标服务器无法访问或网络问题
* **解决方案**：检查网络连接，确保目标服务器可达

### 4. 临时文件问题

* **现象**：运行时会在临时目录生成文件
* **说明**：这是PyInstaller的正常工作机制，程序退出后会自动清理

## 注意事项

1. **安全使用**：仅用于授权的安全测试，禁止用于非法用途
2. **网络环境**：确保网络连接正常，目标服务器可达
3. **Burp Suite**：必须启动并正确配置Burp Suite
4. **端口占用**：确保 6880 端口未被其他程序占用
5. **程序退出**：关闭命令行窗口即可完全退出程序

## 技术支持

如有问题，请检查：

* 端口 6880 是否被占用
* Burp Suite 是否正常运行
* 防火墙设置是否允许本地连接
* 目标服务器是否可达

## 更新日志

* **v1.0.0**：初始版本

+ 实现基本的POC验证功能
+ 集成Burp Suite代理
+ 提供网页操作界面

结尾

**工具获取**

免责声明

获取方法:公众号回复**POC**获取下载

本工具 Universal-POC-Validator 仅用于合法授权的安全测试、漏洞研究，仅限在自建靶机或已获书面授权的系统中使用。严禁用于任何违反《网络安全法》《刑法》等法律法规的非法行为。使用者因违规使用产生的一切法律责任与损失，由其自行承担，与作者、开发团队及「安全 wz 啊」公众号无关，作者保留最终解释权。

往期推荐

[躺着去挖值钱漏洞支付逻辑-思路总结](https://mp.weixin.qq.com/s?__biz=MzkzNTk3NzE3NA==&mid=2247484493&idx=1&sn=001b8c9ad1c26a63e7676bd147ce856b&scene=21#wechat_redirect)

[长篇-Redis从入门到进阶](https://mp.weixin.qq.com/s?__biz=MzkzNTk3NzE3NA==&mid=2247484224&idx=1&sn=78bbbfd5b90393744f1553766544df73&scene=21#wechat_redirect)

[记攻防后续的纯网盘社工](https://mp.weixin.qq.com/s?__biz=MzkzNTk3NzE3NA==&mid=2247484096&idx=1&sn=cb42c04c73f6091961e76d754231f99c&scene=21#wechat_redirect)

[一键梭哈式安装 | 信息收集工具ARL资产侦察灯塔](https://mp.weixin.qq.com/s?__biz=MzkzNTk3NzE3NA==&mid=2247483795&idx=1&sn=20ea2788b21c18906abaa86b6c604f04&scene=21#wechat_redirect)

[别再忽略建站"默认页面"背后的隐秘入口挖掘](https://mp.weixin.qq.com/s?__biz=MzkzNTk3NzE3NA==&mid=2247483757&idx=1&sn=f1ebcf77738051a5698f59f81fa133e7&scene=21#wechat_redirect)

[记一次寻找swagger引发的意外收获](https://mp.weixin.qq.com/s?__biz=MzkzNTk3NzE3NA==&mid=2247483679&idx=1&sn=c0a82b4dc0061d6a1c592e46de4ab1da&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/63E2URbmPgRBBMwWia08k5ma6d0HKcIwruDjHhhoTfM2UnWBXbjRhZ14ylA3276GqKg52lEDykNfjKCFOjDIicVg/0?wx_fmt=png)

安全wz啊

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/63E2URbmPgRBBMwWia08k5ma6d0HKcIwruDjHhhoTfM2UnWBXbjRhZ14ylA3276GqKg52lEDykNfjKCFOjDIicVg/0?wx_fmt=png)

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