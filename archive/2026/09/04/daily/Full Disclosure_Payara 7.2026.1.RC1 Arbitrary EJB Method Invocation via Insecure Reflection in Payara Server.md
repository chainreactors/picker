---
title: Payara 7.2026.1.RC1 Arbitrary EJB Method Invocation via Insecure Reflection in Payara Server
url: https://seclists.org/fulldisclosure/2026/Sep/18
source: Full Disclosure
date: 2026-09-04
fetch_date: 2026-09-05T06:30:33.926013
---

# Payara 7.2026.1.RC1 Arbitrary EJB Method Invocation via Insecure Reflection in Payara Server

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

[![Previous](/images/left-icon-16x16.png)](17)
[By Date](date.html#18)
[![Next](/images/right-icon-16x16.png)](19)

[![Previous](/images/left-icon-16x16.png)](17)
[By Thread](index.html#18)
[![Next](/images/right-icon-16x16.png)](19)

![](/shared/images/nst-icons.svg#search)

# Payara 7.2026.1.RC1 Arbitrary EJB Method Invocation via Insecure Reflection in Payara Server

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sun, 30 Aug 2026 19:50:19 -0400

---

```
Payara Server exposes multiple HTTP-accessible EJB invocation mechanisms
that rely on attacker-controlled reflection, dynamic class loading, and
unsafe deserialization. These endpoints allow remote clients to perform
arbitrary JNDI lookups, resolve attacker-supplied class names, and invoke
EJB business methods via reflection without sufficient authorization
enforcement or input restriction.

Both the deprecated InvokeEJBServlet and the EjbOverHttpResource
(EJB-over-HTTP JAX-RS endpoint) implement the same insecure design pattern:
user-controlled inputs are used to select classes, methods, parameter
types, and argument values, which are then executed reflectively inside the
application context. Deprecation does not disable or mitigate the exposure,
leaving a powerful remote invocation surface reachable in production
deployments.

Affected Components

   -

   *EJB-over-HTTP JAX-RS Resource*
   -

      Class: fish.payara.ejb.http.endpoint.EjbOverHttpResource
      -

      Paths:
      -

         /jndi/lookup
         -

         /jndi/invoke
         -

      Media Types: JSON / Java Serialization
      -

      Technology: JAX-RS / EJB / JNDI / Reflection / JSON-B
      -

   *Deprecated HTTP Servlet*
   -

      Component: fish.payara.ejb.invoke.InvokeEJBServlet
      -

      Servlet Mapping: /ejb/*
      -

      Status: Deprecated but registered, reachable, and functional

Affected Versions

   -

   Payara Server versions that include and expose either:
   -

      InvokeEJBServlet, or
      -

      EjbOverHttpResource

*Vulnerability Details:*
The affected endpoints perform a series of insecure operations that
collectively expose a powerful reflection-based invocation surface.
User-supplied jndiName values are passed directly to InitialContext.lookup,
and the application context is dynamically switched based on parsed JNDI
input, enabling access to arbitrary EJBs within the target application and,
in some cases, across application boundaries. Once a target EJB is
resolved, attacker-controlled method names and parameter type names are
processed using Java reflection, and Method.invoke() is executed on EJB
proxies without any allowlisting, capability checks, or restriction to
intended business methods. In parallel, parameter and return types are
resolved using Class.forName() with the application’s class loader,
allowing resolution of any class visible within the application context.
User-supplied JSON payloads are then deserialized via JSON-B into
attacker-chosen target types, creating a generic deserialization sink that
feeds directly into the reflective invocation flow. Authentication is
optional and controlled by the client, while authorization failures do not
consistently terminate execution, allowing invocation logic to continue
after partial or failed security checks. Finally, detailed reflection and
invocation errors, such as NoSuchMethodException, are returned verbatim to
the client, disclosing internal EJB proxy class names, interface
structures, and method resolution behavior, which enables method and
interface enumeration and facilitates further exploitation.

*Impact:*
A remote attacker may be able to:

   - Invoke arbitrary EJB business methods
   - Access EJBs outside the intended application scope
   - Bypass or weaken authorization controls
   - Abuse JSON-B deserialization with attacker-chosen target types
   - Enumerate internal classes, interfaces, and method signatures
   - Trigger sensitive or administrative application functionality
   - Potentially achieve remote code execution, depending on reachable
   methods and classes
   - The exposure of a generic reflection-based invocation primitive
   significantly increases the attack surface of affected Payara deployments.

*Vulnerable Code — EjbOverHttpResource:*
*Attacker-Controlled JNDI Lookup*
Object bean = service.getBean(jndiName);

*Application Context Switching Based on User Input*
String applicationName = jndiName.substring(12, jndiName.indexOf('/', 12));
ClassLoader appClassLoader = service.getAppClassLoader(applicationName);
Thread.currentThread().setContextClassLoader(appClassLoader);

*Externally Controlled Class Resolution*
Class.forName(name, true, Thread.currentThread().getContextClassLoader());

*Reflection-Based Method Resolution*
Method method = findBusinessMethodDeclaration(
    ejb,
    request.method,
    argTypes
);

*Reflection-Based Method Invocation*
Object result = method.invoke(
    ejb,
    request.argDeserializer.deserialise(
        request.argValues,
        method,
        argActualTypes,
        Thread.currentThread().getContextClassLoader()
    )
);

*Unsafe JSON-B Serialization / Type Handling*
JsonbBuilder.create().toJson(result.result, returnType, output);

*Information Disclosure via Reflection Errors*
throw new NoSuchMethodException(
    "No method matching " + methodName + "(" +
    Arrays.toString(argTypeClasses) + ") found"
);

*Vulnerable Code — InvokeEJBServlet (Deprecated but Active):*

*Attacker-Controlled JNDI Lookup (Direct & Cross-Application)*
Object bean = new InitialContext().lookup(beanName);
*And the cross-application fallback:*
for (String applicationName : registry.getAllApplicationNames()) {

currentThread.setContextClassLoader(registry.get(applicationName).getAppClassLoader());
    Object bean = new InitialContext().lookup(beanName);
    return operation.execute(bean);
}

*Application Context Switching Based on User Input*
String applicationName = beanName.substring(12, beanName.indexOf('/', 12));
currentThread.setContextClassLoader(
    registry.get(applicationName).getAppClassLoader()
);

*Externally Controlled Class Resolution*
Class.forName(className, true,
Thread.currentThread().getContextClassLoader());
(from toClass())
private static Class<?> toClass(JsonValue classNameValue) {
    String className = ((JsonString) classNameValue).getString();
    return Class.forName(className, true,
        Thread.currentThread().getContextClassLoader());
}

*Reflection-Based Method Resolution Using Attacker Input*
this.method = findBusinessMethodDeclaration(methodName, argTypeClasses);
return intf.getMethod(methodName, argTypeClasses);

*Reflection-Based Method Invocation*
this.result = method.invoke(bean, argValues);
(from Invocation.invoke())

*Unsafe JSON-B Deserialization into Attacker-Chosen Types*
return jsonb.fromJson(objectValue.toString(), type);
(from toObject())
argValues[i] = toObject(jsonArgValues.get(i), argTypes[i]);
(from toObjects())

*Broken Authorization Enforcement (Execution Continues)*
if (!request.isUserInRole(role)) {
    response.setStatus(HttpServletResponse.SC_FORBIDDEN);
}

*Information Disclosure via Reflection Errors*
throw new NoSuchMethodException(
    "No method matching " + methodName + "(" +
    Arrays.toString(argTypeClasses) + ") found in business interface"
);
And error propagation:
response.sendError(
    SC_INTERNAL_SERVER_ERROR,
    "Error while invoking invoking method " + methodName +
    " on EJB with name " + beanName + ": " + ex.get...