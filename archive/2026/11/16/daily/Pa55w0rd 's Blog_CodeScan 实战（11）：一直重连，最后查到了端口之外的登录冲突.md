---
title: CodeScan 实战（11）：一直重连，最后查到了端口之外的登录冲突
url: https://www.pa55w0rd.online/codescan-11/
source: Pa55w0rd 's Blog
date: 2026-11-16
fetch_date: 2026-11-17T09:56:37.385951
---

# CodeScan 实战（11）：一直重连，最后查到了端口之外的登录冲突

# [Pa55w0rd 's Blog](/)

## [代码审计、威胁建模与企业安全实践](/)

[首页](/)
[归档](/archives)
[威胁情报](/threat-broadcast)
[关于我](/about)
[留言](/comments)
[公益404](/404.html)

2026-11-16

[开发安全](/categories/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/)►[CodeScan实战](/categories/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/CodeScan%E5%AE%9E%E6%88%98/)

约 1k 字
约 3 分钟读完

2026-11-17

1. [首页](/)
2. [开发安全](/categories/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/)
3. [CodeScan实战](/categories/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/CodeScan%E5%AE%9E%E6%88%98/)
4. CodeScan 实战（11）：一直重连，最后查到了端口之外的登录冲突

# CodeScan 实战（11）：一直重连，最后查到了端口之外的登录冲突

[系列目录](/codescan-00/) · 第 11 篇

任务列表一直显示“重连中”，刷新也没有恢复。与此同时，页面上的部分普通接口还能正常读取数据，很像是实时推送服务坏了。

最后确认的关键条件是：浏览器同时登录了原 Artex 的 8787 和本项目的 17878，两者使用同一个主机名。

## 0x01 端口不同，不代表所有浏览器状态都隔离

前端存储和 Cookie 的隔离方式不同。浏览器源包含协议、主机和端口；Cookie 的匹配主要看域、路径及相关属性，不以端口作为隔离边界。

因此两个 `http://127.0.0.1:<不同端口>` 页面，可以有各自的 localStorage，却仍收到同名旧 Cookie。这次涉及的兼容字段是 `artex_token`。

如果两套实例使用不同的密钥和用户数据，一边签发的令牌到了另一边，校验失败是正常的。真正需要修的是令牌选择、存储与迁移逻辑，而不是让两边共享密钥来绕过错误。

## 0x02 为什么普通 API 能用，SSE 却重连

普通 API 请求可以携带明确的 `Authorization: Bearer ...`。实时通道采用 SSE，在旧路径没有显式查询令牌时，会落到 Cookie 兼容逻辑。

于是出现了两条不同的链：

[![同主机名不同端口可共享旧Cookie，普通API明确Bearer成功，旧SSE使用另一实例Cookie导致401重连；修复身份选择及迁移逻辑。](/assets/codescan/11-sse-auth-paths-v1.webp)](/assets/codescan/11-sse-auth-paths-v1.svg "同一主机名：端口不同仍可能共享旧 Cookie")

图 11｜API 与 SSE 使用不同身份来源时，可能产生“能查数据但一直重连”的现象。 [打开 SVG 原图](/assets/codescan/11-sse-auth-paths-v1.svg)

自动重连解决的是暂时断线，解决不了持续无效的身份。若页面只显示“重连中”，用户就看不到它其实在反复收到鉴权失败。

这也解释了为什么不能只检查服务端端口是否监听。网络连通和身份有效，是两项不同检查。

## 0x03 这轮修复放在哪里

修复包含端口对应的令牌存储与迁移、旧 Cookie 清理，以及 SSE 显式查询令牌和 Bearer 的选择顺序。已经提供有效显式身份时，不应再被另一实例留下的旧 Cookie 遮蔽。

后端还保留数据库用户有效性检查。签名通过但用户已失效，也不能继续开放实时数据。

本轮没有通过复制另一实例密钥、伪造登录态来“验证可用”，也没有为排查重连删除任务或重建数据卷。鉴权问题与任务数据丢失要分别取证。

## 0x04 重连不等于任务被删除

列表加载失败时，首先应该确认任务 API、实时连接和数据库记录各自的状态。前端没有收到列表，不等于数据库执行了删除。

可以按以下顺序缩小范围：

1. 普通任务查询是否返回 200，响应是否包含目标任务。
2. SSE 建连是 200、401，还是网络错误。
3. 当前浏览器选中的身份是否属于本实例。
4. 服务端日志是否记录鉴权失败，任务归属是否一致。
5. 有明确删除记录或数据库证据后，再讨论删除时间与主体。

“页面打不开”本身不够推断谁删了任务，更不应通过重置数据库验证猜测。

## 0x05 恢复是怎样确认的

工程检查覆盖鉴权优先级、失效用户、迁移逻辑和前端状态。部署后，用户按提示强制刷新，实际反馈“实时，已恢复”。

这条反馈是当时真实浏览器恢复的依据，应与自动化测试分开记录；不能把后端测试通过写成已经自动登录并观察过真实页面。

如果后续再次重连，应重新检查响应码和身份来源，不默认还是同一个原因。代理超时、服务器重启、网络中断也会产生相似表象。

[上一篇：完整审计模式](/codescan-10/) · [下一篇：运行预算与断点](/codescan-12/)

<https://www.pa55w0rd.online/codescan-11/>

分享到
[留言](/codescan-11/#comments)

* [SSE](/tags/SSE/)
* [故障排查](/tags/%E6%95%85%E9%9A%9C%E6%8E%92%E6%9F%A5/)
* [身份认证](/tags/%E8%BA%AB%E4%BB%BD%E8%AE%A4%E8%AF%81/)

文章作者：Pa55w0rd

文章链接：<https://www.pa55w0rd.online/codescan-11/>

版权声明：本博客所有文章除特别声明外，均采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh) 许可协议。转载请注明来源 Pa55w0rd！

[**← 上一篇**

CodeScan 实战（12）：79 轮仍然超时：给循环、收尾与断点设边界](/codescan-12/)
[**下一篇 →**

CodeScan 实战（10）：从二选一，走到同一任务内的完整审计](/codescan-10/)

## 留言

欢迎补充、纠错或交流；发表评论需使用 GitHub 账号登录。

正在加载留言…

请启用 JavaScript 以查看留言。

### 近期文章

* [CodeScan 实战（00）：从一次代码审计需求，到一套可追溯的工程实践](/codescan-00/)
* [CodeScan 实战（01）：用 Docker Compose 部署，与原 Artex 共存](/codescan-01/)
* [CodeScan 实战（02）：吸收其他项目的优势，统一威胁、漏洞与证据](/codescan-02/)
* [CodeScan 实战（03）：补齐审计覆盖、反证和收官门禁](/codescan-03/)
* [CodeScan 实战（04）：把威胁建模接进真正的任务生命周期](/codescan-04/)

### 分类

* [note](/categories/note/)46
* [web安全](/categories/web%E5%AE%89%E5%85%A8/)14
* [安全建设](/categories/%E5%AE%89%E5%85%A8%E5%BB%BA%E8%AE%BE/)31
* [应急响应](/categories/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/)4
* [开发安全](/categories/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/)25
  + [CodeScan实战](/categories/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/CodeScan%E5%AE%9E%E6%88%98/)18
* [移动安全](/categories/%E7%A7%BB%E5%8A%A8%E5%AE%89%E5%85%A8/)3

### 标签云

[Android - 安全测试 - 工具使用](/tags/Android-%E5%AE%89%E5%85%A8%E6%B5%8B%E8%AF%95-%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8/) [CI-CD](/tags/CI-CD/) [ChatGPT](/tags/ChatGPT/) [CodeScan-Artex](/tags/CodeScan-Artex/) [DevSecOps](/tags/DevSecOps/) [Docker](/tags/Docker/) [GPT-4](/tags/GPT-4/) [HTTPS](/tags/HTTPS/) [Mantis](/tags/Mantis/) [PHPstudy](/tags/PHPstudy/) [Planner](/tags/Planner/) [SDL](/tags/SDL/) [SSE](/tags/SSE/) [STRIDE](/tags/STRIDE/) [TRS](/tags/TRS/) [TTFT](/tags/TTFT/) [algolia](/tags/algolia/) [checklist](/tags/checklist/) [docker](/tags/docker/) [hexo](/tags/hexo/) [iam](/tags/iam/) [jsonp劫持](/tags/jsonp%E5%8A%AB%E6%8C%81/) [linux](/tags/linux/) [mongodb](/tags/mongodb/) [note](/tags/note/) [sql](/tags/sql/) [sql注入](/tags/sql%E6%B3%A8%E5%85%A5/) [web安全](/tags/web%E5%AE%89%E5%85%A8/) [windows 审计工具](/tags/windows-%E5%AE%A1%E8%AE%A1%E5%B7%A5%E5%85%B7/) [xunfeng](/tags/xunfeng/) [zero-trust](/tags/zero-trust/) [代码审计](/tags/%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1/) [任务模板](/tags/%E4%BB%BB%E5%8A%A1%E6%A8%A1%E6%9D%BF/) [任务状态](/tags/%E4%BB%BB%E5%8A%A1%E7%8A%B6%E6%80%81/) [任务编排](/tags/%E4%BB%BB%E5%8A%A1%E7%BC%96%E6%8E%92/) [任务设计](/tags/%E4%BB%BB%E5%8A%A1%E8%AE%BE%E8%AE%A1/) [分析](/tags/%E5%88%86%E6%9E%90/) [反证](/tags/%E5%8F%8D%E8%AF%81/) [可观测性](/tags/%E5%8F%AF%E8%A7%82%E6%B5%8B%E6%80%A7/) [可靠性](/tags/%E5%8F%AF%E9%9D%A0%E6%80%A7/) [基础](/tags/%E5%9F%BA%E7%A1%80/) [基础知识](/tags/%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/) [增量保存](/tags/%E5%A2%9E%E9%87%8F%E4%BF%9D%E5%AD%98/) [备忘录](/tags/%E5%A4%87%E5%BF%98%E5%BD%95/) [威胁建模](/tags/%E5%A8%81%E8%83%81%E5%BB%BA%E6%A8%A1/) [威胁情报](/tags/%E5%A8%81%E8%83%81%E6%83%85%E6%8A%A5/) [存储清理](/tags/%E5%AD%98%E5%82%A8%E6%B8%85%E7%90%86/) [安全建设](/tags/%E5%AE%89%E5%85%A8%E5%BB%BA%E8%AE%BE/) [安全开发](/tags/%E5%AE%89%E5%85%A8%E5%BC%80%E5%8F%91/) [安全漏洞](/tags/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E/) [安全防护](/tags/%E5%AE%89%E5%85%A8%E9%98%B2%E6%8A%A4/) [安装使用](/tags/%E5%AE%89%E8%A3%85%E4%BD%BF%E7%94%A8/) [完整审计](/tags/%E5%AE%8C%E6%95%B4%E5%AE%A1%E8%AE%A1/) [审计覆盖](/tags/%E5%AE%A1%E8%AE%A1%E8%A6%86%E7%9B%96/) [审计评测](/tags/%E5%AE%A1%E8%AE%A1%E8%AF%84%E6%B5%8B/) [工具](/tags/%E5%B7%A5%E5%85%B7/) [工具使用](/tags/%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8/) [工具调用](/tags/%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8/) [工程实践](/tags/%E5%B7%A5%E7%A8%8B%E5%AE%9E%E8%B7%B5/) [工程维护](/tags/%E5%B7%A5%E7%A8%8B%E7%BB%B4%E6%8A%A4/) [平台建设](/tags/%E5%B9%B3%E5%8F%B0%E5%BB%BA%E8%AE%BE/) [应急响应](/tags/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/) [开发安全](/tags/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/) [开源](/tags/%E5%BC%80%E6%BA%90/) [开源工具](/tags/%E5%BC%80%E6%BA%90%E5%B7%A5%E5%85%B7/) [微信公众号](/tags/%E5%BE%AE%E4%BF%A1%E5%85%AC%E4%BC%97%E5%8F%B7/) [技巧](/tags/%E6%8A%80%E5%B7%A7/) [操作记录](/tags/%E6%93%8D%E4%BD%9C%E8%AE%B0%E5%BD%95/) [故障恢复](/tags/%E6%95%85%E9%9A%9C%E6%81%A2%E5%A4%8D/) [故障排查](/tags/%E6%95%85%E9%9A%9C%E6%8E%92%E6%9F%A5/) [数据安全](/tags/%E6%95%B0%E6%8D%AE%E5%AE%89%E5%85%A8/) [数据库](/tags/%E6%95%B0%E6%8D%AE%E5%BA%93/) [未授权访问](/tags/%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE/) [本地部署](/tags/%E6%9C%AC%E5%9C%B0%E9%83%A8%E7%BD%B2/) [模型性能](/tags/%E6%A8%A1%E5%9E%8B%E6%80%A7%E8%83%BD/) [模型计量](/tags/%E6%A8%A1%E5%9E%8B%E8%AE%A1%E9%87%8F/) [渗透测试](/tags/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95/) [漏洞利用](/tags/%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8/) [漏洞管理](/tags/%E6%BC%8F%E6%B4%9E%E7%AE%A1%E7%90%86/) [私信互动](/tags/%E7%A7%81%E4%BF%A1%E4%BA%92%E5%8A%A8/) [移动安全](/tags/%E7%A7%BB%E5%8A%A8%E5%AE%89%E5%85%A8/) [编程基础](/tags/%E7%BC%96%E7%A8%8B%E5%9F%BA%E7%A1%80/) [蜜罐](/tags/%E8%9C%9C%E7%BD%90/) [解决方法](/tags/%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95/) [记录](/tags/%E8%AE%B0%E5%BD%95/) [证据链](/tags/%E8%AF%81%E6%8D%AE%E9%93%BE/) [资产扫描](/tags/%E8%B5%84%E4%BA%A7%E6%89%AB%E6%8F%8F/) [身份认证](/tags/%E8%BA%AB%E4%BB%BD%E8%AE%A4%E8%AF%81/) [迁移](/tags/%E8%BF%81%E7%A7%BB/) [运维安全](/tags/%E8%BF%90%E7%BB%B4%E5%AE%89%E5%85%A8/) [运行复盘](/tags/%E8%BF%90%E8%A1%8C%E5%A4%8D%E7%9B%98/) [运行预算](/tags/%E8%BF%90%E8%A1%8C%E9%A2%84%E7%AE%97/) [速查表](/tags/%E9%80%9F%E6%9F%A5%E8%A1%A8/) [长上下文](/tags/%E9%95%BF%E4%B8%8A%E4%B8%8B%E6%96%87/) [长程任务](/tags/%E9%95%BF%E7%A8%8B%E4%BB%BB%E5%8A%A1/) [零信任](/tags/%E9%9B%B6%E4%BF%A1%E4%BB%BB/)

### 归档

* [2026年11月](/archives/2026/11/)18
* [2023年08月](/archives/2023/08/)2
* [2022年03月](/archives/2022/03/)5
* [2021年12月](/archives/2021/12/)2
* [2021年09月](/archives/2021/09/)1
* [2021年08月](/archives/2021/08/)5
* [2021年07月](/archives/2021/07/)1
* [2021年06月](/archives/2021/06/)1
* [2021年05月](/archives/2021/05...