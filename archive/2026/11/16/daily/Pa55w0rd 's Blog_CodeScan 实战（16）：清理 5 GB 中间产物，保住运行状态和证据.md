---
title: CodeScan 实战（16）：清理 5 GB 中间产物，保住运行状态和证据
url: https://www.pa55w0rd.online/codescan-16/
source: Pa55w0rd 's Blog
date: 2026-11-16
fetch_date: 2026-11-17T09:56:38.102536
---

# CodeScan 实战（16）：清理 5 GB 中间产物，保住运行状态和证据

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

约 1.1k 字
约 3 分钟读完

2026-11-17

1. [首页](/)
2. [开发安全](/categories/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/)
3. [CodeScan实战](/categories/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/CodeScan%E5%AE%9E%E6%88%98/)
4. CodeScan 实战（16）：清理 5 GB 中间产物，保住运行状态和证据

# CodeScan 实战（16）：清理 5 GB 中间产物，保住运行状态和证据

[系列目录](/codescan-00/) · 第 16 篇

多轮后端测试、前端候选构建和 Linux 打包之后，磁盘开始成为运行障碍。清理中间文件、镜像与容器，释放存储空间。

这轮清理最终删除了约 5.36 GB 文件，但没有删除 Docker 镜像、容器或数据卷。

## 0x01 先按影响分类

“可以重建”不等于“删除没有影响”。编译缓存删后会变慢；依赖树删后构建可能需要重新下载；候选版本删后会失去尚未部署的验证产物；数据库和密钥删后则可能直接影响服务和恢复。

所以先把目标拆开：

| 资源 | 本轮处理 |
| --- | --- |
| 独立 Go 测试缓存和临时目录 | 核对归属、占用后删除 |
| 重复前端依赖副本与中间构建目录 | 删除本轮产生且不再使用的副本 |
| 重复源码打包、测试辅助文件 | 保留必要证据后定向删除 |
| 当前源码、真实依赖树、候选构建 | 保留 |
| 数据库备份、密钥、日志与源码摘要 | 保留 |
| 运行容器、持久卷和使用中的镜像 | 保留 |
| 无法归属的共享 Docker 缓存 | 本轮不清理 |

这里的分类来自实际盘点，不是一份对所有项目通用的删除规则。

## 0x02 目录链接必须单独处理

前端候选目录里曾有一个 `node_modules` 链接，实际指向项目的真实依赖树。如果清理程序跟随链接递归，可能把正常开发环境一起删掉。

本轮保留该链接和真实目标。其他目录也需要先解析绝对路径、核对是否在授权范围，并区分普通目录、junction 和符号链接。

Windows 下尤其不应该先在 PowerShell 枚举，再拼接到另一个 shell 执行递归删除。路径转义、空格和链接解析一旦不一致，盘点对象与最终删除对象可能不再相同。

## 0x03 用保护摘要验证没有误删

清理前列出源码、候选产物和必要证据的保护集合，计算 SHA-256；清理后再次核对。

本轮回执记录：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` 删除目标：492 项 删除文件逻辑字节：5,356,462,662 保护文件：2,219 个 保护摘要：保持一致  删除 Docker 容器：0 删除 Docker 镜像：0 删除 Docker 数据卷：0 ``` |

5,356,462,662 字节约为 5.36 GB，按二进制单位约为 4.99 GiB。这里是删除文件的逻辑大小，不是承诺磁盘可用空间精确增加同样数值。

后台写入、文件系统分配和缓存变化都会影响可用空间差值，因此逻辑删除量与盘符前后可用空间应分别记录。

[![历史回执记录删除492项目标、逻辑大小5.36GB，2219个保护文件摘要不变；Docker容器、镜像和数据卷删除数均为零。](/assets/codescan/16-scoped-cleanup-v1.webp)](/assets/codescan/16-scoped-cleanup-v1.svg "定向清理：释放文件，保留运行与证据")

图 16｜历史清理回执摘要，数值不是实时磁盘监测或本次新增删除。 [打开 SVG 原图](/assets/codescan/16-scoped-cleanup-v1.svg)

## 0x04 Docker 为什么没有顺手 prune

当时 `codescan-artex:local` 仍有容器引用，应用、PostgreSQL 和持久卷均应保留。两个预期的临时测试容器已经不存在，应该标“已不存在”，不能写成“本次成功删除两个容器”。

Docker 查询当时还存在部分响应异常。为了清理本项目去重启共享 Docker，会影响同机其他项目；无法归属的 build cache 也不适合用全局 prune 处理。

因此没有执行 `docker system prune -a --volumes`，没有重启共享运行时。清理报告需要如实区分“已删除”“已不存在”“已检查并保留”和“本轮未处理”。

## 0x05 清理统计本身也可能有错误

这轮过程中，PowerShell 对字典型数据使用聚合统计时曾得到空值。后来按数值类型逐项累加，并结合删除清单重新核算。

这个错误影响的是汇总展示，不能直接推导成“没有删文件”，也不能只修展示、不复查原始清单。统计程序同样需要保留可核对的输入和输出。

## 0x06 后续怎样少产生垃圾

测试缓存和临时目录使用专属位置；构建前检查剩余空间；保留一个可验证候选，及时清理确定不用的重复副本；将证据和缓存分开存放，避免一条清理命令同时触及二者。

[上一篇：Mantis 借鉴](/codescan-15/) · [下一篇：SDL 与旁路 CI 设计](/codescan-17/)

<https://www.pa55w0rd.online/codescan-16/>

分享到
[留言](/codescan-16/#comments)

* [Docker](/tags/Docker/)
* [存储清理](/tags/%E5%AD%98%E5%82%A8%E6%B8%85%E7%90%86/)
* [工程维护](/tags/%E5%B7%A5%E7%A8%8B%E7%BB%B4%E6%8A%A4/)

文章作者：Pa55w0rd

文章链接：<https://www.pa55w0rd.online/codescan-16/>

版权声明：本博客所有文章除特别声明外，均采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh) 许可协议。转载请注明来源 Pa55w0rd！

[**← 上一篇**

CodeScan 实战（17）：下一步接入 SDL：从旁路 Hook 到可审计门禁](/codescan-17/)
[**下一篇 →**

CodeScan 实战（15）：借鉴 Mantis：版本化批次、累计预算和导航](/codescan-15/)

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

[Android - 安全测试 - 工具使用](/tags/Android-%E5%AE%89%E5%85%A8%E6%B5%8B%E8%AF%95-%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8/) [CI-CD](/tags/CI-CD/) [ChatGPT](/tags/ChatGPT/) [CodeScan-Artex](/tags/CodeScan-Artex/) [DevSecOps](/tags/DevSecOps/) [Docker](/tags/Docker/) [GPT-4](/tags/GPT-4/) [HTTPS](/tags/HTTPS/) [Mantis](/tags/Mantis/) [PHPstudy](/tags/PHPstudy/) [Planner](/tags/Planner/) [SDL](/tags/SDL/) [SSE](/tags/SSE/) [STRIDE](/tags/STRIDE/) [TRS](/tags/TRS/) [TTFT](/tags/TTFT/) [algolia](/tags/algolia/) [checklist](/tags/checklist/) [docker](/tags/docker/) [hexo](/tags/hexo/) [iam](/tags/iam/) [jsonp劫持](/tags/jsonp%E5%8A%AB%E6%8C%81/) [linux](/tags/linux/) [mongodb](/tags/mongodb/) [note](/tags/note/) [sql](/tags/sql/) [sql注入](/tags/sql%E6%B3%A8%E5%85%A5/) [web安全](/tags/web%E5%AE%89%E5%85%A8/) [windows 审计工具](/tags/windows-%E5%AE%A1%E8%AE%A1%E5%B7%A5%E5%85%B7/) [xunfeng](/tags/xunfeng/) [zero-trust](/tags/zero-trust/) [代码审计](/tags/%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1/) [任务模板](/tags/%E4%BB%BB%E5%8A%A1%E6%A8%A1%E6%9D%BF/) [任务状态](/tags/%E4%BB%BB%E5%8A%A1%E7%8A%B6%E6%80%81/) [任务编排](/tags/%E4%BB%BB%E5%8A%A1%E7%BC%96%E6%8E%92/) [任务设计](/tags/%E4%BB%BB%E5%8A%A1%E8%AE%BE%E8%AE%A1/) [分析](/tags/%E5%88%86%E6%9E%90/) [反证](/tags/%E5%8F%8D%E8%AF%81/) [可观测性](/tags/%E5%8F%AF%E8%A7%82%E6%B5%8B%E6%80%A7/) [可靠性](/tags/%E5%8F%AF%E9%9D%A0%E6%80%A7/) [基础](/tags/%E5%9F%BA%E7%A1%80/) [基础知识](/tags/%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/) [增量保存](/tags/%E5%A2%9E%E9%87%8F%E4%BF%9D%E5%AD%98/) [备忘录](/tags/%E5%A4%87%E5%BF%98%E5%BD%95/) [威胁建模](/tags/%E5%A8%81%E8%83%81%E5%BB%BA%E6%A8%A1/) [威胁情报](/tags/%E5%A8%81%E8%83%81%E6%83%85%E6%8A%A5/) [存储清理](/tags/%E5%AD%98%E5%82%A8%E6%B8%85%E7%90%86/) [安全建设](/tags/%E5%AE%89%E5%85%A8%E5%BB%BA%E8%AE%BE/) [安全开发](/tags/%E5%AE%89%E5%85%A8%E5%BC%80%E5%8F%91/) [安全漏洞](/tags/%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E/) [安全防护](/tags/%E5%AE%89%E5%85%A8%E9%98%B2%E6%8A%A4/) [安装使用](/tags/%E5%AE%89%E8%A3%85%E4%BD%BF%E7%94%A8/) [完整审计](/tags/%E5%AE%8C%E6%95%B4%E5%AE%A1%E8%AE%A1/) [审计覆盖](/tags/%E5%AE%A1%E8%AE%A1%E8%A6%86%E7%9B%96/) [审计评测](/tags/%E5%AE%A1%E8%AE%A1%E8%AF%84%E6%B5%8B/) [工具](/tags/%E5%B7%A5%E5%85%B7/) [工具使用](/tags/%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8/) [工具调用](/tags/%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8/) [工程实践](/tags/%E5%B7%A5%E7%A8%8B%E5%AE%9E%E8%B7%B5/) [工程维护](/tags/%E5%B7%A5%E7%A8%8B%E7%BB%B4%E6%8A%A4/) [平台建设](/tags/%E5%B9%B3%E5%8F%B0%E5%BB%BA%E8%AE%BE/) [应急响应](/tags/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/) [开发安全](/tags/%E5%BC%80%E5%8F%91%E5%AE%89%E5%85%A8/) [开源](/tags/%E5%BC%80%E6%BA%90/) [开源工具](/tags/%E5%BC%80%E6%BA%90%E5%B7%A5%E5%85%B7/) [微信公众号](/tags/%E5%BE%AE%E4%BF%A1%E5%85%AC%E4%BC%97%E5%8F%B7/) [技巧](/tags/%E6%8A%80%E5%B7%A7/) [操作记录](/tags/%E6%93%8D%E4%BD%9C%E8%AE%B0%E5%BD%95/) [故障恢复](/tags/%E6%95%85%E9%9A%9C%E6%81%A2%E5%A4%8D/) [故障排查](/tags/%E6%95%85%E9%9A%9C%E6%8E%92%E6%9F%A5/) [数据安全](/tags/%E6%95%B0%E6%8D%AE%E5%AE%89%E5%85%A8/) [数据库](/tags/%E6%95%B0%E6%8D%AE%E5%BA%93/) [未授权访问](/tags/%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE/) [本地部署](/tags/%E6%9C%AC%E5%9C%B0%E9%83%A8%E7%BD%B2/) [模型性能](/tags/%E6%A8%A1%E5%9E%8B%E6%80%A7%E8%83%BD/) [模型计量](/tags/%E6%A8%A1%E5%9E%8B%E8%AE%A1%E9%87%8F/) [渗透测试](/tags/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95/) [漏洞利用](/tags/%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8/) [漏洞管理](/tags/%E6%BC%8F%E6%B4%9E%E7%AE%A1%E7%90%86/) [私信互动](/tags/%E7%A7%81%E4%BF%A1%E4%BA%92%E5%8A%A8/) [移动安全](/tags/%E7%A7%BB%E5%8A%A8%E5%AE%89%E5%85%A8/) [编程基础](/tags/%E7%BC%96%E7%A8%8B%E5%9F%BA%E7%A1%80/) [蜜罐](/tags/%E8%9C%9C%E7%BD%90/) [解决方法](/tags/%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95/) [记录](/tags/%E8%AE%B0%E5%BD%95/) [证据链](/tags/%E8%AF%81%E6%8D%AE%E9%93%BE/) [资产扫描](/tags/%E8%B5%84%E4%BA%A7%E6%89%AB%E6%8F%8F/) [身份认证](/tags/%E8%BA%AB%E4%BB%BD%E8%AE%A4%E8%AF%81/) [迁移](/tags/%E8%BF%81%E7%A7%BB/) [运维安全](/tags/%E8%BF%90%E7%BB%B4%E5%AE%89%E5%85%A8/) [运行复盘](/tags/%E8%BF%90%E8%A1%8C%E5%A4%8D%E7%9B%98/) [运行预算](/tags/%E8%BF%90%E8%A1%8C%E9%A2%84%E7%AE%97/) [速查表](/tags/%E9%80%9F%E6%9F%A5%E8%A1%A8/) [长上下文](/tags/%E9%95%BF%E4%B8%8A%E4%B8%8B%E6%96%87/) [长程任务](/tags/%E9%95%BF%E7%A8%8B%E4%BB%BB%E5%8...