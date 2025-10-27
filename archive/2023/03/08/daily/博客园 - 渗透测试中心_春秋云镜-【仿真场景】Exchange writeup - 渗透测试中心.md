---
title: 春秋云镜-【仿真场景】Exchange writeup - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/17187366.html
source: 博客园 - 渗透测试中心
date: 2023-03-08
fetch_date: 2025-10-04T08:55:16.580205
---

# 春秋云镜-【仿真场景】Exchange writeup - 渗透测试中心

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

# [春秋云镜-【仿真场景】Exchange writeup](https://www.cnblogs.com/backlion/p/17187366.html "发布于 2023-03-07 11:09")

## 0x00 Intro

1. OSCP 渗透风格，脱离C2和MSF之类的工具
2. Box 难度不高

## 0x01 Info

* Tag: JDBC, Exchange, NTLM, Coerce Authentication, DCSync
  ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110820305-1199450069.png)

## 0x02 Recon

1. Target external IP
   `39.98.179.149`
2. Nmap results
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110821647-1232626705.png)
3. 直接关注8000端口，前面我已经怼过80了，没东西直接过
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110823014-561855854.png)
4. 华夏ERP，有很多漏洞的，入口点卡了很久，后面看到JDBC，直接谷歌一搜就搜到大哥的文章了
   Fastjson高版本的奇技淫巧 – Bmth (bmth666.cn)(<http://www.bmth666.cn/bmth_blog/2022/10/19/Fastjson%E9%AB%98%E7%89%88%E6%9C%AC%E7%9A%84%E5%A5%87%E6%8A%80%E6%B7%AB%E5%B7%A7/#%E8%93%9D%E5%B8%BD%E6%9D%AF2022%E5%86%B3%E8%B5%9B-%E8%B5%8C%E6%80%AA>)
5. 构造payload
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110823723-696025461.png)
6. Configure MySQL\_Fake\_Server
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110824711-1908553648.png)
7. 未授权 + MySQL Connector JDBC反序列化组合拳直接RCE
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110825622-1322089599.png)
8. RCE后直接获取 Flag01
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110826678-1287995891.png)

## 0x03 入口点：172.22.3.12

1. SMB扫描内网主机，看到Exchange关键字 (EXC01)，尝试访问
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110827628-653997110.png)
2. 172.22.3.9 为 Exchange
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110828408-1266989652.png)
3. Proxylogon 直接打死，获取system权限
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110829291-379517543.png)
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110830544-277141853.png)
4. flag02（后续凭据收集略过）
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110831532-1203973464.png)

## 0x04 入口点：172.22.3.9

* 快进1：已经收集到了exchange机器账户的hash
* 快进2：同时收集到了一个域账户凭据：Zhangtong

1. 这边已经通过上面的操作收集到了exchange的机器账户hash，exchang的机器账户在域内对整个domain-object有writedacl权限，那我们直接使用dacledit.py给Zhangtong加dcsync权限（其实你也可以给自己加上dcsync）
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110832361-1225469485.png)
2. Dcsync，获取到域管和用户lumia的hashes
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110833456-2099783471.png)
3. 进入 172.22.3.2 获取flag04
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110834415-1664088831.png)

## 0x05 Final：172.22.3.26

1. 172.22.3.26上面的Lumia用户文件夹里面有个secret.zip
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110835561-987580207.png)
2. 直接PTH Exchange导出Lumia mailbox里面的全部邮件以及附件
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110836615-702315992.png)
3. item-0.eml，提示密码是手机号
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110837493-1963104690.png)
4. 刚好导出的附件里面有一个csv，里面全是手机号
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110838181-1270837852.png)
5. 常规操作，转换成pkzip格式的hash再跑字典，跑出密码
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110838972-1929033796.png)
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110839731-1408984704.png)
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110840551-1868894190.png)
6. flag03
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110841247-1248332368.png)
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110842067-1310219407.png)

## 0x06 Outro

1. Exchange 后渗透那，作者本意是想让我们用 NTLM Relay去完成DCSync提权，获取Exchange SYSTEM权限后，触发webdav回连中继到ldap，这里的话就不尝试了，有兴趣的话可以看我上一篇文章 Spoofing

2.Lumia用户登录exchange那，作者也是想让你改掉Lumia用户的密码，但是我就懒了，直接PTH

原文链接： <https://www.anquanke.com/post/id/286967>

posted @
2023-03-07 11:09
[渗透测试中心](https://www.cnblogs.com/backlion)
阅读(1073)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202508/35695-20250830121216742-1062949948.jpg)](https://developer.huawei.com/consumer/cn/activity/digixActivity/digixcmsdetail/101750143863263087?ha_source=BKYQ3&ha_sourceId=89000408)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025