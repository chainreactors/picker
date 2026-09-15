---
title: IBM Db2 Mirror for i: pre-auth RCE and the road to QSECOFR
url: https://blog.silentsignal.eu/2026/09/14/IBM-Db2-Mirror-for-i-pre-auth-RCE-and-the-road-to-QSECOFR/
source: Silent Signal Techblog
date: 2026-09-14
fetch_date: 2026-09-15T07:03:20.116956
---

# IBM Db2 Mirror for i: pre-auth RCE and the road to QSECOFR

[![Silent Signal](/assets/img/s2_avatar.jpg)](/)

Silent Signal

Professional Ethical Hacking Services

### Contact us

2026 © Silent Signal

![IBM Db2 Mirror for i: pre-auth RCE and the road to QSECOFR](/img/suits.gif)

# IBM Db2 Mirror for i: pre-auth RCE and the road to QSECOFR

[pz](/authors/pz.html) 2026-09-14

This is a write-up of a bug chain in the IBM Db2 Mirror for i web interface. The chain starts without authentication, reaches arbitrary Java/JSP execution in the Liberty application server, and can then cross into QSECOFR on the local IBM i system.

I am not publishing the JSP payload body or a one-command exploit here. The point of this post is the vulnerability mechanics: why the checks failed, which application features became primitives, and how those primitives were chained.

The tested target was a Db2 Mirror GUI WAR deployed on the IBM i administrative Liberty instance. The lab system was IBM i V7R5. The GUI build timestamp in the test environment was from late 2025.

## The application shape

The WAR is a fairly typical Java administrative application. The frontend is Angular, but almost everything interesting goes through a single servlet:

```
@WebServlet(value={"/Db2MirrorServlet/*"})
public class Db2MirrorServlet extends HttpServlet
```

The servlet does not contain the business logic itself. It uses a URL segment as a class name and a request parameter as a method name. In bytecode, the dispatcher does roughly this:

```
String function = request.getParameter("function");
String uri = request.getRequestURI().substring(1);
if (uri.endsWith("/")) {
    uri = uri.substring(0, uri.lastIndexOf("/"));
}
String[] parts = uri.split("/");

String className = "com.ibm.DB2Mirror.action." + parts[2];
Class<?> actionClass = Class.forName(className);
Constructor<?> ctor = actionClass.getConstructor(
    Db2mHttpServletRequestWrapper.class,
    HttpServletResponse.class
);
Method actionMethod = actionClass.getDeclaredMethod(function);
Object action = ctor.newInstance(request, response);
```

After this it performs optional authority and validation checks, then invokes the selected action method.

This means a normal backend call has the following logical shape:

```
/Db2MirrorServlet/<ActionClass>?function=<methodName>
```

For example, the GUI can call `LogAction.getLogFileContent()` by asking the servlet to instantiate `com.ibm.DB2Mirror.action.LogAction` and invoke `getLogFileContent`.

The web application also has a global authentication filter in `WEB-INF/web.xml`:

```
<filter>
    <filter-name>AuthFilter</filter-name>
    <filter-class>com.ibm.DB2Mirror.utils.AuthFilter</filter-class>
</filter>

<filter-mapping>
    <filter-name>AuthFilter</filter-name>
    <url-pattern>/*</url-pattern>
</filter-mapping>
```

So the intended model is clear: all requests enter `AuthFilter`, and only authenticated sessions should reach dangerous action functions.

That was not what happened.

The reversing workflow was simple:

* unzip Db2Mirror.war
* inspect WEB-INF/web.xml
* decompile com.ibm.DB2Mirror.utils.AuthFilter
* decompile com.ibm.DB2Mirror.action.Db2MirrorServlet
* fall back to javap -p -c when CFR failed on the dispatcher
* grep action classes for request.getParameter(), FileInputStream, FileWriter, Trace.setFileName()

CFR failed to decompile `Db2MirrorServlet.doGet(Db2mHttpServletRequestWrapper, HttpServletResponse)` cleanly, but `javap -p -c` was enough. The bytecode showed the full reflection flow: read `function`, split the URI, build `com.ibm.DB2Mirror.action.<segment>`, instantiate the action with `(request, response)`, validate unless `skipVald` is set, then invoke the method.

That bytecode view was also useful because it showed where the validation check happened relative to reflection. The action class and method are resolved before validation. Validation only controls parameter content, not which action function can be selected.

## Bug 1: authentication based on the wrong path view

`AuthFilter` reads the raw request URI and splits it manually:

```
String requestURI = hRequest.getRequestURI();
String requestCtxPath = hRequest.getContextPath();
...
String[] rets = requestURI.split("/");
```

The security checks for the main servlet are only executed when the third segment equals `Db2MirrorServlet` exactly:

```
if (rets[2].equals("Db2MirrorServlet")) {
    if (!this.isAllowedWithoutSession(request.getParameter("function"))
        && !this.isAuthenticated(hSession)) {
        hResponse.sendError(401);
        return;
    }

    String buildTimeStampInRequest = hRequest.getHeader("BuildTimeStamp");
    if (Db2MirrorConfig.getInstance().getBuildTimeStamp() != null
        && !allowedServiceWithoutBuildTimeStamp.contains(request.getParameter("function"))
        && !Db2MirrorConfig.getInstance().getBuildTimeStamp().equalsIgnoreCase(buildTimeStampInRequest)) {
        hResponse.setHeader("Code", "BT");
        hResponse.sendError(403);
        return;
    }

    if (!allowedServiceWithoutMn.contains(request.getParameter("function"))
        && !this.isMnMatched(hRequest.getHeader("MN"), hSession)) {
        hResponse.setHeader("Code", "MN");
        hResponse.sendError(403);
        return;
    }
}
```

There are actually three protections in that block: authenticated session, build timestamp header, and the `MN` one-time value. All three depend on the same fragile `rets[2].equals("Db2MirrorServlet")` condition.

Servlet path parameters break the assumption. A request can include a semicolon parameter on the servlet path:

```
GET /Db2MirrorServlet;x/DbmConfigAction?function=getAppInitData HTTP/1.1
```

The filter sees segment 2 as:

```
Db2MirrorServlet;x
```

That does not equal `Db2MirrorServlet`, so the authentication block is skipped.

The servlet container still routes the request to `Db2MirrorServlet`, because the path parameter does not stop the servlet mapping from matching. Then the servlet’s own dispatcher strips the leading slash and splits the URI. With the deployed context path included, the servlet still obtains the action class from the next segment:

```
<context>/Db2MirrorServlet;x/DbmConfigAction
          ^ filter misses this          ^ servlet uses this as class
```

This is the first primitive: protected action methods can be reached without a valid GUI login, without the `BuildTimeStamp` header, and without a valid `MN` value.

The harmless proof was to call an initialization function and read the returned build metadata. The useful consequence was much broader: any action method that did not perform its own strong authorization became reachable.

The first request in the lab was intentionally boring:

```
GET /Db2MirrorServlet;x/DbmConfigAction?function=getAppInitData HTTP/1.1
Host: target
```

The expected unauthenticated response is a JSON response object containing application initialization data. A normal protected function without the semicolon path parameter returns 401 or 403 because the filter asks for the GUI session, build timestamp, and `MN` value.

Once this worked, the rest of the exploit stayed on the same pattern:

```
/Db2MirrorServlet;x/<ActionClass>?function=<methodName>&...
```

## Bug 2: the unauthenticated validation bypass switch

The next problem is that `AuthFilter` processes several debug/session options before the servlet-specific authentication check.

One of them is `skipVald`:

```
if ((skipVald = request.getParameter("skipVald")) != null) {
    LogWriter.trace("skipVald=" + skipVald);
    if (skipVald.equalsIgnoreCase("yes")
        || skipVald.equalsIgnoreCase("y")
        || skipVald.equalsIgnoreCase("true")) {
        AdminSession.currentSession(hSession).setSkipVald(true);
    } else if (skipVald.equalsIgnoreCase("false")
        || skipVald.equalsIgnoreCase("no")
        || skipVald.equalsIgnoreCase("n")) {
        AdminSession.currentSession(hSession).setSkipVald(false);
    }
}
```

`AdminSession.currentSession(hSession)` creates or retrieves an `AdminSession` object fo...