---
title: 页缓存篡改破防！Linux kernel Dirty Frag本地权限提升漏洞安全通告
url: https://mp.weixin.qq.com/s/XmuQn8oRJlFHokw9poKA7A
source: Doonsec's feed
date: 2026-05-08
fetch_date: 2026-05-09T05:07:12.644224
---

# 页缓存篡改破防！Linux kernel Dirty Frag本地权限提升漏洞安全通告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YUnWCyLjbukVaqzHkTtyxwbPibxOu2Qk2wTxusBSiaTmciaWy2Fx5licEKwZunwiaSRUJrHzt0iarqhntJW53WWqKyFupbibmofz0NN4yHcxmubUoc/0?wx_fmt=jpeg)

# 页缓存篡改破防！Linux kernel Dirty Frag本地权限提升漏洞安全通告

应急响应中心
应急响应中心

亚信安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YUnWCyLjbumGIryGuMiaGf3TM8EFqiaX4ldsORibfniaJEuEyhg7BnTMHLBw3n4ZHwiak5lTtV5bXmpXdNH9I0BOgqoibJT7GaXoWpfspKBnSRfqY/640?wx_fmt=jpeg)

Linux kernel 存在 Dirty Frag 本地权限提升漏洞。攻击者在获得主机低权限本地执行能力后，可利用页缓存写入问题修改只读文件的 page cache 内容，进而实现本地提权，影响系统完整性与主机安全边界。

当前公开资料显示，相关利用代码已公开，建议相关用户及时开展排查与缓解。

**漏洞概述**

![](https://mmbiz.qpic.cn/mmbiz_png/YUnWCyLjbukktutia4BVBV7jeXd7s65SLcykIuYy7guDXuVm1m5FNYl9ib20icDAt9gyib5Yn3pvnyS2E7iawM87bKGAcBEHQkRPpCU1X3mqWwpU/640?wx_fmt=png)

**漏洞详情**

Dirty Frag 通过组合 xfrm-ESP Page-Cache Write 与 RxRPC Page-Cache Write 两类问题，在特定零拷贝发送路径下使攻击者可将只读文件的 page cache 页植入 skb frag，并在内核侧原地处理时导致页缓存内容被修改。

攻击者在获得低权限本地执行能力后，可能利用该问题修改内存中的关键文件缓存并获取 root 权限。

该漏洞本质上属于本地权限提升问题，需重点关注以下场景：

* 存在普通本地用户登录的 Linux 主机
* 容器宿主机、CI/CD Runner、共享跳板机
* 存在 Web 命令执行面或 SSH 落地面的系统

**影响范围**

**Linux kernel 受影响范围：**

xfrm-ESP Page-Cache Write：从上游提交 cac2661c53f3（2017-01-17）起至当前公开上游版本

RxRPC Page-Cache Write：从上游提交 2dc334f1a63a（2023-06）起至当前公开上游版本

**已公开验证的发行版/内核版本：**

* Ubuntu 24.04.4：6.17.0-23-generic
* RHEL 10.1：6.12.0-124.49.1.el10\_1.x86\_64
* openSUSE Tumbleweed：7.0.2-1-default
* CentOS Stream 10：6.12.0-224.el10.x86\_64
* AlmaLinux 10：6.12.0-124.52.3.el10\_1
* Fedora 44：6.19.14-300.fc44.x86\_64

说明：当前暂无 CVE 编号和统一官方修复版本；以上范围主要来自公开 PoC 和技术分析，实际影响仍需结合发行版安全公告与补丁回移情况确认。

**排查与处置建议**

**01**

**优先排查对象：**

* Linux 服务器
* 容器宿主机
* CI/CD Runner
* 共享运维跳板机
* 存在普通用户 shell 权限或 SSH 落地面的主机

**02**

**快速自查：**

```
uname -rlsmod | egrep '^(esp4|esp6|rxrpc)'sysctl kernel.unprivileged_userns_clone
```

关注点：

* 是否加载 esp4、esp6、rxrpc
* 是否允许低权限本地执行
* 是否存在容器、CI/CD、共享账号等高风险使用场景

**03**

**临时缓解措施：**

在确认业务影响后，可临时禁用相关模块自动加载，并卸载已加载模块：

```
cat >/etc/modprobe.d/dirtyfrag.conf <<'EOF'install esp4 /bin/falseinstall esp6 /bin/falseinstall rxrpc /bin/falseEOF
modprobe -r esp4 esp6 rxrpc 2>/dev/null || true
```

**同时建议：**

* 收敛本地低权限账号
* 限制非必要 SSH 登录入口
* 收敛容器创建与执行权限
* 降低 Web 服务命令执行面
* 视业务情况限制非必要 user namespace

**说明：**

* 禁用 esp4/esp6 可能影响 IPsec ESP
* 禁用 rxrpc 可能影响依赖 RxRPC/AF\_RXRPC 的业务
* 变更前建议先评估业务兼容性

**补充说明：不同内核构建方式下的缓解差异**

* 若相关功能以内核模块方式提供，可通过禁止模块加载并卸载已加载模块的方式实施临时缓解
* 若相关功能已直接编译进内核，则上述模块禁用方式不再适用，应优先关注内核升级，或切换至不包含相关功能的内核版本
* 限制 user namespace 仅能作为部分利用路径的辅助降风险措施，不能替代正式修复，也不能覆盖全部利用路径
* 建议客户结合自身内核配置，确认 ESP 与 RxRPC 相关功能是以模块形式启用还是直接编译进内核；如为模块形式，可优先采用模块黑名单和卸载方式缓解；如为内建形式，则应优先通过升级修复内核降低风险

**疑似已受影响主机处置**

**对疑似已被利用的主机，建议：**

* 先隔离主机并保留必要取证信息
* 重点核查 /etc/passwd、/usr/bin/su 及其他关键 setuid 文件完整性
* 再根据应急流程决定是否重启或清理 page cache
* 说明：
* 该问题可能影响内存中的 page cache 结果，若直接操作主机，可能影响后续核查结论

**修复建议**

当前公开资料显示，上游已出现与该问题相关的修复提交，已确认至少涉及 xfrm-ESP 利用路径。

对于 RxRPC 路径，建议持续跟踪上游内核和各发行版安全公告；在发行版正式发布修复版本前，不建议仅依据单个上游提交判断已完全修复。

建议相关用户持续关注 Ubuntu、Red Hat、SUSE、Fedora、AlmaLinux、CentOS Stream 等发行版公告，并在官方补丁发布后优先升级内核。

**检测与防护建议**

**建议安全产品或主机侧重点关注以下行为：**

* 异常 unshare
* 异常 splice/vmsplice
* 异常 add\_key
* /etc/passwd、/usr/bin/su 等关键文件异常访问
* 临时目录编译执行
* PoC 仓库拉取及异常提权行为链

**参考链接**

* 情报来源：https://github.com/V4bel/dirtyfrag
* 技术文档：https://github.com/V4bel/dirtyfrag/blob/master/assets/write-up.md

本文发布的补丁下载链接均源自各原厂官方网站。尽管我们努力确保官方资源的安全性，但在互联网环境中，文件下载仍存在潜在风险。为保障您的设备安全与数据隐私，敬请您在点击下载前谨慎核实其安全性和可信度。

了解亚信安全，请点击**“阅读原文”**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/iczzp36h0nbHibibbM15ufBwzEl7XmKf0qYkQWrLy6Kib3bicyrLrH8tGx9p996AKQPT93mOcicjK8mzibsV2yVyU6puA/0?wx_fmt=png)

亚信安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/iczzp36h0nbHibibbM15ufBwzEl7XmKf0qYkQWrLy6Kib3bicyrLrH8tGx9p996AKQPT93mOcicjK8mzibsV2yVyU6puA/0?wx_fmt=png)

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