---
title: Chrome 应用绑定加密解密
url: https://blog.upx8.com/4762
source: 黑海洋 - Wiki
date: 2025-04-23
fetch_date: 2025-10-06T22:07:25.743989
---

# Chrome 应用绑定加密解密

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Chrome 应用绑定加密解密

发布时间:
2025-04-22

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
60186

🌐 谷歌近期在Chrome浏览器中推出了**应用绑定加密（App-Bound Encryption）** 技术，提高 Windows 上 Chrome Cookie 的安全性，旨在更有效地保护Cookie、密码及支付信息免受信息窃取程序和黑客攻击。这一安全升级值得肯定，对吧？

其原理简洁而高效：将敏感数据与Chrome独有的应用身份绑定，确保即便其他应用拥有相同用户权限也无法解密。这无疑提高了攻击者的入侵门槛，迫使他们突破更多防线才能窃取用户数据。

**工作原理**

![](https://cdn.skyimg.de/up/2025/4/22/pnq9eu.webp)

不过……我忍不住想挑战一下。为此我编写了一个工具（[github](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3hhaXRheC9DaHJvbWUtQXBwLUJvdW5kLUVuY3J5cHRpb24tRGVjcnlwdGlvbj90cms9cHVibGljX3Bvc3RfY29tbWVudC10ZXh0)）成功破解了该加密机制。

🔒 增加安全防护层固然关键，但这只是防御的一半。

---

用于解密 Chrome 127+ 版本中应用绑定加密密钥的工具，通过 IElevator COM 接口实现，具备路径验证和加密保护功能。

**用途**
解密基于 Chromium 的浏览器（Chrome、Brave、Edge）Local State 文件中存储的应用绑定加密（ABE）密钥，无需管理员权限。

从 Chrome 127 开始，谷歌引入了 ABE 机制：Cookie（未来还将包括密码和支付数据）会使用一个只能由浏览器自身的 IElevator COM 服务解密的密钥进行加密，且调用二进制文件必须位于浏览器安装目录内。

本项目通过向正在运行的浏览器进程注入 DLL（CreateRemoteThread + LoadLibrary），并从中调用 IElevator，从而绕过路径验证要求。

**支持及测试版本**

| 浏览器 | 测试版本 (x64 & ARM64) |
| --- | --- |
| Google Chrome | 135.0.7049.96 |
| Brave | 1.77.100 |
| Microsoft Edge | 135.0.3179.85 |

**⚠注意事项**
注入器要求目标浏览器正在运行。

**构建说明**

1. 克隆仓库并打开 VS 开发者命令提示符（或任何支持 MSVC 的 Shell）。
2. 编译 DLL（负责解密逻辑）：

   ```
   cl /EHsc /LD /O2 /MT chrome_decrypt.cpp ole32.lib oleaut32.lib shell32.lib version.lib comsuppw.lib /link /OUT:chrome_decrypt.dll
   ```
3. 编译注入器（负责 DLL 注入和控制台交互）：

   ```
   cl /EHsc /O2 /MT chrome_inject.cpp ole32.lib shell32.lib version.lib /link /OUT:chrome_inject.exe
   ```
4. （chrome\_inject.exe、chrome\_decrypt.dll）必须位于同一文件夹。

**使用方法**

```
PS chrome_inject.exe <browser>
```

**示例**

```
PS C:\Users\ah\Documents\GitHub\Chrome-App-Bound-Encryption-Decryption> chrome_inject.exe chrome
------------------------------------------------
|  Chrome 应用绑定加密解密工具                |
|  CreateRemoteThread + LoadLibrary 注入      |
|  v0.3 by @xaitax                             |
------------------------------------------------
[*] 定位到 Chrome 进程 PID 16044
[+] Chrome 版本: 135.0.7049.96
[+] DLL 注入成功
[*] 开始 Chrome 应用绑定加密解密流程
[+] COM 库初始化完成
[+] IElevator 实例创建成功
[+] 代理设置成功
[+] 获取 AppData 路径
[+] Local State 路径: C:\Users\ah\AppData\Local\Google\Chrome\User Data\Local State
[+] 提取 Base64 密钥
[+] 解码完成
[+] 密钥头校验有效
[+] 获取加密密钥: 01000000d08c9ddf0115d1118c7a00c04fc297eb...
[+] 为加密密钥分配 BSTR
[+] 解密成功
[+] 解密后的密钥: 97fd6072e90096a6f00dc4cb7d9d6d2a7368122614a99e1cc5aa980fbdba886b
```

**相关链接**

* Google 安全博客([Google Security Blog](https://blog.upx8.com/go/aHR0cHM6Ly9sbmtkLmluL2UyeTNfN2pI))
* Chrome 应用绑定加密服务(Chrome app-bound encryption Services)
* [novvcrash](https://blog.upx8.com/go/aHR0cHM6Ly9haS5kYW5nYmVpLmNvbS9jaGF0L25vdnZjcmFzaA)
* [SilentDev33](https://blog.upx8.com/go/aHR0cHM6Ly9haS5kYW5nYmVpLmNvbS9jaGF0L1NpbGVudERldjMz)

**⚠ 免责声明**
本工具仅用于网络安全研究和教育目的。使用时请确保遵守所有相关法律和道德准则。

[取消回复](https://blog.upx8.com/4762#respond-post-4762)

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