---
title: 利用AI逆向CTF-APK
url: https://mp.weixin.qq.com/s/GtprEVTTq9r3QRY5CYlJZg
source: Doonsec's feed
date: 2026-01-15
fetch_date: 2026-01-16T03:27:27.185052
---

# 利用AI逆向CTF-APK

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2hnvgPYNzpJuiciaH6le2XXQKeFF88PlNPBAGKoVicmib4NhEHW5NATIApibKWqZbdC4AOb3guZABf9Nq0odb2GMlNA/0?wx_fmt=jpeg)

# 利用AI逆向CTF-APK

原创

MicroPest
MicroPest

MicroPest

![]()

在小说阅读器中沉浸阅读

导读：利用多种AI工具+MCP接口+frida hook逆向，绕过限制，解密算法，得出flag，最后给出总结报告。

一、工具准备

1、检材：2024数证杯初赛APK逆向题---“检材-03.apk“；

2、JADX AI-MCP Plugin:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpJuiciaH6le2XXQKeFF88PlNPwp6pIdS67ZryxVlnNgQianlYicYnfyrXUicmTUya4qPcDf4t4MlM2I9rw/640?wx_fmt=png&from=appmsg)

3、jadx-mcp server，如cherry studio中配置：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpJuiciaH6le2XXQKeFF88PlNPAPcRO54qMRu1WRNBic1KgCkA7lET2EqyoAvNZibqVrp6um0jQnCk0B3Q/640?wx_fmt=png&from=appmsg)

4、安装frida:

pip install frida;

pip install frida-tools;

5、安装雷电模拟器；

6、推送frida-server到雷电模拟器中，并运行；

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpJuiciaH6le2XXQKeFF88PlNPeAgdiaDNjlG5nN4qziarAvcqY6n6cpH5G7ibic5E3YcE1tuEwXdGybywIg/640?wx_fmt=png&from=appmsg)

7、配置转发端口：

adb forward tcp:27042 tcp:tcp27042

adb forward tcp:27043 tcp:tcp27043

8、参考文章：《[2024数证杯初赛APK逆向题WP（CTF2023）](https://mp.weixin.qq.com/s?__biz=MzkwODg3NzQ2MQ==&mid=2247483733&idx=1&sn=f6f790a6c609e23aa7a38cfe1bc0d401&scene=21#wechat_redirect)》。

二、逆向过程

先看参考文章。下面我将细化过程，将要点讲明白。

1、通过frida的js将中途释放出来并删除掉的update\_1\_.dex恢复出来（参考文章中提及）；

2、比较 “检材-03.apk”和“update\_1\_.dex”，会发现：前者相比缺少了三个非常重要的字符串DICT、KEY、PASSWORD：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpJuiciaH6le2XXQKeFF88PlNPKNfm5joACX4G8gFzWp1LUTicu73LAZickc3n8mr4oteicJXPEaKm0HCxg/640?wx_fmt=png&from=appmsg)

以及 缺少了一个重要的函数 com.power.flag.A中的calculateFlag(Context context, String str, String str2)，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpJuiciaH6le2XXQKeFF88PlNPYdNY7ntWibuqQNyhd345sJvPU3gq1Rsn2VTcvJxjr0L8IsKcHCc8NoQ/640?wx_fmt=png&from=appmsg)

以及 两者的 loadkey函数都不尽相同。

3、将update\_1\_.dex中的com.power.flag.A和com.power.flag.B交由kimi处理，找到加解密算法，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpJuiciaH6le2XXQKeFF88PlNP2cwk5iapAzmYPgBNPOrJ0Bh6usA2ficKQY5HEZz9qJXNUicibFg4BzuUgg/640?wx_fmt=png&from=appmsg)

如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpJuiciaH6le2XXQKeFF88PlNPThKteEeKE8iclApcu5x74YlbzZvolRwtvZYXax3apgmiaNbFJsE8Kdkg/640?wx_fmt=png&from=appmsg)

4、根据上面的3写一个解密代码：

DICT   = "9>AG3OCP1N2-4L5K6M7+BQD&EVF=0@8$"

CIPHER = "+>M=+K-@MN+-MK-@MN++MK+OM=M&MK"

# （1）. 反向：密文字符 → 原十六进制字符

rev = {DICT[i+1]: DICT[i] for i in range(0, len(DICT), 2)}

# （2）. 逐个替换

hex\_str = ''.join(rev[c] for c in CIPHER)   # 796F752061726520617765736F6D65

print('hex =', hex\_str)

# （3）. 十六进制 → 字符串

plain = bytes.fromhex(hex\_str).decode('ascii')

print('password =', plain)

得出密码：you are awesome

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpJuiciaH6le2XXQKeFF88PlNPWje282JicgsZ9sO8UgwOB6icYFybTOCr7X6xYR59OFVbWCZhdel71nCg/640?wx_fmt=png&from=appmsg)

5、当输入上面的password后，出现：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpJuiciaH6le2XXQKeFF88PlNP5e0C14PqvY3am0dKzJd5BnmRWPxUTDwX8BVZ6iaAdWdvKUia4FpKamrw/640?wx_fmt=png&from=appmsg)

6、再hook textview吧。现在我们提供一个完整的frida hook，省略掉上面的update\_1\_.dex以及上面的5，直接将flag显示出来，代码如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpJuiciaH6le2XXQKeFF88PlNPlGriaWJUcU8TN1rGbHBJnlqwXEHMicrSickfpAuOEs30T0lVIGttNzUtg/640?wx_fmt=png&from=appmsg)

【hook\_textview.js:】

Java.perform(function () {

    letFile=Java.use("java.io.File")

    File.delete.implementation=function () {

    // this.delete(); // 不删除文件

        console.log("Call delete: "+this)

        returntrue;

    }

    letTextView=Java.use("android.widget.TextView");

  TextView.setText.overload('java.lang.CharSequence').implementation=function (text) {

        this.setText(text)

        console.log("SetText: "+text)

    }

});

7、验证：

frida -U -f com.power.ctf2023 -l hook\_textview.js

在雷电模拟器apk密码框输入：you are awesome，提交后得到flag

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpJuiciaH6le2XXQKeFF88PlNPMgRCBVgrHRqsXmNfh3XzyCIIcVfmibUMgDv5Z9wYT0icyLVB1e1wTtSQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpJuiciaH6le2XXQKeFF88PlNPryJWqNCJrkm97CPlh5bKyGOoVYy6KrHC6smUic8DyBkrlSDR8wBPibYA/640?wx_fmt=png&from=appmsg)

三、总结

相比PE的AI-mcp逆向，apk的就显得繁琐些。但核心思想主要在frida hook这里，有了AI助力，包括js的编写都成了飞速。

我们通过frida hook java.io.File提取了被删文件update\_1\_.dex来进行前后对比分析，掌握加解密算法，得出了密码；并再次frida hook android.widget.TextView，将密码输入后解出flag。最后，我将上述两过程合二为一，给出完整的frida hook代码，得到flag。

利用 Frida 对 APK 进行动态分析——完整流程小结

1. 目标

样本： com.power.ctf2023

需求：绕过「动态加载 + 自毁 dex」的密码验证，拿到正确 flag。

2. 静态观察（JEB / jadx）

主 apk 仅负责加载  assets/a  → 解密成  update\_1\_.dex  → 反射调用  com.power.flag.A.loadKey() 。

关键常量： DICT  /  PASSWORD  /  KEY  全部硬编码在  A.class 。

3. 动态痛点

不保留 dex → 无法静态二次反编译；

密码错 → 不进入分支，后续逻辑不加载；

类可能延迟加载 → 直接  Java.use()  报  ClassNotFoundException 。

4. Frida 解决步骤

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpJuiciaH6le2XXQKeFF88PlNPiccdnS5Lsvva3xwcbSCYZmO30HTQTyaA78B8rhGkfib5Ydzw8jOIj3dQ/640?wx_fmt=png&from=appmsg)

5. 结果

运行时字典仍为  "9>AG3OCP1N2-4L5K6M7+BQD&EVF=0@8$" ；

逆算后得到新口令  "you are awesome" ，最终 flag 通过  TextView  日志一次性拿到：flag{ISEC-41a2369f6b586047b628d570c11d66f1}

6. 通用经验

“动态加载 + 自删除”是 CTF/壳常见套路——先拦删除，再枚举类；

遇到  ClassNotFoundException  → 延迟/轮询/枚举 三选一；

任何硬编码的“字典-密文”组合都可逆推，只要运行时把实参抓出来；

Frida 的核心价值：让隐藏逻辑在内存里“现形”，再反推即可。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpI857XC5Kft3W5TyR4cickrqaIUibKveibjF4531l9HGGu8dISFz0Yr6OUkCHfulChWC2acVmh4b39dg/0?wx_fmt=png)

MicroPest

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpI857XC5Kft3W5TyR4cickrqaIUibKveibjF4531l9HGGu8dISFz0Yr6OUkCHfulChWC2acVmh4b39dg/0?wx_fmt=png)

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