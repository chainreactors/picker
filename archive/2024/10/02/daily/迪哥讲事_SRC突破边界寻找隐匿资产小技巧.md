---
title: SRC突破边界寻找隐匿资产小技巧
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495993&idx=1&sn=ad5f7b14b17b40a340106db576d98b64&chksm=e8a5fb5adfd2724c7516b869c6763ae28088d026d57446553c9cb140122705c51eb301965dff&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-10-02
fetch_date: 2025-10-06T18:55:13.158164
---

# SRC突破边界寻找隐匿资产小技巧

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj44O7Z4ysvltJVJxwVHWpUMNTrAOgRLW1PwkXjXyxT3pIfICoCF0ccHDwpzrkw8LRicTCqym3ppI3A/0?wx_fmt=jpeg)

# SRC突破边界寻找隐匿资产小技巧

迪哥讲事

以下文章来源于猪猪谈安全
，作者随风kali

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6Tdsb6fiaynX43ZIBVLFOXXvibjd08a8U8xXYWtPjUYFxA/0)

**猪猪谈安全**
.

致力于让小白也能学懂信息安全，分享一些自己信息安全方面的学习经验，让正在学习信息安全的人少走弯路！不定时推送一些学习路上会使用的工具和一些优质的学习资源。

**0x01 前言**

在SRC漏洞挖掘中或者渗透测试中，前期收集好各种WEB应用，开心的打开Burpsuite准备大干一场的时候，发现全是403 404 400 500，于是你开始扫描端口、爆破目录，但是什么都没有信息都没有出来，结果灰溜溜的关闭了浏览器和你的Burpsuite。作为安全圈的老混子，碰到这种情况我们该怎么破局呢？

**0x02 HOSTS碰撞**

我们在平常摸鱼中，经常会碰到这样一种情况，直接利用ip访问显示的是403 404 400 500，但是用域名请求就会返回正常业务。当然在排除WAF作祟下（有一些WAF它会要求使用域名访问，使用IP的会出现WAF的拦截界面），我们就可以利用hosts碰撞技术来尝试一下是否能突破边界。

**0x03 漏洞原理**

漏洞产生的根本还是源于配置不当，一些系统配置了内网访问，但是由于配置不当的话，例nginx配置不当，或者nignx default\_server没有配置或者配置内网，那么内网的业务可能存在被传出的风险。

**0x04 漏洞利用步骤**

一、收集目标的域名和IP作为字典

可使用一些工具如oneforall

![](https://mmbiz.qpic.cn/mmbiz_png/3ZX4O1QxGtNp412v7zLuasqP6zPjicu5hyBV7Ej5Yicju4Kq3KiaicoQRpM95O2jHfKoGXSoicJdDicWeEJrsmCibicLmg/640?wx_fmt=png)

也可结合其他工具，搜集的域名和IP越详细越好

二、利用脚本碰撞

**脚本地址**

```
https://github.com/fofapro/Hosts_scan
```

将搜集到的域名和IP分别放入hosts.txt 和 ip.txt

**0x05 漏洞复现**

**搭建环境**

**安装nginx**

```
[root@localhost etc]# yum install -y epel-release[root@localhost etc]# yum -y update[root@localhost etc]# yum install -y nginx
```

**配置漏洞环境**

**1、设置反向代理**

这里用apache模拟反向代理端口（实际上应该还要创建一个网卡去模拟内网端口，为了省事就模拟一下端口吧），为了防止端口与nginx冲突，我们修改为8000端口。

**2、限制IP访问**

配置文件位置/etc/nginx/nginx.conf

替换配置文件中的http部分如下

```
http {
  include /etc/nginx/conf.d/*.conf;  # 限制IP访问  server {    listen 80 default;    server_name _;    return 403;    }  server {          listen       80;          server_name  www.test.com;    location / {              #反向代理                proxy_pass http://192.168.178.143:8000;              index  index.html index.htm index.jsp;          }      }}
```

配置好访问结果如下

![](https://mmbiz.qpic.cn/mmbiz_png/3ZX4O1QxGtNp412v7zLuasqP6zPjicu5hsAhjJ8QSN8Ey9UPZEC2k6jzsOBKRnXZkCefPVtfqxsof1vIrh9kCRw/640?wx_fmt=png)

然后我们修改本地hosts文件，添加一条本地解析

![](https://mmbiz.qpic.cn/mmbiz_png/3ZX4O1QxGtNicZ6QvtENZURiaMI3X2eyK9tibcz3k1uNvemicUzGOhMibOhlb81x6zj5mazhiavRcqg3h6MY7KMg9zJg/640?wx_fmt=png)

然后使用www.test.com进行访问

![](https://mmbiz.qpic.cn/mmbiz_png/3ZX4O1QxGtNicZ6QvtENZURiaMI3X2eyK9OUr4A8TTJFRW1LG8PJGEogF0Wa14eMBPx5JXEcxoDiaW0GHicrExDTSQ/640?wx_fmt=png)

即可访问到apache默认页面，假设某公司内部系统也错误配置，我们即可访问到该公司的内部系统。

**3、脚本复现**

下载脚本

```
https://github.com/fofapro/Hosts_scan
```

把收集过来的域名和IP分别存入hosts.txt 和 ip.txt

然后运行脚本

![](https://mmbiz.qpic.cn/mmbiz_png/3ZX4O1QxGtNicZ6QvtENZURiaMI3X2eyK9WSicMqc2hqZwbKw9bqeXNEzO2rSvA7Nl8RWgZquWJ7ELProf3e6iaoHw/640?wx_fmt=png)

可以看到碰撞成功的结果

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

**0x06 参考文献**

```
http://r3start.net/wp-content/uploads/2019/08/2019080916135087.pdf
```

---

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

迪哥讲事

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

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