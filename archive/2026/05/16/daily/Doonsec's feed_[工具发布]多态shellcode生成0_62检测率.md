---
title: [工具发布]多态shellcode生成0/62检测率
url: https://mp.weixin.qq.com/s/xkbXxSpvZ-1h5E-0jbZiyA
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:43:58.305797
---

# [工具发布]多态shellcode生成0/62检测率

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibXL9MCj2GqO0D15zlNWnI6ErkHdRBm6fKkO0eD91ZBUcG1qPXae0FYtOr0XgpjibE34TUSaORD64f4hGia7plCums1N6zX7GzTqTlZ8FluI3M/0?wx_fmt=jpeg)

# [工具发布]多态shellcode生成0/62检测率

原创

陆安予
陆安予

白帽子安全笔记2.0

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# [工具发布]多态shellcode生成0/62检测率

采用多态shellcode将实现内存完全无法检测，绕过基于固定特征的检测。

### 一、背景

众所周知，Donut生成的shellcode`非常容易被检测`，一个精准检测规则如下：

```
meta("shellcode", "Donut");
function detect() {
    bDetected = false;
    // https://github.com/TheWover/donut/blob/dafea1702ce2e71d5139c4d583627f7ee740f3ae/donut.c#L1235
    var bInstCall = Binary.readByte(0);
    if (bInstCall != 0xE8) {
        return result();
    }
    if (Binary.readWord(1) != Binary.readWord(5)) {
        return result();
    }
    var callDest = Binary.readDword(1)
    // https://github.com/TheWover/donut/blob/dafea1702ce2e71d5139c4d583627f7ee740f3ae/donut.c#L1239
    var popECXOffset = callDest + 5; // 1 byte for E8 (call opcode) and 4 bytes for destination offset
    if (Binary.readByte(popECXOffset) != 0x59) {
        return result();
    }
    bDetected = true;
    var archDetectionOffset = popECXOffset + 1;
    var archDetectBytes = Binary.readDword(archDetectionOffset) & 0x00ffffff;
    switch (archDetectBytes) {
        // https://github.com/TheWover/donut/blob/dafea1702ce2e71d5139c4d583627f7ee740f3ae/donut.c#L1242-L1248
        case 0x52515a:
            sOptions = "x86";
            break;
        // https://github.com/TheWover/donut/blob/dafea1702ce2e71d5139c4d583627f7ee740f3ae/donut.c#L1270-L1273
        case 0x48c031:
            sOptions = "x86 + AMD64";
            break;
        default:
            sOptions = "AMD64";
    }
    return result();
}
```

由于Donut每次生成的shellcode特征固定，比如开头必须是`e8`(CALL)，然后连续2个相同数据`79 3B 25 01`。

> 意味着内存扫描一看是donut特征，将立即触发报警，直接GG。

![donut生成的shellcode固定特征](https://mmbiz.qpic.cn/mmbiz_png/ibXL9MCj2GqOWjakhw3nF4zMd0zLH9u3UYZquibtwvGaO7Qmlxiady62uRWttWX3uZiaLARVtbV8yWUTXVnyVvU0LicibbzVsniakVuGqjNEsJ7R0o/640?wx_fmt=png&from=appmsg "null")

donut生成的shellcode固定特征

现在，使用我最近开发的`donut-gui`生成`fscan`的shellcode测试下：

![donut-gui](https://mmbiz.qpic.cn/sz_mmbiz_png/ibXL9MCj2GqMo8ZRou3a7kN637wxD3KyI6ChG7R5g023oJQS6p9ElhyNgzGiclqHv9hV1oia7omXJDXkiaOqnu9hbghPxYF50ibCfGyKTjDuYuCY/640?wx_fmt=png&from=appmsg "null")

donut-gui

接下来，找一个环境验证下这个特征：

![donut在内存中的特征](https://mmbiz.qpic.cn/mmbiz_png/ibXL9MCj2GqNT1xuhF9gh2ebhqX4lwuEtRia6vAfJkPh64W1A8kF0wy07o5ibFQAYEDhSNcAWmGfTjQvhRKQoqoL7SBD6Fatet9eRWagnSvC7c/640?wx_fmt=png&from=appmsg "null")

donut在内存中的特征

> 本以为火绒有donut特征，结果发现没加...

那么就测试下其它的，直接丢到virustotal[1]:

![donut生成的shellcode检测率](https://mmbiz.qpic.cn/sz_mmbiz_png/ibXL9MCj2GqNt3uVz9GkLn1ZuDc3LRUhNyyH3tHLgMbvMkwoTmiaVX1icy7xbeOaskWqNL5SdAMGXAkgSwbZ55rxMyjqSMl7W1icrIL5Cs7MCBI/640?wx_fmt=png&from=appmsg "null")

donut生成的shellcode检测率

如此高的检测率，符合预期。

### 二、多态shellcode超越donut

使用更先进的多态shellcode生成，它将在donut上采用更高级的规避技术。

![fritter-gui生成shellcode](https://mmbiz.qpic.cn/sz_mmbiz_png/ibXL9MCj2GqOaWJzD67XZzZcmUuytaafrRiaDs08CiaBgtJvfLXznTUiaCe4alCJcfhKvmwmibMjx6LRiaJZ8s3ibBUOBaOaUprsleIkYRcqzx7oLk/640?wx_fmt=png&from=appmsg "null")

fritter-gui生成shellcode

每次生成的shellcode都不同。每次工具构建都不同。而且载荷更小，比donut小4倍。

![每次生成都不相同，无特征可循](https://mmbiz.qpic.cn/mmbiz_png/ibXL9MCj2GqNtRMGrG2OU0VoMiaApthFr6N4NWVFYXSRwmlq5qf5AiaZIVqSI455tu4xqEyLfzUbU2xmMUWPGgYskBHuhklDmicoWAMuelYcWs4/640?wx_fmt=png&from=appmsg "null")

每次生成都不相同，无特征可循

接下来直接丢到virustotal[2]，直接秒杀全球杀软，这还是未混淆的fscan。

![多态shellcode秒杀全场](https://mmbiz.qpic.cn/mmbiz_png/ibXL9MCj2GqOZZSIRBsEap9zIicvzuy3qJuOeL6icpH9FW5RQicSrWqSshdeoLH8XmJypLicC5o41BbT9Bbl5IWxhHykHK8SUoSSFGibRaPYwbGdw/640?wx_fmt=png&from=appmsg "null")

多态shellcode秒杀全场

同样的测试下运行，十分流畅。

![fritter在内存中的特征](https://mmbiz.qpic.cn/mmbiz_png/ibXL9MCj2GqM3WlO8icQpar4WxEtUInvu0kPcKCbzfGT0sm59m0697Tfpw3okrb2Z7I5iazicdcAVhd02gSnOHxoz8iasK3LfqqgswQiakdJZ8eNs/640?wx_fmt=png&from=appmsg "null")

fritter在内存中的特征

---

### 三、总结

使用多态shellcode工具将大幅改进donut特性，毫无疑问是红队人员的必备利器。这里我简要对比下：

| 序号 | donut | fritter |
| --- | --- | --- |
| 特征 | 特征固定 | 随机 |
| 大小 | 47.9M | 14M |
| 检测率 | 18/52 | 0/62 |

本文所有涉及工具均公开，清单如下，将放在武器库中供红队人员测试研究：

| 序号 | 工具名 | 用途 |
| --- | --- | --- |
| 1 | donut-gui.exe | donut的gui版本 |
| 2 | fritter.exe | 命令行版本 |
| 3 | fritter-gui.exe | fritter的gui版本 |
| 4 | fscan.exe | 未混淆的fscan |
| 5 | fscan-ob.exe | 混淆处理后的fscan，直接使用 |
| 6 | fscan\_donut.bin | fcan的shellcode |
| 7 | fscan\_fritter.bin | fcan的shellcode |
| 8 | shellcodeTester.exe | 加载shellcode |

---

### 四、最近视频

另外，最近也更新了许多视频，原创文章更新不会那么频繁，但有原创时会发布。

* • 危险的PDF文件，Adobe高危漏洞[3]
* • 无特征载荷绕过全球杀毒软件[4]
* • shellcode/汇编/加载器是什么？怎么用？[5]

---

### 五、免责声明

本文涉及方案仅限合法授权的安全研究、渗透测试用途，使用者须确保符合《网络安全法》及相关法规。具体条款如下：

* • 仅可用于已获得书面授权的目标系统测试；
* • 遵守法律法规，不得用于侵犯他人隐私或数据窃取；

本人不承担因用户滥用本软件导致的任何后果。使用即视为同意并接受上述条款。

---

#### 引用链接

`[1]` : *https://www.virustotal.com/gui/file/d8167724cd7f018fd412b2c11bbcf72d5b801ea6a9111d858a84d75069243578?nocache=1*
`[2]` : *https://www.virustotal.com/gui/file/323b52fd9f771f8cac150d51c118dfe6788ad7ba21c4202ad03a3b3e8e18c201?nocache=1*
`[3]` 危险的PDF文件，Adobe高危漏洞: *https://v.douyin.com/Fj072JVEWGE*
`[4]` 无特征载荷绕过全球杀毒软件: *https://www.bilibili.com/video/BV19A5G6fEQo*
`[5]` shellcode/汇编/加载器是什么？怎么用？: *https://www.bilibili.com/video/BV1RU5A6TENK/*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ibXL9MCj2GqM0QSEUqWHz3BBibqxHbxaC5wibm9paYNX1cJYtzWM4k6eibECJN0DQ2t8WFbiaPsorl4kibSB0hMqdpYmN1TTXHicgnCdSGNSomJBjI/0?wx_fmt=png)

白帽子安全笔记2.0

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ibXL9MCj2GqM0QSEUqWHz3BBibqxHbxaC5wibm9paYNX1cJYtzWM4k6eibECJN0DQ2t8WFbiaPsorl4kibSB0hMqdpYmN1TTXHicgnCdSGNSomJBjI/0?wx_fmt=png)

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