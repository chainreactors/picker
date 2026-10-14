---
title: 硬件钱包里被人偷装了后门：一亿美元加密资产是怎么被卷走的
url: https://mp.weixin.qq.com/s/z2-HejrvLMxO221FmGBeMw
source: Doonsec's feed
date: 2026-10-13
fetch_date: 2026-10-14T06:50:25.483880
---

# 硬件钱包里被人偷装了后门：一亿美元加密资产是怎么被卷走的

# 硬件钱包里被人偷装了后门：一亿美元加密资产是怎么被卷走的

原创

blackorbird
blackorbird

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 从东南亚路边店到欧洲连锁卖场，这条供应链上到底出了什么事

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrj3B4FQyIe7zmINIUzXQfE2PerwJC2tdJPicuIV6pr1W9fdXTmVZ29RthrGvoKG48kgwzTxleQmgIo2925jeLydznCUVmqPGzo/640?wx_fmt=png)

一台被拆解的Ledger Nano X，右下角那块额外的绿色小电路板就是植入的后门模块，附带铜线圈天线和被替换下来的电池

上周，加密货币硬件钱包厂商Ledger向外界确认，在东南亚销售的一批设备里被人动了硬件手脚，攻击者借此悄悄提取了约一亿美元的加密资产。被盗的钱包来自马来西亚授权经销商CryptoBilis，区块链调查公司Bitquery追踪到大约315个地址与这批被污染的设备关联，涉及Bitcoin、Ethereum、Tron等多种币种。消息传开后，欧洲用户也在德国MediaMarkt连锁店买到了带后门的设备，问题不再是某个小卖家的个例。

这件事最让人不安的地方在于，被动手脚的不是软件，而是硬件本身。你买到的那个像U盘一样的小设备，看起来和正品一模一样，开机流程也完全正常，但里面多了一块不该存在的电路板，正在你输入助记词的那一刻把你的私钥悄悄发回给几千公里外的人。

# 先说清楚：硬件钱包到底在保护什么

普通用户用交易所App管理加密资产，私钥存在交易所服务器上，你只是个记账数字。硬件钱包（hardware wallet）的思路是把私钥离线存进一个专门的芯片里，联网操作时签名在设备内部完成，外部电脑碰不到密钥本体。Ledger是这个品类里出货量最大的品牌之一，产品包括Nano X、Flex、Stax等型号，造型小巧，主打离线保管。

首次使用设备时，会生成一组随机的恢复助记词（recovery seed phrase），通常是24个英文单词。这组单词就是你所有加密资产的终极密码，抄在纸上、离线收好，哪怕设备丢了坏了，拿这组词就能在任何同类钱包里恢复资产。也正因为这组词等价于资产本身，窃取它就是攻击者的终极目标。

# 后门是怎么工作的

硬件安全专家Joe Grand最早在今年3月拆穿了这套装置。他收到一台从泰国网购渠道流出来的Nano X，拆开后发现里面多了一整块额外电路板，附带天线、LTE模块和一张eSIM卡。这套东西的目的非常单纯：在设备生成助记词的瞬间，把显示在屏幕上的每一个字符抄走。

具体流程是这样的：用户初始化设备时，Ledger屏幕会逐字显示那24个英文单词，让用户对照抄写。正常情况下这些字符只在屏幕上闪过，设备内部芯片处理完就结束了。但被植入后门的设备里，那块额外电路板直接并联在屏幕的信号走线上，屏幕显示什么，它就记录什么。等助记词完整生成，它通过LTE模块和eSIM连到附近的基站，把这组单词打包发给攻击者控制的服务器。整个过程不需要用户连电脑，不需要用户装任何App，设备外表没有任何异常提示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpc7UlVTI8cqMq87U5VlRKibEnhibARha6t3TRXc5HAyoqmicdVlmAU1GbFZWIEtXMX6piciboC1FCftsGicXwPrQvRSfSmoiaFbciciaYM/640?wx_fmt=png)

Joe Grand分析的第一代植入物，黄色外壳内可以看到飞线手工焊接的细铜线，直接搭接在原厂屏幕走线上

# 后门也在升级迭代

Grand最早发现的版本手法相当粗糙，一堆手工焊上去的飞线明晃晃地露在壳里，任何愿意拆开外壳的人都能一眼看到。他当时从东南亚电商平台Lazada上买了八台设备送检，其中四台被植入了同类装置，卖家都是泰国发货的小店。3月4日他把发现正式通报给Ledger，对方在Zoom会议上表示会调查，但之后几个月没有任何下文。

事情在九十月份起了变化。前Mt.Gox首席执行官、法国人Mark Karpelès自己买了两台Ledger送检，发现植入物已经进化到第二代。这一代不再用裸露的飞线，而是做了一块橙色半透明的柔性电路板（flex PCB），平整贴合在原厂主板上方，关键焊点用导电胶固定。为了腾出空间，攻击者还把原厂电池换成了容量更小的型号。根据板上丝印日期判断，这一批至少是2025年12月之后才组装出来的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDoCP7NWTgQYRw3WvP3SD5FSp0y0ficIbLEgIBF7dedx7dkTftHF7vkQP2QhHJXgFtd5YEOQxMY56Q2NziaVNnc54icSx8K7OrsoII/640?wx_fmt=png)

Karpelès发现的第二代植入物，橙色半透明柔性电路覆在绿色原厂板上，下方是被替换过的电池

而他在一台从马来西亚发货的设备里发现的第三代植入物，已经接近工艺级别的伪装。橙色柔性板被喷成了和原厂主板一样的黑色，零件编号被刮掉，天线沿着主板上边缘极细地伸出来，不仔细看根本注意不到。攻击者甚至把原厂电池原样留着，只挖掉了屏幕后面原本填充的缓冲棉来腾地方。天线上丝印着一个零件号AC-A2016-NANO-V1.1，NANO指明目标机型，V1.1说明这已经是第二版设计。这不是黑客爱好者的手工活，这是开了模具、批量生产出来的工业级产品。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqZCY7DQiatwczLH9Po9Z9icgiaxKjjYwp2YcTy5Dj3PdiceJJMichtYziaXL960jWAickobFBibrIBp0venJpW5HdZ2xSaB3mQXgL6uFM/640?wx_fmt=png)

第三代植入物的粉色款Nano X。外壳和内板都做了黑色涂装伪装，只有沿上边缘伸出的细黑天线露了马脚

# 从野店渗透进正规连锁渠道

Grand最初发现的那批后门设备，全部来自东南亚电商平台上那些开了没多久就消失的小卖家。这类渠道本来就是硬件钱包厂商反复警告用户不要碰的灰色地带。但这一次出事的CryptoBilis是Ledger在马来西亚、印尼、菲律宾的授权经销商，名义上和官方渠道一样可靠。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqLT9vmTep8ay810AcuBwY6qF7ftlYStwxOlP9oTwgvIhdLSQnVgr8ZztibspDfwhcXo4YzgBbbo4GTwlFaCX6VfJWVUJeZd6Cc/640?wx_fmt=png)

德国用户Johannes在MediaMarkt连锁店买到的两台带后门设备，左右两图分别展示拆解后的电路板与电池仓

德国用户Johannes在八月份从MediaMarkt实体店买了一台Nano X，看到新闻后周末拆开一看，里面也有后门模块。他周一又去同集团的另一家店买了第二台，拆开依然中招。MediaMarkt在欧洲十个国家有一千家门店，是德国版BestBuy，在奥地利、德国、西班牙、土耳其都被Ledger列为授权经销商。Johannes最初怀疑是不是买到了被退货后重新封装的样机，但MediaMarkt员工告诉他退货统一退回Ledger，不会二次销售。他据此判断问题出在Ledger本身的供应链，而不是某家门店的翻新机。

Ledger在X上回应说，目前没有证据表明其安全基础设施、系统或服务被攻破，并提醒授权经销商只从正规渠道进货、不要二次销售退回产品。但攻击者从野店转向授权渠道这件事本身，说明他们已经意识到正规渠道的信任价值，专门挑有品牌背书的经销商下手，让受害者放松警惕。目前除了Nano X，已经有用户报告在Ledger Flex和Stax设备上发现类似装置，新加坡机场卖出去的一台Flex也被确认中招。

# 钱是怎么流向攻击者的

一位在日本的安全研究员从今年三月开始跟进这件事。他自己买了十台Nano X，分别从日本亚马逊、泰国发货地、以及大阪一个转运地址购入，全部带后门。他在这些设备里识别出五种不同版本的植入物，工艺水平参差，有的非常粗糙，有的和Karpelès发现的高级版一致。

更关键的是他做的信号溯源。攻击者在设备里塞的eSIM是全球通用的，只要这台设备开过机，eSIM里就会留下最后连接过的基站信息。他从这些eSIM里提取出历史位置，又顺着数据发送方向追查到接收服务器，托管在香港一家数据中心，运营商指向阿里云。仅六月份一个月，他观测到至少90台被感染设备在向这批服务器发送助记词。真实数字大概率远高于此。

至于CryptoBilis本身，联合创始人Arravind Prabu在周末爆出公司在今年三月被收购，他和联合创始人已经完全退出运营。收购方身份没有公开，理由是签了NDA要到十月中旬才能官宣。这种关键节点上的沉默让社区议论纷纷，但目前没有任何证据指向CryptoBilis原团队与盗窃有关。Johannes在德国的发现则说明，问题已经不局限于马来西亚那一家经销商，整个欧洲的正规零售链路都可能存在被渗透的环节。

# 普通人现在该怎么办

如果你手里有Ledger设备，先不要慌，但要做几件事。第一，回忆一下你是从哪里买的，如果是非官方渠道、价格明显低于官网、或者发货地在东南亚，高度警惕，找个懂硬件的朋友帮你拆开看一眼内部有没有多余的电路板。第二，只要你曾经在任何来源不明的硬件钱包上输入过恢复助记词，立刻把资产转到一个你亲手从官网或正规门店新买的设备里，旧设备直接弃用。第三，这次事件告诉我们一个朴素的事实：硬件钱包的安全性建立在供应链可信这个前提上，一旦物流中间环节被人动手脚，软件层面再强的加密也救不了你。

一亿美元不是一个小数字，但它只是这批后门装置已经收割到的部分。那些还没被拆穿的设备，可能正安静地躺在某些人的抽屉里，等待主人第一次开机。在一个靠信任运转的行业里，看不见的那块额外电路板，才是真正昂贵的教训。

---

# 相关阅读，值得一看的会议视频

# TROPICON 2026 | Reverse Engineering a Ledger Nano X Hardware Implant 【youtube.com/watch?v=e8FWAIuO\_l8】

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqicwcRScyVDQsOicVbwNvic3Z3xkRuHGmSMr7gkUDK48FpVjYMBsexlo53qcaICJxoWPdGUeoMBxT2cvicTKOF5zpRc2yh7kbCjtc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrQjcJ7teyiabdmg7dxrmOKiaX58vdTMPCSbap1fX60rNUBarzZiayd9Fxx5TkMKIv8mlTjaKpIKxH0ONY74w8QpdOtic4SvnTWkjI/640?wx_fmt=png&from=appmsg)

预览时标签不可点

不喜欢

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