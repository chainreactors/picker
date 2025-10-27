---
title: How to upload and download file using Webdynpro Technology
url: https://blogs.sap.com/2023/06/08/how-to-upload-and-download-file-using-webdynpro-technology/
source: SAP Blogs
date: 2023-06-09
fetch_date: 2025-10-04T11:47:23.915224
---

# How to upload and download file using Webdynpro Technology

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* How to upload and download file using Webdynpro Te...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160489&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to upload and download file using Webdynpro Technology](/t5/technology-blog-posts-by-members/how-to-upload-and-download-file-using-webdynpro-technology/ba-p/13552556)

![former_member760666](https://avatars.profile.sap.com/former_member_small.jpeg "former_member760666")

[former\_member760666](https://community.sap.com/t5/user/viewprofilepage/user-id/760666)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160489)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160489)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552556)

‎2023 Jun 08
10:13 AM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160489/tab/all-users "Click here to see who gave kudos to this post.")

4,532

* SAP Managed Tags
* [UI Web Dynpro ABAP](https://community.sap.com/t5/c-khhcw49343/UI%2520Web%2520Dynpro%2520ABAP/pd-p/462330605920974660730944876913277)

* [UI Web Dynpro ABAP

  Software Product Function](/t5/c-khhcw49343/UI%2BWeb%2BDynpro%2BABAP/pd-p/462330605920974660730944876913277)

View products (1)

**Introduction**

In this Blog will see how to upload and download file using webdynpro technology.

Follow the following steps as shown below.

**File Upload**

Go to SE80 T-code, in that Repository Brower select Web Dynpro Comm. / Intf. And give the name, discription & save it as shown below.

![](/legacyfs/online/storage/blog_attachments/2023/06/fig1.png)

fig-1

Go to views -> context , right click on context ->create->node.

![](/legacyfs/online/storage/blog_attachments/2023/06/fig2.png)

fig-2

Right click on node-> create-> attribute.

![](/legacyfs/online/storage/blog_attachments/2023/06/fig3.png)

fig-3

Create 3 attributes as mentioned below

|
 Attribute name |
 Type |

|
 Content |
 Xstring |

|
 File\_name |
 String |

|
 Mime\_type |
 String |

![](/legacyfs/online/storage/blog_attachments/2023/06/fig4.png)

fig-4

Go to layout, right click on rootelementcontainer->insert element.

![](/legacyfs/online/storage/blog_attachments/2023/06/fig5.png)

fig-5

Create the element as shown below.

![](/legacyfs/online/storage/blog_attachments/2023/06/fig6.png)

fig-6

In property bind data to content, filename to file\_name and mimetype to mime\_type as shown below.

![](/legacyfs/online/storage/blog_attachments/2023/06/fig7.png)

fig-7

Again right click on rootelementcontainer -> create one more element as shown below.

![](/legacyfs/online/storage/blog_attachments/2023/06/fig8.png)

fig-8

Provide the text for the button in the property.

![](/legacyfs/online/storage/blog_attachments/2023/06/fig9.png)

fig-9

Click on Onaction event property.

![](/legacyfs/online/storage/blog_attachments/2023/06/fig10-2.png)

fig-10

Create on upload event as shown.

![](/legacyfs/online/storage/blog_attachments/2023/06/fig11-1.png)

fig-11

Go to methods tab there a method will be created with your event name of type event handler. Double click on that method(onactiononupload).

![](/legacyfs/online/storage/blog_attachments/2023/06/fig12-1.png)

fig-12

Write the following code in that method.

![](/legacyfs/online/storage/blog_attachments/2023/06/fig13.png)

fig-13

Code

```
Method ONACTIONONUPLOAD.

   data lo_nd_file_upload type ref to if_wd_context_node.

    data lo_el_file_upload type ref to if_wd_context_element.

    data ls_file_upload type wd_this->element_file_upload.

*   navigate from <CONTEXT> to <FILE_UPLOAD> via lead selection

    lo_nd_file_upload = wd_context->get_child_node( name = wd_this->wdctx_file_upload ).

*   @TODO handle non existant child

*   IF lo_nd_file_upload IS INITIAL.

*   ENDIF.

*   get element via lead selection

    lo_el_file_upload = lo_nd_file_upload->get_element( ).

*   @TODO handle not set lead selection

    if lo_el_file_upload is initial.

    endif.

*   get all declared attributes

    lo_el_file_upload->get_static_attributes(

      importing

        static_attributes = ls_file_upload ).

Endmethod.
```

Before activating the method activate the webdynpro object.

![](/legacyfs/online/storage/blog_attachments/2023/06/fig15.png)

fig-14

Then activate the method.
Create the webdynpro application.

![](/legacyfs/online/storage/blog_attachments/2023/06/fig16.png)

fig-15

Give description and save it in your package.
![](/legacyfs/online/storage/blog_attachments/2023/06/fig17.png)

fig-16

Click on webdynpro application and click on execute.
Following output screen will appear

![](/legacyfs/online/storage/blog_attachments/2023/06/fig18.png)

fig-17

Click on browse and choose the file to be uploaded.
In debugging you can see the content , filename and mimetype.

![](/legacyfs/online/storage/blog_attachments/2023/06/fig19.png)

fig-18

**File Download**

Go to SE80 T-code, in that Repository Brower select Web Dynpro Comm. / Intf. And give the name, discription & save it as shown below.

![](/legacyfs/online/storage/blog_attachments/2023/06/fig20.png)

fig-19

Go to views -> context, right click on context ->create->node.

![](/legacyfs/online/storage/blog_attachments/2023/06/fig21.png)

fig-20

Create two nodes as mentioned.

![](/legacyfs/online/storage/blog_attachments/2023/06/fig22.png)

fig-21

Right click on node and create the following attributes under each node

Node – n\_upload

|
 Attribute name |
 Type |

|
 File\_name |
 String |

|
 File\_type |
 String |

|
 File\_size |
 String |

|
 File\_contents |
 Xstring |

Node – n\_file\_download

|
 Attribute name |
 Type |

|
 File\_name |
 String |

|
 File\_type |
 String |

|
 File\_size |
 String |

|
 File\_contents |
 Xstring |

![](/legacyfs/online/storage/blog_attachments/2023/06/fig23.png)

fig-22

Right click on rootelementcontainer and create two groups g1 and g2 as shown.

![](/legacyfs/online/storage/blog_attachments/2023/06/grp.png)

fig-23

![](/legacyfs/online/storage/blog_attachments/2023/06/fig24.png)

fig-24

Right click on group 1 and click on insert element.

![](/legacyfs/online/storage/blog_attachments/2023/06/fig25.png)

fig-25

Create file upload and button element as shown below.

![](/legacyfs/online/storage/blog_attachments/2023/06/fig26.png)

fig-26

In property bind data to content, filename to file\_name and mimetype to mime\_type as shown below.

![](/legacyfs/online/storage/blog_attachments/2023/06/Capture-4.png)

                                                        fig-27

Again right click on rootelementcontainer -> create one more button element as shown below
Create Onaction event as upload.

![](/legacyfs/online/storage/blog_attachments/2023/06/Capture1.png)

fig-28

Right click on group 2 and create table element as shown below.

![](/legacyfs/online/storage/blog_attachments/2023/06/fig29.png)

fig-29

Right click on table element and create binding.

![](/legacyfs/online/storage/blog_attachments/2023/06/fig30.png)

fig-30

...