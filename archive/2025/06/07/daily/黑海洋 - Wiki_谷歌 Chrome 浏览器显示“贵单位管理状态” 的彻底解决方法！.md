---
title: 谷歌 Chrome 浏览器显示“贵单位管理状态” 的彻底解决方法！
url: https://blog.upx8.com/4816
source: 黑海洋 - Wiki
date: 2025-06-07
fetch_date: 2025-10-06T22:56:11.096414
---

# 谷歌 Chrome 浏览器显示“贵单位管理状态” 的彻底解决方法！

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 谷歌 Chrome 浏览器显示“贵单位管理状态” 的彻底解决方法！

发布时间:
2025-06-06

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
58290

![](https://cdn.skyimg.net/up/2025/6/6/97cf8699.webp)

如果你的谷歌 Chrome 浏览器显示 **“贵单位管理状态”** ，通常是因为设备或浏览器被企业、学校或组织通过策略（Group Policy 或 Chrome 企业策略）管理。

以下是彻底解决此问题的几种方法：

### **方法 1：检查并移除 Chrome 企业策略**

1. **在 Chrome 地址栏输入**：

   ```
   chrome://policy/
   ```

   * 查看是否有被强制应用的管理策略（如 `ManagedByYourOrganization` 或 `ExtensionInstallForcelist`）。
2. **删除 Chrome 策略注册表项（Windows）** ：

### **方法 2：使用批处理 移除 Chrome 企业策略**

将下面的代码保存为bat批处理，然后以管理员权限打开运行即可搞定！

```
@echo off

echo Closing Google Chrome...
taskkill /F /IM chrome.exe /T > nul
echo.

IF NOT EXIST "%WINDIR%\System32\GroupPolicy" goto next

echo Deleting GroupPolicy folder...
RD /S /Q "%WINDIR%\System32\GroupPolicy" || goto error
echo.

:next
IF NOT EXIST "%WINDIR%\System32\GroupPolicyUsers" goto next2

echo Deleting GroupPolicyUsers folder...
RD /S /Q "%WINDIR%\System32\GroupPolicyUsers" || goto error
echo.

:next2
IF NOT EXIST "%ProgramFiles(x86)%\Google\Policies" goto next3

echo Deleting GroupPolicyUsers folder...
RD /S /Q "%ProgramFiles(x86)%\Google\Policies" || goto error

:next3
IF NOT EXIST "%ProgramFiles%\Google\Policies" goto next4

echo Deleting GroupPolicyUsers folder...
RD /S /Q "%ProgramFiles%\Google\Policies" || goto error

:next4
gpupdate /force

echo Deleting policies from Windows registries...
reg delete HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome /f
reg delete HKEY_LOCAL_MACHINE\Software\Policies\Google\Update /f
reg delete HKEY_LOCAL_MACHINE\Software\Policies\Chromium /f
reg delete HKEY_LOCAL_MACHINE\Software\Google\Chrome /f
reg delete HKEY_LOCAL_MACHINE\Software\WOW6432Node\Google\Enrollment /f
reg delete HKEY_CURRENT_USER\Software\Policies\Google\Chrome /f
reg delete HKEY_CURRENT_USER\Software\Policies\Chromium /f
reg delete HKEY_CURRENT_USER\Software\Google\Chrome /f
reg delete "HKEY_LOCAL_MACHINE\Software\WOW6432Node\Google\Update\ClientState\{430FD4D0-B729-4F61-AA34-91526481799D}" /v "CloudManagementEnrollmentToken" /f

pause
exit

:error
echo.
echo An unexpected error has occurred. �Have opened the program as an administrator (right click, run as administrator)?
echo.
pause
exit
```

### **注意事项**

1. **企业设备**：如果是公司/学校电脑，擅自修改策略可能违反规定，建议联系 IT 部门。
2. **个人电脑**：若问题反复出现，可能是恶意软件篡改，需全盘杀毒。
3. **同步账户**：如果账号被企业托管，需退出并更换个人账号。

希望以上方法能帮你彻底解决问题！如果仍有疑问，评论区留言！

[取消回复](https://blog.upx8.com/4816#respond-post-4816)

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