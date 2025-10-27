---
title: 提取Maven项目SBOM的坑点
url: https://mp.weixin.qq.com/s?__biz=MzIzMTc1MjExOQ==&mid=2247508088&idx=1&sn=cf1744769d56c6f2c496e7392b634df4&chksm=e89d88a0dfea01b609dffb553b3f0ac6008b85a2902c9b80909cd80590e6fa207940a341fefa&scene=58&subscene=0#rd
source: ChaMd5安全团队
date: 2022-12-29
fetch_date: 2025-10-04T02:40:28.665873
---

# 提取Maven项目SBOM的坑点

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PUubqXlrzBQsw6cdHelCuUpyvBUOLPiaxaMajHNKe9kbjiaudKtzk9WibroeibrSmdLsZrXYXEAlvXhRFIDctAgX3Q/0?wx_fmt=jpeg)

# 提取Maven项目SBOM的坑点

原创

retanoj

ChaMd5安全团队

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQsw6cdHelCuUpyvBUOLPiaxcepiavqQicbL1GicHxXiauGnIaQDnpysSQIRfRyWOMicMaSDDedX1fUFFrg/640?wx_fmt=png)

在前些年工作中，我针对Maven、Composer、Pip等主流构建工具/包管理工具写过提取SBOM的插件。如今看来，面对当下的SCA安全工作，之前写的小工具是过于肤浅了。

近期测试了国内外几家厂商的SCA软件产品，先不论支持类型、漏洞库质量以及交互体验，仅提取SBOM一项的测试结果就千差万别。由此感慨因构建工具冗杂、概念复杂、标准不一而导致如此结果。

以下内容是关于在使用Maven过程中遇到的关键概念，以及测试SCA产品过程中遇到的部分坑点。

注意，本文仅讨论使用单一Maven作为依赖管理工具的Java源码项目。混合其他构建工具，以拷贝源码方式引入依赖，在运行时classpath引入依赖等情况不在本次讨论范围。

## 概念

#### Maven

对于Javaer而言，Maven是一个用于构建和管理Java项目的工具。Maven多以运行插件的方式来达成执行目标。 常用的插件有maven-compiler-plugin、maven-clean-plugin、maven-dependency-plugin等等。

#### POM

项目对象模型。它是一个Maven项目的XML表示，默认保存在`pom.xml`文件中。 Maven工具内置了一个POM文件，也叫Super POM。默认情况下，所有的POM均继承自Super POM。

#### Dependency

依赖项声明了当前项目所依赖的其他项目。

在Maven制品仓库中，可以用{groupId} : {artifactId} : {version} 三元组迅速定位一个制品（依赖项），Maven称其为“坐标”。

而在一个Maven项目中，唯一定位一个依赖所涉及的元素有如下这些： groupId, artifactId, type, version, scope, classifier, optional, exclusion

#### type

依赖的类型。常见的依赖类型是`jar`包与`pom`物料清单，此外还有`war`、`ear`、`rar`等等。

#### scope

Maven假定在编译、测试和运行过程中会使用三套不同的classpath，scope则用于控制依赖项是否出现在相应的classpath中，下表展示了这种关系。scope有6个取值：compile、test、provided、runtime、system、import。

| scope取值 | 编译classpath | 测试classpath | 运行时classpath | 打包 |
| --- | --- | --- | --- | --- |
| compile(默认) | y | y | y | y |
| test |  | y |  |  |
| provided | y | y |  |  |
| runtime |  | y | y | y |
| system | y | y |  |  |

`import`用于从其他的POM项目中导入依赖配置。

举例，`provided` scope暗示了所标记依赖项会在运行时classpath中存在，所以在编译和测试过程中会将它加入对应的classpath，而在最终打包时它被排除。`system`与`provided`十分类似。

同时，scope也影响引入依赖的传递性，见下表。

|  | compile | test | provided | runtime |
| --- | --- | --- | --- | --- |
| compile | compile | - | - | runtime |
| test | test | - | - | test |
| provided | provided | - | provided | provided |
| runtime | runtime | - | - | runtime |

以A依赖B，B依赖C举例，此时A对C为间接依赖。第一纵列表示A对B的scope，第一横行表示B对C的scope。表中内容则回答了A对C的scope。

#### optional

可选依赖。表示当前依赖项不作为间接依赖存在。

#### exclusion

排除依赖。表示不会由当前依赖项间接引入某些依赖项。

#### 依赖调节

依赖调节是Maven在遇到依赖冲突时的解决算法。此部分比较复杂，暂不展开，后文会略微提及。

## 坑点

### 1、同名artifactId

有些软件将{artifactId}展示为组件名称，有些将{artifactId}与{version}结合展示，少部分会带上{groupId}加以区分，通常这没什么问题。 在测试过程中发现，对于artifactId相同且version也相同的依赖组件，有些软件SBOM清单内仅会展示存在一个依赖这样的错误结果。绝大部分软件会展示看上去完全相同的两条记录，点进详情才能发现差异。

**测试样例：**

```
<dependency>
     <groupId>findbugs</groupId>
     <artifactId>annotations</artifactId>
     <version>1.0.0</version>
</dependency>

<dependency>
     <groupId>org.neo4j.gds</groupId>
     <artifactId>annotations</artifactId>
     <version>1.0.0</version>
</dependency>
```

**扩展思考：**

业务线在打jar包的时候，会收集依赖jar包集中放在一个文件夹里，并保持默认命名规则{artifactId}-{version}.jar。在这种打包规则下，对于上面的测试样例会有何表现？

### 2、版本号

比起语义化版本号，Maven在版本号控制上已经收敛太多。使用最广泛的是`LATEST`与`RELEASE`两个特殊版本号。Maven官方称

> For the sake of reproducible builds, Maven 3.x no longer supports usage of these metaversions in the POM.

然而至今仍能正常工作。

有些软件使用depgraph-maven-plugin来做依赖解析。depgraph-maven-plugin的`graph` Mojo使用`requiresDependencyCollection`注解，这代表该Mojo执行前需要Maven先执行依赖收集工作。然而，`requiresDependencyCollection`不会将`LATEST`与`RELEASE`还原为指定版本号。

Maven默认使用的`2.8.0`版本maven-dependency-plugin插件，其`list`和`tree` Mojo均使用`requiresDependencyResolution`注解，这会在Mojo执行前让Maven先完成依赖解析工作，可还原特殊版本号。但是，比起`requiresDependencyCollection`，`requiresDependencyResolution`会将依赖jar包下载回来，增加了更多的网络负担与计算工作。 同时，maven-dependency-plugin在新版上（如3.4.0），`tree` Mojo也更换为`requiresDependencyCollection`注解。

特殊版本号还包括使用`[]/()`的范围版本号（例如`[1.0.0, 2.0.0)`）。对于这类版本号，`requiresDependencyCollection`与`requiresDependencyResolution`注解的Mojo均能正确解析。

提及版本号问题，是因为在某些场景下无法依靠Maven工具进行依赖解析，只能退而求其次，对`pom.xml`进行文本解析后再深入处理。然而某些软件自研的依赖提取算法与Maven相关算法存在差异，导致结果并不准确。

**测试样例：**

```
<dependency>
     <groupId>org.jetbrains</groupId>
     <artifactId>annotations</artifactId>
     <version>LATEST</version>
 </dependency>
```

行文时，该依赖项LATEST的版本为23.0.0

### 3、默认scope

在进行依赖解析生成SBOM时，有些软件默认选取的scope列表是`compile, runtime`，而有些则是`compile, runtime, test`。我想，关于scope取值导致的SBOM差异问题是缺乏标准的典型问题。

以`provided` scope的依赖举例，从制品角度来看，`provided`依赖并未出现在打包制品中，因此的确不应出现在制品SBOM中。然而从实际情况上看，`provivded`语义暗示运行时环境会提供所以打包才不要。那在SCA安全工作上，是否认为当前项目使用了这个依赖呢？

对于获取依赖清单工作，从源码解析、在运行时扫描等多手段并存当然是一种好办法。对于SCA软件，好一些的会提供`scope`选项，差一些的就写个定值不让用户感知。无感知不代表可以被忽视，希望后续各家能遵守同一份标准吧。

### 4、解析层数

在间接依赖层数过多时，有些软件生成的SBOM会很夸张的丢依赖。POM解析依赖本应遵循应解尽解，然而在实际测试过程中还是花样百出。 有不提供解析层数设置项的，有提供设置项但最大值过小的，也有提供设置项且能设置很大值但最终结果设置无效的。

真实场景中我遇到了引入9层间接依赖的案例，且均为`compile` scope的依赖项。下面给出一个层数较多的案例吧：

**测试样例：**

```
<dependency>
    <groupId>org.geotools</groupId>
    <artifactId>gt-geojson</artifactId>
    <version>24.2</version>
</dependency>
```

其中一条引入链条：

```
[
     "org.geotools:gt-geojson:jar:24.2",
     "org.geotools:gt-main:jar:24.2",
     "org.geotools:gt-referencing:jar:24.2",
     "org.geotools:gt-metadata:jar:24.2",
     "org.geotools:gt-opengis:jar:24.2",
     "systems.uom:systems-common:jar:2.0.1",
     "tech.units:indriya:jar:2.0.2",
     "javax.inject:javax.inject:jar:1"
]
```

### 5、按操作系统区分

某些依赖会根据不同的操作系统版本来引入不同的依赖项目，该问题常被忽视而导致分析判断错误。例如，本地开发环境是Mac OS，SCA软件运行环境是Linux，而线上环境可能会是Windows。下面给出测试样例。

**测试样例：**

```
<dependency>
     <groupId>guru.nidi</groupId>
     <artifactId>graphviz-java</artifactId>
     <version>0.18.1</version>
</dependency>
```

它引入的 guru.nidi.com.eclipsesource.j2v8:{artifactId} 依赖会根据操作系统版本而变化。

### 6、插件行为不一致

这个问题源于一次应急响应，并不算是SCA软件的问题。如果非要归属，应当说是由于依赖提取算法不一致而导致的差异。然而，在Maven的生态环境下各种插件实现依赖解析算法并不完全一致，因此该问题可能会一直存在。下面我来描述该问题具体情况。

有两个工程项目，一个叫`Parent`，是个BOM清单，用于管理依赖版本。一个叫`Child`，是个实际业务项目，且业务方配置了maven-assembly-plugin插件用于收集依赖并打包，相关文件如下。

```
// pom.xml of Parent
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>org.example</groupId>
  <artifactId>parent</artifactId>
  <version>1.0-SNAPSHOT</version>
  <packaging>pom</packaging>

  <name>parent</name>

  <dependencyManagement>
    <dependencies>
      <dependency>
        <groupId>com.alibaba</groupId>
        <artifactId>fastjson</artifactId>
        <version>1.2.39</version>
      </dependency>
    </dependencies>
  </dependencyManagement>
</project>
```

```
// pom.xml of child
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>org.example</groupId>
        <artifactId>parent</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    <groupId>org.example</groupId>
    <artifactId>child</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>jar</packaging>

    <name>child</name>

    <dependencies>
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>fastjson</artifactId>
            <version>1.2.83</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-assembly-plugin</artifactId>
                <configuration>
                    <descriptors>
                        <descriptor>src/main/assembly/package.xml</descriptor>
                    </descriptors>
                </configuration>

                <executions>
                    <execution>
                        <id>make-assembly</id>
                        <phase>package</phase>
                        <goals>
                            <goal>single</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

```
// package.xml
<assembly
        xmlns="http://maven.apache.org/plugins/maven-assembly-plugin...