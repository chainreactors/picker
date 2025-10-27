---
title: OpenRASP浅析
url: https://buaq.net/go-134340.html
source: unSafe.sh - 不安全
date: 2022-11-06
fetch_date: 2025-10-03T21:49:33.923936
---

# OpenRASP浅析

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

OpenRASP浅析

最近在学习RASP相关内容，正好OpenRASP开源，大概分析了一下流程。参考了网上师傅们的分析加上自己的理解就有了这篇文章。如有错误或不足，还望指正。RASP技术
*2022-11-5 13:27:0
Author: [xz.aliyun.com(查看原文)](/jump-134340.htm)
阅读量:31
收藏*

---

最近在学习RASP相关内容，正好OpenRASP开源，大概分析了一下流程。参考了网上师傅们的分析加上自己的理解就有了这篇文章。如有错误或不足，还望指正。

## RASP技术

RASP，全称“Runtime application self-protection”，运行时应用程序自我保护技术。它通过JavaAgent将代码注入到某些方法中，与应用程序融为一体，使应用程序具备自我防护能力，当应用程序遭受到实际攻击伤害时，能实时检测和阻断安全攻击，而不需要进行人工干预。

### RASP与WAF的比较

WAF拦截原始http数据包，然后使用规则对数据包进行匹配扫描，如果不满足预设的所有规则，则视为安全，可通过WAF。这样就会造成规则缺失，放行危险行为；同时WAF只是对程序外层进行防护，当数据进入程序后，无法获取后续的行为。

### DAST、SAST和IAST

DAST：动态应用程序安全测试（Dynamic Application Security Testing）技术在测试或运行阶段分析应用程序的动态运行状态。它模拟黑客行为对应用程序进行动态攻击，分析应用程序的反应，从而确定该Web应用是否易受攻击。
SAST：静态应用程序安全测试（Static Application Security Testing）技术通常在编码阶段分析应用程序的源代码或二进制文件的语法、结构、过程、接口等来发现程序代码存在的安全漏洞。
IAST：交互式应用程序安全测试（Interactive Application Security Testing）是2012年Gartner公司提出的一种新的应用程序安全测试方案，通过代理、VPN或者在服务端部署Agent程序，收集、监控Web应用程序运行时函数执行、数据传输，并与扫描器端进行实时交互，高效、准确的识别安全缺陷及漏洞，同时可准确确定漏洞所在的代码文件、行数、函数及参数。IAST相当于是DAST和SAST结合的一种互相关联运行时安全检测技术。

### IAST与RASP

正如[Thoughtworks官网](https://www.thoughtworks.com/zh-cn/insights/decoder/i/iast-rasp)所描述的那样：
IAST：交互式应用程序安全测试。监控应用程序在运行时的安全漏洞——测试时间。
RASP：运行时应用程序自我保护。监控应用程序，以检测其运行时的攻击——生产时间。
IAST 和 RASP 是应用程序运行时寻找问题的安全工具。对于 IAST，作为测试过程的一部分，扫描漏洞。，RAST 检测生产环境中的攻击。

## OpenRASP

OpenRASP是百度在2017年针对RASP概念推出的一款开源免费的自适应安全产品，[官网](https://rasp.baidu.com/)。
这个项目使用v8引擎载入js并实现热加载，通过编写js规则对攻击进行检测，这一点还是比较吸引人的。
另一个引入JS的原因是OpenRASP会支持PHP、DotNet、NodeJS、Python、Ruby等多种开发语言，为了避免在不同平台上重新实现检测逻辑，所以引入了插件系统，选择JS作为插件开发语言。

这里我主要分析了对于Java版本的系统架构与具体的执行流程。

java 版本使用 javaagent 机制来实现。在服务器启动时，可动态的修改Java字节码，对敏感操作的函数进行hook，比如:

* 数据库操作
* 文件读取、写入操作
* 命令执行
* ...

当服务器发生攻击，就会触发这些Hook点，此时RASP agent就可以获取到函数的参数，比如要读取的文件名、要执行的命令等等。

### 系统架构 - Java 版本

Java 版本的系统架构可以参考[官方手册](https://rasp.baidu.com/doc/hacking/architect/java.html)

### 启动流程

这部分的源码在`openrasp/agent/java/boot`

1. OpenRASP使用了 `on load` 的方式进行代理。启动时首先会进入 `com.baidu.openrasp.Agent` 的 `premain` 函数进行初始化操作（`init()`），该函数会在 main 函数之前预先执行。

```
//com.baidu.openrasp.Agent
public static void premain(String agentArg, Instrumentation inst) {
    init(START_MODE_NORMAL, START_ACTION_INSTALL, inst);
}
public static synchronized void init(String mode, String action, Instrumentation inst) {
    try {
        JarFileHelper.addJarToBootstrap(inst);
        //读取MANIFEST.MF相关信息
        readVersion();
        ModuleLoader.load(mode, action, inst);
    } catch (Throwable e) {
        System.err.println("[OpenRASP] Failed to initialize, will continue without security protection.");
        e.printStackTrace();
    }
}
```

1. 在`init()`方法中首先利用`inst.appendToBootstrapClassLoaderSearch(new JarFile(localJarPath))`将自身添加到 `BootstrapClassLoader` 的ClassPath下。
   这是因为双亲委派机制的存在，类加载器在加载类时无法往下委派加载。当被hook的类需要调用漏洞检测方法的代码时，如果该hook类为`BootstrapClassLoader`加载的，则无法从该类调用非 `BootstrapClassLoader` 加载的类中的代码。要解决这个问题，就应该想办法把这种类通过BootstrapClassLoader进行加载。OpenRASP中通过调用`appendToBootstrapClassLoaderSearch`方法，可以把一个jar包放到Bootstrap ClassLoader的搜索路径。这样的话，当Bootstrap ClassLoader检查自身加载过的类，发现没有找到目标类时，会在指定的jar文件中搜索。官方文档也做了如下解释：
   当去 hook 像 `java.io.File` 这样由 `BootstrapClassLoader` 加载的类的时候，无法从该类调用非 `BootstrapClassLoader` 加载的类中的接口，所以 `agent.jar` 会先将自己添加到 `BootstrapClassLoader` 的ClassPath下，这样 hook 由 `BootstrapClassLoader` 加载的类的时候就能够成功调用到 `agent.jar` 中的检测入口

```
//com.baidu.openrasp.JarFileHelper
public static void addJarToBootstrap(Instrumentation inst) throws IOException {
    String localJarPath = getLocalJarPath();
    inst.appendToBootstrapClassLoaderSearch(new JarFile(localJarPath));
}
```

1. 加载和初始化引擎模块(rasp-engine.jar)
   ModuleLoader类的静态方法将moduleClassLoader设置为ExtClassLoader，在ModuleLoader构造函数中实例化ModuleContainer，并调用其start()方法。
   在ModuleLoader构造函数中还会执行`setStartupOptionForJboss();`这里按照源码的解释应该是判断当前进程是否为jboss7 版本，并设置相关属性和预加载包。

```
//com.baidu.openrasp.ModuleLoader
static {
    // juli
    try {
        Class clazz = Class.forName("java.nio.file.FileSystems");
        clazz.getMethod("getDefault", new Class[0]).invoke(null);
    } catch (Throwable t) {
        // ignore
    }
    Class clazz = ModuleLoader.class;
    // path值示例：　file:/opt/apache-tomcat-xxx/rasp/rasp.jar!/com/fuxi/javaagent/Agent.class
    String path = clazz.getResource("/" + clazz.getName().replace(".", "/") + ".class").getPath();
    if (path.startsWith("file:")) {
        path = path.substring(5);
    }
    if (path.contains("!")) {
        path = path.substring(0, path.indexOf("!"));
    }
    try {
        baseDirectory = URLDecoder.decode(new File(path).getParent(), "UTF-8");
    } catch (UnsupportedEncodingException e) {
        baseDirectory = new File(path).getParent();
    }
    ClassLoader systemClassLoader = ClassLoader.getSystemClassLoader();
    while (systemClassLoader.getParent() != null
            && !systemClassLoader.getClass().getName().equals("sun.misc.Launcher$ExtClassLoader")) {
        systemClassLoader = systemClassLoader.getParent();
    }
    moduleClassLoader = systemClassLoader;
}

/**
 * 构造所有模块
 *
 * @param mode 启动模式
 * @param inst {@link java.lang.instrument.Instrumentation}
 */
private ModuleLoader(String mode, Instrumentation inst) throws Throwable {
    if (Module.START_MODE_NORMAL == mode) {
        setStartupOptionForJboss();
    }
    engineContainer = new ModuleContainer(ENGINE_JAR);
    engineContainer.start(mode, inst);
}

/**
 * 加载所有 RASP 模块
 *
 * @param mode 启动模式
 * @param inst {@link java.lang.instrument.Instrumentation}
 */
public static synchronized void load(String mode, String action, Instrumentation inst) throws Throwable {
    if (Module.START_ACTION_INSTALL.equals(action)) {
        if (instance == null) {
            try {
                instxance = new ModuleLoader(mode, inst);
            } catch (Throwable t) {
                instance = null;
                throw t;
            }
        } else {
            System.out.println("[OpenRASP] The OpenRASP has bean initialized and cannot be initialized again");
        }
    } else if (Module.START_ACTION_UNINSTALL.equals(action)) {
        release(mode);
    } else {
        throw new IllegalStateException("[OpenRASP] Can not support the action: " + action);
    }
}
```

在ModuleContainer构造方法中，获取了rasp-engine.jar中MANIFEST.MF文件的Rasp-Module-Name、Rasp-Module-Class字段。然后使用ExtClassLoader加载Rasp-Module-Class，即`com.baidu.openrasp.EngineBoot`，并将其实例化，赋值给module变量，然后ModuleLoader构造函数会调用`new ModuleContainer(ENGINE_JAR).start()`,继而调用`module.start(mode, inst);`即`com.baidu.openrasp.EngineBoot#start()`，启动引擎。

```
private Module module;
private String moduleName;
//jarName = rasp-engine.jar
public ModuleContainer(String jarName) throws Throwable {
    try {
        File originFile = new File(baseDirectory + File.separator + jarName);
        JarFile jarFile = new JarFile(originFile);
        Attributes attributes = jarFile.getManifest().getMainAttributes();
        jarFile.close();
        this.moduleName = attributes.getValue("Rasp-Module-Name");
        String moduleEnterClassName = attributes.getValue("Rasp-Module-Class");
        if (moduleName != null && moduleEnterClassName != null
                && !moduleName.equals("") && !moduleEnterClassName.equals("")) {
            Class moduleClass;
            if (ClassLoader.getSystemClassLoader() instanceof URLClassLoader) {
                Method method = Class.forName("java.net.URLClassLoader").getDeclaredMethod("addURL", URL.class);
                method.setAccessible(true);
                method.invoke(moduleClassLoader, originFile.toURI().toURL());
                method.invoke(ClassLoader.getSystemClassLoader(), originFile.toURI().toURL());
                moduleClass = moduleClassLoader.loadClass(moduleEnterClassName...