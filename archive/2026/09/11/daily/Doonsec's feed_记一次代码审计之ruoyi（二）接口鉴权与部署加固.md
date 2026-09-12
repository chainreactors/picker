---
title: 记一次代码审计之ruoyi（二）接口鉴权与部署加固
url: https://mp.weixin.qq.com/s/cxxOOOIzrerwZJxEDOz5zg
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:45:43.560084
---

# 记一次代码审计之ruoyi（二）接口鉴权与部署加固

# 记一次代码审计之ruoyi（二）接口鉴权与部署加固

Khan安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

记一次代码审计之 RuoYi-Cloud（二）：接口鉴权缺失与部署加固

系列文章第二篇，聚焦接口层鉴权缺失与部署暴露面：从"批量排查漏标权限注解的接口"这一高效审计手法入手，逐一还原文件服务未鉴权、越权读取、actuator/swagger 暴露、运行时竞态与纵深防御缺口。

审计目标：若依微服务版 RuoYi-Cloud v3.6.8

1. 引言

第一篇讲的是"信任了不该信任的输入"。本篇讲的则是另一类根因：该设防的地方没设防——大量接口只依赖"网关要求登录"这一层兜底，业务层没有自己的权限校验；以及该隐藏的东西没藏住——监控端点、接口文档、内部端口直接暴露。

本篇覆盖的问题：

| 漏洞 | 严重性 | 一句话 |
| --- | --- | --- |
| 文件上传/删除接口未鉴权 | 🔴 高 | 未授权上传 + 任意登录用户删除他人文件 |
| 系统参数配置越权读取 | 🟠 中 | 遍历读取全部 sys\_config（含黑名单/初始密码） |
| 角色菜单权限越权读取 | 🟡 中低 | 枚举角色查看任意角色的权限分配 |
| 公告详情越权读取 | 🟡 中低 | 遍历读取任意公告全文 |
| Gen 表结构越权访问 | 🟡 低 | 任意登录用户读取代码生成表结构 |
| Monitor actuator 未授权 | 🟠 中 | /actuator/env、/heapdump 等未认证可达 |
| Swagger 接口文档暴露 | 🟡 中低 | 未登录获取全量接口定义 |
| ValidateCodeFilter 竞态 | 🟠 中 | 验证码校验不可靠，登录链路可用性缺陷 |
| 定时任务 DB 篡改 → RCE | 🟠 中 | 执行路径无二次白名单校验 |

2. 审计方法：权限注解缺失的批量排查

RuoYi 系项目的权限模型是注解驱动的：Controller 方法上标注 @RequiresPermissions("system:xxx:yyy")，由 PreAuthorizeAspect 切面统一鉴权。因此"漏标注解"就是直接漏权限。批量排查非常高效：

```
# 找出所有 Controller 方法，逐一核对上方是否有权限注解grep -rn "public \(AjaxResult\|TableDataInfo\|R<\|void\)" --include="*Controller.java" ruoyi-modules/ | grep -v "RequiresPermissions"
```

更可靠的验证手法是"对照请求"：同一低权限账号，访问疑似越权接口返回 200，访问该模块"需要权限"的列表接口返回 403——200 说明不是账号有权限，而是注解缺失。以 /system/config 为例：

```
# 请求A：疑似越权GET /system/config/1 HTTP/1.1Authorization: Bearer <低权限token># → 200 返回配置
# 请求B：对照（有权限注解）GET /system/config/list HTTP/1.1Authorization: Bearer <低权限token># → 403 "没有访问权限，请联系管理员授权"
```

A 能读、B 被拒，即可坐实"注解缺失"而非"账号有权限"。整套 PoC 里都用这个思路，防误报。

3. 高危：文件上传/删除接口完全未鉴权

3.1 漏洞点①：Controller 无任何鉴权注解

ruoyi-modules/ruoyi-file/src/main/java/com/ruoyi/file/controller/SysFileController.java:32-71

```
@PostMapping("upload")public R<SysFile> upload(MultipartFile file) { ... }   // 无 @RequiresPermissions / @InnerAuth
@DeleteMapping("delete")public R<Boolean> delete(String fileUrl) {    try {        if (!FileUtils.validateFilePath(fileUrl)) {            throw new Exception("资源文件({})非法，不允许删除。");        }        sysFileService.deleteFile(fileUrl);   // 直接删除        return R.ok();    } ...}
```

检查 file 服务的 pom.xml：它甚至没有引入 ruoyi-common-security，意味着服务自身连拦截器都没有，全靠网关兜底。而网关对 /file/\*\* 只要求"有登录 token"，任意低权限用户即可调用。

3.2 漏洞点②：删除只做弱校验

ruoyi-modules/ruoyi-file/src/main/java/com/ruoyi/file/service/LocalSysFileServiceImpl.java:60-64

```
@Overridepublic void deleteFile(String fileUrl) throws Exception {    String localFile = StringUtils.substringAfter(fileUrl, localFilePrefix);    FileUtils.deleteFile(localFilePath + localFile);   // 拼接后直接删}
```

FileUtils.validateFilePath 只拦 .. + 限制扩展名（MimeTypeUtils.DEFAULT\_ALLOWED\_EXTENSION：png/jpg/txt/zip/doc/pdf 等）。也就是上传目录内任何符合扩展名的文件都能被删，包括他人上传的。

3.3 漏洞点③：docker-compose 把端口暴露到宿主机

docker/docker-compose.yml 将 file 服务 9300 端口映射到宿主机 → 直连 http://<ip>:9300/upload 时连 token 都不要，完全未授权。

3.4 攻击链与验证

```
flowchart LR    A[攻击者] -->|POST /upload 无认证| B[file服务 9300]    B --> C[(磁盘写入任意文件)]    A -->|DELETE /delete?fileUrl=目标文件| B    B --> D[(删除他人上传文件)]    style B fill:#ffcdd2,color:#b71c1c
```

```
# 未授权上传（直连 file 服务）POST /upload HTTP/1.1Host: 127.0.0.1:9300Content-Type: multipart/form-data; boundary=----x------xContent-Disposition: form-data; name="file"; filename="poc.txt"Content-Type: text/plain
poc------x--
# 未授权删除DELETE /delete?fileUrl=http%3A%2F%2F127.0.0.1%3A8080%2Fprofile%2F...%2Fpoc.txt HTTP/1.1Host: 127.0.0.1:9300
```

影响：存储耗尽、存放违规内容、删除他人文件造成数据丢失（DoS）。上传扩展名白名单不含脚本类型，未直接 RCE——但如果部署方自定义了允许 html/jsp 等，风险立即升级为存储型 XSS/webshell。

3.5 修复建议

* upload/delete 增加 @InnerAuth（需先给 file 模块引入 ruoyi-common-security），仅允许内部 Feign 调用；

* 删除改为按文件归属（ownerId）校验；

* 生产环境禁止 file 服务端口外放。

4. 权限注解缺失系列：越权读取

用第 2 节的批量手法，命中 4 个越权读取点。

4.1 系统参数配置越权读取（中）

ruoyi-modules/ruoyi-system/src/main/java/com/ruoyi/system/controller/SysConfigController.java:63-76

```
@GetMapping(value = "/{configId}")          // 无 @RequiresPermissionspublic AjaxResult getInfo(@PathVariable Long configId) {    return success(configService.selectConfigById(configId));}
@GetMapping(value = "/configKey/{configKey}")  // 无 @RequiresPermissionspublic AjaxResult getConfigKey(@PathVariable String configKey) {    return success(configService.selectConfigByKey(configKey));}
```

影响：任意登录用户可遍历 configId 读取全部 sys\_config——sys.login.blackIPList（登录黑名单 IP，可用于针对性绕过）、sys.user.initPassword（初始密码）、密码策略等内部配置全部泄露。

4.2 角色菜单权限越权读取（中低）

ruoyi-modules/ruoyi-system/src/main/java/com/ruoyi/system/controller/SysMenuController.java:74-83

```
@GetMapping(value = "/roleMenuTreeselect/{roleId}")   // 无 @RequiresPermissionspublic AjaxResult roleMenuTreeselect(@PathVariable("roleId") Long roleId) {    ...    ajax.put("checkedKeys", menuService.selectMenuListByRoleId(roleId));  // 任意角色的菜单权限    ...}
```

影响：枚举 roleId 即可还原整个 RBAC 权限模型（哪些角色拥有哪些菜单），便于横向/垂直探测。

4.3 公告详情越权读取（中低）

ruoyi-modules/ruoyi-system/src/main/java/com/ruoyi/system/controller/SysNoticeController.java:57-61

```
@GetMapping(value = "/{noticeId}")    // 无 @RequiresPermissionspublic AjaxResult getInfo(@PathVariable Long noticeId) {    return success(noticeService.selectNoticeById(noticeId));}
```

影响：遍历 noticeId 读取任意公告全文。公告往往包含内部通知、链接、账号信息。

4.4 代码生成表结构越权访问（低）

ruoyi-modules/ruoyi-gen/src/main/java/com/ruoyi/gen/controller/GenController.java:92-100

```
@GetMapping(value = "/column/{tableId}")   // 无 @RequiresPermissions（同文件其他接口都有）public TableDataInfo columnList(Long tableId) {    ...}
```

影响：任意登录用户枚举 tableId 获取已导入表的列名/类型/注释，泄露数据库表结构。

4.5 汇总

| 接口 | 泄露内容 | 修复 |
| --- | --- | --- |
| GET /system/config/{id}、/configKey/{key} | 全部系统配置 | 加 system:config:query |
| GET /system/menu/roleMenuTreeselect/{roleId} | 角色权限分配 | 加 system:menu:query |
| GET /system/notice/{noticeId} | 公告全文 | 加 system:notice:query |
| GET /gen/column/{tableId} | 表结构元数据 | 加 tool:gen:query |

共性根因：开发时"顺手没标注解"，又依赖网关登录态兜底，权限缺口被掩盖。批量排查 + 对照请求验证是这类问题最高效的审计方式。

5. 部署暴露面：监控与文档

5.1 Monitor actuator 未授权（中）

ruoyi-visual/ruoyi-monitor/src/main/java/com/ruoyi/modules/monitor/config/WebSecurityConfigurer.java:40-44

```
.authorizeHttpRequests(    (authorize) -> authorize        .requestMatchers(adminContextPath + "/assets/**",            adminContextPath + "/login",            adminContextPath + "/actuator/**",    // ← 未授权放行            adminContextPath + "/instances/**")   // ← 未授权放行        .permitAll()        .anyRequest().authenticated())
```

影响（取决于 nacos 中 management.endpoints.web.exposure.include 的暴露范围）：/actuator/env 泄露环境变量（可能含 DB/Redis 凭据）、/actuator/heapdump 转储堆内存（含内存中的密钥/Token）、/instances/\*\* 泄露全部注册实例元数据。

```
GET /actuator/env HTTP/1.1Host: 127.0.0.1:9100# 未认证返回 200 → 高危信息泄露
```

修复：仅放行 /actuator/health、/actuator/info；exposure.include 只保留 health,info；端口不外放。

5.2 Swagger 接口文档暴露（中低）

ruoyi-gateway/src/main/java/com/ruoyi/gateway/config/SpringDocConfig.java:54-81

```
private final static String[] EXCLUDE_ROUTES = new String[] { "ruoyi-gateway", "ruoyi-auth", "ruoyi-file", "ruoyi-monitor" };...swaggerUrl.setUrl(String.format("/%s/v3/api-docs", instance.getServiceId()));
```

网关把 system/job/gen 的 /v3/api-docs 聚合进 Swagger UI。配合官方默认 nacos security.ignore.whites 放行 /v3/api-docs 与 /swagger-ui/\*\*：

```
GET /v3/api-docs HTTP/1.1Host: 127.0.0.1:8080# 未登录返回全量接口定义（路径/参数/模型）
```

影响：攻击面全量暴露，大幅降低渗透成本。修复：网关默认不放行 swagger 路径，或加登录认证。

6. 运行时缺陷与纵深防御

6.1 ValidateCodeFilter 异步读 body 竞态（中）

ruoyi-gateway/src/main/java/com/ruoyi/gateway/filter/ValidateCodeFilter.java:67-79

```
private String resolveBodyFromRequest(ServerHttpRequest serverHttpRequest) {    Flux<DataBuffer> body = serverHttpRequest.getBody();    AtomicReference<String> bodyRef = new AtomicReference<>();    body.subscribe(buffer -> {              // ① 异步订阅        ...        bodyRef.set(charBuffer.toString());    });    return bodyRef.get();                   // ② 立即取值 → 竞态！}
```

subscribe 是异步的，bodyRef.get() 大概率拿到 null：JSON.parseObject(null) → NPE → 登录被拒；若时序恰好成功，body 已被消费且未缓存回放，下游 auth 服务收到空 body → "用户/密码必须填写"。开启验证码后登录链路不可靠（表现为 500/登录失败为主），是认证链路的可用性缺陷。

修复：改用 DataBufferUtils.join(body).block() 阻塞读取，并用 ServerHttpRequestDecorator 缓存 body 回放下游。

6.2 定时任务 DB 篡改 → 任意方法反射 RCE（中）

ruoyi-modules/ruoyi-job/src/main/jav...