---
title: NTLM 降级攻击
url: https://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247506320&idx=1&sn=e286a9b8b24aa0a52635df60cdc36156&chksm=ce5dfbf1f92a72e7c41dca3a56c3114f19fc40d03972b929d44fa4a28c9ec64714d50aafbc50&scene=58&subscene=0#rd
source: Tide安全团队
date: 2023-01-14
fetch_date: 2025-10-04T03:53:28.287090
---

# NTLM 降级攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RX1l9prZqY89MzIKYGm50iaiaFzbb6zzJvCrzjPMtfKaV9Et3sSicTR0VqnicRGiaKzpxDpdExfnvEX93A/0?wx_fmt=jpeg)

# NTLM 降级攻击

原创

小白

Tide安全团队

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RVEB0NZ87EFzNM4866ybBQMVhN8RQR8c6zEaACxatlch2rgdzYzYAiahr1GUq1cLMMGVnvKpF8biaWA/640?wx_fmt=png)

# 深入研究 NTLM 规范

关于版本协商的一些困惑

在开始研究之前，我试图回答“ NTLM 身份验证协议是否支持版本协商?”.当我开始研究 ADFS 中继攻击时，我假设版本协商是协议本身的一部分。因此，当我在规范中读到“ NTLM 身份验证版本不是由协议协商的”时，我感到非常困惑。在验证之前，它必须在客户端和服务器上进行配置。”图1显示了 NTLM 规范的相关部分。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RX1l9prZqY89MzIKYGm50iaiaTdMAmvichRzZJqAjD5ibDkOSariaDTkoicUbJTqmqKMjtib7GOceSLpragw/640?wx_fmt=png)

图1: NTLM 规范的一部分，其中声明协议本身不协商 NTLM 身份验证版本。

然而，规范的另一部分使我更加困惑。当它描述 NTLMSSP \_ NEGOTIATE \_ EXTENDED \_ SESSIONSECURITY 标志时，它提到当设置该标志时，该标志“请求使用 NTLM v2会话安全性。NTLMv2会话安全性是一个误称，因为它不是 NTLMv2。使用扩展会话安全性的是 NTLMv1，这也在 NTLMv2中。”(见图2)[1]。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RX1l9prZqY89MzIKYGm50iaiaPARcs6SmnWA9BqCxPrhYpEAKleBt8emm1vzMfXsRA7ibZvia1RQpWwJg/640?wx_fmt=png)

图2: 描述扩展会话安全标志的 NTLM 规范的一部分。

# 尝试深入

接下来，我花了一些时间研究可以为 LmCompatibilityLevel 设置配置的各种选项，以进一步了解它们。图3中的表列出了此设置的有效选项。这也证实了我对 NTLM 规范的理解，即它们只支持配置一个选项或另一个选项，而不支持任何类型的协商机制。可以将服务器配置为支持 NTLMv1或 NTLMv2，但是客户端没有同时支持两者的选项。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RX1l9prZqY89MzIKYGm50iaiahejACjBlA0d9XpQVlfiarvtiajdHjucmYInarusibicmlYTjZxCZP7KUSw/640?wx_fmt=png)

图3: 来自 MSDN 的一个表，列出了 LmCompatibilityLevel 设置的可用选项。

后来，我发现了一篇 MSDN 文章，其中提到“与普通的 NTLMv1或 NTLMv2不同，NTLMv1 w/ESS 实际上是在客户端和服务器之间协商的(NTLMv1和 NTLMv2使用安全密钥 LmCompatibilityLevel 进行配置)。它是通过在谈判标志中设置一点来协商的，称为 P (MS-NLMP，Section 2.2.2.5)。”[2].这个声明使我有些困惑，因为它讨论了对附加安全特性的协商支持(请参见图4)。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RX1l9prZqY89MzIKYGm50iaiaQfBWEK7OibXftH8HFWXCQgmQIoGK7sicC2IPNsKe5cJHghbiaPtwRM5ibA/640?wx_fmt=png)

图4: MSDN 文章的摘录，其中提供了有关 NTLMv1扩展会话安全性(ESS)的更多细节。

在深入研究了规范之后，我发现了如图5所示的伪代码，它显示了一些用于计算 NTLMv1中的challenge response的示例代码。我惊讶地注意到，这个版本向函数传递了一个 ClientChallenge 值，因为 NTLMv1实际上并不支持 NTLMv2这样的客户端challenge字段。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RX1l9prZqY89MzIKYGm50iaiaCjvnRGNux7hzlmy5IZp379092kMGqGWdTyvt8qBUqMKVlATCCf14qA/640?wx_fmt=png)

图5: 来自 NTLM 规范的伪代码，指示 NTLMv1如何计算 NtChallengeResponse 和 LmChallengeResponse。

# Client Challenge从哪里发出？

在阅读了当时的规范之后，我不确定客户的质疑从何而来。但是，在图6中，我们可以在 go-ntlm 库源代码中看到客户机的 LmChallengeResponse 字段提示了这个Challenge。我们还可以看到，在 NTLMv2的情况下，这个Challenge是从 NTLMv2 \_ CLIENT \_ CHALLENGE 结构中读取的，该结构存储在 NTLMv2 \_ RESPONSE 字段中，该字段存储在 NtChallengeResponse 字段中。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RX1l9prZqY89MzIKYGm50iaiaC95X6L6ibALgglLicm8gWdaklOfS1Bib4iaoibicibhIuX3rspVbEd3ulWdlA/640?wx_fmt=png "null")

图6: go-ntlm 库中的源代码，它使用 NTLMv1从 LmChallengeResponse 字段读取客户端询问值。

设想一个场景，我们试图从配置为支持具有扩展会话安全性的 NTLMv1身份验证的客户端捕获 NTLMv1散列。在这种情况下，我们需要客户机对攻击者控制的1122334455667788Challenge进行加密，以便利用 crack.sh 站点提供的彩虹表服务。不幸的是，如果我们用来捕获hash的服务器表明它支持服务器发送给客户机的谈判标志中的扩展会话安全性，那么客户机生成的Challenge将会破坏这一点。在这种情况下，我们希望，例如，在 Responder 中使用-able-ess 标志 ，以防止客户端包含一个客户端Challenge，这将破坏与彩虹表的兼容性。

# 响应端的源代码

我的下一个问题是，如果 NTLM 协议不协商版本，那么 Responder 如何区分 NTLMv1和 NTLMv2散列？我认为回答这个问题的最好方法是查看 Responder 实用程序的源代码。

图7和8显示了 Responder 源代码的相关部分，其中我们观察到 NthashLen 是消息的有效负载部分中 NtChallengeResponse 字段的长度。我们可以在这里看到，Responder 正在检查该字段的长度，以确定 NTLM 身份验证协议的版本。我们可以看到，字段的长度在图7中为 NTLMv1的24个字节，在图8中为 NTLMv2的大于24个字节。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RX1l9prZqY89MzIKYGm50iaia3PyMPKlHLfibJPQuYOuhdvVCNp0XmXeTLzMBShBneJRibkrPUx0W7Zow/640?wx_fmt=png)

图7: Responder 用于确定消息是否为 NTLMv1类型的代码。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RX1l9prZqY89MzIKYGm50iaiaLdNGuuw2O8CP3Lhynv1vuykwjINVZY1R6TRY4hkuxHo7l5C7dzuPEQ/640?wx_fmt=png)

图8: Responder 用于确定消息是否为 NTLMv2类型的代码。

如果我们随后查看 NTLM 规范的2.2.2.6部分，我们可以看到 NTLM \_ RESPONSE 格式概要，以便在使用 NTLMv1时使用。图9显示 NTLM \_ RESPONSE 结构包含一个名为 Response 的24字节字段。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RX1l9prZqY89MzIKYGm50iaiaibaywXJibUE7S6BEgQ4NMma0e8olUA7cxgibloK0wa3IuxBsUaGVLxTbA/640?wx_fmt=png "null")

图9: 来自 NTLM 规范的一个表，详细描述了 NTLM \_ RESPONSE 消息的格式。我们注意到它包含一个24字节的单一固定长度字段。

# 如何确定版本？

接下来，让我们看一下 NTLMv2响应，以确定为什么在这个场景中 Responder 要检查长度是否大于24字节。检查规范的2.2.2.8部分(如图10所示) ，我们发现 NTLMv2 \_ RESPONSE 结构包含一个16字节的固定长度字段和一个名为 NTLMv2 \_ CLIENT \_ CHALLENGE 的可变长度字段。我们检查了 NTLMv2 \_ CLIENT \_ CHALLENGE 结构的所需字段(如图11所示) ，并确定该结构至少有28个字节的所需数据。由于计算得到的 NTLMv2响应总是包含至少24字节的所需数据，因此我们可以准确地利用这种机制来确定何时使用 NTLMv2。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RX1l9prZqY89MzIKYGm50iaiaAO6mjcLx0icdtLu1Y2bkw5uwOkuYoicC1eWnWumfnG2zhuPCvB0ad8TQ/640?wx_fmt=png "null")

图10: NTLMv2 \_ RESPONSE 字段包含一个16字节的必需字段和一个嵌入式可变长度 NTLMv2 \_ CLIENT \_ CHALLENGE 结构。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RX1l9prZqY89MzIKYGm50iaiaeibic7miaNXBGT9Sq9iboibbHPPIicSptUK456lADqicZib8XEoPnCQBe4qvCw/640?wx_fmt=png "null")

图11: NTLMv2 \_ CLIENT \_ CHALLENGE 结构必须至少有28个字节长(不包括可变长度的 AvPair 结构，其中还包括所需的字段)。

# 了解 NTLMv1 Hash格式

在更多地了解了 Responder 如何区分 NTLMv1和 NTLMv2散列之后，我很好奇 Responder 使用什么格式来存储 NTLMv1hash。在这种情况下，格式非常简单。在图12中，我们看到 NTLMv1hash包含用户名、计算机名、 LmChallengeResponse、 NtChallengeResponse 和 Challenge。本质上，它包含计算的challenge 的输出和计算challenge 响应所需的输入challenge 。希望恢复用户原始明文密码的攻击者只需利用相同的算法并比较计算出的challenge ，以执行离线攻击，试图恢复用户的密码。在图13中，我们显示了 NTLMv1hash中的 LmChallengeResponse 和 NtChallengeResponse 字段如何与捕获的 NTLM \_ AUTHENTICATE 消息中的相应字段匹配。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RX1l9prZqY89MzIKYGm50iaiaX1FvaAnqqGrYic0fOI3mSvO9zcKHLnnDYl9uTamb8tTN8mLKNsjzfXQ/640?wx_fmt=png "null")

图12: NtChallengeResponse 和 LmChallengeResponse 以及服务器Challenge是生成的 NTLMv1散列的主要组件。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RX1l9prZqY89MzIKYGm50iaiaRMRTwl0ncGuDXibr9ZfbtMR7Qsy5q5nx3Vn9LGLiavvickqmCicOial5bTg/640?wx_fmt=png "null")

图13: Responder 用于计算 NTLMv1hash输出的 NtChallengeResponse 和 LmChallengeResponse 值。

# NTLMv1 DES 加密机制

NTLMv1通过利用 DESL 函数加密服务器请求来计算客户端请求。它通过将用户的 NT hash分解成三个、七个字节的 DES 键来实现这一点。不幸的是，由于它使用的算法也使用三个独立的 DES 密钥加密每个密文值，攻击者可以分别破解每个 DES 密钥，以恢复受害用户的整个 NTLM hash。有关计算 NTLMv1challenge response的 go-ntlm 库代码，请参见图14。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RX1l9prZqY89MzIKYGm50iaia8TgompSnj3T7b3c1IUPE2dCCbIdXQ0NQkoAC9jDy0SbMedvictBevpw/640?wx_fmt=png)

图14: 从 go-ntlm 库生成 NTLMv1 NtChallengeResponse 和 LmChallengeResponse 值的示例代码。

图15显示了代码在图14中使用的 DESL 函数的定义。DESL 函数将用户的 NTLM hash分成三个独立的键，第三个键用零填充。然后，三个独立的 DES 密钥加密并连接服务器Challenge(或扩展会话安全性下的服务器和客户机Challenge的 MD5hash)。不幸的是，由于 DES 算法使用56位密钥，因此攻击者可以利用一个服务(比如 crack.sh)来恢复原始的 NTLM 散列

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RX1l9prZqY89MzIKYGm50iaia5OAULg1FQARibevkRYovLqkqo3QfdAFH8jxN8EiazWh4cvicLyJ1AApAg/640?wx_fmt=png "null")

图15: NTLM 规范的摘录，详细描述了用户的 NT 或 LM hash如何分解成多个 DES 密钥，这些密钥随后对计算出的询问值进行加密。

# 了解 NTLMv2Challenge Response机制

计算 NTLMv2Challenge Response值的方法与 NTLMv1非常相似，但有一些关键差异。首先，它不使用前面提到的 DES 算法，而是利用 HMAC MD5算法来计算Challenge Response。其次，用于计算Challenge的数据包括额外的信息，例如 NTLMv2客户机挑战结构中的 AV \_ PAIR 值。图16显示了计算 NTLMv2Response值的 go-ntlm 库代码。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RX1l9prZqY89MzIKYGm50iaiaf3X4BUicBMYT5VibgKgXWUTgaoT253q5pXJAQxviaEAv6yZawVg0yWTKA/640?wx_fmt=png "null")

图16: go-ntlm 库的摘录，显示了如何计算 NTLMv2challenge response消息。

NTLMv2哈希格式与 NTLMv1哈希格式非常相似。在本例中，它包含用户名、域、服务器请求、计算机响应(NTProofStr)和 NTLMv2 \_ CLIENT \_ CHALLENGE 结构，后者包含时间戳、客户端请求和 AV \_ PAIR 字节。图17显示了 NTLMv2结构的各个字段的详细信息。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RX1l9prZqY89MzIKYGm50iaiaNcNGuJapKu5NUsWpEouTTS1sNPSZHhsXsb08rnQd8eibjmjtXB1AsOA/640?wx_fmt=png)

图17: Responder 捕获的 NTLMv2hash，其标签标识hash数据的相关组件。

# 基于 NTLMv1的 SMB 到 LDAP 中继攻击

从 SMB 中继到 LDAP 服务在理论上也是可行的，使用 NTLMv1。这将提供另一种可供选择的利用方向，它不需要攻击者利用类似 crack.sh 这样的站点，出于安全原因，这可能是不允许的。NTLMv1不支持计算消息完整性代码(请参见图18) ，该代码允许攻击者修改计算出的 NTLM \_ AUTHENTICATE 消息的属性。在图19中，我们看到 LDAP 服务利用 NTLMSSP \_ NEGOTIATE \_ SIGN 字段来确定是否需要签名。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RX1l9prZqY89MzIKYGm50iaiaQon2ehXzQtgkavSXHN6QrqtB4YSqKeWolymQLhDNhhga1pGVObrPvg/640?wx_fmt=png "null")

图18: 使用 NTLMParse 程序检查 NTLMv1 AUTHENTICATE \_ MESSAGE，我们观察到消息完整性代码(MIC)不存在，允许修改消息。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RX1l9prZqY89MzIKYGm50iaia4VcXBSCGWnzBdNFibHGzRLZ382bsUfUGHzWxN0ao3kmq8NQ3L8rLSHw/6...