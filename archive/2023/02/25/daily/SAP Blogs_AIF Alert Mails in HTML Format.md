---
title: AIF Alert Mails in HTML Format
url: https://blogs.sap.com/2023/02/24/aif-alert-mails-in-html-format/
source: SAP Blogs
date: 2023-02-25
fetch_date: 2025-10-04T08:03:43.593962
---

# AIF Alert Mails in HTML Format

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* AIF Alert Mails in HTML Format

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161283&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [AIF Alert Mails in HTML Format](/t5/technology-blog-posts-by-members/aif-alert-mails-in-html-format/ba-p/13557350)

![sebastian_gottmann3](https://avatars.profile.sap.com/7/2/id722b25b2c639f96d6419a0597013b584682f70c9eac3839219fe25ac43315711_small.jpeg "sebastian_gottmann3")

[sebastian\_gottmann3](https://community.sap.com/t5/user/viewprofilepage/user-id/259343)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161283)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161283)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13557350)

‎2023 Feb 24
6:54 PM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161283/tab/all-users "Click here to see who gave kudos to this post.")

4,176

* SAP Managed Tags
* [SAP Application Interface Framework](https://community.sap.com/t5/c-khhcw49343/SAP%2520Application%2520Interface%2520Framework/pd-p/01200314690800001892)

* [SAP Application Interface Framework

  SAP Application Interface Framework](/t5/c-khhcw49343/SAP%2BApplication%2BInterface%2BFramework/pd-p/01200314690800001892)

View products (1)

## Baseline

Within the SAP Application Interface Framework (AIF), e-mail notifications can be sent to interface responsibles via the standard SAP Alert Management. The formatting and content of the email notification is not part of the AIF and must be done in Alert Management. Typically, these email notifications are in rich text format and therefore cannot be extensively formatted in text.

This short blog post is intended to illustrate how to change these email notifications to HTML format so that the text can be formatted to your preferences.

## Prerequisites

An alert category is created for the AIF in Alert Management and the category is assigned to the interface. The alert category is triggered and the system sends an email to the interface responsibles.

## Implementation

In the Alert Management environment there is a classic BAdI (ALERT\_MODIFY\_TEXT) with which the text can be modified. This BAdI returns two parameters in the signature. CP\_TEXT\_TYPE defines the type. This can be changed to "HTM". CT\_LONG\_TEXT is a table and contains the actual text of the e-mail.

The text can be customized and formatted with HTML tags. In order to get information from the alert container, it must be read so that it can be sent in the email.

```
METHOD if_ex_alert_modify_text~modify_long_text.

  CONSTANTS: lc_text_type TYPE so_obj_tp VALUE 'HTM'.

  DATA: lr_swf_cnt_container TYPE REF TO if_swf_cnt_container,

        lv_ns                TYPE /aif/ns,

        lv_ifname            TYPE /aif/ifname,

        lv_ifversion         TYPE /aif/ifversion,

        lv_nsrecipient       TYPE /aif/ns,

        lv_recipient         TYPE /aif/alrt_rec,

        lt_messages          TYPE TABLE OF bapiret2,

        lv_messages_nr       TYPE sytabix,

        lv_msgguid           TYPE sxmsguid,

        lv_date(10)          TYPE c,

        lv_time(10)          TYPE c.

* Set Time/Date Format

  CONCATENATE sy-uzeit+0(2) sy-uzeit+2(2) sy-uzeit+4(2) INTO lv_time SEPARATED BY ':'.

  WRITE sy-datum TO lv_date MM/DD/YYYY.

* Change Mail Format to HTML

  cp_text_type = lc_text_type.

* Assign alert data

  DATA(lr_alert) = NEW cl_alert( ).

  lr_alert ?= io_alert.

* Get Alert Container

  TRY.

      CALL METHOD lr_alert->get_ifcontainer

        RECEIVING

          result = lr_swf_cnt_container.

      CALL METHOD lr_alert->get_creatime

        RECEIVING

          result = DATA(lv_creatime).

      CALL METHOD lr_alert->get_logical_system

        RECEIVING

          result = DATA(lv_logical_system).

    CATCH cx_os_object_not_found.

  ENDTRY.

* Get Elements

  TRY.

      CALL METHOD lr_swf_cnt_container->if_swf_ifs_parameter_container~get

        EXPORTING

          name  = 'NS'

        IMPORTING

          value = lv_ns.

      CALL METHOD lr_swf_cnt_container->if_swf_ifs_parameter_container~get

        EXPORTING

          name  = 'IFNAME'

        IMPORTING

          value = lv_ifname.

      CALL METHOD lr_swf_cnt_container->if_swf_ifs_parameter_container~get

        EXPORTING

          name  = 'IFVERSION'

        IMPORTING

          value = lv_ifversion.

      CALL METHOD lr_swf_cnt_container->if_swf_ifs_parameter_container~get

        EXPORTING

          name  = 'NSRECIPIENT'

        IMPORTING

          value = lv_nsrecipient.

      CALL METHOD lr_swf_cnt_container->if_swf_ifs_parameter_container~get

        EXPORTING

          name  = 'RECIPIENT'

        IMPORTING

          value = lv_recipient.

      CALL METHOD lr_swf_cnt_container->if_swf_ifs_parameter_container~get

        EXPORTING

          name  = 'MESSAGES'

        IMPORTING

          value = lt_messages.

      CALL METHOD lr_swf_cnt_container->if_swf_ifs_parameter_container~get

        EXPORTING

          name  = 'MESSAGES_NR'

        IMPORTING

          value = lv_messages_nr.

      CALL METHOD lr_swf_cnt_container->if_swf_ifs_parameter_container~get

        EXPORTING

          name  = 'MSGGUID'

        IMPORTING

          value = lv_msgguid.

    CATCH cx_swf_cnt_elem_not_found.

    CATCH cx_swf_cnt_elem_type_conflict.

    CATCH cx_swf_cnt_unit_type_conflict.

    CATCH cx_swf_cnt_container.

  ENDTRY.

* Build Mailtext

  CLEAR ct_long_text.

  APPEND VALUE #( line = '<p style="color:red;font-weight:bold;">Attention!<br />An error occured during message processing.</p>' ) TO ct_long_text.

  APPEND VALUE #( line = '<p style="font-weight:bold;">Following, you will find all necessary information.</p>' ) TO ct_long_text.

  APPEND VALUE #( line = '<ul style="list-style-type: disc;">' ) TO ct_long_text.

  APPEND VALUE #( line = '<li>Namespace:&nbsp;' && lv_ns && '</li>' ) TO ct_long_text.

  APPEND VALUE #( line = '<li>Interface:&nbsp;' && lv_ifname && '</li>' ) TO ct_long_text.

  APPEND VALUE #( line = '<li>Interface Version:&nbsp;' && lv_ifversion && '</li>' ) TO ct_long_text.

  APPEND VALUE #( line = '<li>Alert Recipient:&nbsp;' && lv_nsrecipient && '/' && lv_recipient && '</li>' ) TO ct_long_text.

  APPEND VALUE #( line = '<li>User:&nbsp;' && sy-uname && '</li>' ) TO ct_long_text.

  APPEND VALUE #( line = '<li>Date:&nbsp;' && lv_date && '</li>' ) TO ct_long_text.

  APPEND VALUE #( line = '<li>Time:&nbsp;' && lv_time && '</li>' ) TO ct_long_text.

  APPEND VALUE #( line = '<li>Message GUID:&nbsp;' && lv_msgguid && '</li>' ) TO ct_long_text.

  APPEND VALUE #( line = '</ul>' ) TO ct_long_text.

  APPEND VALUE #( line = '<p style="font-weight:bold;">Log Messages:</p>' ) TO ct_long_text.

  APPEND VALUE #( line = '<p>----------------------------------------------------------------------------------------------------</p>' ) TO ct_long_text.

  LOOP AT lt_messages INTO DATA(lv_message).

    APPEND VALUE #( line = '<span>' && lv_messa...