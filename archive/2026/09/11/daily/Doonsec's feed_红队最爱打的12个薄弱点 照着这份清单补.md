---
title: 红队最爱打的12个薄弱点 照着这份清单补
url: https://mp.weixin.qq.com/s/093kFDOPrAs8GIFc-eKsGA
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:44:17.206915
---

# 红队最爱打的12个薄弱点 照着这份清单补

# 红队最爱打的12个薄弱点 照着这份清单补

宝十八
宝十八

网络安全老宋

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**导语：** 你好，我是网络安全老宋。安全攻防干货准时送达！

网络安全老宋// 攻防演练 · 加固清单

// 攻防演练 · 甲方运维

# 红队最爱打的12个薄弱点 照着这份清单补

把攻击手册翻过来，就是一份能落地的加固清单

甲方运维加固清单攻防演练

🔑 一句话精华：红队不打你的强点，专挑你没盯住的口子——这份清单，就是照着红队思路反过来堵。

![](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93fl8AYMQo0iaMhbSZItgJmzX4HHh6v95RwcFaf4pZYfd0mjFQ4PxNdQILiaGSxgDm2LrkTx26xuACGmVxzptolDYevOGDBZHHnPeKM/640?wx_fmt=png&from=appmsg)

你昨天刚部署完新系统，觉得自己边界防火墙、WAF、EDR 都齐了，应该稳了。问题在于，护网演练里 90% 以上的单位，不是被"正面突破"打穿的，是被红队顺着一条没人管的测试系统、一个弱口令 VPN、一个忘了下线的旧后台，悄无声息摸进内网的。

那两篇《红队攻击手册》上下篇，把攻击路径写得明明白白。甲方运维看完最容易犯的错，是觉得"那是攻击方的事"。错了。手册里列的每一个"防守方薄弱点"，翻过来就是一条你今天就能照着改的加固项。这篇文章不跟你讲攻击多厉害，只干一件事：把那 12 类薄弱点，逐条翻译成你周一上班就能执行的命令和配置。

转发给你负责服务器的同事，他们最需要看到。

## 01边界暴露面：你根本不知道自己暴露了多少

红队的 reconnaissance 阶段，第一件事不是攻，是"数你家门口开了几扇门"。他们用 fofa、shodan、证书透明度日志，把你没报备的资产全翻出来：测试环境、忘记下线的旧系统、开发自己搭的 GitLab、一个写着 admin 的后台管理页。

💡 **注意：**很多单位的内网系统，因为"反正不对外"就裸奔在公网 IP 上，红队一扫描就进来了，连边界都没碰到。

**你该怎么补**：先把资产摸清，再做暴露收敛。

⏺ Bash · 暴露面自检

# 用 nmap 自己扫一遍对外端口，看哪些是不该开的

nmap -sS -Pn -p 1-65535 --open 你的公网IP段 | tee exposure.txt

# 重点看 22/3389/6379/27017/9200，公网一律不该开

收敛动作就三条：① 公网只留 80/443，其余端口全部上 ACL 或零信任代理；② 测试系统、演示系统一律不出公网，要访问走 VPN 内的隔离网段；③ 上线前强制"资产登记"，没人认领的 IP 自动断网。

## 02VPN 与远程接入：弱口令是红队最大的后门

手册里"VPN 弱口令破域控"是四大复盘场景之一。原因很直白：VPN 是进入内网的咽喉，一旦咽喉用 admin/123456 这种口令，红队爆破成功就等于拿到了内网入场券。

**你该怎么补**：双因素认证（2FA）必须开，口令策略必须硬。

⏺ OpenVPN · 双因子配置核对

# 确认证书+口令双因子已启用，禁用纯口令登录

grep -E "auth-user-pass-verify|plugin" /etc/openvpn/server.conf

落地口径：VPN、堡垒机、邮件系统，这三个入口没有 2FA 的，今年护网基本都会出事。口令长度拉到 12 位以上、强制 90 天轮换、连续 5 次失败锁账号。

![](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93flicGLfdzO81IzwKgPpLmojCh6cpRcPYx7ra31QHqXG9aFgHf6bGwpXibfdBBNbk4zBKyx7MqibDYrbURNHGBBtQqnGN9ZeEAt4N84/640?wx_fmt=png&from=appmsg)

## 03Web 应用：上传点和反序列化是重灾区

红队突破 Web 边界，最爱两件事：文件上传没校验后缀直接 getshell，以及反序列化/表达式注入拿权限。手册里点名的 OA、邮件系统，翻车基本都在这。

**你该怎么补**：上传目录禁执行，危险组件升级或卸载。

⏺ Nginx · 上传目录禁执行

location ^~ /upload/ {

location ~\* \.(php|jsp|asp|aspx)$ { return 403; }

}

nginx -t && nginx -s reload  # 改完重载，别直接 restart

## 04内网隔离：一张大扁平网络等于敞开家门

红队进内网之后能横向乱跑，根子在"东西向零隔离"。一台跳板机拿下，整个网段都是它的。手册里"内网横移"那章，前提是你的网络是通的。

💡 **注意：**域控、数据库、核心业务系统，必须放在独立网段，和办公网、开发网物理或逻辑隔离，否则一台办公机中招就直连域控。

核心动作：① 域控 389/636、数据库 1433/3306 端口，只允许特定管理段访问；② 关闭不必要的 SMB（445）、RDP（3389）横向端口；③ 上主机防火墙，默认拒绝、按需放行。

## 05域环境：域管账号是红队的终极目标

Zerologon、Kerberoasting、ADCS 提权，手册里写了三种打域控的路子。它们的共同前提：域环境里权限乱给了，服务账号被加了域管，或者证书服务配置有漏洞。

⏺ PowerShell · 域管与SPN核查

Get-ADGroupMember "Domain Admins" | Select Name  # 应极少

setspn -T %USERDOMAIN% -Q \*/\*  # 查高权限SPN

落地：域管组控制在 3 人以内，日常运维用普通账号 + 提权跳转；服务账号禁止加入特权组；ADCS 若不用就关掉，要用就打补丁、收紧模板权限。

## 06终端：没有 EDR，等于裸奔

红队在终端上做的提权、免杀、持久化，靠的是你装了杀软却没开行为监控。传统杀软只对已知特征报警，红队换个免杀壳就过了。

⏺ Bash · EDR Agent 健康核对

systemctl status edr-agent          # 看是否 active

tail /opt/edr/logs/health.log       # 看心跳和策略下发

终端至少做到：EDR 全覆盖、本地管理员账号回收（员工别用 admin 日常办公）、PowerShell 约束语言模式开启、宏脚本默认禁用。

## 07弱口令：全场景的万能钥匙

这是最老套也最管用的突破口。数据库、Redis、MongoDB、Tomcat 后台、路由器，默认口令和弱口令遍布。手册里钓鱼破 OA、VPN 破域控，底层都是弱口令。

⏺ Hydra · 授权内弱口令扫描

hydra -L user.txt -P top1000.txt ssh://10.10.10.10 -t 4

# 扫出来的弱口令账号，强制首次登录改密

别只盯 SSH。Redis 没设密码、MongoDB 无鉴权、Tomcat manager 用弱口令，这些在红队眼里都是送分题。

## 08多因素认证：开了不等于管用

有些单位 2FA 开了，但把"记住设备 30 天"开到最大，或者短信验证码能被拦截/重放，等于没开。手册里没细写，但这是真实演练里常被绕过的点。

**你该怎么补**：2FA 用 TOTP/硬件 Key，别依赖短信；关键系统不勾"信任设备"。

## 09最小权限：服务账号变内鬼

一个 Web 服务被拿下，结果它跑在 root 上，红队直接就是系统权限。最小权限原则说了十年，落地的没几个。

⏺ Bash · 服务降权运行

useradd -r -s /sbin/nologin appuser

chown -R appuser:appuser /opt/myapp

# service 文件写 User=appuser

## 10监测与响应：看不见，就谈不上防

手册里"监测响应薄弱"这条，很多单位的理解是"我装了 SIEM"。但日志没全量收集、告警没人看、事件没人研判，等于监控室没人值班。

⏺ Bash · 日志采集与关键事件

systemctl status filebeat         # 确认采集器在线

grep -E "Failed password|useradd" /var/log/secure | tail

建议先把三类日志收全：认证日志、权限变更日志、外连连接日志。再配几条高频告警：短时间内大量失败登录、非工作时间新增域管、服务器主动外连陌生 IP。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yJLbez93flictpUW47LgIjufeZ8cAsCFSyaJzl7duWwe1TO4zFPGwtKo3Hiat5x87ychhHp2gNjJbZ3DqJlXia9sVVLjWNW7Yn3ibnPCCRibD7M4/640?wx_fmt=png&from=appmsg)

## 11数据安全：备份没隔离，等于没备份

红队现在流行加密或删你的备份，逼你就范。很多单位备份和 production 在同一个域、同一个网络，红队顺着权限一路把备份也端了。

💡 **注意：**备份恢复演练一年至少做一次，别到了出事才发现备份文件是坏的。

**你该怎么补**：3-2-1 备份，备份机离线或独立鉴权，定期演练恢复。

## 12配置基线：镜像自带后门你都不知道

最后这条最隐蔽。很多单位用公开镜像、第三方模板批量装机，里面可能带着后门账号、开着不必要的服务。手册提到"供应链破核心系统"，底层逻辑一样。

⏺ Bash · 安全基线检查

lynis audit system --quick               # 基线检查

oscap xccdf eval --profile cis scan.xml   # CIS 基线评估

// 老宋说：这件事真正的根子，不在缺哪台设备，而在"没人替资产负责"。红队能打穿，往往是因为那台测试机、那个旧后台，上线时没人登记、下线时没人管，权限散着给、日志散着丢。

行业里有个怪现象：安全预算花在"看得见"的盒子上，资产台账、口令治理、日志闭环这些"看不见"的活儿一直没人接。等演练一复盘，问题全在后者。

你现在能做的，不是立刻买新平台，而是把这 12 条里标号 02、07、10 的先改了——VPN 双因子、全量弱口令整改、日志收起来有人看，这三件事做完，能挡掉演练里至少七成的自动化突破。

改配置前先备份，命令都带注释，照着敲不会错。这份清单收藏好，下次护网自查直接用。

防御，不是在演练期间发现攻击，而是在演练开始前就把攻击面收敛到最小。

end

不想错过文章内容？读完请点一下**“在看**![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/4hgdCZdc8jUczamtqCrTy0y1qxtj2D4su6J9PETsVrjWFibSzm7JzZEXeaJeovtAiaIWVQiclhQuENTqFwTzwUH8w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&wx_co=1&randomid=g5u115ni&tp=webp#imgIndex=1)******”**，加个**“****关注”**，您的支持是我创作的动力

期待您的一键三连支持（点赞、在看、分享~）

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sowcUpcXRY07WiafrWPnt0icqSjEOPqweHgqfN5sMGTgMPP5yciaeNiaPx8oJtcS4I6dCcBUL6q4JOY9jNalwkxmZQ/0?wx_fmt=png)

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