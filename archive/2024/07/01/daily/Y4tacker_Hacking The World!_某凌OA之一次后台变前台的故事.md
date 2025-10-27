---
title: 某凌OA之一次后台变前台的故事
url: https://y4tacker.github.io/2024/06/30/year/2024/6/%E6%9F%90%E5%87%8COA%E4%B9%8B%E4%B8%80%E6%AC%A1%E5%90%8E%E5%8F%B0%E5%8F%98%E5%89%8D%E5%8F%B0%E7%9A%84%E6%95%85%E4%BA%8B/
source: Y4tacker:Hacking The World!
date: 2024-07-01
fetch_date: 2025-10-06T17:38:31.294550
---

# 某凌OA之一次后台变前台的故事

* [Home](/)
* [Writing](/archives/)
* [Topics](/tags/)
* [Search](/search/)
* [About](/about/)
* [Friends](/link/)

Previous post Next post Back to top Share post

1. [1. 前言](#%E5%89%8D%E8%A8%80)
2. [2. 为什么突然变成了前台](#%E4%B8%BA%E4%BB%80%E4%B9%88%E7%AA%81%E7%84%B6%E5%8F%98%E6%88%90%E4%BA%86%E5%89%8D%E5%8F%B0)
3. [3. getThemeInfo调用被拦截怎么破](#getThemeInfo%E8%B0%83%E7%94%A8%E8%A2%AB%E6%8B%A6%E6%88%AA%E6%80%8E%E4%B9%88%E7%A0%B4)

# 某凌OA之一次后台变前台的故事

Y4tacker

2024-06-30 (Updated: 2025-09-02)

[Java](/categories/Java/)

[Java](/tags/Java/), [OA](/tags/OA/)

## 前言

​ 在某凌的后台功能中，无论是`sysUiExtend`还是`sysUiComponent`，都可以使用`getThemeInfo`完成WebShell的上传。至于这个点如何利用就不再细说了，网上已经有很多带POC的漏洞复现帖了，同时针对权限绕过，对于前者是配合了`/api`端点完成了权限检查的Bypass(这个看看配置即可)，对于后者，则是由新版本引入的功能。据不准确猜测大概是V16之后有的，至于为什么直接访问可以不经过鉴权在后文也会简单讲到，另外在文末也会介绍一种新的利用姿势，避免在对抗流量设备时因为严格限制拦截`getThemeInfo`的调用导致束手无策。

## 为什么突然变成了前台

​ 这个其实非常好理解，简单提一下即可，我们直接看desgin.xml中对于权限的配置部分，漏洞路由为`/sys/ui/sys_ui_component/sysUiComponent.do`，可以看到在下面的配置当中并没有对端点`/sys_ui_component`做权限的配置，猜测应该是来源开发的疏忽，同时由于这个类是新引入的，所以如果在老一点的系统，是没有这个类的，这点在看代码的时候需要注意下

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 ``` | ``` <?xml version="1.0" encoding="UTF-8"?> <configs 	xmlns="http://www.example.org/design-config" 	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 	xsi:schemaLocation="http://www.example.org/design-config ../../design.xsd "> 	<module 		messageKey="sys-ui:module.sys.ui" 		urlPrefix="/sys/ui/" 		defaultValidator="true"> 		<request 			path="index.jsp*" 			defaultValidator="roleValidator(role=SYSROLE_ADMIN;SYSROLE_SYSADMIN)" /> 		<request 			path="tools.jsp*" 			defaultValidator="roleValidator(role=SYSROLE_ADMIN;SYSROLE_SYSADMIN)" /> 		<request 			path="tree.jsp*" 			defaultValidator="roleValidator(role=SYSROLE_USER)" /> 		<request 			path="help/font/**" 			defaultValidator="roleValidator(role=SYSROLE_USER)" />	 		<request 			path="help/component/**" 			defaultValidator="roleValidator(role=SYSROLE_ADMIN;ROLE_SYSPORTAL_BASE_SETTING)" /> 		<request 			path="help/**" 			defaultValidator="roleValidator(role=SYSROLE_ADMIN;ROLE_SYSPORTAL_EXT_SETTING)" /> 		<request 			path="demo/**" 			defaultValidator="roleValidator(role=SYSROLE_USER)" /> 		<request 			path="jsp/**" 			defaultValidator="roleValidator(role=SYSROLE_USER)" /> 		<request 			path="sys_ui_logo/**" 			defaultValidator="roleValidator(role=SYSROLE_ADMIN;SYSROLE_SYSADMIN)" /> 		<request 			path="sys_ui_extend/**" 			defaultValidator="roleValidator(role=SYSROLE_ADMIN;ROLE_SYSPORTAL_EXT_SETTING)" /> 		<request 			path="sys_ui_tool/**" 			defaultValidator="roleValidator(role=SYSROLE_ADMIN;SYSROLE_SYSADMIN)" /> 		<request 			path="sys_ui_config/**" 			defaultValidator="roleValidator(role=SYSROLE_ADMIN;SYSROLE_SYSADMIN)" /> 		<request 			path="sys_ui_qrcode/**" 			defaultValidator="roleValidator(role=SYSROLE_USER)" /> 		<request 			path="/sys_ui_compress/sysUiCompress.do*" 			defaultValidator="roleValidator(role=SYSROLE_ADMIN;SYSROLE_SYSADMIN)"/> 	</module> </configs> ``` |

## getThemeInfo调用被拦截怎么破

​ 我们知道一些流量设备对于拦截的策略比较严格，特别是在hvv期间，为了防止被攻击会更容易使用一些更严格的规则，那假设我们对于`getThemeInfo`的调用被拦截了怎么办，最容易想到的思路就是尝试去寻找其他的利用，以`com.landray.kmss.sys.ui.actions.SysUiComponentAction#replaceExtend`为例，这里接收两个非空参数`extendId`和`folderName`

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``` | ``` public void replaceExtend(ActionMapping mapping, ActionForm form, HttpServletRequest request, HttpServletResponse response) throws Exception {     response.setCharacterEncoding("UTF-8");     if (UserOperHelper.allowLogOper("Base_UrlParam", (String)null)) {         UserOperHelper.setModelNameAndModelDesc((String)null, ResourceUtil.getString("sys-admin:home.nav.sysAdmin") + "(" + ResourceUtil.getString("sys-ui:ui.extend.replace") + ")");     }      String extendId = request.getParameter("extendId");     String folderName = request.getParameter("folderName");     if (StringUtil.isNotNull(extendId) && StringUtil.isNotNull(folderName)) {         try {             boolean bool = this.getSysUiComponentService().replaceExtend(request);             response.getWriter().print(bool ? "1" : "2");         } catch (Exception var8) {             this.logger.error("替换部件包失败：", var8);             response.getWriter().print("0");         }     } else {         response.getWriter().print("0");     }  } ``` |

继续往下看，再往下一层调用的是`com.landray.kmss.sys.ui.service.SysUiComponentService#replaceExtend`，在这里可以看到首先会删除`extendId`对应的目录，如果对应目录存在则删除并返回`true`

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``` | ``` public boolean replaceExtend(HttpServletRequest request) throws Exception {     String extendId = request.getParameter("extendId");     String folderName = request.getParameter("folderName");     boolean bool = this.deleteExtendDirectory(extendId);     if (bool) {         this.saveExtend(extendId, folderName);     }      return bool; }  public boolean deleteExtendDirectory(String extendId) throws Exception {     boolean bool = false;     if (StringUtil.isNotNull(extendId)) {         File extendFolder = new File(PluginConfigLocationsUtil.getWebContentPath() + "/sys/portal/template/ui_component/" + extendId);         if (extendFolder.exists()) {             File file = new File(ResourceUtil.KMSS_RESOURCE_PATH + "/ui_component/" + extendId);             FileUtils.deleteQuietly(file);             FileUtils.deleteDirectory(extendFolder);             SysFileLocationUtil.getFileService().deleteFile("/ui_component/" + extendId + ".zip");             bool = true;             ResourceCacheListener.updateResourceCache();         }     }      return bool; } ``` |

接下来我们重点看`com.landray.kmss.sys.ui.service.SysUiComponentService#saveExtend`，可以看到配合路径穿越能够复制任意目录到指定位置

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 ``` | ``` // com.landray.kmss.sys.ui.service.SysUiComponentService#saveExtend public void saveExtend(String extendId, String folderName) throws Exception {     String folderPath = System.getProperty("java.io.tmpdir");     if (!folderPath.endsWith("/") && !folderPath.endsWith("\\")) {         folderPath = folderPath + "/";     }      folderPath = folderPath + folderName;     File extendFolder = new File(ConfigLocationsUtil.getWebContentPath() + "/sys/portal/template/ui_component/" + extendId);     File resourcePath = new File(ResourceUtil.KMSS_RESOURCE_PATH + "/ui_component/" + extendId);     File sourcePath = new File(folderPath);     FileUtils.copyDirectory(sourcePath, resourcePath);     FileUtils.copyDirectory(sourcePath, extendFolder);     SysFileLocationUtil.getFileService().writeOFolder(folderPath, "/ui_component/", extendId + ".zip", "/ui_component/", (Map)null);     ResourceCacheListener.updateResourceCache(); }  // org.apache.commons.io.FileUtils#copyDirectory(File, File) public static void copyDirectory(File srcDir, File destDir) throws IOException {     copyDirectory(srcDir, destDir, true); }  public static void copyDirectory(File srcDir, File destDir, boolean preserveFileDate) throws IOException {     copyDirectory(srcDir, destDir, (FileFilter)null, preserveFileDate); }  public static void copyDirectory(File srcDir, File destDir, FileFilter filter) throws IOException {     copyDirectory(srcDir, destDir, filter, true); }  public static void copyDirectory(File srcDir, File destDir, FileFilter filter, boolean preserveFileDate) throws IOException {     checkFileRequirements(srcDir, destDir);     if (!srcDir.isDirectory()) {         throw new IOException("Source '" + srcDir + "' exists but is not a directory");     } else if (srcDir.getCanonicalPath().equals(destDir.getCanonicalPath())) {         throw new IOException...