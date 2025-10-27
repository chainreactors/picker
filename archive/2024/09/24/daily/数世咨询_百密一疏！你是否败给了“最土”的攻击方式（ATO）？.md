---
title: 百密一疏！你是否败给了“最土”的攻击方式（ATO）？
url: https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247517513&idx=1&sn=c41f61cb0c552f04499e055580a5de5a&chksm=c144f7f4f6337ee2e31a8440863d2968e494e4f53476ff31181456c37342c1c141dcd0172c8c&scene=58&subscene=0#rd
source: 数世咨询
date: 2024-09-24
fetch_date: 2025-10-06T18:28:25.596759
---

# 百密一疏！你是否败给了“最土”的攻击方式（ATO）？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y9btpvDIDqoDyowYRUKOIEJF9cQ4EI7dL3sZZuIqgliadSpdT87sFNfuddoic7NiaYYtgsAfvaC1LhjSYQIAcKBqA/0?wx_fmt=jpeg)

# 百密一疏！你是否败给了“最土”的攻击方式（ATO）？

原创

零零信安 王宇

数世咨询

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqoDyowYRUKOIEJF9cQ4EI7dczBribKpcvE2abicQxMOKZIeSWBPM85alDNGIdiaUaeic61D9aSPNicibvLA/640?wx_fmt=png)

长文，但是干货。

本文第一部分为案例，第二部分为原理，第三部分为解决方案。

# **背景**

时间回到二十多年前，那时候上网还需要拨号，大家用的聊天工具叫OICQ，服务器还在用WINNT。从那时起，有一个网络安全词汇就已被网吧战神熟知，它叫“盗号”。

这个“最土”的词伴随着网安成长了二十多年，现在它早已被专业人士改成了另一个洋气的名字“账号接管攻击”（Account Takeover，简称ATO）。

有时候我觉得安全行业很奇怪，AI、TI、BAS、ASM、XDR、CTEM等等，新鲜概念层出不穷，数百款产品貌似各显神通。但是无数政府、军队、企业最终却倒在了“最土”的“盗号”攻击下（好吧，我指的是国外，你懂的）。

不管您是甲方还是乙方，可能都会感到惊讶，这怎么可能？

废话少说，有图有真相。

# **第一类案例：军政系统的管理和操作权限**

## **案例1：美军的开源情报监测系统**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqoDyowYRUKOIEJF9cQ4EI7dCwk4WqxxkibPUtCzEn8uXxhjWXZzDmibVrjgYl5qP6wInLxUgXHRJPow/640?wx_fmt=png&from=appmsg)

美军正在使用该系统监测和分析全球开源情报，包括：中国、俄罗斯、波兰动乱、北非间谍、欧洲联合演习等。该系统存在ATO风险，攻击者可以通过该攻击方式获得和接管美军账号权限。

美国陆军、空军、海军、海军陆战队等部队有数万人员的账号面临ATO风险的威胁。

## **案例2：法国法务部**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqoDyowYRUKOIEJF9cQ4EI7dWG5AM8ibbex6LjrJGomc45pbcEddtoIbLVOgRiaI8icChFyEFJJYfWeuw/640?wx_fmt=png&from=appmsg)

法国法务部的内部工作系统存在ATO风险，攻击者可通过该攻击方式获得和接管管理员权限，并查询和操作数千名工作人员的个人信息和账号：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqoDyowYRUKOIEJF9cQ4EI7d1QAbNPT2oicib3YTVBMMY7YYS5rQtDVIWkJ3cmlia9icYewUk38YiaB2ia7w/640?wx_fmt=png&from=appmsg)

法国法务部至少有数百员工面临ATO风险的威胁。

# **第二类案例：金融和电商的用户权限**

你可能会觉得政府的安全性不好，那么我们看一下离钱最近的金融和电商行业，他们通常是我们认为安全性很好的。

## **案例3：著名交易所crypto.com**

Crypto是全球TOP15的虚拟货币交易所，使用了异常登录检测和双因素认证（2FA）策略。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqoDyowYRUKOIEJF9cQ4EI7dHIhjhNFkyggmcexp8uOzeWufmiaaHnyPSicegmOqDEdTB405RpD4dG5w/640?wx_fmt=png&from=appmsg)

可惜的是，它仍然存在ATO风险，攻击者可以绕过他的安全策略接管用户账号，并进行该权限下的所有操作，不仅可以查询隐私信息，还可以进行交易查询和规则设置。

Crypto交易所有超过10万用户可能面临ATO风险的威胁。

## **案例4：澳大利亚保险公司medibank**

澳大利亚保险公司medibank.com.au是澳大利亚最大的健康保险公司，其宣称投资1.26亿澳元（约6亿人民币）建设网络安全体系。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqoDyowYRUKOIEJF9cQ4EI7dActBNmUyH5dVUNDswwrHKY0wJVDNpg0yiaLd7ticwPBUNf7eHxAZ1ichg/640?wx_fmt=png&from=appmsg)

它仍然没有对用户进行完善的保护，攻击者可以利用其存在的ATO风险对用户进行攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqoDyowYRUKOIEJF9cQ4EI7dicoWpsrd4z5oicjIEnuJyialqSib3FL0VXk1nQIFgEoyFE0Vyukm9pQqKg/640?wx_fmt=png&from=appmsg)

不仅可以查询个人隐私，还可以“帮助”用户购买产品、修改订单等诸多操作。

Medibank保险公司至少有数千用户面临ATO风险的威胁。

# **第三类案例：头部IT科技公司**

你也许会认为，以上案例中，都是不懂网络安全的企业，那我们就用全球头部IT科技公司为例，证明这并不是“打哪指哪”的偶发风险。

## **案例5：Github**

Github，应该不用介绍了，无数企业和个人的代码仓库和文件储存在这里。它的安全性很好，也使用了异常登录检测和双因素认证（2FA）策略。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqoDyowYRUKOIEJF9cQ4EI7diby0sBEmia9h62cENMCSuBlAnABhdKKQYVu0clh3fTbCsXLwDqNcufxg/640?wx_fmt=png&from=appmsg)

可惜它也存在ATO风险，以上截图你可以说我是随便编的（信不信由你），不过攻击者确实可以很容易的绕过其安全策略接管用户账号。

Github至少有数百万用户面临着ATO风险的威胁。

## **案例6：Cisco**

对，就是你知道的那个Cisco公司。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqoDyowYRUKOIEJF9cQ4EI7dHvrHUJDICbR8f2NialunF0rT3HXPEGHXsShCn2WvJXWvOXxutzX97Dw/640?wx_fmt=png&from=appmsg)

仍然同上一个案例所述，信不信由你，攻击者可以利用ATO风险接管Cisco的企业和个人用户账号权限。

Cisco公司至少有上百万用户面临着ATO风险的威胁。

# **第四类案例：网络安全相关网站**

我们再来看看全球著名的网络安全相关网站是否会受到“账号接管攻击”（ATO）风险的影响。

## **案例7：全球头号网络空间搜索引擎shodan**

网络空间搜索引擎作为最主要的攻防工具，国外有shodan、censys，国内有fofa、zoomeye等。作为全球第一的shodan.io，同样存在账号接管风险，攻击者在成功攻击后可以使用该账号的权限和会员等级。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqoDyowYRUKOIEJF9cQ4EI7dhzSW8uXTDO1v8ZYXIERhvibbIv070nDw3IQhTRKIWuUR9yBu2eZ2ibAg/640?wx_fmt=png&from=appmsg)

Shodan网站至少有数万用户面临着ATO风险的威胁。

## **案例8：著名黑客论坛Leakbase**

作为暗网十大黑客论坛之一的Leakbase，以发布大量的账号泄露信息出名，但是它自身却存在账号接管（ATO）风险，攻击者在攻击成功后可使用相应用户的权限和积分，更重要的是，可以查询到该账号的隐私信息（这对于在暗网和黑客论坛注册的用户来说，是致命的）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqoDyowYRUKOIEJF9cQ4EI7dGQ09AdUUo0HRa2IqataYAuiaZN9aAaJHS4YE1qwCraibyrrVw5r3Dmxg/640?wx_fmt=png&from=appmsg)

作为十大暗网黑客论坛之首的Breachforums，也存在相同的风险，并且从BF V1到现今的V3，该风险一直存在。

你可以质疑说，黑客论坛没有保护用户的义务。但是同样作为十大暗网黑客论坛之一的Exploit，在这方面就做的非常棒，至今尚未发现有可被利用的账号接管（ATO）风险。

Leakbase网站至少有数百用户面临着ATO风险的威胁。

# **第五类案例：国内企业**

因为众所周知的原因，我们仅以国内网络安全企业作为样例。这里选取某宣称一直对抗国外APT攻击的头部上市安全企业和某宣称被美方忌惮和制裁的头部云安全企业作为样例。

在看了上述案例和以下国内安全企业的案例后，不知道你会对每年一度的全国性攻防演练持何种看法？

大范围的ATO攻击是用于实战的，而非攻防演练。

“规则”让参与者的安全性看起来很棒！

## **案例9：某头部上市安全企业**

该企业不仅提供众多网络安全产品，还为企业和个人提供大量互联网应用产品和服务。该案例仅以其中某个为企业开放的“移动开发”产品为例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqoDyowYRUKOIEJF9cQ4EI7dWlt2ibAOZ7hF1ricnZ6v1WruHSnIGOftBOglO0Z0A6qjtCDbX8clFcKg/640?wx_fmt=png&from=appmsg)

攻击者可以利用该平台存在的账号接管风险（ATO）获得相关企业用户权限，并进行全部操作，在以下演示中可见，攻击者可轻易获得该企业权限：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqoDyowYRUKOIEJF9cQ4EI7d6tHpVw50g3PiaIN16jynSCkOFK4TQnib22c17xO2s5t7rhvW8VRiaWtWA/640?wx_fmt=png&from=appmsg)

该企业至少有数万用户面临着ATO风险的威胁。

## **案例10：某头部云安全企业**

该头部云安全厂商为政府和企业提供云WAF、抗D、CDN等一系列安全解决方案。但由于其云防御平台存在账号接管（ATO）风险，一旦被攻击者利用，可修改该用户管辖的所有域名的全部安全策略，使再优秀的防御策略也完全失效。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqoDyowYRUKOIEJF9cQ4EI7dSCw9xc0gHFdz1yFvpVCJWq6gxx80CRsWBeUJmvngdfxSHEGx5CEwmQ/640?wx_fmt=png&from=appmsg)

多年前曾经有人问我如何绕过云WAF？其实针对云WAF平台的ATO攻击就是绕过云WAF的技术手段之一。

该企业至少有数百用户面临着ATO风险的威胁。

# **ATO攻击的原理**

从概念上来说，账号接管攻击（ATO）实际上指的是结果，它可以通过各种手段达成，例如：钓鱼、中间人攻击、漏洞、暴力破解、凭据泄露等等。

但当前国外更多的是将其特指通过账号泄露（combolist）引发的一系列后续攻击。近年由于大量始于LOG数据泄露而引发的精准账号泄露数据加之算力的提升和大数据清洗技术的完善，导致ATO攻击效率有了质的提升。

为了区别于二要素（账号/密码），我们将该数据命名为Combolog（由LOG数据清洗出的账号数据）。该类数据需要3个要素：

* n 准确的登录地址（WEB或APP）
* n 唯一的登录名（手机号/身份证/用户名/邮箱）
* n 明文密码

格式如下例所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqoDyowYRUKOIEJF9cQ4EI7dzUhWH1uJT46NTlwl7iatHf77paqbvXhCRNvhiaplUrDCaPE28ktCFmhg/640?wx_fmt=png&from=appmsg)

该数据是如此简单，攻击方式是如此没有技术含量。以至于不懂网络安全的人都能想象得到如何利用它进行攻击。

只有泄露了的账号才会被攻击，那么它们是否只能用来随机进行攻击？无法进行精准攻击？

在多年前，是的。但是当这个数据量达到十亿、百亿量级（去重）时，它就变成了一个可以进行无差别攻击的武器。它在面对以政府或企业为目标时，几乎是最高效的攻击方式（甚至超过0day）。而就在最近一两年，这个数量级的条件已经达成。

并且该攻击手段有一个“致命”的“优点”（对防御者致命，对攻击者是优点）：正常使用情况下，它不会触发任何安全设备的报警！（在有代理池的加持下，它是如此正常且低频的“访问”，而非攻击，你仔细想）这导致ATO攻击成为了一个高效且攻击成本几乎为0的攻击手段。

# **ATO攻击的解决方案**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IE9trzzTPA9rtK0z9qicfgw256rKOMtrFE9wBkibeesfDiayI70gsdq06vK3J3U8VhFUp9TTCLnzmsibnUsow0HV7g/640?from=appmsg)

由于泄露的登录凭据在用户总量中仍属于少数，因此解决方案如下：

**无论是否使用了双因素认证（2FA），都可以使用ATO泄露情报，将泄露的账号进行锁定，在用户再次登录时，要求重新进行身份认证，并要求其修改登录凭据。**

**目前Google、Proton等安全性极佳的企业已自建了账号泄露情报（不仅是HIBP所能提供的情报，实际上在HIBP的数据中ATO情报较少），除了用于提升用户安全性、降低ATO风险外，还为他们的VIP用户提供“暗网报告”增值服务，告知用户，他们的哪些账号和密码在暗网中存在泄露。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Rjg5A263WzAT22BSBt8cb8W6KY4UNqFy0g5XCcDrXEzC8ylT7EFhjmojeZFkqmvdWBBHz0ibaBHN5Cib2xgPxgibg/640?from=appmsg)

以下为Proton（暗网“玩家”最受欢迎、使用率最高、安全性最强的邮件服务商）为其VIP用户提供的安全保护策略，供借鉴：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqoDyowYRUKOIEJF9cQ4EI7dbYZuDppRm7icpxFoLiauwAWHAo7GXjEKry27PlRycYx843OWQOJic0ibkw/640?wx_fmt=png&from=appmsg)

关于企业的用户中，有多少账号存在ATO风险，以及企业内部有多少员工的账号存在ATO风险，可以在下述网站进行免费检测：

**https://darkweb.vc**

同时该网站还提供泄露账号订阅（ATO风险订阅）服务，以下为示例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqoDyowYRUKOIEJF9cQ4EI7dLdOukOIibujAuDAA2p1Kkx568fgbuodWIZViaWyXrJTbibI8BibM6p04dg/640?wx_fmt=png&from=appmsg)

补充说明：为什么双因素认证（2FA）已经不能完全安全需求？

曾经最简单应对ATO攻击的方案是异常登录检测（IP/设备变更或多次登录失败等时触发）+双因素认证（2FA），但是以发展的视角来看，这个方案有其局限性。主要有以下几点：

1. 因为某些主观或客观原因，有的系统无法使用双因素认证（2FA）；
2. 有的双因素认证需要填写身份证或SSN等个人信息，该类信息可能已经泄露；
3. 当双因素认证使用邮箱接收安全码时，该安全邮箱的安全性未必有保障，攻击者可能因此绕过双因素认证；
4. 当双因素认证使用短信码时，有可能会面临短信劫持（虽然成本较高）；
5. 当双因素认证使用人脸识别时，理论上存在AI伪造的可能性；
6. 等等，绕过异常登录检测或双因素认证的方法有很多。

关于异常登录检测和双因素认证绕过的案例，可参考以上提供的部分案例，例如上述的crypto.com、Github等案例。

# **结束语**

零零信安为政府和各类企事业单位提供最专业的暗网监测、数据泄露监测产品和服务，并提供最优质的ATO风险情报服务，合作咨询请扫描以下二维码，联系客服：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqoDyowYRUKOIEJF9cQ4EI7dNgoJdYkibmTjY271Iskw2yoicaPPgGt022V6UdM96kOUcn1fCiaHCwGdw/640?wx_fmt=png&from=appmsg)

— 【 THE END 】—

🎉 大家期盼很久的#**数字安全交流群**来了！快来加入我们的粉丝群吧！

🎁 **多种报告，产业趋势、技术趋势**

这里汇聚了行业内的精英，共同探讨最新产业趋势、技术趋势等热门话题。我们还有准备了专属福利，只为回馈最忠实的您！

👉 扫码立即加入，精彩不容错过！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqPJv9p5ibKIhJXQjWHJmSlibSdib80Llfp8mlV0ibf7m47jyaVeGoFeorddtIuxS5liafTJRKHeSdLnaQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

😄嘻嘻，我们群里见！

更多推荐

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp72VD8Ft2xAxulKkNQzCpMYmic4x...