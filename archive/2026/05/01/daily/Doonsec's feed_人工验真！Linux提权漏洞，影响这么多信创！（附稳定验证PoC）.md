---
title: 人工验真！Linux提权漏洞，影响这么多信创！（附稳定验证PoC）
url: https://mp.weixin.qq.com/s/7mVx3sKx4SFSXR28Q1fOrA
source: Doonsec's feed
date: 2026-05-01
fetch_date: 2026-05-02T04:59:36.335313
---

# 人工验真！Linux提权漏洞，影响这么多信创！（附稳定验证PoC）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZaibroIiatwe3hCQTASuQgUG8YxK5gVho0Iiahva43oSuXqicJ6phc0FrpFtbuNQVvpZNrYYcvpPpCxPiaiarwew2FAXHjtuxJ1AeKo8lqZkmoyaA/0?wx_fmt=jpeg)

# 人工验真！Linux提权漏洞，影响这么多信创！（附稳定验证PoC）

利刃信安
利刃信安

利刃信安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

人工验真！Linux提权漏洞，影响这么多信创！（附稳定验证PoC）

一、 漏洞概况

微步情报局监测到，Linux Kernel 被披露存在本地权限提升漏洞，漏洞编号 CVE-2026-31431，代号 “Copy Fail”。该漏洞源于内核 crypto: algif\_aead 模块在处理 AEAD操作时的逻辑缺陷，可导致本地低权限攻击者通过 AF\_ALG 加密接口向任意可读文件的页缓存（page cache）写入受控的少量数据（PoC 中为 4 字节块），进而篡改 setuid 等特权二进制文件，实现本地权限提升至 root。

目前该漏洞细节及 PoC 已公开，利用门槛极低（仅需约 10 行 Python 脚本），影响过去 9 年内大多数主流 Linux 发行版。

微步情报局对部分操作系统进行了验证，UOS、麒麟、openEuler等信创系统，以及Redhat、Ubuntu等非信创系统均受影响，列表见下文。

OneSEC可以关注提权相关告警(规则ID：9030):![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/KJ5kFuz2K95LDOJCIlHvaJicgO2sTcu91HFmoDBy4Pf82Ih0ymCEy0qq0omnCjW2jEibz7KCFyg2cnMDxsTNhT4xrqicNdEFA4UAt5gUnVic7p0/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

二、已人工验证的系统

# UOS  受影响版本：1070、1060

统信软件推出的国产商业化Linux桌面/服务器发行版，基于Debian社区版深度定制

1070：

![图片](https://mmbiz.qpic.cn/mmbiz_png/KJ5kFuz2K945eYDaendmgfOL3hibtsGJ1MnaHQ0Y1icKuJAW6slyYUicFzc0Kmas3icVicw1LlicPKHrcC6icfowk55icLibf4JAibv3dzbfE4YUCdK3Q/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

1060：![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/KJ5kFuz2K95T42cRZ7JCFMEYOLicGkNObh6wficuVWciaRXvZYHS6TkkS1HyXmgNKBictdLBdpqlrpoM5M8DlUPlr7YMZkMC9xEfYonkKG2hJgM/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/KJ5kFuz2K95eaiaI17nDpNEsycRHOerCdI4fAeUByVmPzoYgx9Mk6e28RZN4rSN5ibW1FZuvl2PCxmOHV86LzrkyEx5QuOKeYDoBiakSyHlWEM/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

kylin  受影响版本：V11、V10

天津麒麟开发的国产Linux操作系统，广泛应用于政府与军工领域

V11：

![图片](https://mmbiz.qpic.cn/mmbiz_png/KJ5kFuz2K95pHGtqrDaVGiaKrTiawU3Ziasr0HVxPtw7TGQ9EalTnkbvNb3cgpyboF3GB752ef99v0fibLSK8vHArx0FghZck4H7V6hUtwECORU/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/KJ5kFuz2K94mAEDxzlz8mcyePXdR3aoPEPH1tPoW8PmLhuOWpTa1y6yaOUoa2kl8ibNXgH4hrQZEibYxGZ1krnzZYNY1Q1vNXaITzFlicMCbIM/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

V10：

![图片](https://mmbiz.qpic.cn/mmbiz_png/KJ5kFuz2K97pslyhEO7ztMJNy2cMK9RcEabPC7HohGgE6qpUQuaIdIqd8pZMpnoIqw34sNLB10165vcG8lbLp0NPQPXUZndOaue1SicNXA6s/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

CUOS   验证版本：4  不受影响

中国联通推出的企业级Linux服务器操作系统，聚焦云与通信场景

![图片](https://mmbiz.qpic.cn/mmbiz_png/KJ5kFuz2K97q2YryQz1XMJqSbFicHibop0e3H9pfbSyc8F0fWxibPXzJp6JBYrqiaWt0ibj6CPJiajTF6ILvnrmCBC5q2gSoDkiaqJ9icV7CWbzdys4/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

openEuler  受影响版本：24.03 (LTS-SP1)

华为开源的国产Linux发行版，聚焦服务器与云计算场景，LTS长期支持版本

![图片](https://mmbiz.qpic.cn/mmbiz_png/KJ5kFuz2K97NibakmRibewd28TOCT6C288ca28Ez5J95me5iacBZmMtqFiaJGbp8ZRO5ENWdTLUPIefq5fL2ENDPicl3CxHFmCiavVzF1sqGx8Rds/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

CTyunOS  受影响版本：V4.0 25.07

中国电信基于openEuler衍生的服务器操作系统，面向CTyun电信云基础设施

![图片](https://mmbiz.qpic.cn/mmbiz_png/KJ5kFuz2K96YvU1MnY8Mbia5rdLnhUptdhFoM0UxewpiaqRH0XnDzROKwkzYGUO7xf1JrcY3aobywRnfYTrpbEiaSMfOzBjTPPnibVicKMXjw9Gc/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

Ubuntu  受影响版本：V22.04  不受影响版本：V17.04

Canonical发行的全球流行Linux桌面/服务器发行版，生态成熟、用户基数大

V22.04：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/KJ5kFuz2K95lFgzSVzwiaCXib4meuFsEYdnk83HV25Sf1nFOIxrvwZTOjv1ohoiaSrPhyoibP1QjvrXJmFze2ibibaicmeRIjcu5PicI26iaV70x44RY/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)

V17.04：

![图片](https://mmbiz.qpic.cn/mmbiz_png/KJ5kFuz2K94DTU29d0dflAiaRHl25FvPKlN6GSCtyicXmqRDqqMTXcbrydNGg19czwZuqtlTichpxgqlzaX3G3RomxRdbFLIiaPDMNPylnGQibMw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=11)

Redhat  验证版本：7.9不受影响

红帽企业级Linux（RHEL）经典版本，企业服务器市场的主流选择之一

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/KJ5kFuz2K97qDribohPvCSmZv5aJzEOwTXMrWKRJW9L7sgaVqKXrBAoyQqbaSVCrGuMOfUXIt4htvOgyXBuagc6mibKRaK3ibl1ibqNQnZH3hTI/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=12)

CentOS  验证版本：7不受影响

原社区版企业级Linux，7为Stream前身，现已转型为RHEL的上游预览版

![图片](https://mmbiz.qpic.cn/mmbiz_png/KJ5kFuz2K96icxkFsY6QtWtNiabVVqclAUhkQ6PSbcH9l3GOuwudgkZQoH0J3h5BziaFL2gPDkhCXVAI29oJecA40YKBf5cDAsM1GnbY0oOsII/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=13)

Anolis OS  受影响版本：8.9

阿里云开源的国产Linux发行版，与RHEL生态二进制兼容，专注云与数据中心场景

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/KJ5kFuz2K95dufPr9tyu3rQDJB7dgxhSxqBwp2NKL4icYq5bSWDH1icBpEU31DibS8Pp8ibb4AmiazIV5JbzibMSaTkJKwJuf0OS7H0lXQtjD0tg0/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=14)

Oracle Linux  受影响版本：10.0

甲骨文推出的企业级Linux，基于RHEL兼容内核，提供UEK内核与RHCK双启动选项

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/KJ5kFuz2K96BLVBZnjJjQ0HuXLnQoxibpDvJ5EbmRcI8Ad3z50Gn5iaeIibdHzvlA2Ric409adXCoicYbSIrGqib0GEK0NJUgWtcQLEdMdfyhC6ro/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=15)

OpenCloudOS  受影响版本：9.4

腾讯主导开源的国产Linux发行版，源自CentOS Stream，聚焦云原生与服务器场景

![图片](https://mmbiz.qpic.cn/mmbiz_png/KJ5kFuz2K95cGdd8LFwH5JOtn3mxSK8k0h6aRViaEwA1kYgFc4ib14716hxVeUZ0EBpiasbwJnbJaBrNSUdV47z8G5EbKXDJJEDxt5AbV3bJXE/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=16)

NewStartOS  受影响版本：6.06

湖南麒麟研发的国产Linux桌面/服务器操作系统，基于Kylin内核，聚焦政府与教育行业

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/KJ5kFuz2K94pHYryqicZqKicn8dUxQpvVIjkphF6vncC3XM1emR0kibz0qiawjmTd5Z2OWrXM6iasVtdM398ia4feyMeTJOtBW61oDuTvFMqQOPh4/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=17)

Debian  受影响版本：13

社区主导的经典自由开源Linux发行版（代号"Trixie"），是Ubuntu/RHEL等众多发行版的上游根基

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/KJ5kFuz2K95gemxE0ibW7R2yUZibnORVjiaZiauKHicCh5ibkiaIybKodg9ibbBPI61ib8BrpoibK7Es3GOJSozlvMV7FcORNO3b3lo9M1nYFcrPVnXWI/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=18)

三、其他版本验证

由于公开的Python PoC的检测准确性依赖于Python版本（Python低版本较低时需要的底层接口可能并未实现），如果想自查所用操作系统是否受影响，建议使用微步提供的通用PoC进行排查。

风险提示：禁止在线上环境进行验证，验证程序可能会损坏系统的su命令内存映像。

curl -fsSL https://onesandbox-release.threatbook.cn/poc/CVE-2026-31431/copyfail -o /tmp/copyfail && chmod +x /tmp/copyfail && /tmp/copyfail && rm -f /tmp/copyfail

![图片](https://mmbiz.qpic.cn/mmbiz_png/KJ5kFuz2K94Gxb4RoOzWiaCFIkUKgo65MPqjWUgMVqxdO546zZWPywpfnwDuXcH1XSY3QazPqcvL8icODtY1ZWkoLYKypcNaxNkkpk5IMQhN4/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=19)

四、修复方案

* ### 彻底修——升内核

| 情况 | 命令 / 操作 |
| --- | --- |
| 查看当前内核 | `uname -r` |
| Ubuntu / Debian | `sudo apt update && sudo apt install linux-image-6.18.22-generic && sudo reboot` |
| 通用升法 | 去 kernel.org 拉 6.18.22 / 6.19.12 或更高版本 自己编，或者等发行版更新 |

* ### 临时堵——禁用 algif\_aead

```
sudo modprobe -r algif_aeadecho "blacklist algif_aead" | sudo tee /etc/modprobe.d/99-copy-fail.conf
```

绝大多数系统用不到这个模块，禁掉无副作用。

* ### 容器 / 沙箱应急——拦 AF\_ALG

用 seccomp 或容器策略，禁止创建 AF\_ALG 套接字（type=38）。

Docker 示例：

```
{  "defaultAction": "SCMP_ACT_ALLOW",  "syscalls": [{    "names": ["socket"],    "action": "SCMP_ACT_ERRNO",    "args": [{"index": 0, "value": 38, "op": "SCMP_CMP_EQ"}]  }]}
```

* ### 快速自查

```
lsmod | grep algif_aead   # 模块在不在lsof | grep AF_ALG         # 有进程在用这个 socket 吗
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe1Ijz7jib5Bwjy65Kzg7q6JU6BGvgr2NLDZOvGs639QJHWib6ibMWNN4nGGlAgbfBtiaRWccAfh4KGpoibDzDwLQW9Nbb5QtE0yibdww/0?wx_fmt=png)

利刃信安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe1Ijz7jib5Bwjy65Kzg7q6JU6BGvgr2NLDZOvGs639QJHWib6ibMWNN4nGGlAgbfBtiaRWccAfh4KGpoibDzDwLQW9Nbb5QtE0yibdww/0?wx_fmt=png)

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