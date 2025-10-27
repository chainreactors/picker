---
title: Customized SAP Data Intelligence Deployment cycle using Github Action Workflows
url: https://blogs.sap.com/2023/06/16/customized-sap-data-intelligence-deployment-cycle-using-github-action-workflows/
source: SAP Blogs
date: 2023-06-17
fetch_date: 2025-10-04T11:47:00.330363
---

# Customized SAP Data Intelligence Deployment cycle using Github Action Workflows

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Customized SAP Data Intelligence Deployment cycle ...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161681&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Customized SAP Data Intelligence Deployment cycle using Github Action Workflows](/t5/technology-blog-posts-by-members/customized-sap-data-intelligence-deployment-cycle-using-github-action/ba-p/13559578)

![patrobibeksap](https://avatars.profile.sap.com/2/b/id2b135c957c550f4203cd7ca94cb579cd56db6b878e7071f2521c21bf43367081_small.jpeg "patrobibeksap")

[patrobibeksap](https://community.sap.com/t5/user/viewprofilepage/user-id/787935)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161681)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161681)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559578)

‎2023 Jun 16
2:59 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161681/tab/all-users "Click here to see who gave kudos to this post.")

1,307

* SAP Managed Tags
* [SAP Data Intelligence](https://community.sap.com/t5/c-khhcw49343/SAP%2520Data%2520Intelligence/pd-p/73555000100800000791)
* [Data and Analytics](https://community.sap.com/t5/c-khhcw49343/Data%2520and%2520Analytics/pd-p/87817424-f4e7-46f2-af14-88bf0f4ba034)

* [SAP Data Intelligence

  SAP Data Intelligence](/t5/c-khhcw49343/SAP%2BData%2BIntelligence/pd-p/73555000100800000791)
* [Data and Analytics

  Product Category](/t5/c-khhcw49343/Data%2Band%2BAnalytics/pd-p/87817424-f4e7-46f2-af14-88bf0f4ba034)

View products (2)

**Introduction**:

This is going to be my first blog on SAP Data Intelligence and quite excited about sharing with all my SAP colleagues/members working on this tool.

This document overviews about deployment life cycle management for SAP Data Intelligence using CI/CD methodology. Since SAP DI doesn’t provide any proprietary tools for deployments as of the current DI version 2303.15.28.

**Business Pain Points:**

* There is no SAP proprietary solution for deployment of SAP DI pipelines and operators using CI/CD approach

* Exporting and Importing files into Production systems are restricted in some of the client deployments

* Manual method of deploying DI objects is susceptible to human mistakes

**Business Value Proposition:**

* Implementation of CI/CD throughout Development, testing and Production phases of SAP DI development.

* Automatic deployment of DI pipelines and operators without any manual intervention

* Review of the DI objects when pushed for deployment to check its completeness and inform developers/object owners about it.

* Authentication based approach where the DI objects are reviewed and authenticated at every level to discard any unintended changes to get moved between different systems.

**Deployment Workflow Path:**

The following picture shows the path how the objects are moved starting from development till getting it deployed into Production.

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture1-28.png)

The following points to be noted here:

* Develop, Test and Master branches are protected so that no one can able to push to it directly.

* The changes can be moved from Feature branches to develop, test and Master separately which helps us independently deploy DI objects in case required.

* Each workflows are event based triggered like based on pull or push requests

* Each workflow can identify and deploy only new DI pipelines or changes pipeline rather than picking all from the repository. This is the strength of this pipeline which avoids re-deployment of unchanged DI objects into test and production systems.

**Design of deployment workflow**

The workflows are designed using Git Action commands. These action commands are branch specific and execution is based on event (Push or Pull requests). This workflow can identify the DI pipelines/operator files which are modified or newly created and trigger deployment only for those objects.

The sample code here can be referenced for designing your deployment workflows.

```
name: Deployment of DI objects to DEVELOPMENT tenant

on:

  push:

    branches: [<Github development branch name>]

jobs:

  setup:

    runs-on: ubuntu-latest

    outputs:

      matrix: ${{steps.list_file.outputs.value}}

    steps:

      - name: check out repo

        uses: actions/checkout@v2

      - name: Get Diff Action

        uses: technote-space/get-diff-action@v6

        with:

          format: JSON

      - name: Filter files for graphs and operators only

        run: |

          res=$(echo '${{ env.GIT_DIFF }}' | jq '.[] | select(. | contains("graph.json") or contains("operator.json"))' | jq -Rsc '. / "\n" - [""]')

          echo "filtered_op=$res" >> $GITHUB_ENV

        shell: bash

      - name: Passing the final output to build

        id: list_file

        run: |

          res=$(echo '${{ env.filtered_op}}' | jq '.[]')

          if [ -z $res ]; then

            echo '::set-output name=value::["NO DEPLOYMENT OBJECTS FOUND"]'

          else

            echo '::set-output name=value::${{ env.filtered_op }}'

          fi

  build:

    needs: [setup]

    runs-on: windows-latest

    strategy:

      max-parallel: 1

      matrix:

        value: ${{fromJson(needs.setup.outputs.matrix)}}

    steps:

      - name: Checking out your current git repository

        if: ${{ matrix.value != 'NO DEPLOYMENT OBJECTS FOUND' }}

        uses: actions/checkout@v2

      - name: Capturing the solution name to bundle

        if: ${{ matrix.value != 'NO DEPLOYMENT OBJECTS FOUND' }}

        run: echo "obj_name=$(echo ${{ matrix.value }} | awk 'BEGIN{FS=OFS="/"} {print $--NF}')" >> $GITHUB_ENV

        shell: bash

      - name: Finding the Source directory

        if: ${{ matrix.value != 'NO DEPLOYMENT OBJECTS FOUND' }}

        run: |

          echo "source_dir=$(echo ${{matrix.value}} | awk 'BEGIN{FS=OFS="/"}NF--')" >> $GITHUB_ENV

        shell: bash

      - name: Defining the target directory for solution

        if: ${{ matrix.value != 'NO DEPLOYMENT OBJECTS FOUND' }}

        run: |

          echo "target_dir=$(echo ${{ env.obj_name }}/content/files/vflow/${{env.source_dir}})" >> $GITHUB_ENV

        shell: bash

      - name: Building the solution directory structure

        if: ${{ matrix.value != 'NO DEPLOYMENT OBJECTS FOUND' }}

        run: |

          mkdir -p ${{env.target_dir}}

          cp -R ${{env.source_dir}}/* ${{env.target_dir}}/

          cp -R ${{env.source_dir}}/manifest.json ${{ env.obj_name }}/

        shell: bash

      - name: Log-in to DI through vctl

        if: ${{ matrix.value != 'NO DEPLOYMENT OBJECTS FOUND' }}

        run: vctl\vctl.exe login ${{secrets.<DEV INSTANCE URL GIT SECRET>}} --user-cert ${{secrets.<bundle.pem GIT SECRET>}} ${{secrets.<key.pem GIT SECRET>}}

      - name: Bundle the solution into zip file in current working directory

        if: ${{ matrix.value != 'NO DEPLOYMENT OBJECTS FOUND' }}

        run: vctl\vctl.exe solution...