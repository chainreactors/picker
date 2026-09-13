---
title: 【安全圈】GitLab曝CVSS 10满分漏洞：免密盗源码，数小时遭在野狂扫
url: https://mp.weixin.qq.com/s/4m54ExpMl47aP4hLf-4HXA
source: Doonsec's feed
date: 2026-09-12
fetch_date: 2026-09-13T06:57:39.049278
---

# 【安全圈】GitLab曝CVSS 10满分漏洞：免密盗源码，数小时遭在野狂扫

# 【安全圈】GitLab曝CVSS 10满分漏洞：免密盗源码，数小时遭在野狂扫

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

**核心事实：**GitLab 官方紧急发布安全补丁，披露一处危险等级拉满的最高危任意文件读取漏洞（`CVE-2026-85706`，CVSS 10.0）。攻击者无需登录凭据，只要目标实例存在任意一个公开项目，就能远程读取服务器核心配置文件与商业源代码。威胁情报机构 watchTowr 证实，在官方公告披露仅数小时后，全网已出现大规模自动化在野探测。

![](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyEsl7gMm85dNicjT8WYwyaRnicD6qKCzIiaUNeoSQLicLicj2ibUx6LmYgFqoRpvjjsNHnDdp9fkbj8jYeRd6C57XQUS150XiblxJUgeg/640?wx_fmt=other&from=appmsg)

## 🔍 一、 漏洞成因剖析：API 鉴权与路径校验双重失守

该缺陷扎根于 GitLab 的代码仓提交记录接口（Repository Commits API）。按照正常业务设计，该接口用于查询项目提交元数据与特定文件改动，但开发团队在该端点遗漏了两道最基础的防御栅栏：既没有强制执行会话鉴权，又没有对输入的文件路径做规范化沙箱限制。

外部未授权攻击者只需向公开项目提交 API 发起特定的 HTTP POST 请求，并在请求参数中夹带目录穿越序列，服务器底层的文件读取函数便会径直跳出代码仓根目录，将系统底层文件原原本本回显至前端。

⚡ 攻击利用关键要素

▪️ **唯一触发前置：**目标 GitLab 实例上开放了至少一个公开（Public）可见的项目仓。

▪️ **零认证攻击面：**调用链不校验 Cookie、Private-Token 或 OAuth 凭证，匿名访客即可发起交互。

▪️ **路径越界读取：**通过在 `file.Path` 字段注入穿越符号，直接扒取服务器敏感文件。

▪️ **连带修复高危漏洞：**同步修复了 Duo Chat AI 助手的反序列化漏洞（`CVE-2026-87719`，CVSS 9.9），防止认证用户越权提取系统搜索配置与核心 Secret。

## ⚠️ 二、 研发底裤被扒：供应链失陷的链式反应

GitLab 是现代企业研发生命周期的核心大脑。单纯的“任意文件读取”看似不执行系统命令，但在真实的 GitLab 架构下，这足以让企业防御体系瞬间崩塌：

**1. 窃取 `secrets.yml` 伪造最高权限：**
GitLab 的会话加密与持久化 Token 均高度依赖底层主密钥。攻击者一旦利用该漏洞读取到系统的私钥文件，便能自主生成不可撤销的管理员会话 Cookie，实现无需密码的隐蔽接管。

**2. 私有业务代码与 CI/CD 环境变量外泄：**
攻击者不仅能批量偷窥未开源的商业核心逻辑，还能直接提取 CI/CD 流水线中预置的云厂商 AccessKey、生产数据库密码及发布机 SSH 秘钥。

**3. 在野探测已全网铺开：**
威胁情报机构 watchTowr 监测显示，自协调披露当日 06:00 UTC 开始，公网多个已知扫描节点已频繁向全球暴露的自建 GitLab 发起包含特征参数的侦察探测，极可能在短时间内转入无差别自动化收割阶段。

📦 受影响产品与安全版本对照

受影响版本范围

GitLab CE / EE 18.7 至 19.1.8 之前、19.2 至 19.2.6 之前、19.3 至 19.3.2 之前的所有历史发行版。

已修复安全版本

官方已发布 **19.3.2**、**19.2.6**、**19.1.8** 补丁。所有自建用户需立即升级。

## 🛡️ 三、 紧急排查命令与防御应对动作

**1. 快速检查 Web 访问日志中是否存在攻击利用痕迹：**
安全团队可通过下述指令，全面检索 Nginx 访问日志与 GitLab API 审计日志，排查是否有人尝试向 commits 接口传入路径穿越参数。

```
# 扫描 Nginx 访问日志中匹配 /repository/commits/ 且携带 file.Path 的异常 POST 请求
grep -Ei "POST.*/api/v4/projects/.*/repository/commits" /var/log/gitlab/nginx/gitlab_access.log | grep -Ei "file\.Path|\.\./"
```

**2. 应急处置与加固落地清单：**

① **立刻拉齐补丁：**根据当前实例的大版本分支，立刻升级至 19.3.2、19.2.6 或 19.1.8；

② **临时切断公开可见性：**若因业务窗口期无法立即重启升级，管理员应临时将所有公开仓库（Public Projects）修改为内部（Internal）或私有（Private），直接破坏攻击利用链的前提条件；

③ **收缩公网暴露面：**禁止将企业自建 GitLab 管理端口与 API 直接暴露在裸公网，应强制接入内网 VPN 或零信任安全网关。

***END***

阅读推荐

[【安全圈】思科防火墙FMC曝满分漏洞：免密直取Root遭勒索攻陷](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652078830&idx=2&sn=552967b4aa41758e08d40d2c71bd56ca&scene=21#wechat_redirect)

[【安全圈】JFrog制品库曝组合漏洞：免密换取Admin凭据篡改依赖](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652078830&idx=3&sn=ae55fabe5ad167e850024e3d3f9b890b&scene=21#wechat_redirect)

[【安全圈】豆包又崩了！！！](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652078814&idx=1&sn=4bb4de8f89d37090d16af701bb3151a7&scene=21#wechat_redirect)

[【安全圈】JumpServer曝高危越权漏洞：普通用户发请求可窃管理员AK](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652078814&idx=2&sn=377865fd1deaae1b0ff7ae47552a4242&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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