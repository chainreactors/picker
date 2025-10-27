---
title: 浅析JeecgBoot-jmreport最新权限绕过
url: https://y4tacker.github.io/2024/08/01/year/2024/8/%E6%B5%85%E6%9E%90JeecgBoot-jmreport%E6%9C%80%E6%96%B0%E6%9D%83%E9%99%90%E7%BB%95%E8%BF%87/
source: Y4tacker:Hacking The World!
date: 2024-08-02
fetch_date: 2025-10-06T18:02:10.206439
---

# 浅析JeecgBoot-jmreport最新权限绕过

* [Home](/)
* [Writing](/archives/)
* [Topics](/tags/)
* [Search](/search/)
* [About](/about/)
* [Friends](/link/)

Previous post Next post Back to top Share post

# 浅析JeecgBoot-jmreport最新权限绕过

Y4tacker

2024-08-01 (Updated: 2025-09-02)

[Java](/categories/Java/)

[Java](/tags/Java/), [JeecgBoot](/tags/JeecgBoot/)

这个漏洞还是蛮有意思的，`/jmreport`下的拦截器是在`org.jeecg.modules.jmreport.config.init.JimuReportConfiguration#addInterceptors`中添加的，这部分非常简单

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` public void addInterceptors(InterceptorRegistry registry) {     String[] var2 = new String[]{"/*.js", "/*.css", "/*.svg", "/*.pdf", "/*.jpg", "/*.png", "/*.ico", "/*.html", "/html/**", "/js/**", "/css/**", "/images/**"};     registry.addInterceptor(this.jimuReportInterceptor()).excludePathPatterns(var2).addPathPatterns(new String[]{"/jmreport/**"});     registry.addInterceptor(this.jmSignatureInterceptor()).addPathPatterns(new String[]{"/jmreport/queryFieldBySql", "/jmreport/loadTableData", "/jmreport/dictCodeSearch", "/jmreport/testConnection"}); } ``` |

在这里我们主要看`org.jeecg.modules.jmreport.config.firewall.interceptor.JimuReportTokenInterceptor#preHandle`

从我以下标注的点开始看，对于带`JimuNoLoginRequired`注解的，也就是不用登录的类方法，那就直接跳过鉴权

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 ``` | ``` public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {     if (!(handler instanceof HandlerMethod)) {         return true;     } else {         String var4 = d.i(request.getRequestURI().substring(request.getContextPath().length()));         log.debug("JimuReportInterceptor check requestPath = " + var4);         int var5 = 500;         if (n.a(var4)) {             log.error("请注意，请求地址有xss攻击风险！" + var4);             this.backError(response, "请求地址有xss攻击风险!", var5);             return false;         } else {             String var6 = this.jmBaseConfig.getCustomPrePath();             log.debug("customPrePath: {}", var6);             if (j.d(var6) && !var6.startsWith("/")) {                 var6 = "/" + var6;             }              request.setAttribute("customPrePath", var6);             HandlerMethod var7 = (HandlerMethod)handler;             Method var8 = var7.getMethod();             // 关注点主要从这里开始             if (var4.contains("/jmreport/shareView/")) {                 return true;             } else {                 JimuNoLoginRequired var9 = (JimuNoLoginRequired)var8.getAnnotation(JimuNoLoginRequired.class);                 if (j.d(var9)) {                     return true;                 } else {                     boolean var10 = false;                      try {                         var10 = this.verifyToken(request);                     } catch (Exception var14) {                     }                      if (!var10) {                         if (this.jimuReportShareService.isSharingEffective(var4, request)) {                             return true;                         } else {                             String var16 = request.getParameter("previousPage");                             if (j.d(var16)) {                                 if (this.jimuReportShareService.isShareingToken(var4, request)) {                                     return true;                                 } else {                                     log.error("分享链接失效或分享token不匹配(" + request.getMethod() + ")：" + var4);                                     this.backError(response, "分享链接失效或分享token不匹配，禁止钻取!", var5);                                     return false;                                 }                             } else {                                 log.error("Token校验失败！请求无权限(" + request.getMethod() + ")：" + var4);                                 this.backError(response, "Token校验失败，无权限访问！", var5);                                 return false;                             }                         }                     } else {                         b var15 = (b)var8.getAnnotation(b.class);                         if (var15 != null) {                             String[] var11 = var15.a();                             String[] var12 = this.jimuTokenClient.getRoles(request);                             if (var12 == null || var12.length == 0) {                                 log.error("此接口需要角色权限，请联系管理员！请求无权限(" + request.getMethod() + ")：" + var4);                                 if ("/jmreport/loadTableData".equals(var4)) {                                     var5 = GEN_TEST_DATA_CODE;                                 }                                  this.backError(response, NO_PERMISSION_PROMPT_MSG, var5);                                 return false;                             }                              boolean var13 = Arrays.stream(var12).anyMatch((code) -> {                                 return j.a(code, var11);                             });                             if (!var13) {                                 log.error("此接口需要角色权限，请联系管理员！请求无权限(" + request.getMethod() + ")：" + var4);                                 if ("/jmreport/loadTableData".equals(var4)) {                                     var5 = GEN_TEST_DATA_CODE;                                 }                                  this.backError(response, NO_PERMISSION_PROMPT_MSG, var5);                                 return false;                             }                         }                          return true;                     }                 }             }         }     } } ``` |

接下来根据token的结果(这里就是JWTToken)，`var10 = this.verifyToken(request);`，如果校验成功则走else部分，如果不成功那么就走if部分，我们重点看这部分即可，对于`org.jeecg.modules.jmreport.desreport.service.a.f#isSharingEffective`

从逻辑来看，主要是对这部分API的处理，简单看没什么太多值得关注的点，利用面也太窄了

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 ``` | ``` GET_QUERY_INFO("/jmreport/getQueryInfo"), SHARE_VERIFICATION("/jmreport/share/verification"), ADD_VIEW_COUNT("/jmreport/addViewCount/"), SHOW_DATA("/jmreport/show"), EXPORT_PDF_STREAM("/jmreport/exportPdfStream"), EXPORT_ALL_EXCEL_STREAM("/jmreport/exportAllExcelStream"), CHECK_PARAM("/jmreport/checkParam/"), QUERYMAP_BY_CODE("/jmreport/map/queryMapByCode"), QUREST_SQL("/jmreport/qurestSql"), QUREST_API("/jmreport/qurestApi"), GET_CHAR_DATA("/jmreport/getCharData"); ``` |

我们主要关注`org.jeecg.modules.jmreport.desreport.service.a.f#isShareingToken`

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 ``` | ``` public boolean isShareingToken(String requestPath, HttpServletRequest request) {     String var3 = request.getHeader("JmReport-Share-Token");     String var4 = "";     if (j.c(var3)) {         var3 = request.getParameter("shareToken");     }      String var5 = request.getParameter("jmLink");     if (j.d(var5)) {         try {             byte[] var6 = Base64Utils.decodeFromString(var5);             String var7 = new String(var6);             String[] var8 = var7.split("\\|\\|");             if (ArrayUtils.isNotEmpty(var8) && var8.length == 2) {                 var3 = var8[0];                 var4 = var8[1];             }         } catch (IllegalArgumentException var9) {             a.error("解密失败：" + var9.getMessage());             a.error(var9.getMessage(), var9);             return false;         }     }      if (j.c(var3)) {         return false;     } else {         JimuReportShare var10 = this.jimuReportShareDao.getShareByShareToken(var3);         if (var10 != null) {             var10 = this.compareToDate(var10);             if (!"0".equals(var10.getStatus())) {                 return false;             }         }          if (requestPath.startsWith("/jmreport/view")) {             if (!j.d(var4)) {                 return false;  ...