---
title: 开源一个 OTP 管理工具-口令盒子
url: https://mp.weixin.qq.com/s/OlO3O15u_U-CrH6VDt-ASQ
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:48:04.861998
---

# 开源一个 OTP 管理工具-口令盒子

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BowImrBK4tLgpccicrGZzlbOkGPuHwL2zFIe2Uyk8S5yAvD0ECeWj93xN3vZZDoibM0rsUW2zv3nmoKSZ2s5icRnYWcwQ37D6gusHbdzxpZwLs/0?wx_fmt=jpeg)

# 开源一个 OTP 管理工具-口令盒子

原创

adra1n
adra1n

YY的黑板报

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

先说下背景，为啥要做这个，互联网上的 otp 管理工具不少，开源的也有，但是发现存在一个问题，不开源的要不全是广告，要不没办法同步，同步还需要收费，开源的找了半天，https://github.com/beemdevelopment/Aegis 这个还是比较满足需求，但是用久了，换手机时候发现一个问题，他没有同步功能，需要把文件导出来再导入进去，后来想还不如自己做一个。

使用的工具介绍下：OpenCode+OpenSpec+Superpower+hy3，现在腾讯的 hy3 模型可以免费使用，赶紧在这段时间内完成，也算薅一把羊毛。

具体其他几个工具都是干啥的，大家可以网上查查看，简单来说，安装了这几个之后，你只要自然语言描述就可以做项目开发了，后续任何需求都可以通过聊天方式进行。

用时 60 分钟，完成了初版开发，界面和Aegis类似，但是去掉了一些用不到的设置和功能，做了精简。

### 地址：

https://github.com/adra2n/otpbox

### 简介：

一款注重隐私与安全的 Android 两步验证（2FA / TOTP）认证器应用。所有密钥均在本地加密存储，支持指纹 / PIN 应用锁，并可选地通过你自己的 GitHub Gist 进行端到端加密同步。

### 功能：

* **扫码添加**：使用 CameraX + ML Kit 实时扫描 `otpauth://` 二维码
* **图片导入**：从相册选择含二维码的图片自动识别
* **手动录入**：填写密钥（Base32）或粘贴 `otpauth://` 链接
* **JSON 导入**：支持口令盒子自有备份格式与 **Aegis 未加密导出**
* **Google Authenticator 迁移**：解析 `otpauth-migration://` 批量导入
* 编辑服务名 / 账号 / 备注，删除账号
* 首页搜索、排序（自定义 / 按服务名 / 按账号）

为了安全和同步，实现了数据加密和 github 的上传：

### 安全

* **SQLCipher** 加密数据库，密钥由 Android Keystore（硬件级，若支持）封装
* 敏感配置存于 **EncryptedSharedPreferences**
* **应用锁**：指纹 / 面容 / 设备凭证解锁
* **6 位 PIN 码**备用解锁（PBKDF2 加盐哈希）
* **自动锁定**：立即 / 1 分钟 / 5 分钟
* 默认开启 `FLAG_SECURE`，阻止截屏与录屏
* 关闭系统自动备份，防止密钥外泄

### 备份与同步

* **加密导出**：PBKDF2-HMAC-SHA256 (600k) 派生密钥 + AES-256-GCM 信封
* **GitHub Gist 同步**：手动推送 / 拉取，云端仅存密文
* 按账号 ID 合并（`updatedAt` 最新优先，尊重删除墓碑），多设备安全合并
* 备份密码与应用锁 PIN 相互独立

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/SvuJD1DySG2d6mQWxGEyagnIWESbzcu70bFm0XE7XrypIlcD3ic3MJ28Xibqic0Crfaltk51bVKOibr7Xg0fGASj9Q/0?wx_fmt=png)

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