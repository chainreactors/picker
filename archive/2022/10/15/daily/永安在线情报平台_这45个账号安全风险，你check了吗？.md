---
title: 这45个账号安全风险，你check了吗？
url: https://mp.weixin.qq.com/s?__biz=MzI3NDY3NDUxNg==&mid=2247494521&idx=1&sn=07a0cd6080cd0ee4b499bf100498b1c6&chksm=eb12cd42dc6544543d69e64dce671845fbf1d9b79460f331db3ee98663f5d28fc653df300442&scene=58&subscene=0#rd
source: 永安在线情报平台
date: 2022-10-15
fetch_date: 2025-10-03T19:57:45.837103
---

# 这45个账号安全风险，你check了吗？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/4mAgZtBianqF4bvbzskZ44Su5ibPjFObyRshG3ejcmcd4qybnZO54cMuw1sxvzQSUNqOlJD30dVJVovB7HqnPEZg/0?wx_fmt=jpeg)

# 这45个账号安全风险，你check了吗？

原创

永安在线

威胁猎人Threat Hunter

![](https://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqHJGmTgK1IkdGenlrsehnKe61VhicFG0G5lEPxtqmdyOjtsLNHfq998Mv1SvZzYufxKKmOAgvxibRyA/640?wx_fmt=png)

信息化时代，大部分平台都需要通过账号登录才可体验更多功能，近些年为方便用户操作，平台演变出了扫码登录、第三方授权登录等多种登录方式，同时也为攻击者打开了更大的攻击面。

**账号****包含着各种重要信息**如个人手机APP账户、网站账户、银行卡账户密码等，是黑产眼中的“香饽饽”。

永安在线情报平台监测过多起**黑产利用账号缺陷发起规模攻击**，如扫号攻击、撞库攻击、盗号登录等，最终**达到窃取敏感数据、资金盗取、网络诈骗、薅羊毛等目的**。因此，加强账号安全管理，是企事业单位业务和数据安全保障的第一道屏障。

为此，猎人君为大家梳理了**45个账号安全风险点**，方便大家在账号安全管理中**查缺补漏**，从而建立更加全面的账号安全体系。

![](https://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqF4bvbzskZ44Su5ibPjFObyRAUnJnVhYt7iclolnQZ4c7SkIndO7qQYHCRSXuUrTvib3lfxKl9FCLOSg/640?wx_fmt=png)

**下文将****结合永安在线情报平台捕获到的攻击案例**，**对不同安全场景和凭证中45个安全风险逐一分析：**

**按照不同场景分析**

**密码登录场景**

**账号相关**

***1.*****账号可枚举**

//

**危害性：**低

**普遍性：**高

**可利用性：**高

**通过响应体的内容可以判断账号在系统中是否存在，拿到存在的账户后可进一步发起撞库/爆破攻击，提高攻击效率。**

例如该接口会对不存在的用户名返回“用户名不存在”，可利用这个提示来枚举账号。

![](https://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqEaed7OFgVFgYldL33TpKtz0CMSMOBa2Ejc9jdQBv4IHvCFvaXMMGDMxjqKWWUSyia1eLiabMf10kXg/640?wx_fmt=png)

***2.*****默认账号**

//

**危害性：**低

**普遍性：**高

**可利用性：**高

**很多系统都会有默认的账号，比如很多管理后台都会有个admin账号**，这样攻击者即使无法枚举账号在系统中是否存在，也可以尝试对默认账号发起攻击。

**密码相关**

***3.*****撞库**

//

**危害性：**高

**普遍性：**中

**可利用性：**中

一般情况下，用户会用一个手机号或邮箱在多个平台上注册账号，为了方便记忆，**密码可能会设置成一样的**。当某些平台的用户数据泄露了，**攻击者就会拿泄漏的账号密码去别的平台尝试登录**。比较常见的有游戏行业的「撞库攻击」，游戏账号的价值比较高，对攻击者来说可获取高额利润。

永安在线情报平台曾捕获过多起黑产贩卖撞库成功得来的账号信息：

![](https://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqEaed7OFgVFgYldL33TpKtzszA5RYGuNqhSafyCatVwmBJWIOIYiap1gibALq6E75XkQBhzzFhZRvwA/640?wx_fmt=png)

***4.*****钓鱼**

//

**危害性：**高

**普遍性：**高

**可利用性：**中

攻击者通过准备一个和官方平台基本一样的登录页面（域名不同）或礼品领取、抽奖的页面等，引诱受害者输入账号密码。攻击者通过这种方式**可****直接获取到受害者的明文账号密码**。

***5.*****弱密码**

//

**危害性：**高

**普遍性：**高

**可利用性：**高

「弱密码」没有一个明确的定义范围，任何可能被猜解出来的密码都可以被称为弱密码。常见的弱密码123456，像dingdang2022、dingdang.com、dingdang@2022也可被称为弱密码。**攻击者通过常见的弱密码以及收集目标的相关信息，组合起来生成密码进行爆破。**

例如某个管理后台存在弱密码，域名为pass\*\*\*\*.cn，通过爆破就得到账号密码为pass\*\*\*\*、pass\*\*\*\*2016。

***6.*****万能密码**

//

**危害性：**高

**普遍性：**低

**可利用性：**高

「万能密码」指的是用什么密码都可以登录系统，**是因为登录接口存在SQL注入漏洞造成的**。

例如输入账号admin密码123456，后端会执行的SQL语句大概为：

SELECT \* FROM user WHERE username='admin' AND password='123456'

如果存在SQL注入漏洞，攻击者可以构造语句，输入账号admin' # ，输入任何密码，后端会执行的SQL语句就变为：

SELECT \* FROM user WHERE username='admin' #' and password='123456'

这里通过#注释符把后面查询密码的语句注释掉了，校验账号密码的逻辑就失效了，实现万能密码登录。

***7.*****密码明文传输**

//

**危害性：**高

**普遍性：**中

**可利用性：**低

密码在提交到服务器的过程中，**没有进行加密处理**，攻击者可通过中间人攻击的方式获取到明文密码。

***8.*****密码在URL中**

//

**危害性：**高

**普遍性：**低

**可利用性：**低

如果一个登录请求会**把账号密码写在URL中**，即把密码暴露在浏览器的地址栏上，或可能会被浏览器、安全软件给记录下来。如果包含密码的这个URL，是个HTML，HTML上又会加载JS、CSS等第三方的资源文件，那在请求这些第三方文件的时候，就会通过Referer把密码泄漏了。

![](https://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqEaed7OFgVFgYldL33TpKtzUxPYGJ2Dk6pg9wArjxBX2vIiap2lNEnIvC6RN4cHGm7oZOG6AyMGRGg/640?wx_fmt=png)

***9.*****密码明文存储**

//

**危害性：**高

**普遍性：**低

**可利用性：**低

用明文存储密码有很大的安全隐患， 一般数据库里还存有用户的姓名、手机号、用户名等信息，一旦数据库发生泄漏，再加上用户的明文密码，攻击者就可以用账号和密码去其他网站尝试登录。因为用户往往会根据习惯**将多个网站的密码成一样**的，跟前面提到的撞库攻击存在的问题一样。

***10.*****API泄露密码**

//

**危害性：**高

**普遍性：**低

**可利用性：**高

因为开发人员的疏忽，**A****PI接口可返回用户的所有字段（包括密码）的信息**，攻击者就可轻易获取到用户的密码。

![](https://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqEaed7OFgVFgYldL33TpKtzRdUyHFcQpibXy3Dqy2FIBtw2mpLBIj768DqRKSD0rzJhzJAAq3beBlQ/640?wx_fmt=png)

**验证码相关**

***11.*****图形验证码失效**

//

**危害性：**低

**普遍性：**低

**可利用性：**高

常见的让图形验证码失效的方式有**把验证码参数值填空，或者验证码参数删掉**。

如下案例就是直接把验证码参数删除，验证码失效，不再返回验证码错误。

![](https://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqEaed7OFgVFgYldL33TpKtzyc0V4Q3jyMwmVHN97aspLcSPuacicyznCibFPDfI0Kjqt5lRxJ0U8alQ/640?wx_fmt=png)

***12.*****滑块验证码失效**

//

**危害性：**低

**普遍性：**低

**可利用性：**高

最常见的滑块验证码是通过SaaS接入的，但为了避免第三方服务器出问题影响业务的正常运营，**通常会提供一个宕机模式****（即第三方服务器出问题时可不用进行滑块验证码）**，攻击者利用这一点就可以让滑块验证码失效。

如下是在请求中添加了个"xx\_server\_status":0，让服务端以为第三方服务宕机了，就不用进行滑块验证了，从而绕过了滑块验证。

![](https://mmbiz.qpic.cn/mmbiz_jpg/4mAgZtBianqF4bvbzskZ44Su5ibPjFObyR7ZsxCj5Bk9mx8mGiapMylADohCE6e6gxBHxvicvIKaPtelZhbDETwXsQ/640?wx_fmt=jpeg)

***13.*****不同端验证码策略不一致**

//

**危害性：**低

**普遍性：**低

**可利用性：**高

平台可能对一套系统开发了PC网页版、移动网页版、APP等，在不同端上验证码的策略可能不同。比如在PC网页版的登录接口是有验证码的，换到APP可能就没有验证码了，攻击者就可利用APP的接口来发起攻击。

***14.*****验证码可复用**

//

**危害性：**低

**普遍性：**低

**可利用性：**高

「验证码可复用」即**验证码使用多次不失效**，利用这个缺陷来绕过验证码发起攻击。

永安在线情报平台就捕获过多起攻击者利用验证码可复用的漏洞进行扫号攻击。如下图，攻击者多次请求都是使用的同一个验证码，并且都请求成功。

![](https://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqEaed7OFgVFgYldL33TpKtz2g3zusRGjZjk1XibXXM0PKlYfWYNMqJdQZm6nGc7GRVeeqZCFDWX2kA/640?wx_fmt=png)

***15.*****使用老接口**

//

**危害性：**低

**普遍性：**高

**可利用性：**中

平台开发了新的接口，但是老的接口可能没下线，这类老接口很容易被攻击者利用。

下图是永安在线情报平台捕获的一个攻击事件，平台在页面上显示的是中文验证码：

![](https://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqEaed7OFgVFgYldL33TpKtzbGVjcOa9ic11GjlJZ3X5aa00wXbYpjlaeSLIEFT2SQ1tEibSrWxic5TDg/640?wx_fmt=png)

但从永安在线情报平台流量中看到，攻击者请求中的验证码都是英文数字，并非中文验证码。

![](https://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqEaed7OFgVFgYldL33TpKtzXIRaFqYv9x2uElamtMiaHBwgXxpykek1Sl08mQSfH0pvzmqECqqhwIg/640?wx_fmt=png)

通过分析得出应该是平台新接口升级了验证码为中文验证码，但老的接口还能继续使用英文数字验证码，攻击者正是利用这一漏洞对老接口发起攻击。

**短信验证码场景**

***16.*****验证码位数过短**

//

**危害性：**高

**普遍性：**中

**可利用性：**高

如果短信验证码是纯数字的，位数又比较短（小于等于4位），攻击者很容易把验证码爆破出来。

下图所示是一个短信验证码登录接口，对手机号为13888888888的短信验证码进行爆破，可实现任意用户登录。

![](https://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqEaed7OFgVFgYldL33TpKtzH3HicH5QNQltrSwibr0GNYiaymA1JfDLL9JrYwIM9SOCCGtFZcLCWbU5A/640?wx_fmt=png)

***17.*****验证码有效期过长**

//

**危害性：**中

**普遍性：**低

**可利用性：**低

6位纯数字的验证码爆破的成本比较高，一共有一百万个数字需要爆破，耗费的时间会非常长。但如果验证码的有效期比较长，比如1小时甚至更久，还是存在被爆破的风险。

如下案例，某接口登录使用的是6位验证码，有效期超半小时，案例中的验证码是0开头的（运气比较好），所以比较快地爆破出了验证码为064716。

![](https://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqEaed7OFgVFgYldL33TpKtzNzdzG6W0YbxmakYHE1rXmpMrFaNE1tCbfk4SmGgha3PGZVHhNODXUw/640?wx_fmt=png)

***18.*****验证码在响应中泄露**

//

**危害性：**高

**普遍性：**低

**可利用性：**高

**发送短信验证码的接口，有可能在其响应体/响应头中泄漏了验证码。**如下案例所示，某教育类APP发送验证码的API接口，在响应体中泄漏了验证码，和客户实际收到的短信验证码一致，攻击者可利用该漏洞实现任意用户登录/注册等操作。

![](https://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqEaed7OFgVFgYldL33TpKtz5dAicSK3MGt8jVFh2k4mTlo67o42b4X1PtNhkjFNy9ZeSHjsLohuT9A/640?wx_fmt=png)

***19.*****验证码由客户端生成**

//

**危害性：**高

**普遍性：**低

**可利用性：**高

在发送短信验证码的接口，也**有可能****由客户端来生成验证码，然后给到后端来发送短信验证码**，相当于可以自己指定手机号的验证码，攻击者可利用该漏洞实现任意用户登录/注册等操作。

***20.*****测试验证码未删除**

//

**危害性：**高

**普遍性：**低

**可利用性：**中

在应用上线前，开发人员可能为了方便测试，设置了测试专用的验证码（如0000、1111、2222等），输入该验证码即可完成登录/注册等操作。**在应用上线后可能未删除该验证码**，攻击者可利用测试验证码实现任意用户登录/注册等操作。

***21.*****验证码与手机号未绑定**

//

**危害性：**高

**普遍性：**低

**可利用性：**高

在短信验证码登录的场景下，后端校验验证码是否正确时，**没有验证验证码与手机号的关系**，仅仅校验验证码是否为有效期内下发过的验证码。**攻击者可利用自己的手机号接受短信验证码，实现任意用户登录/注册等操作。**

**扫码登录场景**

***22.*****扫码授权登录CSRF**

//

**危害性：**高

**普遍性：**低

**可利用性：**中

扫码登录的流程大概如下：

![](https://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqEaed7OFgVFgYldL33TpKtzniaKeWKCtiaNLsYKgsiaypJrvgVDjnicagszEdgBRE99OKCmoB9UKY6DOA/640?wx_fmt=png)

有些后端没有去验证用户是否扫描了这个二维码，可以直接跳到授权登录这一步，在授权登录这个点上如果又存在CSRF漏洞，攻击者即可构造一个恶意的链接，引诱用户打开链接，利用该漏洞就可以轻易获取用户账号权限。

***23.*****凭证窃取**

//

**危害性：**高

**普遍性：**低

**可利用性：**中

通过对某个平台的扫码登录逻辑进行分析，猎人君发现最后确认登录时，只需用户的memberId就可以完成登录，每个用户的memberId又是唯一不变的。如果有办法获取到用户的memberId，就相当于永久获取到了其账户的权限。

再进一步挖掘发现在APP内可以使用JavaScript通过JSBridge调用Native方法拿到当前用户的memberId，又通过平时收到的营销短信中的链接发现可以使用Deep Link唤醒APP打开任意URL。

三者结合在一起可构造一个恶意URL，引诱用户打开，打开后会通过Deep Link唤醒APP打开构造好的页面，页面就是通过JavaScript拿到memberId并外传，再拿着memberId通过确认登录的接口就可以登录用户的账号了。

**第三方授权登录场景**

***24.*****凭证窃取**

//

**危害性：**高

**普遍性：**低

**可利用性：**中

**第三方授权登录指的是通过QQ、微信或微博等进行登录，如果配置不当也会存在漏洞。**

以QQ授权登录举例：

https://graph.qq.com/oauth2.0/show?which=Login&display=pc&response\_type=code&client\_id=123456&redirect\_uri=http://www.aaa.com/user/thirdparty/qq\_callback.php&state=8ccc0aef42194df06cfd42c606e4d59a&scope=all

用户使用QQ号登录成功后，会把登录凭证code传递给回调地址redirect\_uri，如下所示：

Location: http://www.aaa.com/user/thirdparty/qq\_callback.php&state=8ccc0aef42194df06cfd42c606e4d59a&scope=all&code=xxxxxxxxx

那么如果redirect\_uri这个值是攻击者可控的，那攻击者可以构造恶意URL来窃取用户的code。正常都会限制redirect\_uri的域名，比如为\*.aaa.com，这样域名攻击者不可控，就不会有什么问题了。但如果结合其他子域下的问题，还是可能导致用户的code被窃取。...