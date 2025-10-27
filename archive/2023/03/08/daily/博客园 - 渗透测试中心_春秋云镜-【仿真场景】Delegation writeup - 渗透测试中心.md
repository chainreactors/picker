---
title: 春秋云镜-【仿真场景】Delegation writeup - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/17187378.html
source: 博客园 - 渗透测试中心
date: 2023-03-08
fetch_date: 2025-10-04T08:55:16.234395
---

# 春秋云镜-【仿真场景】Delegation writeup - 渗透测试中心

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

# [春秋云镜-【仿真场景】Delegation writeup](https://www.cnblogs.com/backlion/p/17187378.html "发布于 2023-03-07 11:11")

## 0x1 Info

![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307111012281-1611145621.png)
靶场地址：https://yunjing.ichunqiu.com/ranking/summary?id=BzMFNFpvUDU 从web到内网再到域的靶场环境都全，且出题的思路很好，感兴趣的可以去玩玩

## 0x2 Recon

1. Target external IP
   `39.98.34.149`
2. Nmap results
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307111013018-1994290663.png)
3. 关注80端口的http服务，目录爆破（省略）找到 /admin
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307111013771-683340567.png)
4. 使用弱口令登录进入后台，去到模板页面，编辑header.html，添加php一句话
   \

   ```
   用户名: admin, 密码：123456
   ```

![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307111014563-523612405.png)

1. 命令执行
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307111015323-735890634.png)

## 0x03 入口点：172.22.4.36

1. 弹shell
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307111016092-732592990.png)
   快速过一下：
   * 入口机器没特别的东西
   * 没能提权到root权限（也不需要提权到root权限）
   * stapbpf suid利用失败

     找到diff suid
     ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307111016857-359466286.png)
2. flag01
   `diff --line-format=%L /dev/null /home/flag/flag01.txt`
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307111017663-2014746256.png)
3. flag01 里面有提示用户名
   `WIN19\Adrian`
4. 挂代理扫 445
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307111018401-1731727318.png)

   获取到三个机器信息

   172.22.4.19 fileserver.xiaorang.lab
   172.22.4.7 DC01.xiaorang.lab
   172.22.4.45 win19.xiaorang.lab
5. 用 Flag01提示的用户名 + rockyou.txt 爆破，爆破出有效凭据 (提示密码过期)

   `win19\Adrian babygirl1`
6. xfreerdp 远程登录上 win19 然后改密码
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307111019537-1814451092.png)
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307111020840-719422388.png)

## 0x04 Pwing WIN19 - 172.22.4.45

前言：当前机器除了机器账户外，完全没域凭据，需要提权到system获取机器账户

1. 桌面有提示
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307111021701-1881902141.png)
2. 关注这一栏，当前用户Adrian对该注册表有完全控制权限
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307111022625-805434115.png)
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307111023436-71797962.png)
3. 提权
   msfvenom生成服务马，执行 sam.bat
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307111024192-439128100.png)

   sam.bat
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307111024902-2054700660.png)

   修改注册表并且启用服务，然后桌面就会获取到 sam，security，system
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307111025720-844847027.png)
4. 获取 Administrator + 机器账户 凭据

   Administrator:500:aad3b435b51404eeaad3b435b51404ee:ba21c629d9fd56aff10c3e826323e6ab:::
   $MACHINE.ACC: aad3b435b51404eeaad3b435b51404ee:917234367460f3f2817aa4439f97e636

   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307111026599-2118355643.png)
5. flag02
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307111027517-837571057.png)
6. 使用机器账户收集域信息
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307111028372-786215835.png)

## 0x05 DC takeover - 172.22.4.7

1. 分析 Bloodhound，发现 WIN19 + DC01都是非约束委派
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307111029250-262578989.png)
2. 使用Administrator登录进入 WIN19，部署rubeus
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307111030106-1114898806.png)
3. 使用DFSCoerce强制触发回连到win19并且获取到DC01的TGT
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307111030890-1203152302.png)
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307111031925-1979811480.png)
4. Base64的tgt 解码存为 DC01.kirbi
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307111033057-1510149895.png)
5. DCSync 获取域管凭据
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307111034392-1202387932.png)
6. psexec - flag04
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307111035397-1270368273.png)

## 0x06 Fileserver takeover - 172.22.4.19

1. psexec - flag03
   ![image](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307111036423-1841112756.png)

## 0x07 Outro

* 感谢Alphabug师傅的提示（0x03 - 0x04），大哥已经把入口点都打完了，我只是跟着进来而已
* 感谢九世师傅的合作

原文链接：https://www.freebuf.com/articles/web/352151.html

posted @
2023-03-07 11:11
[渗透测试中心](https://www.cnblogs.com/backlion)
阅读(656)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025