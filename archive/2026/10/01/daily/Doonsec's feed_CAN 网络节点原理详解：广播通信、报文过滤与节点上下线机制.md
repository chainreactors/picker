---
title: CAN 网络节点原理详解：广播通信、报文过滤与节点上下线机制
url: https://mp.weixin.qq.com/s/BHY210DbUNBF_MvwjfSYTg
source: Doonsec's feed
date: 2026-10-01
fetch_date: 2026-10-02T07:44:03.344475
---

# CAN 网络节点原理详解：广播通信、报文过滤与节点上下线机制

# CAN 网络节点原理详解：广播通信、报文过滤与节点上下线机制

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBvgQxffuoSxCK5zHBjMe1zHgWJ84eiapLGn9OJxaSDIkr7ZxqlZePY6F37BhEGKickoLHqodK770FzBXHPlIuxyHCSicGTiaF5FP4/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247580896&idx=1&sn=36a65f68d014c79310fdeb0e1e55b6b0&scene=21#wechat_redirect)

首先，在Can网络中，每个ECU相当于一个Can的网络节点，如果ECU有多个核，那就可能存在多个节点。Can通信是基于高低电平两条线传输数据，如果节点在这组高低电平线上，就归属于这个网络。在一个Can网络中的所有节点通信速度是相同的，不同网络通信速度可以不同。在一组Can网络中，各个节点通过Can报文进行通信，首先，Can报文是通过广播的形式在总线上传输到各个节点，这帧传输的数据包含了源地址的节点地址，通过解析Can报文的ID字段获取。也就是说所有节点都是通过分析接收和发送的报文，来判断自己和其他ECU在网络中的地址，可以联想到手机的电话通讯，我拨打号码给我的朋友，我知道我要拨打的号码，肯定是我的朋友，我的朋友看见打过来的电话号码可以确定是我打过去的，但是我们互不知道我们现在的地理位置。

第二，在广播的条件下，各个ECU节点都会收到这帧报文，但是ECU在内部通过寄存器配置Can Controller的MailBox（MessageRAM），会确定哪些Can报文可以通过各个ECU控制器的MailBox的筛选机制（Filter），也就是说，虽然源节点广播了报文到所有节点，但是因为其他ECU都配有筛选机制，导致其他节点只会回收自己想要的报文，其他报文都会拒掉，比较类似与手机中的黑白名单。

第三，如果在一个原本稳定的Can网络中，新加入一个Can节点，一般情况下，只要新节点ID与网络中的其他节点不冲突，就可以正常加入，但考虑到网络安全，比如某个黑客把自己伪装成给车辆转向发送信号的节点，并且把原本应该给车辆转向发送信号的节点给破坏了，那么此刻，黑客就接管了车辆的安全驾驶。所以可以通过Can Transceiver TJA1145，对收到其他节点加入请求后，实施节点身份合法性验证，消息过滤和异常检测。

**什么是CAN的网络节点**

网络节点是指连接到CAN总线上的设备或模块，每个网络节点都具有唯一的标识符，称为节点ID，用于在CAN总线上进行通信和识别。在一个MCU 中，CAN通道的数量决定了它支持的CAN节点数量。每个CAN通道相当于一个独立的CAN控制器，可以与一个CAN节点进行通信。

各个单元通过 CAN 总线连接在一起，每个单元都是独立的 CAN 节点。同一个 CAN 网络中所有单元的通信速度必须一致，不同的网络之间通信速度可以不同。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8tYvQba1WnSnaVWTgIOE3HhvQjrAE9N7YjKFvBxpqCERWFZXVTcJURM1RQPWA07lS3YaeI8Qde1Q/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8tYvQba1WnSnaVWTgIOE3HUrpckWEC4fsFRbUicMSm0MwOmgXYURdFePElyv1DFKibsMlmvxEa3TLw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

**如何判断CAN的网络节点是多少？**

可以根据DBC来定义查看。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8tYvQba1WnSnaVWTgIOE3Hfvz7BbZ5LtuenXehJTdb3icKIQTticeXvhyJGricuRreIe8LhRibXoL3Vg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8tYvQba1WnSnaVWTgIOE3H7rIR77DCCiaL6QXGvZ1R5LsWeTaGQRmmLAozVIxnRLP2WWCicxX2Yu6Q/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

以ADCU为例，域控作为主节点，一般外部的像雷达，camera的数据都是向域控发送的，0x26节点向0x40节点发送报文。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8tYvQba1WnSnaVWTgIOE3Hxq2GBbgEnkNTI23Uw6fLXtwnn3R8JHmk4FgnaJoJlZd3mU4OntemVg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8tYvQba1WnSnaVWTgIOE3Hyy67Ik2fQGRtcL5Lxb9e05Huic0KCA8icp4OPJmbCpyDvMEtWlJlG4lg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

**MCU如何检测和识别CAN网络中有哪些节点?**

**在CAN网络中，每个节点都可以发送和接收消息，但是并没有一个直接的方法让MCU知道网络中有哪些节点。这是因为CAN网络是一种多主机系统，每个节点都可以同时发送和接收数据。**

有一些间接的方法可以帮助MCU了解网络中的节点：

* 通过消息交换：如果一个节点在网络上发送了消息，那么其他的节点就可以通过接收这个消息来知道发送节点的存在。这种方法需要节点定期发送消息，或者在加入网络时发送一条特殊的消息。
* 通过网络管理：在某些CAN网络中，可能会有一个网络管理协议，这个协议可以用来发现和监控网络中的节点。例如，AUTOSAR CAN网络管理就是一种无中心式的网络管理，网络中的每个节点都依赖于自己和别人的网络管理报文（NM PDU）来实现通信的睡眠和唤醒。
* 通过错误管理：当网络中的一个节点出现错误时，它会发送一个错误标志。其他节点可以通过接收这个错误标志来知道出错节点的存在。

MCU可以通过监听CAN总线上的报文来检测网络中的活动节点。当其他节点发送报文时，MCU可以接收到报文并解析其中的节点ID。根据CAN 2.0A和CAN 2.0B标准，CAN网络支持最多 1 至 2047 个节点。对于CAN 2.0A，节点ID为 0 至 127。对于CAN 2.0B，节点ID为 0 至 2047。

发送节点探测报文：MCU可以发送特定的节点探测报文来主动探测网络中的其他节点。探测报文可以包含特定的节点ID或标识符，其他节点可以对这些报文进行回应。通过接收到的回应报文，MCU可以确定哪些节点是活动的。

* 通过读取CAN消息中的节点ID字段，您可以确定消息来自哪个节点。
* 对于11位标识符（CAN 2.0A），前5位通常用于设备类型和网络地址，后6位用于节点ID。
* 对于29位标识符（CAN 2.0B），前11位通常用于设备类型和网络地址，后18位用于节点ID。通过解析标识符字段的后18位，您可以确定CAN消息是来自哪个节点。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8tYvQba1WnSnaVWTgIOE3H6cHyibYC5gzfqicXJpQWYIn3iafSibKKB18rJrNgTQFX1WtricViaiaePJ4UA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8tYvQba1WnSnaVWTgIOE3HLNqhHEIbcPSyjcmlXVfFYcdFm3aWlGRqp0FECFhoOjw3EQViaAF4yAg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8tYvQba1WnSnaVWTgIOE3HQk9rBkgch3KY8stpLJmbT3d0fmawhic9IiccDOEU6SHPoGEM7FXaM0Eg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8tYvQba1WnSnaVWTgIOE3HYDI6Vt6YSU0sZLzC5fUba1Wx6WI24sd0TTyQN1iaoDk9ty9IMKNUrkw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

* 广播的can报文，可以发到所有的can网络节点，但是通过can控制器的MailBox机制筛选出想要的报文。除此之外，Can\_Trcv可以用于过滤特定类型的报文，配置为仅接收特定标识符的CAN报文。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8tYvQba1WnSnaVWTgIOE3HBRZ3kLszYiaUmt2rfPGDab8nxgZ3sicRX2UGtnTaSvzaDwO5QftXfDxw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)

**如何通过广播发送CAN报文到对应的节点，对应的节点如何收到自己想要的报文？**

广播类型的总线意味着所有节点都可以侦听到所有传输的报文，无法将报文一对一发送给指定节点。所有节点都将始终捕获所有报文。但是，CAN硬件能够提供本地过滤功能，让每个节点对报文有选择性地做出响应。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8tYvQba1WnSnaVWTgIOE3HXxymZjnMDTlZNcdgBnGuiaYZFHzaz1ficsLnibRW73e4moK2icWC0jmOcg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=11)

**CAN的筛选机制：**

消息 RAM 实现了过滤器、接收 FIFO、接收 buffer、 发送事件 FIFO 和发送 buffer。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8tYvQba1WnSnaVWTgIOE3HP6zoiajU9Ahia85SxsRdxI7XNm2UHmGhVLF8t6u6oxdIEzajjI9ibECiag/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=12)

通过配置寄存器，确定接收过滤器用于定义节点接收哪些报文，过滤器的定义是通过设置报文标识符（ID）参数来实现的还有屏蔽寄存器（Mask Registers），可以与AUTOSAR中的Basic Can一起用。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8tYvQba1WnSnaVWTgIOE3HvOq3lehU9yGGRvOIRzCib3IUYMqElvkaZhUib9jCcdFXufBBaKJ9NWQQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=13)

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8tYvQba1WnSnaVWTgIOE3HBaN9bncEKowINyt2NjhtRFbUl6Ea3APsoFYXrhj8kib9iaAWBdibDAztw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=14)

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8tYvQba1WnSnaVWTgIOE3HnMBvo95sG5r18cAGcIoJWEydlPbEo6DRrzwbNiczyAJCzGKpp0IcRHA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=15)

**如何确保网络中的节点能够正确地加入和离开网络？**

**节点插入CAN网络的过程：**

* 加入网络：节点会发送加入网络的请求或广播消息，通知其他节点它的存在并请求加入网络。节点的加入请求可能会包含节点ID和其他必要的信息。
* 网络确认：其他节点收到加入请求后，会验证节点的身份和合法性。如果节点ID与网络中的其他节点不冲突，并且节点满足网络的要求和策略，则可以接受该节点的加入请求。
* 网络配置：一旦节点成功加入CAN网络，它可能会接收到网络的配置信息，包括通信参数（如波特率）和过滤器设置等。节点需要根据配置信息进行相应的参数设置。

**节点拔出CAN网络的过程：**

* 离开网络：节点发送离开网络的通知或广播消息，通知其他节点它即将离开网络。该消息可能包含节点ID或其他标识。
* 网络确认：其他节点收到离开通知后，会从网络中移除该节点的信息。其他节点可能会相应地调整网络配置和拓扑结构。

来源：汽车电子嵌入

原文链接：https://blog.csdn.net/xiandang8023/article/details/137838100

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAI8KMQg42koBCmQ8xCYRUVtiaem7dsJtOqV3DGOX6iaYEHyxflLz2KpKog3fHia0MOsJl0uRNIdyy32iaibZKpdT4LKv907eGCWcdA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaA7BGa1vwHmHNlluBv83nX42cOwngUmsgRicQ6oyhxN3HmOsFIml2sUM8Yibk5GELQqiaFLt2dVzmf01r90xrW0vMWGpJX7zOsmkM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247575659&idx=3&sn=1b3acb3a33e0fc992b67b37bc4d04a0e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBvgQxffuoSxCK5zHBjMe1zHgWJ84eiapLGn9OJxaSDIkr7ZxqlZePY6F37BhEGKickoLHqodK770FzBXHPlIuxyHCSicGTiaF5FP4/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247580896&idx=1&sn=36a65f68d014c79310fdeb0e1e55b6b0&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkP4bDWQkLJvELA6L8vJsCRctQMTiasyhKEkb1ujgIjlGBVx91jbsQ29g/640?wx_fmt=jpeg&from=appmsg)](https:...