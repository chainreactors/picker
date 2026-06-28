---
title: 不会找漏洞 试试Nuclei这款神器
url: https://mp.weixin.qq.com/s/6J6VJ_XGoC4lk-WrdM9N7g
source: Doonsec's feed
date: 2026-06-27
fetch_date: 2026-06-28T06:12:53.710245
---

# 不会找漏洞 试试Nuclei这款神器

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6OgreibV1aHcZQL6ZYKOKLtia9pYRdGBlzcN54YtjDFqZ2fOMHCkyGxYibAjlK8svPVNC0cK3bAl64VG940ISqgNxbTymRBVmkibe0/0?wx_fmt=jpeg)

# 不会找漏洞 试试Nuclei这款神器

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于kali笔记
，作者大表哥吆

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6DBXaFMbqQ0IcXx6yjOS0WlJOZqJj2a6TyY8zId0YJ0g/0)

**kali笔记**
.

发布关于Kali Linux学习和相关安全领域的文章、致力于网络完全学习和研究。以及Debian Centos等操作系统的安全和运维，同时涉及到对树莓派 ESP8266 Arduino等物联网领域的开发和应用。

> 在日常学习中，安全扫描是绕不开的一环。传统的工具如 `OpenVAS`、`Nessus`要么太重，要么太贵，而且扫描规则更新慢、定制难度大。而今天为大家推荐的Nuclei是 一款**基于模板的扫描器**。

Nuclei 官方模板库目前已有 **7000+ 个模板**，覆盖 CVE、默认配置泄露、渗透测试、技术指纹识别、网络基础设施检测等方方面面。而且每天都有新的模板发布。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBoreIKWhzhibFA3BjicS7NouqicF9GcrHBkLRcCoPydVh4qRAbTVSLyrlNdfHxNrbYZlicia8yib07TriaSvrlHuibRy0M4oCgDwradV8R7s/640?wx_fmt=png&from=appmsg)

# ![](https://mmbiz.qpic.cn/mmbiz_gif/1N1JeeKBorcWzpUa4nicDVficia3fkhUWHm9hvF7bsG4Qyx77Acw2x9paPSJ5azARCs72IkibfJ6M2I496lRTSVLDhZLXo1TpMfmHdY5uA3qm9s/640?wx_fmt=gif&from=appmsg)安装![](https://mmbiz.qpic.cn/mmbiz_gif/1N1JeeKBorcqM8yNc7ktLT1qmmYqtJD7hWBsVcgtWOpy24jlCJU78PSMss57QGdlQLJtic9nXA08MM2U3hmiayjOYaIuZRSbq5kaDDCzTIldo/640?wx_fmt=gif&from=appmsg)

在Kali中已经默认安装，若没有安装，可以通过下面命令一键安装。

```
sudo apt update
sudo apt install nuclei -y
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBorcrVSy9OIeD5xcy0kwKy5EtTJhx9Y8ZXFt1dAFMaFRFiasv3ibP4Hx3gXcXESBibm9Lf9jRiaGbRyauOwLfxib4qz4XthEPYbDYbMjM/640?wx_fmt=png&from=appmsg)

**更新模板**（最重要的一步！）
Nuclei 的功能完全靠模板驱动，所以第一步就是把模板更新到最新：

```
nuclei -ut
```

这条命令会从 GitHub 下载/更新官方模板库，存放在 `~/.local/nuclei-templates/` 目录。
如果不能安装，可以直接在Github中下载到本地。

> https://github.com/projectdiscovery/nuclei-templates

# ![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1N1JeeKBorffDWO2IcAqvbg7CJrymvAsJsnZEaKgKYTZ9Uk9ayJGEeMXqibTSnrCOzmaB5o5n8d2EfMZxTib6Ks1kBnV8UicTl2Xkw0GFudmTM/640?wx_fmt=gif&from=appmsg)快速开始![](https://mmbiz.qpic.cn/mmbiz_gif/1N1JeeKBoreQ2DIuDFbbopNibKcrkrDffWZnQ7Xo6CRVTlfiaHQ3MqV4h4mTwwQIp3ldohI4RuW61CsyxhCKjITRxaORF8Yw0BMMMPQvicPN9E/640?wx_fmt=gif&from=appmsg)

**扫单个目标：**

```
nuclei -u https://example.com
```

![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBordz6WRv2Nia9rMRSem08ubLgBY4sbOkFsrH84LQsQhdycxOT4NiasbdEggdp01nPekd5GIw8ibxt0tdXJAiauPwYj5a5DxiacMMLg5w/640?wx_fmt=png&from=appmsg)

这是最简单的用法。Nuclei 会自动加载所有模板，逐个发送请求进行检测。如图，共加载了`2390`个模板。

**😘批量扫描多个目标：**

```
nuclei -l targets.txt
```

**☢️只显示发现的问题**（静默模式）

```
nuclei -u https://example.com -silent
```

默认输出会带上各种信息头，`-silent` 只打印发现的漏洞结果，干净利落，适合管道操作。

**🐧只扫高危和严重漏洞**：

```
nuclei -u https://example.com -s high,critical
```

可用级别：`info`、`low`、`medium`、`high`、`critical`、`unknown`

**🐻‍❄️按模板 ID 指定**
默认是全部扫描，这个的扫描是非常耗时的，因此我们可以指定模板进行扫描。

```
nuclei -u https://example.com -id spring4shell,log4shell
```

多个 ID 用逗号分隔，支持通配符。

**📧只跑指定模板目录**

```
nuclei -u https://example.com -t http/cves/
nuclei -u https://example.com -t http/cves/2024/
```

**`-as` 参数是 Nuclei 3.x 的王牌功能！** 它会先用 Wappalyzer 识别目标用的技术（如 Nginx、PHP、WordPress 等），然后只加载相关的模板，大幅提升扫描效率和准确率。
自动识别技术栈 + 定向扫描（推荐）

```
nuclei -u https://example.com -as -s medium,high,critical -o vulns.txt
```

![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBoreIz8H4X2AriceOPBicuywDiaMhEGcAoboBon0lbxgnMkWC7CmaHdj5wj5uzD132I8p4jG9PEHlnIyorBica4WIs2jbB8icf52YLo1A/640?wx_fmt=png&from=appmsg)

Nuclei 先自动识别目标用了什么技术（Nginx、PHP、某 CMS 等），然后只跑相关模板，速度快了不止一个量级。

![扫描到的信息](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorcfXVvggXQMwVR83ia79icvmQuLCmzLmCp6gibKYEtzfC9xgs3QHj2RibVGR8ibmQmcG1QAZMdLrz3AE8Za6e6eB3Jian9iaibibpKQq6iak/640?wx_fmt=png&from=appmsg)

扫描到的信息

**🐸批量扫 CVE 漏洞**

```
nuclei -l targets.txt -tags cve -s high,critical -o cve_results.txt
```

只扫高危和严重等级的 CVE 漏洞。适合用来快速排查目标是否存在近期高危漏洞。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1N1JeeKBorfFCsWsiaKI0reicwPdQ3NQic4xrq1FPrlibV5JaX6PZsicDVlic4ma8hWaUsk4hnSdUicEZPMxlMpJS4F7WbhZ08sy7UL5ia4LxkN1OsQ/640?wx_fmt=gif&from=appmsg)模板编写入门![](https://mmbiz.qpic.cn/mmbiz_gif/1N1JeeKBorfNfR8Lj531WLMae0ClJaTPhvxF7ThwtIaLOfg5ibNfQ2f7TU1hyGalibmXCmz65abq53OCIBhoBkoy6z9f4TKrwEib6e6tye5UVM/640?wx_fmt=gif&from=appmsg)

Nuclei 最强大的地方在于**你可以自己写模板**。举个例子，假设你想检测某个应用的后台路径是否存在，只需要写一个 YAML 文件：

```
id: myapp-admin-panel

info:
  name: MyApp Admin Panel
  author: 逍遥子大表哥
  severity: info
  description: 检测 MyApp 后台管理页面
  metadata:
    max-request: 1

http:
  - method: GET
    path:
      - "{{BaseURL}}/admin/"

    matchers-condition: and
    matchers:
      - type: word
        words:
          - "MyApp Admin"
          - "Dashboard"
        condition: or

      - type: status
        status:
          - 200
```

保存为 `myapp-admin.yaml`，然后用：

```
nuclei -u https://example.com -t myapp-admin.yaml
```

# ![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1N1JeeKBordV5sercKVJba2sX5grYN86z5mxyHBMuWg3Yicve588Dv1mQ9PH8Khvvr3vMHS9dDQQ39zsibUcoAwFS35licm2BzA019gNHy3sNY/640?wx_fmt=gif&from=appmsg)AI接入![](https://mmbiz.qpic.cn/mmbiz_gif/1N1JeeKBorfp5hVWIPds07kVc02ib8GbMYEjQDibhdqVCEoxHTcRa12NI89XY6hsszQfexC7fr8RW50Kic8n4PHUWQicQ4EQeNrc3ov2vq5Q57k/640?wx_fmt=gif&from=appmsg)

Nuclei 3.x 新增的杀手级功能——**用自然语言描述漏洞，AI 自动生成检测模板**：

```
nuclei -u https://example.com -ai "检测 Apache Shiro 反序列化漏洞"
```

Nuclei 会调用 AI 模型，根据你的描述生成对应模板并立即执行扫描。前提是配置了 AI API Key（目前支持 OpenAI 兼容 API）。

# ![](https://mmbiz.qpic.cn/mmbiz_gif/1N1JeeKBorc7BXpB1Qo3G6fIjPicxVqmCjvydgo8LFAC4wcFZfYIhiaEYyOaicL8l545tYwDr4e4uMJCyB9BILuzvMHxPVngaQ7b3wuNiceRUlU/640?wx_fmt=gif&from=appmsg)总结![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1N1JeeKBorc5lsAeNNEvrUBRz1j9z6zIOSKyBrTuCfaPQcg9bDdpK8cMDkpcmYWFQONx2wicKtgtPJHBLKI3UAjiadY93oSF4ByaWI2BIPxU0/640?wx_fmt=gif&from=appmsg)

Nuclei它不只是一个扫描器，更像是一个漏洞检测框架。YAML 模板的灵活性让任何人都能快速编写检测规则。让小白上手更简单！

更多精彩文章  欢迎关注我们

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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