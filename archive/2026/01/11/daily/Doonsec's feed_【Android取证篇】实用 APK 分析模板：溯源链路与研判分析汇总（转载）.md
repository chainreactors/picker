---
title: 【Android取证篇】实用 APK 分析模板：溯源链路与研判分析汇总（转载）
url: https://mp.weixin.qq.com/s/3xBspxVdP2HNwQra_aBVQw
source: Doonsec's feed
date: 2026-01-11
fetch_date: 2026-01-12T03:35:57.887743
---

# 【Android取证篇】实用 APK 分析模板：溯源链路与研判分析汇总（转载）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cTMnmj6uIq1JkbrpDibZh5UkwiaPU9KJIfF3a1kicMkFuOhib5M3uErd63WQhy077Z4aQHuyR55ql7uPq1w72rrfkg/0?wx_fmt=jpeg)

# 【Android取证篇】实用 APK 分析模板：溯源链路与研判分析汇总（转载）

DFIR蘇小沐

![]()

在小说阅读器中沉浸阅读

编者荐语：

整理的很全，推荐

以下文章来源于凌风小屋
，作者凌风

![](http://wx.qlogo.cn/mmhead/SCug0ESSOHicsU5FbIA1iaoytdrJSGcvRiayW0oA4x7zIKHqzwxTwr7SSa21zbXy3Skudp4J7wW1Wk/0)

**凌风小屋**
.

专注于电子数据取证领域创作和分享

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/cTMnmj6uIq3uP0qrBnshO1sYwfGhVDv9Vv5hEBnR35Lb3xoqowUSTicGFuYWSfrd72hy0GMhnLOQoAFDVU8oTKA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/cTMnmj6uIq3uP0qrBnshO1sYwfGhVDv9ThJsjEyahFXBia7r2icSFnwyt7bLYhcQx88ibJh5yJnRkf9puffTFo3fg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

关注公众号 一起交流进步

这模板的设计思路特简单：就是想让大家“能用、好用、还能互相核对”，把APK那些绕人的技术特征，变成一个个“勾√项”，让分析从“靠老师傅凭感觉”，变成“按说明书走流程”——稳得很，还不费脑子！

为啥得搞个“标准模板”？

在日常工作中，很多朋友问我分析APK有没有模板，他们

有的懂分析技术但是不清楚要分析的具体有哪些，恐有遗漏；

有的还没有掌握分析技术，感觉学的云里雾里，不知所措；

要么就是“磨洋工”——每个人查的思路都不一样，跨团队协作跟“鸡同鸭讲”似的，重复沟通能把人烦死。

而这模板的作用就是来救场的，它把APK分析拆成了固定的“查岗清单”，从“先搞清楚这APP是谁家的”到“揪出它有哪些坏心眼”，一步都不落下——既保证了啥风险都逃不掉，又能让所有人按同一套逻辑干活，不用再重复干活。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cTMnmj6uIq1JkbrpDibZh5UkwiaPU9KJIfFZw5pax1j4Se7EXArE05TRXO1ZP05F9n48Cc0M8xOatuCeUBANfFJg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/cTMnmj6uIq1JkbrpDibZh5UkwiaPU9KJIficFQyxvYqicPBN8VENzIRUSy8DIAt4kmaX06rSMu57o4VB5bUGvoODWw/640?wx_fmt=gif&from=appmsg)

二维码获取

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/cTMnmj6uIq1JkbrpDibZh5UkwiaPU9KJIfiaH8P7fJR4jDmia2dgrJ5R10vrBjkFrFanaTAaDslh1BMfccfFGHtk1Q/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cTMnmj6uIq1JkbrpDibZh5UkwiaPU9KJIfNaQv8iaLMGhQbS7vcGB6jpFe1QzKIprgx7dKhYw72LHVM1wTNozmrTw/640?wx_fmt=png)

APK 传播链路追踪：通过解析二维码，还原从 “扫码入口” 到 “APK 下载” 的完整路径，可用于定位违规 / 恶意 APK 的分发渠道。

①二维码解析工具：“草料二维码转码器” 是在线二维码解析工具，用于提取二维码包含的链接信息；

②跳转网址：二维码对应的直接访问链接（http://XXX.com/1234），是用户扫码后的初始跳转入口；

③下载网址：分发平台提供的 APK 具体下载链接（http://XXX.com/download），是用户获取 APK 的最终地址。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/cTMnmj6uIq1JkbrpDibZh5UkwiaPU9KJIficFQyxvYqicPBN8VENzIRUSy8DIAt4kmaX06rSMu57o4VB5bUGvoODWw/640?wx_fmt=gif&from=appmsg)

包名信息

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/cTMnmj6uIq1JkbrpDibZh5UkwiaPU9KJIfiaH8P7fJR4jDmia2dgrJ5R10vrBjkFrFanaTAaDslh1BMfccfFGHtk1Q/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cTMnmj6uIq1JkbrpDibZh5UkwiaPU9KJIfh6fVCv3ksibkePcKGuygTXAXBFhd05kWu7ZpWNlFibMOLemrTffnornQ/640?wx_fmt=png)

包名通常遵循 “反向域名” 规则（如开发者官网为xxx.com，包名多设为com.xxx.应用名），是 Android 应用的唯一标识，模板记录的包名可关联应用商店的开发者注册信息（如开发者姓名、企业主体），直接缩小人员范围；包名的一致性可以用于串并案。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/cTMnmj6uIq1JkbrpDibZh5UkwiaPU9KJIficFQyxvYqicPBN8VENzIRUSy8DIAt4kmaX06rSMu57o4VB5bUGvoODWw/640?wx_fmt=gif&from=appmsg)

签名信息

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/cTMnmj6uIq1JkbrpDibZh5UkwiaPU9KJIfiaH8P7fJR4jDmia2dgrJ5R10vrBjkFrFanaTAaDslh1BMfccfFGHtk1Q/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cTMnmj6uIq1JkbrpDibZh5UkwiaPU9KJIfB8jictwkLdTSibmCysvxvJNibMhjtvhbcUIkQW76xCIeWxfkqcibEicpk4g/640?wx_fmt=png)

通过 APK 签名证书的指纹（如 SHA256），在应用商店 / 开发者平台反向查询绑定的企业信息（如 Google Play 后台需绑定企业开发者账号，可关联工商信息）。另外通过“企查查”等可以查到该公司开发的其他APP，对比是否有关联。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/cTMnmj6uIq1JkbrpDibZh5UkwiaPU9KJIficFQyxvYqicPBN8VENzIRUSy8DIAt4kmaX06rSMu57o4VB5bUGvoODWw/640?wx_fmt=gif&from=appmsg)

开发者信息

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/cTMnmj6uIq1JkbrpDibZh5UkwiaPU9KJIfiaH8P7fJR4jDmia2dgrJ5R10vrBjkFrFanaTAaDslh1BMfccfFGHtk1Q/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cTMnmj6uIq1JkbrpDibZh5UkwiaPU9KJIfeQO4Ckw8xxR0zzvu6BVboJp5tWZ0PbjhM8libX3juRiaCh4GxHM7R9bQ/640?wx_fmt=png)

AndroidManifest.xml 文件中可能包含开发者官网（android:website属性）、开发者邮箱 / 电话（android:email/android:phone）；示例：<application android:label="XX应用" android:website="https://www.xxx.com">。或者直接整个文件中搜索“http”或“https”定位网址。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/cTMnmj6uIq1JkbrpDibZh5UkwiaPU9KJIficFQyxvYqicPBN8VENzIRUSy8DIAt4kmaX06rSMu57o4VB5bUGvoODWw/640?wx_fmt=gif&from=appmsg)

第三方SDK

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/cTMnmj6uIq1JkbrpDibZh5UkwiaPU9KJIfiaH8P7fJR4jDmia2dgrJ5R10vrBjkFrFanaTAaDslh1BMfccfFGHtk1Q/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cTMnmj6uIq1JkbrpDibZh5UkwiaPU9KJIfX49H2n1y7VyXjtyzHEcurW9aSKokiazPWOrbqNWmRLC9a4etuMB9ulA/640?wx_fmt=png)

第三方 SDK 大致分为 “正常功能类 SDK” 与 “恶意 SDK” 两类。

①正常功能类 SDK（定位、推送、支付、统计），SDK调用第三方服务的授权标识：对应的开发商（如 XX 科技有限公司）、API 凭证（如API\_KEY、API\_id），借助记录的开发商与 API 信息，向 SDK 的官方开发商调证。

②恶意 SDK（短信轰炸、非法支付、非法采集隐私），这类 SDK 本身属于违规 / 违法工具，核心关注点是其恶意功能而非授权信息。通过技术手段（如 SDK 的代码特征、网络请求链路）追踪其开发者的真实身份。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/cTMnmj6uIq1JkbrpDibZh5UkwiaPU9KJIficFQyxvYqicPBN8VENzIRUSy8DIAt4kmaX06rSMu57o4VB5bUGvoODWw/640?wx_fmt=gif&from=appmsg)

加固识别

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/cTMnmj6uIq1JkbrpDibZh5UkwiaPU9KJIfiaH8P7fJR4jDmia2dgrJ5R10vrBjkFrFanaTAaDslh1BMfccfFGHtk1Q/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cTMnmj6uIq1JkbrpDibZh5UkwiaPU9KJIfdYlickFYOXhuyoCOuaFibnU2TWZD4Mx4xVKW7qMFhoECWiaO93S51S7oA/640?wx_fmt=png)

“360 加固、爱加密、梆梆加固” 是国内主流的商业 APK 加固工具 —— 这类工具通过代码混淆、加密、加壳等方式，防止 APK 被轻易反编译，保护应用代码不被泄露。处置方法有：

①通过 “FDEX”（一种 APK 脱壳工具）对加固后的 APK 进行 “脱壳” 操作，可提取其原始源码，进而还原应用的业务逻辑。

②向加固服务提供方调证该 key/id 对应的授权主体、服务协议等信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/cTMnmj6uIq1JkbrpDibZh5UkwiaPU9KJIficFQyxvYqicPBN8VENzIRUSy8DIAt4kmaX06rSMu57o4VB5bUGvoODWw/640?wx_fmt=gif&from=appmsg)

服务器地址查询

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/cTMnmj6uIq1JkbrpDibZh5UkwiaPU9KJIfiaH8P7fJR4jDmia2dgrJ5R10vrBjkFrFanaTAaDslh1BMfccfFGHtk1Q/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cTMnmj6uIq1JkbrpDibZh5UkwiaPU9KJIfBZkkCl1S0EvE9qUDs74qiaLPOy5icRNib1FQnDCzibApsvicjrqgx7Nk1ag/640?wx_fmt=png)

针对不同部署形式，操作方式大致有两种：“IDC 机房→实地排查 + 现场固定”和“云服务器→调证”。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/cTMnmj6uIq1JkbrpDibZh5UkwiaPU9KJIficFQyxvYqicPBN8VENzIRUSy8DIAt4kmaX06rSMu57o4VB5bUGvoODWw/640?wx_fmt=gif&from=appmsg)

IP查询

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/cTMnmj6uIq1JkbrpDibZh5UkwiaPU9KJIfiaH8P7fJR4jDmia2dgrJ5R10vrBjkFrFanaTAaDslh1BMfccfFGHtk1Q/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cTMnmj6uIq1JkbrpDibZh5UkwiaPU9KJIfB6TLbcDYLWyqWqYYNAiblRxUUEQ0q4sVJiaXRaNVvpA5KFtxnNI7eKrQ/640?wx_fmt=png)

“IP138” 在线查询：通过 IP138 这类 IP 信息查询工具，可直接获取 IP 的地理位置、历史绑定域名、运营商等基础信息，是服务器信息溯源的常用工具

①真实 IP：服务器的实际网络地址（示例为178.251.XXX.321），是服务器在网络中的唯一标识，也是后续调证的核心依据；

②服务器地址：IP 对应的物理地理位置（示例为 “中国江苏 XX”），反映服务器的部署区域，辅助判断业务的服务覆盖范围；

③IP 历史绑定域名：该 IP 曾关联的域名及对应时间区间（如2021-01-01----2022-01-01 XX.XXX.com），可溯源服务器曾承载的业务，辅助关联目标其他业务资产；

判断是否存在宝塔面板：通过访问IP:8888端口，验证该服务器是否部署了宝塔面板（若能进入面板登录页，则说明存在），这是服务器管理工具的存在性检测手段，若有可以去宝塔面板公司进行调证注册信息等。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/cTMnmj6uIq1JkbrpDibZh5UkwiaPU9KJIficFQyxvYqicPBN8VENzIRUSy8DIAt4kmaX06rSMu57o4VB5bUGvoODWw/640?wx_fmt=gif&from=appmsg)

域名Whois信息

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/cTMnmj6uIq1JkbrpDibZh5UkwiaPU9KJIfiaH8P7fJR4jDmia2dgrJ5R10vrBjkFrFanaTAaDslh1BMfccfFGHtk1Q/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cTMnmj6uIq1JkbrpDibZh5UkwiaPU9KJIficMj2ealx3rgGKCugicu8maf5pY61K1A4axwnFk140wjgibUbDD7Xh9oA/640?wx_fmt=png)

“站长工具”“微步在线” 是常用的 Whois 信息查询平台：通过这类工具，无需直接访问域名注册商后台，即可快速获取域名的 Whois 信息、DNS 配置等内容，是域名资产调研的常用手段

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/cTMnmj6uIq1JkbrpDibZh5UkwiaPU9KJIf1Pygyd0iaLiaqrqyjDnruMrw2HbOoVQDCxXvKgVMib4tcJVlyUfP1VMoQ/640?wx_fmt=gif&from=appmsg)

Whois 信息（域名注册核心信息）Whois 是域名的官方注册信息，包含域名的全生命周期与管理信息：域名：目标域名本体（如XXX.com）；注册商：负责该域名注册、管理的服务机构；联系邮箱 / 电话：域名管理者的联系方式；创建 / 过期时间：域名的注册生效时间与到期时间，决定域名的可用周期；域名服务器：管理该域名解析记录的服务器地址。DNS：域名的解析服务器地址，决定域名请求的解析路径。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/cTMnmj6uIq1JkbrpDibZh5UkwiaPU9KJIficFQyxvYqicPBN8VENzIRUSy8DIAt4kmaX06rSMu57o4VB5bUGvoODWw/640?wx_fmt=gif&from=appmsg)

域名ICP备案号

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/cTMnmj6uIq1JkbrpDibZh5UkwiaPU9KJIfiaH8P7fJR4jDmia2dgrJ5R10vrBjkFrFanaTAaDslh1BMfccfFGHtk1Q/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz....