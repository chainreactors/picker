---
title: 【已复现】Linux FUSE page cache 越界写本地提权漏洞
url: https://mp.weixin.qq.com/s/8z3EhwgnTyTj6Hkq8dDNCQ
source: Doonsec's feed
date: 2026-07-07
fetch_date: 2026-07-08T05:03:28.896547
---

# 【已复现】Linux FUSE page cache 越界写本地提权漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dZ7ia5iaWFzzibrqndoZlyDJiaSvuyoKiceDacmT2ibibMO6lr7etLqILhlia1MWxHCDjDgJcMhCDia20samGmhRiarf5Msm9BgYmaW57p623bFicKarV4/0?wx_fmt=jpeg)

# 【已复现】Linux FUSE page cache 越界写本地提权漏洞

原创

360漏洞研究院
360漏洞研究院

360漏洞研究院

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Linux 内核 FUSE 子系统曝出 page cache 越界写本地权限提升漏洞（CVE-2026-31694，CVSS 7.8），本地攻击者通过构造恶意 FUSE 文件系统目录项数据，可触发内核 page cache 越界写，破坏相邻缓存页面内容，并在特定利用条件下实现 root 权限提升。

**利用前置条件：**

* 攻击者需要具备本地执行能力
* 允许用户挂载或运行受控 FUSE 文件系统

目前 **360漏洞挖掘智能体已成功复现该漏洞**。本文包含完整影响范围、修复方案、技术原理与复现细节，建议用户立即升级。

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | Linux FUSE page cache 越界写本地提权漏洞 | | |
| **漏洞编号** | CVE-2026-31694 | | |
| **公开时间** | 2026-05-01 | **POC状态** | **已公开** |
| **漏洞类型** | 本地权限提升 | **EXP状态** | **已公开** |
| **利用可能性** | 高 | **技术细节状态** | **已公开** |
| **CVSS 3.1** | 7.8 | **在野利用状态** | 未发现 |

**01**

**漏洞影响范围**

漏洞相关缓存逻辑由commit 69e34551152a286f827d54dcb5700da6aeaac1fb引入；修复 commit 51a8de6c50bf947c8f534cd73da4c8f0a13e7bed 于 2026-04-24 合入主线，首次出现在 v7.1-rc1，正式版本 v7.1 已包含修复。

该漏洞自 Linux 内核 6.15 起引入。已确认的修复情况如下：

* 在 6.18 分支中，自 6.18.25 起修复
* 在 7.0 分支中，自 7.0.2 起修复
* 在 7.1 及后续版本中已全部修复

Linux 内核 6.15 及之后、低于上述修复版本的中间版本均受影响。

已知受影响发行版：

* Ubuntu
* Fedora

**02**

**修复建议**

**正式防护方案**

官方修复补丁已经发布，受影响版本请尽快修复。

```
diff --git a/fs/fuse/readdir.c b/fs/fuse/readdir.cindex c2aae2eef0868..aae657fd56c0e 100644--- a/fs/fuse/readdir.c+++ b/fs/fuse/readdir.c@@ -41,6 +41,10 @@ static void fuse_add_dirent_to_cache(struct file *file,unsigned int offset;void *addr;
+  /* Dirent doesn't fit in readdir cache page?  Skip caching. */+  if (reclen > PAGE_SIZE)+    return;+   spin_lock(&fi->rdc.lock);    /*    * Is cache already completed?  Or this entry does not go at the end of
```

补丁在 fs/fuse/readdir.c 的 fuse\_add\_dirent\_to\_cache() 中新增检查：当 reclen > PAGE\_SIZE 时直接 return，避免将大于单页的 FUSE dirent 写入 readdir page cache。

**03**

**漏洞描述**

CVE-2026-31694 是 Linux 内核 FUSE 子系统中的 page cache 越界写漏洞，问题位于 fs/fuse/readdir.c 的 fuse\_add\_dirent\_to\_cache()。该函数从 FUSE 服务端可控的 dirent->namelen 计算序列化目录项长度 reclen，并将目录项复制到单个 page cache 页面中；原逻辑只判断目录项能否放入当前页剩余空间，若放不下就切换到新页，但没有检查单个目录项本身是否大于 PAGE\_SIZE。恶意 FUSE 服务端可返回 namelen=4095 的目录项，使 FUSE\_DIRENT\_SIZE 变为 4120 字节，在 4 KB 页面系统上造成 24 字节可控数据写出到相邻内核页面。

攻击者需要具备本地执行能力，并能挂载或驱动一个恶意 FUSE 文件系统，例如通过 fusermount3 或允许非特权用户命名空间的环境。成功利用后，可通过污染相邻 page cache 页面影响 SUID 程序或敏感文件缓存，实现本地权限提升。

**04**

**漏洞复现**

360漏洞研究院已成功复现 Linux FUSE page cache 越界写本地提权漏洞（CVE-2026-31694），实现本地权限提升。

![](https://mmbiz.qpic.cn/mmbiz_png/dZ7ia5iaWFzz9iao1AQ8zPt5JVvbKjiaz9ibMpngBKicEhoAHSiazGdxlHRNDscwI9rVlnGeJwwkPfW71O1WeBpSyD2lRQlibOjicBrG0PvUNY7twV0Y/640?wx_fmt=png&from=appmsg)

CVE-2026-31694

Linux FUSE page cache 越界写本地提权漏洞复现

**05**

**时间线**

2026年7月7日，360漏洞研究院发布本安全风险通告。

**06**

**参考链接**

https://nvd.nist.gov/vuln/detail/CVE-2026-31694

https://bynar.io/blog/discovery-validation-in-the-linux-kernel-part-2-fuse-page-cache-overflow

https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=51a8de6c50bf947c8f534cd73da4c8f0a13e7bed

**07**

**更多漏洞情报**

“扫描下方二维码，进入公众号粉丝交流群。更多一手网安资讯、漏洞预警、技术干货和技术交流等您参与！”

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/dZ7ia5iaWFzz8YToicKab1BicPnEdr7jiatvQUVWSMnYTBeG5ibibgxkGAG1rF4pUdpowPcCmokOO5tp4UjjhUsos4Zf4VwE1aM9NTUz3ogfgdwwFw/640?wx_fmt=gif&from=appmsg)

建议您订阅360数字安全-漏洞情报服务，获取更多漏洞情报详情以及处置建议，让您的企业远离漏洞威胁。

邮箱：360VRI@360.cn

网址：https://vi.loudongyun.360.net

**“洞”悉网络威胁，守护数字安全**

**关于我们**

360 漏洞研究院，隶属于360数字安全集团。其成员常年入选谷歌、微软、华为等厂商的安全精英排行榜, 并获得谷歌、微软、苹果史上最高漏洞奖励。研究院是中国首个荣膺Pwnie Awards“史诗级成就奖”，并获得多个Pwnie Awards提名的组织。累计发现并协助修复谷歌、苹果、微软、华为、高通等全球顶级厂商CVE漏洞3000多个，收获诸多官方公开致谢。研究院也屡次受邀在BlackHat，Usenix Security，Defcon等极具影响力的工业安全峰会和顶级学术会议上分享研究成果，并多次斩获信创挑战赛、天府杯等顶级黑客大赛总冠军和单项冠军。研究院将凭借其在漏洞挖掘和安全攻防方面的强大技术实力，帮助各大企业厂商不断完善系统安全，为数字安全保驾护航，筑造数字时代的安全堡垒。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5nNKGRl7pFgicOqv9MYiaOG44RH4yyGnFKEytIx6iaYAmN9fbvKEicEu6LfaG7sCicKKibyCdbTYiaprPsq0VhvEu3ZuA/0?wx_fmt=png)

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