---
title: Upgrade to Java Spring Boot Version 2.7.x on BTP
url: https://blogs.sap.com/2022/11/17/upgrade-to-java-spring-boot-version-2.7.x-on-btp/
source: SAP Blogs
date: 2022-11-18
fetch_date: 2025-10-03T23:06:15.521312
---

# Upgrade to Java Spring Boot Version 2.7.x on BTP

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Upgrade to Java Spring Boot Version 2.7.x on BTP

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158679&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Upgrade to Java Spring Boot Version 2.7.x on BTP](/t5/technology-blog-posts-by-sap/upgrade-to-java-spring-boot-version-2-7-x-on-btp/ba-p/13552620)

![showkath_naseem](https://avatars.profile.sap.com/b/3/idb31430339dce394fae56e5099a002a181ef4cf21068545b19463517d3280ac9b_small.jpeg "showkath_naseem")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[showkath\_naseem](https://community.sap.com/t5/user/viewprofilepage/user-id/1529)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158679)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158679)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552620)

‎2022 Nov 17
7:48 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158679/tab/all-users "Click here to see who gave kudos to this post.")

4,917

* SAP Managed Tags
* [Java](https://community.sap.com/t5/c-khhcw49343/Java/pd-p/615693459582413452469752593601406)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [Java

  Programming Tool](/t5/c-khhcw49343/Java/pd-p/615693459582413452469752593601406)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (2)

In this blog post i would like to share my experience on upgrading Java projects , BTP CAP Java projects migration to Spring Boot 2.7.5 version

* As you might know Spring Boot 2.7 release includes [31 bug fixes, documentation improvements, and dependency upgrades](https://github.com/spring-projects/spring-boot/releases/tag/v2.7.5).

* If you decided to upgrade to Spring Boot Version 2.7.x but if your java spring project has old dependencies less than Spring Boot <2.7.x then  you may face lot of an arbitrary problems.

# Context

If you are going to upgrade your project

* Then this **may** affect maven dependencies

* Eventually compile, build issues

* Java application may not start/Java application deployment issues runtime issues .

Java developers may some tough time in fixing depended on project source code or dependencies versions , how project packaged .

Below errors **may** **be** due to inconsistency in the Spring libraries of application.

|
 Error 1    creating bean with name 'dataSource' defined in class path resource [org/springframework/boot/autoconfigure/jdbc/DataSourceConfiguration$Hikari.class]: Bean instantiation via factory method failed |

|
 Error 2 :         Request processing failed; nested exception is com.sap.cds.CdsDataStoreException: Error executing the statement OUT Caused by: org.h2.jdbc.JdbcSQLSyntaxErrorException: Table "CONFIGSERVICE\_LOCATIONS" not found; SQL statement: |

|
 Error 3 :         org.springframework.boot.sql.init.dependency.AnnotationDependsOnDatabaseInitializationDetector. |

|
 Error 4 :    org.springframework.beans.BeanInstantiationException: Failed to instantiate [org.springframework.web.servlet.HandlerMapping]:    Factory method 'resourceHandlerMapping' threw exception; nested exception is java.lang.NoSuchMethodError: '    io.github.classgraph.ClassGraph io.github.classgraph.ClassGraph.acceptPaths(j |

|
 Error 5 :    Request processing failed; nested exception is com.sap.cds.CdsDataStoreException:  Caused by: org.h2.jdbc.JdbcSQLSyntaxErrorException: Table "x" not found; SQL statement:  Caused by: com.sap.cds.CdsDataStoreException: Error executing the statement  OUT at org.h2.message.DbException.getJdbcSQLException(DbException.java:453) ~[h2-1.4.200.jar:1.4.200]  OUT at org.h2.message.DbException.getJdbcSQLException(DbException.java:429) ~[h2-1.4.200.jar:1.4.200]  OUT at com.sap.cds.impl.JDBCClient.lambda$executeQuery$5(JDBCClient.java:262) ~[cds4j-runtime-1.33.0.jar:na]  OUT com.sap.cloud.sdk.cloudplatform.exception.ShouldNotHappenException:  com.sap.cloud.sdk.cloudplatform.thread.exception.ThreadContextExecutionException: org.springframework.web.util.NestedServletException: |

|
 Error 6 :         Caused by: com.sap.cloud.sdk.cloudplatform.thread.exception.ThreadContextExecutionException: org.springframework.web.util.NestedServletException: Handler dispatch failed; nested exception is java.lang.NoClassDefFoundError: com/sap/cloud/security/servlet/MDCHelper |

|
 class com.sap.cloud.security.token.XsuaaToken does not define or inherit an implementation of the resolved method 'abstract java.util.Set getAudiences()' of interface com.sap.cloud.security.token |

|
 … .. etc |

# Troubleshoot : Discovering the root causes of problems

* If your application failed to start or unsuccessful deployment java app , then try to find Deployment errors locally by running  java app

```
mvn spring-boot:run
```

* For BTP Cloud Foundry Java (Native Deployment Manifest.yml based ) , If deployment failed on BTP then you can Download Java Deployment logs using below command &  examine the potential errors

```
cf logs --recent yourjava-app-name
```

* if Java project is one of module in MTA then you can refer below article

[How to Download MTA Deployment Logs from SAP Business Technology Platform Cloud Foundry Environment](https://blogs.sap.com/2022/10/21/how-to-download-mta-deployment-logs-from-sap-business-technology-platform-cloud-foundry-environment/)

# Solution

If your facing Deployment errors  or Spring Boot APPLICATION FAILED TO START

* Please check that you consistently use Spring Boot 2.7.5 for all Spring Boot Modules and that you also included the correct Spring Framework version that is expected to be used by Spring Boot 2.7.5

* Try to have all of these dependencies managed by the Spring Boot BOM and not maintain yourself.

* Java Developers needs to analyse the dependency tree for project using commands or Eclipse IDE

#### *Maven*

For maven based projects you can get the list of dependent libraries by calling & then you can examine the potential version conflicts

**mvn dependency:tree**

or

mvn dependency:tree -Dincludes= org.springframework.\*

* Then fix versions . For example Spring Boot 7.5uses [Spring Security 5.7.4](https://github.com/spring-projects/spring-boot/blob/v2.7.5/spring-boot-project/spring-boot-dependencies/build.gradle#L1778) but application may have older version of Spring dependencies loaded form other dependencies (example : outdated SAP Cloud SDK bom downgraded the spring dependency to version 5.3.9. but spring-boot 2.7.5 requires a newer spring version. )

* SAP also released the correspondingNotes

Please take a look inside the [important-changes-in-java](https://cap.cloud.sap/docs/releases/aug22#important-changes-in-java),    [CAP release notes](https://cap.cloud.sap/docs/releases/oct22#important-changes-in-java)and the [Spring Boot release](https://github...