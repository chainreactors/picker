---
title: 春秋云镜-【仿真场景】Tsclient writeup - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/17187342.html
source: 博客园 - 渗透测试中心
date: 2023-03-08
fetch_date: 2025-10-04T08:55:17.415412
---

# 春秋云镜-【仿真场景】Tsclient writeup - 渗透测试中心

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/backlion/)

# [渗透测试中心](https://www.cnblogs.com/backlion)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/backlion/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%AD%E5%BF%83)
* [管理](https://i.cnblogs.com/)
* 订阅
  [![订阅](/skins/coffee/images/xml.gif)](https://www.cnblogs.com/backlion/rss/)

# [春秋云镜-【仿真场景】Tsclient writeup](https://www.cnblogs.com/backlion/p/17187342.html "发布于 2023-03-07 11:03")

## 0x1 Info

* Tag:
  MSSQL，Privilege Escalation，Kerberos，域渗透，RDP
  ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110259333-549860048.png)
  靶场地址：https://yunjing.ichunqiu.com/ranking/summary?id=BzMFNFpvUDU

## 0x2 Recon

1. Target external ip
   `47.92.82.196`
2. nmap
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110300682-1162543153.png)
3. MSSQL 弱口令爆破，爆破出有效凭据，权限为服务账户权限（MSSQLSERVER）
   `sa:1qaz!QAZ`
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110301582-1376953214.png)

## 0x3 入口点 MSSQL - 172.22.8.18

* 前言，该机器不在域内

1. 直接MSSQL shell（这里做完了忘记截图了..）
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110302266-1569608829.png)
2. 提权，这里直接获取Clsid暴力怼potato（前面几个clsid是用不了的）

   修改GetClsid.ps1，添加执行potato
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110303088-310600875.png)

   Potato和GetClsid.ps1
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110303895-691003509.png)

   执行GetClsid.ps1
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110304882-970189786.png)

   获取到有效clsid以及命令执行结果
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110305695-1163714298.png)
3. 导出SAM，SYSTEM，Security
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110306566-224206839.png)

   解出凭据，用administrator + psexec 139横向（外网没有开445）就能获取到 flag01
   `administrator 2caf35bb4c5059a3d50599844e2b9b1f`
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110307433-679873801.png)
4. qwinsta和端口连接看到有机器rdp过来
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110308193-736893816.png)
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110308949-1990767440.png)
5. 这边使用administrator psexec后上msf（system权限），使用incognito模块，模拟至john（本人实测，只有msf的incognito能完成后续操作，f-secure lab等其他的模拟令牌工具没成功）
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110309911-833847510.png)
6. 使用john的token执行 net use 看到 \\tsclient\C 共享
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110310986-1363833566.png)
7. 直接获取 \\tsclient\C 下面的 credential.txt，同时提示 hijack image (镜像劫持)
   `xiaorang.lab\Aldrich:Ald@rLMWuy7Z!#`
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110311788-427566290.png)

* 快进，略过搭建代理过程

1. CME 扫描 172.22.8.0/24，有三个机器提示密码过期了
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110312492-1853626447.png)
2. 测试一下 DC01 88端口是否开启（测是否域控），DC01为域控
3. smbpasswd.py 远程修改一下过期密码，改成111qqq...
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110313206-571546994.png)
4. ldapshell.py 验证，登录域成功
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110313915-485783230.png)
5. CME 枚举 RDP，显示能登录进入 172.22.8.46（用CME官方的RDP模块不会扫出有效RDP凭据，这边自己写了一个基于xfreerdp的CME模块）
   [XiaoliChan/CrackMapExec-Extension](https://github.com/XiaoliChan/CrackMapExec-Extension)
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110314779-1318824357.png)

## 0x4 域渗透 - 入口 - 172.22.8.46

1. 登录进入，查看到 xiaorang.lab\Aldrich 不是这台机器的管理员，只是普通用户

* 提权，两种方法

  Priv-ESC1：镜像劫持提权（常规）

  Get-ACL查看到任何用户都可以对注册表 "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options" 进行写入，创建操作
  ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110315643-1017949705.png)

  创建一个劫持magnify.exe（放大镜）的注册表，执行CMD.exe
  ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110316454-773861417.png)

  锁定用户
  ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110317362-1869427212.png)

  点击放大镜
  ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110318282-1365782290.png)

  提权至system
  ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110319196-572104112.png)

  Priv-ESC2：krbrelayup提权

  域普通权限用户在域内机器，直接带走（非常规，推荐）
  ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110320037-641362153.png)
  ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110320889-988840085.png)

1. 快进mimikatz，获取到当前机器的机器账户 win2016$

```
xiaorang.lab\WIN2016$ 4ba974f170ab0fe1a8a1eb0ed8f6fe1a
```

## 0x5 域渗透 - DC Takeover

* 两种方法

1. 观察 WIN2016$ 的组关系，发现处于 Domain Admins 组，直接使用 Dcsync 带走 DC01 （过程略）
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110321677-1499424111.png)
2. 约束委派（非常规）

   Bloodhound收集域信息，分析，发现存在约束委派
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110322338-1637270297.png)

   使用 getST.py 进行约束委派攻击
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110322989-1561042099.png)

   带走 DC01
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110323735-1632474545.png)

##

原文链接： <https://www.freebuf.com/articles/system/352237.html>

posted @
2023-03-07 11:03
[渗透测试中心](https://www.cnblogs.com/backlion)
阅读(711)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025