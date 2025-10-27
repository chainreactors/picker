---
title: 实战|内网中vcenter集群攻击全程实录，学会你也行！
url: https://forum.butian.net/share/4091
source: 奇安信攻防社区
date: 2025-02-08
fetch_date: 2025-10-06T20:33:57.019499
---

# 实战|内网中vcenter集群攻击全程实录，学会你也行！

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 实战|内网中vcenter集群攻击全程实录，学会你也行！

* [渗透测试](https://forum.butian.net/topic/47)

内网中vcenter集群攻击过程详细记录，学会你也行！

#### 前言
最近在做项目的时候，测到了一个部署在内网的存在漏洞的vCenter集群，这不巧了，正好最近在研究这vCenter、域这些集控类设备的打法，于是做了详细记录，有很多碰到的问题和解决办法，大佬勿喷哈哈。
#### vCenter服务器权限获取
内网信息搜集过程中fscan扫描报告显示存在一套vCenter服务器，并且其存在RCE漏洞cve-2021-21972：
```php
[+]https://内网IP poc-yaml-vmware-vcenter-unauthorized-rce-cve-2021-21972
```
![1.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-175fe8c2cc33550bc1dec15ee186ffae8ef2b380.png)
一般而言，进行vCenter攻击首先要确定版本、搜集域名，其中域名获取方式分为两种：一是通过LDAP匿名绑定获取目标域名，二是通过HTTP重定向获取域名，这里采用第二种方式。有个小技巧就是利用密码喷洒规避SSO登录锁定策略可以用来爆破普通用户密码。这里因为存在rce漏洞，是可以直接用exp打下来的。
我们首先利用CVE-2021-21972漏洞成功获取普通用户权限的webshell，但是无法提权为root
![2.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-67be63ecf481f5a8810bdef102a03164a2008036.png)
然后尝试利用CVE-2021-3156漏洞提升为root权限
[https://github.com/HynekPetrak/HynekPetrak/blob/master/take\\_over\\_vcenter\\_670.md](https://github.com/HynekPetrak/HynekPetrak/blob/master/take\_over\_vcenter\_670.md)
[https://raw.githubusercontent.com/worawit/CVE-2021-3156/main/exploit\\_userspec.py](https://raw.githubusercontent.com/worawit/CVE-2021-3156/main/exploit\_userspec.py)
但是第一次执行时遇到错误
![3.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-a38f1a11ecfa74aa6c27b60344a71ba53d0a1e5a.png)
分析后发现是脚本执行到628行打开/dev/null权限不足，直接修改脚本
![4.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-4029c749bc5601bf94b3279d7e9ca65423575493.png)
发现null\\_fd并没有什么用，仅仅具有日志记录的作用，于是将其改为1.txt
![5.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-40e78780832c1b46451d0c96a246588fe91c855b.png)
在上次报错的位置再次运行提权脚本，最终创建了一个gg用户（管理员权限，密码gg）,可以su到root账户上，至此提权成功！
再次备份木马到隐藏目录下，访问路径为https://内网IP/idm/..;/update.jsp 重新用哥斯拉连接之，这样就成功获取root权限的webshell
![6.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-4b6076d1b388c9b5e1f8fd3544bf710465bcdba4.png)
查看/etc/shadow获取root密码密文内容
```php
root:$6$QL15TDCu$8HetMyfCTNW6LDS5XKb0yvY7SZqxa55PExH9SKb1pjnzSr/4yVBkOQLAghKwWah3NuqxWIaSFJZ//:0:0:365:7:::
```
这里直接放到在线破解网站发现无法破解，只能先保存下来后面有时间可以破解之，尽管没有破解出明文也是不影响后面的攻击流程的。
#### vCenter控制台权限获取
我们知道vCenter控制台管理了众多的ESXI虚拟机，这些都是业务系统载体，是我们攻击方非常感兴趣的点。为此我们要通过vCenter后台服务器权限来绕过SAML登录，基本思路是：
```php
vCenter SSO：
1. 用户访问vCenter
2. vCenter生成SAML Request，通过浏览器携带参数重定向到Idp地址
3. 用户在Idp地址完成认证
4. Idp生成SAML Response(包含身份断言，签名)，通过自动门提交表单将其发送
给vCenter
5. vCenter 对 SAML Response 的内容进行检验，通过后返回session cookie
6. 用户成功登录
```
为了进一步获取vCenter控制台管理权限，下面利用三好学生脚本vCenterLDAP\\_Manage.py按照步骤：获取域控信息-&gt;添加新用户admin-&gt;将新用户加入管理员组中
可以在github上下载三好学生的利用脚本
[https://github.com/3gstudent/Homework-of-Python/blob/master/vCenterLDAP\\_Manage.py](https://github.com/3gstudent/Homework-of-Python/blob/master/vCenterLDAP\_Manage.py)
获取域控信息
![7.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-351d3375204185c86030f631b5bcb136e8e26fd2.png)
添加新用户admin
![8.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-e9575a7dcdc0935c9c9fa7cf8728ba63b71d9513.png)
将新用户加入管理员组中
![9.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-51a232697cb7d35c5c53526007a5f71688b2db25.png)
成功添加管理员admin，最终的vcenter管理员账号admin@ZXZ.COM.local/P@ssWord123
最终成功登录vcenter web控制台界面如下：
![10.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-6b75a925a26838e8404e60f28d3cd25dd9444f6e.png)
该vCenter服务器管理68台服务器，存在一个域环境ZXX.COM，锁定域控机器Win2k8R2\\_DC。如何拿到该域控制器管理员密码呢？
#### 攻击域控
首先克隆域控所在的虚拟机。通过菜单Actions-&gt;Clone-&gt;Clone to Virtual Machine...命名为Win2K8R2\\_Test，然后稍等一会儿就成功克隆该虚拟机。
![11.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-c43038116d83baa234e6700c612fd2269bd5b80a.png)
在网上下载一个启动盘镜像kon\\_boot.iso到本地，点击菜单编辑虚拟机，在虚拟机硬件出展开CD/DVD drive 1选择挂载CD/DVD为kon\\_boot.iso即可，最后启动克隆虚拟机
![12.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-5f7a48a13231aad0b0deb363a49c218366ce9b73.png)
启动成功后连续按5下shift弹出cmd.exe，添加管理员
![13.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-f5621ad8445d1b057963ac12519af4e92ea5bd58.png)
至此就能够登录该域控克隆主机
![14.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-79e7d577587a5c79de2e866987838ce4a297c9d1.png)
总结一下上述攻击过程为：克隆虚拟机-&gt;挂载CD/DVD为kon\\_boot.iso-&gt;利用shift后门弹出cmd.exe并添加管理员用户-&gt;登录域控克隆主机。
#### 域内信息搜集
利用上面步骤中 vcenter服务器攻击最后添加的账号test/Admin@123进入域控克隆主机，进行域内信息搜集：
![15.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-ed19034eed2c814411f9988d05c5f15c0d4a0dd2.png)
利用mimikatz导出所有用户hash，利用CMD5在线破解成功用户ZXX.COM\\backupuser明文密码为admiN@123
![16.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-474b19fbff7557f5829f6ab712e574481cf4c70a.png)
值得注意的是backupuser是域管理员权限，利用账号backupuser/NNN@123登录真正的域控主机
![17.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-f4c7c2ee99ca5abdb171758bd36dc51fc1ce5004.png)
利用impacket工具模块secretsdump再次抓取域内所有用户hash
![18.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-5cc5b4d7094d743300d9d5a5f046cd8ac01206d6.png)
#### 域内横向移动
域内主机A
通过域管账号backupuser登陆域内主机A，利用横向移动工具Impacket wmiexec+net use进入命令行界面，上传密码抓取工具GetPass\\_x64获得明文密码为administrator/TTT@321，也可以上传免杀木马并执行，上线后抓取hash及明文密码
![21.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-06478b2f7994c752b2e0c29b43d106b68f62b1ec.png)
以管理员帐号登录远程桌面后，发现文件夹Share存在大量技术文档
![22.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-7c0095e76a79f98feeaaecb70a6223884f6afdd4.png)
域内主机B
该主机是一台文件存储服务器，利用横向移动工具Impacket wmiexec+net use上传免杀木马并执行，上线后抓取hash及明文密码
![23.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-bb4c4f243530331efb5bc57a76d2c97c6660623e.png)
开启远程桌面的cmd指令
```php
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG\_DWORD /d 0 /f
```
防火墙开放端口3389
```php
netsh advfirewall firewall add rule name="Remote Desktop" protocol=TCP dir=in localport=3389 action=allow
```
开启3389端口后，以管理员帐号成功登录远程桌面
![24.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-8968f8190ff2dde09ecbd6bd92edde6a6e381fca.png)
#### 总结
最后通过攻防两个侧面来谈谈vCenter：
对于红队而言，vCenter人送外号小域控，拿下vCenter之后，不单单只是获取一台服务器的权限，vCenter中存在的虚拟机以及ESXI主机都有可能成为后续的攻击目标，因此拿下vCenter的价值不亚于域控的价值。
对于运维管理人员来说要实时关注vCenter操作系统自身的安全漏洞，要确保漏洞能 够及时发现，并能够及时打补丁,以积极应对来自终端层面的攻击威胁。

* 发表于 2025-02-07 11:08:44
* 阅读 ( 5212 )
* 分类：[渗透测试](https://forum.butian.net/community/Pen_Testing)

2 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![青橄榄](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/11376)

[青橄榄](https://forum.butian.net/people/11376)

1 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2023 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

×

#### 发送私信

请先 [登录](https://forum.butian.net/login) 后发送私信

×

#### 举报此文章

垃圾广告信息：
广告、推广、测试等内容

违规内容：
色情、暴力、血腥、敏感信息等内容

不友善内容：
人身攻击、挑衅辱骂、恶意行为

其他原因：
请补充说明

举报原因:

取消
举报

×

#### ![青橄榄](https://forum.butian.net/static/images/default_avatar.jpg)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![]()

---