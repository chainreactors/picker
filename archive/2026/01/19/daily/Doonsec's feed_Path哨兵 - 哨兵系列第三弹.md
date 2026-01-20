---
title: Path哨兵 - 哨兵系列第三弹
url: https://mp.weixin.qq.com/s/TR_WruOgdlfL5FkyE4N9Gg
source: Doonsec's feed
date: 2026-01-19
fetch_date: 2026-01-20T03:32:54.951430
---

# Path哨兵 - 哨兵系列第三弹

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YqguuzCS2ibthsoMvQCBs4xjUgiaCGRW6S4wq2kIweuv6fYjKodK3FzqeBLq1ekBPebbL8frTIdGQw2uoWdMlZbQ/0?wx_fmt=jpeg)

# Path哨兵 - 哨兵系列第三弹

原创

0xShe
0xShe

安全社

![]()

在小说阅读器中沉浸阅读

# PATH-SB 路径哨兵

> 任意文件读取漏洞检测工具

### 1. 🔧介绍

```
Path-SB 路径哨兵，智能化检测URL中的路径，快速发现潜在任意文件读取漏洞，自动化fuzz，支持Windows和Linux，支持自定义配置/自定义payload。
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YqguuzCS2ibthsoMvQCBs4xjUgiaCGRW6Sx4Sbe2xjiaM6c66zXMmxa13OdVy7Yz1dYZeG6OvqLuUJsE8CCCTD0Wg/640?wx_fmt=png&from=appmsg)

###

### 2. 🌏下载

访问官网：https://sbbbb.cn 找到 - 0xShe工具- 点击进去即可获取解压密码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YqguuzCS2ibthsoMvQCBs4xjUgiaCGRW6STgP7H7Jjb5icuLJbWtNYYtWkqHmH6usb8ZT3QkBmVFA683hT3ibic7F8g/640?wx_fmt=png&from=appmsg)

---

## 功能说明

### 两种模式

**监听模式**：实时监听新请求

* 点击"启动监听"
* 自动测试符合规则的参数

**扫描模式**：扫描历史记录

* 点击"扫描历史"
* 可暂停/继续/停止

### 检测规则

**核心规则**：

1. **必须包含**`.` (点号)
2. **并且包含**`/` 或 `\` (路径分隔符)

**支持URL编码**：自动识别 `%2F``%5C``%2E` 等编码形式

**匹配示例**：

```
✓ file=/etc/passwd          → 有 . 且有 /
✓ path=C:\Windows\win.ini   → 有 . 且有 \
✓ doc=../../../config.php   → 有 . 且有 /
✓ file=%2Fetc%2Fpasswd      → URL编码形式
✓ path=../../test.txt       → 有 . 且有 /
✗ domain=example.com        → 只有 . 没有 / \
✗ email=test@qq.com         → 只有 . 没有 / \
✗ dir=/var/log              → 只有 / 没有 .        *这一块不知道要不要加上 很纠结 等反馈
✗ id=123                    → 无任何特征
```

**优势**：避免误报domain和email，同时捕获所有文件路径参数。

### 配置选项

**Payload类型**

* Linux：针对Linux系统文件
* Windows：针对Windows系统文件

**编码选项**

* 原始编码：根据原请求决定是否编码
* 强制编码：

+ URL编码：强制编码payload
+ 不编码：强制不编码payload

* 暴力模式：编码+不编码都测试

---

## 操作指南

### 查看结果

1. 左侧"URL列表" → 点击URL
2. 中间显示该URL的所有测试结果
3. 点击Payload → 底部显示请求/响应包

### 发送到Burp工具

在底部数据包查看器中右键：

* Send to Repeater
* Send to Intruder
* Copy URL
* ...（所有Burp原生功能）

### 清空结果

点击"清空"按钮 → 清空所有结果和缓存

### 编辑Payload

点击"编辑Payload" → 切换Linux/Windows → 编辑 → 保存

---

## 内置Payload

### Linux (20个)

```
/etc/passwd
/proc/self/environ
/etc/hosts
../../../etc/passwd
/var/log/nginx/access.log
...
```

### Windows (10个)

```
C:\Windows\win.ini
C:\Windows\System32\drivers\etc\hosts
C:\Windows\System32\license.rtf
...
```

---

## 技术信息

* **版本**：1.0
* **作者**：0xShe
* **环境**：Java 8+| Burp 2022.9.5+

---

**让任意文件读取无所遁形！** 🛡️

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/YqguuzCS2ibvXTgfmibh2tJhDohia3n9gXbwZHickdg6lg6JhV149icd6fYfQqcACy0COLDu63hV22pEwMXIjYflB2A/0?wx_fmt=png)

安全社

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/YqguuzCS2ibvXTgfmibh2tJhDohia3n9gXbwZHickdg6lg6JhV149icd6fYfQqcACy0COLDu63hV22pEwMXIjYflB2A/0?wx_fmt=png)

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