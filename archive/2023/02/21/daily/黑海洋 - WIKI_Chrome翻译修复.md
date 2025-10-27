---
title: Chrome翻译修复
url: https://blog.upx8.com/3228
source: 黑海洋 - WIKI
date: 2023-02-21
fetch_date: 2025-10-04T07:37:46.599679
---

# Chrome翻译修复

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Chrome翻译修复

发布时间:
2023-02-20

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
11592

谷歌Chrome 109.0.5414.120最新稳定版是一款非常好用的浏览器，简洁，速度快，支持多标签浏览，而新版本的到来，更进一步提速操作，即当标签组被折叠以减少占用空间时，浏览器将自动冻结这些页面以释放系统CPU/内存资源。谷歌浏览器最大的亮点就是没有任何广告，为用户提供了最为干净的网页浏览体验。

### **安装说明**

1.软件支持32/64位的Win7/Win8/Win10/Win11系统或更高，安装包大小89.1M。

以下是bat代码：

> :: This is a batch script for fixing Google Translate and making it available
> :: in the Chinese mainland. If you experience any problem, visit the page below:
>
> @echo off
> setlocal enabledelayedexpansion
> chcp 437 >NUL
>
> set "ips[0]=74.125.137.90"
> set "ips[1]=74.125.193.186"
> set "ips[2]=74.125.196.113"
> set "ips[3]=108.177.97.100"
> set "ips[4]=108.177.111.90"
> set "ips[5]=108.177.122.90"
> set "ips[6]=108.177.125.186"
> set "ips[7]=108.177.126.90"
> set "ips[8]=108.177.127.90"
> set "ips[9]=142.250.0.90"
> set "ips[10]=142.250.1.90"
> set "ips[11]=142.250.4.90"
> set "ips[12]=142.250.8.90"
> set "ips[13]=142.250.9.90"
> set "ips[14]=142.250.10.90"
> set "ips[15]=142.250.11.90"
> set "ips[16]=142.250.12.90"
> set "ips[17]=142.250.13.90"
> set "ips[18]=142.250.27.90"
> set "ips[19]=142.250.28.90"
> set "ips[20]=142.250.30.90"
> set "ips[21]=142.250.31.90"
> set "ips[22]=142.250.96.90"
> set "ips[23]=142.250.97.90"
> set "ips[24]=142.250.98.90"
> set "ips[25]=142.250.99.90"
> set "ips[26]=142.250.100.90"
> set "ips[27]=142.250.101.90"
> set "ips[28]=142.250.102.90"
> set "ips[29]=142.250.103.90"
> set "ips[30]=142.250.105.90"
> set "ips[31]=142.250.107.90"
> set "ips[32]=142.250.111.90"
> set "ips[33]=142.250.112.90"
> set "ips[34]=142.250.113.90"
> set "ips[35]=142.250.114.90"
> set "ips[36]=142.250.115.90"
> set "ips[37]=142.250.123.90"
> set "ips[38]=142.250.125.90"
> set "ips[39]=142.250.126.90"
> set "ips[40]=142.250.128.90"
> set "ips[41]=142.250.138.90"
> set "ips[42]=142.250.141.90"
> set "ips[43]=142.250.142.90"
> set "ips[44]=142.250.145.90"
> set "ips[45]=142.250.152.90"
> set "ips[46]=142.250.153.90"
> set "ips[47]=142.250.157.90"
> set "ips[48]=142.250.157.183"
> set "ips[49]=142.250.157.184"
> set "ips[50]=142.250.157.186"
> set "ips[51]=142.250.158.90"
> set "ips[52]=142.250.159.90"
> set "ips[53]=142.251.1.90"
> set "ips[54]=142.251.2.90"
> set "ips[55]=142.251.4.90"
> set "ips[56]=142.251.5.90"
> set "ips[57]=142.251.6.90"
> set "ips[58]=142.251.8.90"
> set "ips[59]=142.251.9.90"
> set "ips[60]=142.251.10.90"
> set "ips[61]=142.251.12.90"
> set "ips[62]=142.251.15.90"
> set "ips[63]=142.251.16.90"
> set "ips[64]=142.251.18.90"
> set "ips[65]=142.251.107.90"
> set "ips[66]=142.251.111.90"
> set "ips[67]=142.251.112.90"
> set "ips[68]=142.251.116.90"
> set "ips[69]=142.251.117.90"
> set "ips[70]=142.251.120.90"
> set "ips[71]=142.251.160.90"
> set "ips[72]=142.251.161.90"
> set "ips[73]=142.251.162.90"
> set "ips[74]=142.251.163.90"
> set "ips[75]=142.251.166.90"
> set "ips[76]=172.217.192.90"
> set "ips[77]=172.217.195.90"
> set "ips[78]=172.217.203.90"
> set "ips[79]=172.217.204.90"
> set "ips[80]=172.217.214.90"
> set "ips[81]=172.217.215.90"
> set "ips[82]=172.253.58.90"
> set "ips[83]=172.253.62.90"
> set "ips[84]=172.253.63.90"
> set "ips[85]=172.253.112.90"
> set "ips[86]=172.253.113.90"
> set "ips[87]=172.253.114.90"
> set "ips[88]=172.253.115.90"
> set "ips[89]=172.253.116.90"
> set "ips[90]=172.253.117.90"
> set "ips[91]=172.253.118.90"
> set "ips[92]=172.253.119.90"
> set "ips[93]=172.253.123.90"
> set "ips[94]=172.253.124.90"
> set "ips[95]=172.253.125.90"
> set "ips[96]=172.253.126.90"
> set "ips[97]=172.253.127.90"
> set "ips[98]=216.58.227.65"
> set "ips[99]=216.58.227.66"
> set "ips[100]=216.58.227.67"
>
> set /a "index=%RANDOM% %%100"
> set "random\_ip=!ips[%index%]!"
>
> set "divider=----------------------------------------------"
> set "target\_domain=translate.googleapis.com"
> set "hosts\_file=C:\Windows\System32\drivers\etc\hosts"
>
> goto :start
>
> :generate\_new\_rule
>  echo Modify hosts file to fix Google translate service.
>  echo %divider%
>  echo [1] Automatically [2] Manually
>  echo %divider%
>  set /p action="Enter a number to choose an IP adding method:"
>
> if "%action%"=="2" (
>  set /p ip="Please enter a valid IP address: "
>  )
>
> if "%ip%"=="" (
>  set "ip=!random\_ip!"
>  )
>
> set "new\_rule=%ip% %target\_domain%"
> goto:EOF
>
> :start
>
> set "old\_rule=null"
> set "comment=# Fix Google Translate CN"
>
> for /f "tokens=\*" %%i in ('type %hosts\_file%') do (
>  set "line=%%i"
>  :: Retrieve the rule If the target domain exists.
>  if not "!line:%target\_domain%=!"=="%%i" set "old\_rule=%%i"
> )
>
> if not "%old\_rule%"=="null" (
>  echo A rule has been added to the hosts file.
>  echo %divider%
>  echo [1] Update [2] Delete
>  echo %divider%
>  set /p action="Enter a number to choose an action: "
>  if "!action!"=="1" (
>  call :generate\_new\_rule
>  if not "%old\_rule%"=="!new\_rule!" (
>  echo Deleting the rule "%old\_rule%"
>  echo Adding the rule "!new\_rule!"
>  set "new\_line=false"
>  for /f "tokens=\*" %%i in ('type %hosts\_file% ^| find /v /n "" ^& break ^> %hosts\_file%') do (
>  set "rule=%%i"
>  set "rule=!rule:\*]=!"
>  if "%old\_rule%"=="!rule!" set "rule=!new\_rule!"
>  if "!new\_line!"=="true" >>%hosts\_file% echo.
>  >>%hosts\_file% <NUL set /p="!rule!"
>  set "new\_line=true"
>  )
>  ) else (
>  echo The rule already exists, nothing to do.
>  )
>  ) else (
>  if "!action!"=="2" (
>  echo Deleting the rule "%old\_rule%"
>  set "new\_line=false"
>  for /f "tokens=\*" %%i in ('
>  type "%hosts\_file%" ^| findstr /v /c:"%comment%" ^| findstr /v "%target\_domain%" ^| find /v /n "" ^& break ^> "%hosts\_file%"
>  ') do (
>  set "line=%%i"
>  set "line=!line:\*]=!"
>  if "!new\_line!"=="true" >>%hosts\_file% echo.
>  >>%hosts\_file% <NUL set /p="!line!"
>  set "new\_line=true"
>  )
>  )
>  )
> ) else (
>  call :generate\_new\_rule
>  echo Adding the rule "!new\_rule!"
>  echo.>>%hosts\_file%
>  echo %comment%>>%hosts\_file%
>  <NUL set /p="!new\_rule!">>%hosts\_file%
> )
>
> echo Done.
> pause

# 下载地址（含浏览器）：https://www.123pan.com/s/Lv0DVv-OWq1H

[取消回复](https://blog.upx8.com/3228#respond-post-3228)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")