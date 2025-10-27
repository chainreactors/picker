---
title: Reflected XSS vulnerabilities in Squidex &quot;/squid.svg&quot; endpoint
url: https://census-labs.com/news/2023/03/16/reflected-xss-vulnerabilities-in-squidex-squidsvg-endpoint/
source: CENSUS
date: 2023-03-17
fetch_date: 2025-10-04T09:53:43.003395
---

# Reflected XSS vulnerabilities in Squidex &quot;/squid.svg&quot; endpoint

[![CENSUS | Cybersecurity Engineering](/static/assets/img/logos/logo.png)](/)

[CONTACT](/contact)

* [BLOG](/news/category/blog/)
* [ADVISORIES](/news/category/advisories/)
* [CAREERS](/openings/)
* [INTERNSHIP](/internship/)

* [INDUSTRIES](/industries/)
* [CAPABILITIES](/capabilities/)
* [SOLUTIONS](/solutions/)
* [LABS](/labs/)
* [COMPANY](/census/)

POSTED BY:
[Ioannis Christodoulakos](/cdn-cgi/l/email-protection#c4a3a7acb6adb7b0aba0abb1a8a5afabb784a7a1aab7b1b7e9a8a5a6b7eaa7aba9)
/
16.03.2023

# Reflected XSS vulnerabilities in Squidex "/squid.svg" endpoint

|  |  |
| --- | --- |
| CENSUS ID: | CENSUS-2023-0001 |
| CVE ID: | [CVE-2023-24278](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24278) |
| Affected Products: | [Squidex](https://squidex.io/) versions prior to 7.4.0 |
| Class: | Improper Neutralization of Input During Web Page Generation ([CWE-79](https://cwe.mitre.org/data/definitions/79.html)) |
| Discovered by: | Ioannis Christodoulakos |

CENSUS has discovered two reflected cross site scripting (XSS) vulnerabilities in the Squidex open source headless CMS software. The Reflected Cross Site Scripting vulnerabilities affect all versions of Squidex prior to 7.4.0 and affect both authenticated and unauthenticated victim users. The Squidex development team has addressed the issues in version 7.4.0 of the software.

## Vulnerability Details CENSUS identified two Reflected XSS (Cross-site scripting) vulnerabilities affecting the [Squidex](https://squidex.io/) "headless" CMS framework, during an application security assessment of a web application based on Squidex. These vulnerabilities enable attackers to embed malicious JavaScript code into a link and have the malicious code be executed within a victim user's browser when the victim user clicks the malicious link. The flaws affect the "/squid.svg" endpoint, which is accessible to both authenticated and unauthenticated users. Attackers may employ these vulnerabilities to extract the CMS token from the browser's local storage, allowing them to take control of the user's CMS session. The vulnerabilities affect versions prior to Squidex 7.4.0. CENSUS has confirmed this to be the case for versions 5.0.0 and 6.8.0. The issue stems from the fact that the application fails to embed user-supplied data as text in an auto-generated SVG image, allowing for the introduction of arbitrary SVG elements, including elements that may include malicious JavaScript code. The user-supplied data are passed to the "/squid.svg" endpoint through a GET request requiring no authentication. Malicious code passed as a parameter to this endpoint, is "reflected" back to the visitor's browser, thus allowing an attacker to execute arbitrary JavaScript code on victim browsers through the distribution of a malicious URL. The vulnerable code in question is shown below: ``` // File: backend/src/Squidex/Pipeline/Squid/SquidMiddleware.cs ... public sealed class SquidMiddleware { ... private static (string, string, string) SplitText(string text) { var result = new List(); var line = new StringBuilder(); foreach (var word in text.Split(' ')) { if (line.Length + word.Length > 16 && line.Length > 0) { result.Add(line.ToString()); line.Clear(); } line.AppendIfNotEmpty(' '); line.Append(word); } result.Add(line.ToString()); while (result.Count < 3) { result.Add(string.Empty); } return (result[0], result[1], result[2]); } public async Task InvokeAsync(HttpContext context) { var request = context.Request; ... if (request.Query.TryGetValue("title", out var titleValue) && !string.IsNullOrWhiteSpace(titleValue)) { title = titleValue; } var text = "text"; if (request.Query.TryGetValue("text", out var textValue) && !string.IsNullOrWhiteSpace(textValue)) { text = textValue; } var background = isSad ? "#F5F5F9" : "#4CC159"; if (request.Query.TryGetValue("background", out var backgroundValue) && !string.IsNullOrWhiteSpace(backgroundValue)) { background = backgroundValue; } ... var (l1, l2, l3) = SplitText(text); svg = svg.Replace("{{TITLE}}", title.ToUpperInvariant(), StringComparison.Ordinal); svg = svg.Replace("{{TEXT1}}", l1, StringComparison.Ordinal); svg = svg.Replace("{{TEXT2}}", l2, StringComparison.Ordinal); svg = svg.Replace("{{TEXT3}}", l3, StringComparison.Ordinal); svg = svg.Replace("[COLOR]", background, StringComparison.Ordinal); context.Response.StatusCode = 200; context.Response.ContentType = "image/svg+xml"; context.Response.Headers["Cache-Control"] = "public, max-age=604800"; await context.Response.WriteAsync(svg, context.RequestAborted); } ... ``` In the above code snippet in method InvokeAsync() the **text** user-supplied parameter is being split into three lines, via SplitText(), and is then embedded "as is" into the generated SVG image, thus allowing for SVG markup injection. Moreover, the **background** user-supplied parameter is simply copied "as is" to the generated SVG image, again allowing for SVG markup injection. Finally, the "title" is also a user-supplied parameter, however due to it being transformed to uppercase one would not be able to inject malicious JavaScript code (due to the case-sensitive nature of SVG tags). Therefore, it is possible for an attacker to conduct a reflected XSS attack by abusing either the **text** or **background** parameters (or both). The example below demonstrates a reflected XSS attack via the **background** parameter: ``` GET /squid.svg?title=Not%20Found&text=This%20is%20not%20the%20page%20you%20are%20looking%20for!&background=%22%3E%3Cscript%3Ealert(1)%3C/script%3E%3Cimg%20src=%22&small HTTP/2 [...] HTTP/2 200 OK Content-Type: image/svg+xml [...] <svg id="Layer_1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 391.9"> [...] <path d="M349 [...] 67.5-3.8z" fill=""><script>alert(1)</script><img src=""/> <text transform="translate(97.559 104.938)" letter-spacing="1" class="st6 st71" fill="#4cc159"> NOT FOUND </text> <text transform="translate(97.559 147.894)"> <tspan x="0" y="00" class="st5 st6 st70">This is not the</tspan> <tspan x="0" y="28" class="st5 st6 st70">page you are</tspan> <tspan x="0" y="56" class="st5 st6 st70">looking for!</tspan> </text> [...] </svg> ``` [CVE-2023-24278](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24278) has been assigned to these vulnerabilities. Recommendation It is highly recommended to upgrade to version 7.4.0 of Squidex or newer to mitigate the aforementioned vulnerabilities. Disclosure Timeline | | | | --- | --- | | Vendor Contact: | July 7, 2022 | | Vendor Confirmation: | Janurary 12, 2023 | | Vendor Fix Released: | February 1, 2023 | | CVE Allocation: | February 25, 2023 | | Public Advisory: | March 16, 2023 | * Tags: [XSS](/news/tag/xss/) , [code injection](/news/tag/code-injection/) , [advisories](/news/tag/advisories/) , [squidex](/news/tag/squidex/) , [SVG](/news/tag/svg/) , [reflected XSS](/news/tag/reflected-xss/) Share this * [X](https://x.com/census_labs) * [email](/cdn-cgi/l/email-protection#90afb6e3e5f2faf5f3e4adc2f5f6fcf5f3e4f5f4b5a2a0c8c3c3b5a2a0e6e5fcfef5e2f1f2f9fcf9e4f9f5e3b5a2a0f9feb5a2a0c3e1e5f9f4f5e8b5a2a0b5a2a2bfe3e1e5f9f4bee3e6f7b5a2a2b5a2a0f5fef4e0fff9fee4b6f2fff4e9adb5a3d3e4f1f2fcf5b5a3d5b5a0d4b5a0d1b5a3d3e4f2fff4e9b5a3d5b5a0d4b5a0d1b5a3d3e4e2b5a3d5b5a3d3e4f4b5a3d5d3d5dec3c5c3b5a2a0d9d4b5a3d1b5a3d3bfe4f4b5a3d5b5a3d3e4f4b5a3d5d3d5dec3c5c3bda2a0a2a3bda0a0a0a1b5a3d3bfe4f4b5a3d5b5a3d3bfe4e2b5a3d5b5a0d4b5a0d1b5a3d3e4e2b5a3d5b5a3d3e4f4b5a3d5d3c6d5b5a2a0d9d4b5a3d1b5a3d3bfe4f4b5a3d5b5a3d3e4f4b5a3d5b5a3d3f1b5a2a0f8e2f5f6b5a3d4b5a2a2f8e4e4e0e3b5a3d1bfbff3e6f5befdf9e4e2f5beffe2f7bff3f7f9bdf2f9febff3e6f5fef1fdf5bef3f7f9b5a3d6fef1fdf5b5a3d4d3c6d5bda2a0a2a3bda2a4a2a7a8b5a2a2b5a3d5d3c6d5bda2a0a2a3bda2a4a2a7a8b5a3d3bff1b5a3d5b5a3d3bfe4f4b5a3d5b5a3d3bfe4e2b5a3d5b5a0d4b5a0d1b5a3d3e4e2b5a3d5b5a3d3e4f4b5a3d5d1f6f6f5f3e4f5f4b5a2a0c0e2fff4e5f3e4e3b5a3d1b5a3d3bfe4f4b5a3d5b5a3d3e4f4b5a3d5b5a3d3f1b5a2a0f8e2f5f6b5a3d4b5a2a2f8e4e4e0e3b5a3d1bfbfe3e1e5f9f4f5e8bef9ffbfb5a2a2b5a3d5c3e1e5f9f4f5e8b5a3d3bff1b5a3d5b5a2a0e6f5e2e3f9fffe...