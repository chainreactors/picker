---
title: 一场假面试引发的入侵
url: https://mp.weixin.qq.com/s/6Aq5RXJuJZGv5K63Gg33gQ
source: Doonsec's feed
date: 2026-09-21
fetch_date: 2026-09-22T07:00:29.292455
---

# 一场假面试引发的入侵

# 一场假面试引发的入侵

blackorbird
blackorbird

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

2026年4月，一起巨额加密货币劫案震动行业。去中心化金融（DeFi）协议KelpDAO被盗走2.92亿美元，入侵的入口是跨链通信服务商LayerZero。攻击者的手法相当老练：先攻陷LayerZero，再伪造一场加密货币铸币事件，同时对验证服务器发起DDoS攻击，让被攻陷的服务器批准这次非法的铸币，巨额资产就这样被卷走。

攻击者是谁？网络安全公司SentinelOne在调查中把矛头指向TraderTraitor，一个带有朝鲜（DPRK）国家背景的Lazarus子组织，又名WaterPlum，UNC4899、PUKCHONG、Jade Sleet。这个组织在2026年全年持续针对加密货币交易实体发动攻击，经济动机非常明确。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqAQGrXuVOsWPykaGUKJAKjvbjJ2aTGSJ77MD7SicUYGlXKLWiaVL4aVMLMaLyIv8Cicic9UthmVQ5dNtNleFVYLQJBv9170hPWH7g/640?wx_fmt=png&from=appmsg)

但故事没有结束。LayerZero事件公开之后，SentinelOne顺着遥测数据又找到了另一个受害者。和之前的高调目标完全不同，这是一家与加密货币毫无关系的印度IT服务公司，规模小得多。研究团队正好借此看清一件事：当这个威胁组织入侵一家小公司，而这家公司又没能为入侵提供足够价值时，攻击会走向哪里。

# 假面试，真后门

先从钓鱼说起。这类攻击沿用了DPRK系组织惯用的「Contagious Interview（传染式面试）」套路：攻击者伪装成招聘方，主动接触目标公司的求职者。SentinelOne确认的每位受害求职者，其GitHub档案都集中在DevOps或加密货币、金融科技工程项目上。

诱饵仓库的选题也很有讲究，它们被设计成伪装公司的「基础设施工程项目」，让求职者误以为是真实的面试作业。从LayerZero事件报告中提到的gtn-candidate-repo仓库入手，研究人员又挖出了更多诱饵，其中一些指向名为Northwind和Novacart的公司。目前还不清楚这些公司是攻击者虚构的，还是他们冒用了真实公司的名义，其中一个Northwind的示例把自己描述成一家即将上线的电商公司。其他发现的仓库还包括Northwind-IAC、novacart-interview和terraform-candidate-repo。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDrYOIxW6w6qGKSibRDZFH5ib2K7QohZzibnATlL3VUdsdnQuwNXfgibMUG05iaSPfkxs3hwQxsPAGMRgjBofuicMxOvzCtKV89gwdvibE/640?wx_fmt=jpeg)

图1 武器化GitHub仓库里的面试任务，背景设定是电商公司Northwind的基础设施工程题

上面这张图就是一个典型诱饵。

任务背景是电商初创公司Northwind即将上线，团队还在手动操作AWS控制台，这显然不可持续，求职者需要用Terraform搭建一套能扛住流量峰值、安全处理数据库连接的两层架构。任务还给出了质量、安全、环境三方面的约束：模块化以利于维护、严格遵循DRY原则、在架构中贯彻安全最佳实践。乍看完全是一道正经的技术面试题，对吧？

机关藏在一个不起眼的文件里：.terraform.lock.hcl。

这是Terraform的依赖锁文件。正常项目里，它记录的是插件提供商的版本和哈希，保证构建可复现。但攻击者在这个文件里塞进了一个「自定义provider」，把来源指向自己控制的域名。SentinelOne在多个仓库里识别出三个恶意provider域名：

registry.hashicorp-aws[.]com

registry.hashicorp-aws[.]io

registry.hashicorp-terraform[.]io

这三个域名都在仿冒Terraform官方provider域名registry.terraform.io，属于典型的仿冒域名（typosquatting）。受害者一旦带着被污染的锁文件运行terraform init，Terraform就会把这个自定义provider当作真相来源，从攻击者控制的域名下载并执行恶意provider模块，代码就在你的机器上跑起来了。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDp5IuH7vbfiaV4pibd0tnRZxO2yiaKqzESVzxneJDYD9TpB6iar35BtzfkP40BrfJia1zz6cYQjPw0Z7ffFGwH17liblorF79qmbLicIQ/640?wx_fmt=jpeg)

图2 武器化锁文件，provider指向仿冒域名registry.hashicorp-aws.com下的hashicorp/awsbeta

上图是其中一个诱饵仓库里的锁文件内容，可以看到provider指向registry.hashicorp-aws.com/hashicorp/awsbeta，版本1.0.0.0，后面跟着一长串哈希值。不了解Terraform的人看到这串哈希，反而会觉得「挺正规的」，这正是迷惑性的来源。

有意思的是，开发者的安全意识确实能给这类攻击制造摩擦。在另一个仓库里，一位被面试的候选人主动留言，说自己删掉了项目锁文件里一个仿冒provider，他可能以为这是面试官在考察他的安全意识。可惜现实中，并非每个求职者都会这么做。

根据LayerZero事件报告，攻击者在员工把武器化面试项目装进公司电脑后，部署了FLATROOF和ROOFDECK这两个macOS后门，用它们收集API密钥、提升权限，进而渗透进受害者的AWS和Google Cloud环境。

# 新受害者：一家与加密货币无关的公司

SentinelOne通过自己的遥测数据，拿着LayerZero事件中观察到的后门哈希做了一次反向狩猎，找到了这个此前未知的受害者。

受害组织是一家总部在印度的IT服务提供商，与加密货币毫无关联。受影响的只有一台端点：一位DevOps工程师的Apple Silicon MacBook。这位工程师几乎每个工作日都用Terraform和Ansible操作AWS、OVH和OpenStack，机器上存放着云凭据和源代码访问权限，活脱脱一个LayerZero事件里「Developer1」的翻版。研究人员：在社交媒体上公开基础设施或DevOps身份的人，就是这类攻击的候选人，而目标的价值，取决于这台笔记本能触达什么。

# 感染时间线

根据这台主机上的遥测数据，两个后门早在3月18日就已经躺在磁盘上，投递方式已无法考证。它们一直保持休眠，直到3月29日才出现beacon和主机活动。

表1 新受害者的感染时间线

| 时间戳（UTC） | 活动 | 细节或证据 |
| --- | --- | --- |
| 2026-03-18 | FLATROOF与ROOFDECK已存在 | 按遥测数据，受害者机器上发现两个后门的哈希 |
| 2026-03-25至03-28<o:page></o:page> | 休眠阶段 | Cursor每天正常使用，未发现恶意活动 |
| 2026-03-29 05:00:41 | 打开工作区 | 开发者在Cursor里打开 ~/DevOps-Automation/cloudshield |
| 2026-03-29 05:00:46 | Shell生成 | Cursor集成终端生成登录shell（zsh -l）及Node进程 |
| 2026-03-29 05:00:53 | 首次观察到执行 | Cursor同时启动两个植入体：nohup .../SystemUpdate --type=renderer与nohup .../iSync --type=renderer |
| 2026-03-29 05:00:55 | C2连接 | SystemUpdate连向technicais（176[.]97.114.232），iSync连向hubpage（45[.]11.59.140），05:00:58出现Telegram活动 |
| 2026-03-29 05:00:58 | 植入体重置 | 对iSync执行xattr -rd com.apple.quarantine与chmod +x（Gatekeeper绕过） |
| 2026-03-30至04-19 | 稳定beacon | 以Cursor会话为门控，Cursor运行期间FLATROOF与ROOFDECK才回连，Cursor关闭即安静 |
| 2026-04-13 | GitHub诱饵 | 开发者用GitHub Desktop克隆terraform-candidate-repo |
| 2026-04-14 18:25 | 植入体重置 | FLATROOF重新武装ROOFDECK（再次去除quarantine属性、chmod +x） |
| 2026-04-20 08:48:59 | 第三阶段暂存 | ROOFDECK从85[.]137.56.10获取第三阶段loginwindow，时间在LayerZero公开声明后一天 |
| 2026-04-20 08:49:38 | 第三阶段C2连接 | loginwindow上线，连向grenight[.]com（85[.]137.56.245） |
| 2026-04-20 13:15:11 | 反取证 | loginwindow删除两个原始植入体（rm -f） |
| 2026-05-03至06-01 | 第三阶段继续 | loginwindow持续向grenight[.]com（85[.]137.56.245）beacon |
| 2026-06-01 06:08 | 最后一次观察到C2 | 已收集遥测中loginwindow的最后一次beacon |

时间线里最值得玩味的细节：植入体是3月29日被Cursor启动的，就在cloudshield工作区打开后几秒。两个后门在磁盘上躺了十几天毫无动静，直到开发者在Cursor里打开那个工作区。这种「等工作区打开才动手」的门控设计，说明攻击者在等一个合适的时机，或者说，等一台处于工作状态的机器。

表2 工作区打开后数秒内的进程创建序列

| 时间戳（UTC） | 活动类型 | 细节 |
| --- | --- | --- |
| 2026-03-29 05:00:41 | 进程创建 | Cursor Helper (node) 首次引用cloudshield工作区 |
| 2026-03-29 05:00:45 | 文件创建 | ~/.cursor/projects/...-cloudshield/terminals/1.txt（集成终端） |
| 2026-03-29 05:00:46 | 进程创建 | bash --init-file .../shellIntegration-bash.sh |
| 2026-03-29 05:00:47 | 进程创建 | zsh -l（登录shell，source ~/.zshrc与.zprofile） |
| 2026-03-29 05:00:53 | 进程创建 | Cursor（父进程launchd）→ nohup .../com.apple.iTunesCloud/SystemUpdate --type=renderer |
| 2026-03-29 05:00:53 | 进程创建 | Cursor（父进程launchd）→ nohup .../com.apple.internal.ck/iSync --type=renderer |

# macOS后门拆解

这次事件里出现了两个恶意软件家族，和LayerZero事件中描述的一致，由LayerZero和Mandiant命名为FLATROOF与ROOFDECK。两者都是ARM64架构的macOS后门（backdoor），用Rust编写。

## FLATROOF（SystemUpdate）

FLATROOF以SystemUpdate的名字部署在~/Library/com.apple.iTunesCloud/SystemUpdate，主要职责是初始数据收集，以及部署次级载荷。

启动后它做的第一件事，就是绕过Gatekeeper：用xattr -rd com.apple.quarantine去除ROOFDECK的quarantine属性，再执行chmod +x设置可执行位。这样一来，第二个植入体不需要任何签名校验，也不会弹出用户确认，就能直接运行。Gatekeeper是macOS内置的防线，本意是阻止来历不明的程序运行，而这段操作相当于亲手拆掉了这道防线。

xattr -rd com.apple.quarantine .../com.apple.internal.ck/iSync

chmod +x .../com.apple.internal.ck/iSync

FLATROOF又名macOS.Gaslight，SentinelLABS在2026年6月已发布过详细分析。这里按它支持的C2命令，简要梳理一下能力：

后门还附带一个数据收割Python模块，用内置的Telegram bot token把下列数据经Telegram外传：

·Chrome、Brave、Firefox和Safari的浏览器数据

·终端命令历史

·已安装应用列表

·ps aux获取的运行进程快照

·system\_profiler获取的系统软硬件信息

·login.keychain-db的原始拷贝

钥匙串（keychain）是macOS保存密码和证书的地方，拿到原始数据库文件，等于拿到了整台机器最值钱的密码库。

## ROOFDECK（iSync）

ROOFDECK要复杂得多，侦察和横向移动能力更强，部署在~/Library/com.apple.internal.ck/iSync。从设计上就能看出来，它定位成「站稳脚跟之后再追加部署」的工具：首次连接C2之前，需要一个预置的配置文件，里面至少包含攻击者控制的Nostr公钥。

配置文件放在~/.config/.repl\_history，用于存放C2地址、密钥，并设定beacon行为。

这里有个相当新颖的设计：Nostr寻址。

Nostr是一个去中心化通信协议，ROOFDECK首次执行时会从api.nostr[.]watch/v1/online拉取在线Nostr中继，再和自己硬编码的合法Nostr服务中继列表合并，然后在Nostr网络上按配置里的nostr\_public\_keys寻找操作者的profile，找到后读取profile的website字段，把它当作C2地址。换句话说，攻击者的C2地址不是写死的，而是「在去中心化网络上发一条公开信息，后门自己去找」。该朝鲜组织此前就使用过Nostr。

用于操作者profile发现的Nostr中继列表如下：

wss://relay.damus[.]io

wss://nos[.]lol

wss://nostr[.]mom

wss://relay.snort[.]social

wss://offchain[.]pub

wss://relay.nostr[.]band

wss://nostr.oxtr[.]dev

wss://nostr[.]wine

持久化靠的是~/Library/LaunchAgents/loginwindow.plist这个launch agent条目，应用标识符字符串是动态指定的，硬编码的--type=renderer参数则让植入体进程看起来像个正常的渲染进程，Chrome、Electron这类应用里经常出现同样的参数，很难引起注意。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDpEhZv6AibrneLNMCgic7EtaUslO6vQRWRKNDCNOQzAkib1aaG8ZpMo7ydR6U6MtAVwVfibpXsrT0hicD1VrAmgGrlmaWIpQ3cRYzHM/640?wx_fmt=jpeg)

图3 用于持久化的plist，和在运行时填入

C2端点是硬编码的/app\_version，通过HTTPS轮询命令，植入体内嵌了一张自定义的固定TLS证书。有意思的是，作者在生成证书时用了mkcert的默认元数据设置，结果暴露了自己的底细：运行环境是一台Linux QEMU虚拟机，用户名是ub。这个证书CN关联到一批域名，全部列在原文报告的IOC里。

原文地址：https://www.sentinelone.com/labs/dont-call-us-well-call-your-apis-tradertraitor-backdoors-resurface-on-victim-with-no-crypto-ties/

More👇

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqicDvERLTuy6Yo2PUS5sCSLCWBlXcichCYke51phlZqJvemVicckicq5cDX67WMuDvDmWX3HQaiaFCeKnMRuEVv2jsQCv90kc27HwE/640?wx_fmt=jpeg&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

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