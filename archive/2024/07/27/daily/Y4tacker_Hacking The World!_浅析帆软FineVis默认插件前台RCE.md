---
title: 浅析帆软FineVis默认插件前台RCE
url: https://y4tacker.github.io/2024/07/26/year/2024/7/%E6%B5%85%E6%9E%90%E5%B8%86%E8%BD%AFFineVis%E9%BB%98%E8%AE%A4%E6%8F%92%E4%BB%B6%E5%89%8D%E5%8F%B0RCE/
source: Y4tacker:Hacking The World!
date: 2024-07-27
fetch_date: 2025-10-06T17:41:31.629225
---

# 浅析帆软FineVis默认插件前台RCE

* [Home](/)
* [Writing](/archives/)
* [Topics](/tags/)
* [Search](/search/)
* [About](/about/)
* [Friends](/link/)

Previous post Next post Back to top Share post

# 浅析帆软FineVis默认插件前台RCE

Y4tacker

2024-07-26 (Updated: 2025-09-02)

[Java](/categories/Java/)

[Java](/tags/Java/), [帆软](/tags/%E5%B8%86%E8%BD%AF/)

这个漏洞根本原因还是未授权与程序内部校验问题所导致，分析这个漏洞适合倒着来更容易分析

在`com.fr.plugin.wysiwyg.web.controller.DuchampThemeRequestService#applyThemeResource2Tpl`中

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 ``` | ``` public void applyThemeResource2Tpl(HttpServletRequest req, HttpServletResponse res, @RequestBody ThemeResourceBean bean) throws Exception {     WebUtils.printAsJSON(res, DuchampThemeRequestHelper.applyThemeResource2Tpl(bean)); }  public class ThemeResourceBean {     private String id;     private String[] attachIDs;     private String[] reuseIDs;     private String tplPath;      public ThemeResourceBean() {     }      public String getId() {         return this.id;     }      public String[] getAttachIDs() {         return this.attachIDs;     }      public String[] getReuseIDs() {         return this.reuseIDs;     }      public String getTplPath() {         return this.tplPath;     } } ``` |

继续跟进`DuchampThemeRequestHelper.applyThemeResource2Tpl`，首先根据`id`获取对应的样式模板，之后遍历`attachIDS`，并提取对应`attachID`中的文件内容以及`metadata`信息，之后根据`attachID`是否为图片文件后缀，如果不是则取`metadata`中 的内容，并调用`DuchampIO.EDIT_CACHE.write`完成文件写入（这里存在一个严重的逻辑绕过问题，导致可以实现任意文件写入）

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 ``` | ``` // com.fr.plugin.wysiwyg.web.controller.DuchampThemeRequestHelper#applyThemeResource2Tpl static JSONArray applyThemeResource2Tpl(ThemeResourceBean bean) throws IOException {     FVSTemplateStyle fvsTemplateStyle = FVSTemplateStyleConfig.getInstance().get(bean.getId());     JSONArray result = new JSONArray();     if (fvsTemplateStyle != null) {         String[] var3 = bean.getAttachIDs();         int var4 = var3.length;          for(int var5 = 0; var5 < var4; ++var5) {             String attachID = var3[var5];             byte[] image = fvsTemplateStyle.getAttachImage(attachID);             JSONObject metadata = new JSONObject(fvsTemplateStyle.getAttachMetadata(attachID).getMap());              try {                 String name = DuchampResourceRequestHelper.isImageResource(attachID) ? attachID : metadata.optString("name");                 if (StringUtils.isEmpty(name)) {                     name = attachID + ".png";                 }                  DuchampIO.EDIT_CACHE.write(bean.getTplPath(), name, image);                 result.add(metadata.put("name", name));             } catch (Exception var10) {                 FineLoggerFactory.getLogger().error("applyThemeResource2Tpl :{} error", new Object[]{attachID});                 FineLoggerFactory.getLogger().error(var10.getMessage(), var10);             }         }     }      return result; }  // com.fr.plugin.wysiwyg.web.controller.DuchampResourceRequestHelper#isImageResource private static final Set<String> IMAGE_SUFFIXES = new HashSet(Arrays.asList("jpg", "jpeg", "png", "apng", "webp", "hdr", "gif"));  public static boolean isImageResource(String resource) {     String suffix = resource.substring(resource.lastIndexOf(".") + 1);     return IMAGE_SUFFIXES.contains(suffix); } ``` |

`DuchampIO.EDIT_CACHE.write`，最终通过`com.fr.plugin.wysiwyg.io.fvs.edit.FVSFileOperateWrapper4Edit#write(String, String, byte[])`，逻辑很简单简单看看即可

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``` | ``` public static final String INITIAL_TEMP_PATH = StableUtils.pathJoin(new String[]{"assets", "fvs", "initial_temp"});  public boolean write(String zipPath, String resourceName, byte[] data) {     synchronized(ZipTplHelper.createFileLock(zipPath)) {         String cacheFolderPath = this.getResourceCacheFolderPath(zipPath);         String cacheResourcePath = StableUtils.pathJoin(new String[]{cacheFolderPath, resourceName});         WorkContext.getWorkResource().write(cacheResourcePath, data);         CacheTimestampHelper.makeCacheTimestampInconsistent(cacheFolderPath);         return true;     } }  private String getResourceCacheFolderPath(String zipPath) {     return isInitialTempPath(zipPath) ? zipPath : ZipSyncConfigManager.getCachePath("FVSIO", zipPath); }  static boolean isInitialTempPath(String zipPath) {     return zipPath.startsWith(INITIAL_TEMP_PATH); } ``` |

接下来由于我们的文件名以及文件内容就是持久化存入`FVSTemplateStyle`对象中，接下来我们需要查找从哪里做了保存处理

最终在`attach`路由发现存在这部分保存操作，很简单传入`id`、`attachID`以及文件上传流即可，当然`id`对应的值需要在`FVSTemplateStyleConfig`中，这部分其实也就是创建模板

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 ``` | ``` @PostMapping({"/attach"}) @ResponseBody @TemplateAuth(     product = TemplateProductType.FVS ) public void uploadAttachImage(HttpServletRequest request, HttpServletResponse response) throws Exception {     DuchampThemeRequestHelper.uploadTemplateStyleAttach(request, response); }  public static void uploadTemplateStyleAttach(HttpServletRequest request, HttpServletResponse response) throws Exception {     String id = WebUtils.getHTTPRequestParameter(request, "id");     String attachID = WebUtils.getHTTPRequestParameter(request, "attachID");     if (!StringUtils.isEmpty(id) && !StringUtils.isEmpty(attachID)) {         FVSTemplateStyle templateStyle = FVSTemplateStyleConfig.getInstance().get(id);         if (templateStyle == null) {             FineLoggerFactory.getLogger().error("no template style on fr server, id is {}", new Object[]{id});         } else {             Pair<ParseResult, InputStream> pair = DuchampResourceRequestHelper.getFileFromReq(request);             InputStream fileDecoratorStream = (InputStream)pair.getSecond();             if (pair.getFirst() != null && fileDecoratorStream != null) {                 templateStyle.addAttachImage(attachID, IOUtils.inputStream2Bytes(fileDecoratorStream));                 JSONObject metadata = new JSONObject(WebUtils.getHTTPRequestParameter(request, "metadata"));                 templateStyle.addAttachMetadata(attachID, metadata);                 FVSTemplateStyleConfig.getInstance().update(id, templateStyle, new CallBackAdaptor());                 WebUtils.printAsString(response, String.format("%s&themeID=%s", attachID, id));             } else {                 FineLoggerFactory.getLogger().error("sth is error with image file, id is {}", new Object[]{id});             }         }     } else {         FineLoggerFactory.getLogger().error("invalid id or attachID, id is {}, attachID is {}", new Object[]{id, attachID});     } } ``` |

创建模板的处理在`com.fr.plugin.wysiwyg.web.controller.DuchampThemeRequestService#copy`

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``` | ``` @PostMapping({"/item/copy"}) @ResponseBody @TemplateAuth(     product = TemplateProductType.FVS ) public void copy(HttpServletRequest request, HttpServletResponse response) throws Exception {     String id = WebUtils.getHTTPRequestParameter(request, "id");     String sourceID = WebUtils.getHTTPRequestParameter(request, "sourceID");     String config = WebUtils.getHTTPRequestParameter(request, "config");     DuchampThemeRequestHelper.copy(id, sourceID, new JSONObject(config)); } // com.fr.plugin.wysiwyg.web.controller.DuchampThemeRequestHelper#copy public static void copy(String id, String sourceID, JSONObject config) {     FVSTemplateStyle templateStyle = FVSTemplateStyleConfig.getInstance().get(sourceID);     if (templateStyle == null) {         templateStyle = new FVSTemplateStyle();     } else {         try {             templateStyle = (FVSTemplateStyle)templateStyle.clone();         } catch (CloneNotSupportedException var5) {         }     }      templateStyle.setConfig(config);     FVSTemplateStyleConfig.getInstance().update(id, templateStyle, new Call...