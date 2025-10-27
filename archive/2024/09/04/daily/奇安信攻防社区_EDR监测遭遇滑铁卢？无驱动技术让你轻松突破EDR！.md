---
title: EDR监测遭遇滑铁卢？无驱动技术让你轻松突破EDR！
url: https://forum.butian.net/share/3706
source: 奇安信攻防社区
date: 2024-09-04
fetch_date: 2025-10-06T18:25:35.249826
---

# EDR监测遭遇滑铁卢？无驱动技术让你轻松突破EDR！

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### EDR监测遭遇滑铁卢？无驱动技术让你轻松突破EDR！

挑战EDR：不依赖驱动的防护瘫痪方法

\*\*从想法到现实，我的脑洞实践大冒险\*\*
====================
大家好，我是顺丰安全成文实验室的安全研究员观沧海。前不久在办公室与团队成员闲聊时，PX-0#4search突然提到：“现在的EDR监测越来越智能了，好多漏洞驱动都被拉黑了，每次尝试新手法都被秒发现。”想起之前被EDR系统“揪”出来的尴尬经历，我们“抱头哭诉”起来。
在吐槽间我突然脑洞大开：“既然驱动层面的防护这么严密，咱们何不换条路走走，试试无驱动的手法呢？说不定能给这EDR来个‘出其不意’的惊喜！”话一出口，我就像打了鸡血一样，立刻开始研究起怎么“无驱动干掉EDR的网络监测能力”。
![图片](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-7c0d2b7dcdd6ca1c5323328934edfe9034116584.jpeg)
\*\*挑战EDR：不依赖驱动的防护瘫痪方法\*\*
======================
大家可能都知道，以前要搞垮EDR，一般都得靠驱动来帮忙，比如通过调用驱动的TerminateProcessAPI强制终止EDR的进程，或者通过驱动在内核中找到驱动注册的回调函数，从注册列表中将其移除，让它在线却啥也干不了。但现在啊，随着那些漏洞驱动被拉黑，这条路是越来越难走了。
不过别担心！我这回可是找到了个新招儿——无驱动瘫痪EDR！这可是我研究了一段时间，还参考了@netero1010大神的EDRSilencer项目，然后稍微改了一下，让它更适合我们的需求。
![图片](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-27fdbd050a6029fac3360e76ef95b483360c8645.jpeg)
\*\*无驱动绕过EDR网络监测能力原理\*\*
====================
首先需要声明的是，本文的尝试是针对EDR实现流量监测的原理，做的仅局限于流量监测模块的对抗。好处是，它不再需要驱动实现，只要获取到管理员权限，即可完成。
@netero1010大神的思路非常Nice，利用WFP（Windows Filter Platform）创建若干流量过滤规则，从而阻断EDR进程对外发送的流量。
其实原理也挺简单，就是利用Windows的一个叫WFP（Windows Filter Platform）的家伙，给EDR进程设点“路障”，让它没法往外发送那些待分析的信息和日志。这样一来，EDR的防护能力就降低了，运营人员也不会收到告警（当然前提是他们没发现我们的小动作）。
\*\*01 WFP技术详解\*\*
WFP是Windows为了取代较老的各类数据包筛选技术（如传输驱动程序接口TDI、网络驱动程序接口规范NDIS）推出的开发框架，它由一组API和系统服务所组成。
从Win Server2008和Win Vista开始，防火墙Hook和Filter Hook驱动改为使用WFP技术开发。它同时支持IPv4和IPv6，可实现对数据包的过滤、修改和注入，支持对数据包和数据流的处理。WFP具备较高的灵活性，可对每个用户的每个连接、每块网卡、每个端口单独做策略。
借助WFP的API，开发人员能够实现防火墙、入侵检测系统、防病毒、网络监测的开发。WFP API分为用户模式API和内核模式API两类。
WFP主要的组件如下：
| | | |
|---|---|---|
| 核心组件 | 简单解释 | 学术定义 |
| Filter Engine（过滤引擎） | WFP的核心，处理各种协议层的过滤器 | 内核和用户模式下的网络过滤引擎 |
| Base Filtering Engine（基础过滤引擎） | WFP的服务组件 | 提供过滤器管理和调度的服务 |
| Filter（过滤器） | 指定具体的过滤规则 | 包含过滤判定条件和触发行为的具体规则 |
| Provider（提供者） | 管理多个Filter的实体 | 负责创建和管理过滤规则的实体 |
| Shim内核模式组件 | 流量信息采集器 | 支持多种协议的内核模式数据包采集组件 |
| Callouts（回调函数） | 当发现目标流量时，执行特定的操作 | 捕获流量后触发的回调函数 |
| API（应用程序接口） | 开发WFP应用的函数集 | 用于与WFP组件进行交互的一组函数和方法 |
Filter Engine（过滤引擎）
WFP的核心组件，支持多种协议层的过滤器，同时存在于内核模式和用户模式中。主要有四个功能：
1. 过滤由shim采集到的所有流量
2. 实现可供外部调用的(callout)过滤器
3. 控制shim放行或阻断流量
4. 综合考量各条策略，判断流量该放行还是阻断
Base Filtering Engine（基础过滤引擎）
WFP的服务组件，主要功能如下：
1. 接收WFP各个过滤器和相关配置的设置
2. 统计和输出当前系统的状态信息
3. 负责WFP的安全模型和权限管理
4. 连接WFP的各个模块
Filter（过滤器）
过滤的具体规则，指定过滤的判定条件、触发行为等。
Provider（提供者）
每一个具体的Filter都会归属到一个Provider，一个Provider可以管理一个或多个Filter。
Shim
内核模式组件，介于网络栈和Filter Engine之间，能够采集应用层、传输层、网络层、ICMP的流量，可处理流。根据Filter Engine的策略决定处理流量。可以将其理解为支持多种协议的流量采集器。
Callouts
当捕获到目标流量时，执行的回调函数。
API
用于开发WFP应用的一套函数集。
\*\*\\*\\*02 思路的延申\*\*
我们可以从上面的内容知道，WFP发挥流量监测效果的地方主要是各个Filter和Callout。当流量经Filter过滤，触发Callouts，执行相应的处置函数。也许是我的环境问题，使用EDRSilencer时只能封禁掉普通进程的出口流量，目标为EDR进程时会报异常。审计代码后，发现作者逆向了获取进程ID的函数，并自实现了一个同等效果的函数（这一步的原因是直接调用Windows提供的API会无法获取到杀软进程的ID， 权限不够）。于是我开始思考其他的利用方案。
如下图所示，是一台安装了Bitdefender企业版的机器内已有的Filter列表，你可以使用WFPExplorer查看：
![图片](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-143950e329463b64cf4b4e97783a08e050a803d3.png)
其中，BD和Bitdefender开头的都是EDR添加的过滤器，在捕获到对应的流量时，会执行所属的Callout函数：
![图片](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-aa8d0fa89caa83ccbbe6f4900ce704c52cd134bd.png)
那么，如果将EDR放置的所有的滤网，都从“流量管道里”拿上来，是不是就意味着所有的流量都能在这通道里出去呢？是否也如同其他访问EDR相关文件/进程一样，会因权限不足而被拒绝呢？随着研究的跟进，我发现WFP并不会对对象执行如同进程杀除一样的权限判断。只要获取到了管理员，你就拥有了对用户层WFP全部的控制能力。
若EDR厂商在实现流量监测功能时，仅通过用户层的WFP来做，则会因此而彻底失去对进程进出流量的监控能力——换言之，\*\*你的C2对于EDR而言不会有任何的对外流量，在它眼里C2的客户端只是一个在本地运行的进程\*\*，这一点，通过比对EDR的管理台日志得到了验证。
除此以外，部分EDR厂商在管理后台可以配置”禁止端口扫描“功能，如下图所示，实际上，它们也是依赖WFP实现的，可参考\*\*微软官方用例\*\*。这一功能，同样可以连带被删除。
经实际测试了国内外约8~9家的防护产品发现，没有一家针对WFP的篡改行为做了防护或监测。所有的EDR均放行了该操作，并且未有相关告警出现。同时，不像EDR进程被杀除会有守护进程重新拉起那样，\*\*EDR Agent未对自身的WFP Filter做状态监控。一经删除，直到用户重启前，都不会重新启动相关的流量监测功能。\*\*由于EDR的其他模块未受到影响，因此，EDR agent仍然在线，且有其他的正常日志传输。但管理员如果仔细审计，将会发现再也没有任何新的网络流量日志出现。在后续行动时，由于EDR视角里，C2客户端没有对外流量，在告警的行为审计上也会有不一样的策略，能有效提升行动的隐蔽性。
\*\*无驱动绕过EDR操作指南\*\*
================
删除WFP Filter主要分三个步骤：
1.类似于打开服务管理器一样，打开FWP引擎：
```php
if (FwpmEngineOpen0(NULL, RPC\_C\_AUTHN\_DEFAULT, NULL, NULL, &hEngine) != 0) {
```
2\. 获取所有的Filter：
```php
DWORD res = 0;
```
3.通过FilterID删除目标Filter：
```php
void DeleteFilter(HANDLE hEngine, std::wstring target, FWPM\_FILTER0\*\* ppFilters, UINT32 numFilter) {
```
\*\*EDR绕过前后对比，请看大屏幕\*\*
===================
想要实际对比删除前后的效果，需要满足如下条件：EDR无法捕获到注入行为的同时，能够通过网络行为抓出shellcode的执行动作。从成文实验室的武器库里挑选一个合适的注入器，并放入最基础的网络请求shellcode，以满足上述条件。
\*\*01\*\* 删除WFP前
使用比特梵德作为测试对象，成功注入并未告警：
![图片](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-49ca64dff78be9003da21557231dd33bb6f531b9.png)
触发shellcode时，会有一个网络请求bin文件的行为。比特梵德通过网络行为审计抓出了这个动作，拦截了后续的请求行为，导致C2无法上线：
![图片](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-03b971f6a8fb08f011d65a7f95f2ab19cb82e267.png)
对应的，管理台立即收到了告警：
![图片](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-7390748dc337a1cf9dbad6795010e6dc2d4e3f8f.png)
\*\*02 删除WFP后\*\*
简单列举一下当前环境内存在的Filter：
![图片](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-7de2cedc08b2b70f7ac35006923f8a1b760abd11.png)
将比特梵德所有的Filter删除：
![图片](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-ad05d7775f14a38b52fb510076631e4cd26c4267.png)
使用相同的样本注入，再触发shellcode，成功请求到bin文件并上线，且管理台没有任何告警提示。对比之前甚至二阶段shellcode都无法请求到，此操作明显降低了EDR的监测拦截能力：
![图片](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-c15dbe83e61aa3f52b7fb80079873bc91426fed9.png)
如果你想做得彻底一点，也可以像我一样，将所有的Filter一并干掉，只留下禁止删除的几个。这并不会影响用户的网络出入：
![图片](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-785dd3b8dd8e4f9a7b041b9d8839635ce90d9e90.png)
最后需要声明的是，这一项操作的目的主要是在有限的范围内以较低的成本取得较好的致盲效果。同时，也并不代表所有的EDR都能仅用该技术就能实现同等的效果。对于使用了ETW从内核监测流量行为的EDR，则无法有效致盲流量监测模块，请读者自行测试总结。
\*\*应对无驱动绕EDR的防御策略\*\*
==================
可参考如下防护手段：
1. 间歇检查Filter过滤状态
2. 监测相关API调用
3. 补充内核ETW监测流量的功能
\*\*参考文献\*\*
========
> <https://learn.microsoft.com/zh-cn/windows/win32/fwp/windows-filtering-platform-start-page>
>
> <https://github.com/netero1010/EDRSilencer>
- - - - - -

* 发表于 2024-09-03 10:00:01
* 阅读 ( 4585 )
* 分类：[其他](https://forum.butian.net/community/other1)

3 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![顺丰安全应急响应中心](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/b152e4065ac7a08ae7cf4043afb288ed4289ff5.jpg)](https://forum.butian.net/people/13240)

[顺丰安全应急响应中心](https://forum.butian.net/people/13240)

4 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2023 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

×

#### 发送私信

请先 [登录](https://forum.butian.net/login) 后发送私信

×

#### 举报此文章

垃圾广告信息：
广告、推广、测试等内容

违规内容：
色情、暴力、血腥、敏感信息等内容

不友善内容：
人身攻击、挑衅辱骂、恶意行为

其他原因：
请补充说明

举报原因:

取消
举报

×

#### ![顺丰安全应急响应中心](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/b152e4065ac7a08ae7cf4043afb288ed4289ff5.jpg)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![]()

---