---
title: 【攻防实战10】记一次医药公司的深度穿透（一）
url: https://mp.weixin.qq.com/s/FQyEqrd0JJZgOFYYSOgAYA
source: Doonsec's feed
date: 2026-01-08
fetch_date: 2026-01-09T03:27:24.356158
---

# 【攻防实战10】记一次医药公司的深度穿透（一）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BJUTXWkQqmCPSQawDQjytHfGDbE1VmXd7sCWgINS6IsXuK8el7z7PwTrCdzlfYIicKLibwmdjmtvQwhiaYx6j5o2Q/0?wx_fmt=jpeg)

# 【攻防实战10】记一次医药公司的深度穿透（一）

天启攻防实验室

![]()

在小说阅读器中沉浸阅读

以下文章来源于十二主神
，作者十二

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5SmoGvQhdVZt3HnJhCaTsqw8CDhd2U8EH28EHwbYicjLA/0)

**十二主神**
.

十二主神安全团队，成立于2022年05月26日，是一群白帽子组织成立的非营利性的研究机构，以网络信息安全领域为焦点，致力于网络安全、应用安全与WEB安全领域的研究探索。

# 01-前言

这次是针对某个医药公司的实战攻防，这次拿到的内网权限比较多，一篇肯定是写不完的，所以分开来写，但是我会尽量把细节阐述清楚，各位大佬勿喷，刚开始以为可以通过smart bi的RCE漏洞打进去的，没想到最后是通过一个任意文件读取的漏洞打进内网，进而打通全网，姿势确实有点骚，所以在实战的过程中，只要漏洞有利用的价值，千万不要放弃，说不定有柳暗花明的时候。

# 02-入口打点

开始信息收集发现一个smart bi组件的资产，随机进行测试，发现存在漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmCPSQawDQjytHfGDbE1VmXdqlubuSzeVW3pVMwRNNJsaDZnq5YZoeiakp6M3l3OvPnjibqDmdYhwYhw/640?wx_fmt=png&from=appmsg)

使用poc进行测试，发现可以设置引擎地址

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmCPSQawDQjytHfGDbE1VmXd0fZ9Z5mJClu7rWRiaibroUG7XHv4AwS5JibIHWASbibtIgWNc4Het7oddw/640?wx_fmt=png&from=appmsg)

也拿到管理员的smart bi的管理员token

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmCPSQawDQjytHfGDbE1VmXdw7Q3vR2asMmX17SXlSHnibElfqWJrB1OtdmZF4jSAwE0sPoiag4leKAw/640?wx_fmt=png&from=appmsg)

以为拿到token稳了一波，结果没有登录成功，result：false

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmCPSQawDQjytHfGDbE1VmXdzfTlibufYeRUwZDFWGO5RnEQEpK9MHJicIBwVmNnNu7OzxxlkyRkfLoA/640?wx_fmt=png&from=appmsg)

真是有点戏剧性，那么就继续打点，这次是发现了一个呼叫中心系统

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmCPSQawDQjytHfGDbE1VmXdVibJTbI77sLVxiaKyG4fzMsFsHf7C81KEZPPg1sZAlN0jVR0qIDA132w/640?wx_fmt=png&from=appmsg)

对目标站点进行漏洞挖掘，发现path参数可以进行任意文件读取，那么直接去读取.bash\_history文件，发现有root密码修改的命令，并且泄露了出来

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmCPSQawDQjytHfGDbE1VmXdka4CICDfVKAI9S5JmGPpwKeP8kD6F9sgx2GccKwmVcK0JSibQzJ6TEA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmCPSQawDQjytHfGDbE1VmXdykic8Qib83hXLgIU0nI2ibg3fvFxiagDG0QkFWX5hibBprurrYeyvkYmQeA/640?wx_fmt=png&from=appmsg)

把history文件里面的历史命令进行汇总，获取网站路径，继续进行利用，读取

config.properties配置文件，获取到内网ftp的用户密码

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmCPSQawDQjytHfGDbE1VmXdibicU8NTWF7SQNHWX3dGyU8CYBfvgAk5iapDfc4aqdhDOTj3Kw4McKzibw/640?wx_fmt=png&from=appmsg)

继续读取datasource.properties数据库配置文件内容，拿到了两个数据库的用户密码

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmCPSQawDQjytHfGDbE1VmXdqkZpkVg33v7JibgcbqLRTqbGD4WIJAxgDjMC2zBK9JJShaIotIcfXrQ/640?wx_fmt=png&from=appmsg)

这个时候拿到数据库的密码，去撞呼叫系统网站后台的密码，一下就可以直接进，这个运气直接逆天

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmCPSQawDQjytHfGDbE1VmXdRMianwFZa3w2uuXucObdPiaUhfXTcLKPwCOrsQ0Wmib2fzlteC4mtm0vA/640?wx_fmt=png&from=appmsg)

进了网站后台，直接寻找上传的口子，在通知中心找到一个文件上传的功能点

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmCPSQawDQjytHfGDbE1VmXdXWkKibvKXM3526cibxblV5SwxibSkfM0y3q9dwjxQZIT8xmO2z0ZnZ3icw/640?wx_fmt=png&from=appmsg)

上传成功

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmCPSQawDQjytHfGDbE1VmXdAuMAMOUCF2KOe9MlsVLY5Ky6f1SAv2cuDTDmWkocZEMH1HvWVlOBvQ/640?wx_fmt=png&from=appmsg)

直接开连，马子已上线

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmCPSQawDQjytHfGDbE1VmXdWmCQyNFOljB6ZHDlotHiaZlOrNCk9MTsPG49lxCKY66hBRoosANPwpw/640?wx_fmt=png&from=appmsg)

#### Oracle:10.0.91.119:1521  ，获取数据库权限

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmCPSQawDQjytHfGDbE1VmXdCjZp9AiaX86Rsf3r7yN4ia0yIAoTs58vsUpkhGt1FWXXMNrJ9hEYCz7w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmCPSQawDQjytHfGDbE1VmXdnHxyShYR6ibLgkZLgOrpyoibyAErkCEsjWXxpzZ6tDOzQBnD5LlVevRA/640?wx_fmt=png&from=appmsg)

#### Oracle:10.0.91.31:1521，获取数据库权限

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmCPSQawDQjytHfGDbE1VmXdPRld1ubyQoctaY1iccxkb0kKe4fXerCp20ZlNxjB0FGv86gREWMZ1ww/640?wx_fmt=png&from=appmsg)

# 03-内网成果

把内网代理出来之后，开始搞内网成果，在内网发现另外一套呼叫中心系统，使用前面一样的手法，读取history文件

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmCPSQawDQjytHfGDbE1VmXdlDxMYQlgR9G0MefsKIeotLV3iatXrZx0kc47kgRsJkcSMeXqN0NprOw/640?wx_fmt=png&from=appmsg)

同样拿到修改后的root密码，那么开始对内网的SSH进行密码碰撞了

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmCPSQawDQjytHfGDbE1VmXd5r6tXaCW5WALFVY5j1xDJibj55c6ibUPpl39Ab9sThXxIicVYkZwOoFbw/640?wx_fmt=png&from=appmsg)

#### SSH:10.0.91.113  root权限

可以碰撞出一台root权限的主机，并且发现了上次登录的地址是172网段的

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmCPSQawDQjytHfGDbE1VmXdCaWcwRkPlFAKSZtKHPzwU3YDqQPXHMg88oP0jwTXDKhozOCkq1CsuQ/640?wx_fmt=png&from=appmsg)

#### mysql:10.0.91.31

通过对这台主机进行信息收集，拿到了10.0.91.31的Oracle数据库用户密码

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmCPSQawDQjytHfGDbE1VmXddHb3kspY4HydZlb35VibWHVG2JbYOVpKHj3rmNgYl1XXOkeSj2wYibVA/640?wx_fmt=png&from=appmsg)

#### 10.0.91.182 ms17-010

并且182存在永恒之蓝漏洞，获取182的system权限

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmCPSQawDQjytHfGDbE1VmXdeSN9ZJZibDicR1A0py3D74mFMO9y14Hck6C5UK2IibdEl2vkwL1bKNaOA/640?wx_fmt=png&from=appmsg)

#### mstsc:10.0.91.182

dump用户密码凭证，获取了远程桌面的权限

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmCPSQawDQjytHfGDbE1VmXd4uHEaBw9FNuiaYsxpvSicxqmiconR9ZWoHqHyUE4iaK9ma0YISBj3ibccibw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmCPSQawDQjytHfGDbE1VmXd4MQkj9BfNMGWcDBXsWTk4bK8hZOJBG94wwG01PaqGunias60LJ4QPZw/640?wx_fmt=png&from=appmsg)

而拿到了182这台主机的权限，相当于拿到了通往内网其他网段的一把钥匙，欲知后事如何，请看下篇文章。

![](https://mmbiz.qpic.cn/mmbiz_jpg/XpEvyXAhfbjSo5qNqibUE7MozLLRYPibbiawHOQh9hkgWtBak2pZuibHBUX3P6EYLicehqDwdDN7F26Zhp2qb6u5Bwg/640?wx_fmt=jpeg)

免责声明：本文章仅做网络安全技术研究使用！严禁用于非法犯罪行为，请严格遵守国家法律法规；请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。使用本文所提供的信息或工具即视为同意本免责声明，并承诺遵守相关法律法规和道德规范。公众号发表的一切文章如有侵权烦请私信联系告知，我们会立即删除并对您表达最诚挚的歉意！感谢您的理解！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/XpEvyXAhfbiaJ61H9FoBrVmJo0iaiaWiaxArrG3QD5xzyjuqaRyMcp4sscPupOsXE59edBmQibm67pn5vW0jUTmQk2A/0?wx_fmt=png)

天启攻防实验室

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/XpEvyXAhfbiaJ61H9FoBrVmJo0iaiaWiaxArrG3QD5xzyjuqaRyMcp4sscPupOsXE59edBmQibm67pn5vW0jUTmQk2A/0?wx_fmt=png)

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