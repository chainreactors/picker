---
title: 2026FIC决赛（windows服务器部分）
url: https://mp.weixin.qq.com/s/fq9BAds1wu_gCiZfj2V0DA
source: Doonsec's feed
date: 2026-07-06
fetch_date: 2026-07-07T06:01:52.600402
---

# 2026FIC决赛（windows服务器部分）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/T5C6icTcSx9MlgjnDVO7blaHsoSzlPTL4ibZjibibUvgIqbyzkc4CBqZWf5QvqnNKHaTiaicTbbYUaxreVibAKeUDHQT5EuDu2LqZIRIWiaKaxYgUx8/0?wx_fmt=jpeg)

# 2026FIC决赛（windows服务器部分）

原创

Serendipity
Serendipity

Serendipity的小屋

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

容器密码：`\/a15f5b1d-a9fbdb79-de9ee6bf-28b9fce1\/`

## windows服务器

> 第一次遇到windows服务器，借鉴大佬的wp以及官方结题思路
> https://blog.enxiaohao.cn/posts/Forensics/2026FICFinalWinserverwp/

火眼看到网络配置，系统配有两张网卡 172.28.0.100，172.27.0.100，分别对应两个公网地址 40.72.166.187，139.217.21.231

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9NvQjt8ChtVjlIn7ODgyAnmibD9MLDaQ5fiaZDaickzXEYjEPAlKibcBalD72icbouL7UJQ3V2ag2OZWIwh5cWdDFhsdUrYabb53CYo/640?wx_fmt=png&from=appmsg "null")

根据这个网卡配置网络

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9MUiayCE970dGicYA1VwxEichRonF1hMf42DiciacMgZf9ZVDnHPy6gUHOjsltbRpoheK5mXg1d1ibNxUEicg0XiaeVNHOx5WF9IsaE6Pw/640?wx_fmt=png&from=appmsg "null")

这里可以将dhcp起始地址改为0，方便后续操作

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9OwP01g0zkjViaQTsIia0gbUNsePAAZJugyG71GuzJgkSQaic4kbUyx4SOSJEjpTjcXDcAbOcdKu1icEGr2CIdeTvWPKYkuXOpYJico/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9N27kz7ky6EuiaGmIzdeCa7LibbibOX3zLkZ9uhcGGwHSZmzxoFTAzoUDmc4NiaZocZu4GhicAl4QLsUKaJsLicrcXrLYibsfVMFHaIicE/640?wx_fmt=png&from=appmsg "null")

仿真之后按照指示输入密码`F1cWinC@re`

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9PKFhXdmsFzsMWic1onClNnOstR2ZNGiaMibaczO9BDehK1tAX6mdF6mDvupvbeNybIObVv2Ceev8aIANAo8PXzymVzntQLCoaoy8/640?wx_fmt=png&from=appmsg "null")

进入一个windows的cmd页面，这里之后其实就可以rdp连接了

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9N4ib8fjibxPCnOookSv1h7TdSn7muWNLKhSOZnErLVrmjauubEzltzOXAFBSJrbhnG56UTQyav0PwlSebM3xWdafhHeyyII4Rfo/640?wx_fmt=png&from=appmsg "null")

成功连接，便于后续指令的输入

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9PibQfo8JKOSd6oBrhqtw7BicyF9RPOFn1j2WibbYFibicycDyVT5xicmj06KNJZbWAdcYraOLicjCfDjZyHpBpX2ng94VlOcWnYic9zUg/640?wx_fmt=png&from=appmsg "null")

接下来看服务，服务列表中可以发现自动启动的FicWeb和PostgreSQL，以及手动的containerd和Docker![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9NxmDO8fxibsgyyMd6yQ8zFx8wn4jzt3K6xHwzbbVwR5ExhEvToB9KqQYubICPia4eZTfnCw9F35bZjzc9JhI0Rx7nXB9zqS1d4E/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9Ol0f6LibWQxNAefWG7KVpY2I6F4GTIgq0g33aS1uat8vhyRXy23mzXnHRePgltbtRrZwokDKibA0S7JJCwSCx3ibw4icgvhkQxy1Q/640?wx_fmt=png&from=appmsg "null")

计划任务中有MountVHDXatStartup，会把ROOT.vhdx挂载到T，并在T下创建root和state连个目录，同时启动containerd

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9MkCpmG5PYCV6anNbPPCB0khHuRuKmrNd4aVFducBibPcicnAIZCebwicvO4KLNartcibymsBw6TT5TUEggbbBh1SibB3fnn6IzvCL4/640?wx_fmt=png&from=appmsg "null")

可以查看一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9OXpYM5kssJDlbxuVR8MB4IQ0A7OQ3iaGddHaia3EnTIIGbrbwh9aloxjibicI5OH401dMicxibYVpB0gImJI1Fp67VGZHf0hKtdAnkI/640?wx_fmt=png&from=appmsg "null")

`nerdctl ps -a`可以看到当前启动的容器，postgres已启动

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9Mn8IbJicrOHSNq5E2Yaru2e2micNiamj6JIMbuayxPTg5k4UxSBksRicouVqf1HibpYt084bgc842Mz71o4kQRLHtzxRYBPlJWPR3c/640?wx_fmt=png&from=appmsg "null")

然后启动网站，直接运行exe启动会报错，用sc.exe可以启动

`sc.exe start FicWeb`

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9N0OzGOQlFDibwW7hgK9IKic9AxZic20XnlXfWw4ySlkiawLQiaRSWgewq42KVwfrCxicRVm5hWoib1knSibU78rDUbp2NvrEXR3icXaG3Y/640?wx_fmt=png&from=appmsg "null")

`sc.exe query FicWeb`

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9MNL8Bia9mcDxwh8iaxrbHThP33DgEl1T3LfCBWL8pkuUeUHNTN3g5Z7ILVeq94vsxbmLXCunwX9JQNsHq21kibxzzHCBYhjAV9tw/640?wx_fmt=png&from=appmsg "null")

然后直接用ip访问不到，要改hosts并配置本地dns才能启动
先改hosts（根据自己的ip）

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9Mk2ichBUmnvz2RBV1BDHYhNFZwpohStQ5K7Gf6UKtlBmy7QH5lzsEss7LrT0r0bWYSed7dFrjSYF7TV2woDkdJSOz2OouG9AhU/640?wx_fmt=png&from=appmsg "null")

```
172.28.0.100 admin.ficads.site172.28.0.100 mtls.ficads.site172.27.0.100 ficads.site
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9OUXBlZHjuLnhia5YFBciaN5UYiaG2bbOjFXx781a4x5Pv9ibma1AwQT6wPMfAPbHt3HLcicys2fegefDMDbFudaXfrJmgiby3QuBn4I/640?wx_fmt=png&from=appmsg "null")

然后会发现后台还是连不上，看到题目提供的附件4，是因为这里走的是http3，对应的传输层是QUIC，基于UDP

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9M6vffNZNuxYPibyshkNKc0DBjg32D7ibB9qHxGkOCrIQbC0loJRYjqulJ4Lok5SYQN9jGExWt9SChCNUXfcibmfsjLaRCeROfj0Q/640?wx_fmt=png&from=appmsg "null")

所以用这个方式启动，强制这个域名走QUIC：

```
$chrome = 'C:\Program Files\Google\Chrome\Application\chrome.exe'$profile = "$env:TEMP\fic-admin-http3-profile"
Start-Process -FilePath $chrome -ArgumentList @(  '--user-data-dir=' + $profile,  '--origin-to-force-quic-on=admin.ficads.site:443',  '--host-resolver-rules="MAP admin.ficads.site 172.28.0.100, MAP mtls.ficads.site 172.28.0.100"',  'https://admin.ficads.site/')
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9O9F4Xc1Ifha4q0HVj90UVrL3iaCezUeLplqlwnMWkSMGzzqkGImpIZotiaPElkQPlFicxZkiazS4NOUxib6iao4CnqvBuWbJ2krCMaM/640?wx_fmt=png&from=appmsg "null")

### 1 分析服务器检材，系统分区的文件系统类型是？

### 【参考格式：FAT32】

### **REFS**

可以输入命令`fsutil fsinfo volumeInfo C:`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9Oic1KIcYHO1Iic5nP6MJbibVJic09BfGGzunz5JGTxWnjoH3Qh6Ye2A9OkQmicDaeTc4IzwwRDO96OuxaTlxXzXiaBicEYIvCVZKh7vI/640?wx_fmt=png&from=appmsg "null")

也可以直接看分析的结果

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9OWEM501R9w7iaUD0oNNic72sjW7BuqShicskt6sVWWv0ibIr6B4xN7S35GIZqfR8d8OiaPMIQTJT6BtTefiayEZ3nZmqRRYJDIayTrA/640?wx_fmt=png&from=appmsg "null")

### 2 分析服务器检材，系统分区的文件系统版本是多少？

### (格式:1.23)

**3.14**

使用 fsutil 查看 ReFS 版本信息`fsutil fsinfo refsInfo C:`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9OmyGGO9S0JgXBlQPrjBAt0y6tb5FAKSpHMwxeibVH2vP3xfyhOrPErNtk44FwXKiaaRTABxLpbyXA7YcYvrRXYXnhc1QDF2EMK8/640?wx_fmt=png&from=appmsg "null")

### 3 分析服务器检材，系统的SKU编号（OperatingSystemSKU）是什么？

**407**

可以通过`(Get-CimInstance Win32_OperatingSystem).OperatingSystemSKU`获取或者通过`[int](Get-ComputerInfo).OsOperatingSystemSKU`获取

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9OA93SObXWcXic0yhzqTOGmcmavqOHgjia2CktjUsmdM8icWFKboialjSWUXM1HVRIfjt9nhbl7iaDpSd6RRdvel0A7olClcIWcCtib0/640?wx_fmt=png&from=appmsg "null")

### 4 服务器中的WinRM HTTP服务的端口是多少？

### (格式:65535)

**59508**

使用命令查询WinRM的服务配置`winrm enumerate winrm/config/listener`

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9P0TJWr88REh9mt71EoZ3mIfuJxJtx5nkxsCrIAPa44PGQZhY469zVpV5wPKUysCMZ0A2ELeg3Up5ElpiaKQ1CMgCpreRtUxY5M/640?wx_fmt=png&from=appmsg "null")

> 不能单纯看winrmgetconfig，这个只会打印默认的端口，这里需要查看实际的监听器端口

### 5 最后一次通过WinRM远程访问的北京时间是

### (格式:1970-01-01 00:11:22)

**2026-05-17 16:38:06**

用powershell命令分析事件日志Microsoft/Windows/WinRM

`Get-WinEvent -LogName 'Microsoft-Windows-WinRM/Operational'`

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9PWPzvxhHT3t7yxKt6jxjawfBiabQWBB3YoKXYvichmQD4Wk5XbUFMHGlK4jJ246pF2XjleibjFAeEibLm8ib5knKiaa4pvaX5ohhHlg/640?wx_fmt=png&from=appmsg "null")

### 6 服务器除了允许上一题登录记录的IP地址远程登录，还允许哪个IP地址远程管理

### (格式:1.2.3.4)

**117.184.20.123**

上一题可以看到一个ip

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9MoFUiaTicDuzgqJicahHzBs0GbOP25F0VmyWa3aPx8kHPXNVcaLeAahWqadK0XB4leMnZKHdScbt7xSiar9icA76wg8Y8ktHbGSHrY/640?wx_fmt=png&from=appmsg "null")

根据已经查询到的端口 59508 获取对应端口的防火墙规则

```
Get-NetFirewallPortFilter |Where-Object LocalPort -eq 59508 |Get-NetFirewallRule |ForEach-Object {    $_ | Get-NetFirewallAddressFilter | Select-Object LocalAddress, RemoteAddress}
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9N8oMoVewaN8CYbK4gvOr2xUL3FKAUDhLxspAPjFNeyh0PlPWYDvMMoJync2H7no3p6KYmy5icB92LiclCNA4yHXW1biawoAkQFcg/640?wx_fmt=png&from=appmsg "null")

排除上一题的ip可知117.184.20.123

### 7 主机secrets目录中存放有一批密码文档，找到存在历史快照版本的文件，该文件历史版本中存放的密码是什么

### (格式:Abc123!@#)

**pMLCzXOd+<.&.pUw**

> 这两题考点是ReFS文件系统文件流的快照，有关ReFS文件系统的流，要用refsutilstreamsnapshot工具来查看。这个结构和NTFSADS流蛮像的，只不过Refs的流一般更偏向于文件快照，ADS流更偏向附加数据

先查看流

```
Get-ChildItem . -File -Recurse | ForEach-Object {    $f = $_    Get-Item -LiteralPath $f.FullName -Stream * |    Where-Object Stream -like '*:$SNAPSHOT' |    Select-Object @{n='File';e={$f.FullName}}, Stream, Length}
```

可以看到有一个快照

![](https://mmbiz.qpic.cn/mmbiz_...