---
title: 中间人代理功能上线！
url: https://mp.weixin.qq.com/s/q9C7f0zCrvwOECG58ErN-A
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T05:00:06.839832
---

# 中间人代理功能上线！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/cwEIcam01wZfoMyYfIl6lM3wJKTGdNzmIJ44yCDgFDkF3fa1KvUeuCia3s3AdvPyOOQzazRAVtIT7vB2GzibwAKVzJDqN7hLxBLkHia9x9EmjQ/0?wx_fmt=jpeg)

# 中间人代理功能上线！

朱厌安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于Venom Sec
，作者Zcentury

![](http://wx.qlogo.cn/mmhead/Iic9WLWEQMg2k8MltbFj458HmfG5bbcTw9BJcuJibGlUlIlFhOYqpqbb0Y9GVqsS8G7TPl2eDSCko/0)

**Venom Sec**
.

致命精准的红队作战兵器。模块化集成资产发现、漏扫与利用，重新定义渗透测试工作流的新一代安全平台

> "NOTE
>
> Venom 的 MITM 模块定位不是“另一个抓包页”，而是流量入口层。
>
> 它把监听、命中、改写、工作流预设和上游转发放进同一条处理链，适合承接那些已经超出“看包”范畴的前置工作，例如规则收口、签名重算、协议解包、固定字段回填，以及把处理后的流量继续转给 Burp 或其它上游链路。
>
> 它最有辨识度的地方，在于能和 `数据处理 / 加解密` 模块直接联动：先在可视化界面里拖动处理步骤，把 workflow 调通并保存成预设，再在 MITM 规则里直接引用，让自动签名、自动加解密、自动改写真正做到零代码接入。
>
> 如果日常主工作台仍然是 Burp，MITM 模块的价值也不是替代，而是把原本分散、重复、依赖人手的前置步骤固化下来。

## 界面展示

![image-20260424204937791](https://mmbiz.qpic.cn/sz_mmbiz_png/cwEIcam01wYPveFhkynAQsRNVibXWq3GllJEeSJCQPdlAFsWFJV7jXGgoWczAdFSorw9lXIEyNy8Jnjq45YXRO9NpL5L44IdVsNhgYv5icE3w/640?wx_fmt=png&from=appmsg)

![image-20260424204946130](https://mmbiz.qpic.cn/sz_mmbiz_png/cwEIcam01wbbicVJFdtO1eIt6DCtPiaXlB1wL0jj4YMxn3IrUINIHH7vVKEsXP9ao912umuYbt4oic4S2wR4nIMX8IacGbrIF92ESBuicYkzPmE/640?wx_fmt=png&from=appmsg)

![image-20260424204957307](https://mmbiz.qpic.cn/sz_mmbiz_png/cwEIcam01wb8xCiat0BejHHoNIFfAGNI94GK0yMulvG8KwG9coK4HjM71LjyiaKSjZZFzrFArJbGS03n88e6Ja3wfRW2Y4kHDjzJcboLObUkI/640?wx_fmt=png&from=appmsg)

![image-20260424205023992](https://mmbiz.qpic.cn/sz_mmbiz_png/cwEIcam01wYAJHcaPRPquZUTkNlyajKiaZWicgibhW3icKqtiaBuVmugicMmtrBc2cB6ZWMxaGLYWo9ZpNXBHKRJBIDK1CibrXduB1mfX5sJ53dTws/640?wx_fmt=png&from=appmsg)

![image-20260424205033472](https://mmbiz.qpic.cn/sz_mmbiz_png/cwEIcam01wZGIg70iaj4jmKKbGHGk8Uuiakp1ia7f8sK8kXGsodd2Of7332B4w70PZYaorbKqfMHGwyribSvOY8Eaf7EByuA0LDcjjlA5gfofbM/640?wx_fmt=png&from=appmsg)

![image-20260424205127805](https://mmbiz.qpic.cn/mmbiz_png/cwEIcam01wbicDIlrL2tiadwWLzMklNK4OUpOZYGxQ9wXu9Xvnsdtv8SI1VXakia2j6cRuyKwpLAzgftCvPCxKuxjQjqTfWkm0I3KicVTQMJTss/640?wx_fmt=png&from=appmsg)

## 使用场景

### 自动签名

很多接口并不是“抓到请求就能直接重放”。真正阻碍后续测试的，往往是请求里的动态签名、时间戳、Nonce 或经过特定顺序拼接后的摘要字段。直接在 Burp 里修改参数后再发，服务端很快就会因为签名失效而拒绝请求，后续重放、批量测试、爆破也就都卡住了。

先看直接重放失败的情况：

![image-20260424174141567](https://mmbiz.qpic.cn/mmbiz_png/cwEIcam01wYPm2ARqJeez7ib5EkujACIF9o75FgfHYiaJMicadRX7Fnecrjib3vP0Y4ic1MjokNXHxdBBZkicpxoibj3zGkTJDJQhaEicJ3Ej2lVibicI/640?wx_fmt=png&from=appmsg)

这种场景下，Venom 的处理方式不是去替代 Burp，而是把“签名如何生成”这件事前置固化下来。可以先在 `数据处理 / 加解密` 页面里把签名流程拖出来，例如从当前请求中提取关键字段、按协议要求拼接、做摘要或加密，再把结果保存成预设；随后在 MITM 的 `修改规则` 中引用这个预设，把结果自动写回 Header、Query 或 Body 中的签名字段。

配置完成后，同类请求每次经过监听器时都会自动完成签名重算，Burp 侧看到的就不再是“改一个字段就失效”的请求，而是一个仍然可继续重放、调试和验证的链路。下面是接入 Venom 后的效果：

![image-20260424175337632](https://mmbiz.qpic.cn/sz_mmbiz_png/cwEIcam01wYMA24ZrYFzeQJDL1lRALmgWKnI3a6pGqTrSjIWnpjgh4IxFehojXbAFicxlJJdBJVVvQsSyot7vHEcYC3GF05apJyypqQ8BPD0/640?wx_fmt=png&from=appmsg)

当签名逻辑被固化进 MITM 规则后，后续价值就不只是在“能重放”。对于需要高频发送同类请求的场景，例如批量枚举、验证码联调、参数遍历、口令喷洒或其它依赖重复请求的测试动作，也可以继续沿用原有工具链，而把签名重算交给 Venom 自动完成。

接着看批量测试时的效果：

![image-20260424175516616](https://mmbiz.qpic.cn/mmbiz_png/cwEIcam01wZPMWtzqlDumdCsaQPtKXPA8nk6exX7IoImO2cez5sZAnHkSvYZibicXqV5RpiauoFibicKJkhoFlHRiaJ2GsOtCNT75om4CgXUzgSmo/640?wx_fmt=png&from=appmsg)

### 加密请求响应转明文

另一类更常见的场景是：请求和响应虽然能抓到，但内容本身是密文。Burp 能看到流量，却看不到可直接分析和修改的业务数据；这时候问题不在代理链，而在业务层编码、加密或封装没有被处理。

先看 Burp 中只能看到密文时的情况：

![image-20260424204405572](https://mmbiz.qpic.cn/mmbiz_png/cwEIcam01wbtH1FpicfQXfQ9JrxFibHiahZbPicdcsT6a3PnQV8uK00JCgk5TmQQ0ff6EWeXkb95Ycbs0xR44zRoiaIJsajCUrEsjtETX6ICf6tI/640?wx_fmt=png&from=appmsg)

Venom 适合处理的正是这一层。可以先在 `数据处理 / 加解密` 页面里把解包、提取、解密、转码等步骤通过拖拽方式串起来，验证输出已经恢复为可读明文后保存为预设；再在 MITM 里分别挂到请求和响应的修改规则上。这样流量在经过监听器时，就可以自动完成“密文进、明文出”或“明文改、再加密回写”的处理。

接入 Venom 后，同一条流量在代理侧就可以被还原成更适合分析的形态：

![image-20260424204651978](https://mmbiz.qpic.cn/mmbiz_png/cwEIcam01wYPCCRmojK95ZFxIwCXWniaMhIqFLOfkql7kEe2wt1UqribZdC9952YSchkcachqykmcFYNnMd3HAGRFkpCWAf2ChcQvnYic5nlA0/640?wx_fmt=png&from=appmsg)

这类联动的意义不只是方便查看。真正有价值的是，后续调试动作可以基于明文继续进行，而不是每次手工拷贝出去单独解密、修改后再重新封装。也就是说，重放时你关注的是业务字段本身，Venom 负责把请求重新处理成目标服务可接受的格式。

下面是重放时的效果：

![image-20260424204731460](https://mmbiz.qpic.cn/mmbiz_png/cwEIcam01wYv4dnyN6WymBdJ9nf4wgeHnoK3iaoADPVORrFiaPSG6ia4Iah8kfnnGEPhAicAyKyYCdib4cgmjNn0tQXOFffIQNh2o36nN9T7Cy3A/640?wx_fmt=png&from=appmsg)

同样地，一旦“解密查看 + 修改明文 + 重新编码/加密写回”被固化成预设并接入 MITM，后续批量请求也就不再依赖人工参与。对于需要对明文字段做遍历、枚举、批量构造的场景，这一点会比单纯“看见明文”更重要。

最后看批量测试下的效果：

![image-20260424204829030](https://mmbiz.qpic.cn/mmbiz_png/cwEIcam01wbdwa9c0q7Woib3EgO7BiaMmniaxt8vwpcQvlibaWCTa7icg6yEtm8k4oSStWaGeIOqLa0TQsLQvGyC3rgTz5y7dPic3yb4WUMKiaBWYk/640?wx_fmt=png&from=appmsg)

## 模块定位

从实际使用上看，MITM 模块主要承担四类职责：

●作为统一入口承接 HTTP/HTTPS 流量

●在进入上游之前完成匹配、改写和预处理

●将可视化编排好的加解密 workflow 直接接到流量处理链上

●把处理后的流量继续转发到 Burp、远程代理或其它出口

对应地，它解决的问题也比较明确：

●哪些流量需要进入处理链

●哪些请求或响应需要被改写

●改写所需的数据从哪里取、如何拼接、是否需要预设处理

●处理完成后是否继续转发，以及转发到哪一层

## 功能结构

MITM 模块由五个页面组成：`代理流量` 、`代理监听` 、`上游代理` 、`触发器` 、`修改规则`

这五部分不是独立功能点，而是一条完整链路上的不同节点：

| 页面 | 功能 |
| --- | --- |
| `代理监听` | 承接流量入口 |
| `触发器` | 决定哪些请求进入规则处理 |
| `修改规则` | 负责具体改写逻辑 |
| `上游代理` | 决定后续转发路径 |
| `代理流量` | 提供观测面和派生入口 |

## 代理流量

`代理流量` 是观测面，也是规则配置的起点。

页面会展示已捕获流量的核心信息，并支持按监听器、方法、关键字等条件快速收敛范围。对于已经定位到的目标流量，可以直接下钻查看原始请求和响应。

更重要的是，这个页面并不只负责“看”，而是允许直接从当前流量派生后续动作：`修改此请求` 、`修改此响应` 、`创建触发器` 、`发送到加解密`

实际价值在于减少二次录入。确认目标流量之后，可以直接基于当前报文生成规则或把选中内容送入 `加解密` 分析，而不是在不同模块之间重复拷贝结构和字段路径。

## 代理监听

`代理监听` 是整个处理链的绑定层。

监听器本身定义了流量从哪里进入，也定义了进入后会套用哪些能力。一个监听器通常会绑定以下信息：

●监听地址和端口

●TLS 相关配置

●HTTP/2、长连接等连接层选项

●上游代理

●触发器

●修改规则

需要注意的是，规则是否真正生效，取决于监听器绑定关系，而不是规则本身是否存在。

可以把执行关系理解为：

1.流量进入监听器

2.按监听器绑定的触发器判断是否命中

3.命中后按顺序执行修改规则

4.处理完成后再按监听器配置决定是否转发到上游

### 证书状态

对于 HTTPS 流量，监听器页面会直接展示当前 CA 状态，包括是否存在、是否已安装、安装范围等。证书链未建立时，先解决信任问题，再排查后续命中和改写，效率会更高。

### 规则顺序

同一监听器下可以挂多条修改规则，执行顺序按列表顺序依次推进。前一条规则的输出会直接影响后一条规则的输入，因此多规则场景建议按处理阶段组织，而不是按字段零散堆叠。

## 上游代理

`上游代理` 决定 MITM 处理后的流量往哪里走。

当前支持 HTTP、HTTPS 和 SOCKS5，上游配置可以用于：

●接 Burp 做后续人工验证

●接远程代理或测试出口

●构建多层代理链

●区分不同监听器的出站路径

如果 Burp 是后续主工作台，常见链路就是：`Client -> Venom -> Burp -> Target`

在这条链路里，Venom 负责前置处理，Burp 继续承接人工验证、重放和深入调试。这个组合的关键点不在于“多串了一层”，而在于把稳定、重复、适合前置固化的步骤提前收口。

## 触发器

`触发器` 的职责只有一个：控制哪些流量进入规则处理。

它不负责是否捕获流量，而只负责是否执行后续改写。匹配条件支持`方法`、`URL 正则`、`Header`、`Body` 等维度，并提供包含与排除两种模式。

比较适合用触发器收口的场景包括：

●只处理某一组接口

●只处理带特定标记的请求

●只处理特定协议段或特定请求体特征

●将静态资源、无关域名、噪声请求排除在规则链之外

页面内置原始 HTTP 请求测试能力，建议在真正绑定到监听器之前先做一次命中验证，尤其是在正则较复杂或排除逻辑较多时。

## 修改规则

`修改规则` 是 MITM 模块最核心的执行层，也是 MITM 与 `数据处理 / 加解密` 预设真正接起来的地方。

它的处理模型不是简单替换，而是一个明确的流水线：

1.指定写回目标

2.组合输入来源

3.按顺序拼接输入

4.交给 `加解密` 预设处理

5.将结果写回目标位置

也就是说，规则层本身负责的是“把什么数据送进去、结果写到哪里”，而真正的 **加密**、**解密**、**摘要**、**编码**、**字段提取** 等逻辑，可以在 `数据处理 / 加解密` 页面通过拖拽方式提前编排好。

### 写回目标

规则支持写回到请求或响应中的多个位置，覆盖 `Header`、`Query`、`Form`、`JSON Body` 和 `Raw Body`。多目标写回适合处理同值多处落点的场景，例如签名同时存在于 `Header` 和 `Body`。

### 输入来源

输入来源可以来自固定文本，也可以来自当前流量上下文，例如 `URL 组成部分`、`Header`、`Cookie`、`Query`、`JSON 字段`、`Form 字段`或`原始 Body`。多个来源可以顺序拼接，再进入 workflow。

这种设计适合以下类型的处理：

●**签名串拼接**

●**字段重排后重新编码**

●**请求上下文参与摘要或加密**

●**响应字段抽取后回写到其它位置**

### 处理预设

这里的关键不是“规则里能选一个预设”，而是这个预设本身来自 `数据处理 / 加解密` 的可视化编排结果。

实际使用时，通常是先在加解密页面里把处理步骤拖好、顺序排好，确认预览结果正确后保存为预设；然后在 MITM 的 `处理预设` 中直接选择它，再配合 `取值与拼接` 把当前请求或响应上下文送进去。这样做有几个直接好处：

●不需要额外写脚本或插件

●签名、解密、重编码逻辑可以复用

●调试 workflow 和挂接规则是两步操作，排查更清晰

●同一套处理逻辑可以被多条规则重复引用

对于自动签名、请求体加解密、响应解包、字段重算这类场景，这一层就是 MITM 的 **核心亮点**。

### 错误处理

规则执行失败时，可按配置选择原样放行、跳过当前规则或直接阻断请求。对于测试链路，通常建议优先选择便于观察的策略；对于需要强约束的场景，再启用阻断。

## 与加解密模块联动

MITM 模块真正拉开差异的地方，不只是“能调用 workflow”，而是这套 workflow 可以完全通过可视化方式完成。

在 `数据处理 / 加解密` 页面里，可以直接拖动处理步骤，把字段提取、解密、摘要、签名、编码转换等动作串成一条链；确认结果无误后保存为预设，再回到 MITM 规则中直接引用。整个过程不需要额外写一行代码。

一条典型路径如下：

1.在 `代理流量` 中定位目标请求或响应

2.将选中内容发送到加解密模块分析

3.在 `数据处理 / 加解密` 中拖拽并调通 workflow

4.将验证完成的 workflow 保存为预设

5.在 `修改规则` 中引用该预设

6.让监听器在流量经过时自动执行

这意味着 workflow 不再只是分析工具，而是可以直接成为流量处理链的一部分。对于签名协议、字段加密、业务层编解码这类场景，价值主要体现在两点：

●调试一次，后续规则直接复用

●从人工改包切换到自动处理，不必在代理侧再写脚本

如果要概括这个联动的亮点，可以理解为：先在数据处理里把逻辑拖出来，再在 MITM 里把它挂到真实流量上。

## 常见排查点

### 看不到流量

优先检查：

●监听器是否已启动

●客户端代理是否确实指向当前监听地址

●监听地址是否覆盖目标流量来源

●请求路径是否绕过了当前代理链

### HTTPS 无法正常解密

优先检查：

●CA 是否存在且被目标客户端信任

●客户端是否已重启并重新建立连接

●目标应用是否存在证书固定或额外校验

### 规则未执行

优先检查：

●监听器是否绑定了该规则

●触...