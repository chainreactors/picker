---
title: 【0DAY漏洞】xa0全球5G手机芯片厂商之一u200c的紫光展锐SOC存在RCE漏洞，影响数十家手机厂商，还未发布补丁
url: https://mp.weixin.qq.com/s/3BMvBXIW9MNgnyNTcKPZKg
source: Doonsec's feed
date: 2026-08-18
fetch_date: 2026-08-19T02:53:16.042461
---

# 【0DAY漏洞】xa0全球5G手机芯片厂商之一u200c的紫光展锐SOC存在RCE漏洞，影响数十家手机厂商，还未发布补丁

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LAQpgdWQSct4ox7hAy1j3PnibFic2cl53SiccR5LUpkubQRibKd1GKYG1ZevfDunRDEpKzeyd0AiamQnnsfFcTnZb1ibyMqOricmjlFdc6F1QnzNJk/0?wx_fmt=jpeg)

# 【0DAY漏洞】 全球5G手机芯片厂商之一‌的紫光展锐SOC存在RCE漏洞，影响数十家手机厂商，还未发布补丁

YGnight
YGnight

night安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LAQpgdWQSctVS8Ps0NsFTqMiasz8uDibcvoib0spt17ORFYGT7Lk8y0JElHpWukiczXboIicO8mrOUut0DwfE4PvMwpuReeibS0yQHqN8Tictdm4Z4/640?wx_fmt=png&from=appmsg)

## 漏洞描述

紫光展锐是中国集成电路设计产业的主要企业，‌全球公开市场 3 家 5G 手机芯片厂商之一‌。收到情报紫光展锐移动 modem 固件蜂窝网络侧存在远程代码执行缺陷0DAY漏洞。攻击面位于 SIP 信令层，畸形 SDP 载荷经 SIP INVITE 抵带至目标 modem，触发内存破坏并在受害 modem 上执行任意原生代码。载体是 SIP 消息内夹带的 SDP，无需受害者交互，双方处于同一电话网络可达路径即成立。经查询涉及此楼的4个展锐 SoC 平台：T612、T616（官方已更名 T7255）、T606、T7250。这些平台广泛用于入门/低端 Android 机型，覆盖约 10 个品牌

这个漏洞归类为 CWE-674 不受控递归。modem 解析 SDP 时，acap 属性解码函数 \_SDPDEC\_AcapDecoder 未设递归调用上限。单行属性内连续出现多个 acap 时，SIP 任务栈持续向下生长，越过自身栈边界踩入相邻 sblock\_0\_2 任务栈，从而导致栈溢出问题。

|  |  |
| --- | --- |
| 漏洞类型 | 不受控递归 / 栈溢出 / 远程代码执行 |
| 影响组件 | 紫光展锐 modem 固件 SDP/SIP 解析层 |
| 受影响型号 | T612、T616、T606、T7250 |
| 受影响固件 | MOCORTM\_22A\_W23.02.5\_P12.14\_Debug（Realme C33 搭载） |
| CWE | CWE-674 不受控递归 |
| 攻击前提 | 攻击者持有一台 UE，蜂窝网络可达，无需受害者交互 |
| 报告来源 | SSD-Disclosure 公开技术报告 |

攻击者持一台网络可达 UE。后果：受害 modem 上执行任意原生代码。紫光展锐官方截至目前还没有发布漏洞相关补丁，也还没有公开回应。

## 漏洞原理

主要原因是acap 属性解码函数未对递归深度设限。modem 收到 SIP INVITE 后解析其 SDP，SDP 每行属性经 SipHandler\_AttrDecoder 查表取得对应 handler 并调用。acap 对应 handler 为 \_SDPDEC\_AcapDecoder，该函数解析完当前 acap 值后读取下一属性名再查表，若仍为 acap 则递归调用自身。

```
undefined8 _SDPDEC_AcapDecoder(Token *token, ParseBuffer *parse_buffer, SdpMsgStruct *hSdpMsg)
{
    // ... 解析当前 acap 值 ...
    iVar2 = search_handler(&token->CurrToken, SipHandler_AttrDecoder, 0x38, &handler_id);
    handler = SipHandler_AttrDecoder[(int)handler_id].handler;
    token->currentHandlerExecution = handler;
    if ((handler == (sipHandlerFunc *)0x0) ||
        (cVar1 = (*handler)(token, parse_buffer, (int)hSdpMsg), cVar1 == '\x01')) {
        // handler 调用，若下一个属性仍为 acap，则递归调用自身
    }
}
```

acap 在 handler 表中自我引用，一行内连续多个 acap 时 handler 逐层递归调用自身，全程无深度上限。触发载荷格式如下。

```
8d0f280c 80 a0 e1 8b 3d   SipHandler [49] = "acap"
00 00 00 c3 15 c9 8b
```

```
v=0
a=acap:1 acap:1 acap:1 acap:1 acap:1 acap:1 acap:1 acap:1 [...] acap:1
```

递归层数叠加，SIP 任务栈持续消耗内存，越过自身栈边界写入相邻 sblock\_0\_2 任务栈，栈溢出。

```
for i, part in enumerate(get_shellcode_parts()):
    send_exploit(part, SIP_SEQ_ID, 165 - i * 8)
    SIP_SEQ_ID += 1
```

栈溢出后，原生的shellcode分块写入后续的SIP请求，modem 内存暂存拼接。shellcode是ARM Thumb 汇编，向固定地址 0x8d0f270c 写入标记值 0xdeadbeef，确认代码执行在 modem 上成立。

```
_second_chunk:
    movw r1, #0x270c
    movt r1, #0x8d0f
    movw r2, #0xbeef
    movt r2, #0xdead
    str r2, [r1]
```

验证脚本 dump\_modem.sh 经 adb 导出整块 modem 内存，analysis.py 解析 0x372F000 起始的寄存器区，得到 r1 = 0x8d0f270c、r2 = 0xdeadbeef。0xdeadbeef 已写入目标地址，代码执行在 modem 环境成立。

## 修复建议

官方修复状态：紫光展锐官方截至目前还没有发布漏洞相关补丁，无明确修复时间表，等待厂商后续固件推送。由于modem 固件是闭源的，使用的用户是无法自查或修复防御的，能做的就是保持运营商固件为最新、避免接入不可信漫游和SIM网络

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/SaibaRNhOjqiaCicRfSc5cJ3oiaCRqb97SmncCWWvuTyytibyIDxB9ZXWOuNaiaGAX2t0DYAAbdJ7aicS6WeCz4wfMoUg/0?wx_fmt=png)

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