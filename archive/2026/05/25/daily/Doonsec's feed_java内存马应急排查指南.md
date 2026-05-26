---
title: java内存马应急排查指南
url: https://mp.weixin.qq.com/s/jOFOkvCQnm8KofpO4rmfIQ
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:02:32.601879
---

# java内存马应急排查指南

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8XAVqrZAgibJRnzGBm6rpQ2NAa6Oz1yr4YCyAqfMEjCYn5wZV6uNsqX5WibalfSBzZrqef8h6a9NFfSd1Lk1bA046Z2ibqMJwMtSH4GtvO2ZWU/0?wx_fmt=jpeg)

# java内存马应急排查指南

Xluo
Xluo

摸鱼划水

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

本文转载至Xluo大佬写java内存马应急排查指南

```
================================================================================  内存马应急排查手册 v2.0  |  更新日期: 2026-05  场景: 安全演练期间服务器被植入内存马，上机应急定位与清除  适用环境: Linux (x86_64/ARM64), Java Web (Tomcat / Spring Boot / Resin)  使用方式: 逐条复制到终端执行，观察输出结果================================================================================
命令标记说明:  [必] 必须执行  [荐] 强烈建议  [选] 视情况执行
================================================================================〇、快速决策流程================================================================================
                        ┌─────────────────┐                        │  上机排查内存马  │                        └────────┬────────┘                                 │                    ┌────────────▼────────────┐                    │ [1-3] 确认Java进程信息   │                    │ 检查 -javaagent 等可疑参数│                    └────────────┬────────────┘                                 │              ┌──────────────────┼──────────────────┐              │                  │                  │    ┌─────────▼─────────┐  ┌────▼─────┐  ┌────────▼────────┐    │[6-13] 找磁盘注入器 │  │[14-18]   │  │[19-22]          │    │ 可疑JSP/class文件  │  │配置篡改   │  │网络连接排查     │    └─────────┬─────────┘  └────┬─────┘  └────────┬────────┘              │                  │                  │              └──────────────────┼──────────────────┘                                 │                    ┌────────────▼────────────┐                    │ [23-37] Arthas内存马检测 │                    │ sc -d 查恶意类 + codeSource│                    └────────────┬────────────┘                                 │                    ┌────────────▼────────────┐                    │    判断 codeSource       │                    └─┬─────────────────────┬─┘                      │                     │            指向JSP/jar路径            为空/null            ┌─▼──────────────┐   ┌──────▼──────────┐            │磁盘有注入器     │   │远程漏洞一次性注入 │            │删注入器+重启    │   │重启即清除,查日志  │            └────────────────┘   └─────────────────┘
紧急场景: 直接跳到「快速排查6步法」(第60-65条)

================================================================================一、已知内存马特征速查表================================================================================
┌──────────┬──────────────────────────────────┬──────────────────────────────┐│ 工具      │ 已知类名/特征                     │ 类型                          │├──────────┼──────────────────────────────────┼──────────────────────────────┤│ 冰蝎      │ EdwardsiidaeFilter               │ Filter型                     ││          │ EdwardsiidaeServlet              │ Servlet型                    │├──────────┼──────────────────────────────────┼──────────────────────────────┤│ 哥斯拉    │ PlasmodesmaFilter                │ WebSocket Filter型           ││          │ Alginv8I58akMMnCA7T0A            │ 载荷组件(随机类名变种)        ││          │ Eutropic                         │ 载荷组件                     ││          │ Poliorcetic                      │ 载荷组件                     ││          │ LithoprintxCVIGnPE53kMja9q       │ 载荷组件                     ││          │ Zygosporangium                   │ 载荷组件                     │├──────────┼──────────────────────────────────┼──────────────────────────────┤│ 代理隧道马│ Prepupa                          │ Runnable代理线程             │├──────────┼──────────────────────────────────┼──────────────────────────────┤│ 通用特征  │ 类名为生僻英文词+Filter/Servlet   │ 动态注册型                   ││          │ /Listener/Runnable               │                              ││          │ 无包名或包名异常的Filter/Servlet  │                              ││          │ $$Lambda$ 结尾的Filter            │ Lambda表达式伪装             ││          │ -javaagent:指向非APM的jar         │ Agent型                      │└──────────┴──────────────────────────────────┴──────────────────────────────┘
注入器磁盘特征关键词:  defineClass / Unsafe / Base64.decode / Runtime.getRuntime / ProcessBuilder  / ScriptEngine / ClassLoader

================================================================================二、常见框架Filter/Listener白名单（防误判）================================================================================
以下为常见框架正常注册的Filter/Servlet，排查时可跳过:
  Spring框架:  CharacterEncodingFilter, hiddenHttpMethodFilter,              httpPutFormContentFilter, requestContextFilter,              DelegatingFilterProxy, FilterChainProxy,              SpringSecurityFilterChain, MultipartFilter
  Shiro:      SpringShiroFilter, InvalidRequestFilter
  Druid:      DruidWebStatFilter, DruidStatViewServlet
  Tomcat:     CorsFilter, CsrfPreventionFilter, ExpiresFilter,              RemoteAddrFilter, RemoteHostFilter, RemoteIpFilter,              SetCharacterEncodingFilter, WebdavFixFilter
  Resin:      ServletConfigImpl, WebApp, ConfigContext
  其他:       CasFilter, XssFilter, LogFilter, UrlRewriteFilter
判断原则: 堆栈顶部全是框架自身类(catalina/spring/caucho/shiro) → 大概率误报         堆栈顶部出现生僻词+Filter/Servlet/Listener → 真内存马

================================================================================三、分阶段排查命令================================================================================
--------------------------------------------------------------------------------第一阶段: 确认Java进程和基本信息--------------------------------------------------------------------------------
[1][必] 查看Java进程信息    ps aux | grep java
    >> 看什么: 找到目标Java进程，记录PID    >> 重点: 启动命令中是否包含 -javaagent、-Xbootclasspath 等异常参数    >> 说明:       -javaagent:xxx.jar → Agent型内存马，可修改任意类字节码       -Xbootclasspath   → 替换引导类加载器路径，植入底层恶意代码
[2][必] 查看Java进程详细启动参数    cat /proc/$(pgrep -f java | head -1)/cmdline | tr '\0' '\n'
    >> 看什么: 逐行显示JVM启动参数，检查是否有 -javaagent 或可疑 -classpath    >> 如果看到 -javaagent:xxx.jar，记录该jar路径，可能是恶意Agent
[3][荐] 查看Java进程环境变量    cat /proc/$(pgrep -f java | head -1)/environ | tr '\0' '\n' | grep -i "java\|agent\|tool\|opts"
    >> 看什么: 检查 JAVA_TOOL_OPTIONS、JAVA_OPTS 等是否被注入恶意参数    >> 示例: JAVA_TOOL_OPTIONS=-javaagent:/tmp/evil.jar 即为恶意注入
[4][荐] 确认应用工作目录    ls -la /proc/$(pgrep -f java | head -1)/cwd
    >> 看什么: 查看Java进程工作目录（如 /opt/tomcat），确定应用安装路径
[5][选] 查看进程打开的文件描述符    ls -la /proc/$(pgrep -f java | head -1)/fd/ | head -50
    >> 看什么: 可能发现可疑的jar/class文件，或被删除但仍被进程占用的文件    >> 标记: 显示 (deleted) 的文件表示已被删但进程仍持有句柄
--------------------------------------------------------------------------------第二阶段: 查找磁盘注入器 (最关键!)--------------------------------------------------------------------------------
【说明】内存马驻留JVM内存中，重启即消失。但多数内存马借助磁盘上的JSP注入器实现持久化——应用重启后JSP被访问即重新加载恶意类。找到注入器是切断重复感染的关键。
[6][必] 定位应用部署路径    find / -name "webapps" -type d 2>/dev/null    find / -name "catalina.sh" 2>/dev/null    find / -name "application.properties" -o -name "application.yml" 2>/dev/null    find / -name "resin.xml" 2>/dev/null
    >> 看什么: 确定 Tomcat webapps / Spring Boot 配置 / Resin 配置路径    >> 说明: 后续搜索建议限定在此路径下，全盘搜索太慢
    # 设定搜索根目录变量（后续命令可用）    APP_ROOT=/opt/tomcat    # ← 替换为实际发现的路径
[7][必] 查找近期修改的JSP文件 (30天)    find ${APP_ROOT:-/} -name "*.jsp" -mtime -30 -ls 2>/dev/null
    >> 看什么: 30天内修改过的JSP，重点关注非业务目录下的JSP    >> 重点: 文件名随机(如 aB3x.jsp)、路径异常、修改时间与入侵时间吻合
[8][必] 查找近期新增的JSP文件 (7天，范围更小)    find ${APP_ROOT:-/} -name "*.jsp" -mtime -7 -ls 2>/dev/null
    >> 看什么: 7天内新增的JSP，更容易定位
[9][必] 查找包含危险代码的JSP文件    grep -rl "Runtime.getRuntime\|ProcessBuilder\|defineClass\|ClassLoader\|ScriptEngine" \        ${APP_ROOT:-/} --include="*.jsp" 2>/dev/null
    >> 看什么: 包含命令执行/类加载等危险函数的JSP，极大概率是注入器    >> 注意: 全盘搜索较慢，建议用 APP_ROOT 限定范围
[10][荐] 查找Base64解码+类加载的JSP (内存马注入器典型特征)     grep -rl "Base64\|decodeBuffer\|defineClass\|Unsafe" \         ${APP_ROOT:-/} --include="*.jsp" 2>/dev/null
     >> 看什么: Base64解码后 defineClass 是内存马注入的标准手法
[11][荐] 查找近期修改的class文件 (非jar包内的)     find ${APP_ROOT:-/} -name "*.class" -mtime -30 \         -not -path "*/lib/*" -not -path "*/WEB-INF/lib/*" -ls 2>/dev/null
     >> 看什么: 正常类都在 lib/*.jar 或 WEB-INF/lib/*.jar 中，...