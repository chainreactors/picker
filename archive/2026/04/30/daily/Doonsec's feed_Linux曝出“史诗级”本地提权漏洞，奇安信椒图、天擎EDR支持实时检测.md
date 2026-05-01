---
title: Linux曝出“史诗级”本地提权漏洞，奇安信椒图、天擎EDR支持实时检测
url: https://mp.weixin.qq.com/s/V5fn25CICy1eN_LV1omcLA
source: Doonsec's feed
date: 2026-04-30
fetch_date: 2026-05-01T05:36:58.258000
---

# Linux曝出“史诗级”本地提权漏洞，奇安信椒图、天擎EDR支持实时检测

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mSqhDgeKrPDyLZnPR548Ja1rtGBnf0ZUpZEudichrzsyibicSBMxJt4t0h3r0AMaF3GibicrcQD9XYSGOCYpQELibLFTEP9vWue8xzvg3iaKZASXTA/0?wx_fmt=jpeg)

# Linux曝出“史诗级”本地提权漏洞，奇安信椒图、天擎EDR支持实时检测

奇安信集团

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

[ 零日警报 ]CVE-2026-31431

# Copy Fail · 史诗级内核提权漏洞

极低门槛 · 单次提权 · 跨容器逃逸

4月30日，Linux内核曝出CVE-2026-31431（Copy Fail）高危本地权限提升漏洞，凭借极低利用门槛、超高成功率与跨容器逃逸能力，被业内称为“史诗级”安全危机。该漏洞影响2017年以来几乎所有主流Linux发行版，普通权限用户可通过一段仅732字节的Python脚本，无需竞争条件、无需偏移适配，单次执行即可获取系统root权限，对政企服务器、云平台、容器集群构成严重威胁。

目前，奇安信椒图（服务器安全管理系统）无需更新特征库，依托本地提权行为检测引擎，默认可检测此漏洞利用行为；奇安信天擎EDR高级版可基于EDR进程数据重建进程树，通过识别不符合正常授权路径的权限跃迁（非root→root）行为进行检测，发现此提权漏洞攻击。

![](https://mmbiz.qpic.cn/mmbiz_png/mSqhDgeKrPBxYocoDk4LXnfJJCBia5VQCiblB6mlgXqU1ToKhSPCbgYRbxAjYnw5naLjIqibES35d5mCFub4yOpIxXD9GlVCQAUns4AndibcwVw/640?wx_fmt=png&from=appmsg)

## ⚡ 本次提权漏洞影响范围广、危害大

奇安信安全专家表示，该漏洞源于Linux内核加密子系统的逻辑缺陷，因algif\_aead模块引入的“原地优化”，导致AF\_ALG加密接口与splice()系统调用组合时，可向任意可读文件的页缓存写入4字节受控数据。攻击者借此篡改setuid程序，直接完成权限提升。更危险的是，漏洞利用仅修改内存页缓存、不触碰磁盘文件，痕迹可随系统重启消失，常规文件校验工具难以溯源；同时页缓存为主机全局共享，普通容器Pod可借此实现逃逸，接管整个节点。

![](https://mmbiz.qpic.cn/mmbiz_png/mSqhDgeKrPDFK8RmMpfib5H8IjibSPZgeWDlWb6nLjxZ9cuKX7T98W8vmXrj8zuuiakCUquQC9FJFjg8oQ6d6gADXc30VDGmT6ia0FKic9uHXD80/640?from=appmsg)

据悉，本次漏洞受影响范围覆盖Ubuntu 24.04 LTS、Amazon Linux 2023、RHEL 8/9/10、SUSE 16等主流发行版，多租户服务器、K8s集群、CI/CD环境、云主机成为重灾区，一旦被利用，将导致数据泄露、系统被非法控制、横向渗透扩散等严重后果。

## 🛡️ 椒图、天擎EDR高级版可有效检测本地提权行为

面对突发高危漏洞，奇安信椒图（服务器安全管理系统）率先实现漏洞利用行为检测，无需更新特征库、无需人工配置规则，依托本地提权行为检测引擎，默认可精准识别CVE-2026-31431漏洞攻击行为。当攻击者执行漏洞利用脚本、发起权限提升操作时，椒图能实时捕获提权进程链、权限变更轨迹与命令行为，快速标记高危事件并告警，帮助运维人员第一时间发现入侵，阻断攻击落地。

同时，奇安信天擎EDR高级版可基于EDR进程数据完整重建进程树，精准识别从普通权限非法提升至root权限的异常权限跃迁行为，无需特征库即可有效检测 CVE-2026-31431 漏洞利用攻击，及时发现并阻断非授权提权操作，强化主机端入侵检测能力。

### 🔧 紧急处置建议 | 内核升级 + 行为防御

为保障Linux系统安全，奇安信向广大政企机构用户发布紧急处置建议，优先完成内核补丁升级，从根源修复漏洞：

1. Linux Kernel 6.18版本，升级至6.18.22及以上；

2. Linux Kernel 6.19版本，升级至6.19.12及以上；

3. Linux Kernel 7.0版本，升级至7.0或应用对应补丁；

4. 旧版本内核，应用官方Commit a664bf3d603d补丁回滚不安全优化。

暂无法立即升级内核的系统，可采取临时缓解措施：禁用algif\_aead内核模块，该操作对dm-crypt、SSH、kTLS等常用服务无影响，可有效阻断漏洞利用路径；容器与云环境可通过seccomp策略限制AF\_ALG套接字创建，缩小攻击面。同时，建议用户借助奇安信椒图、天擎EDR高级版等持续监控系统提权行为，定期巡检内核版本与模块状态，重点加固多租户、容器、跳板机等高风险场景。

### 结束语

Linux作为政企数字化转型的核心基础设施，其安全直接关系业务稳定。此次Copy Fail漏洞再次凸显内核级防护的重要性，奇安信椒图凭借实时行为检测能力，为用户构筑漏洞爆发期的安全屏障。奇安信将持续跟踪漏洞动态，快速迭代防护能力，助力政企用户高效应对各类内核安全风险，筑牢服务器、终端主机等安全防线。

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/G3LNmiaOGjarwCHGK4V5d5pFicUo1yED6dkswm0BfC0ncqh9D2G8Rvuelo3qdHlWFv4KMF78FsOIEKiaJrgmdIlJw/0?wx_fmt=png)

奇安信集团

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/G3LNmiaOGjarwCHGK4V5d5pFicUo1yED6dkswm0BfC0ncqh9D2G8Rvuelo3qdHlWFv4KMF78FsOIEKiaJrgmdIlJw/0?wx_fmt=png)

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