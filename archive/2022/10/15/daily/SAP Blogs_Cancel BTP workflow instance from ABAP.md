---
title: Cancel BTP workflow instance from ABAP
url: https://blogs.sap.com/2022/10/14/cancel-btp-workflow-instance-from-abap/
source: SAP Blogs
date: 2022-10-15
fetch_date: 2025-10-03T19:56:39.243376
---

# Cancel BTP workflow instance from ABAP

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Cancel BTP workflow instance from ABAP

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/157202&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Cancel BTP workflow instance from ABAP](/t5/technology-blog-posts-by-members/cancel-btp-workflow-instance-from-abap/ba-p/13531222)

![sujitsingh5191](https://avatars.profile.sap.com/b/e/idbe0ee5490565c0784aa07879d43a3687e123e71f7e679b631bbd5ba6532b3bb4_small.jpeg "sujitsingh5191")

[sujitsingh5191](https://community.sap.com/t5/user/viewprofilepage/user-id/38682)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=157202)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/157202)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13531222)

‎2022 Oct 14
6:56 PM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/157202/tab/all-users "Click here to see who gave kudos to this post.")

2,199

* SAP Managed Tags
* [SAP Workflow Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Workflow%2520Management/pd-p/73554900100800003239)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [SAP Workflow Management, business rules capability](https://community.sap.com/t5/c-khhcw49343/SAP%2520Workflow%2520Management%252C%2520business%2520rules%2520capability/pd-p/73554900100800000842)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [SAP Workflow Management, business rules capability

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BWorkflow%2BManagement%25252C%2Bbusiness%2Brules%2Bcapability/pd-p/73554900100800000842)
* [SAP Workflow Management

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BWorkflow%2BManagement/pd-p/73554900100800003239)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (4)

**Introduction:**

As an abapper most of us might be new to calling external APIs from the ABAP environment. There are lots of APIs on cloud foundry or deployed elsewhere which we can use as per as our need. Most of them use the OAuth 2.0 authentication and other authentication processes.

You must have heard about SAP Workflow Management Triggering the workflow and getting in my In Box. But What about cancelling the running workflow instance from the ABAP environment.

In this blog we not only learn how to cancel the workflow instance but also we can use this to call any APIs which uses OAuth 2.0 authentication.

**Scenario:**

Let's imagine a scenario where I triggered a workflow for some PR amount. But I need to change the PR amount and retrigger new workflow with the new amount, also cancelling the previous workflow instance, so the users are in sync with the new approval amount. In this case there are APIs that are available and documented on the Cloud Foundry.

The workflow API is documented and available in the API hub [Workflow API for Cloud Foundry](https://api.sap.com/api/SAP_CP_Workflow_CF/resource)

The prerequisites for calling the API are:

1. Workflow Instance Id.

2. Client Id, Client Secret, URL of workflow service instance for generating Bearer token

3. Workflow API of cloud foundry to update the status of the workflow instance.

Below in the workflow instance created for workflow service in service marketplace and your workflow must be bound to this instance.

![](/legacyfs/online/storage/blog_attachments/2022/10/Workflow-Instance.png)

Workflow Instance

Use the credentials of the service key of the above workflow instance.

![](/legacyfs/online/storage/blog_attachments/2022/10/service-key-credentials.png)

Service Key Credentials

Client Id, Secret and URL are used to generate the Bearer token required for OAuth 2.0 authentication.

Now we are all set to call the workflow Api from the Abap environment.

**Code:**

Below is the code for your reference.

```
    DATA : lv_body          TYPE string,

        lv_client_id     TYPE string,

        lv_client_secret TYPE string.

    DATA: lv_service TYPE string.

    DATA: lv_json_data  TYPE string,

          lr_data       TYPE REF TO data,

          lv_token      TYPE string,

          lv_token_type TYPE string,

          lv_body_data  TYPE string,

          ls_ex_sum_hdr TYPE zicam_exec_sum,

          lv_wfid       TYPE string,

          lv_url        TYPE string.

    FIELD-SYMBOLS: <data>        TYPE data,

                   <results>     TYPE any,

                   <table>       TYPE any,

                   <structure>   TYPE any,

                   <field>       TYPE any,

                   <field_value> TYPE data.

"store client Id, secret and Url, workflow instance Id in some table for different environments and fetch at runtime.

    CALL METHOD call_token_service(

      EXPORTING

        iv_client_id     = lv_client_id

        iv_client_secret = lv_client_secret

        iv_url           = lv_url

      IMPORTING

        ev_token         = lv_token

        ev_token_type    = lv_token_type ).

    lv_wf_id = ''. "Fetch from some table where you store the active worflow instance

    lv_service = 'https://api.workflow-sap.cfapps.us20.hana.ondemand.com/workflow-service/rest/v1/workflow-instances/' && lv_wf_id .

    lv_body_data = lv_body = |\{"status": "CANCELED","cascade": false \}| .

    DATA: lo_http_client TYPE REF TO if_http_client.

    CALL METHOD cl_http_client=>create_by_url

      EXPORTING

        url                = lv_service

      IMPORTING

        client             = lo_http_client

      EXCEPTIONS

        argument_not_found = 1

        plugin_not_active  = 2

        internal_error     = 3

        OTHERS             = 4.

    IF sy-subrc <> 0.

      "error handling

    ENDIF.

    "setting request method

    lo_http_client->request->set_method('PATCH').

    CONCATENATE 'Bearer'  lv_token INTO DATA(lv_auth_value) SEPARATED BY space.

    "adding headers

    lo_http_client->request->set_header_field( name = 'Authorization' value = lv_auth_value ) ##NO_TEXT.

    lo_http_client->request->set_header_field( name = 'Content-Type' value = 'application/json' ) ##NO_TEXT.

    lo_http_client->request->set_header_field( name = 'Accept' value = 'application/json' ) ##NO_TEXT.

    CALL METHOD lo_http_client->request->set_cdata

      EXPORTING

        data = lv_body_data.

    CALL METHOD lo_http_client->send

      EXCEPTIONS

        http_communication_failure = 1

        http_invalid_state         = 2

        http_processing_failed     = 3

        http_invalid_timeout       = 4

        OTHERS                     = 5.

    IF sy-subrc = 0.

      CALL METHOD lo_http_client->receive

        EXCEPTIONS

          http_communication_failure = 1

         ...