---
title: EDUSRC--985证书站从接口FUZZ到满分漏洞
url: https://mp.weixin.qq.com/s/LEg8p-tNyuy_I-6ILQkEOQ
source: Doonsec's feed
date: 2026-03-23
fetch_date: 2026-03-24T04:13:31.369892
---

# EDUSRC--985证书站从接口FUZZ到满分漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibeMgKhFUfbRhUibQcBaM3sMKzXopOV0Wic8c5VhzMYoYWJUdhDuFcIMJ8JQicP2iciaxMTricKoBicBHszcMsYUsgJKbMPgLOicehKP08wAVVFS438M/0?wx_fmt=jpeg)

# EDUSRC--985证书站从接口FUZZ到满分漏洞

狗窝集团
狗窝集团

狗窝集团

![]()

在小说阅读器中沉浸阅读

记录一下一次985证书站漏洞的挖掘的过程，如果有写的不对的地方欢迎各位师傅指正。因为是最近的漏洞，不知道修复了没有，厚码原谅。

常规的信息收集开局，找到一个登录框，明面上只有统一登录和手机号登录两种方式，因为没有账号所以不去考虑统一登录。这里思路是用自己的手机号去获取验证码，看看能不能发出来验证码然后通过修改响应包进入后台，或者是跑手机号字典，看看有没有开发留下的18888888888的这种类型的手机号，然后去爆破验证码进行登录。

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbSKxjAYZGgfPACxdk6iaLv0JJYTIQJf8L2ibzRRfX7L7k2Pmwq2r6M0UFX771KNqLGg1X573iacrWahY5szib2R0Jn26nHh395hPu8/640?wx_fmt=png&from=appmsg)

此处用自己的手机号是可以获取到验证码的，但是会提示账号没有开通。那这样子的话其实也不好跑手机号字典了，因为不清楚账号是否存在

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibeMgKhFUfbQnEXatiariaNZOAppUXShFe3EOUtpF2zqlJflA3sysITZEhZyyEesL6h4ROaBBfDUmfhkcEh9ZhKJdSicpspdcGe62QvdyvMTiaL0/640?wx_fmt=png&from=appmsg)

这里观察了一下登录界面，感觉登录界面是被删过，手机登录后面空了一大截，这里猜测开发之前可能是想做账号登录，或者是做过账号登录，但是接入了统一登录之后就将账号登录给删掉了。

看了一下登录的请求包，后面有一个grant\_type参数，猜测是登录方式，这里是手机号，那更确定之前是存在账号登录的，于是通过对常见的账号登录参数去进行fuzz，例如账密登录的方式可能是pwd，接受账号和密码的参数是username和password或者user和pwd

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibeMgKhFUfbRDyAnNb6cBg0aBYlE1I4JU1EWowxic68P5dUMMBicCicZSjxER7qrN2uRvfBMOf2nXTLRr4SUBxZ1jUWLLGNF3UJsKvNsGzDzwJg/640?wx_fmt=png&from=appmsg)

这里将前面login/moblie改为了login/pwd，将参数改为了username和password出现了401，而不是404，这里猜测没问题，是有这个接口的，但是需要权限，但是按照正常的开发逻辑，在没登录账号之前是没有权限的，所以不可能对登录接口去做鉴权，这里猜测是login/后面的路径没猜对，于是换上路径字典去跑了一遍，结果除了pwd其他全是404。

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbQWMcibAejTFgyNK3ibvYsSxbzIDaZvGaBnG61ZjaDpBCKRJhk2ictaoDkiccquPJycxZd78EanPR3yicAawwR3zAWPP4DQhQ5cP4cM/640?wx_fmt=png&from=appmsg)

此时灵机一动直接将login/后面的路径给删掉，让login直接去接收username和password（其实是跑红温了，毛个路径没跑出来）

这里确实有运气成分，不过结果是好的，通过账号密码的方式跑出来弱口令，直接显示登录成功了，并且返回了token

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbS90cNlqlzEHzFib7KQHpkticehKCQF7IhSBnc3LM6AD0vMjWbWCjnK5sJSmAELgcPX4YELlwuBTZG1LYviabJxxicsAaQ42n2m4uU/640?wx_fmt=png&from=appmsg)

这里直接进入后台了，也是超级管理员权限，并且功能非常多，对于这种功能很多的后台站点，建议各位师傅不要着急去打，用bp的浏览器去多点点，然后bp带上hae和xiasql的插件，熟悉网站功能的同时，也可以让hae和xiasql去对流量包检测是否存在敏感信息和sql注入

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbS4oYQQ4Fuux3SgEkNPaGia0SappV4hSVyzbX7FHatz491ubpkfy379SpcYvcVK8RcdpqAOYcMcVWP4Hkudl8Gp2EiaDFXaia1kuY/640?wx_fmt=png&from=appmsg)

后续在一个审批的功能点中发现了进校预约的信息，有预约人员上传的证件信息，那这里也可以知道，这个站点的普通用户是有文件上传的功能，而文件上传之后会进行存储，这里可以看看是存在本地还是云存储桶中，如果在本地的话可以去尝试打文件上传或者xss，如果在云存储桶中的话可以看看是否存在云存储桶的未授权删除、文件覆盖等

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibeMgKhFUfbT68GLEicnWdwticZp25iaiby0eWfs1vkr1xvcyfwcMcggoqS2ZWEeibZ1XtrkMZnvS0naFP8yMXFBlf95PMj5XMxenma6BnFUr6SUY/640?wx_fmt=png&from=appmsg)

这里右键图片，新建链接打开，发现路径中存在oss，那就是保存在云存储中（路径中有oss/s3/minio等字样就是云存储，实在判断不出来就逐个路径删除来进行判断）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibeMgKhFUfbSqbj7wM19BYqyMw3AI1iaLuJ7TWMx0GcXAAc9pFhvqaKcVbU0pfGaTuEl00RIVZGSuwYxVHO9diaID5ese0FXcayc0bZS1QM4xI/640?wx_fmt=png&from=appmsg)

这个地方删除路径到根路径，直接将存储桶中的所有文件列出了，能列桶的话就有可能存在文件删除和文件覆盖

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbQuTdDXwnxgpjtqm44Gbyh4usqAwAntBLhznRR3sOXLT29JKTcX4gjIHJIU9LmwLxCqNB27IcP5qCduDlVPV1iaLPtUYMU1BgU8/640?wx_fmt=png&from=appmsg)

这里构造数据包，用PUT方法去上传一个文件

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbQxicVDhcAd33tuffCpmuNKeZupNQiaS2H9ZTPxu88hUlmLbb7mK9xffGGZwzqUiaLlfic0gbicDAia6Lm0kquZfwdVnayphue4l3Ll0/640?wx_fmt=png&from=appmsg)

显示上传成功后，去刷新一下浏览器确认一下

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbS01YjC7kdgR4uflSiaBsMxXYocJbZOyT9bErOHJJsbIAnGQqSBMDOMVOvFTuAozK1DW8D32UFT3ibgOHEeIQERAJM8DQe3ic2lVo/640?wx_fmt=png&from=appmsg)

此时再上传一个同样名字，但是内容不一样的文件，如果ETag的值发生了变化，就证明存在文件覆盖

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbTWcdoxLFWPpS94Fxg38U0SDh7ibia476pbU6yyiarxjibsibMoiaBaMjhEWwDcHibIDkQIYibhjQO6rm9Z70qGdvSH9SyD6Wh4wjeshEM/640?wx_fmt=png&from=appmsg)

此处ETag变化，证明存在文件覆盖，删除也同理，将请求方式变为DELETE即可，这里就不多写了。

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbRpnK6o5mwu9U8v6oo0yTXpW4m3ow1tLUEicDcA2dYo4LyYzsWttTkWdz9L3KMgyEvfib6B8dHcRicU68zQ9d76NY0ibOnofhUFJuU/640?wx_fmt=png&from=appmsg)

存储桶打完了后续又看了一下别的功能，在预约处发现了身份证照片（这里截掉了）及证件信息。大概有4w

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbS9ZruAVsKg6IQFvAnPksA6usRJ7yMfbqOfeRyGLGcraU3x504iajjwohCRzFRojGLkOmAHiaK7DjSsXxic7a9pbAYicibR6HPw7nCA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibeMgKhFUfbQDN8ytmUbwX6j59wkdwoibxKFZ4FLSnzVibCyOiagGWsgombr8ia5UnPia3siaZ8TBDbgTJicBpef7S6OBt1TaXuXicDR4bqPM0gRRXVQ/640?wx_fmt=png&from=appmsg)

打到这里就已经高危了，因为是我们是超管用户进来的，可以给普通用户添加管理权限，于是找个普通用户去给他升级为管理员，同时将升级管理员的请求包记录下来，一会找个普通用户去调用这个升级接口，看看是否存在普通用户越权使用管理员的接口来打一个越权（虽然麻烦，但是可以多恰点烂分）。

前面忘记说了，这个站点的登录账号和密码是一样的，有很多系统都是这个规则，初始账号和密码是一样的，大家平时在那种拿手机号登录进去的网站，可以尝试找一下有没有账号登录的地方，然后去跑弱口令，因为很多快捷登录，登录之后会自动创建一个账户（默认账密），如果确定账户和密码是一样或者密码统一为弱口令的话，可以去找找有没有的接口可以拿到别人的用户名，如果有接口泄露全站用户名的话，就可以去打个全站用户接管。

好了我们再回到这个站点的测试，此时我们已经换成了普通用户（看功能应该能看出来吧，这个号少了很多功能）

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbT8ALhnqKAwOibLeZOFvqdWnMAoQicM6ADbTMibU1icvPVdnIITWBY9r4OcJVlicM3WHczs4zdGXg79eMXwjicEEfT5QggGo0hotTpXw/640?wx_fmt=png&from=appmsg)

不过在刚登录这个账户的时候发现了一个数据包，这个数据包的普通用户查看自己的预约记录的，是通过applyerId来进行查询的

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbRODcXYSAuQu9p8Cb5Lhlb1uMHUib8zM3TtbRXXW7ucFTFicUMHkk4hSL9HibXbUEfMq2KZL0AP4rqYE4R6H9HluhfdQR3clD9vBw/640?wx_fmt=png&from=appmsg)

这个applyerId看着像是不可以遍历的，不过很多系统都有这个问题，就是将参数置空或者改为null，会返回全站用户的信息，此处置空id，确实返回了全站信息（因为有敏感信息，就直接打码了，各位师傅看两个数据包显示的名字也能看出存在这个漏洞的，反正也是一种思路吧）

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbTTkjIpEGwJ6ib5b11RCwvBibtVoVvuwV3AB3L2akmsojjCVpATTiaGw65ay99icsgzdPROO196cxic776F73OFubCWpjbt89791P9M/640?wx_fmt=png&from=appmsg)

这里光打个信息泄露肯定不够，这是刚才预约查询的页面，我们可以发现是通过id来进行查询的，并且下面是要上传证件照的，我们可以通过置空参数，获取全站用户的id，然后在浏览器中更换别人的id，来进行一个越权

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbSywpyx95QHo0ia1gic5pRH1eAcV8Vfd9Xul10F4djEicbqRlbdrDjmI25NnpBcicxnFPGicbsWsqvBfM1zq53amwEB08m25dodFlCg/640?wx_fmt=png&from=appmsg)

这里将id改为胡某某的id，再刷新浏览器就直接更新变为了胡某某的预约界面了，也算是可以多水一个越权吧

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbRcXhOnDchQLenAaazqvpZMKgBpZxeI274qFWnJicQShRG9AdnxnMzu1n3eZG6YTLt6ImGgEMicIp4nHicaMSrrK5FDcDTMd68niaY/640?wx_fmt=png&from=appmsg)

好了回归最开始切换普通用户的初衷，我们要去尝试越权为管理员，用普通用户的cookie去调用升级管理员的接口，看响应是直接成功了，那么垂直越权也是存在的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibeMgKhFUfbRhAe97rxz8pyulOc8ZKuNkpu60RrpKf7hwJUVuctC4lHhszx0RqkoVHTibjiaicCNfPqyttGv70ohVcCEia1lM5CerVjX6tHT2icEM/640?wx_fmt=png&from=appmsg)

刷新一下界面，可以看见已经变成管理员了（功能多了，这里名字不一样是因为测试的时候换了几个号弄混了，这个号也是普通用户的）

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbRfLmzdJibia3GWZFz69Z9Y1CkzDkEl2aIgoKMqPzIUBf5iaTTup0jVKZy2anIITicwIqQrOPrgibZScjsX7BYviatAjjviaZyWk2u8Ck/640?wx_fmt=png&from=appmsg)

（下面的是升级之前的截图，不然你们说我拿个管理员用户来糊弄你们）

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbQZIMPAm34xiaDdiaSlfYvGtnJCEXTB6rhE3ib86qyPGnSASPpkNsUibaiatbN1JTjn8LB2pw85YShgZoZ8oxh47dPia0FEnhYUY7eOY/640?wx_fmt=png&from=appmsg)

最后算一下这个系统（管理员权限、存储桶未授权、多处越权、4w信息），其实这里分加起来是肯定够10分的，不过因为是985证书站，自己的朋友们也想要，奈何实力不够，于是把报告给拆了分开交了，自己号交了俩个，给了朋友两个，所以四舍五入的话也算满分吧（手动狗头）

![](https://mmbiz.qpic.cn/mmbiz_png/ibeMgKhFUfbSYiaSgM7NL8s3rHWptu4H4tV8d9HqauV8MdMCMjU76o5F5PpribpT1akWiaqdtXK2o3kHEEFGOKhfrv2CuCKicP9Zlj9K47aSiaSUI/640?wx_fmt=png&from=appmsg)

最后也欢迎各位亦菲彦祖加入狗窝，一起交流经验，交换情报

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibeMgKhFUfbRnTsb98HgfCDG1SrZ17kHm2ic2pzlC82bs3AsntuiaiaLqnO2IZfZ1xISCC22gQHaZ1T7wDtTfLX4rWmAva9NEVXkUymnPTDlABg/640?wx_fmt=jpeg&from=appmsg)

结尾打个广告

狗窝小课堂开课啦！

课程分配：50%理论课程+50%实践学习(导师直播带)

课程大纲

(大纲仅供参考，实际内容细分下去只会更多)

形式为直播互动教学以及一对一答疑，每次直播都会有录播(敏感操作除外)

每周两次直播，每次直播一到二小时，第二期课程周期预计三个月

![图片](https://mmbiz.qpic.cn/mmbiz_png/57W11VialTL9iaNP0xw4BF7QjUPcdNuHheqfNSzoziafW9qQTefKlmxVgm0WhVohjWRia7ETORQeVphJOZjIZXQyww/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

第一期部分成果展示

![图片](https://mmbiz.qpic.cn/mmbiz_png/57W11VialTL9iaNP0xw4BF7QjUPcdNuHhekpFEotHJFQz24pNr4NBB3K3WkDSDt0zHtyz9yIqdtvaheyqr89XOEA/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

![图片](https://mmbiz.qpic.cn/mmbiz_png/57W11VialTL9iaNP0xw4BF7QjUPcdNuHheBlEFmdgsU4tlodLNQ5p2ogI0nHjMmPbnIzSU78Jz7FhdeGK6GWaGSQ/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#img...