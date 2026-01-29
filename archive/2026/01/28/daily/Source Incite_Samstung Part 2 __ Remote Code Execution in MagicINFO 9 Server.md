---
title: Samstung Part 2 :: Remote Code Execution in MagicINFO 9 Server
url: https://srcincite.io/blog/2026/01/28/samstung-part-2-remote-code-execution-in-magicinfo-server.html
source: Source Incite
date: 2026-01-28
fetch_date: 2026-01-29T04:04:40.915413
---

# Samstung Part 2 :: Remote Code Execution in MagicINFO 9 Server

[![Source Incite](/assets/si.png)](/)

[About](/about/) [Blog](/blog/) [Advisories](/advisories/) [Exploits](/exploits/) [Research](/research/)

[Training](/training/)

[Syllabus](/training/syllabus/) [Prerequisites](/training/prerequisites/) [Challenge](/training/challenge/) [Schedule/Signup](/training/schedule-signup/) [Testimonials](/training/testimonials/) [Faq](/training/faq/)

[Contact](/contact/)

# Samstung Part 2 :: Remote Code Execution in MagicINFO 9 Server

Jan 28, 2026

In [part 1](/blog/2026/01/28/samstung-part-1-remote-code-execution-in-magicinfo-server.html) I detailed my approach to following a rabbit hole that almost turned into pre-auth remote code execution with a default setup. Although I didn’t achieve my goal in the first part, on further review of the patches I was finally able to reach a full success - albeit it does take on average ~12 hours to land the shell. Let’s investigate the bug chain and determine why.

Please note that in this blog post, I will show you snippets of code decompiled directly with the [fernflower decompiler](https://github.com/fesh0r/fernflower) instead of the usual [jd-eclipse](https://github.com/java-decompiler/jd-eclipse). This is because jd-eclipse failed to decompile many of the classes correctly.

## Version

The version that was tested, was the latest patched version at the time, `21.1080.0`. The file that was tested was `MagicInfo 9 Server 21.1080.0 Setup.zip` released on the 5th of August, 2025 and had a sha1 hash of `9744711fe76e7531f128835bf83c9ae001069115`. Note that the patch in July was fixing 18 high impact vulnerabilities, many that were pre-authenticated or allowed for an authentication bypass.

## Bugs

Today we are going to discuss the following bugs:

1. [SRC-2025-0003](/advisories/src-2025-0003) - Samsung MagicINFO 9 Server downloadChangedFiles Directory Traversal Authentication Bypass Vulnerability
2. [SRC-2025-0004](/advisories/src-2025-0004) - Samsung MagicINFO 9 Server ResponseUploadActivity TOCTOU Remote Code Execution Vulnerability

## The WSServlet Attack Surface

```
    <servlet>
        <servlet-name>WSRMService</servlet-name>
        <servlet-class>com.samsung.magicinfo.protocol.http.service.WSServlet</servlet-class>
        <init-param>
            <param-name>CONF_PATH</param-name>
            <param-value>/WEB-INF/conf/</param-value>
        </init-param>
        <init-param>
            <param-name>SERVICE_DESCRIPTOR</param-name>
            <param-value>
                samsung-wsf-service-descriptor.xml
            </param-value>
        </init-param>
        <load-on-startup>1</load-on-startup>
    </servlet>
    <servlet-mapping>
        <servlet-name>WSRMService</servlet-name>
        <url-pattern>/WSRMService</url-pattern>
    </servlet-mapping>
```

In the first blog post, I mentioned how there is quite an interesting attack surface in the `com.samsung.magicinfo.protocol.http.service.WSServlet`. Before we dive into the vulnerability, let’s walk through the attack surface to get a better understanding. When calling the `process` method inside of `com.samsung.magicinfo.protocol.interfaces.SRMServiceInterfaceImpl` class which is called from any of the web service requests; `NOTIFY`, `DOWNLOAD`, `REPORT` or `COMMAND`. We reach the following code:

```
   private MOMsg process(MOMsg moMsg) throws BasicException {
      ServiceOPManager manager = null;
      manager = ServiceOPManagerFactory.getServiceOPManager(ActionParser.parse(moMsg)); // 1
      return manager.process(moMsg); // 2
   }
```

At [1] the code will call `getServiceOPManager` which will return the `com.samsung.magicinfo.protocol.interfaces.NOTIFYExecuter` class instance if we are calling the `NOTIFY` function from the web service.

```
public class NOTIFYExecuter extends Executer {
   Logger logger = LoggingManagerV2.getLogger(NOTIFYExecuter.class);

   protected AppBO process(HashMap params) throws BasicException {
      AppBO responseAppBO = null;
      String mo_Event = null;

      try {
         mo_Event = this.resultSet.getAttribute("MO_EVENT");
      } catch (RMQLException ex) {
         this.logger.error((String)"", (Throwable)ex);
         throw new BasicException(ex.getMessage(), ex);
      }

      try {
         ServiceDispatcher dispatcher = WSRMServiceDispatcher.getInstance();
         ServiceFactory sfc = WSRMServiceFactory.getInstance();
         String service_id = sfc.getServiceId(mo_Event, this.appBO.getOperation()); // 3
         responseAppBO = (AppBO)dispatcher.startService(service_id, params); // 4
         return responseAppBO;
      } catch (Exception ex) {
         this.logger.error((String)"", (Throwable)ex);
         throw new BasicException(ex.getMessage(), ex);
      }
   }
}
```

Calling into the `com.samsung.magicinfo.protocol.servicemanager.WSRMServiceFactory` classes `getServiceId` at [3] the code attempts to determine what the `service_id` is for this request. This is important because an attacker cannot *directly* control it:

```
   public String getServiceId(String mo_path, String operation) {
      for(int i = 0; i < serviceOpMapList.size(); ++i) {
         ServiceOpMap serviceOpMap = (ServiceOpMap)serviceOpMapList.get(i); // 5
         if (operation != null && operation.equals(serviceOpMap.getOperation())) { // 6
            if (mo_path == null) {
               if (serviceOpMap.getMo_path() == null) {
                  return serviceOpMap.getService_id();
               }
            } else {
               if (serviceOpMap.getMo_path() == null) {
                  return serviceOpMap.getService_id();
               }

               if (mo_path.indexOf(serviceOpMap.getMo_path()) >= 0) { // 7
                  return serviceOpMap.getService_id();
               }
            }
         }
      }

      return null;
   }
```

At [5] the code gets each `serviceOpMap` from the `serviceOpMapList` and checks that the [6] incoming operation is matching and if a `mo_path` is defined, that it matches the one in the `serviceOpMap` at [7]. If it does, then return the `service_id`. But where is this `serviceOpMapList` defined? During initialization we can see that the `serviceOpMapList` is set from a call to `getServiceOpMapList` at [8]

```
   private static synchronized boolean initialize() {
      serviceStore = new HashMap();
      ServiceStatusManager serviceStatusManager = ServiceStatusManagerImpl.getInstance();
      List serviceList = null;

      try {
         serviceList = serviceStatusManager.getServiceManageList();

         for(int i = 0; i < serviceList.size(); ++i) {
            ServiceManageList serviceMgmt = (ServiceManageList)serviceList.get(i);
            serviceStore.put(serviceMgmt.getService_id(), new ServiceInfo(serviceMgmt.getService_id(), serviceMgmt.getService_name(), serviceMgmt.getClass_name(), serviceMgmt.isLogging()));
         }

         serviceOpMapList = serviceStatusManager.getServiceOpMapList(); // 8
      } catch (Exception e) {
         logger.error((Object)e);
      }

      return true;
   }
```

Inside of the `ServiceStatusManagerImpl` class, we can see that it’s just a wrapper around the database:

```
   public List getServiceOpMapList() throws Exception {
      return dao.selectServiceOpMapList();
   }
```

Which is defined in the `com/samsung/magicinfo/protocol/servicestatus/dao/ServiceStatusDAOMapper.xml` file:

```
        <select id="selectServiceOpMapList" resultType="com.samsung.magicinfo.protocol.entity.ServiceOpMap">
                SELECT * FROM MI_RM_MAP_SERVICE_OPERATION
        </select>
```

When we step into the `size` method of the `ArrayList` inside of the `getServiceId` method, we can see there are 16 entries:

![](/assets/images/samstung-part-2-remote-code-execution-in-magicinfo-server/determining_surface.png "A breakpoint to see the number of entries and their values")

…and these correspond with the number of entries in the `MI_RM_MAP_SERVICE_OPERATION` table within the database:

![](/assets/images/sams...