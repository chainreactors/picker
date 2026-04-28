---
title: [更新]红队加载器LoaderV6.2
url: https://mp.weixin.qq.com/s/2iLSl2pkr7cYUWq-WLcvbg
source: Doonsec's feed
date: 2026-04-27
fetch_date: 2026-04-28T05:26:24.095635
---

# [更新]红队加载器LoaderV6.2

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibXL9MCj2GqN76SXfjpof69BByc3lWP6icCP9TFlia3SicO5jgWs4VO6FXxOTBsCdPuibn9kIOTyLb5aqAvYXNVkB2PTedNlzXGOrnQhNwYlQBYc/0?wx_fmt=jpeg)

# [更新]红队加载器LoaderV6.2

原创

陆安予
陆安予

白帽子安全笔记2.0

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# [更新]红队加载器LoaderV6.2

这是一个具有高级规避功能的有效载荷加载器。

### 一、新增内容

1.新增了OLLVM代码混淆。
2.修复个别细微Bug。

> 当启用OLLVM代码混淆时，支持codasm和codasm+veh两种加载方式。

![代码混淆](https://mmbiz.qpic.cn/sz_mmbiz_png/ibXL9MCj2GqMnoZ6QsuWaFpZ8ic6GxwHqNEDvjfar4jUMU9OccrZRiacib1Q8EM59Bsicq414pqaSJCDicslAjibC6oQPiajsEhZfbjDraYnszq9tzU/640?wx_fmt=png&from=appmsg "null")

代码混淆

整体效果如下，截至目前共支持7种加载方式：

![工具演示](https://mmbiz.qpic.cn/sz_mmbiz_gif/ibXL9MCj2GqMpLtLoYtHw7lKnM7sRjqria2HL1CKGXib8MIte1kF4jTSz6jRKNrkHTLYVicxoPoIVCt00Xq089Z7NKQ0dDVWKI5bVYnCRwGDDN0/640?wx_fmt=gif&from=appmsg "null")

工具演示

### 二、技术细节

#### 1. OLLVM代码混淆

轻松支持代码混淆，只需菜单下载OLLVM并启用该功能即可，无需复杂配置。

什么是代码混淆，以示例代码为例：

```
#include <stdio.h>
int main() {
    printf("Hello, World!\n");
    return 0;
}
```

![未混淆程序反编译](https://mmbiz.qpic.cn/mmbiz_png/ibXL9MCj2GqOkS2Qic5HK3ib2WdLJrQEvTvwDW1gecSWEicgaycQPjqIlFrtsXCV5SLXKfR5onhuicOVicO7U951j4DhPB80vZd3TozCxVbpIGnWw/640?wx_fmt=png&from=appmsg "null")

未混淆程序反编译

将IDA反汇编信息丢给AI分析，总结如下：

> 该程序是一个使用 MinGW-w64 编译的简单 Windows 控制台应用程序，其核心逻辑是通过互斥锁确保单实例运行，初始化 CRT 运行库和 TLS 回调，执行 PE 伪重定位修复，最终输出 "Hello, World!"，并设置了结构化的异常处理机制来捕获访问冲突、除零等异常。

使用OLLVM混淆，开启-mllvm -sobf -mllvm -fla -mllvm -sub -mllvm -bcf高级混淆。

![混淆的程序反编译](https://mmbiz.qpic.cn/mmbiz_png/ibXL9MCj2GqMJ6biaiaprQPibqSD1KvCuQHnIZlpFqRIc4tRzAVwKiasgPqDKlicU0ibLhCdiaVdsGQRStyEtZ3M2F4EGXJ2ibrdHYZSmxF8CuUmo6ho/640?wx_fmt=png&from=appmsg "null")

混淆的程序反编译

将IDA反汇编信息丢给AI分析，总结如下：

> 该程序是一个经过高度混淆的Windows PE64可执行文件，通过控制流扁平化、动态字符串解密、TLS回调及自定义异常处理等反分析技术来阻碍逆向工程，并结合VirtualProtect动态修改内存权限以执行伪重定位操作，表现出明显的"恶意软件"加壳或反调试特征。。

### 三、检测情况

[略]

该项目是[顶级武器-完全无法检测的cobalt strike](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247483684&idx=1&sn=5b97213cbd35cd78540645379db925a1&scene=21#wechat_redirect)项目的附赠内容，可至工具菜单【更新】下载。

如果你对这些红队项目感兴趣或想了解更多信息，可查阅我的产品清单《2026年度红队战术攻防武器库产品手册》[1]及协议《合规协议》[2]。

#网络安全 #红队训练

---

### 四、免责声明

本文涉及方案仅限合法授权的安全研究、渗透测试用途，使用者须确保符合《网络安全法》及相关法规。具体条款如下：

* • 仅可用于已获得书面授权的目标系统测试；
* • 遵守法律法规，不得用于侵犯他人隐私或数据窃取；

本人不承担因用户滥用本软件导致的任何后果。使用即视为同意并接受上述条款。

---

#### 推荐阅读

* • [高级LNK中的反沙箱技术](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247485293&idx=1&sn=3ff02916e7a6b13d280fa145a281e42e&scene=21#wechat_redirect)
* • [[重要更新]高级lnk快捷方式](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247485269&idx=1&sn=8897a078d020aa9ff1a1f36c253dedd0&scene=21#wechat_redirect)
* • [红队基础设施指南与高级匿名技术](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247485253&idx=1&sn=c55c3849c88bd3b039427b66dd7802fb&scene=21#wechat_redirect)
* • [[更新]红队加载器LoaderV6.0](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247485185&idx=1&sn=00d9086d1bb96b9ba57f62c74f0243e6&scene=21#wechat_redirect)
* • [[更新]红队加载器LoaderV5.1](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247485168&idx=1&sn=0d6f115dfafd6b98dba7deb7fe816afb&scene=21#wechat_redirect)
* • [100多个C#工具怎么用？先学会这招绕过AMSI](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247485138&idx=1&sn=500f122481008e8010194dbf79574fbf&scene=21#wechat_redirect)
* • [红队攻防的十年：这些经验让你少走弯路](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247485110&idx=1&sn=a76ddd623589846f9fcc9e2e2fcb6c15&scene=21#wechat_redirect)
* • [Lua作为攻击载体的技术分析](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247485047&idx=1&sn=bab961b4ca0d9dd1a9454b3455eaa0a2&scene=21#wechat_redirect)
* • [[更新]红队加载器LoaderV5](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247485039&idx=1&sn=8ec2ff200c6d47d34f3ee7674ab5a963&scene=21#wechat_redirect)
* • [[更新]红队加载器LoaderV4](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247485029&idx=1&sn=31ac67de9dac6b5f8bf994cd405f7f25&scene=21#wechat_redirect)
* • [攻防必备，DLL代理自动化生成](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247484664&idx=1&sn=161e2f5bd7433ff9404ac38ecc7724b9&scene=21#wechat_redirect)
* • [攻防必备，DLL侧载（白加黑）自动化生成](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247484651&idx=1&sn=f51b71f50fa18120513848832a7bcdd0&scene=21#wechat_redirect)

#### 引用链接

`[1]` 《2026年度红队战术攻防武器库产品手册》: *https://www.kdocs.cn/l/coR1BuQkseWz*
`[2]` 《合规协议》: *https://www.kdocs.cn/l/cqPic7iLh0hn*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ibXL9MCj2GqM0QSEUqWHz3BBibqxHbxaC5wibm9paYNX1cJYtzWM4k6eibECJN0DQ2t8WFbiaPsorl4kibSB0hMqdpYmN1TTXHicgnCdSGNSomJBjI/0?wx_fmt=png)

白帽子安全笔记2.0

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ibXL9MCj2GqM0QSEUqWHz3BBibqxHbxaC5wibm9paYNX1cJYtzWM4k6eibECJN0DQ2t8WFbiaPsorl4kibSB0hMqdpYmN1TTXHicgnCdSGNSomJBjI/0?wx_fmt=png)

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