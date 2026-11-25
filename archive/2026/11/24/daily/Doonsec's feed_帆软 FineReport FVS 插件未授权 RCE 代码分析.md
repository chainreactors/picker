---
title: 帆软 FineReport FVS 插件未授权 RCE 代码分析
url: https://mp.weixin.qq.com/s/CgXGY1_ajQBL6_GkfSX9aw
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:40:08.119128
---

# 帆软 FineReport FVS 插件未授权 RCE 代码分析

# 帆软 FineReport FVS 插件未授权 RCE 代码分析

Kratos
Kratos

Kratos Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

11 月 22 日，长亭安全应急响应中心发布通告并完成复现：帆软 FineReport 的 FineVis（FVS）大屏插件存在未授权远程代码执行，编号 QVD-2026-115643。攻击者不需要任何账号，向暴露在网络里的报表服务器上传并"应用"一个构造的 FVS 复用包（.mfvs 文件），就能以应用进程权限执行任意系统命令——复现环境里这个进程在容器内是 root。同一天 360 漏洞研究院发了独立通告，定性与长亭一致：鉴权、输入处理、连接层防护三处缺陷叠加。

两个背景先记下。一是 FVS 是帆软的可视化大屏插件，官方安装包通常自带——也就是说大量部署在金融、制造、政企的 FineReport 实例，默认就带着这个攻击面。二是修复版本（FineReport 11.5.16 与 FVS 插件 4.15.0，10 月 16 日发布）比披露早了一个多月，走了先修后曝的流程，但帆软官方漏洞声明页至今没有单列这个条目——十月份默默发版，十一月份才被通告点破，中间这一个多月打没打补丁，全看客户是不是每周盯升级公告。

登录校验是怎么被一个归一化为空的参数击穿的、复用包里的哪些字段变成了任意文件写和 JDBC URL 注入、以及三个执行出口分别借了服务端的什么现成能力——全程无内存破坏。

## 0x0 事件概述

| 项目 | 内容 |
| --- | --- |
| 编号 | QVD-2026-115643（长亭漏洞库；暂无 CVE，官方未给 CVSS 分值） |
| 组件 | FineReport + FineVis（FVS）插件复用资源导入链路（插件 artifact 名 wysiwyg，端点前缀 /view/duchamp） |
| 披露 | 长亭安全应急响应中心 2026-11-22 通告并复现；360 漏洞研究院同日独立通告 |
| 影响 | FineReport < 11.5.16 且 FVS 插件 < 4.15.0 |
| 修复 | FineReport 11.5.16 / FVS 4.15.0（均 2026-10-16 发布） |
| 前提 | 网络可达目标报表服务，且装有 FVS 插件（官方安装包通常自带）；无需任何凭据 |
| 结果 | 应用进程权限执行任意系统命令（实验容器内 uid=0），数据库连接凭据随之泄露 |
| 在野利用 | 截至通告发布未确认 |

复现口径两个来源可以互相印证：长亭在 FineReport 11.5.11 + FVS 4.9.0 上复现；社区仓库（evenomn/FineReport-FVS-Unauth-RCE，独立复现）在 11.5.15 + 插件 4.13.0 的出厂镜像上打通了全部三条执行路径。下文反编译级的代码证据均来自后者，与两家通告的成因描述逐条对得上。

## 0x1 攻击面：一个 .mfvs 复用包里装了什么，谁在校验它

FVS 内部代号 Duchamp，插件的 HTTP 端点全部挂在 `/view/duchamp/**` 下，其中复用包的上传与应用在 `/view/duchamp/reuse/*`。复用包（.mfvs）本意是模板及其依赖资源的搬家载体，解开后是几层结构：

```
content/biz/BizLayer.json                     # 实体映射
content/biz/attachments/AttachmentLayer.json  # 附件清单：{"attachInfos":[{exportPath, originPath}]}
content/biz/attachments/…                     # 附件本体（按清单写入服务端）
data/appdata.mv.db                            # 嵌入式 H2 示例库（数据层）
props.name                                    # 复用包名 → appName，多个环节复用
```

这些端点本应经过模板鉴权组件做登录校验。反编译 4.13.0 的鉴权逻辑（示意还原）：

```
// wysiwyg 插件 4.13.0，/view/duchamp/** 全端点共用
// DuchampTemplateRequestChecker.checkRequest（逻辑还原）
String templateId = normalize(req.getParameter("tplPath"));
// normalize 会剥掉模板目录前缀，例如 "reportlets/xxx" → "xxx"
if (StringUtils.isEmpty(templateId)) {
    return true;                    // 空值 = 判定为"无需登录的模板访问"，直接放行
}
return loginCheck(req, templateId); // 正常路径：按 templateId 查权限
```

缺陷就在这：`?tplPath=reportlets` 剥掉 `reportlets` 前缀后得到**空字符串**，`checkRequest` 对空 templateId 直接返回 true。请求被当成"无需登录的模板访问"，未认证用户就此进入了本该登录才能用的上传与 apply 流程。带尾斜杠的 `reportlets/` 同样剥空——证明根因是"空值放行"而不是某个特定字符串。版本差分给了实锤：4.15.0 加了空值卫兵，同样的请求被拒。

一个参数归一化为空，整棵 `/view/duchamp/**` 端点树的登录校验就全部失效。这是 360 通告里"资源复用与模板导入接口在特定请求形态下会错误放行未登录请求"的代码形态。

## 0x2 字段流向：复用包里两个不带过滤的入口

进门之后看数据流。复用包应用阶段，导入组件把包内字段往两个危险方向送，对应两个缺陷。

**入口一：props.name 一路拼进 JDBC URL。** 数据层的导入代码（反编译）：

```
// fine-app-reuse-2.1-SNAPSHOT.jar  DBFileImporter.writeDuckFile
byte[] data = IOUtils.inputStream2Bytes(dataLayer.getDirectory().read("appdata.mv.db"));
this.localImportAndTestConnect(reusePack.readInfo().getName(), data);  // name 可控

// localImportAndTestConnect 双流程穿透
String dbPath = ExampleDBFileUtils.importDBFileToLocal(appName, data); // ① 写文件
ExampleDBConnectionHelper.local(dbPath).testConnection();              // ② 建连接
```

流程① 把上传的 mv.db 写到 `<WEB-INF>/assets/reuse/import_temp_dir/<appName>/appdata.mv.db`——appName 是复用包名，攻击者可控。流程② 打开它时 URL 由 `H2ExampleDB.constructUrl` 拼出：

```
return String.format("%s:%s;%s", "jdbc:h2", path /* 含 appName */,
        "USER=sa;DEFAULT_LOCK_TIMEOUT=5000;MODE=MYSQL;…");   // 尾部固定设置串
```

appName 落在 `;` 分隔的连接设置串中间——**在这里面注入 `;INIT=…` 就是一条合法的 H2 连接设置**，URL 尾部自动拼的库名用 SQL 行注释 `--` 吃掉。`testConnection` 建立连接时执行 INIT 语句，H2 内置的 `FILE_WRITE(字节, 路径)` 就是任意路径、任意后缀的文件写。

**入口二：附件清单直通 WEB-INF。** 附件层的导入先于实体导入执行：

```
// BizLayerImporterChain.apply（反编译）
AttachmentLayerBean bean = …getAttachmentLayer().getInfo();  // 读包内 AttachmentLayer.json
for (AttachmentInfoBean a : bean.getAttachInfos()) {
    byte[] data = attachmentLayer.getDirectory().read(a.getExportPath());
    SafeImportIO.write(a.getOriginPath(), data);             // originPath 相对 WEB-INF
}
```

`SafeImportIO.write` 只有两道检查（反编译，4.13.0）：

```
ReuseFileUtils.checkInvalidPath(path);                 // 路径中不得出现 ".." 子串，
                                                      // 目录名不得为 classes/lib/plugins
if (FileSecurityChecker.check(data, getSuffix(path)))  // 后缀白名单：
                                                      // geojson env fedge svg cpt fvs frm
                                                      // json js css xml txt + 魔数放行
    WorkContext.getWorkResource().write(path, data);   // new File(WEB-INF 根 + path) 直接写
```

看起来有白名单有黑名单，但罩不住要害：`.xml` 在白名单里——**WEB-INF/web.xml 可以整个覆盖**；`.env` 也在——**JSP 内容换个后缀照写**。`..` 被拦、`classes` 目录被禁，所以附件层出不了 WEB-INF，但 WEB-INF 根部本身就是攻击者想要的落点。

**连接层的拦截机制为什么没起作用。** 这是 360 通告里最含糊的一句——"连接层原有的危险参数拦截机制在该调用路径上未正常启用"。社区复现把这件事查清了：插件内置定制加固版驱动 `h2-jdk8-0.1-SNAPSHOT.jar`（基线 2.2.224），`ExampleDBClassLoaderHandler.isInterceptAllowed` 对所有 `jdbc:h2:` 开头的 URL 记一条 `The connection has been intercepted.` 然后**放行**——它的实际作用是把 H2 驱动替换成加固版，也就是说拦截机制存在、并且在本路径上执行了，问题出在加固内容罩不住载荷：

| # | 定制加固（反编译） | 绕过方式 |
| --- | --- | --- |
| 1 | `Command.checkBeforeUpdate` ：语句含 `$$` 且含 `java` → 拒绝 | 载荷不用 `$$` |
| 2 | `RunScriptCommand.checkSql` ：RUNSCRIPT 文件白名单 + ALIAS 正则 | **CALL/查询语句不经过 checkSql** |
| 3 | parser：单引号源码形式 ALIAS 直接语法报错 | 不用源码 ALIAS |

三条加固全部针对"CREATE ALIAS 执行 Java 代码"这条经典 H2 RCE 老路，而 `INIT=CALL FILE_WRITE(...)` 根本不走这三条道。加固对着昨天的攻击面，载荷走的是今天的位置。

## 0x3 三个执行出口：都借服务端现成的能力

文件写和 JDBC 注入到手，剩下的的问题是"写到哪、怎么被执行"。同一个鉴权缺陷，三条路。

**出口 A：H2 的 FILE\_WRITE，直接写执行载体。** 单语句 `CALL FILE_WRITE(X'hex','绝对路径')` 一次写一个文件，无路径后缀限制。两种用法：交互式——写一个小 JSP 到 Tomcat 默认的 ROOT webapp，`GET /xxx.jsp?c=<命令>` 即时执行；植入式——三枪连写投毒的 `WEB-INF/web.xml`、内容为 jspInit 声明块的 `WEB-INF/x.env`、以及 Tomcat 上下文描述符，然后什么都不做，等容器自己动。出厂镜像实测时间线：

| 时间 | 事件 |
| --- | --- |
| 14:27:17–18 | 三枪写入：毒 web.xml、x.env、conf/Catalina/localhost/z.xml |
| 14:27:21 | Tomcat 日志出现 deployDescriptor（3 秒后） |
| 14:28:03 | 部署完成（42.5 秒），jspInit 执行，输出文件落地 uid=0 |

机制拆开是三层现成能力的接力：Tomcat 出厂默认 `autoDeploy="true"`，`HostConfig` 每约 10 秒扫一遍上下文描述符，发现新增就自动部署；部署时要读 `WEB-INF/web.xml`（被投毒的那个）；web.xml 里声明了 `<jsp-file>/WEB-INF/x.env</jsp-file>` 加 `<load-on-startup>1</load-on-startup>`，Jasper 部署期预编译这个"JSP"并初始化 servlet——**jspInit() 在重载过程中自动执行，全程零触发请求**：

```
<!-- 覆盖写入的 WEB-INF/web.xml（FR 本体没有 web.xml，servlet 走注解注册，
     写一个全新的不会破坏原功能） -->
<servlet>
  <servlet-name>xs</servlet-name>
  <jsp-file>/WEB-INF/x.env</jsp-file>   <!-- .env 过后缀白名单，内容是 JSP -->
  <load-on-startup>1</load-on-startup>  <!-- 部署时预编译并执行 jspInit -->
</servlet>
```

```
<%! public void jspInit() {
  try { Runtime.getRuntime().exec(new String[]{"/bin/sh","-c","<命令>"}).waitFor(); }
  catch (Throwable t) {}
} %>
```

**出口 B：纯附件层，连 H2 都不用。** 对由 Tomcat 自己管理的应用，`WEB-INF/web.xml` 一变就自动重载（与 reloadable 无关）——所以仅靠附件清单覆盖一个 web.xml 加写入 x.env 就是完整利用，实测写入后 8 秒触发重载、约 64 秒后 jspInit 以 uid=0 执行。这条出口对应长亭通告那句"附件可被写入应用的 WEB-INF 目录，甚至覆盖容器配置，容器检测到配置变更后重载，写入的代码随之被解析执行"。帆软官方 ops 镜像把 /webroot 写死在 server.xml 且 appBase="none"，应用不受部署管理，纯附件只能潜伏等重启——但出口 A 的描述符一写，应用就转为 Tomcat 管理，两条出口就此合流。

**出口 C：类加载 + 模板实例化，最安静的一条。** FR 解析模板 XML 时对 `class` 属性的处理（反编译）：

```
// com.fr.general.xml.GeneralXMLTools.readXMLable
if (reader.getAttrAsString("class", null) != null) {
    xMLable = (XMLable) reader.getAttrAsClass(...).newInstance();  // 按类名加载+实例化
    …
} catch (Exception e) { /* 只打一条 warn */ }
```

三步组合：附件把类文件字节以 `.txt` 后缀落进 `WEB-INF/logs/`（白名单内且不查文件头）；H2 的 `FILE_WRITE(FILE_READ(…), …)` 把它复制到 `WEB-INF/classes/V.class`——目标路径里的 `classes` 在 SQL 里拼接构造，躲开路径名检查；再导入一个 XML 里写着 `<Layout class="V"/>` 的 frm 模板，导入器解析时 V 被加载实例化，静态块和构造函数执行，读命令、执行、把输出写到 webroot 静态文件等待回读。全程约 3–5 秒，**不写 JSP、不改 web.xml、不依赖任何重载**，JSP 类监控完全无感。随后的导入失败空指针发生在执行之后，不触发回滚。

三条出口对照：

|  | A：H2 数据连接层 | B：附件层 | C：类文件+模板实例化 |
| --- | --- | --- | --- |
| 入口字段 | props.name → JDBC URL | AttachmentLayer.json | 附件字节 + 包内 frm 模板 |
| 写入能力 | 任意路径任意后缀 | WEB-INF 内、白名单后缀 | 任意（H2 代复制） |
| 执行载体 | JSP / jspInit | jspInit | 类加载 newInstance |
| 依赖重载 | 交互不依赖，植入依赖 autoDeploy | 依赖应用重载 | 不依赖 |
| 监控穿透 | 换 webapp 绕 JSP-Monitor | WEB-INF+非 jsp 后缀 | 不落 JSP |

共同点值得点透：**没有任何内存破坏，全是服务端已有合法能力...