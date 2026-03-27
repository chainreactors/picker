---
title: 红队工具 - MDUT-Extend 植入高级间谍木马（RAT）全链路分析
url: https://mp.weixin.qq.com/s/okTVeh6Ndclf1sm_qA5UGQ
source: Doonsec's feed
date: 2026-03-26
fetch_date: 2026-03-27T04:29:50.811600
---

# 红队工具 - MDUT-Extend 植入高级间谍木马（RAT）全链路分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J7CSmJcRR8l4ytibYEY3ibUNYicwEZYHM2R6OC9icHznsB4dbCIjhYbNnZ0tZ7Stx2g49Sr0933UJ65XiasDVBPaYP5mK9icvZiam3DvQyxn3tPYY8/0?wx_fmt=jpeg)

# 红队工具 - MDUT-Extend 植入高级间谍木马（RAT）全链路分析

Khan安全团队

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/J7CSmJcRR8nLnbzyvxVjkw4h3MrzZmpkvrIYTBboibvQVrY1p2Oj4SAIib7ObyeQdeGUH0Bp1In2iaQvPMdTaiaoxYOmJaekYUBQF7S3u0v21QY/640?wx_fmt=png&from=appmsg)

```
https://github.com/DeEpinGh0st/MDUT-Extend-Release/issues/22
```

该木马的植入逻辑极其老练，采用了多级跳板和云服务掩护技术：

1. **诱饵阶段**：用户下载并运行 MDUT-Extend 执行 MongoDB 利用功能。
2. **加载阶段 (`https.py`)**：

* 脚本静默安装 `requests` 依赖。
* 利用 **Mapbox API**（合法云服务）作为指令中转站，下载 Base64 加密的第二阶段载荷。

3. **执行阶段 (`pozos.py`)**：

* 载荷直接在内存中 `exec()`，不产生本地文件。
* 建立互斥锁（Mutex）防止重复运行，并在注册表/隐藏目录实现持久化身份识别。

4. **收割阶段**：自动触发全方位的敏感信息窃取模块。

---

## 核心恶意功能拆解

##

通过对 `pozos.py` 源码的分析，该木马的危害远超常规后门：

### 1. 浏览器“核弹级”窃密

木马内置了针对 **Chrome、Edge、Brave、Firefox** 的自动化解密插件。

* **脱库攻击**：它会直接拷贝浏览器的 `Login Data`、`Cookies`、`History` 数据库。
* **绕过加密**：利用 `win32crypt` 调用系统 API 解密受害者存储在浏览器中的**所有网站账号和密码**。
* **Session 劫持**：窃取 Cookies 意味着攻击者可以绕过 MFA（多因子认证）直接接管你的 GitHub、阿里云、公司内网后台。

### 2. 系统画像与历史痕迹搜集

脚本执行后会立即运行 `tasklist`、`ipconfig`、`netstat` 等命令。最危险的是，它会专门提取 `.bash_history` 和 `.zsh_history`。对于安全人员来说，这些历史记录中往往包含**临时 API 密钥、数据库连接字符串或内网渗透路径**。

### 全盘文件外泄（Exfiltration）

###

木马包含一个精密的过滤引擎：

* **目标**：自动搜索全盘（包括外挂硬盘）中的 `.txt` 和 `data.db` 文件。
* **加密外传**：使用 **AES-256-CBC** 加密打包数据，并使用内置的 **RSA 公钥**加密对称密钥，确保只有攻击者本人能解开数据。
* **回传地址**：数据通过 64MB 分块上传至 C2 服务器 `139.99.54.58`。

---

##

## 攻击者技术特征：典型的“Living off the Land”

##

* **云端隐藏**：使用 Mapbox 合法 API 避开防火墙的域名黑名单检测。
* **无文件化（Fileless）**：核心 Payload 全程在 Python 进程内存中运行，逃避传统磁盘扫描。
* **跨平台支持**：源码兼顾了 Windows 和 Linux 的适配逻辑，展现了极高的攻击成本。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aPmkR80bcV3JwGBDpU6XB9v8QmVNuqicT4vSSnibBesxWSwrwSORopnXEPcjahRUcLrTDK5MszhYG4ho8icFMuXMg/0?wx_fmt=png)

Khan安全团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aPmkR80bcV3JwGBDpU6XB9v8QmVNuqicT4vSSnibBesxWSwrwSORopnXEPcjahRUcLrTDK5MszhYG4ho8icFMuXMg/0?wx_fmt=png)

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