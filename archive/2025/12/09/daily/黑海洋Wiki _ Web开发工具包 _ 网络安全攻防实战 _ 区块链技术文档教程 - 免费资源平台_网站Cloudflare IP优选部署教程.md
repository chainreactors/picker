---
title: 网站Cloudflare IP优选部署教程
url: https://blog.upx8.com/4917
source: 黑海洋Wiki | Web开发工具包 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台
date: 2025-12-09
fetch_date: 2025-12-10T03:21:31.533009
---

# 网站Cloudflare IP优选部署教程

# [黑海洋 | Wiki](/ "黑海洋Wiki | Web开发工具包 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台 - 点击返回首页")

# 网站Cloudflare IP优选部署教程

发布时间:
2025-12-09

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
3848

# 一. 啥是优选, 对我网站的优化明显吗?

由于众所周知的原因, Cloudflare 的大部分节点在高峰期的表现的不堪入目. 所以引申出了节点优选. 通常是把特定区域的流量引导至我们想要的 PoP(例如 HKG/NRT/SIN). 优选的节点通常会有更优的线路和性能. 优选的原理如下:

```
用户 (海外或大陆)
         |
         v
第三方 DNS 服务商 (例如阿里云, 华为云的解析服务)
         |
         v
├── 海外用户返回 Cloudflare 分配的IP
└── 大陆用户返回 自定义的 Cloudflare IP
         |
         v
用户访问对应节点, 实现优化
```

至于效果是否明显, 我觉得还是挺明显的. 大部分前端文件都可以被Cloudflare Edge缓存, 最明显的效果就是静态资源和前端页面加载的更快了, 用户只需要等待Cloudflare Edge返回api请求即可.

# 二. 如何为我的网站配置优选?

从本段开始就是正式教程了. 只要你按照教程一步一步做, 我就不信还有人能看不明白. (要是还看不明白我就真没招了)

> 情景带入:
> 我是一个新手, 我的 **主域名 sin.fan 在 Cloudflare 上托管**, 但是由于 Cloudflare 太卡了, 我真受不了, 所以我决定让用户从我的**子域名 [abab.rikka-ai.com](http://abab.rikka-ai.com/)** 访问我的网站, **[abab.rikka-ai.com](http://abab.rikka-ai.com/)** 是我要进行优选并**接入到 abab.sin.fan** 的域名.

## 1. 检查条件

必要条件, 没有的可以不用往下看了

* 一个有支付方式的Cloudflare 账号 (据说此步骤可以卡bug跳过检查, 可自行查找解决方法)
* 至少一个可用的主域绑定在Cloudflare 上, 至少一个可添加多个解析的子域名(不同主域). (单域名接入请看我的另一个优选教程)
* 一个支持分地区解析的DNS服务商 (例: 阿里云, 腾讯云, 华为云…)

## 2. 基础配置

**A. 配置回源**
根据情景带入, 我的主域是 sin.fan, 回源域名为 abab.sin.fan. 所以我先为回源添加一个解析:

[![配置回源](https://linux.do/uploads/default/optimized/4X/d/6/6/d663fec7438b87a7acc1005fc11b20c701f5b69c_2_648x250.png)](https://linux.do/uploads/default/original/4X/d/6/6/d663fec7438b87a7acc1005fc11b20c701f5b69c.png "配置回源")

**B. 配置自定义主机名**
依据情景带入和上一步添加的回源解析, 我的回源是 abab.sin.fan; 用户要访问的域名是 [abab.rikka-ai.com](http://abab.rikka-ai.com/). 根据这些信息, 进行配置:

I. 转到配置页面
查看侧边栏, 点击自定义主机名

[![自定义主机名侧边栏](https://linux.do/uploads/default/original/4X/f/7/2/f721d2b1f5be1565f38de57be179b1a1812fd0c1.png)](https://linux.do/uploads/default/original/4X/f/7/2/f721d2b1f5be1565f38de57be179b1a1812fd0c1.png "自定义主机名侧边栏")

II. 配置默认回源
在主页面配置回源, 回源就是你在步骤A中添加的解析. 我设置的是 abab.sin.fan. 你应该替换为你自己配置的回源.

[![配置默认回源](https://linux.do/uploads/default/optimized/4X/d/7/1/d71ca3b8d9cf68baeb5202deae2f7a66f73c7485_2_690x454.png)](https://linux.do/uploads/default/original/4X/d/7/1/d71ca3b8d9cf68baeb5202deae2f7a66f73c7485.png "配置默认回源")

III. 添加自定义主机名
现在回源配置完毕, 开始添加自定义主机名.
根据情景带入, 用户应该用 [abab.rikka-ai.com](http://abab.rikka-ai.com/) 访问我的网站.

首先点击 “添加自定义主机名按钮”:

[![点击自定义主机名按钮](https://linux.do/uploads/default/original/4X/1/2/9/129de8c387ab4c9e11e2c3ee181820717394183c.png)](https://linux.do/uploads/default/original/4X/1/2/9/129de8c387ab4c9e11e2c3ee181820717394183c.png "点击自定义主机名按钮")

随后在新的页面中完成添加:

[![开始添加自定义主机名](https://linux.do/uploads/default/optimized/4X/6/c/f/6cf5d8dbefb74f72f7edd018da65a1681d71126d_2_663x500.png)](https://linux.do/uploads/default/original/4X/6/c/f/6cf5d8dbefb74f72f7edd018da65a1681d71126d.png "开始添加自定义主机名")

最后点击添加自定义主机名按钮保存设置.

至此, 你已经完成了本步骤: 基础配置.

## 3. 开始接入主机名并完成优选

还记得你在步骤 2.B.III 中配置的自定义主机名吗? 当你成功配置后, 自定义主机名主页会有个类似的卡片:

[![自定义主机名卡片](https://linux.do/uploads/default/optimized/4X/b/d/6/bd69be1bde274dc3a1e178b347c5d8c4f9466f3a_2_690x370.png)](https://linux.do/uploads/default/original/4X/b/d/6/bd69be1bde274dc3a1e178b347c5d8c4f9466f3a.png "自定义主机名卡片")

待会需要你根据卡片中的内容, 进行设置

**A.接入支持分地区解析的服务商**
根据情景带入, [abab.rikka-ai.com](http://abab.rikka-ai.com/) 是我要接入的域名.
这里用阿里云作为示例, 你应该根据你使用的服务商自行调整:

I. 添加域名
将 [abab.rikka-ai.com](http://abab.rikka-ai.com/) 添加到阿里云中, 你应该会收到如下提示:

[![阿里云提示](https://linux.do/uploads/default/original/4X/4/d/4/4d4cde492a0e1a1e11eb2fe6ec91e5c9a60eb8b0.png)](https://linux.do/uploads/default/original/4X/4/d/4/4d4cde492a0e1a1e11eb2fe6ec91e5c9a60eb8b0.png "阿里云提示")

点击 `TXT授权验证` 会打开一个新的卡片:

[![阿里云验证](https://linux.do/uploads/default/original/4X/a/3/0/a3090bfd0d096672601588bb19eae197ec7b006a.png)](https://linux.do/uploads/default/original/4X/a/3/0/a3090bfd0d096672601588bb19eae197ec7b006a.png "阿里云验证")

根据卡片的描述, 我们需要给 [alidnscheck.rikka-ai.com](http://alidnscheck.rikka-ai.com/) 添加TXT解析,
这里需要你转到原DNS服务商添加解析, 例如我的 [rikka-ai.com](http://rikka-ai.com/) 托管在 Cloudflare 上, 因此我需要到 Cloudflare 上添加解析:

[![完成阿里云域名验证](https://linux.do/uploads/default/optimized/4X/d/b/b/dbb2ebc0726958d1e56b08e224bb3e5a19b72f11_2_690x312.png)](https://linux.do/uploads/default/original/4X/d/b/b/dbb2ebc0726958d1e56b08e224bb3e5a19b72f11.png "完成阿里云域名验证")

现在回到阿里云, 点击验证. 等待验证通过.

验证通过后, 进入配置页, 查看阿里云为你分配的名称服务器:

[![查看分配的NS服务器](https://linux.do/uploads/default/optimized/4X/4/3/8/43891635c441662c5f5e0c20adf24e45fbe661c4_2_690x154.png)](https://linux.do/uploads/default/original/4X/4/3/8/43891635c441662c5f5e0c20adf24e45fbe661c4.png "查看分配的NS服务器")

转到原服务商, 为子域添加NS解析:

[![添加NS解析](https://linux.do/uploads/default/optimized/4X/b/b/6/bb663852bf732f96e0b527b4fb37ddc0d85f204d_2_690x280.png)](https://linux.do/uploads/default/original/4X/b/b/6/bb663852bf732f96e0b527b4fb37ddc0d85f204d.png "添加NS解析")

添加完成后, 回到阿里云. 刷新页面后应该能看见 `域名的DNS信息配置正确。` 提示.
![NS配置正确](https://linux.do/uploads/default/optimized/4X/4/3/9/439098e9627bacf1de66c262a2300608034fd7ff_2_690x23.png)

II. 添加解析
根据自定义主机名卡片中的要求, 添加以下解析:
TXT:
`_acme-challenge`:

[![_acme-challenge](https://linux.do/uploads/default/optimized/4X/c/3/5/c359e9ecd982bdc9a211160ff248276f4545bdda_2_446x499.png)](https://linux.do/uploads/default/original/4X/c/3/5/c359e9ecd982bdc9a211160ff248276f4545bdda.png "_acme-challenge")

`_cf-custom-hostname`:

[![_cf-custom-hostname](https://linux.do/uploads/default/optimized/4X/0/e/f/0ef00c16483c61930c86b35aa1ee526b13ea790c_2_438x499.png)](https://linux.do/uploads/default/original/4X/0/e/f/0ef00c16483c61930c86b35aa1ee526b13ea790c.png "_cf-custom-hostname")

接下来是CNAME解析, 一共两条
第一条为 Cloudflare 要求你设置的回源解析, 根据情景导入, 我的回源是 abab.sin.fan, 因此我先添加一条**解析请求来源为境外**的 CNAME 解析:

[![阿里云配置回源](https://linux.do/uploads/default/optimized/4X/8/2/c/82c91e6248970060c9d07a87539061c6661696eb_2_440x499.png)](https://linux.do/uploads/default/original/4X/8/2/c/82c91e6248970060c9d07a87539061c6661696eb.png "阿里云配置回源")

第二条为 **为国内流量提供优化的** CNAME 解析, 因此解析请求来源设置为中国地区, 内容为任意的优选域名, 这里我推荐 **saas.sin.fan**:

[![配置优选](https://linux.do/uploads/default/optimized/4X/1/0/7/107b61bc6f40be2d3c8891f234d764c1ffdb5c29_2_441x500.png)](https://linux.do/uploads/default/original/4X/1/0/7/107b61bc6f40be2d3c8891f234d764c1ffdb5c29.png "配置优选")

III. 检查是否生效
现在回到 Cloudflare 的自定义主机名页面, 点击刷新. 如果两个待定均变为有效, 代表你的所有设置均是正确的! 至此本篇教程已经结束.

[![完成最终配置](https://linux.do/uploads/default/optimized/4X/d/3/7/d3779f76a13c1e30634d02cf7fe1b43798e16be7_2_690x253.png)](https://linux.do/uploads/default/original/4X/d/3/7/d3779f76a13c1e30634d02cf7fe1b43798e16be7.png "完成最终配置")

[取消回复](https://blog.upx8.com/4917#respond-post-4917)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2025 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号")