---
title: 好用到爆了Burp的微信小程序渗透测试利器
url: https://mp.weixin.qq.com/s/ly6G21lmdZEvHVnaVyO3bA
source: Doonsec's feed
date: 2026-02-06
fetch_date: 2026-02-07T04:02:28.714590
---

# 好用到爆了Burp的微信小程序渗透测试利器

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zDP7QPgHQjSXPsNe9RfzibsAwmd8BHzMCyut6OOsgSEPRiaWYdI3Qw5KY0icv6CndEK6mPL5akMRyic84CH1GGx4zFfYbALHKoXSKNErLdP1PMA/0?wx_fmt=jpeg)

# 好用到爆了Burp的微信小程序渗透测试利器

Enginge
Enginge

Enginge

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/SEdvtYR5JaYI00RAa1ZTy35yKKkZEN7ElLsNgz8ts6yTA4cMcHfnGFJotpTGKt04nQBy5H1nAkTOUzZ0AqpdKg/640?wx_fmt=jpeg)

人类本性中最深层的渴望是被人欣赏的感觉。——

JaySenWxapkg一键自动解密+批量解包+API接口提取+敏感数据泄露检测，Burp可视化操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zDP7QPgHQjTWJU8N07NJNDnyKYUbp4bc28f5Og13bLByiaeARbC9JVRWtE4RET9CWW6uBEhJqVVGwcAhZ7cC8EDRaDOVicKLkkMn3GrHtSgMM/640?wx_fmt=png&from=appmsg)

## 📋 功能清单

| 功能模块 | 核心能力 |
| --- | --- |
| 🔓 wxapkg解密 | 自动识别加密包，AES-CBC+XOR解密，兼容PC微信小程序缓存包 |
| 📦 批量解包 | 递归扫描目录，多线程解包主包/分包，自动清理缓存 |
| 🚪 API提取 | 自定义正则规则，过滤前端路径（pages/components等），一键复制所有接口 |
| 🔍 敏感检测 | 内置手机号、身份证、AppID、密钥等规则，支持自定义敏感类型正则 |
| ⚙️ 灵活配置 | 接口前缀/后缀黑名单、API正则、敏感信息正则，修改自动保存 |
| 📊 可视化面板 | 小程序信息、API结果、敏感数据分栏展示，清晰直观 |
| 📱 小程序信息查询 | 自动提取AppID，查询小程序名称、主体、描述等基础信息 |

微信的小程序包生成路径，默认是

```
C:\Users\你的用户名\AppData\Roaming\Tencent\xwechat\radium\Applet\packages\
```

## 📝 配置示例

## 敏感信息正则示例

```
手机号:1[3-9]\d{9}车牌:^[京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领A-Z]{1}[A-Z]{1}[A-Z0-9]{4}[A-Z0-9挂学警港澳]{1}$AppSecret 泄露:(?i)\b\w*secret\bIP地址:^(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$微信小程序 session_key 泄露:(?i)\bsession_key\b身份证号:\b\d{17}([0-9]|X|x)\b邮箱地址:[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}
```

## `API提取正则示例（默认规则）`

```
(?:"|')(((?:[a-zA-Z]{1,10}://|//)[^"'/]{1,}\.([a-zA-Z]{2,})[^"']{0,})|((?:/|\.\./|\./)[^"'><,;| *()(%%$^/\\\[\]][^"'><,;|()]{1,})|([a-zA-Z0-9_\-/]{1,}/[a-zA-Z0-9_\-/]{1,}\.(?:[a-zA-Z]{1,4}|action)(?:[\?|/][^"|']{0,}|))|([a-zA-Z0-9_\-]{1,}\.(?:php|asp|aspx|jsp|json|action|html|js|txt|xml)(?:\?[^"|']{0,}|)))(?:"|')
```

## `前缀/后缀黑名单示例`

```
前缀黑名单：/pages/,/components/,/static/,/uni_modules/,uview-ui/后缀黑名单：jpg,gif,svg,wxss,wxml,png,js,jpeg
```

## `可回复"260206"获取工具链接`

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/SEdvtYR5JabmH4p5zqINv9hK3mIfaDs0YRicvRQAMFtXk6ZwibGBEzyhm0DWkOvbXSa044LTVoFI7jfqOibSSmWMg/0?wx_fmt=png)

Enginge

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/SEdvtYR5JabmH4p5zqINv9hK3mIfaDs0YRicvRQAMFtXk6ZwibGBEzyhm0DWkOvbXSa044LTVoFI7jfqOibSSmWMg/0?wx_fmt=png)

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