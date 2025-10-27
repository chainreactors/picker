---
title: Jasper Reports Library Code Injection
url: https://buaq.net/go-168594.html
source: unSafe.sh - 不安全
date: 2023-06-14
fetch_date: 2025-10-04T11:44:43.877537
---

# Jasper Reports Library Code Injection

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/2ab422bb9ad4759ef5798ef5b7f300d5.jpg)

Jasper Reports Library Code Injection

During the past year we had several projects where our target application used Jasper Repo
*2023-6-13 22:8:10
Author: [insinuator.net(查看原文)](/jump-168594.htm)
阅读量:43
收藏*

---

During the past year we had several projects where our target application used [Jasper Reports](https://community.jaspersoft.com/) in some way. In a few of the cases we found an API that offered to render a template along with some arguments into a PDF file. This was done with the help of the Jasper Reports Java library. Due to the way the library and the expression mechanism works, this endpoint gave us the possibility to inject Java code and gain remote code execution on the target systems.

In this blog post we want to provide an overview over the Jasper Reports Java library in terms of security especially with regard to expression injection attacks.

**TL;DR;** If you come across an API that lets you freely define a Jasper Report template you very likely have code execution. Or to put it differently: Never let Jasper Report templates be user or attacker controlled.

## What are Jasper Reports?

Jasper Reports is a reporting software that comes in various forms. A [Report Designer GUI](https://community.jaspersoft.com/project/jaspersoft-studio), a [server component](https://community.jaspersoft.com/project/jasperreports-server), and the [Java library](https://community.jaspersoft.com/project/jasperreports-library). There are a few more, but for this post the only relevant component is the Java library.

According to its [website](https://community.jaspersoft.com/project/jasperreports-library), Jasper Reports *“is the world’s most popular open source reporting engine”*. The usage is described as being *“able to use data coming from any kind of data source and produce pixel-perfect documents that can be viewed, printed or exported in a variety of document formats including HTML, PDF, Excel, OpenOffice and Word”*

Templating and reporting engines in general are often prone to (template) injection attacks, so when we first encountered Jasper Reports we were immediately curious.

There is some previous work on Jasper Reports. *Foxglovesecurity* described in a [blog post](https://foxglovesecurity.com/2016/10/14/hacking-jasperreports-the-hidden-shell-feature/) how to compromise the Jasper Reports server component using *Scriptlets*. There is also a [GitHub gist](https://gist.github.com/v-p-b/dd95c72c6924dc1338e78e9d380bd388) that contains a Jasper Report template JRXML file that leads to Java Code execution. The issue is essentially the same as the one we found during one of our penetration tests. [This blog post](https://depthsecurity.com/blog/exploiting-custom-template-engines) also briefly mentions the issue. The blog post and the Gist are more than four years old, but the issue exists to this day.

Jasper Reports offer a wide variety of features and APIs. In this blog post we’re only going into the parts that are relevant for gaining code execution via template expressions. This is by no means a proper security assessment of the library. Moreover, we really only examined the parts that were relevant for the exploitation, so the features we’re showing are only a very small subset of what Jasper Reports can do.

## Jasper Report Creation

Imagine a REST endpoint, `/render-xml-template`, that accepts a template and optional parameters and returns a rendered PDF file. This involves loading and deserializing the template into a `JasperDesign` object. The format of the template can either be an XML file, typically with the ending `.jrxml`, or a serialized Java object (in form of a `.jasper`) file.

This `JasperDesign` object is then compiled into a `JasperReport` object. Before rendering or exporting it into a target format, it can be filled with parameters. A template can define *named parameters* that can be references inside the template. The `JasperFillManager` takes the compiled report as well as a dictionary of parameters and fills the report accordingly.

In the end, the `JasperReportManager` can be used to export the filled report to a PDF file.

With a Java Spring endpoint, the whole process may look as follows:

```
@PostMapping(value="/render-xml-template", consumes = MediaType.
             APPLICATION_JSON_VALUE, produces = MediaType.APPLICATION_PDF_VALUE)
public ResponseEntity<byte[]> renderXMLTemplate(@RequestBody
                                                RenderTemplateRequest req)
                                                throws JRException {
    // Decode template from base64
    byte[] templateXMLBytes = Base64.getDecoder().decode(req.getTemplate());

    // Load template and compile to report
    JasperDesign design = JRXmlLoader.load(new ByteArrayInputStream(
                          templateXMLBytes));
    JasperReport rep = JasperCompileManager.compileReport(design);

    // Decode and set the template's parameters
    HashMap<String, Object> new_params = new HashMap<String, Object>(req.
                                         getParameters());
    JasperPrint print = JasperFillManager.fillReport(rep, new_params, new
                        JREmptyDataSource());

    // Export template to PDF
    ByteArrayOutputStream out = new ByteArrayOutputStream();
    JasperExportManager.exportReportToPdfStream(print, out);

    HttpHeaders headers = new HttpHeaders();
    headers.setContentType(MediaType.APPLICATION_PDF);
    headers.setContentDispositionFormData("report.pdf", "report.pdf");
    ResponseEntity<byte[]> response = new ResponseEntity<>(out.toByteArray(),
                                      headers, HttpStatus.OK);

    return response;
}
```

We accept a JSON POST body that contains a base64-encoded Jasper template as well as a dictionary with template parameters. The template is decoded and parsed into the `JasperDesign` object using the `JRXmlLoader.load()` method. Afterwards it is compiled using the `JasperCompileManager`. The provided parameters are then filled in the template using the `JasperFillManager`. Lastly, the PDF output stream is created and returned in the HTTP response.

An example POST request may look as follows:

```
POST /render-xml-template HTTP/1.1
Content-Type: application/json
Host: localhost

{
    "parameters": {
        "param1": "something",
        "param2": 123
    },
    "template": "ZHVtbXkgY29udGVudCwgbm90IHhtbCA6KQo="
}
```

This is a very simplified version of what we have seen during our engagements in the past. If you are ever in such a situation, you’ll likely be able to execute arbitrary code.

To understand why, let’s look closer into what these templates look like.

## Jasper Report Templates

As mentioned before, Jasper Report templates can come in different formats. A more or less human-readable XML version – the JRXML files, or the binary serialized `.jasper` files. The information encoded in these files is pretty much the same. It’s also possible to convert the formats into each other. For purposes of readability, we will focus on XML files here. Functionally and from a point of view of exploitability the two representations are equal in all relevant aspects to the best of our knowledge.

Below is an excerpt of one of the example template files [FirstJasper.jrxml](https://github.com/TIBCOSoftware/jasperreports/blob/master/jasperreports/demo/samples/jasper/reports/FirstJasper.jrxml).

```
<?xml version="1.0" encoding="UTF-8"?>
<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports" ..>
    ...
    <parameter name="ReportTitle"...