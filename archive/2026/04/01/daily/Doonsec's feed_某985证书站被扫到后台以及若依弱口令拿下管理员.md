---
title: 某985证书站被扫到后台以及若依弱口令拿下管理员
url: https://mp.weixin.qq.com/s/Lng2Ss4ZthbcL36ABc_vrQ
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:21:21.925071
---

# 某985证书站被扫到后台以及若依弱口令拿下管理员

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/AFmUR0mIsJSrgjjAvbTu1q9lTIYtCNh9M6qkS4orc7QeCbUQrFyErbia5SuiarenMVRK16tYdib0eOpCnmibHcJFibqX80bOj7W4TwJVJjr4WUhM/0?wx_fmt=jpeg)

# 某985证书站被扫到后台以及若依弱口令拿下管理员

原创

小菜鸟
小菜鸟

智动心域

![]()

在小说阅读器中沉浸阅读

本篇文章豆包写的，内容也是问的豆包，漏洞原理也是挖到以后问豆包的

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AFmUR0mIsJSeK6VyNZhAZoN9Le6YL5IEkXILbibGRZGIVicgCzwCeibvg2m6iacycTqqghTL8trgr5LeGZM2ypojIsJ4yLZDHrXp39nribDPNbiaw/640?wx_fmt=jpeg)

在教室突然给我发了个短信打算晚上回来玩玩它

短信里面有个网站,注册进去了啥洞也挖不到，新版若依框架貌似很安全

最后目录开扫发现后台，密码写在前端直接进去了

![](https://mmbiz.qpic.cn/mmbiz_jpg/AFmUR0mIsJScFuiatTZOnTBGkPzp2pNFNKG3ta4BzK5kJzpzPNoahb8ttysjuArgicibbHYCuaRo94J1kGic0UHErAP0tvFHh0O0fF70JU6n1Y0/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AFmUR0mIsJR5LMxmKJEkHPibqZmfqmIGzPyLNWkO0EXWicvALrxBUxia8vQibpfCZJ5U3AzUblUlRFibp2qbKlmLdFVbUnRg6UAC7vypN8Ria4Q7A/640?wx_fmt=jpeg)

总结：

比如输入：/xxabcdefg（纯乱码，不存在的路径）

比如输入：/xxabc123（随机字符，无实际意义）

正常情况下，访问不存在的路径，服务器会返回「404 页面不存在」。但这个平台不一样：

它会直接 302 重定向到登录页面，而且最关键的是——你刚才输入的乱码路径，会被直接暴露在登录页的URL里，格式如下：

/xx/auth/login?redirect=/你输入的乱码路径

简单说：攻击者可以通过目录扫描，只要字典里面有"/xx+任意字符"的路径，就会跳登录页，就说明这个路径是真实存在的——相当于系统主动告诉攻击者“这个路径是我们的后台接口”，大大降低了攻击难度。

更值得警惕的是，该平台基于若依框架搭建，而平台并未修改框架自带的默认管理员口令，属于典型的弱口令漏洞

豆包写的代码我也看不大懂，核心逻辑应该可以懂

// 后台权限配置核心代码（若依框架常用写法）

@Override

protected void configure(HttpSecurity http) throws Exception {

  http

.authorizeRequests()

        // 👇 漏洞关键：只要路径以/xx开头，就要求登录（无路径存在性判断）

      .antMatchers("/xx\*\*").authenticated()

        // 其他路径无需登录

        .anyRequest().permitAll()

        // 登录页路径（就是我们看到的/xx/auth/login）

        .formLogin().loginPage("/xx/auth/login")

        // 重定向参数（就是暴露路径的redirect）

        .redirectParameter("redirect")

        .permitAll();

}

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Ss2ZBltf4c3Iuia91VP9sgOZMVtTMGBIiaNlE1XaPCaZBaTQUrNyabA1ialBrzeLpS2sOdJWXBCTB8Pv2PUYkwExg/0?wx_fmt=png)

智动心域

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Ss2ZBltf4c3Iuia91VP9sgOZMVtTMGBIiaNlE1XaPCaZBaTQUrNyabA1ialBrzeLpS2sOdJWXBCTB8Pv2PUYkwExg/0?wx_fmt=png)

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