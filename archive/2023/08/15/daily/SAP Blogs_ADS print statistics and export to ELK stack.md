---
title: ADS print statistics and export to ELK stack
url: https://blogs.sap.com/2023/08/14/ads-print-statistics-and-export-to-elk-stack/
source: SAP Blogs
date: 2023-08-15
fetch_date: 2025-10-04T12:01:38.219122
---

# ADS print statistics and export to ELK stack

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* ADS print statistics and export to ELK stack

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/164940&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [ADS print statistics and export to ELK stack](/t5/technology-blog-posts-by-members/ads-print-statistics-and-export-to-elk-stack/ba-p/13578060)

![platinumicef](https://avatars.profile.sap.com/5/5/id55072126e8a0e5e108c7f280116b0618c30c782a4e5bf5f84b17ab4e07be7e06_small.jpeg "platinumicef")

[platinumicef](https://community.sap.com/t5/user/viewprofilepage/user-id/353185)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=164940)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/164940)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13578060)

‎2023 Aug 15
12:32 AM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/164940/tab/all-users "Click here to see who gave kudos to this post.")

1,676

* SAP Managed Tags
* [SAP Forms service by Adobe](https://community.sap.com/t5/c-khhcw49343/SAP%2520Forms%2520service%2520by%2520Adobe/pd-p/73555000100800000066)
* [NW AS Java Administrator (NWA)](https://community.sap.com/t5/c-khhcw49343/NW%2520AS%2520Java%2520Administrator%2520%28NWA%29/pd-p/350991270579841525753072979612318)
* [SAP Interactive Forms by Adobe](https://community.sap.com/t5/c-khhcw49343/SAP%2520Interactive%2520Forms%2520by%2520Adobe/pd-p/582573882271271216439685697820265)

* [SAP Forms service by Adobe

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BForms%2Bservice%2Bby%2BAdobe/pd-p/73555000100800000066)
* [NW AS Java Administrator (NWA)

  Software Product Function](/t5/c-khhcw49343/NW%2BAS%2BJava%2BAdministrator%2B%252528NWA%252529/pd-p/350991270579841525753072979612318)
* [SAP Interactive Forms by Adobe

  Software Product Function](/t5/c-khhcw49343/SAP%2BInteractive%2BForms%2Bby%2BAdobe/pd-p/582573882271271216439685697820265)

View products (3)

Observability is a key to a successful long-term maintenance of any system. One of the aspects that we considered worth monitoring in our landscape was Adobe Document Services and its usage from connected systems. For observability we are using ELK (Elasticsearch - Logstash - Kibana) stack. This blog article explains how we managed to connect ELK to ADS and build a dashboard over ADS logs.

![](/legacyfs/online/storage/blog_attachments/2023/08/1-34.png)

One of the widgets built in Kibana

## Enabling statistics in ADS

To enable statistics being written to NWA logs you need to enable IFbA statistics to be written to the log. This feature is available starting from Adobe Document Services 7.50 SP09. Information on required SP and patch levels is listed in [Note 2714231 – IFbA: Configuration for collection of ADS performance data](https://me.sap.com/notes/2714231/E). This note outlines that if you have compatible ADS release a log entry under location "*com.adobe.Monitoring*" is generated every time a PDF form is being printed but not written to the log by default.

If you are not keen on using  ELK stack for observability and want to get plain TXT \ Excel files for further study, you can follow the note's instructions. They outline steps required to enable writing ADS print statistics entries to separate files in server filesystem, and the note also includes a Python script for generating Excel-file based on those files.

Below we will look only at getting to these events to ELK stack.

## Enable writing statistics entries

First you need to enable writing statistics entries to default location. For this you need to change logging severity level for "*com.adobe.Monitoring*" tracing location to **INFO** instead of default **ERROR**. We did not need to change logging location (as described in Note 2714231) since we are already ingesting developer trace files directly from NWA using Logstash.

![](/legacyfs/online/storage/blog_attachments/2023/08/2-29.png)

Log configuration for com.adobe.Monitoring

After that a new entry is added to the logfile every time any print request is sent to ADS.

![](/legacyfs/online/storage/blog_attachments/2023/08/3-23.png)

Log entry as viewed in NWA Log Viewer

Information is written as comma-separated values with columns as described in Note 2714231. Here I will describe some of useful ones:

* **template**: name of the print form

* **adsTime**: time it took ADS to fulfil request in milliseconds

* **requestSize**: size of HTTP request to ADS in bytes

* **responseSize**: size of HTTP response from ADS in bytes

* **system**: ABAP client system ID which requested printing

* **client**: ABAP client number which requested printing

* **user**: ABAP user which triggered PDF printing

* **interactivePDF**: true if the form was requested to be printed as Interactive form

* **success**: false if ADS subsystem call fails for any reasons (ADS warnings are not considered a failure)

## Export to ELK stack

The following section assumes that Logstash is already connected to NWA logs. Also the following assumptions about ELK are made:

* Log messages marked with "*NWA*" tag are sourced from on-premise NWA installations

* Field "*sap\_location*" contains "*location*" field from NWA log entry

* Field "*message\_text*" contains "*message*" field from NWA log entry

Here is a Logstash filter configuration we used for processing ADS monitoring log entries:

```
filter {

  # parsing of Adobe monitoring info

  if "NWA" in [tags] and [sap_location] == "com.adobe.Monitoring" {

    csv {

      # mark entry with ADS tag for easy search

      add_tag => ["ADS"]

      # split CSV message into fields

      autogenerate_column_names => false

      target => "ads"

      columns => ["template", "adsTime", "requestSize", "responseSize", "system", "client", "user", "transactionType", "renderOutputType", "numberOfPages", "interactivePDF", "xmlFormTime", "templateUuid", "success"]

      convert => {

        "adsTime" => "integer"

        "requestSize" => "integer"

        "responseSize" => "integer"

        "numberOfPages" => "integer"

        "interactivePDF" => "boolean"

        "xmlFormTime" => "integer"

        "success" => "boolean"

      }

      separator => ","

      skip_header => true

      source => "message_text"

    }

    mutate {

      # concat system and client into one field

      update => {

        "[ads][system]" => "%{[ads][system]}/%{[ads][client]}"

        }

      # remove client field

      remove_field => ["[ads][client]"]

      # split fields

      split => {

        "[ads][renderOutputType]" => "/"

        "[ads][transactionType]" => "/"

        }

    }

  }

}
```

Elasticsearch will receive new fields under "ads" group of fields. Afterwards these fields are available for discovery and analytics in Elasticsearch.

![](/legacyfs/online/storage/blog_attachments/2023/08/4-19.png)

List of ADS-related fields available in ELK stack

![](/legacyfs/online/storage/blog_attachments/2023/08/5-14.png)

Table view of ADS statistics in Kibana

![]...