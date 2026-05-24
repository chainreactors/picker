---
title: SRC 每日漏洞复现学习系列（第 8 篇）：反射型 XSS 漏洞详解与报告模板
url: https://mp.weixin.qq.com/s/ZQwt43XOwi5RVr9VUa_oFA
source: Doonsec's feed
date: 2026-05-23
fetch_date: 2026-05-24T05:59:23.218803
---

# SRC 每日漏洞复现学习系列（第 8 篇）：反射型 XSS 漏洞详解与报告模板

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Vs6KsYlvMyPNQiaDFYSibqKKdNzCXeNI3Q71fQYVtia61Ms3YKLJX5dia8iaibGIMqYZk8wicwvZws1dTmycoI4NibfzoOFpWclDWwo3M9Gn3x9WIo8/0?wx_fmt=jpeg)

# SRC 每日漏洞复现学习系列（第 8 篇）：反射型 XSS 漏洞详解与报告模板

原创

点击关注👉
点击关注👉

网络安全学习室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 反射型 XSS 漏洞 完整讲解 + 可直接提交报告模板

反射型 XSS 属于高频基础漏洞，和存储型 XSS 同属主流 XSS 类型，无数据持久化存储，仅访问恶意链接时临时触发，测试门槛低，是入门必学内容。

## 一、漏洞基础认知

### 漏洞原理

网站直接将 URL 携带的参数内容回显页面，未做字符过滤与转义编码。恶意脚本不会存入服务器，仅用户打开带恶意参数的链接时执行，也称作非持久型 XSS。

### 主要危害

构造钓鱼链接诱导他人点击，窃取会话 Cookie、劫持账号权限，篡改页面展示内容，存在社工欺诈类安全风险。

## 二、挖洞选目标思路

重点排查具备参数回显的功能

* 站内搜索、关键词展示页面
* 页面跳转、错误提示、弹窗提示模块
* 标题自定义、消息提示类接口
* URL 包含 keyword、msg、title 等可控参数地址

## 三、漏洞复现实操步骤

### 步骤 1：常规访问页面

正常访问带参数的搜索页面

```
https://xxx.xxx.com/search.php?keyword=测试文字
```

页面直接展示传入的关键词内容。

### 步骤 2：构造测试脚本

修改参数嵌入 XSS 测试语句

```
https://xxx.xxx.com/search.php?keyword=<script>alert(document.domain)</script>
```

### 步骤 3：核验漏洞状态

访问链接后页面弹出域名弹窗，脚本成功执行，确认反射型 XSS 漏洞存在。

## 四、SRC 标准漏洞报告模板

### 漏洞标题

某企业搜索功能存在反射型 XSS 漏洞，可构造恶意链接执行非法脚本

### 漏洞等级

中危

### 漏洞描述

站点搜索接口 search.php 的 keyword 参数未对外部传入数据做安全过滤与转义处理。攻击者可拼接带有恶意脚本的访问链接，诱导用户点击访问。脚本触发后可窃取用户会话信息、操控账号状态、篡改页面信息，对用户账号及网站运行造成安全威胁。

### 复现步骤

1. 进入网站搜索页面，确认参数可在前端页面回显；
2. 在 URL 参数中插入 XSS 测试代码，拼接生成恶意访问地址；
3. 访问构造后的链接；
4. 页面弹窗正常弹出，脚本运行生效，漏洞复现完成。

### 影响范围

1. 盗取普通用户与管理员 Cookie 信息，劫持登录会话；
2. 伪造页面内容，发布不实违规信息；
3. 制作钓鱼链接，诱导用户泄露账号隐私数据；
4. 借助漏洞发起后续渗透攻击，扩大安全影响。

### 修复建议

1. 对尖括号、引号、连接符等特殊字符进行拦截过滤；
2. 页面输出数据时统一做 HTML 编码转义；
3. 配置 CSP 安全策略，限制未知脚本运行；
4. 校验外部传入参数格式，阻断恶意代码传入。

### 漏洞证明

（粘贴正常访问页面、弹窗触发页面、参数修改截图，敏感信息打码处理）

## 五、新手学习忠告

1. 搜索、提示类页面优先检测该漏洞，修改 URL 即可快速验证；
2. 区分存储型与反射型差异，针对性书写报告内容；
3. 上报时标注链接诱导风险，提升漏洞评定等级。

## 六、文末学习福利

如果你也是零基础、想参加竞赛网安但不知道从哪开始，可以点击文末阅读原文领取200节攻防教程，帮你少走弯路。后续我会持续更新网安实战、就业、副业相关干货，关注我，带你从零基础一步步靠网安变现。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/iaLzURuoralYx8yXB4LvFH5iaWSZLQIibIy0cjSua3jS1U4ibv8YxBJtIbq5qiahPnPyjH1eicWEbpedhFmOLmYozvFA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=17)

## 后续更新

每日更新经典 Web 漏洞实操讲解与报告模板，零基础循序渐进学习网络安全，稳步提升漏洞挖掘能力。

#SRC漏洞复现 #反射型XSS #Web安全入门 #网络安全学习 #漏洞报告模板

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