---
title: 警惕，最新LINUX漏洞
url: https://mp.weixin.qq.com/s/cEe6CNPqRg16OBPVUTuZgA
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:28:23.236716
---

# 警惕，最新LINUX漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2nYVbJUzOCLbKicCeDibzpoYsOP6C78mmEwmkqppBOwJibQIJJcBUSzn2KrtjicCVeougic7SEkib87Am4EwibNlgCzdUdtC3BCicDMve05eQz5QQ3s/0?wx_fmt=jpeg)

# 警惕，最新LINUX漏洞

原创

大兵说安全
大兵说安全

大兵说安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz/M8lZIYZticqSUBxpojuz0dvFDdU3BkVJ2mNfvorv6uNqHGpL9MAhb4mlh288yS4iaQiarSWUkdK4sBKZsHl77Qx3w/640?wx_fmt=gif)

近⽇，Theori / Xint Code 披露本地权限提升漏洞CVE-2026-31431，该漏洞⼜被称为Copy Fail。Ubuntu 安全公告显示该漏洞发布时间为2026-04-23，最近更新时间为2026-04-29；

该漏洞存在于 Linux 内核加密子系统相关逻辑中，攻击者在获得本地普通用户权限后，可通过 AF\_ALG、splice() 与 authencesn 相关逻辑组合，触发对 page cache 的受控写入，从而实现本地提权。研究方称，公开 PoC 可在多个主流 Linux 发行版上将普通用户提升为 root。

该漏洞的危险点不在于远程直接入侵，而在于它会把“已经获得的低权限执行点”迅速放大为 root 权限。因此，对于多用户 Linux 主机、Kubernetes 节点、容器平台、CI/CD 构建机、自托管 Runner、云端 Notebook、沙箱执行环境等场景，风险显著高于普通单用户服务器。研究方特别指出，page cache 在宿主机范围内共享，因此该问题也具备容器逃逸和跨租户影响。

所以，对现在有很多这种养马的、养小龙虾的，特别是在用这种容器去跑的，尤其应该注意。

一、漏洞描述

CVE 编号：CVE－2026－31431

漏洞类型：内存破坏 ／ 逻辑错误

危险等级：高 （High）

CVSS 评分：7.8 （CVSS：3.1／AV：L／AC：L／PR：L／UI：N／S：U／C：H／I：H／A：H）

受影响组件：Linux Kernel 中的crypto：algif＿aead模块（用户空间加密接口）

二、漏洞描述

该漏洞源于 Linux 内核加密子系统的 algif＿aead 模块在处理“原地操作”（in－place operation）时的逻辑缺陷。

技术细节：原本内核试图通过 72548b093ee3 次提交引入优化，允许在同一内存地址进行加密／解密映射。然而，由于 AEAD（关联数据的认证加密）的源地址和目的地址通常来自不同的映射，这种“原地”处理带来了极高的复杂度并导致了潜在的缓冲区溢出或内存损坏风险。

影响：本地攻击者可以利用此漏洞通过构造特定的加密请求，导致系统崩溃（DoS）或实现内核层面的权限提升（PrivilegeEscalation）。

三、影响范围

受影响系统：Debian 安全跟踪⻚⾯显示 bookworm、bullseye 等分⽀中的相关linux包仍有 vulnerable 状态记录,Linux 内核版本：⾃ 2017 年后引⼊该优化的所有发⾏版均受影响，包括但不限于：

CentOS 7/8/9

RHEL 7/8/9

Ubuntu 18.04–24.04

Debian 10/11/12

国产麒麟、统信等基于 Linux 的系统

建议重点排查以下环境：

1. 多⽤户共享服务器、堡垒机、CI/CD Runner、容器宿主机；

2. 允许低权限⽤户登录或执⾏代码的 Linux 主机；

3. Web 服务、应⽤服务、数据库服务等⼀旦被低权限⼊⼝突破即可继续本地提权的场景；

4. 云主机、Kubernetes Node、虚拟化宿主机等对本地提权⻛险敏感的基础设施。

三、修复建议

（一）、临时缓解⽅案

截⾄⽬前，部分主流 Linux 发⾏版稳定分⽀的内核安全更新仍可能未完全推送或尚未覆盖所有环境。对于暂时⽆法⽴即升级内核的系统，建议临时禁⽤ algif\_aead 模块。公开缓解建议也明确提到，在补丁部署前可禁⽤ algif\_aead 模块以降低攻击⾯。

|  |
| --- |
| 1. 创建禁⽤配置⽂件  echo "install algif\_aead /bin/false" | sudo tee /etc/modprobe.d/disable-algif\_aead.conf  2. ⽴即尝试卸载已加载的模块  sudo rmmod algif\_aead 2>/dev/null || true  3. 更新 initramfs（Ubuntu/Debian 建议执⾏）  sudo update-initramfs -u  4. 建议在业务允许的窗⼝重启服务器  sudo reboot  5. 验证是否⽣效，正常情况下应⽆输出  lsmod | grep algif\_aead |

如系统中确有显式依赖 AF\_ALG AEAD 能⼒的业务，禁⽤前应进⾏兼容性评估。公开资料称，⼤多数常⻅场景如 dm-crypt/LUKS、kTLS、IPsec/XFRM、OpenSSL/GnuTLS/NSS 默认构建、SSH 等通常不通过 AF\_ALG 使⽤该路径，但显式配置使⽤ AF\_ALG 的⽤户态程序可能受影响。

如需恢复启⽤

|  |
| --- |
| 1. 删除禁⽤配置⽂件  sudo rm -f /etc/modprobe.d/disable-algif\_aead.conf  2. ⽴即尝试加载模块  sudo modprobe algif\_aead  3. 验证是否加载成功  lsmod | grep algif\_aead |

（二）、⻓期修复⽅案。

请立即检查您的 Linux 内核版本，并同步至官方发布的稳定分支。

截至撰稿时间 2026年4月30日 14:30

* Debian 所有支持中版本仍未修复，请参考下文部署缓解措施。

https://www.suse.com/security/cve/CVE-2026-31431.html

https://www.openeuler.org/en/security/cve/detail/?cveId=CVE-2026-31431&packageName=kernel

* Ubuntu 仅 26.04 LTS 不受影响，其他支持中版本仍未修复，请参考下文部署缓解措施。

https://access.redhat.com/security/cve/cve-2026-31431#cve-affected-packages

* RHEL 8、9、10 仍未修复，请参考下文部署缓解措施。RHEL 6、7 不受影响。

https://ubuntu.com/security/CVE-2026-31431

* openEuler 已独立验证 24.03、24.03-LTS-SP3 可复现，官方仍在调查中，请参考下文部署缓解措施。

https://security-tracker.debian.org/tracker/CVE-2026-31431

* SUSE 12~16 仍未修复，请参考下文部署缓解措施。（除15.6、15SP6、16.0部分内核）

https://deb.freexian.com/extended-lts/tracker/CVE-2026-31431

（三）、安全审计建议

权限限制：由于该漏洞需要本地访问权限（Local Access），建议严格审查系统上的低权限用户账号，防止攻击者获取初始立足点。

日志监控：监控系统日志（如dmesg 或／var／log／syslog），关注与 crypto 或 segmentation fault 相关的内核异常。

建议处置优先级：

 公⽹业务主机、CI Runner、容器宿主机、多⽤户登录主机 > 内⽹核⼼服务器 > 普通终端与低暴露⾯主机。

## 五、外部参考

* Copy.fail 网站：https://copy.fail/
* 漏洞报告者 Xint Code 技术分析：https://xint.io/blog/copy-fail-linux-distributions
* OSS-SEC 邮件列表： https://seclists.org/oss-sec/2026/q2/283
* CNVD 安全公告：https://www.cnvd.org.cn/webinfo/show/12336

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2nYVbJUzOCLdfwkVMSk0PQYHGMMEeUNNNEtadibvO9kdyxU8pNwe61WYA1VNIsFb5AzQOUvsPBOwFKoZHkaC3ZTq4fJWYQKthBnK62bicYtJw/640?wx_fmt=png&from=appmsg)

（图片由邵博同学提供）

感谢我公司邵博同学提供素材并进行漏洞验证。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/M8lZIYZticqThicmRwDMVejWOMdkFlrCt14n93c3scxgeDNsz071dNWRHLcmS28qGHReibpS7ZDFicXicKtkHmgE1vg/0?wx_fmt=png)

大兵说安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/M8lZIYZticqThicmRwDMVejWOMdkFlrCt14n93c3scxgeDNsz071dNWRHLcmS28qGHReibpS7ZDFicXicKtkHmgE1vg/0?wx_fmt=png)

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