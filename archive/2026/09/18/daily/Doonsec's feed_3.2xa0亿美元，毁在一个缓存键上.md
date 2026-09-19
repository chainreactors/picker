---
title: 3.2xa0亿美元，毁在一个缓存键上
url: https://mp.weixin.qq.com/s/kQuj8aZOf3tqAJW-P88MxQ
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:52:16.622726
---

# 3.2xa0亿美元，毁在一个缓存键上

# 3.2 亿美元，毁在一个缓存键上

原创

BlockSec
BlockSec

BlockSec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/2ibKZs4HxyqtHYWvlnQNalqAdr14bRCYPB7Ymg14o0BVRCnTCmK94JySap6R7sNS4EApc4gLJT8qf62j8ZpzoJbx5s3CYoPfoYN3UlF92GzA/640?wx_fmt=gif&from=appmsg)

**简介**

核心要点：

* 本报告收录2起安全事件，合计损失约$320M，一起发生在比特币侧链Liquid Network，另一起是比特币桥Symbiosis（部署在BNB Smart Chain、Ethereum和Rootstock）。Liquid Network这起事件占了总损失的99%以上，Symbiosis造成的估计损失为$770K。
* 两起事件中，那道本该拦下伪造的校验都跑通了、也都返回了“通过”，只是通过的理由都不对。Liquid节点把一份自己从未检视过的范围证明判定为true，因为另一份证明的结论恰好归档在了同一个缓存键下；Symbiosis的签名者在一个铸造数额上签下了有效签名，而这个数额，是他们自己在比特币一侧的decoder根据存款人可控字段算出来的。
* 一笔伪造出来的余额值多少钱，取决于它最终怎么变现，而不是它的面值。Liquid凭空造出的4,000枚L-BTC背后没有任何真实比特币，但绝大部分经由双向锚定变成了真正的比特币，约$320M因此流出；Symbiosis铸出的syBTC数量超过比特币总供应量的两千倍，但它必须卖进的那些资金池里只有11.26枚syBTC，流动性提供者与用户的估计损失为9.97 BTC。

过去一周（2026/09/07 - 2026/09/13）内，以下2起安全事件被收录，总损失约$320M。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4HxyqvtPqJrlCryVSKnW6mffyFNhw5ibxia2pVOdMy3wicI5EINEtzH2Qb4HLICHQicE7bAvF5xVYKoicOiaKfPya7bpdFRb0ibJF9OSAuVJw/640?wx_fmt=png&from=appmsg)

表 1：本周收录的安全事件概览

*\* Liquid Network事件发生于9月6日，未被上周报告覆盖，此处纳入以保持完整性。*

**本周看点：Liquid Network**

本事件被选为本周看点，是因为它那套隐蔽的缓存键碰撞机制，以及它造成的巨额损失。攻击者构造出一笔交易，让它的校验数据把前一笔交易的字节重新切分了一遍，于是一份从未被检查过的证明，拿到了缓存里那条现成的校验结论。

2026/09/06，比特币侧链Liquid Network被攻击，损失约$320M [1]。Liquid所运行的节点软件Elements，其范围证明校验缓存发生了一次碰撞：为某个输出记录下的valid结论，被返还给了另一个完全不同的输出，后者的证明因此在从未被检视的情况下获得通过。攻击者借此凭空造出4,000枚没有任何比特币与之对应的L-BTC，再通过网络正常的peg-out把它们提走。次日，3,400枚BTC被退还给联邦，约598.5枚BTC留在攻击者手中 [2]。

**背景**

Liquid Network是一条构建在Elements之上的比特币侧链，Elements是一个从比特币代码库派生出来的开源区块链平台。它的存在是为了让比特币的转移比主链更快、更便宜、更私密。比特币在两条网络之间通过双向锚定往返：peg-in时，用户把BTC锁定给网络的联邦（一组共同托管锚定资金的受信任机构），换得等量的L-BTC；peg-out时，用户销毁L-BTC，联邦释放出对应的BTC。Liquid的区块不靠挖矿产生，而是由联邦的一组轮值职能节点（functionary）提出，再由达到门限数量的联邦签名完成最终确认。

和比特币一样，Liquid把资金记作未花费的交易输出，而不是账户余额。一笔交易要指明已有的未花费输出、将其解锁，并创建新的输出，且它创建的价值必须等于它消耗的价值。每个输出都带有一段锁定脚本，即scriptPubKey。以OP\_RETURN开头的输出永远无法被花费，它的用途就是承载数据，而一次peg-out正是以这种输出的形式表达的。

Liquid还默认隐藏金额。它写入输出的不是金额本身，而是对该金额的Pedersen承诺（金额承诺）。承诺具有可加性，因此节点无需知晓其中任何一个数值，就能确认一笔交易的输入与输出是否配平。这个性质是双向的：承诺同样可以藏起一个行为上为负的数值，那会让一笔交易的输出超过输入却仍然配平。所以每个隐藏了金额的输出还要附带一份范围证明，用来证明被承诺的金额落在[0, 2^64)之内。验证一份范围证明代价不低，而同一个输出会被验证不止一次——交易进入内存池时一次，交易随区块抵达时又一次——因此Elements会把已经通过的证明缓存起来，以该证明本身、以及它当时所比对的数据为键。

**漏洞分析**

缺陷在于Elements（每个Liquid参与者都运行的节点软件）是如何缓存已验证范围证明的。

CachingRangeProofChecker::VerifyRangeProof()会为眼前这个输出推导出一个缓存条目，一旦命中就立即返回成功，根本不去碰那份证明：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4HxyqtyVSE49F0YibdkUqycGta3pWkdwKZaxHcgDROPnRYGkVtWNfpbwicyiawRaPM0rfZNmoO36icKOjriaiaFZ02eeXycCPN3Sic9d5ibJXU/640?wx_fmt=png&from=appmsg)

图1：Elements范围证明校验代码在缓存命中时直接返回true，此时证明本身尚未被检视

条目由ComputeEntryRangeProof()生成，它把四个字段一个接一个写进同一个SHA-256流，然后取出摘要：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4HxyqsxfUCgYNcLbicZpdVckRGMJuC4KO3w4wDV1YZPteF3t8YJ3ibCxrmb3ib0FHC8on2438EiaIHVH1L5E5cOPkxOfYrTRa3iby3ibmxTo/640?wx_fmt=png&from=appmsg)

图2：ComputeEntryRangeProof把四次Write串接进同一个带salt的SHA-256哈希器，字段之间既无长度前缀也无分隔符

这四个字段分别是：范围证明本身、对金额的Pedersen承诺、标识该输出持有何种资产的资产生成元，以及scriptPubKey，纳入它是为了让一份通过的证明绑定到某一段特定的锁定脚本上。

四个字段都没有带着长度前缀或分隔符写入：范围证明和scriptPubKey是变长的，Pedersen承诺和资产生成元则始终是33字节的定长点。于是摘要记下的只是拼接后的那串字节，至于一个字段在哪里结束、下一个从哪里开始，无从体现。两组不同的字段只要拼接出同一串字节，就会得到同一个条目，而先被校验的那一组会留下一条结论，供另一组直接取用。哈希器确实用每个节点各自的随机salt做了初始化，但这个salt同样被加在两条字节流的最前面，它改变了摘要，却并不能把两份输入区分开。这个缺陷在提交94000967中被修复 [3]。

**攻击分析**

以下分析基于交易271147...187ec5和f24a4b...0a183f，两笔都被运行着存在缺陷版本代码的节点所接受。

**Step 1：**攻击者发出一笔交易，其第一个输出是一个承载了67字节数据的OP\_RETURN。

![](https://mmbiz.qpic.cn/mmbiz_png/2ibKZs4Hxyqv5OvsFHxaDzloGvk0YWjMbhYk1Vh0kfKEoIVGD9Kfic8jsEGj1ULGMbJVMdA6lSicib8MQCNlrjI0W4BYIP1t0wBVpHic8FYu5qJY/640?wx_fmt=png&from=appmsg)

图3：Liquid交易输出，显示一段带67字节推送的OP\_RETURN脚本，并标注出scriptPubKey与金额承诺

它的scriptPubKey以6a 43开头——OP\_RETURN操作码，后跟一次67字节的推送，然后是两个33字节的值和结尾的一个6a。被推送的这67字节并不是这笔交易需要的数据。它们是另一个尚不存在的输出的金额承诺和资产生成元。对这个输出的校验，把一条valid结论存进了由它自己那四个字段所决定的条目下。

**Step 2：**攻击者随后提交了增发交易。这笔交易的OP\_RETURN输出，其scriptPubKey只有单字节6a，而它的金额承诺，正是前一笔交易那次推送里嵌着的那个33字节的值。它的范围证明字段，则由前一笔交易的范围证明、承诺和资产生成元拼成，末尾再接上6a 43两个字节。

![](https://mmbiz.qpic.cn/mmbiz_png/2ibKZs4HxyqvkZGQm9lvFs4icgP2Io4JNOzxXUHRfQvTlL9Kc5LkkEdNTNatbv6G7bsCiatXhPia8tonB4sEcnaGFQHETQx4mm3Libe4uEtcIicW4/640?wx_fmt=png&from=appmsg)

图4：增发交易的输出，第一个被标注为发往攻击者地址的4,000枚有效L-BTC，第二个是脚本仅有单字节的OP\_RETURN

于是这个输出的四个字段，拼接出的字节流与前一笔交易完全相同，只是切分的位置换了地方：

Primer: P0 | C0 | X | S0, where S0 = 6a 43 <33-byte C1> <33-byte X> 6a

Inflation: P1 | C1 | X | S1, where P1 = P0 || C0 || X || 6a 43 and S1 = 6a

Both concatenate to: P0 || C0 || X || 6a 43 || C1 || X || 6a

缓存返还了此前那条结论，P1从未被验证过，它根本不是一份范围证明。C1承诺的是一个数额很小的负值。这笔交易的另一个输出是一个发往攻击者地址ex1q7kg...qa2w的普通P2WPKH输出，带着一个数额很大的正向承诺和一份货真价实的范围证明，两者正好相互抵消，交易因此配平。它留下了4,000枚没有任何比特币与之对应的未花费L-BTC。

**Step 3:** 攻击者执行peg-out。两笔交易通过普通的OP\_RETURNpeg-out输出销毁了3,996.01834922和2.65138358枚L-BTC，合计3,998.66973280枚。负责授权peg-out的职能节点用的还是那份存在缺陷的代码，校验通过后释放了比特币：3,995.99999857枚BTC和2.49749857枚BTC抵达攻击者在比特币网络上的地址，共计3,998.49749714枚。

网络暂停并分裂成两条链，事件在这期间得到处置 [4]，恢复运行时拒绝了那笔无效的peg-out [2]：如今区块浏览器上primer交易显示为已确认，而inflation交易没有，尽管它放出的那些比特币早已从联邦的钱包里流出。次日16:09:25 UTC，攻击者把3,400.00000000枚BTC退还到联邦的锚定钱包，剩余约598.5枚BTC仍未归还 [2]，双方通过嵌入比特币交易的消息继续磋商 [4]。

**结论**

攻击者没有攻破任何密码学，也没有拿到任何私钥。缺陷在于范围证明缓存是如何标识“这个我已经查过了”的：它的键把四个字段——其中两个是变长的——拼进同一条哈希流，而没有任何东西标明每个字段到哪里为止，于是另一组字段可以把同样的字节重新切分一遍，落到同一个条目上。一条存好的valid结论就这样被返还给了一份任何节点都不曾验证过的证明；而一旦范围证明不再约束它背后的金额，一条隐藏金额的账本也就失去了唯一能保证这些数值非负的东西。一个精心构造的输出变成了4,000枚L-BTC，双向锚定又把它们变成了主链上真正的比特币。

任何由一个以上变长输入推导出来的标识符，都必须把输入之间的边界一并纳入：要么给每个字段加上长度前缀，要么把各字段哈希进彼此分开的定长槽位。做不到这一点，推导就不是单射的，两份不同的输入便可能被当成同一份。这条要求在以缓存替代校验的场合尤其关键，因为在那里，一次命中就是一个“不再执行校验”的决定。

**本周其它事件**

**Symbiosis**

2026/09/11，跨链桥Symbiosis的比特币通道在BNB Smart Chain、Ethereum和Rootstock三条部署上被攻击，流动性提供者与用户的估计损失为9.97 BTC（约$770K，按9月11日约$77K的价格计）[5]。负责决定要为一笔比特币存款铸造多少合成比特币的那段链下代码，从交易中存款人可以控制的一部分数据里读取存款人身份，这让攻击者得以冒充管理员，把最低手续费压到负数；随后它从存款额里减去这笔手续费时不检查符号，于是减法变成了加法。

**背景**

Symbiosis是一个跨链流动性协议，它在链间转移价值靠的是锁定加铸造，而不是把资产本身搬过去：在有智能合约的链上，用户的代币由源链上的Portal合约锁定，宿主链上的Synthesis合约随即铸造出等量的合成代币，即sToken；销毁sToken则释放出原始资产 [6]。比特币经由这条通道抵达时以syBTC的形式出现，这是一个8位小数、精度与比特币自身最小单位相匹配的代币，发行在BNB Smart Chain、Ethereum和Rootstock上，并在资金池中与BTCB、cbBTC、WBTC和RBTC配对 [5]。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4HxyqtdbZLicXFYVbzAx8uugToUY6vu90e6XHTECwiaYjRQIN0rByHxY8RbfMS37LrxlmNOaXQRcKOdDK3Biaj9HFdc7sSJpCK4jzlYyc/640?wx_fmt=png&from=appmsg)

图5：Symbiosis官方文档中的铸造流程与销毁流程示意图

比特币没有这些：没有智能合约，也就没有Portal合约来锁定存款。取而代之的是portal——一个扮演同样角色的指定比特币地址。一笔存款就是一笔付给它的普通比特币交易，目标链所需的指令作为数据附着在这笔交易上。属于该桥的链下代码读取这些数据，从中得知是谁在存款、存了多少、合成代币要发去哪里，并负责征收portal的手续费——这笔手续费在铸造数额被确定之前先从存款额里扣除——其最低额度是一个由管理员设定的参数。

比特币一侧发生的一切，目标链都无从得知，因此由Relayers Network把由此产生的请求送到对岸。请求以编码调用的形式抵达该桥的链上入口BridgeV2，再由它转发给Synthesis。授权依托于一个MPC密钥：协议的签名者各持一份私钥分片，共同对请求产出单一签名。接收中继请求的入口只有一个修饰器把关，在分发调用之前不做任何别的事：

![](https://mmbiz.qpic.cn/mmbiz_png/2ibKZs4HxyqsKoQk3RwfibRJNDEe15kuaXSVEOiccA6K8zAItEMRYSFbXZQI6Ek9pB0ArJiccamIVQ1ibn0GHQc2sT88Yd3SymqibQpZdNl6h3bHg/640?wx_fmt=png&from=appmsg)

图6：receiveRequestV2Signed把调用转发给\_processRequest，仅由标红的onlySignedByMPC修饰器把关

该修饰器对请求做哈希，并要求随附的签名对MPC地址有效：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4Hxyqs1eK57lrC7ZI2VXMj8AoY1iarAm44oC2REdz8Nfk8w9Zf5v6Dy6TIaEV5vqWam4aQdgg5vaoBvKXLpBicCys0ZmA8tjl4xnEUAk/640?wx_fmt=png&from=appmsg)

图7：onlySignedByMPC修饰器要求SignatureChecker.isValidSignatureNow针对请求哈希与MPC地址校验通过

这份合约确立的是：MPC密钥签了这个请求。请求里携带的数额，是在比特币一侧算出来的。

**漏洞分析**

缺陷不在目标链的合约里，而在那个读取比特币存款、把它们转成跨链请求的链下服务中。它的源码不公开，因此以下内容依据的是项目方的post-mortem [5]，以及一份2024年的第三方审计报告，其中有一段代码片段看起来与此相关 [7]。

存款路径上的两个缺陷必须叠加才能成事，post-mortem明确指出，单独任何一个都不足以让攻击得手。

第一个缺陷在于存款人身份是如何被识别的。附着在存款上的指令会被解码，以还原出是谁在存款，而这个decoder把身份取自交易数据中由花费该输入的人所控制的那一部分。于是存款人可以把自己冒充成协议认得的任何角色，包括portal的管理员，也就是设定portal能接受的最低手续费的那个角色。

第二个缺陷在于这笔手续费是如何被扣除的。2024年的审计报告指出了decodeWrap()里那一行代码，它通过从存款输出的金额中减去手续费来计算铸造数额：

Value: types.Satoshi(tx.TxOut[idx].Value) - info.PortalFee,

该审计的发现是：types.Satoshi是一个有符号整型，而携带PortalFee的info结构体不可信且由用户控制，因此结果可以被压成负数；序列化给目标链时又按无符号数解释，足以铸出任意数量的合成比特币。审计当时将这一问题记为已修复 [7]。2026年的post-mortem描述了同类失效：这笔手续费在没有检查符号的情况下被减去 [5]，一笔负的手续费因此放大了存款额，而不是缩小它。存款路径上似乎没有任何环节，把铸造数额与实际收到的比特币数量绑定起来。

**攻击分析**

十二笔伪造铸造在BNB Smart Chain、Ethereum和Rootstock上于约四分钟内接连得手 [5]。以下分析基于其中一笔，即BNB Smart Chain上的交易0x9a2bc0...21b9b959。

![](https://mmbiz.qp...