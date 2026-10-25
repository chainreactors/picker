---
title: 速修 | WordPress 备份插件未认证 PHP 对象注入，9.8 分
url: https://mp.weixin.qq.com/s/Zm5I5K4tM3aNM6yAcOsM4A
source: Doonsec's feed
date: 2026-10-24
fetch_date: 2026-10-25T07:06:38.246588
---

# 速修 | WordPress 备份插件未认证 PHP 对象注入，9.8 分

# 速修 | WordPress 备份插件未认证 PHP 对象注入，9.8 分

红队安全圈
红队安全圈

红队安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

漏洞编号CVE-2026-115806

影响产品Prime Mover 备份迁移插件

漏洞类型未认证 PHP 对象注入

危害等级CVSS 9.8 Critical

修复版本2.2.2

攻击者留言就能埋雷，管理员一点导出就引爆——WordPress 备份插件 Prime Mover 的 9.8 分反序列化漏洞，留言接口直通管理员会话。

## 01  这个洞是什么

Prime Mover 是 WordPress 上一款常用的备份和站点迁移插件，支持单站、多站迁移和一键备份恢复。它在 2.2.1 及以下版本里有一个反序列化漏洞：不需要任何登录权限，只要网站开放评论，攻击者就能往里塞一个恶意对象；等管理员哪天做一次常规的导出或恢复操作，这个对象会被直接反序列化执行。CVSS 3.1 评分 9.8（Critical），向量 AV:N/AC:L/PR:N/UI:N——网络可达、复杂度低、无需权限、无需交互，四个维度全是最差情况。

## 02  漏洞成因

根因在迁移的搜索替换例程 recursiveUnserializeReplace()。攻击路径分两步：

第一步，攻击者通过 WordPress 标准评论接口 wp-comments-post.php 提交一条评论，评论内容里是一个 base64 编码的恶意序列化对象，被存进 wp\_comments.comment\_content 字段。这一步不需要登录，也不需要评论通过审批——评论躺在数据库里就够了。

第二步，管理员之后做一次 Prime Mover 的常规导出或恢复。插件在数据库内容上跑搜索替换时，会把这条评论的值 base64 解码后直接丢给 unserialize()，没有设置 allowed\_classes 限制，任意对象都会被还原成类实例。

更麻烦的是 POP 链的问题：插件自带的 Freemius 库里就有一条现成的 gadget 链——FS\_Clone\_Manager::\_\_set → FS\_Option\_Manager::set\_option → store() → update\_option()。也就是说不需要再装别的插件或主题凑利用条件，gadget 是插件自己打包送进来的。

## 03  利用价值判断

这个洞的利用门槛非常低：PR:N 加 UI:N 意味着从攻击者视角几乎零成本——写条评论，然后等。管理员做导出恢复是低频但绝对会发生的动作，插件用户里做站点迁移的人尤其密集，中招概率不低。

危害上限取决于环境里可用的 POP 链。Freemius 这条链本身是写 update\_option，可做选项篡改；真实世界里 WordPress 反序列化一旦得手，通常还会链上其他组件的 gadget 走向文件写入甚至 RCE。即便只停留在选项篡改，改掉 siteurl、植入存储型 XSS 钩子也足够恶心了。

## 04  检测与排查

后台插件页看版本号，低于 2.2.2 就在中招范围内。再补一步排查：查一遍 wp\_comments 表里最近 30 天的评论，重点看内容是一长串 base64（只有字母数字和 +/= 的连续 40 字符以上）的可疑留言，有的话直接删掉并检查该时间段的管理操作日志。

## 05  修复建议

立即把 Prime Mover 升级到 2.2.2，这次更新明确加固了 unserialize 实现防止对象注入。

升级后顺手清理 wp\_comments 表里来历不明的评论，别让埋好的雷留到升级之后。

通用建议：任何把数据库内容喂给 unserialize() 的地方，都该用 allowed\_classes: false。

## 06  红队视角

这类漏洞在授权渗透里是 WordPress 攻击面的常客：评论入口永远开放、永远不用认证，是整个 CMS 里最容易摸到的匿名写入口之一。看到站点装了备份迁移类插件，先记下版本号——这类插件的处理逻辑经常要反序列化整库内容，攻击面比表面看起来大。实战里验证版本号用一条命令就够：

curl -s https://target/wp-content/

  plugins/prime-mover/readme.txt \

  | grep -i "stable tag"

## 07  参考来源

https://www.wordfence.com/threat-intel/

vulnerabilities/id/ab6ebd66-c7a4-402e-

b51e-3f1f3183bd97

说明：暂无公开 PoC，以上为厂商漏洞详情页，后续有 PoC 会跟进。

下期继续蹲厂商补丁和 PoC 动静，**关注**后漏洞先知道，修复不踩坑。

— END —

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5HsgFkdwV2JyJtbCAnjqN7qIvk8GZkoD7I5eY36IQQvribiauFhgInT7GIPm2O5D9d2ynIcbnPicbGnox7PL4Hh4g/0?wx_fmt=png)

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