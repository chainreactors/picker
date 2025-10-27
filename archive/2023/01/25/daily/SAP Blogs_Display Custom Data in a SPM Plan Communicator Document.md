---
title: Display Custom Data in a SPM Plan Communicator Document
url: https://blogs.sap.com/2023/01/24/display-custom-data-in-a-spm-plan-communicator-document/
source: SAP Blogs
date: 2023-01-25
fetch_date: 2025-10-04T04:43:37.225139
---

# Display Custom Data in a SPM Plan Communicator Document

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)
* Display Custom Data in a SPM Plan Communicator Doc...

Human Capital Management Blog Posts by SAP

Learn directly from SAP experts through blogs that deliver practical guidance and opportunities to deepen your expertise.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-sap/article-id/5670&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Display Custom Data in a SPM Plan Communicator Document](/t5/human-capital-management-blog-posts-by-sap/display-custom-data-in-a-spm-plan-communicator-document/ba-p/13548222)

![joncadby](https://avatars.profile.sap.com/9/5/id95e254f5d00974d158a2fb37116a98caf8b3a156d67d1472c6541be065a5f859_small.jpeg "joncadby")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[joncadby](https://community.sap.com/t5/user/viewprofilepage/user-id/116351)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-sap&message.id=5670)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-sap/article-id/5670)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548222)

‎2023 Jan 24
8:40 PM

[5
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-sap/message-id/5670/tab/all-users "Click here to see who gave kudos to this post.")

868

* SAP Managed Tags
* [SAP SuccessFactors Incentive Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Incentive%2520Management/pd-p/73555000100800001602)

* [SAP SuccessFactors Incentive Management

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BIncentive%2BManagement/pd-p/73555000100800001602)

View products (1)

# Overview

The purpose of this article is to show how to include any data that is available in the SAP Commissions database (TCMP and EXT schemas) in a SPM Plan Communicator Document.

# Introduction

Plan Communicator Documents can display the following Commissions elements:

* Formula

* Rate Table

* Fixed Value

* Territory

* Variable

* Quota

* Data Fields (Position, Participant, Title, Position Group)

The elements above are directly associated to the user via their plan assignment. It is possible to display anything stored in the SAP Commissions database (TCMP and EXT schemas) in a SPM Plan Communicator Document using a Formula with the “Query for String” rule function.

Some common use cases for this solution are:

* MDLT

* Category and Classifier

* Territory & Quota objects

* Custom database tables

# Worked Example

The solution is described in this section by way of a worked example in a HANA database. Similar steps would apply to an Oracle environment.

## Step 1: Create a HANA Function

While not required, it is recommended that the logic to retrieve the data is compiled in a HANA function. The following example retrieves an MDLT and formats it as an HTML table

```
create or replace function EXT.JC_FNC_LT_Bonus_Lookup(i_positionSeq bigint default null, i_periodSeq bigint default  null) returns v_ret varchar(32000) as

begin

  declare v_eot date := '2200-01-01';

  declare v_mdlt varchar(255) := 'LT_Bonus_Lookup';

  declare cursor c_mdlt for

  select mdlt.name as mdlt_name, re.description as mdlt_desc,

  dim0.name as dim0_name, ind0.minstring as dim0_value,

  dim1.name as dim1_name, to_char(cast(ind1.minvalue as integer)) as dim1_value,

  to_char(cast(cell.value as decimal(25,2))) as cell_value,

  row_number() over (order by ind0.displayorder, ind1.displayorder) as rn

  from cs_relationalmdlt mdlt

  join cs_ruleelement re on mdlt.ruleelementseq = re.ruleelementseq and re.removedate = :v_eot and re.effectivestartdate = mdlt.effectivestartdate

  join cs_mdltdimension dim0 on mdlt.ruleelementseq = dim0.ruleelementseq and dim0.removedate = :v_eot and dim0.dimensionslot = 0

  join cs_mdltindex ind0 on mdlt.ruleelementseq = ind0.ruleelementseq and ind0.removedate = :v_eot and ind0.dimensionseq = dim0.dimensionseq

  join cs_mdltdimension dim1 on mdlt.ruleelementseq = dim1.ruleelementseq and dim1.removedate = :v_eot and dim1.dimensionslot = 1

  join cs_mdltindex ind1 on mdlt.ruleelementseq = ind1.ruleelementseq and ind1.removedate = :v_eot and ind1.dimensionseq = dim1.dimensionseq

  left outer join cs_mdltcell cell on cell.mdltseq = mdlt.ruleelementseq and cell.removedate = :v_eot and cell.dim0index = ind0.ordinal and cell.dim1index = ind1.ordinal

  where mdlt.removedate = :v_eot

  and mdlt.name = :v_mdlt

  order by ind0.displayorder, ind1.displayorder;

  for x as c_mdlt

  do

    if :x.rn = 1 then

      v_ret := '<p><b>'||:x.mdlt_name||' '||:x.mdlt_desc||'</b></p>'

            || '<table class="ruleElementTable table table-condensed">'

            || '<thead><tr><th>'||:x.dim0_name||'</th><th>'||:x.dim1_name||'</th><th>Value</th></tr></thead>';

    end if;

    v_ret := :v_ret || '<tr><td>'||:x.dim0_value||'</td><td>'||:x.dim1_value||'</td><td>'||:x.cell_value||'</td></tr>';

  end for;

  v_ret := ifnull(:v_ret || '</table>', 'MDLT "'||:v_mdlt||'" not found.');

end;
```

## Step 2: Add Query to CS\_PluginQuery

This step allows the query to be used by the Commission rules.

```
insert into CS_PluginQuery (tenantId, name, query) values (<TENANT_ID>, 'LT_Bonus_Lookup', 'select EXT.JC_FNC_LT_Bonus_Lookup(positionSeq, periodSeq) from (select $positionSeq as positionSeq, $periodSeq as periodSeq from dummy)');

commit;
```

## Step 3: Create Formula

A formula is created that calls the database function.

![](/legacyfs/online/storage/blog_attachments/2023/01/Formula-1.png)

Formula

## Step 4: Add Dummy Rule to Plan

Create a deposit rule that will never fire (Conditions: false) that uses the formula from the previous step (Generic Attribute 1: F\_Plan\_Communicator\_LT\_Bonus\_Lookup)

![](/legacyfs/online/storage/blog_attachments/2023/01/Deposit-Rule.png)

Deposit Rule

Add the rule to the plan.

## Step 5: Add Formula to Plan Communicator Document

You can now use the formula in the Plan Communicator Documents to display the required data.

![](/legacyfs/online/storage/blog_attachments/2023/01/Document.png)

Document

Result:

![](/legacyfs/online/storage/blog_attachments/2023/01/Result.png)

Result

## Technical Notes

* The max length of a VARCHAR/NVARCHAR returned by a HANA is documented as 8388607.

* The “Query for String” will timeout after 5 seconds.

* The return string can include HTML tags for formatting.

* The period input parameters are set to the leaf level period that is effective for the end date of the distribution.

* The performance of the function should be considered to avoid timeouts. If the query is complex, then the data can be prebuilt in a custom table.

* A deposit rule is used because:

  + It has considerably fewer evaluations compared to a credit rule

  + It does not create unwanted objects like a measurement or incentive rule

Labels

* [Technology Updates](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap/label-name/technology%20updates)

* [Plan Communicator](/t5/tag/Plan%20Communicator/tg-p/board-id/hcm-blog-sap)

You must be a registered user to add a comment. If you've al...