---
title: Apache Struts2 Spring Plugin Uses a Previously Closed Resource
url: https://seclists.org/fulldisclosure/2026/Nov/5
source: Full Disclosure
date: 2026-11-02
fetch_date: 2026-11-03T08:51:59.264404
---

# Apache Struts2 Spring Plugin Uses a Previously Closed Resource

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](4)
[By Date](date.html#5)
[![Next](/images/right-icon-16x16.png)](6)

[![Previous](/images/left-icon-16x16.png)](4)
[By Thread](index.html#5)
[![Next](/images/right-icon-16x16.png)](6)

![](/shared/images/nst-icons.svg#search)

# Apache Struts2 Spring Plugin Uses a Previously Closed Resource

---

*From*: Daniel Owens via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Sat, 31 Oct 2026 19:46:10 +0000

---

```
Description
The Apache Struts2 Spring Plugin opens a Spring `ApplicationContex` via a try-with-resources block and, outside of said
block, then continues to use the closed resource, resulting in an uncaught `IllegalStateException`.  This particular
issue prevents proper functionality and indicates poor code quality and code review standards and processes, while not
being, itself, otherwise excessively meaningful for a production environment (as developer mode should not be enabled
in such an environment), although it would hamper staging, test, and developer environments that are configured in
accordance with Apache-recommended hot-reload configurations for such environments
(https://struts.apache.org/plugins/spring/#class-reloading).

Impact
Anyone who follows Struts' documented configuration for this plugin -- enabling `struts.devMode`, setting a non-blank
`struts.objectFactory.spring.class.reloading.watchList`, and declaring `ClassReloadingXMLWebApplicationContext` as the
root context class in web.xml -- will trigger this pathway on every application startup.  Since close() call `null`s
the context's internal bean factory immediately after `refresh()` succeeds,
`SpringObjectFactory.setApplicationContext()`call to `getBeanFactory()` throws an uncaught `IllegalStateException`,
aborting the Struts-Spring integration startup process before it can ever finish.  Even if the exception were caught,
`close()` has already stopped the `FilesystemAlterationMonitor` watchdog thread, so the live class-reloading capability
would never fire a single reload.  As such, the hot-reload feature cannot and does not work with this
Apache-recommended configuration.

Examples
Sample Code
The code below clearly shows the issue when in developer, a watch list, and hot-reloading are enabled.  The
try-with-resources calls `.close()` when exiting, against `reloadingContext`, which is merely a pointer to
`appContext`, thereby closing `appContext`.  Immediately after exiting the try-with-resources and wrapping conditional,
`this. setApplicationContext` is called, passing in the now closed `appContext`.  Importantly, `
ClassReloadingXMLWebApplicationContext`, to which `appContext` was cast during the initialisation of the
try-with-resources and against which the `finally` that this construct generates (try-with-resources effectively being
syntactic sugar for a `try{...} finally{reloadingContext.close()}`), has a `close()` defined that calls to
`super.close()` before removing and stopping the listener.

```java
        String watchList = container.getInstance(String.class,
SpringConstants.STRUTS_OBJECTFACTORY_SPRING_CLASS_RELOADING_WATCH_LIST);
        String acceptClasses = container.getInstance(String.class,
SpringConstants.STRUTS_OBJECTFACTORY_SPRING_CLASS_RELOADING_ACCEPT_CLASSES);
        String reloadConfig = container.getInstance(String.class,
SpringConstants.STRUTS_OBJECTFACTORY_SPRING_CLASS_RELOADING_RELOAD_CONFIG);

        if ("true".equals(devMode)
                && StringUtils.isNotBlank(watchList)
                && appContext instanceof ClassReloadingXMLWebApplicationContext) {
            //prevent class caching
            useClassCache = false;

            try (ClassReloadingXMLWebApplicationContext reloadingContext = (ClassReloadingXMLWebApplicationContext)
appContext) {
                reloadingContext.setupReloading(watchList.split(","), acceptClasses, servletContext,
                        "true".equals(reloadConfig));
                LOG.info("Class reloading is enabled. Make sure this is not used on a production environment!\n{}",
                        watchList);

                setClassLoader(reloadingContext.getReloadingClassLoader());

                // we need to reload the context, so our isntance of the factory is picked up
                reloadingContext.refresh();
            }
        }

        this.setApplicationContext(appContext);
```
Code snippet from `struts2-spring-plugin`'s
plugins/spring/src/main/java/org/apache/struts2/spring/StrutsSpringObjectFactory.java, lines 97-120

```java
    public void close() {
        super.close();

        if (filesystemAlterationMonitor != null) {
            filesystemAlterationMonitor.removeListener(this);
            filesystemAlterationMonitor.stop();
        }
    }
```
Snippet from `struts2-spring-plugin`'s
plugins/spring/src/main/java/org/apache/struts2/spring/ClassReloadingXMLWebApplicationContext.java, lines 157-164,
showing the close() override invoked by the implicit try-with-resources call
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](4)
[By Date](date.html#5)
[![Next](/images/right-icon-16x16.png)](6)

[![Previous](/images/left-icon-16x16.png)](4)
[By Thread](index.html#5)
[![Next](/images/right-icon-16x16.png)](6)

### Current thread:

* **Apache Struts2 Spring Plugin Uses a Previously Closed Resource** *Daniel Owens via Fulldisclosure (Nov 01)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap Public Source License](https://nmap.org/npsl/)

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")
[![](/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")
[![](/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")