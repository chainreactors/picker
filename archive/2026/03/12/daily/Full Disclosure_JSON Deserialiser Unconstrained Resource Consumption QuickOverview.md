---
title: JSON Deserialiser Unconstrained Resource Consumption Quick	Overview
url: https://seclists.org/fulldisclosure/2026/Mar/6
source: Full Disclosure
date: 2026-03-12
fetch_date: 2026-03-13T04:08:09.860298
---

# JSON Deserialiser Unconstrained Resource Consumption Quick	Overview

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

[![Previous](/images/left-icon-16x16.png)](5)
[By Date](date.html#6)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](5)
[By Thread](index.html#6)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# JSON Deserialiser Unconstrained Resource Consumption Quick Overview

---

*From*: Daniel Owens via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Sat, 7 Mar 2026 05:45:20 +0000

---

```
As previously mentioned, via "Struts2 and Related Framework Array/Collection DoS" (26 October 2025), hundreds of
JavaScript object notation (JSON) libraries are vulnerable to unconstrained resource consumption through large JSON
arrays, which, when deserialised, create arbitrarily large collections/arrays/data structures.  This work looks
specifically at the Apache Struts2 JSON Plugin, using it as an example for why this vulnerability exists, how to
exploit it.

Understanding Deserialisation
There are, regardless of the library, language, three methods of deserialisating data:

  1.  Call constructors
  2.  Call setters
  3.  Set the variable directly

Most systems opt for #2, at least by default, and for a variety of reasons.  By leveraging setters (and serialisation
then often uses getters), the deserialiser needn't reflect into non-public or static structures - they simply use the
default constructor to create the base object, then call to the referenced or mapped public methods.  This means that
the deserialiser, which has to use reflection as part of the process (even if that reflection is obscured - there are
exceptions but they are not relevant to this discussion and, even then, almost always still have reflection, even if
outside of the purview of the purported library), doesn't need to allow reflection to override visibility or allow
static references, either of which open the system up to a large number of attacks.  While option #1 also can allow the
same "safer" reflection than option #3, it creates "bloat" with complex constructors, multiple constructors just to
rehydrate an object, so is less favoured by both developers picking a deserialiser and individuals writing the
deserialisers.  Option #3 requires the variables to be either directly exposed as public variables, which makes race
conditions and other issues more likely, gives up control over the variable and shaping it (e.g., performing input
validation, sanitisation, and escaping as it flows into the object), etc., or requires the deserialiser to allow
reflecting into private variables, which makes the deserialiser a massive target.

Both Struts2 and the Struts2 JSON Plugin prefer to use setters and getters for the deserialisation/serialisation
process (notably, a deserialiser need not include a serialiser and vice versa).

The Flow
When a user makes a request to Apache Struts2, the data flows through the StrutsPrepareAndExecuteFilter to all
applicable ServletFilters, then to the ActionMapper, the ActionProxy, all configured Interceptors, and eventually to
the mapped Action.  The deserialisers - be they the default Apache Struts2 deserialiser, the Apache Struts2 JSON
Plugin, or something else - are interceptors.  To help the reader visualise and understand this dataflow, we have
created the sequence diagram below.

[cid:image005.png@01DCADCB.ACA14A10]

The Apache Struts2 JSON Plugin, itself, is composed of multiple classes, but the classes of importance for this
discussion are the JSONInterceptor, JSONUtil, JSONReader, and JSONPopulator.  The following is a high-level diagram
showing the data flow of interest for this discussion - specifically focusing on deserialisation of JSON arrays as the
JSON flows through the library.

[cid:image006.png@01DCADCB.ACA14A10]

Vulnerable Code
The vulnerable code, in this example, is contained within JSONReader, which is responsible for rehydration of the JSON
string into either a Map or a List, which is then bubbled up to the JSONUtil, returned to the JSONInterceptor (via
Object obj = JSONUtil.deserialize(request.getReader())), translated into a Map if it is a list, and then the Map is
passed to the JSONPopulator, which is nothing more than a standard reflective layer that builds the objects, sets the
variables using the default constructor to instantiate objects and setters (if it can find them) to set the variables.
Below is some of the offending code that is vulnerable to trivial resource exhaustion, from JSONReader:

   protected List array() throws JSONException {
        List ret = new ArrayList();
        Object value = this.read();
        while (this.token != ARRAY_END) {
            ret.add(value);
            Object read = this.read();
            if (read == COMMA) {
                value = this.read();
            } else if (read != ARRAY_END) {
                throw buildInvalidInputException();
            }
        }
        return ret;
    }

Notably, this method foolishly will keep reading until it reaches a JSON array terminator -- `]`.  Attackers can, as
such, simply send large arrays and the reader will continuously create new Java Object instances and add them to the
`ret` ArrayList.  The protected Map object() method suffers similarly, endlessly adding Object instances to the `ret`
HashMap.  In fact, this paradigm is peppered throughout this code and that of, again, literally hundreds of JSON
deserialisers.

There are a few things to understand about why this is dangerous.

First, from a language-specific perspective, ArrayList and HashMap experience automatic growth and both default to a
rather small capacity (10 and 16, respectively) and grow rather quickly (~50% and ~100% capacity increase,
respectively).  HashMap growth triggers when the size (number of elements in the instance) exceeds the threshold
(capacity * loadfactor, or put another way, capacity * 0.75).  ArrayList grows only when one more element is added than
it has capacity.  The growth operation for both is O(n), where n is the number of elements, but the memory impact is
far greater than the compute, which, itself becomes sizable quickly, since the memory must be allocated for the new
data structure while the old still exists - for a HashMap, that means that you go from n to 3n, since the size doubles
(2n) but the original is still in memory during the copy operation.  For an ArrayList, it is closer to 2.5 - the size
increases to 1.5n and the original n remain in memory during the copy operation.  Of course, on top of this, you have
garbage collection, so the old data structures - which are simply arrays - remain until they are cleaned up.

Outside of the language-specific perspective, attackers can simply create arbitrarily large JSON arrays and, even if
simply null, they will result in stuffing entries into data structures.  Attackers can simply exhaust memory,
especially if they run just a few concurrent instances of malicious requests.  Even if attackers cannot exhaust memory,
they can exhaust compute - the information system must parse the entire array, must build out the data structure, must
then map the data structure out, and must then attempt to stuff the data into the rehydrated object.

In this way, the attack operates to target both processor and memory of the victim system and has been used to
successfully bring down hundreds of thousands of information systems within seconds and with just a few requests.

The Attack
Much like a "ping of death", "zip bomb", or related non-volumetric denial of service attack, the...