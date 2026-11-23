---
title: PHP CTF 离线速查手册 - PHP CTF Handbook
url: https://mp.weixin.qq.com/s/MZCSsJqCCav2mi85H7aZ9w
source: Doonsec's feed
date: 2026-11-22
fetch_date: 2026-11-23T10:02:09.178206
---

# PHP CTF 离线速查手册 - PHP CTF Handbook

# PHP CTF 离线速查手册 - PHP CTF Handbook

GSDK
GSDK

GSDK安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

01项目地址

`https://github.com/writerosee/php-ctf-handbook`

02项目介绍

打 CTF 线下赛，赛场断网，比赛进行到一半突然想不起来 `phar` 反序列化的利用细节，或者一个伪协议的参数写法：

`没有网，PHP 官方手册查不了
赛前整理的笔记东一坨西一坨，翻起来像考古
payload 找到了，还要现敲现改
比赛环境不让带资料？手册就藏在浏览器里`

**PHP CTF Handbook** 是一个专为 CTF 线下赛断网环境准备的 **PHP 离线速查手册**，成品是一个 13MB 的单页 HTML，下载双击即用，不用装任何环境。内容分三部分：**PHP 官方中文手册的全量索引**（11,930 条）、**196 条 CTF 实战技巧**（附 990 段可直接复制的 payload）、以及一个本地运行的工具箱。赛前联网拉一遍 CVE，比赛中手册会补上中文的判断方法和利用思路。

**核心理念：把整个 PHP 手册和打法库塞进一个 HTML 文件，断网也能秒查。**

![主界面：条目搜索](https://mmbiz.qpic.cn/mmbiz_png/Wq4VJsQicA18Ol2pKBNDg79hia8m2r9ibJtLF4VmQAVA1eDFmN32fGicFYEicbYS8iauYtbicia9mLIuibZd4BgHrCQBnMOibjdM3K7Gmy15nh2Pcy6KQ/640?from=appmsg)

主界面：条目搜索

03核心亮点

`📖 全量离线索引：11,930 条条目来自 PHP 官方中文手册，断网即查
🎯 196 条 CTF 实战技巧：附 990 段可复制 payload，覆盖文件包含与伪协议、
   反序列化、SSTI 与框架、各类过滤绕过、XXE/JWT/SSRF、后渗透
🧰 内置工具箱：序列化 payload 生成、反弹 Shell 命令、JWT 拆解、哈希
   识别、编码器，全部本地运行
🔍 高级搜索语法：k:ctf 按类型筛、pl:base64 只搜 payload、-redis 排除、
   "精确短语" 精确匹配；Ctrl+K 唤起命令面板，跳条目、切视图、导出
🛡️ CVE 更新：接入 OSV，赛前联网拉取最新漏洞并自动补上中文利用思路
💾 零部署：成品单 HTML 双击即用；收藏、笔记、条目本地修改存浏览器，
   JSON 导出备份，换机器导入即恢复`

![工具箱：序列化与反弹 Shell](https://mmbiz.qpic.cn/mmbiz_png/Wq4VJsQicA1iciaOwoicAUCcpRG4kGIicmSIwibCVhibXQvMKiaWV490pfwjCjtf9SPiajCXiaYQvv92dxGkqHr5Q9njqWWOvYMpNtwQZKkBfyicjQ7DEk/640?from=appmsg)

工具箱：序列化与反弹 Shell

04技术栈与部署

纯静态单页应用，零依赖零部署：从 Releases 下载 `php-ctf-handbook.html`，双击打开就能用。唯一要注意的是 Windows Defender 可能因启发式扫描误报删除（13MB HTML 里塞了大量 PHP 代码），记得加白名单。

开源协议 MIT；手册文本索引自 PHP 官方中文手册，版权归 PHP Documentation Group，作者已如实标注。

**一句话概括：赛前 5 分钟准备，赛中 0 秒联网——11,930 条手册、196 条技巧、990 段 payload，全在一个双击即开的 HTML 里。**

免责声明

⚠️ 免责声明

注：工具仅供安全研究与学习之用，若将工具做其他用途，由使用者承担全部法律及连带责任，作者及发布者不承担任何法律及连带责任。信息及工具收集于互联网，真实性及安全性自测！！

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Xu1xJEZRrFjUe1HmsusbqLJiaQvscUlHp1kgYagMRTFy1TyiaryxmOjvkpS6UKic5ricVOjdicibiaLMTibKkUqiafYD8vw/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过