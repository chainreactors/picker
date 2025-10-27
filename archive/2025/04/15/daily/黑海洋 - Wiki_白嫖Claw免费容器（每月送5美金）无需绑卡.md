---
title: 白嫖Claw免费容器（每月送5美金）无需绑卡
url: https://blog.upx8.com/4750
source: 黑海洋 - Wiki
date: 2025-04-15
fetch_date: 2025-10-06T22:07:17.030739
---

# 白嫖Claw免费容器（每月送5美金）无需绑卡

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 白嫖Claw免费容器（每月送5美金）无需绑卡

发布时间:
2025-04-14

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
45055

## 🌟 超简单白嫖流程

1. **点击注册链接**
   👉 [https://console.run.claw.cloud/signin](https://blog.upx8.com/go/aHR0cHM6Ly9jb25zb2xlLnJ1bi5jbGF3LmNsb3VkL3NpZ25pbj9saW5rPUE1RzA3RDA1TUMzTQ "https://console.run.claw.cloud/signin")
2. **选择登录方式**
   用你的GitHub账号或者Gmail账号（两种方式都可以，选你常用的）
3. **立即获得$5额度**
   💰 每月自动送5美金，不用绑信用卡！在Plan查看余额.

![](https://cdn.skyimg.de/up/2025/4/14/5765a1.webp)

# 免费claw容器能干啥？实测这几个用法最靠谱

我最近把各种免费云服务都试了一遍，发现大多数常见用法都不太实际。比如：

1. **挂探针监控**：就是个容器环境，监控了也没啥用
2. **搭梯子**：试了根本连不上，还强制HTTPS，流量也有限制
3. **放数据库**：小网站用不上，大网站又不敢放
4. **建个人网站**：容易被搞，流量分分钟超限

想来想去，最实用的还是用来跑**青龙面板**这种个人小工具。原因很简单：

* 永久在线，适合定时任务
* 流量消耗少，不怕超限
* 自带HTTPS，不用自己折腾
* 完全自己用，不会被封

具体可以：

* 挂签到脚本（京东、贴吧之类的）
* 跑定时备份任务
* 部署一些小工具API
* 做开发测试环境

总结：免费云最适合跑那些**不需要高性能，但要长期在线**的个人小工具。既不会浪费资源，又能物尽其用，完美！

### 示例：**青龙面板**教程

进 [https://console.run.claw.cloud](https://blog.upx8.com/go/aHR0cHM6Ly9jb25zb2xlLnJ1bi5jbGF3LmNsb3Vk) , 选第一个`App Launchpad`。

![Image description](https://s.rmimg.com/2025-04-12/1744468310-776076-image.png)

**因为只有这个可以选到0.5核1G，其他的最低1C2G，送的余额不够用。**

点`Create APP`，信息填写如下：

#### 基础信息

![Image description](https://s.rmimg.com/2025-04-12/1744468645-867624-image.png)

| Key | Value | Remark |
| --- | --- | --- |
| Application Name | qinglong | 自己随便取 |
| Image | public |  |
| Image Name | whyour/qinglong:debian | 我个人习惯用debian版 |
| Usage | Fixed |  |
| Replicas | 1 | 不需要扩容 |
| CPU | 0.5 |  |
| Memory | 1G |  |
| Container Port | 5700 | Enable Internet Accesses要打开，会自动生成一个https域名 |

#### 环境变量

```
QlBaseUrl="/"
QlPort="5700"
```

#### Local Storage

需要把容器内的`/ql/data`挂载到硬盘上，不然重启了数据就没了。

![Image description](https://s.rmimg.com/2025-04-12/1744469695-339615-pasted-image-20250412220501.png)

填完之后是这样的：

![Image description](https://s.rmimg.com/2025-04-12/1744469748-975310-pasted-image-20250412220521.png)

## 每月预算分配

* 💻 计算资源：4.2（每天4.2（每天0.14）
* 🌐 网络+存储：$0.8
* 总预算：$5（刚好够用）

### 创建

点击创建后，等待下面状态变成`Active`就行。

![Image description](https://s.rmimg.com/2025-04-12/1744469886-381378-pasted-image-20250412221004.png)

### 进入青龙

之后直接访问Network里那个域名，就能进入青龙面板了，就这么简单。

![Image description](https://s.rmimg.com/2025-04-12/1744469299-582887-image.png)

后面的操作就不用多说了，在青龙里设置拉取的库就行了。

## 问题现象

* 用户运行脚本时会在某条命令处卡住
* 重新运行脚本会重复出现相同问题
* 网页会闪烁几下
* Claw面板中Pod的Age被重置为0

## 根本原因分析

1. **资源限制问题**：

   * 当前Pod配置为0.5核CPU，这对某些操作来说过于极限
   * 触发了Kubernetes集群的自动扩缩容机制(HPA)
2. **副本设置问题**：

   * Replica Count设置为1，没有冗余
   * 当Pod因资源不足被终止时，会立即重新创建新Pod
3. **CPU阈值触发机制**：

   * 一般集群Pod的CPU阈值设置为60%-70%
   * 0.5核配置意味着实际占用0.3-0.35核就可能触发扩容
   * Claw设置的阈值估计也在这个范围内

## 解决方案建议

1. **调整资源配置**：

   * 适当增加Pod的CPU限制(如提高到1核)
   * 确保有足够buffer避免频繁触发阈值
2. **优化副本设置**：

   * 考虑增加Replica Count提供冗余
   * 或配置更合理的HPA策略
3. **监控优化**：

   * 检查并调整Claw的监控阈值
   * 添加资源使用监控，提前预警
4. **代码优化**：

   * 检查卡住的命令，看是否可以优化资源使用
   * 考虑分批处理大数据量操作

需要进一步检查具体业务场景来确定最适合的资源配置方案。

1. ![难眠的小女孩](//q2.qlogo.cn/headimg_dl?dst_uin=958875986&spec=100)

   **难眠的小女孩**

   2025-04-14 16:22:36

   [回复](https://blog.upx8.com/4750/comment-page-1?replyTo=30556#respond-post-4750)

   可以挂探针吗

[取消回复](https://blog.upx8.com/4750#respond-post-4750)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")