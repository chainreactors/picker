---
title: 针对新型SWIFT勒索病毒的详细分析报告
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247489118&idx=1&sn=eb14f5ed58d5793629466f95ef82e2bc&chksm=902fb976a7583060ea24a1f47ae8535a6af799e5d3ed74007aa9a3b1f3432133bcf95be2dd0a&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2024-10-17
fetch_date: 2025-10-06T18:52:04.468875
---

# 针对新型SWIFT勒索病毒的详细分析报告

![cover_image](http://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmXuAicCmLaZLmokBLJHRlUgsanMez7YuKnMhGicfzqf6ibDcRicfpQAyf0Al2icicwYBp90ZSPMicibYhrYcw/0?wx_fmt=jpeg)

# 针对新型SWIFT勒索病毒的详细分析报告

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

原文首发出处：

https://xz.aliyun.com/t/13777

先知社区 作者：熊猫正正

这几年勒索病毒已经在全球范围内大规模爆发，全球基本上每天都有企业被勒索病毒攻击，勒索攻击已经成为了全球网络安全最大的威胁，未来随着数字经济的发展，勒索攻击在未来几年，甚至很长的一段时间内仍然是全球最大的网络安全威胁，而且勒索攻击已经形成了一套非常完整的生态化体系运作流程，要想彻底解决勒索病毒需要涉及到很多层面，这也是为啥勒索攻击一直无法有效解决的原因。

最近几个国家联手打击LockBit勒索病毒黑客组织，可能LockBit勒索病毒黑客组织会像此前的GandCrab和Sodinokibi勒索病毒黑客组织一样消失，但是勒索攻击仍然会一直发生，正所谓野火烧不尽，春风吹又生，只要勒索攻击能给黑客组织带来巨大的经济利益，就会一直有新的勒索病毒黑客组织出现，需要持续关注。

笔者近期注意到一款新型的勒索病毒SWIFT，并对这款新型的勒索病毒进行了详细分析。

详细分析

1.样本的编译时间为2024年2月15日，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXuAicCmLaZLmokBLJHRlUgs4NpKhWVCPMqQ5lSopJiamiawqW2MuZiaS9BF7ZquiamwqNCvnMITmMvO0Q/640?wx_fmt=png)

2.获取操作系统语言，如果操作系统语言ID为0x429，则直接退出，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXuAicCmLaZLmokBLJHRlUgswRepHwFotCXe9uicjWvbLfyQDJZgqrc4VMZkwGlHZ20kLwicOKZ48icxQ/640?wx_fmt=png)

3.判断当前进程是否以管理员或ROOT权限运行，如果以管理员权限运行，则创建互斥变量，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXuAicCmLaZLmokBLJHRlUgsqvzgQgyx4OY5Ax2us2RUg1Xx0iaMvnugD00OHpk10eSwPGmExSASabw/640?wx_fmt=png)

4.获取勒索病毒加密密钥相关信息，并设置注册表项，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXuAicCmLaZLmokBLJHRlUgsUWy2Max815LhmyGZJiasBia4GXbCAoBpickn41nvU5a0ts32AeZVdhlhA/640?wx_fmt=png)

5.设置注册表项HKEY\_CURRENT\_USER\Software\Proton\public，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXuAicCmLaZLmokBLJHRlUgs4NiavS4japCCcPTw7USqmKQTPYqS9vj7oyNpvAITiaicClfRsa8UWicSOQ/640?wx_fmt=png)

6.设置注册表项HKEY\_CURRENT\_USER\Software\Proton\full，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXuAicCmLaZLmokBLJHRlUgs3mca7pJzDjQCdjvab9KMI0Zx7eGP8dxWsEIVjoAgykCP25arHZlnLA/640?wx_fmt=png)

7.获取加密后的文件后缀名、勒索邮箱(备用邮箱)地址、受害者ID等相关信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXuAicCmLaZLmokBLJHRlUgsfUgo1nuEpoOx3qFmg9a714MtVbO1K5U50Qnb249OXag72ibPT5XyUdA/640?wx_fmt=png)

8.加密后的文件后缀名、勒索邮箱(备用邮箱)、受害者ID等信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXuAicCmLaZLmokBLJHRlUgsjsv9IoyMssb8VTMeuqVIib44icgjjql1cibUaG5L3KSkvsPZn2NicZTpxA/640?wx_fmt=png)

9.清理回收站的内容，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXuAicCmLaZLmokBLJHRlUgs1YVN5TQs2ThVeGpQL9fuWib8NcD7ZJwH5TUAFfDaW8FbwAsjD6IxvYQ/640?wx_fmt=png)

10.通过CMD命令执行删除磁盘卷影幅本和禁用系统修复操作，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXuAicCmLaZLmokBLJHRlUgsE7uBevW8kibPz1bMTlw0Zx1knyKZ7JNCMibgmghSNCDx69iaLBBMr2yMg/640?wx_fmt=png)

相关命令，如下：

vssadmin Delete Shadows /All /Quiet

bcdedit /set {default} recoveryenabled No

bcdedit /set {default} bootstatuspolicy ignoreallfailures

wmic SHADOWCOPY /nointeractive

11.将程序拷贝一份到系统开始自启动目录下，命名为此前生成的[ID].exe，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXuAicCmLaZLmokBLJHRlUgsJWNUDUMrAUaxibyDjAsmicLXsYWF0S27GW0icmMhMk7ulxeFjTCuicEB0g/640?wx_fmt=png)

12.解密获取进程列表信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXuAicCmLaZLmokBLJHRlUgsqsdZEW59nribMibsSicCia17IPEa922iarwjvTlvjGPiciaxl9Nv4hUib4XAbw/640?wx_fmt=png)

进程列表：

wxServer,wxServerView,sqlmangr,RAgui,supervise,Culture,Defwatch,winword,QBW32,QBDBMgr,qbupdate,axlbridge,httpd,fdlauncher,MsDtSrvr,java,360se,360doctor,wdswfsafe,fdhost,GDscan,ZhuDongFangYu,QBDBMgrN,mysqld,AutodeskDesktopApp,acwebbrowser,CreativeCloud,AdobeDesktopService,CoreSync,AdobeCEF,Helper,node,AdobeIPCBroker,sync-taskbar,sync-worker,InputPersonalization,AdobeCollabSync,BrCtrlCntr,BrCcUxSys,SimplyConnectionManager,Simply.SystemTrayIcon,fbguard,fbserver,ONENOTEM,wsa\_service,koaly-exp-engine-service,TeamViewer\_Service,TeamViewer,tv\_w32,tv\_x64,TitanV,Ssms,notepad,RdrCEF,sam,oracle,ocssd,dbsnmp,synctime,agntsvc,isqlplussvc,xfssvccon,mydesktopservice,ocautoupds,encsvc,tbirdconfig,mydesktopqos,ocomm,dbeng50,sqbcoreservice,excel,infopath,msaccess,mspub,onenote,outlook,powerpnt,steam,thebat,thunderbird,visio,wordpad,bedbh,vxmon,benetns,bengien,pvlsvr,beserver,raw\_agent\_svc,vsnapvss,CagService,DellSystemDetect,EnterpriseClient,ProcessHacker,Procexp64,Procexp,GlassWire,GWCtlSrv,WireShark,dumpcap,j0gnjko1,Autoruns,Autoruns64,Autoruns64a,Autorunsc,Autorunsc64,Autorunsc64a,Sysmon,Sysmon64,procexp64a,procmon,procmon64,procmon64a,ADExplorer,ADExplorer64,ADExplorer64a,tcpview,tcpview64,tcpview64a,avz,tdsskiller,RaccineElevatedCfg,RaccineSettings,Raccine\_x86,Raccine,Sqlservr,RTVscan,sqlbrowser,tomcat6,QBIDPService,notepad++,SystemExplorer,SystemExplorerService,SystemExplorerService64,Totalcmd,Totalcmd64,VeeamDeploymentSvc

13.遍历上面的进程列表，并结束该进程，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXuAicCmLaZLmokBLJHRlUgskOy32TIPgfOkLuoUKOEVbmoibuF44775ibzyeuDYibxL8XzqdxzrRGCVg/640?wx_fmt=png)

14.解密获取服务列表信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXuAicCmLaZLmokBLJHRlUgsxqrfO7vtKED83hjXibIlDxvohvIVsK1Xt2iaLLO13PC06Yh3AZicjfxicw/640?wx_fmt=png)

服务列表：

wrapper,DefWatch,ccEvtMgr,ccSetMgr,SavRoam,Sqlservr,sqlagent,sqladhlp,Culserver,RTVscan,sqlbrowser,SQLADHLP,QBIDPService,Intuit.QuickBooks.FCS,QBCFMonitorService,msmdsrv,tomcat6,zhudongfangyu,vmware-usbarbitator64,vmware-converter,dbsrv12,dbeng8,MSSQL$MICROSOFT##WID,MSSQL$VEEAMSQL2012,SQLAgent$VEEAMSQL2012,SQLBrowser,SQLWriter,FishbowlMySQL,MSSQL$MICROSOFT##WID,MySQL57,MSSQL$KAV\_CS\_ADMIN\_KIT,MSSQLServerADHelper100,SQLAgent$KAV\_CS\_ADMIN\_KIT,msftesql-Exchange,MSSQL$MICROSOFT##SSEE,MSSQL$SBSMONITORING,MSSQL$SHAREPOINT,MSSQLFDLauncher$SBSMONITORING,MSSQLFDLauncher$SHAREPOINT,SQLAgent$SBSMONITORING,SQLAgent$SHAREPOINT,QBFCService,QBVSS,YooBackup,YooIT,vss,sql,svc$,MSSQL,MSSQL$,memtas,mepocs,sophos,veeam,backup,bedbg,PDVFSService,BackupExecVSSProvider,BackupExecAgentAccelerator,BackupExecAgentBrowser,BackupExecDiveciMediaService,BackupExecJobEngine,BackupExecManagementService,BackupExecRPCService,MVArmor,MVarmor64,stc\_raw\_agent,VSNAPVSS,VeeamTransportSvc,VeeamDeploymentService,VeeamNFSSvc,AcronisAgent,ARSM,AcrSch2Svc,CASAD2DWebSvc,CAARCUpdateSvc,WSBExchange,MSExchange,MSExchange

15.遍历上面的服务列表，并停止服务，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXuAicCmLaZLmokBLJHRlUgshQvic3xia7oxHVfkd7lXK48e7liaTAtl0qOK8qcn8yjeKNB1mgJgmf9ng/640?wx_fmt=png)

16.遍历系统磁盘目录和网络共享目录，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXuAicCmLaZLmokBLJHRlUgsxG6V17zeia4TcWSas8qo5kZXQJ7c7VjHaRwbRmkQzopJUo9J9Qib16tg/640?wx_fmt=png)

17.创建线程遍历磁盘目录下的文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXuAicCmLaZLmokBLJHRlUgsC8mmWdQiaaUoh0wx2vaibicfF2n591QGOSkdVQP4t0SO3ictSUPalV58fg/640?wx_fmt=png)

18.生成勒索提示信息文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXuAicCmLaZLmokBLJHRlUgskLLseokhPnKceOEQChtuxXAoG6xeaDyI8rMDwSDrPKBraJw7pEGp1w/640?wx_fmt=png)

勒索提示信息文件名为#SWIFT-Help.txt，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXuAicCmLaZLmokBLJHRlUgsicHKBRpm435rwPdjThDZGepYibPKwXpR58xp6SbeKOSE0dkRKvkwKmbw/640?wx_fmt=png)

勒索提示信息文件内容，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXuAicCmLaZLmokBLJHRlUgsrA909O8aO8v2iaIQX5VibEhf80ib2jp6uiaV0yTS3XOXLI1dhiajPYOudSg/640?wx_fmt=png)

19.将遍历到的系统文件读取到内存中，然后进行加密操作，当文件大小小于0x96000时，直接加密整个文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXuAicCmLaZLmokBLJHRlUgsBibZACX65FrEnXkmQpFxIVpVZ35mhk4lFGNgo7LRfDoCmvCETJtRLiag/640?wx_fmt=png)

20.当文件大小大于0x96000时，采用分块加密的方式，按0x2000大小分块进行加密操作，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXuAicCmLaZLmokBLJHRlUgslpJyz5dmIw6BciaicKYJvpREHUda8wV1128HFfCKIAibnnUDKsibn3w7DA/640?wx_fmt=png)

21.加密算法使用AES+ECC算法，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXuAicCmLaZLmokBLJHRlUgs7mwVYa36p9ibykbRgmZ0Hq7MBNhXH8ichcc4cXwqQ3A4T8D5NszVWsCA/640?wx_fmt=png)

22.加密完成之后，通过MoveFileW函数对原文件进行重命名操作，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXuAicCmLaZLmokBLJHRlUgs5qmKytTMGzrzBlF0rOG9eBK2GiaqAeAh43UrwG6lA2No1EVbcZHNILQ/640?wx_fmt=png)

23.加密后的文件后缀名为[swift\_1@tutamail.com].SWIFT，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXuAicCmLaZLmokBLJHRlUgs9pqhNlmoBZINevu5G1DQkT9SDgkjia61zrWx79ic6yicsic4ZT1FDcxYTQ/640?wx_fmt=png)

24.获取桌面勒索提示信息，然后替换桌面背景图片，如下所示：

![](https://mmbiz.qpi...