---
title: HVV面试!红蓝对抗10连问
url: https://mp.weixin.qq.com/s/k3cAWQ2tZgoGpMG6KmOwkQ
source: Doonsec's feed
date: 2026-07-08
fetch_date: 2026-07-09T06:00:39.267329
---

# HVV面试!红蓝对抗10连问

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/N46S2sKsyIDvoGw2QnhDDvfgID1p5NcibnfBEtVNqlXq5el4ytWWXlT0TWSTzLaBCZodmHmfkLQPnonIWd7TK783mfe0BHK5nRzDZff0hGao/0?wx_fmt=jpeg)

# HVV面试!红蓝对抗10连问

原创

ladon
ladon

306Safe

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

护网面试到了中高级阶段，面试官不再问你"SQL注入有几种类型"，而是问你"拿到一个webshell后怎么横向移动"、"黄金票据和白银票据什么区别"、"如何做安全加固"。这些题考的是你的实战深度和体系化思维。本文整理10道进阶真题，助你拿下中高级岗。

## 一、拿到WebShell后的完整渗透思路？

**答：**

这道题考的是内网渗透的体系化思维，不能零散回答：

**第一步：信息收集**：

* whoami /priv：查看当前权限和特权
* ipconfig /all：查看网络配置，判断是否在域内
* net user / net localgroup administrators：查看本机用户和管理员
* net view / net group "domain computers"：查看域内主机（如在域内）
* systeminfo：查看系统版本和补丁情况

**第二步：权限提升**：如果当前权限不足，尝试提权（系统漏洞提权/服务提权/数据库提权/令牌窃取）。

**第三步：权限维持**：

* 新建隐藏管理员账户（用户名以$结尾）
* 植入SSH公钥到authorized\_keys
* 添加计划任务（schtasks/crontab）
* 植入内存马（Filter/Servlet型）

**第四步：内网探测**：使用代理工具（frp/nps/CS SOCKS代理）建立隧道，通过nmap/fscan扫描内网网段，发现内网服务和存活主机。

**第五步：横向移动**：利用445/SMB（永恒之蓝）、RDP、SSH弱口令、数据库弱口令、域渗透（Pass the Hash/Pass the Ticket）等手法渗透其他主机。

**第六步：目标达成**：获取域控权限或核心数据，完成演练目标。

## 二、黄金票据和白银票据的区别？

**答：**

这是域渗透面试的必考题：

**黄金票据（Golden Ticket）**：

* 本质：伪造的TGT（Ticket Granting Ticket）
* 需要的信息：域名 + 域SID + krbtgt账户的NTLM Hash + 伪造的用户名
* 权限：拥有全域管理员权限，可以访问域内所有服务的所有资源
* 持久性：krbtgt密码很少变更，票据有效期可长达10年
* 前提：必须先获取krbtgt的Hash（通常需要域控权限或DCSync攻击）

**白银票据（Silver Ticket）**：

* 本质：伪造的ST（Service Ticket），即服务票据
* 需要的信息：域名 + 域SID + 目标服务账户的NTLM Hash + 目标服务SPN
* 权限：只能访问伪造票据对应的特定服务（如CIFS文件共享、LDAP目录服务等）
* 持久性：依赖服务账户密码，不涉及krbtgt
* 前提：需要知道目标服务账户的Hash（如计算机账户Hash）

**核心区别**：黄金票据伪造TGT→可访问所有服务；白银票据伪造ST→只能访问特定服务。黄金票据需要krbtgt Hash，白银票据需要服务账户Hash。黄金票据威力大但获取门槛高，白银票据获取门槛低但权限有限。

## 三、Pass the Hash（哈希传递）攻击原理？

**答：**

**原理**：Windows NTLM认证过程中，用户密码的NTLM Hash直接参与认证，而不是明文密码。攻击者获取到某用户的NTLM Hash后，可以直接使用该Hash进行认证，无需知道明文密码，从而访问该用户有权限的所有资源。

**利用场景**：

* 通过Mimikatz从LSASS进程提取用户Hash
* 使用impacket的psexec.py或wmiexec.py直接用Hash连接远程主机
* CrackMapExec批量验证Hash有效性并执行命令
* 在域环境中，域管Hash可横向移动到所有域内主机

**防御方案**：

* 启用Windows Credential Guard（基于虚拟化的凭据保护），隔离LSASS进程中的Hash
* 限制本地管理员账户的权限范围，避免相同密码多机复用
* 部署EDR监控Mimikatz等凭据窃取工具的运行
* 启用帐户保护策略，限制NTLM认证的使用

## 四、Windows提权的常见方式有哪些？

**答：**

提权是内网渗透的关键环节：

* **系统漏洞提权**

  ：利用未安装补丁的系统漏洞（MS16-032/MS15-051/CVE-2021-1732等），是最常用的提权方式
* **服务提权**

  ：以高权限运行的服务存在漏洞或配置不当（如MySQL UDF提权、SQL Server xp\_cmdshell、Redis写计划任务）
* **令牌窃取**

  ：使用Mimikatz的token::elevate窃取高权限令牌，或incognito列举和模拟可用令牌
* **DLL劫持**

  ：替换高权限程序加载的DLL，以高权限执行恶意代码
* **注册表提权**

  ：利用AlwaysInstallElevated策略（如果启用），普通用户可高权限安装MSI
* **计划任务提权**

  ：修改高权限计划任务执行的脚本路径
* **内核驱动漏洞**

  ：利用驱动程序的漏洞（如Win32k漏洞、打印驱动漏洞）

面试加分：提到"提权前先systeminfo看补丁，再找对应CVE"，说明你有实战经验。

## 五、Linux提权的常见方式有哪些？

**答：**

* **SUID提权**

  ：find / -perm -4000 -type f 2>/dev/null查找SUID文件，如find/nmap/vim/bash等具有SUID权限的程序可直接提权
* **内核漏洞**

  ：脏牛(CVE-2016-5195)、DirtyPipe(CVE-2022-0847)等内核漏洞，通过uname -a确认内核版本后选择对应EXP
* **Sudo配置不当**

  ：sudo -l查看当前用户可执行的sudo命令，如允许无密码执行vim/find/python等，可直接提权（sudo vim -c '!sh'）
* **Cron任务提权**

  ：查看/etc/crontab和/var/spool/cron，如果高权限的cron任务执行的脚本可写，则可注入恶意代码
* **能力(Capabilities)提权**

  ：getcap -r / 2>/dev/null查找具有cap\_setuid等危险能力的程序
* **Docker逃逸**

  ：如果当前用户在docker组中，可通过docker run -v /:/mnt --rm -it alpine chroot /mnt/shell获取宿主机root权限
* **计划任务路径劫持**

  ：cron任务使用相对路径时，可通过在搜索路径中放置同名恶意程序劫持执行

## 六、如何做安全加固？从操作系统到应用层

**答：**

安全加固是护网防守方的核心工作，面试官要看你的体系化思维：

**操作系统加固**：

* 关闭不必要的服务和端口，最小化安装
* 禁用默认账户（如Guest），修改默认密码，实施密码复杂度策略
* 开启日志审计（Windows事件日志/Linux rsyslog），配置日志远程备份
* 禁用SMBv1、Telnet等不安全协议
* 安装安全补丁，保持系统更新

**Web应用加固**：

* 部署WAF，配置SQL注入/XSS/文件上传等防护规则
* 中间件加固：Tomcat删除默认应用/禁用PUT/禁用manager，Nginx隐藏版本号/禁止目录遍历
* 数据库加固：禁用xp\_cmdshell/限制文件导出/修改默认端口/禁用远程root登录
* 代码层：输入校验 + 参数化查询 + 输出编码 + CSP策略 + HttpOnly Cookie

**网络层加固**：

* 最小化开放端口，非必要不暴露到互联网
* 内网分区隔离（DMZ/App/DB分段），限制横向流量
* 部署IDS/IPS，配置入侵检测规则
* 限制ICMP/SSH/RDP等协议的来源IP

## 七、域渗透的攻击思路？

**答：**

域渗透是高级岗必考：

**1. 域信息收集**：

* net time /domain：判断是否在域内，同时获取域控主机名
* net group "domain admins" /domain：获取域管列表
* nltest /dclist:domain\_name：获取域控列表
* AdFind / AdMod：LDAP查询工具，枚举域用户、计算机、组策略等

**2. 获取域控权限**：

* Pass the Hash：利用域管Hash直接访问域控
* Kerberoasting：请求服务ST票据，离线爆破服务账户密码
* AS-REP Roasting：针对不需要预认证的用户，获取AS-REP离线爆破
* DCSync攻击：利用DRS协议模拟域控复制，直接获取krbtgt Hash（需要域管权限或特定ACL）
* 利用域控漏洞：Zerologon(CVE-2020-1472)、PrintNightmare(CVE-2021-1675)等

**3. 权限维持**：

* 黄金票据：用krbtgt Hash伪造TGT，实现全域持久控制
* AdminSDHolder后门：修改AdminSDHolder ACL，自动传播权限到受保护组
* Skeleton Key：在域控注入万能密码，任何账户都可以用该密码登录
* DSRM后门：修改域控的DSRM管理员密码并同步为域管Hash

## 八、如何检测和防范内网横向移动？

**答：**

横向移动检测是蓝队高阶能力：

**检测手段**：

* **流量层面**

  ：监控445/SMB、3389/RDP、22/SSH等端口的异常连接（非工作时间的横向连接、短时间内大量主机互连），检测Pass the Hash的NTLM认证特征
* **日志层面**

  ：Windows事件ID 4624（登录类型3/10的异常远程登录）、4672（特权登录）、4688（可疑进程创建如mimikatz.exe/psexec.exe）
* **终端层面**

  ：EDR监控Mimikatz、PsExec、WMI远程命令执行等工具的使用，检测LSASS进程的异常访问
* **网络层面**

  ：部署微隔离策略，限制主机间的横向流量，异常流量自动告警

**防范方案**：

* 网络微隔离：限制主机间非必要的网络访问，特别是445/3389/22端口
* 消除密码复用：每台主机使用不同的本地管理员密码（LAPS方案）
* 启用Credential Guard：防止LSASS中的Hash被窃取
* 限制NTLM认证：优先使用Kerberos，禁用或限制NTLM
* 部署蜜罐：在内网部署蜜罐，横向移动时触发告警

## 九、红队钓鱼攻击的常见手法？如何防范？

**答：**

钓鱼是护网红队突破边界最常用的手段：

**常见手法**：

* **鱼叉邮件**

  ：针对特定人员发送伪装邮件（如"工资调整通知"、"紧急安全通告"），附带恶意Office文档（宏病毒/远程模板注入）或恶意链接
* **伪装网站**

  ：克隆OA/VPN/邮箱登录页面，窃取用户凭据
* **即时通讯钓鱼**

  ：通过企业微信/钉钉/飞书发送恶意链接或文件
* **U盘投递**

  ：在目标单位周边丢弃伪装U盘，利用自动运行或快捷方式漏洞
* **电话社工**

  ：冒充IT部门/安全部门，诱导用户执行特定操作

**防范措施**：

* 安全意识培训：定期进行钓鱼演练，提高员工警惕性
* 技术防护：邮件网关过滤恶意附件和链接，Office禁用宏，浏览器隔离
* 多因素认证(MFA)：即使密码泄露，攻击者也无法直接登录
* URL预扫描：对邮件中的链接进行沙箱分析，识别恶意页面
* 外发邮件限制：配置SPF/DKIM/DMARC，防止域名被伪造

## 十、护网实战中，蓝队核心工作流程是什么？

**答：**

这道题考的是你对护网全局的理解：

**1. 监控值守**：7x24小时盯设备（IDS/IPS/WAF/态势感知），及时发现异常告警。重点监控：Web攻击告警、异常外连、异常登录。

**2. 研判分析**：对告警进行研判，区分误报和真实攻击，确定攻击类型、攻击IP、攻击目标、是否成功。研判是蓝队最核心的能力。

**3. 处置封堵**：

* 封禁攻击IP（防火墙/安全组/WAF黑名单）
* 下线被控主机或隔离受影响网段
* 清除WebShell和恶意文件
* 重置被泄露的密码
* 修复被利用的漏洞

**4. 溯源反制**：定位攻击者身份（IP归属、攻击手法特征、使用的工具和基础设施），编写溯源报告。有条件的可进行反制（蜜罐诱捕、攻击者IP反制）。

**5. 报告总结**：每日编写防守日报（告警数量、攻击事件、处置措施），演练结束后编写总结报告（攻击复盘、薄弱环节、改进建议）。

以上10道题覆盖了内网渗透、域渗透、安全加固、横向移动检测等高级实战场景。护网面试的核心逻辑：初级看你能干什么（盯设备/看告警），中高级看你脑子里有没有体系（信息收集→权限提升→横向移动→权限维持的完整链条，以及对应的检测和防御方案）。

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rvkyDDyx4sv53bdQHLc9aiaciaqqxoojmXlic5HzYKRWCHnibkX1MXkqzL652lJpPoacJ8owSC6fuxHgnIgcWDVMIg/0?wx_fmt=png)

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