---
title: Chronicle Wire v2026.8 Arbitrary Class Instantiation During YAML Deserialization via Externally Controlled YAML Type Tags
url: https://seclists.org/fulldisclosure/2026/Aug/103
source: Full Disclosure
date: 2026-08-26
fetch_date: 2026-08-27T12:14:26.755646
---

# Chronicle Wire v2026.8 Arbitrary Class Instantiation During YAML Deserialization via Externally Controlled YAML Type Tags

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

[![Previous](/images/left-icon-16x16.png)](102)
[By Date](date.html#103)
[![Next](/images/right-icon-16x16.png)](104)

[![Previous](/images/left-icon-16x16.png)](102)
[By Thread](index.html#103)
[![Next](/images/right-icon-16x16.png)](104)

![](/shared/images/nst-icons.svg#search)

# Chronicle Wire v2026.8 Arbitrary Class Instantiation During YAML Deserialization via Externally Controlled YAML Type Tags

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sat, 22 Aug 2026 08:42:32 -0400

---

```
Chronicle Wire permits YAML type tags supplied within serialized input to
influence Java class selection and object instantiation during untyped
deserialization.

When applications deserialize attacker-controlled or otherwise untrusted
YAML through APIs such as readObject() or object(Object.class), an
externally controlled YAML type tag can identify a Java class that
Chronicle Wire resolves through its configured ClassLookup.

When the default permissive class lookup is used and the supplied class can
be resolved, the resulting class can propagate through Chronicle Wire's
generic object deserialization path and ultimately reach
ObjectUtils.newInstance(clazz). Chronicle Wire can then invoke the selected
class's deserialization lifecycle, including readMarshallable() where
applicable.

The security-sensitive behavior is therefore not limited to ordinary data
binding. Externally supplied serialized data can influence *which Java
class is instantiated during deserialization*.

The accompanying proof of concept confirms that:

   - An externally controlled YAML type tag selects the Java class
   instantiated by readObject().
   - The selected class's constructor is executed.
   - A selected class's readMarshallable() implementation is automatically
   invoked during deserialization.
   - An existing third-party class already present on the runtime classpath
   can be instantiated using a YAML type tag.
   - Configuring a restrictive ClassLookup prevents the demonstrated
   arbitrary class selection.

The practical security impact depends on the classes available on the
target application's classpath and whether untrusted YAML reaches an
affected untyped deserialization API. The PoC establishes the arbitrary
class-selection and instantiation primitive but does not claim universal
arbitrary code execution.
Vulnerability Details

Chronicle Wire supports YAML type tags capable of identifying Java classes
during deserialization.

For example:

!fully.qualified.ClassName

The parser does not treat this value solely as descriptive metadata. The
supplied class name is resolved using the wire's configured ClassLookup.

The default wire configuration initializes the lookup using the global
alias pool:

protected ClassLookup classLookup =
    ClassAliasPool.CLASS_ALIASES;

When a YAML TAG token is encountered, the supplied type is resolved:

Class<?> typePrefix() {
    ...
    return classLookup().forName(stringBuilder);
}

The class represented by the serialized YAML can therefore influence the
Java type selected during deserialization.

In affected object-reading paths, Chronicle Wire can subsequently
instantiate the resolved class:

Class<?> clazz = typePrefix();

if (clazz != object.getClass())
    object = ObjectUtils.newInstance(clazz);

The externally selected type can also propagate into the generic object
deserialization path:

Object o = typePrefixOrObject(clazz);

...

t = Wires.object2(..., (Class) o);

Within Wires.object2(), the type supplied by serialized input can replace
the caller's original type under several conditions:

if (clazz == null
        || clazz.isAssignableFrom(clazz2)
        || ReadResolvable.class.isAssignableFrom(clazz2)
        || !ObjectUtils.isConcreteClass(clazz))
{
    clazz = clazz2;
}

Chronicle Wire can then instantiate the selected class:

if (o == null)
    o = ObjectUtils.newInstance(clazz);

and continue the object's deserialization lifecycle:

Wires.readMarshallable(
    clazz,
    o,
    in.wireIn(),
    true);

As a result, when permissive class resolution is available, externally
controlled YAML can influence both the class instantiated by Chronicle Wire
and the class-specific deserialization logic subsequently executed.
Root Cause

The root cause is the use of serialized YAML type information to select
Java classes during generic or untyped object deserialization without a
mandatory deny-by-default class allow-list.

Chronicle Wire resolves externally supplied YAML type tags through its
configured ClassLookup. When the default permissive lookup permits the
requested type, the resulting class can propagate into generic object
deserialization and reach ObjectUtils.newInstance().

The security boundary becomes particularly important when an application
performs operations such as:

TextWire.from(untrustedYaml).readObject();

or equivalent untyped deserialization.

In this situation, the application is not exclusively determining the Java
class being constructed. The serialized YAML participates in that decision.

A restrictive ClassLookup can prevent arbitrary class resolution, but such
a restriction is not inherent to the demonstrated default deserialization
path.
Proof of Concept Results

The security test suite successfully reproduced multiple independent paths
in which serialized type information caused Chronicle Wire to instantiate
classes selected through the supplied Wire/YAML data.

The tests completed successfully with no failures or errors:

[INFO] Running net.openhft.chronicle.wire.SecurityAdditionalPoCTest

[INFO] Tests run: 13, Failures: 0, Errors: 0, Skipped: 0

[INFO] BUILD SUCCESS

Direct Tagged Class Instantiation

The PoC confirmed that Chronicle Wire resolves a supplied YAML type tag and
instantiates the corresponding Java class during deserialization.

Observed result:

WireObjectInput.readObject instantiated tagged class:
net.openhft.chronicle.wire.SecurityAdditionalPoCTest$AdditionalTypedPathProbe

This confirms that the class encoded in serialized input is not merely
parsed as metadata. The resolved type reaches object construction and
results in an instance of the tagged class.
Map Value Type Instantiation

The same externally controlled type-selection behavior was reproduced while
deserializing a typed value contained within a map.

Observed result:

Map value read instantiated tagged class:
net.openhft.chronicle.wire.SecurityAdditionalPoCTest$AdditionalTypedPathProbe

This demonstrates that the behavior is not limited to a single top-level
readObject() operation. Typed serialized values encountered within other
object-reading paths can also cause tagged classes to be instantiated.
File-Based Typed Deserialization

The PoC additionally confirmed arbitrary class instantiation when typed
serialized data is loaded from a caller-controlled file.

The test file contained:

!net.openhft.chronicle.wire.SecurityAdditionalPoCTest$FilePathProbe {
    marker: from-file
}

The test output confirmed the exact payload written to the file:

WireType.fromFile payload written BEGIN
!net.openhft.chronicle.wire.SecurityAdditionalPoCTest$FilePathProbe {
marker: from-file }
WireType.fromFile payload written END

Chronicle Wire subsequently instantiated the class identified by the
serialized type tag:

WireType.fromFile instantiated tagged class:
net.openhft.chronicle.wire.SecurityAdditionalPoCTest$FilePathProbe

This provides an additional concrete deserialization path where serialized
type information determines the Java class inst...