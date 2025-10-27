---
title: 版本升级 | v1.0.12发布，许可证风险早知道
url: https://buaq.net/go-172082.html
source: unSafe.sh - 不安全
date: 2023-07-15
fetch_date: 2025-10-04T11:51:33.895389
---

# 版本升级 | v1.0.12发布，许可证风险早知道

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/8f1099e52a33bcb9d952e301f251e76a.jpg)

版本升级 | v1.0.12发布，许可证风险早知道

新版本来啦~~~~优化许可证检出功能，可通过JSON / HTML / SPDX 报告获知许可证信息支持HTML报告自定义分页1、优化许可证检出功能
*2023-7-14 17:1:0
Author: [xz.aliyun.com(查看原文)](/jump-172082.htm)
阅读量:16
收藏*

---

新版本来啦~~~~

* 优化许可证检出功能，可通过JSON / HTML / SPDX 报告获知许可证信息
* 支持HTML报告自定义分页

## 1、优化许可证检出功能，许可证风险早知道

### 1.1 开源许可证介绍

开源软件一般都有对应的开源许可证（Open Source License）对软件的使用、复制、修改和再发布等进行限制。许可证即授权条款，开源许可证就是保证开源软件这些限制的法律文件，目的在于规范受著作权保护的软件的使用或者分发行为。开源许可证是开源软件生态系统的基础，可以促进软件的协同开发。

### 1.2 常见开源许可证

常见的开源许可证主要有 Apache、MIT、BSD、GPL、LGPL、MPL、SSPL 等，可以大致分为两大类：宽松式许可证（Permissive free software licence）和著佐权许可证（copyleft license）。

根据开源许可证授权的限制程度，可以将开源许可证从宽松到严格进行梳理：

1. 最宽松的是BSD许可证、MIT许可证、Apache许可证、ISC许可证等，这些许可证授权几乎没有任何限制，允许自由地使用、修改、复制和分发软件，同时允许将软件用于商业和非商业目的，只要在软件的副本中包含许可证和版权声明即可。
2. MPL许可证和LGPL许可证，这些许可证要求将修改后的代码以同样的许可证进行发布，并且要求在修改后的代码中包含原始代码的授权和版权信息，但不要求将整个项目以同样的许可证进行发布。
3. GPL许可证、AGPL许可证和CPL许可证相对严格，这些许可证要求将整个项目以相同的许可证进行发布，即使只是使用软件的一部分，也必须以相同的许可证进行发布。此外，这些许可证还要求修改后的代码必须公开发布。

更多关于许可证的知识及选择建议参见：[开源许可证保姆级入门手册](http://https://xz.aliyun.com/t/12671 "开源许可证保姆级入门手册")

### 1.3 检出结果示例

HTML报告：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230714170604-a97e986c-2225-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230714170613-ae7d2d06-2225-1.png)
JSON格式报告：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230714170620-b3162534-2225-1.png)

## 2、HTML报告分页，与“加载过慢”说拜拜

检出结果条目较多时，可以自定义设置每页展示的结果条目数（可选每页展示50/100/150/200条）。
![](https://xzfile.aliyuncs.com/media/upload/picture/20230714170638-bd61bd32-2225-1.png)
图：HTML页面分页结果展示

以上就是本次更新内容的完整介绍~

感谢每一位开源社区成员对OpenSCA的支持和贡献。我们鼓励更多伙伴参与到OpenSCA开源项目的建设中来，成为开源贡献者，有任何建议都可以发在评论区或者Gitee、GitHub上OpenSCA项目的Issues中。让我们一起拥抱开源，共筑开源安全生态，促进开源产业健康发展。

OpenSCA的代码会在GitHub和Gitee持续迭代，欢迎Star和PR，成为我们的开源贡献者，也可提交问题或建议至Issues。我们会参考大家的建议不断完善OpenSCA开源项目，敬请期待更多功能的支持。

GitHub：
<https://github.com/XmirrorSecurity/OpenSCA-cli/releases>

Gitee：
<https://gitee.com/XmirrorSecurity/OpenSCA-cli/releases>

OpenSCA官网：
<https://opensca.xmirror.cn/>

文章来源: https://xz.aliyun.com/t/12697
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)