---
title: CAN 协议全解：分层模型、四大帧、错误与过载机制梳理
url: https://mp.weixin.qq.com/s/LudoC7RGgiU87civ7cUgtg
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:43:31.009178
---

# CAN 协议全解：分层模型、四大帧、错误与过载机制梳理

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD39fbDicSib534iap9hyFTvFZqtYD1u6osX8RwiczwbYgvjGrE1Wuw9HnUMe72D5XPmnxk1Gg9OtOQwtoeXSR7ue2nzS238Mx0OZk/0?wx_fmt=jpeg)

# CAN 协议全解：分层模型、四大帧、错误与过载机制梳理

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAI8KMQg42koBCmQ8xCYRUVtiaem7dsJtOqV3DGOX6iaYEHyxflLz2KpKog3fHia0MOsJl0uRNIdyy32iaibZKpdT4LKv907eGCWcdA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

**01**

**CAN 协议与 OSI 七层模型的关系**

OSI（Open Systems Interconnection，开放式系统互联参考模型）是国际标准化组织（ISO）制定的一套通信分层标准。它的核心思想是：把完整的数据通信流程拆分成 7 个独立层级，每层只干自己分内的事，上下层之间仅通过标准接口交互。这样一来，不同厂商的硬件和软件只要遵守同一套分层规范，就能实现互联互通。

OSI 七层模型自上而下依次为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDD9ZabiaIeRKdXEhuWiahtHJ2fCOjsFlP6gaAK2G1xG9k7fHAib99sb0aSbbwX25RLHDk3HmhkgeRulTr8y6wUXh0xNqfBS6xyfg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBWPCfzoW3zrjDJibRJJNEGxXfJIbKWatX6EjOibNOHkPcia5jzaDiaKSwrS2KN0DbZdicCxaRTQX5WhVc8EEECG5uBNVZdWLN0ibygU/640?wx_fmt=png&from=appmsg)

根据 ISO 11898 系列标准（CAN 2.0A/B、CAN FD），CAN 协议本身仅定义了第 1 层（物理层）和第 2 层（数据链路层）。但在实际车载诊断场景中，UDS 诊断不能直接跑在裸 CAN 上，还需要在上层叠加 ISO 15765-2（DoCAN）来封装分段重组、流控等机制。因此，一套完整的 UDS on CAN 通信栈，自上而下分为如下四层：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCyqL6MLrXXHQNQLApykiaQJpokTp5Dauuiaibic0brzibXV0ZXyhJhLIvItsoydiaIpxJH6ahqbq3Edsia2dE3ddSJdXD1dicglR5oj0k/640?wx_fmt=png&from=appmsg)

**02**

**数据链路层**

数据链路层介于硬件和上层应用之间，是 CAN 协议的核心。它又进一步拆分为两个子层：MAC 子层（Media Access Control，媒介访问控制） 和 LLC 子层（Logical Link Control，逻辑链路控制）。

两个子层的分工各有侧重：

* LLC 子层：作为上层（DoCAN / 应用）与 MAC 之间的桥梁，负责帧类型发起、ID 管理、报文过滤等逻辑控制；
* MAC 子层：直接操作总线比特流，负责帧的物理组装、总线传输、自动重发等底层操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDVViaLLg1hwR8Qs8ZTgWF5gIWkCFWJgJjQGuGSGIyicqG3fjOBSuBlwKMoKK2LVwzhCULEtRahygEOpicQ5nNWicor61WslAZYFLk/640?wx_fmt=png&from=appmsg)

数据链路层的MAC和LLC子层

在日常车载诊断工作中，99% 的情况下我们看到的数据帧，就是在第 2 层干活儿的。因此，吃透数据链路层的仲裁机制、帧格式、错误处理等内容，对于打好 CAN 总线基础非常关键。

**03**

**帧的种类**

ISO 11898 定义了 4 种帧类型，外加一个用于帧间分隔的 帧间隔：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaB4iaBlicHVTicK2oQv84p948d1XVicvfXnFYkpAE62M0MWJvB2L5hq3TTtkLciaeTez5ZFkb7k6xc5XRC3EMqv9Bkbzics1zQia0HmEo/640?wx_fmt=png&from=appmsg)

其中，数据帧和遥控帧是最常打交道的两类；错误帧和过载帧由 CAN 控制器硬件自动处理，平时我们很少直接感知到它们，但理解其原理对于排查总线故障至关重要。

**04**

**标准帧与扩展帧**

CAN 2.0 规范由 Bosch 于 1991 年发布，最初规定标识符（ID）为 11 位，也就是所谓的标准帧。后来 ID 资源不够用了，Bosch 又在 CAN 2.0B 中把 ID 扩展到了 29 位，这就是扩展帧。

日常使用 Vector 等工具时，看到 Standard 就知道是标准帧，看到 Extended 就知道是扩展帧。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCWPDDm0Fj2W1ibF5sdmx3wiartILofFFiaZQNRzbPMbgrPwhjtp4RZG4KMsE8lyHKiaxRpiaNq4zY563W0HChbMZLZZcdIqB5II2j8/640?wx_fmt=png&from=appmsg)

**标准帧 ID 的范围**

标准帧 ID 范围是 0x000 ~ 0x7FF。为什么最大值不是 0xFFF？

因为 11 位二进制数的最大值 = 2¹¹ − 1 = 2047，换算为十六进制就是 0x7FF。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAVEUZGtDKtBYDloj1f6VGaFYFibXEz6WhoxGHB0gbbKBcc4m7Ka89CHQkTdGGh84rUVJ3v4AOXiaXwtlAC5zOERgPrfRVEGr1ao/640?wx_fmt=png&from=appmsg)

**为什么诊断报文都是 0x7xx 开头？**

在车载诊断中，物理寻址和功能寻址都以 0x7xx 开头，而不是 0x1xx、0x2xx、0x3xx。原因很简单：

CAN 总线的仲裁规则是——ID 越小，优先级越高。 把 0x000 ~ 0x6FF 留给更重要的业务报文（动力系统、底盘安全等），诊断报文统一使用 0x7xx 段，可以确保诊断通信不会抢占高优先级业务报文的带宽。

**05**

**帧格式详解**

数据帧和遥控帧都分别有标准格式和扩展格式两种，但它们在结构上有一些差异。下面逐一拆解。

**5.1 数据帧的标准格式与扩展格式**

数据帧由 7 个段组成：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaB7QHNEicjpyeU8JojJxZqmzevDGhelMVibVGyvRCe0IicTJ806JzESzh0iaI160jp0HmfhVPxvCF1ZTibGHhGpQ6av71cMPFpibUBns/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCsHKoX4XE3J0vicHMhKJt6HNZffiajibAPlTpVw5rdKmmUkrnbbcpfXz2RWQgWGnzZelezJYMiceROu57h8XkoPjP9UD3k4IkzyWY/640?wx_fmt=png&from=appmsg)

数据帧结构

在深入细节之前，先回顾一下上一篇学过的逻辑电平：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaA8OWAicQiaQR1ulticNWKlibcvicbkxVwybgF9Gc0iaGIiazZyxr1nJqCLGL3bNO8sibECqZSTNJqLryqiaHTFvCaibxzrzHNsgl03Gic9yM/640?wx_fmt=png&from=appmsg)

CAN 总线通过"线与"机制实现仲裁：显性电平会覆盖隐性电平。

① 帧起始（SOF，Start of Frame）

一帧的开始标志。发送方发出1 位显性电平 0，打破总线空闲状态，告诉总线上所有节点："我要开始发数据了！"

SOF 之后紧接着就是 ID 字段（标准帧 11 位，扩展帧 29 位）。

② 仲裁段

仲裁段的结构在标准帧和扩展帧中有所不同：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaC4LIiafQbj8KHhVI6cibCA6mPCxI2okQtqibEohlTa5BFYcwBRc1ID4yCqrmGjZoJxu1bHWWCMT53LQr63BSDMpSfsB6ngAPuKVM/640?wx_fmt=png&from=appmsg)

几个关键位的含义：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBKZeDC71L5b3BV50YrPWLaa0WKjGcJMlBPhIROUOE6Uucpc2ianKtvRwbkIF5WTFGqaEklmxH0chy5GaLGs4jRldp0iaEqoP4gI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAchrI3c6nuYMuDaJ0tTyvbAGPCEBktkUustU5IZiam4yibibJia1e7Fb9Q0LX4QuiaTIq3Uo1AK5HnacedjRLJHJVjQ1XicyAibK7JtQ/640?wx_fmt=png&from=appmsg)

仲裁段结构

**为什么要区分标准帧和扩展帧？**

因为标准帧和扩展帧可能共存于同一总线。节点通过 IDE 位来识别当前帧的 ID 是 11 位还是 29 位，从而正确解析后面的字段。

③ 控制段

控制段包含保留位、IDE 位（仅扩展帧需要再次出现）和 DLC。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaD7mjn75prXpSP9fedId78FCLDKLNA8rdDVGKr2qYnnkXjPA1UiaeqmH7kP6ickhc9ZQl0wD1A7Cgxu9LoV4UQkOn2Z1FRVMJ79g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCztAhvWy6uUzmEL9wNqeLA2fXvN0g3CxeW2bJr5kSKzL3rB0aYeiaQ6yciaSxkdSERlE21DjmL8L4LuDpjRBQevsHF3JpZ7AKaw/640?wx_fmt=png&from=appmsg)

控制段结构

④ 数据段（Data Field）

数据段内容长度由 DLC 决定，0 ~ 8 字节。CAN 2.0 标准帧/扩展帧最大有效载荷均为 8 字节（CAN FD 之后扩展到了最多 64 字节，后续文章再聊）。

DLC 与实际数据字节数的对应关系：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDtA73GvyvMHibdic0nFQIUgd4YlakqEpiabvcpgw23D11Adqjick3uAqYL9KVXSJajsEecLjkg8fO2Re3j13IibX9YibsqsXAnJWiajI/640?wx_fmt=png&from=appmsg)

DLC与数据字节数的对应关系

💡 DLC 的值可以超过 8（CAN FD），但在经典 CAN 中，DLC > 8 视为无效，按 8 字节处理。

数据段在标准帧和扩展帧中结构完全相同：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBIPCL5Ekia5EAyWzt0aicBUHleGLgWLWWVYmczwiblCd9YCesZHffOYpdNKDjfreib8MBtgjNFnAwfyuNGI9Zia1nibxpnRTamJVTMA/640?wx_fmt=png&from=appmsg)

数据段结构

⑤ CRC 段（Cyclic Redundancy Check）

用于校验数据传输是否出现错误。标准帧和扩展帧格式相同。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAyMiayTr7HG9X3KH4Hp1Da432kRibH3SMTxjTvr4kzyGDz8jIwfhkyjamBh5gIS23iaFGs19a3ZL9cmu6k6GbRZY8raL19Nwowico/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDU9sibmulEklwIBoFvefgvg3HsPqwGZqIMS9I9JTYpqFg9cl6HIEQIbG1r8bMLS9kOz6A2jSTkvYHS4uNgzZKsQKpxOuNhdJ6A/640?wx_fmt=png&from=appmsg)

CRC段结构

**CRC 校验算法是什么？**

CAN 协议使用的 CRC 多项式为：x¹⁵ + x¹⁴ + x¹⁰ + x⁸ + x⁷ + x⁴ + x³ + 1（CRC-15）。

发送方按位流计算 CRC 值并填入 CRC 段；接收方用同样的多项式重新计算，若结果不一致，说明数据在传输中受损，触发CRC 错误。

⑥ ACK 段（Acknowledgment，应答段）

用于确认数据是否被至少一个接收方正确接收。标准帧和扩展帧格式相同。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAB0kkL7oWKlyxc1aVzgbuDuvicTCoOedSL8pOSkoXKdoIicMhgHZspdQ5j7qzkKmb0hhyBfkKXwd0RbVOwlmjgzmPRcfCJFpMiak/640?wx_fmt=png&from=appmsg)

**ACK 的工作流程：**

1. 发送方在 ACK 槽发送隐性 1；
2. 所有接收到正确 CRC 校验的节点，会在 ACK 槽回应显性 0 拉低总线；
3. 发送方在 ACK 槽位置采样总线电平：

* ✅ 读到了 0 → 至少有一个节点正确接收，传输成功。
* ❌ 读到了 1 → 无应答（ACK Error），触发错误处理机制。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDkyv9gqIPTNYlsmZEUz3s2qibC0A0Bvam8Pra12mibLkcdJicaQE9UE2nG5jsxq3HyA6pGDonadpjdHBXiaC0RMbJdIqQXDtbcE5g/640?wx_fmt=png&from=appmsg)

模板ACK段结构

⑦ 帧结束（EOF，End of Frame）

连续发送 7 位隐性 1，标志本帧数据传输完毕。有始有终，SOF 用 0 开头，EOF 用 7 个连续的 1 收尾。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDvWpdXRhrtSZUHKZQRibSzSUibIVGutxzMicHVx6c0bTPN2E86aNh916I8KpFOWppW8bR0ibYJ1lyicUa9gzrcKKRY3hKlt0xpzjh0/640?wx_fmt=png&from=appmsg)

帧结束结构

**5.2 遥控帧的标准格式与扩展格式**

遥控帧在实际应用中极少使用，它的作用仅仅是：请求拥有相同 ID 的节点发送数据。

遥控帧的结构与数据帧几乎一致，但没有数据段，只有 6 个部分：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBavyhgXk26K5N4XTHHq9Jic2bBEl8H8xCGdAhRXYLS6FL9wFkBFANa0eFOAZKnXYHIULJicdnWtMGGDJzTDWsrcXPgFb95dy8zk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaD88uVJLKib2iaXsIJJplAJl8Wt4BIdMVJicvial1GGy6Tou6Eic5HKTQKud7FoAiaUFdAVsYjk5bTrygWpnTXYtSXK918MtwNLZKCGU/640?wx_fmt=png&from=appmsg)

遥控帧结构

最关键的区别在于仲裁段中的 RTR 位：遥控帧的 RTR = 1（隐性），而数据帧的 RTR = 0（显性）。由于显性电平会覆盖隐性电平，如果同一 ID 的数据帧和遥控帧同时发送，数据帧会因仲裁胜出而优先发送。

**5.3 数据帧 vs 遥控帧：一张表搞懂**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDdK9wrG04ggic4ibFJibmaaer0WricWQic2oVTeicGlTlF4q1WiaHw9VTdGYveFDqXJNI7FMVAu4ZtbgwtuGGGxD7KXbLFpxSXzP1T2o/640?wx_fmt=png&from=appmsg)

**06**

**错误帧**...