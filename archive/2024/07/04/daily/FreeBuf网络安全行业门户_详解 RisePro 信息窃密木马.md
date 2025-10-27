---
title: 详解 RisePro 信息窃密木马
url: https://www.freebuf.com/articles/network/405109.html
source: FreeBuf网络安全行业门户
date: 2024-07-04
fetch_date: 2025-10-06T17:43:50.302116
---

# 详解 RisePro 信息窃密木马

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

详解 RisePro 信息窃密木马

* ![]()
* 关注

* [基础安全](https://www.freebuf.com/articles/network)

详解 RisePro 信息窃密木马

2024-07-03 16:26:29

RisePro 是一种窃密木马，以恶意软件即服务（MaaS）的模式在地下论坛出售。该恶意软件家族最早在 2022 年被发现，近期攻击行为快速增长。

RisePro 不依赖特定的感染媒介，可以通过多种方式植入失陷主机，通常使用恶意链接和其他诱饵获得立足点。曾经 RisePro 与 PrivateLoader 联合投递，通过 PrivateLoader 将 RisePro 投递到失陷主机。研究人员发现 RisePro 与 PrivateLoader 共享大量代码，这表明两者之间存在联系。

一旦在系统上站稳脚跟，RisePro 就会检查系统是否有互联网连接，然后与 C&C 服务器通信。RisePro 也可以对受害者的系统进行指纹识别，窃取数据并回传。尽管目前没有明确的攻击者归属，但根据控制面板与活跃情况来看，开发人员应该是讲俄语的。

## 技术分析

### 感染媒介

RisePro 采用订阅模式，因此初始感染媒介千差万别，完全取决于运营人员。RisePro 的运营人员向开发恶意软件的攻击者支付许可费，运营人员就可以自由地生成二进制文件，按照自己的意愿和需求进行定制化构建。

RisePro 经常使用欺骗手段来辅助投递，将自己伪装成合法软件的破解版。例如，2024 年 3 月，RisePro 的变种利用 GitHub 部署伪装成合法软件的恶意软件。

根据 3 月初的统计数据，RedLine、Vidar 和 Raccoon 是使用最广泛的窃密木马。仅 RedLine 在 2023 年 10 月到 2024 年 3 月的半年间就泄露了超过 1.7 亿个密码。被窃取的账户还可以进一步被用于其他恶意活动，甚至是传播勒索软件。

### 分析

RisePro 通过构建工具来为使用者提供灵活性与定制化。攻击者可以指定可执行文件的类型、构建名称，甚至是用于 C&C 通信的 IP 地址。RisePro 还原生支持如下功能：

* 反调试
* 反虚拟机
* 禁用 Windows Defender

执行后，RisePro 复制自身作为持久化方式。通常，RisePro 会将自身放置在如下位置：

* %AppData%\Local\Temp
* %ProgramData%\

如果攻击者开启了持久化配置，RisePro 会通过 schtasks(.)exe 创建计划任务，登录时与每小时都会执行。

* C:\Windows\SysWOW64\schtasks.exe：schtasks /create /f /RU "Admin" /tr "C:\ProgramData[RisePro].exe" /tn "%RisePro% HR" /sc HOURLY /rl HIGHEST
* C:\Windows\SysWOW64\schtasks.exe schtasks /create /f /RU "Admin" /tr "C:\ProgramData[RisePro].exe" /tn "%RisePro% LG" /sc ONLOGON /rl HIGHEST

成功入侵后 RisePro 会进行一系列检查，查看设备是否处在隔离或者虚拟化的环境中。为此，恶意软件查了多个 IP 位置服务信息提供商：

* ipinfo(.)io
* db-ip(.)com
* maxmind(.)com

这不仅可以确定恶意软件是否在分析环境中，也能够收集到受害者的相关信息。RisePro 也支持根据受害者的所在地区，在不同条件下运行。

![1719994920_66850a284abab6f4252d0.png!small?1719994920680](https://image.3001.net/images/20240703/1719994920_66850a284abab6f4252d0.png!small?1719994920680)

典型通信模式

### 通信

此前，RisePro 通过替换密码和异或加密的方式进行 HTTP 通信。2023 年底，RisePro 已经过渡到使用 TCP 自定义协议进行通信。2024 年 3 月，在野发现的基本都是 1.6 版本的 RisePro。不过，1.0 版本与 1.6 版本的 RisePro 通信方式基本没有差别。

2024 年 6 月，RisePro 升级到 2.0 版本。尽管 RisePro 仍然使用 TCP 进行通信，也使用与 1.6 版本相同的替换密码，但不同的 TCP 端口会使用不同的异或加密逻辑。

C&C 服务器回传给 RisePro 命令，包含攻击者希望从失陷主机窃取的信息。配置中的大多数选项都可以启用/禁用，攻击者可以按照自己的需要和喜好进行定制化。

![1719994940_66850a3ca796260b8b271.png!small?1719994941365](https://image.3001.net/images/20240703/1719994940_66850a3ca796260b8b271.png!small?1719994941365)

C&C 通信

### 信息窃取

RisePro 主要是进行窃密的，C&C 服务器下发了窃密目标，恶意软件就会进行窃密。除了 C&C 信道，恶意软件还可以通过 Telegram 将窃取的信息回传。

![1719994961_66850a512661cad437e8a.png!small?1719994961627](https://image.3001.net/images/20240703/1719994961_66850a512661cad437e8a.png!small?1719994961627)

配置选项

在确认执行命令时，恶意软件也会发送 Loader 配置。该配置是恶意软件的另一个功能，也可以充当恶意软件下载器。启用后，RisePro 则可以根据攻击者的部署下载其他恶意软件。

![1719994979_66850a633d02baf6a8dcc.png!small?1719994979674](https://image.3001.net/images/20240703/1719994979_66850a633d02baf6a8dcc.png!small?1719994979674)

Loader 配置

RisePro 通过其自定义的 TCP 协议进行 C&C 通信，窃取数据以 base64 编码的 zip 文件形式回传，文件内容取决于配置设置于失陷主机上的具体信息。

![1719994990_66850a6e58525f52260df.png!small?1719994990840](https://image.3001.net/images/20240703/1719994990_66850a6e58525f52260df.png!small?1719994990840)

攻击方式

可以确认复现的文件是：

* information.txt
* password.txt

information.txt 中主要是指纹识别信息，包括：

![1719995003_66850a7b5a3d713407f89.png!small?1719995003913](https://image.3001.net/images/20240703/1719995003_66850a7b5a3d713407f89.png!small?1719995003913)

指纹信息

passwords.txt 中存储发现的所有账户与密码，如下所示：

![1719995024_66850a9097304af5b5d24.png!small?1719995025219](https://image.3001.net/images/20240703/1719995024_66850a9097304af5b5d24.png!small?1719995025219)

释放的文件

### 归因

RisePro 经常通过暗网在地下论坛上推广，也以恶意软件即服务（MaaS）而闻名。但根据恶意软件与控制面板的设计，研究人员高度确信开发者是俄语使用者。目前为止，尚未能够确认任何攻击者与 RisePro 存在直接关联。

RisePro 通过恶意软件即服务（MaaS）使得付费订阅的攻击者都可以将恶意软件武器化，在全球进行各种攻击。

![1719995041_66850aa14a2fe5373f2a1.png!small?1719995041706](https://image.3001.net/images/20240703/1719995041_66850aa14a2fe5373f2a1.png!small?1719995041706)

旧版本的构建工具

### 攻击目标

RisePro 的受害者不是特定的，不同的运营人员的攻击倾向也不相同。只要付费的攻击者都可以自行定制 RisePro 恶意软件，因此攻击形式也千变万化。

此前 RisePro 与其他商业恶意软件勾结在一起，现在 RisePro 也仍是如此。攻击形式多种多样，投递的方式也不局限于特定。

## 结论

RisePro 采用了复杂的技术，对个人与组织都构成巨大风险。RisePro 的演变凸显了网络安全形势的不断演变，也显示出安全防御的必要性。

## IOC

```
2229327fa653ffd07f11773ee22eb00e580b6824ce122a1e788f19859aa9dca2
5e1a1b2e2c20bc50b54e02393fa6f26a2b8c2f4d87f2abdecaca73472b5c5dba
a36d5e790ca17fb6f70884942d868d29c6854054f2db79ed8f4e2d0d16ef1647
4f0e839393df72db99a05ade0848979ff375399b104e59a7cc3847d746c17e5c
56108c707fcaf87b2220c081db115171ff35811946b3ad2d76105715e8530fbe
b4ad80860c773c79c946c3a4df13e534153bd17ceebad6acedac3156dfe0144c
77e97faca59d8de34ddc7272791efac41da9ff5b7b175a99e09a255e2701d725
a78513831b47f4b35ee9063aa167bf5d05c61559b2ac7f8fb93fa966a36e34d2
30baf54d50379893b23b24203611da331d436dfc35f2d0a805bac4da0d310489
c48eb226b641b382fd4155f10c96aacc585c6e65814865cd762e88b8a5cffd14
6b82e6f228cbb8143b68e1739f3d083cf6ab0ba9c202ce1ec769bb12c9030619
5719a862d5a32ec56328f8e066a83b6b0577a6965074ca671d0cecce681d5f79
9d540839e75daf4f31eb36271fef6eb16a913446384d07e4d8dbb2602f18bf0f
15dfbd2df433c9725239d6602bdfc56d00db62f88a1769a534d98cad50536c27
c7a40fb4aa017a0d17b535c1857d51f95b7ed8684a1ea860294bf5d897667839
6113bc3f3f972393acff5022f5ba95fb96c3d9038386ada49ccf244fa5f885fa
ce930238a02a55d7b6f13fdf9b3306de61c5c25513ed396c7e9a8dbd4c45dbd9
19c98cba0d8037a36b00d2c11cc24d25e1f388ba5093a4b6e9017508371fb34b
d2cbb7a5ef2ecdf7c6f8c965df5886a18ea0e630009cdedb3692ed1b8c77b487
078b3f37483cfc697fbd67120311e6109843804f5cae9c46f04fa1b51ba7120a
d435d7cf9077533a7c23129a8d7462e7596505e3990664dd5888fce40652bb14
d7c3c01d62fb59e186b2256894fb089c01e1aeda5dbd86a3004f1857a13313ad
0d5bb8b8da18abd1f3934103c501abf9b9cd3a6e1656853359a568dca3229765
cb21be437c800875400a94b2442bbe02ccaf31ee49e1f440aac378fc2b0b756d
f87dd2b6a63e850b6c2128ec139c6334b572b1c80698fcc30de6f39ffc788f4f
5[.]42[.]92[.]73:8081
185[.]196[.]9[.]38:8081
147[.]45[.]47[.]116:8081
101[.]99[.]92[.]169:8081
147[.45[.]47[.]80:8081
37[.]120[.]237[.]196:8081
95[.]216[.]41[.]236:8081
185[.]221[.]198[.]67:8081
194[.]33[.]191[.]159:8081
94[.]156[.]8[.]188:8081
ipinfo(.)io
db-ip(.)com
maxmind(.)com
hxxp://185[.]215[.]113[.]46/mine/plaza[.]exe
hxxp://185[.]215[.]113[.]46/cost/ladas[.]exe
hxxp://77[.]91[.]77[.]81/cost/go[.]exe
hxxp://77[.]91[.]77[.]81/cost/lenin[.]exe
hxxp://77[.]91[.]77[.]81/mine/amadka[.]exe
```

## Yara

```
import "pe"
import "math"
import "hash"

rule Mal_Infostealer_RisePro_v1.6

{
    meta:
    description = "Detects RisePro v1.6 Infostealer"
    author = "BlackBerry Threat Research"
    date = "2024-03-20"
    license = "This Yara rule is provided under the Apache License 2.0 (https://www.apache.org/licenses/LICENSE-2.0) and open to any user or
organization, as long as you use it under this license and ensure originator credit in any derivative to The BlackBerry Research & Intelligence Team"
    strings:

        $s0 = {3231F531F52DF52DF5CBCBA57DFD7DCBCBCB363231312E312DF5F52DF5CB09AF08D4080908090909F5CBCBCB59FD7DCBCBCB
82F6D4080809090809090DCB82F6AFAFAFAFAF08D4090DCBCBCB59FD81CBCBCB86B3AFAFAFAF08AFD409F5CB09F6AF0EAF0EAF0AAF0931
CBCBCB7DFD7DCBCBCB09D1AF0AAF0EAF0AAF0832CF86D1B3AFAFAFAFAFAF0832CBCBCB59FD81CBCBCB86F6D1F6AFAFAFAFAFD431CC09F
FF60AF60AB30AAF}

        $s1 = {565AEAEAEAEA565AEAEAEAB2BEAEAEA56445AEAEAEA56445AEAEAEB2BA}

        $s2 = {4321FFD9F4FFFFE1733AFFCF6630F...