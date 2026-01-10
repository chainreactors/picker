---
title: 轻量级安全扫描工具Lightx，内网自查与渗透测试利器
url: https://mp.weixin.qq.com/s/3jb_q_CwVD1tUut0b-HMCg
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:24:02.952675
---

# 轻量级安全扫描工具Lightx，内网自查与渗透测试利器

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/GOiczibvxk0XRI1oNZzFD04egYEwdB02JVChIXHlX0f5PAiajMub2r7oVyvibhoaBicdGo5Jia8wClBJCIEHqlKsTyPw/0?wx_fmt=jpeg)

# 轻量级安全扫描工具Lightx，内网自查与渗透测试利器

onewinner 陌离

泷羽Sec-陌离

![]()

在小说阅读器中沉浸阅读

# 轻量级安全扫描工具Lightx，内网自查与渗透测试利器

> ❝
>
> 为企业安全建设者打造的一站式扫描解决方案

在网络安全的日常工作中，高效且全面的扫描工具能极大提升工作效率。今天给大家介绍一款轻量级但功能强大的网络安全扫描工具——Lightx，它专为企业安全建设者和渗透测试工程师设计，集成了多种实用功能。

> ❝
>
> **工具我已经提前打包好了，可以扫描文中二维码进行保存，也可以后台留言"扫描工具"获取**![](https://mmbiz.qpic.cn/sz_mmbiz_png/GOiczibvxk0XRI1oNZzFD04egYEwdB02JVdB1coXkrp8DYibIbtiaKng13tia57ks2HbmhzicKw9zeLZhue6uQ7QYSpA/640?wx_fmt=png&from=appmsg)

## 工具简介

Lightx是一款集成端口扫描、服务识别、Web指纹识别、漏洞扫描和弱口令检测等多功能于一体的安全评估工具。它提供全面的安全评估能力，覆盖多数两高一弱（高危端口、高危漏洞、弱口令）场景，是企业内网自查和渗透测试的得力助手。

相比于一些庞大的安全扫描套件，Lightx保持了**轻量级**特性，资源占用少，却功能俱全。它的设计初衷很明确：满足日常检查工作需要和企业安全建设，提供全面的企业内网自查能力。

## 核心功能亮点

**多目标支持，灵活扫描**支持单个URL/IP、IP段、域名和文件列表等多种输入方式，适应不同扫描场景。无论是针对单个目标进行深度检测，还是对整个网段进行普查，都能轻松应对。

**智能端口识别与服务发现**采用高效的端口扫描技术，快速识别开放端口和服务类型。同时集成服务指纹识别功能，精准判断运行的服务及其版本信息。

**强大的Web应用识别能力**基于先进的指纹识别技术，Lightx能够精准识别Web应用程序、框架、CMS等技术栈。这对于资产梳理和风险定位尤为重要。

**全面的漏洞检测**内置基于Nuclei SDK引擎的漏洞检测能力，支持多种常见漏洞扫描。工具还保持了POC更新机制，确保能够及时发现新增漏洞。

**弱口令检测覆盖广泛**Lightx的一大特色是支持**全网最全的国产数据库检测**，包括DM达梦、Kingbase人大金仓、GaussDB高斯、TiDB、OceanBase等众多国产数据库的弱口令检测能力。同时覆盖30多种常见服务的弱口令检测。

## 实战操作指南

### 基本扫描命令

```
# 扫描单个目标
Lightx -t http://example.com

# 扫描IP段
Lightx -t 192.168.1.1/24

# 从文件读取目标列表
Lightx -t targets.txt
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GOiczibvxk0XRI1oNZzFD04egYEwdB02JVdB1coXkrp8DYibIbtiaKng13tia57ks2HbmhzicKw9zeLZhue6uQ7QYSpA/640?wx_fmt=png&from=appmsg)

### 常用场景示例

**完整安全评估**

```
Lightx -t example.com -r report.html
```

这个命令将对目标进行全方位扫描，包括端口、服务、Web应用和漏洞，并生成详细的HTML报告。

**专注Web应用扫描**

```
Lightx -t https://example.com --tag sqli,xss
```

仅针对SQL注入和跨站脚本漏洞进行扫描，适合针对性的安全测试。

**国产数据库专项检测**

```
Lightx -t 192.168.1.1 -p db -op dm_brute,kingbase_brute
```

专门针对国产数据库进行弱口令检测，突出重点资产安全。

### 插件化架构的灵活性

Lightx采用插件化设计，目前支持**70种服务**，插件总计**60个**，这种设计使得工具扩展性极强。用户可以根据需要启用或禁用特定插件：

```
# 列出所有可用插件
Lightx -lp

# 只运行指定插件（白名单模式）
Lightx -t 192.168.1.1 -op "mysql_brute,ssh_brute"

# 排除指定插件（黑名单模式）
Lightx -t 192.168.1.1 -ep "mysql_brute,ssh_brute"
```

插件按功能分为爆破类、未授权访问检测类、漏洞检测类和信息收集类四大类别，用户可以根据测试环境灵活选择。比如在生产环境中，可以排除爆破插件以避免账号锁定；在合规性审计中，可以只进行信息收集，不执行攻击性测试。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GOiczibvxk0XRI1oNZzFD04egYEwdB02JVdB1coXkrp8DYibIbtiaKng13tia57ks2HbmhzicKw9zeLZhue6uQ7QYSpA/640?wx_fmt=png&from=appmsg)

## 实操图片展示

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/GOiczibvxk0XRI1oNZzFD04egYEwdB02JVsItUib9DbZLbjF5h6XZmyouxcia9EVia2zzqvGjrrF3FYGDicsPQaico7rw/640?wx_fmt=jpeg&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/GOiczibvxk0XRI1oNZzFD04egYEwdB02JVGiaGAiaceSJ3mREOwcfDJFFkOQWxHZgqI1LicZzO88l6ibIITVOWCQwADQ/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/GOiczibvxk0XRI1oNZzFD04egYEwdB02JVYhP1qWv2RMCRzAqYDfFvOSFvsX1oUo3TKicEUUYJibQbYibdVYRaIWC0A/640?wx_fmt=jpeg&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/GOiczibvxk0XRI1oNZzFD04egYEwdB02JVSOQUsnl0RrjsMkKI6y6P4SmzvEE0X4kn00nof1icDFvtlLbNloP9FicQ/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/GOiczibvxk0XRI1oNZzFD04egYEwdB02JVvNRHSEnxmCXOjsWyd6t9FooPwwDRvN6oUE4vJl9Biaq1X3zt97Akbsw/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/GOiczibvxk0XRI1oNZzFD04egYEwdB02JV27qXEXn7DQibnLSkFgeJYCZFsV4xJoAoeKwWR3TT75YRJyYeqeagThg/640?wx_fmt=jpeg&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/GOiczibvxk0XRI1oNZzFD04egYEwdB02JVFugHicddrTRDwNOyoh5K8bac3LUCQV89qtb4YoiblFOUnHiapEmB52ThA/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/GOiczibvxk0XRI1oNZzFD04egYEwdB02JVpjlQ9rz0oqVKEeD3brBaVCglBgDds5qOF1TLf4jhdGRNVjakGYiaFCw/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/GOiczibvxk0XRI1oNZzFD04egYEwdB02JVc8o40CBM1lwtErRtZOMYYyGxwXwPTM2TrmnQ6W6AGOmJ69WRjovkJw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GOiczibvxk0XRI1oNZzFD04egYEwdB02JVdB1coXkrp8DYibIbtiaKng13tia57ks2HbmhzicKw9zeLZhue6uQ7QYSpA/640?wx_fmt=png&from=appmsg)

## 输出报告一目了然

Lightx生成的HTML报告包含完整扫描结果，结构清晰，包括：

* **扫描概览**：目标、时间、漏洞数量统计
* **端口扫描结果**：开放端口、服务类型、版本信息
* **漏洞详情**：发现的安全漏洞描述和风险等级
* **弱口令检测结果**：爆破成功的服务账号密码
* **统计信息**：各类扫描结果的汇总数据

报告还支持导出为markdown、json以及excel格式，方便进一步分析和归档。![](https://mmbiz.qpic.cn/sz_mmbiz_png/GOiczibvxk0XRI1oNZzFD04egYEwdB02JVqUxLXauLrDgaem6uo9tQDEzz0OicqNAkHic5zagqCgicFytcEZPdtaa4g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GOiczibvxk0XRI1oNZzFD04egYEwdB02JV2RcKpstc4nSf9030CqyemsNNDjz0TliaYbiaZmBI03f2kib2GHyeD8Pug/640?wx_fmt=png&from=appmsg)

## 使用技巧与注意事项

**性能调优经验**对于大型内网扫描，可以适当调整线程数参数`--thread`和TCP端口扫描线程数`--tcp-threads`，在速度与稳定性之间取得平衡。通常建议先在小范围测试，再逐步扩大扫描规模。

**规避防护策略**当目标部署有WAF等防护设备时，可以启用无痕模式`--stealth`，减少主动探测，降低被封锁的风险。同时，合理设置请求超时时间`--timeout`也能提高扫描成功率。

**合规性考量**在进行企业内网扫描时，注意排除爆破插件`-ec "brute"`，只进行信息收集，这样既满足合规审计要求，又避免对业务系统造成影响。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GOiczibvxk0XRI1oNZzFD04egYEwdB02JVdB1coXkrp8DYibIbtiaKng13tia57ks2HbmhzicKw9zeLZhue6uQ7QYSpA/640?wx_fmt=png&from=appmsg)

## 总结

> ❝
>
> 项目地址链接和详细教程：https://github.com/onewinner/Lightx

Lightx作为一款轻量级但功能全面的网络安全扫描工具，在企业内网自查和渗透测试场景中表现出色。其插件化架构和丰富的国产数据库支持使其在国内环境中具有独特优势。

**重要提示**：本工具仅限合法授权的安全测试使用，任何未经授权的扫描行为均可能违反法律法规。在进行安全测试前，请确保已获得充分授权。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/GOiczibvxk0XROVdRHd20297HPqUe6JxtuibRY8k4292NiaPqHIVPzf4CL3CiafGQAut0nZLWiau48GX68lVVovImbsQ/0?wx_fmt=png)

泷羽Sec-陌离

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/GOiczibvxk0XROVdRHd20297HPqUe6JxtuibRY8k4292NiaPqHIVPzf4CL3CiafGQAut0nZLWiau48GX68lVVovImbsQ/0?wx_fmt=png)

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