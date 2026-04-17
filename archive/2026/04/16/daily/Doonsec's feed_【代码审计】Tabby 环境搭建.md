---
title: 【代码审计】Tabby 环境搭建
url: https://mp.weixin.qq.com/s/EWqCiEg3TQp609gOlTR_gQ
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:48:24.452656
---

# 【代码审计】Tabby 环境搭建

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ocg1gpicEs1v0UsEu6UT1ZnAbzPT2KMqibyIAb4iaV8nke9nerEBeWU8nODSjlpVYn7fKA1F73OglMpRUhX5b8bgE4rNaOm5icoClbujt3OEYEw/0?wx_fmt=jpeg)

# 【代码审计】Tabby 环境搭建

原创

十月的进阶之路
十月的进阶之路

十月的进阶之路

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 你的代审`baby`

### 目录

一、环境要求

二、安装 `tabby` 核心

三、安装 `tabby-vul-finder`

四、配置 `tabby` 项目结构

五、配置修改

六、配置`neo4j` 数据库

七、安装 `neo4j` 插件

八、初始化 `neo4j` 索引

九、验证插件安装

十、测试运行

注意事项

### 一、环境要求

* Java 17：需配置 `Java 17` 环境。
* Neo4j 图数据库：推荐使用**Neo4j Desktop**（需注意版本兼容性，如`tabby`需要搭配`5.26.1`）。

### 二、安装 Tabby 核心

1. 克隆项目：

   ```
   git clone https://github.com/wh1t3p1g/tabby.git
   ```
2. 编译打包： 在项目根目录执行：

   ```
   mvn clean package -DskipTests "-Dfile.encoding=UTF-8"
   ```
3. 准备核心 JAR： 将 `target` 目录下生成的 `tabby.jar` 复制到项目根目录。

### 三、安装 tabby-vul-finder

1. 克隆项目：

   ```
   git clone https://github.com/wh1t3p1g/tabby-vul-finder.git
   ```
2. 编译打包： 进入项目目录执行 `mvn clean package -DskipTests`，生成 `tabby-vul-finder.jar`。
3. 复制规则文件： 将 `tabby-vul-finder/rules/cyphers.yml` 复制到Tabby 项目的`rules`文件夹中。

### 四、配置 Tabby 项目结构

确保`tabby`项目目录包含以下结构：

```
tabby/
├── cases/          # 放置待分析的 JAR 包（如 commons-collections-3.2.1.jar）
├── config/         # 配置文件目录
│   ├── db.properties       # 数据库连接配置
│   └── settings.properties # 分析任务配置
├── output/         # 生成的 CSV 文件输出目录
├── rules/          # 规则文件（含 sinks.json、cyphers.yml 等）
├── libs/           # 目标项目依赖 jar 包
├── temp/           # 临时文件目录
├── tabby.jar       # 核心 JAR
└── tabby-vul-finder.jar # 导入/查询 JAR
```

#### 关键配置文件

1. config/settings.properties： 配置待分析项目、`JRE`路径、分析模式等。
2. config/db.properties： 配置`Neo4j`连接信息：

   ```
   # 路径适配配置
   tabby.cache.isDockerImportPath            = false

   # Neo4j数据库连接配置
   tabby.neo4j.username                      = neo4j
   tabby.neo4j.password                      = 你的Neo4j数据库密码
   tabby.neo4j.url                           = bolt://127.0.0.1:7687
   ```

### 五、配置修改

将`java_home`修改为`Windows`本地有效的`JDK`路径。

```
# 目标项目java-sec-code为JDK8编译，推荐配置本地JDK8路径
tabby.build.javaHome = D:/Java/jdk1.8.0_202
# 也可使用Windows双反斜杠写法
# tabby.build.javaHome = D:\\Java\\jdk1.8.0_202
```

`tabby.build.isJDKProcess = false`，关闭了对`JDK`内置类的分析，但是如果你打开就会导致`OOM`。`tabby`的内存由`JVM`控制，核心通过两个参数调整：

* Xms：`JVM`初始堆内存，建议和最大值设为一致，避免运行时动态扩容缩容带来的性能损耗与`GC`压力
* Xmx：`JVM`最大堆内存，决定了`tabby`能使用的内存上限，也是解决`OOM`的核心参数

```
# 示例1：16G内存机器，分配8G最大堆内存（推荐）
java -Xms8G -Xmx8G -jar tabby.jar

# 示例2：32G内存机器，分配16G最大堆内存（大项目/全量依赖分析）
java -Xms16G -Xmx16G -jar tabby.jar

# 示例3：8G内存机器，分配4G最大堆内存（低配环境）
java -Xms4G -Xmx4G -jar tabby.jar
```

补充说明：此处`javaHome`是待分析目标项目的编译`JDK`版本，而`tabby`本身运行需要 `Java17`环境，需确保执行`java -jar`命令时，系统默认`Java`版本为`Java17`。配置了`tabby.build.target = cases/java-sec-code-1.0.0.jar`，必须确保`cases`目录下确实存在`java-sec-code-1.0.0.jar`文件，这个`jar`文件就是你的审计目标，否则`build`阶段会直接因找不到目标文件失败。

### 六、配置 Neo4j 数据库

1. **下载并安装 Neo4j Desktop**：

* 官网下载最新版即可，若桌面版无法打开，可先**断网**再启动。
* `neo4j desktop`无法通过`ui`界面安装程序到指定目录，参考如下命令`.\neo4j-desktop-2.1.3-x64.exe /S /D=D:\code-audit\neo4j\app`将程序安装到指定目录。
* 数据库实例推荐版本：`5.26.1`（需代理才会出现下载版本列表，`tabby`推荐`5.26.1`），创建后开始自动下载数据库，这个过程需要点时间。

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1txLmXxK0AptCgso4icibGR5zQzaiaYFNNEUt7hbCIJ7hZGHLhyJxDb34PeDpoWm2jkaUbInonpIYtiba5KQydkruvPKlLd69bEnqc/640?wx_fmt=png&from=appmsg)

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1voOTAw6WPyMEVc5neCeI5F9mxicpGMAqc6OynZgaDdFuW0m0YnOSsG2q6hvew78YOnP8P9BQmxeSt5R7efDVCFAh3OeJwTTrTU/640?wx_fmt=png&from=appmsg)

2. **修改 Neo4j 配置**： 打开`Neo4j Desktop`，进入数据库管理界面，修改 `neo4j.conf`。我猜测如果您整个过程中将会碰到的最大的麻烦一定是将`tabby`的数据导入`neo4j`，因此请导入数据之前修改`neo4j.conf`配置文件，这相当重要，参考如下的内容，您可以将您的计算机配置给`ai`以获取一份量身定制的配置。

   ```
   # 注释掉 import 目录限制，允许从任意位置加载 CSV
   #server.directories.import=import

   # 允许 APOC 和 Tabby 扩展
   dbms.security.procedures.unrestricted=jwt.security.*,apoc.*,tabby.*

   #其他配置参考如下
   server.default_listen_address=0.0.0.0

   server.bolt.enabled=true
   server.bolt.listen_address=0.0.0.0:7687
   server.bolt.tls_level=DISABLED

   server.http.enabled=true
   server.http.listen_address=0.0.0.0:7474

   server.memory.heap.initial_size=6G
   server.memory.heap.max_size=6G
   server.memory.pagecache.size=4G

   db.memory.transaction.max=256M
   db.memory.transaction.total.max=1G

   db.transaction.timeout=30m
   server.config.strict_validation.enabled=true
   ```
3. **创建 `apoc.conf`**： 在`Neo4j`配置目录新建 `apoc.conf`：

   ```
   apoc.import.file.enabled=true
   apoc.import.file.use_neo4j_config=false
   ```

### 配置文件目录如下。

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1tVU3tcb6MgAQ0amahxKhtGR0Qgb1qqYR4ibZwWbaJjOIcZj7JVV9dtkhx1D7yezKgm6fefyiaxMVGkO7uN2S9Q9hHka6SOSjx3w/640?wx_fmt=png&from=appmsg)

### 七、安装 Neo4j 插件

将以下插件`JAR`放入`Neo4j` 的 `plugins` 目录：

1. **APOC 插件**：

* apoc-core：`https://github.com/neo4j/apoc`
* apoc-extended：`https://github.com/neo4j-contrib/neo4j-apoc-procedures`

* Neo4j v5 需分为 `apoc-core` 和 `apoc-extended`：
* **版本对应**：`APOC`插件版本前两位需与`Neo4j`版本一致（如`Neo4j 5.26.x`对应`APOC 5.26.x`）。

2. **tabby-path-finder 插件**：

* 克隆项目：`https://github.com/wh1t3p1g/tabby-path-finder`
* 编译打包：`mvn clean package -DskipTests`，生成`JAR`后放入 `plugins`目录。（注意: 不是`tabby-vul-finder`插件，别搞混了）

最终您的插件目录包含如下内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1vovwkZLOO4WsXT95sPyiaN7RSTfmvlSLk9iaA7NWNJcsfYFiakb5ianA54LXicOgbS8Q90ib1m1jopBriahmia0r0liaY6VmdicR5bhrX2Y/640?wx_fmt=png&from=appmsg)

### 八、初始化 Neo4j 索引

启动`Neo4j`数据库，打开`Neo4j Browser`，执行以下`Cypher`语句创建索引（通过浏览器访问`http://127.0.0.1:7474/`，并键入您的账号密码）：

```
CREATE CONSTRAINT c1 IF NOT EXISTS FOR (c:Class) REQUIRE c.ID IS UNIQUE;
CREATE CONSTRAINT c2 IF NOT EXISTS FOR (c:Class) REQUIRE c.NAME IS UNIQUE;
CREATE CONSTRAINT c3 IF NOT EXISTS FOR (m:Method) REQUIRE m.ID IS UNIQUE;
CREATE CONSTRAINT c4 IF NOT EXISTS FOR (m:Method) REQUIRE m.SIGNATURE IS UNIQUE;
CREATE INDEX index1 IF NOT EXISTS FOR (m:Method) ON (m.NAME);
CREATE INDEX index2 IF NOT EXISTS FOR (m:Method) ON (m.CLASSNAME);
CREATE INDEX index3 IF NOT EXISTS FOR (m:Method) ON (m.NAME, m.CLASSNAME);
CREATE INDEX index4 IF NOT EXISTS FOR (m:Method) ON (m.NAME, m.NAME0);
CREATE INDEX index5 IF NOT EXISTS FOR (m:Method) ON (m.SIGNATURE);
CREATE INDEX index6 IF NOT EXISTS FOR (m:Method) ON (m.NAME0);
CREATE INDEX index7 IF NOT EXISTS FOR (m:Method) ON (m.NAME0, m.CLASSNAME);
```

### 九、验证插件安装

在`Neo4j Browser`中执行：

```
CALL apoc.help('all');  // 验证 APOC
CALL tabby.help('tabby'); // 验证 Tabby
```

若成功返回结果，说明插件安装成功。

### 十、测试运行

1. 生成图数据（Build）： 在`Tabby`项目根目录执行如下命令。

   ```
   java -Xmx16g -jar tabby.jar
   ```

   成功后会在 `output` 目录生成`CSV`文件。
2. **导入数据到 Neo4j（Load）**：

   ```
   java -Xms12G -Xmx12G -jar tabby-vul-finder.jar --load ./output/dev
   ```
3. **查询漏洞链**： 在`Neo4j Browser`中执行`Cypher`查询，验证是否能返回结果。

### 注意事项

* **Neo4j 版本**：需与`APOC`、`Tabby`插件版本严格匹配。
* **内存配置**：`Neo4j`和`Tabby`的内存分配需足够大，避免`OOM`。
* **网络问题**：`Neo4j Desktop`下载版本需挂代理。

完成以上步骤后，即可开始使用`Tabby`进行代码审计和漏洞链分析。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GFPic2iaAJQw9icmAfmmEej0faflh5tB82cUK35MTVuw42wOQtcxfYUV0AXBEgJCSan9OhFhdMXuUpjtyUB8cxwVA/0?wx_fmt=png)

十月的进阶之路

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GFPic2iaAJQw9icmAfmmEej0faflh5tB82cUK35MTVuw42wOQtcxfYUV0AXBEgJCSan9OhFhdMXuUpjtyUB8cxwVA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过