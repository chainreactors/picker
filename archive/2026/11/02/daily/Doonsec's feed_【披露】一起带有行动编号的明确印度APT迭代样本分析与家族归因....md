---
title: 【披露】一起带有行动编号的明确印度APT迭代样本分析与家族归因...
url: https://mp.weixin.qq.com/s/wIyObxYAANGLnkBrROe7Sw
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:46:49.562399
---

# 【披露】一起带有行动编号的明确印度APT迭代样本分析与家族归因...

# 【披露】一起带有行动编号的明确印度APT迭代样本分析与家族归因...

原创

问鼎安全
问鼎安全

问鼎安全应急响应中心

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/uaicQKAnia61ic6icsUvZxiaLFFTCTxWH7hCTG06D5Z7f1WGlfFUgeQ4GxFK2Jlx2xevic0nFtlObIU7WHMOniatic6n67RWvsWsx5ziaZouPNcOMbAk/640?wx_fmt=png&from=appmsg)

------免责声明------

本文内容仅供学习交流与借鉴，旨在提升安全意识、加强安全防护。请勿用于非法用途，擅自操作后果自负。如有内容存在争议或侵权请联系我们删除。感谢您的理解与支持，让我们共同维护网络安全环境。

本文涉及相关情报细节均为原创披露，非杜撰情节

# 前言

问鼎安全应急响应中心长期深耕高级威胁狩猎与政企单位一线应急响应场景，持续捕获、研判并处置多起 APT 高级持续性威胁入侵事件、定向渗透攻击及高危木马入侵案例，积累了丰富的实战化攻防与溯源取证经验。

本文以一起印度 APT 组织的真实样本事件为例，完整还原从样本分析到确定组织画像的全过程，涵盖样本细节、攻击者样本自身存在的缺陷以及 APT 行动代号等关键信息。全文干货充足、细节详实，建议收藏细读。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uaicQKAnia61ic1xmTHp52DFNzvsMaIMq0CN8VKOBK8o4JzZjEdFhpUKib3GyfYkibGzsrHDrUpdShm7L4xJQlvzkmcCb0iafPCibv0x6OyhgnB7rY/640?wx_fmt=png&from=appmsg)

【下期预告】

一场全球性印度尼西亚DDOS集团的揭秘；从测绘，挖掘到定性的全流程(涉及美国卷宗的全球六百万公网账密租赁集团)。

# APT 家族背景

| 属性 | 详细信息 |
| --- | --- |
| 组织名称 | 白象（Patchwork）/ 肚脑虫（APT-C-35） |
| 组织别名 | 摩诃草、APT-C-09、Hangover、Dropping Elephant 等 |
| 归属国家 | 印度（具有印度国家 / 政府背景） |
| 活跃时间 | 自 2009 年起持续活跃 |
| 主要攻击目标 | 东亚、巴基斯坦等国政府机构、科研教育、军事部门等关键领域，针对政府官员、科研人员、军事机构等敏感目标 |
| 攻击动机 | 网络间谍活动（情报窃取），服务于印度的地缘政治与国家安全利益 |

以上是APT家族背景。

# 样本分析

样本通过钓鱼邮件完成初始投递，此处不再赘述，下面直接进入样本本体分析。

## 3.1 样本可疑资源包

样本中明显包含一个可疑的资源节 TYPELIB，其整体内容加密存储，大概率承载配置或指令参数等关键信息。

![](https://mmbiz.qpic.cn/mmbiz_png/uaicQKAnia618TbTFXQIk1HME8biaCsQYTDdWv2UTPXBVicqkd6fGkia5tMGWwehxIREPTDv4AF6b9eeaBGZn9p9V7X20sDyuxA8EMUhYianPEriaU/640?wx_fmt=png&from=appmsg)

## 3.2 样本导入表

该样本并未采取自定义加密导入表等加载对抗措施，可直接查看导入表，关键导入项如下：

![](https://mmbiz.qpic.cn/mmbiz_png/uaicQKAnia619Eibgmj08bYQibC3yS8U7ib5eC4YYPQ3AA5iapnsVhhCx69iaUK8vx1ZGt2D2T9sSnBBplvHuy5iccGwDAFxQOCtCnFuN9vk3wmDnvg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uaicQKAnia61ibwc3ZeqHHeGBjubHatOldWC5W9s3FTQHT2EZP0ncdzZtpnlsmNq7BQLz1rknhiayC8voEmSxROoy8h6kH1dmgDPuywEo8bdG7U/640?wx_fmt=png&from=appmsg)

| 模块 | 关键 API | 用途 |
| --- | --- | --- |
| KERNEL32 | CreateProcessW/A、CreateMutexA、Sleep、GetComputerNameW、GetUserNameW | 进程执行、互斥锁、系统信息收集 |
| ADVAPI32 | RegCreateKeyExA、RegSetValueExA | 注册表持久化 |
| WS2\_32 | WSAStartup、socket 系列函数 | 网络通信 |
| WININET | InternetOpenA、HttpSendRequestA | HTTP 信标通信 |
| CRYPT32 / ADVAPI32 | CryptAcquireContextW、BCrypt\* | 加密相关 |
| SHELL32 | SHGetFolderPathA | 启动文件夹路径获取 |
| OLE32 | CoCreateInstance、CoInitializeEx | COM 接口（IShellLink 快捷方式创建） |

部分模块如上。

## 3.3 程序流程

程序启动后先解密内置配置，随后创建全局互斥体以保证单实例运行；接着判断自身是否位于安装路径，若否则复制自身、删除原文件并设置隐藏属性；最后写入三种自启动项并连接 C2。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uaicQKAnia61icCoeoictBgbpFDVSPvJr4iaan43Geib3BicZp8ZuvN7fdQ2r3jf7X6vrWjsPBowtNABbRqBpQvHPp8PAe3jsjjrr8UErFukCpB5n0/640?wx_fmt=png&from=appmsg)

若配置解密失败，程序不会退出，而是使用 localhost:443 作为默认值继续运行。

## 3.4 资源 BLOB 解密

配置密文位于资源 RT\_HTML(23)/TYPELIB 中，文件偏移 0x1353E4，共 417 字节：前 33 字节为头部，自第 34 字节起为 384 字节密文。

| 项目 | 详情 |
| --- | --- |
| 算法 | AES‑256‑ECB（自定义实现） |
| 密钥 | 32 字节硬编码 |
| 密钥来源 | 直接内嵌在函数 sub\_425590 的栈变量中 |
| 资源类型 | TYPELIB（PE 资源 type=0x17，name="TYPELIB"） |
| 资源大小 | 417 字节 |
| 数据格式 | [33 字节头部] + [AES‑256‑ECB 密文（384 字节 = 24 块 × 16）] |

完整密钥：

00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F 10 11 12 13 14 15 16 17 18 19 1A 1B 1C 1D 1E 1F

![](https://mmbiz.qpic.cn/mmbiz_png/uaicQKAnia61ibvuicK4wCxGSYlEOVsDbdfNwWvonpE1p308uQv5jXh7nkR42tZpDmdwXq3KEKJ5s1pBsqa5h2fBO8dfYTxhxA9yJRzwIAsLOXA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uaicQKAnia61ibmvDl8qgKCiaQhiaPsGRYGgBxjSVNIVWtUIjtC0YcTUJSgm0yXe3qdoNMtAvBBNsngJpluZyOyw7bmfVLqavMI1ia5O0YTqALicV8/640?wx_fmt=png&from=appmsg)

核心解密逻辑如下：

```
ResourceW = FindResourceW(0, L"TYPELIB", (LPCWSTR)0x17);if (!ResourceW)    ResourceW = FindResourceW(0, (LPCWSTR)0x409, (LPCWSTR)0x17);Resource = LoadResource(0, ResourceW);v19 = LockResource(Resource); v4 = SizeofResource(0, ResourceW); v30[0] = 0x03020100;  v30[1] = 0x07060504;v30[2] = 0x0B0A0908;  v30[3] = 0x0F0E0D0C;v31_low  = 0x1716151413121110;v31_high = 0x1F1E1D1C1B1A1918;v21 = v4 - 33; sub_401ED0(v23, v30);  for (v7 = 0; v7 < v21; v7 += 16) {    v31 = *(_OWORD *)&v19[v7 + 33];      sub_402280(&v31, v23);    }sub_4258D0();
```

## 3.5 AES-256 密钥扩展

样本进行 AES-256 密钥扩展，将 32 字节密钥扩展为 240 字节轮密钥，过程中使用 S 盒与 Rcon 表。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uaicQKAnia618k8LickDDkkOGwoW07pL1fD34N3qSNLibjBWE9aUyQRG2QK7KZSStwtlt2qm4tQovic2fmUKeXoOfwETrwjjjFmXIOqyerDx1lr4/640?wx_fmt=png&from=appmsg)

| 参数 | 值 | 说明 |
| --- | --- | --- |
| Nk（密钥字数） | 8 | 32 字节密钥 = 8 个 32 位字 |
| Nr（轮数） | 14 | AES‑256 标准 14 轮 |
| 扩展密钥大小 | 240 字节 | (Nr+1) × 16 = 15 × 16 |
| 循环次数 | 8 → 59 (0x3C) | 60 - Nk = 52 次迭代 |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uaicQKAnia61ic6naO46EfArn2V8gM3DibYvVibN5FKEPMI4S9CARnytbNp5T6beGu0PsTMTg4NmuJ5bT785xic0xuiaeibTibe7sibAhWotMib47bzibbU/640?wx_fmt=png&from=appmsg)

## 3.6 AES 解密

下面进入 AES 解密流程：按 16 字节为步长循环处理，解密结果拼接为字符串后交由配置解析函数处理。

解密流程（逆运算）：

AddRoundKey（第 14 轮密钥，偏移 a2+224 = 14×16） 循环 i = 13 → 0： InvShiftRows（字节逆行移位）

InvSubBytes（使用逆 S-Box 表）

AddRoundKey（第 i 轮密钥，偏移 a2 + 16\*i）

InvMixColumns（最后一轮除外）

![](https://mmbiz.qpic.cn/mmbiz_png/uaicQKAnia61icsPCaibqm98jh66ttOQvsD9F0zQjOazEM4N60nibBV5AWnQfn16CFic35RmbppicDuWlWHJFEv8uCkE5HcxGXawJHRLf2TkDj9q9c/640?wx_fmt=png&from=appmsg)

解密过程中还需定位以下三张表：

正向 S-Box（密钥扩展用）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uaicQKAnia61906sPtXgnfaZNOIw5ZGvFPKkwT2be8gwFZ2xeSDDhwaVgDib0gxJlqwOmWc1zCsk7NFibENYvCusst4FWu7hVHwnickcAicqu6bYU/640?wx_fmt=png&from=appmsg)

逆向 S-Box（解密用）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uaicQKAnia619Uz2tstdgddlm8KBRdAAmVBHXrTAUc7BXz3yJ2v5iaUykapC4v8eQ5iaAhOFlE92Kom88U2Joic9mWzsV8D6DHVQ4Vic8Cv91HGYM/640?wx_fmt=png&from=appmsg)

轮常数 Rcon：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uaicQKAnia618mRjuYMqDhEA0LSWFyvefJdrrSryQeDTibATvB8LicUnIfoWRdBgWJ4yRmLIpUSicXR2Bh5xy2FL7DOJzictWURaF56ibBKOLcsgx4/640?wx_fmt=png&from=appmsg)

## 3.7 配置解析器解密配置

理解上述流程后即可对配置进行解密，当前配置器字段信息如下：

| JSON 路径 | 对应用途 |
| --- | --- |
| network.domain | C2 服务器域名 |
| network.port | C2 服务器端口 |
| network.https | 是否使用 TLS（wss://） |
| network.prefix | WebSocket URL 路径前缀 |
| identity.project | 项目代号 |
| identity.contact | 联系邮箱 |
| identity.agent\_name | Agent 标识 |
| persistence.task\_name | 持久化任务名称 |
| persistence.mutex\_prefix | 互斥锁前缀 |
| persistence.startup\_method | 启动方式标志 |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uaicQKAnia618fxTbufpjkwjTx9vlKX9ks4kHib3khc9jWjy8AzmOpmRjffnzNHzQFgsreBSrHOvI7H5DyHlFicbUKAO5l5JbIXrZStIjYibTWlY/640?wx_fmt=png&from=appmsg)

直接使用解密脚本输出配置文件，脚本如下：

```
import pefilefrom Crypto.Cipher import AESAES_KEY = bytes(range(32))HEADER_SIZE = 33defextract_typelib_resource(pe_path):    pe = pefile.PE(pe_path, fast_load=True)    pe.parse_data_directories(directories=[        pefile.DIRECTORY_ENTRY['***************']    ])for entry in pe.DIRECTORY_ENTRY_RESOURCE.entries:if entry.id != 0x17: continuefor sub in entry.directory.entries:for lang in sub.directory.entries:                rva = lang.data.struct.OffsetToData                size = lang.data.struct.Sizereturn pe.get_data(rva, size)returnNonedefdecrypt_aes_256_ecb(encrypted_data):    ciphertext = encrypted_data[HEADER_SIZE:]    ciphertext = ciphertext[:len(ciphertext) - (len(ciphertext) % 16)]    cipher = AES.new(AES_KEY, AES.MODE_ECB)return cipher.decrypt(ciphertext)resource_data = extract_typelib_resource("*****.exe")plaintext = decrypt_aes_256_ecb(resource_data)config = plaintext.rstrip(b'\x00').decode('utf-8')print(config)
```

解密结果为一段 JSON，包含 C2 地址、端口、项目代号、联系人、互斥体前缀、计划任务名等字段：

```
{  "network":{    "domain":"*********.com",    "port":443,    "https":true,    "prefix":"analytics"  },  "identity":{    "project":"CTD KP",    "contact":"kpctd@gov.pk",    "process_lock":"hardcoded_lock",    "cf_uid":"SA",    "agent_name":"ShadowAgent"  },  "persistence":{    "filename":"CHANGE_THIS.exe",    "mutex_prefix":"asus_4df7009c18a879e7",    "task_name":"",    "startup_method":1,    "location":1,    "enable_app_path":true  }}
```

**ShadowAgent**木马的 C2 与持久化配置：

1. **通信配置**

   使用 wss 加密 WebSocket，C2 域名`******.com`，443 端口，URL 前缀`analytics`。
2. **身份标识**

   项目代号`CTD KP`，Agent 名称 ShadowAgent；内置硬编码进程...