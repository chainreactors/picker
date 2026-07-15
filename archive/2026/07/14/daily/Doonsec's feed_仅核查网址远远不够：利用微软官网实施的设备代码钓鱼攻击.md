---
title: 仅核查网址远远不够：利用微软官网实施的设备代码钓鱼攻击
url: https://mp.weixin.qq.com/s/weTIK84gE49scv77GgfYOQ
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:45:44.858737
---

# 仅核查网址远远不够：利用微软官网实施的设备代码钓鱼攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5DBHibIELyXB7E9tSI1EQFIwpH8m9lo7fgDn1c9HscDGDD7gUnsmHgJFhtVyibwxJ4ltrr09ZBer5Xs2bx5Ukoyib3BClhK0q8InHzjalYONPM/0?wx_fmt=jpeg)

# 仅核查网址远远不够：利用微软官网实施的设备代码钓鱼攻击

原创

卡巴斯基
卡巴斯基

卡巴斯基威胁情报

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5DBHibIELyXBWxpVR64Xkzympicg9ejlX4vZgyic9jibMibRULTQGvySvSiarJiaemDriaibiakwpHZUPibm7HHN85cM8tasQph1W5QxeZFANnTNFXwomQ/640?wx_fmt=png&from=appmsg)

防范钓鱼攻击最常用的一条建议，就是在输入账号凭证前仔细核对网站域名。通常，具备辨别经验的人一眼就能看出仿冒域名的破绽 —— 这类域名和官方网址至少会有几个字符存在差异。但近期我们监测到一类新型攻击活动：攻击者诱导受害者直接在正规、可信的企业站点中提交信息，该站点即微软身份平台，它支持一项名为设备授权许可的 OAuth 2.0 规范。

这一专属协议扩展功能，初衷是简化智能电视、物联网硬件、打印机等输入受限设备的登录流程，这类设备往往没有完整浏览器或实体键盘。用户可借助身边的手机或电脑，授权上述设备登录自己的账号；完成授权的操作步骤，是在专用验证页面输入一组一次性验证码。当访问https://login.microsoftonline.com/{租户ID}/oauth2/v2.0/devicecode接口发起请求时，微软身份平台会返回验证码以及对应的验证页面链接。利用该机制实施的攻击，就被称作设备验证码钓鱼攻击。

本文将拆解设备授权许可规范（也叫设备授权流程、设备验证码流程）的运行原理，剖析现实中利用该技术发起的真实攻击案例，并梳理可有效抵御设备验证码钓鱼攻击的防护方案。

**设备授权码流程核心步骤**

**1. 请求授权码**

用户在客户端设备打开应用（例如智能电视上的流媒体软件）时，应用检测到当前未完成身份验证，会向地址 https://login.microsoftonline.com/{租户ID}/oauth2/v2.0/devicecode 发送 POST 请求。该请求携带客户端 ID（即在微软 Entra ID / 旧版 Azure AD 中注册应用的唯一标识）与权限范围（申请的访问权限）。

服务端会返回多项参数：设备授权码（服务内部使用的私密编码）、用户验证码（展示给终端用户的短码）、验证地址（用户需访问的登录网址）、有效期（验证码存活时长）、轮询间隔（应用向服务端查询状态的频率）。

**2. 向用户展示验证码**

设备屏幕向用户展示用户验证码与验证网址，引导用户使用另一台设备完成身份核验。以智能电视为例，屏幕会显示验证码和网址，通常还会将验证地址转为二维码，方便用户用手机扫码访问。

**3. 输入验证码并授权访问**

用户使用手机摄像头扫描二维码，或手动输入网址，跳转至验证页面（如 https://microsoft.com/devicelogin），随后输入屏幕上的用户验证码。

**4. 轮询查询服务端授权状态**

智能电视等设备会持续向服务端轮询，确认用户是否已同意授权。设备向令牌接口 https://login.microsoftonline.com/{租户ID}/oauth2/v2.0/token 发送 POST 请求；请求中携带授权类型参数，取值为 urn:ietf:params:oauth:grant-type:device\_code，代表采用设备授权码流程。该参数告知授权服务器当前通过何种认证方式申请访问令牌。

服务端持续等待用户在辅助设备输入验证码并授予资源 / 数据访问权限。在用户完成授权前，服务端会返回两类错误码：authorization\_pending（授权待确认，继续轮询）、slow\_down（降低轮询频率）。

**5. 下发各类访问令牌**

用户成功授权应用后，服务端向设备下发令牌：访问令牌（用于调取业务数据）、刷新令牌（后续免登续期权限）、身份令牌（包含姓名、邮箱等用户个人信息），同时附带其他业务参数。

**6. 自动续期访问权限**

智能电视等设备可凭借刷新令牌静默更新访问令牌，无需用户重复操作。当前访问令牌过期（通常有效期 1 小时）时，设备自动携带刷新令牌向令牌接口发起续期请求，获取全新的访问令牌与刷新令牌，实现无感持续登录。

这套流程对缺少完整输入键盘的设备十分便捷，但攻击者可利用该机制劫持用户账号，并借助刷新令牌实现长期持久非法访问。下文结合真实场景拆解该攻击路径。

**设备验证码钓鱼攻击分析**

![](https://mmbiz.qpic.cn/mmbiz_png/5DBHibIELyXA4C5K1lW9LcJaibevDEZXCKX0VrlalDIic8oWic8CfPyOCVbl6HY9XFAeg7ev3atYjlXzvwvicNbHicibsIbBW0JBmsYmsv31ebkBa0/640?wx_fmt=png&from=appmsg)

**钓鱼邮件**

在我们监测到的一场 2026 年 4 月初至 5 月中旬持续开展的钓鱼攻击活动中，攻击者发送的初始邮件伪装成律所通知，邮件内附带一份设置了密码保护的 PDF 文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5DBHibIELyXBBApMMmP2mFVrWPqvEly2Nia7d36FibAic7XlISUA7oafwOb3SOt40rwZv5iclObI74XF67EOLZJoh0zuLnwDgITjWqEUknIAEQFI/640?wx_fmt=png&from=appmsg)

受害者打开该PDF并输入密码后，页面会跳转至一个落地页，上面罗列了多份文件。但想要查看这些文件，必须点击页面提供的链接。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5DBHibIELyXBIXpoKxjSW1qoEpHal6QUa2fOxc765y9Sxib1TvMaGVguiaUtzy0Z8Hl91pIMIwAJKbtgoCLibELdRHPvicYXia7cBvG1rfIGZFDKk/640?wx_fmt=png&from=appmsg)

包含恶意链接的 PDF 文件

仔细查看目标网址可以发现，该链接并未指向常见、易于识别的钓鱼域名，而是跳转至微软官方合法地址。但网址内的参数经过特殊配置，会将用户重定向至钓鱼页面。

![](https://mmbiz.qpic.cn/mmbiz_png/5DBHibIELyXDthK9KPlMYrem6HcnB0RKpWgGic48CrZcmXImGic4tRdxCnhXItWOKSic0qwVDVrgUfC9UM0UVBpDETLVK0ibA3pv4hZPwNTvKrhg/640?wx_fmt=png&from=appmsg)

文档内的链接不会将用户留在微软平台，而是会立即跳转至仿冒企业法务门户的钓鱼页面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5DBHibIELyXBKULxTyVoyFhdELTAiaEazo42rWzO9yHGjUC1go8fK7jwZf54otiaBiaIcc5wumOWmbKMWNWISrmFNh199EsRWzfiabmk8M7GRj5c/640?wx_fmt=png&from=appmsg)

钓鱼页面

值得一提的是，该落地页面设置了多道验证码验证环节，推测是用来拦截各类安全扫描爬虫。用户完成全部验证后，会跳转至最终页面，页面提示用户复制一次性授权码。该串代码即为用户验证码（user\_code），攻击者服务端程序早已通过请求接口 https://login.microsoftonline.com/{tenant}/oauth2/v2.0/devicecode 获取到该验证码，完整流程上文已有详述。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5DBHibIELyXDRbjBHSTVRv2bpWLgNp2XxFJ7hTGcSDulKU7GDhlT3m4Yljgibrt3GnNPE2yYjkPWSSHGWsvzC45EsrUV0no4ZWgWh7CzYy9kY/640?wx_fmt=png&from=appmsg)

一次性验证码

点击页面显示的一次性验证码后，该验证码会自动复制至剪贴板，同时页面将跳转至微软官方正规身份验证页面（验证地址），提示用户粘贴并输入该验证码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5DBHibIELyXA4aUbXNZ50MBMy3s7DmIkvYYhJ2BB9PMAbDiagdHzWic7MuvYZqZLPH6zK3s1ravEmdJwxecW9DT2CBNJ9dWtYlWFhgC3o6G1YE/640?wx_fmt=png&from=appmsg)

微软官方身份验证页面

用户输入验证码后，系统便启动前文所述的设备授权码流程。毫无防备的受害者随即在微软官方页面完整完成多因素认证流程。认证一旦通过，攻击者就会窃取该会话的访问令牌、刷新令牌与身份令牌。借此，攻击者可查看、发送受害者邮箱内的邮件，窃取 OneDrive 中的文件，并访问 Teams 聊天记录。

攻击手段的适配调整

本次钓鱼活动波及范围有限，持续时长仅一个多月。但该威胁组织仍在持续活跃运用此类攻击手段，并针对特定地域进行适配改造。近期我们监测到多套经过小幅改动的设备授权码钓鱼攻击，攻击重点已转向巴西等地的用户群体。

![](https://mmbiz.qpic.cn/mmbiz_png/5DBHibIELyXAZqGUWdpdwhuh2onRqCJUDmxJOnH5j9bxmH6xYOgT9wibrwwDvyQuyTF1OvLYggibIRSCatg4yapvqD5wGVVCdGwkUCqCUbVWec/640?wx_fmt=png&from=appmsg)

巴西钓鱼邮件变种

（葡萄牙语原文译文）

“您好！

您的订单已完成处理，确认单已以 PDF 文件形式发送给您，详情见下文。

打开 / 下载 PDF

本邮件附有一份新报价单。

如需其他帮助，请告知我。”

与此前钓鱼攻击活动不同，该邮件并未附带恶意 PDF 附件，而是内嵌了指向cacoo.com的链接。Cacoo 是 Nulab 公司旗下正规在线绘图平台。和以往手段一致，攻击者利用这个可信域名做开放跳转，引导用户访问钓鱼服务器。

代理链接先经由正规网站Cacoo.com域名跳转，再重定向至钓鱼网站。

（葡萄牙语原文译文）

请求确认

状态码 = 操作成功

下载或查看文件

重要提示：请使用接收本邮件的账号登录，完成文件安全核验。

用户点击链接后，页面会跳转至常见登录页，并展示一次性验证码。

![](https://mmbiz.qpic.cn/mmbiz_png/5DBHibIELyXCWNKbo86vCAkGCDr7fxIrqIFjb94LHAXwicsQCWJrKYQQ7CYll04szGrehN94UudhyHMSECVfFWjFWbpia4fKuPWpFR1zhG0Iks/640?wx_fmt=png&from=appmsg)

展示授权验证码的落地页面

潜在受害者会从该页面再次跳转至微软官方门户，完成设备授权码流程的身份验证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5DBHibIELyXBicjuSDDl6wZTvDoVdoibAzjplqHhfkicckb0GNqyJuf00MMficSRmkRR1ueETEiboNEU0hP8wj5w9Kkv1yRdicmTZoqshn6EXkWgfc/640?wx_fmt=png&from=appmsg)

提示输入用户授权码的微软官方页面

**抵御设备码钓鱼攻击的防护方案**

研究表明，网络威胁分子并非只能通过窃取账号凭证、植入恶意程序来窃取敏感数据，正规授权工具同样会被他们改造利用。因此，用户不仅在访问可疑网站时要提高警惕，在微软、Cacoo 官网这类正规平台操作时也需多加防范。

用户防护建议：

1. 若你本人并未通过微软设备授权码流程在外部设备发起登录请求，切勿通过该授权申请。
2. 切勿在收到陌生邮件、短信后输入其中附带的授权码，即便链接显示跳转至微软官方域名也不行。
3. 攻击者常利用正规域名的开放跳转漏洞，在网址问号后拼接redirect\_uri、return\_url、next等跳转参数，诱导用户跳转至恶意页面。点击链接前，将鼠标悬停在链接上查看主域名与可疑跳转参数；页面加载完成后，核对最终网址是否为官方地址 —— 输入企业账号密码前，这是最基础的安全操作。

我们强烈建议企业运维团队评估自身业务是否需要启用设备码授权流程。若日常办公无需该认证方式，应通过微软 Entra ID 的条件访问策略全局关闭该功能。同时安全团队需单独监控设备码登录事件，严格管控设备合规状态，并针对异地异常登录行为配置告警机制。

企业若要搭建完整的设备码钓鱼防御体系，需部署专业邮件安全防护工具，同步防护企业邮箱与员工个人通信渠道。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5DBHibIELyXDFxbcaywTiagTPo0sQhdZq1cOLSvM5uHv2dh65nWjwVliaaoDdUNEDwPZthhMO0ib1cqCHlb613acCP768fpfzn1nDXaibeQMwNqE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5DBHibIELyXCah5IRNjk9zHOKZbx80DibicMPy8WmiakxYmljMQmzFUF8IRQerJydCH6EL5b5IdH0g7Seibsr1Viafic32bopxn5d7NlyCn076syAU/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/BscvC1hbNBeSmiaUVZgOGDgO90z283FHJJEFDSgcic66vuFibgIKkCKTo1EmvYFUl1uVoPaO0o9AEv6j1Sm8IdcBQ/0?wx_fmt=png)

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