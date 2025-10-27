---
title: GC analysis and troubleshooting with SapMachine
url: https://blogs.sap.com/2023/05/05/gc-analysis-and-troubleshooting-with-sapmachine/
source: SAP Blogs
date: 2023-05-06
fetch_date: 2025-10-04T11:40:29.078772
---

# GC analysis and troubleshooting with SapMachine

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* GC analysis and troubleshooting with SapMachine

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/160333&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [GC analysis and troubleshooting with SapMachine](/t5/technology-blog-posts-by-sap/gc-analysis-and-troubleshooting-with-sapmachine/ba-p/13557268)

![ansteiner](https://avatars.profile.sap.com/1/f/id1f2fa43f59da6226ccc5517c01dc40a20750dad7090ffc3f98273a71d8f6f406_small.jpeg "ansteiner")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[ansteiner](https://community.sap.com/t5/user/viewprofilepage/user-id/179729)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=160333)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/160333)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13557268)

‎2023 May 05
3:44 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/160333/tab/all-users "Click here to see who gave kudos to this post.")

1,750

* SAP Managed Tags
* [SAP Java Virtual Machine](https://community.sap.com/t5/c-khhcw49343/SAP%2520Java%2520Virtual%2520Machine/pd-p/01200615320800003576)

* [SAP Java Virtual Machine

  SAP Java Virtual Machine](/t5/c-khhcw49343/SAP%2BJava%2BVirtual%2BMachine/pd-p/01200615320800003576)

View products (1)

There are several possibilities to analyze and troubleshoot GC issues. You can activate the gc log via Unified JVM logging([-Xlog:gc](https://openjdk.org/jeps/158)) to get a textual log output. This can be also set for detailed GC phases and to specific levels. The analysis can be done on the textual log file or with available open source tools like [JIFA](https://github.com/eclipse/jifa) or commercial tools like [GCeasy](https://gceasy.io) to parse and analyze the log and visualize the findings.

Another possibility is to use the Java Flight Recorder ([JFR](https://openjdk.org/jeps/328)) to profile your Java application and analyze this with Java Mission Control ([JMC](https://wiki.openjdk.org/display/jmc/Main)).

We, from SapMachine development team, build and provide also a JMC version on [SapMachine](https://sap.github.io/SapMachine/).

## SapMachine will provide two additional Flight Recording configurations

The SapMachine starting with 11.0.19 and 17.0.7 provides two additional Flight Recording configurations(located in the directory lib/jfr of the JDK/JRE), especially for GC profiling.
The gc.jfc, which is a lightweight GC profiling. This can be used also for longer profiling runs and will provide general GC profiling data with limited details and small recording size.
The gc\_details.jfc will record all GC events and details. This will have a higher impact caused by heap inspection initiated GCs to get e.g. heap statistics and have a large recording size.

## How to do the JFR profiling:

In general there are three ways to do the recording:

1. The Flight Recording can be enabled by JVM parameter to start this with the startup already(-XX:StartFlightRecording). Per option you can specify the filename to be used to save the recording and you can specify the settings/configuration file.
   E.g. -XX:StartFlightRecording,filename=./my\_recording.jfr,settings=gc\_details.jfc

2. Start the Flight Recorder via jcmd. Connect to the running Java application(jcmd <main class|PID>) and start/dump/stop the recording by specific command(JFR.start, JFR.dump, JFR.stop). You can specify the recording name, settings(configuration), etc. Check the help of the commands to get all available options.
   In SAP BTP you have to [enable ssh in CF](https://docs.cloudfoundry.org/devguide/deploy-apps/ssh-apps.html) first to call the jcmd via cf ssh.
   E.g.:

   ```
   cf ssh <your app name> -c "app/META-INF/.sap_java_buildpack/sap_machine_jre/bin/jcmd $(pgrep java) JFR.start name=gc_recording settings=gc_details.jfc filename=/home/vcap/tmp/gc.jfr"
   ```

3. Connect with JMC to a running local or remote Java application to start/dump/stop the recording without restart. You have to open JMX protocol listener. This can be done with e.g. jcmd <main class|PID> ManagementAgent.start jmxremote.authenticate=false jmxremote.ssl=false jmxremote.port=5555.
   If you want to profile a Java application running behind a firewall you may need port forwarding.
   In SAP BTP you have to start your app with -Djava.rmi.server.hostname=127.0.0.1 and start the Management Agent via cf ssh and use a ssh tunnel. E.g.:

   ```
   cf ssh <your app name> -c "app/META-INF/.sap_java_buildpack/sap_machine_jre/bin/jcmd $(pgrep java) ManagementAgent.start jmxremote.authenticate=false jmxremote.ssl=false jmxremote.port=5555 jmxremote.rmi.port=5555"
   ```

   ```
   cf ssh <your app name> -N -T -L 5555:127.0.0.1:5555
   ```

   Connect with JMC to 127.0.0.1:5555 to get the JMX Console or starting the Flight Recording.

   **Note:**

   Depending on what your SapMachine is using (JRE or JDK), specify the path accordingly (**sap\_machine\_jre** or **sap\_machine\_jdk**). To learn more, see: [SapMachine](https://help.sap.com/docs/btp/sap-business-technology-platform/sapmachine?version=Cloud).

## How to analyze the JFR recording:

The collected jfr recording can be analyzed with JMC. Open the JFR recording file to get the Automated Analysis Results as a first overview.

![](/legacyfs/online/storage/blog_attachments/2023/04/automated-analysis-results_1-1.png)

Figure 1: Analysis overview

The provided findings can be expanded to get more details with hints for optimization.

![](/legacyfs/online/storage/blog_attachments/2023/04/automated-analysis-results-with-details_1-1.png)

Figure 2: Expanded analysis details with hints for optimization

In addition JMC is providing specific Outlines e.g. Java Application, JVM Internals, Environment and the Event Browser. The Outlines will show the specific data in tables or graphs.

In JVM Internals you will find the GC Summary with average, maximum, total GC times of the collections:

![](/legacyfs/online/storage/blog_attachments/2023/04/gc-summary_1-1.png)

Figure 3: GC summary

The GC configuration details:

![](/legacyfs/online/storage/blog_attachments/2023/04/gc-configuration_1-1.png)

Figure 4: The GC configuration details

The Garbage Collections with the GC details:

![](/legacyfs/online/storage/blog_attachments/2023/04/garbage-collections_1-1.png)

Figure 5: Garbage collection details

Depending of the enabled events in the used JFR configuration, the table will show some or all the GC Phase Pause Levels with detailed pause time.

All collected events can be found in the Event Browser:

![](/legacyfs/online/storage/blog_attachments/2023/04/Event-Browser-GC_1-1.png)

Figure 6: Event Browser

There you can also create your own specific outlines/pages for events your are interested in and no outline exists already. In addition you can create outlines/pages for your own custom events.

## Conclusion

With the additional JFR configurations the SapMachine provides, general G...