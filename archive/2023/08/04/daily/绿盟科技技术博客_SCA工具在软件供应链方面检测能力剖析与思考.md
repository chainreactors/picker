---
title: SCA工具在软件供应链方面检测能力剖析与思考
url: http://blog.nsfocus.net/sca-2/
source: 绿盟科技技术博客
date: 2023-08-04
fetch_date: 2025-10-04T12:03:07.936898
---

# SCA工具在软件供应链方面检测能力剖析与思考

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# SCA工具在软件供应链方面检测能力剖析与思考

### SCA工具在软件供应链方面检测能力剖析与思考

[2023-08-03](https://blog.nsfocus.net/sca-2/ "SCA工具在软件供应链方面检测能力剖析与思考")[王永吉](https://blog.nsfocus.net/author/wangyongji/ "View all posts by 王永吉")

阅读： 6,112

## **一、软件供应链**

1.1  软件供应链漏洞

Verocode研究结果表明[1]，在开源组件仓库中70.5%的代码库存在安全漏洞，而这些安全漏洞风险46.6%是由其他开源项目直接、间接引进所导致的。Black Duck 报告发现，2020年经过审计的1,546个商业代码库中，98%包含开源软件包，每个代码库平均有528个软件包，84%的代码库在其开源依赖项中至少包含一个公开已知的漏洞[2]。

开源组件的依赖项一环套着一环，在引入开源组件的时候，你不会知道你额外引入了哪些其他的组件及漏洞，例如，在实际编写项目的时候，为了兼容性，你引入了著名Python组件Requests的2.24.0版本，但实际上，Requests的2.24.0版本依赖了Certifi 2023.5.7版本、Chardet 3.0.4版本、Idna 2.10.0版本、Urllib3 1.25.11版本。若不使用软件供应链漏洞检测工具，Requests 2.24.0版本目前是没有漏洞的，但是由于软件供应链的特性，Urllib3 1.25.11版本存在CVE-2021-33503漏洞，导致自身代码存在危险。

## **二、软件供应链漏洞检测工具简介**

2.1  软件供应链漏洞检测工具

目前的软件供应链漏洞检测工具集成在SCA（Software Composition Analysis：软件组成分析）工具内，软件成分分析的目的即是分析出软件组成成分、以及软件内的漏洞，这些工具在检测依赖项的方式以及它们维护的漏洞数据库方面可能有所不同。笔者这篇文章中并不会太多关注软件成分分析是如何实现的，重点关注软件供应链漏洞的检测方法，以及这些工具对比、不足、优势。

目前国外的检测工具有OWASP Dependency-Check、Snyk、GitHub Dependabot、Maven Security Versions (MSV)、Npm audit、Eclipse Steady、WhiteSource等等。每个工具由不同强大的公司作为背景，应用的场景不尽相同，下面将一一简单介绍。

OWASP Dependency Check[3]是一个开源的软件组件漏洞检测工具，旨在帮助开发人员和安全专家发现和分析应用程序中存在的组件漏洞。Dependency Check通过分析应用程序的依赖关系，包括使用的第三方库、框架和组件，来检测其中是否存在已知的安全漏洞。它使用漏洞数据库（如NVD、Sonatype OSS Index等）来匹配组件版本与已知漏洞之间的关联，从而确定应用程序是否受到已知漏洞的影响。它提供了一种自动化的方式来检测漏洞，减少了手动检查的工作量，同时提供了详细的报告和输出，方便开发人员和安全专家进行漏洞分析和修复工作。

Snyk是一套云原生、以开发人员为中心的工具，专为DevSecOps和云原生开发商店而构建。它以其SCA和容器安全扫描功能而闻名，能够扫描应用程序的依赖文件[4]，包括开源库和框架，以检测其中是否存在已知的漏洞。它使用多个漏洞数据库，包括NVD（National Vulnerability Database）和自有的漏洞数据库，来匹配组件版本与已知漏洞之间的关联。它还提供与常见集成开发环境（IDE）的集成，如IntelliJ IDEA、VS Code和Eclipse等，通过这些插件，开发人员可以在编码过程中及时获取组件漏洞信息，从而更好地集成安全性和及时修复漏洞。同时提供了命令行工具，可以方便地集成到CI/CD流程中，实现自动化的漏洞扫描和报告生成。

Dependabot是一款流行的自动化依赖项更新工具，旨在帮助开发人员保持应用程序的依赖项和组件库的最新状态，使用GitHub自建漏洞库[5]。它能够检测项目的依赖关系，并在相关的依赖项有新版本发布时提供自动更新建议。它会扫描各种语言和平台的依赖关系，包括常见的编程语言如Java、JavaScript、Python、Ruby等，以及常用的包管理器如Maven、Npm、Pip、Bundler等。它允许用户对其行为进行定制化配置。用户可以定义更新策略、指定更新频率、设置安全漏洞提醒级别等，以满足项目的具体需求和安全要求。同时它支持多种语言和平台，并与各种版本控制系统（如Git、GitHub、GitLab等）和持续集成工具（如Travis CI、CircleCI等）集成，使得它在不同开发环境和工作流程中都能方便地使用。

Maven Security Versions (MSV)是一款轻量级的工具，特别适合用于Maven项目[6]的安全漏洞管理。它提供了简单易用的界面和丰富的功能，帮助开发人员快速发现和解决项目中的安全漏洞，提升应用程序的安全性和可靠性。它支持多个漏洞数据库，包括NVD（National Vulnerability Database）、Red Hat Security Data API等。这使得它能够获取广泛的漏洞信息，并与不同的安全数据源保持同步。同时它可以与持续集成/持续交付（CI/CD）流程集成，以自动化漏洞扫描和修复过程。通过将MSV添加到您的CI/CD工作流中，您可以在每次构建或部署时自动运行漏洞扫描，并根据报告中的结果采取相应的行动。

Npm audit：这是Npm包管理器的原生工具，用于扫描Npm项目。该工具通过扫描依赖文件来工作并维护自己的漏洞数据库[7]。

Eclipse Steady是一个开源的漏洞管理工具，旨在帮助开发人员和安全专家管理和修复应用程序中的开源组件漏洞[8]。它提供了一套完整的工具链，用于分析项目的依赖关系、检测组件漏洞、提供修复建议以及跟踪漏洞修复的进展。它提供了一个可视化的界面，用于跟踪漏洞修复的进展。它可以显示漏洞的状态、修复建议的接受情况以及已经修复的漏洞数量等信息。这有助于团队协作和及时解决漏洞问题。

WhiteSource Software工具的一大亮点是对开发人员友好的组件安全问题进行修复，其中包括警报和修复过期和恶意组件[9]。它有一个名为“WhiteSource Bolt”的GitHub机器人，它可以扫描Maven和Npm项目。他们说，“WhiteSource提供与众不同的功能，包括一个浏览器插件，以帮助避免有问题的组件，并从开发人员队列中删除无法访问的漏洞，以改善开发人员体验。但它落后的一点是缺乏开箱即用的政策。”WhiteSource公司今年早些时候推出了静态应用程序安全测试(SAST)解决方案。

2.2 软件供应链漏洞检测工具架构

针对于软件供应链漏洞检测过程，所有工具的框架都是大体一致的，每个厂商在细节实现略有不同，在应用场景上大不相同。

软件供应链漏洞检测框架如图1所示。

![](https://blog.nsfocus.net/wp-content/uploads/2023/08/wps_doc_0-300x263.png)

图1 软件供应链漏洞检测通用架构

各家厂商均有自己的组成成分分析工具、依赖关系库、漏洞库，最终完成软件供应链漏洞的关联。

组成成分分析是识别该组件内的组成成分，一般是组件、版本。识别过程分为HASH比对，即厂家组建一个巨大的HASH库，数据库包含各个发布组件的HASH值，经过比对后便可识别该组件是该组件的哪个版本。另一种方法是识别各个语言、系统的构建工具，例如Python的requirements.txt、Setup脚本，Java语言的Pom文件，Go语言的go.mod等等。然而每种方法各有优略，基于HASH的方法漏报率较大，随便修改一下便不能正确识别，基于构建脚本的工具误报率较大，经常针对某一组件错误识别，库组件与自定义组件混淆等等。

针对于以上，目前努力的方向有基于抽象语法树的相似性检测算法、基于TOKEN的相似性检测算法，由于本文着重于漏洞检出工具的比较，所以不再赘述。

依赖关系的分析是通过分析组件之间的依赖关系，组成一个组件和组件之间的依赖关系数据库。组成成分分析可以理解为分析项目中直接使用的组件，而依赖关系数据库分析的是隐藏依赖关系，即组件与项目间接的依赖关系。

漏洞库是由目前公开的漏洞库，经过整理组成，从漏洞的描述中整理出漏洞影响组件的名称、版本信息。

由此，整体分析工作便完成了，先由软件成分分析从项目内分析出项目直接使用了哪些组件，再由依赖关系关联出所有的隐藏依赖组件，对于上述所有的组件匹配出相关联的漏洞。

然而虽然原理比较简单，但各个技术部分实施存在着巨大的挑战。

2.3 软件供应链工具做了什么

漏洞告警：这是最主要的工作，即对项目中有威胁的漏洞进行告警，具体包括漏洞数量、漏洞相关维度（危险等级、时间、描述等等）、影响组件、位置等等。

依赖项、依赖路径：项目中的依赖关系。

扫描时信息：具体扫描了哪些内容，整体花费的时间。

其他信息：修复建议、漏洞可利用性确认等等。

## **三、对比分析**

3.1 检测对象

检测对象是OpenMRS，一个电子病历平台的网络应用程序，使用的是2.10.0版本，OpenMRS由44个项目组成，这些项目托管在GitHub上各自独立的存储库中。在44个项目中，39个是Maven项目，1个是Npm项目。其他4个项目分别由一个Maven和一个Npm项目组成。基于OpenMRS结构，研究范围为Maven和Npm依赖关系及其关联漏洞库[10]。

OpenMRS依赖于许多第三方依赖项，作为一个Web应用程序，它由多个异构组件组成，例如数据库、内容生成引擎、客户端代码等，因此增加了存在大量不同的易受攻击依赖项的可能性。适用于检测对象。

3.2 识别能力区别

![](https://blog.nsfocus.net/wp-content/uploads/2023/08/wps_doc_1-300x109.png)

图2 对于漏洞依赖项及其关系识别能力

![](https://blog.nsfocus.net/wp-content/uploads/2023/08/wps_doc_2-300x124.png)

图3 对于MAVEN库、NPM库漏洞识别能力

漏洞依赖项是指漏洞能够直接、间接影响的上游组件。

由图2、3可得：OWASP DC检测Maven和Npm项目的最多数量的独特依赖项和独特漏洞。对于Maven项目，WhiteSource也报告了Snyk报告的漏洞依赖项的54%。

对于Maven和Npm项目，MSV和Dependabot分别检测到最少数量的独特漏洞，由于数量较少未在图中展示。

其中，对于Maven库，除了MSV和Dependabot均报告了非CVE漏洞，对于Npm库，所有工具均报告了非CVE漏洞。

对于漏洞依赖过程，只有Npm-audit和Snyk报告每个独特漏洞的所有可能的依赖路径。

对于可达性分析：可达性分析是指主程序对于组件是否具有代码路径的可达性。漏洞代码的可达性分析具有重要意义，在软件供应链中具有大量代码的冗余，开发者往往为了使用了组件的一小部分功能而将组件的全部代码引入项目。本次分析的所有SCA工具只有Steady对代码通过静态分析进行可达性分析。对于本次84.2%的漏洞告警，Steady没有找到对应的依赖项。发现2.1%的漏洞告警可能能执行，对于1.6%的告警实际能执行。但是此次OpenMRS项目在Steady中仅达到20%左右的测试覆盖率。有限的测试覆盖范围可能影响了前面的数据的正确性。

对于漏洞的报告，这些工具均提供漏洞严重程度指标，当然，这些都是NVD公开的CVSS数据，但是针对于非CVE漏洞，Snyk也给出了CVSS分数，此外Snyk提供公开的EXP信息。Steady提供了漏洞流行度信息，该数据是Google做的趋势分析。

此外，OWASP DC通过扫描多个数据源提供了扫描出来依赖关系的置信度。

3.3 总结

SCA工具组件成分分析准确性：目前SCA分析只是针对于清单扫描，例如requirement.txt、pom.xml等，然而这些清单的准确性是不确定的，大多数工具未对代码进行组成成分分析，因此被关联出来的漏洞组件不一定存在于项目中。

SCA工具组件依赖关系、漏洞映射的准确性：不同的工具对于同一个组件版本扫描出来的漏洞是不一致的，是因为依赖关系以及漏洞的数据库发生了变化，由于组件的不同生态，组件的同一版本发布后也有可能更改内部的依赖关系，漏洞发布之后也有可能更改影响范围，因此自建库应定时扫描数据变化及时更改。

漏洞的可利用性：目前漏洞越来越多，影响的组件越来越多，扫描报告的漏洞往往不能做到及时响应，因此，工具的可达性分析是十分重要的，对于不可达的漏洞可以直接删除漏洞代码作为响应，对于可达的漏洞可根据调用链做规则截断处理。

非CVE漏洞的存在：Snyk报告的53个非CVE中，有41个是在2020年之前发布的；而WhiteSource报告的54个非CVE中，有50个是在2020年之前发布的。因此，开发人员可能会质疑为什么报告的漏洞没有CVE标识符，因为CVE验证通常需要三个月左右的时间。因此，在构建漏洞数据库时应扫描全网，包括GitHub Issue等关键点，及时对没有CVE标识的漏洞进行响应。

参考文献

[1]. Veracode. State of Software Security: Open Source Edition. https://info.veracode.com/report-state-of-software-security-open-source-edition.html

[2]. Synopsys. 2021 open source security and risk analysis report. https://www.synopsys.com/software-integrity/resources/analyst-reports/opensource-security-risk-analysis.html, 2021.

[3] OWASP Dependency Check [EB/OL]. https://www.owasp.org/ index.php/OWASPDependencyCheck, 2018.

[4] Snyk open source security management. https://support.snyk.io/hc/enus/articles/360000925438-What-does-Snyk-access-and-store-when-scanninga-project-.[5] Github advisory database. https://github.com/advisories.

[6] Victims software vulnerability scanner. https://blog.victi.ms/.

[7] npm security advisories. https://www.npmjs.com/advisories.

[8] Eclipse steady 3.1.14 (incubator project). https://eclipse.github.io/steady/about/.

[9] Whitesource bolt for github. https://github.com/apps/whitesource-bolt-forgithub.

[10] Imtiaz N, Thorn S, Williams L. A comparative study of vulnerability reporting by software composition analysis tools[C]//Proceedings of the 15th ACM/I...