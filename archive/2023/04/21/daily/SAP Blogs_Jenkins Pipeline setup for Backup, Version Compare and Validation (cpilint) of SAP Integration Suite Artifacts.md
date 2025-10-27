---
title: Jenkins Pipeline setup for Backup, Version Compare and Validation (cpilint) of SAP Integration Suite Artifacts
url: https://blogs.sap.com/2023/04/20/jenkins-pipeline-setup-for-backup-version-compare-and-validation-cpilint-of-sap-integration-suite-artifacts/
source: SAP Blogs
date: 2023-04-21
fetch_date: 2025-10-04T11:34:37.613594
---

# Jenkins Pipeline setup for Backup, Version Compare and Validation (cpilint) of SAP Integration Suite Artifacts

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Jenkins Pipeline setup for Backup, Version Compare...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161416&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Jenkins Pipeline setup for Backup, Version Compare and Validation (cpilint) of SAP Integration Suite Artifacts](/t5/technology-blog-posts-by-members/jenkins-pipeline-setup-for-backup-version-compare-and-validation-cpilint-of/ba-p/13558342)

![asutoshmaharana2326](https://avatars.profile.sap.com/a/6/ida613264dd8e590b139031a977789d3a2b83f16028183eed06be5bd24357b2466_small.jpeg "asutoshmaharana2326")

[asutoshmaharana2326](https://community.sap.com/t5/user/viewprofilepage/user-id/651788)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161416)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161416)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558342)

‎2023 Apr 20
9:00 PM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161416/tab/all-users "Click here to see who gave kudos to this post.")

3,212

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)

* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)

View products (1)

# Introduction

This article will explain step by step procedure to create Jenkins’s pipeline to backup source code, compare Versions and perform basic validation/checks (Using [cpilint](https://blogs.sap.com/2019/02/01/meet-cpilint/) tool) for Integration Flows created in SAP Integration Suite. I have mostly taken (almost all) reference from below two GitHub repo.

[**CICD-StoreIntegrationArtefact**](https://github.com/SAP/apibusinesshub-integration-recipes/tree/master/Recipes/for/CICD-StoreIntegrationArtefact) - sunny.kapoor2 and SAP team

[**cpilint**](https://github.com/mwittrock/cpilint) - 7a519509aed84a2c9e6f627841825b5a

# Main

Prerequisites:

1. Docker should be installed.(Docker Desktop as well for GUI)

* ## Jenkins Installation (Using Docker)

Jenkins can be installed using simple command from any terminal or cmd.

```
docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts-jdk11
```

![](/legacyfs/online/storage/blog_attachments/2023/04/jenkinsDocker1-1.png)

Jenkins Docker Image Run

After Installation, copy the temp password and go to localhost:8080 in the browser and provide the password and click next. Then create one admin user and press next. In the next page choose appropriate uri and then click save and finish. Do not install all the the plugins and only proceed with "Select Plugins to install".

* ## GitHub Repo Creation

* Create a new private repository with appropriate name in GitHub.

* Create a "Jenkinsfile" with below code.

```
pipeline {

	agent any

	parameters {

		string defaultValue: 'internalEventListener', description: 'Iflow Name', name: 'Name', trim: true

	}

	//Configure the following environment variables before executing the Jenkins Job

	environment {

		IntegrationFlowID = "${Name}"

		CPIHost = "${env.CPI_HOST}"

		CPIOAuthHost = "${env.CPI_OAUTH_HOST}"

		CPIOAuthCredentials = "${env.CPI_OAUTH_CRED}"

		GITRepositoryURL  = "${env.GIT_REPOSITORY_URL}"

		GITCredentials = "${env.GIT_CRED}"

		GITBranch = "${env.GIT_BRANCH_NAME}"

		GITFolder = "IntegrationContent/IntegrationArtefacts"

		GITComment = "Integration Artefacts update from CICD pipeline"

   	}

	stages {

		stage('download integration artefact and store it in GitHub') {

			steps {

			 	deleteDir()

				script {

					//clone repo

					checkout([

						$class: 'GitSCM',

						branches: [[name: env.GITBranch]],

						doGenerateSubmoduleConfigurations: false,

						extensions: [

							[$class: 'RelativeTargetDirectory',relativeTargetDir: "."],

							//[$class: 'SparseCheckoutPaths',  sparseCheckoutPaths:[[$class:'SparseCheckoutPath', path: env.GITFolder]]]

						],

						submoduleCfg: [],

						userRemoteConfigs: [[

							credentialsId: env.GITCredentials,

							url: 'https://' + env.GITRepositoryURL

						]]

					])

					//get token

					println("Request token");

					def token;

					try{

					def getTokenResp = httpRequest acceptType: 'APPLICATION_JSON',

						authentication: env.CPIOAuthCredentials,

						contentType: 'APPLICATION_JSON',

						httpMode: 'POST',

						responseHandle: 'LEAVE_OPEN',

						timeout: 30,

						url: 'https://' + env.CPIOAuthHost + '/oauth/token?grant_type=client_credentials';

					def jsonObjToken = readJSON text: getTokenResp.content

					token = "Bearer " + jsonObjToken.access_token

				   	} catch (Exception e) {

						error("Requesting the oauth token for Cloud Integration failed:\n${e}")

					}

					//delete the old flow content so that only the latest content gets stored

					dir(env.GITFolder + '/' + env.IntegrationFlowID){

						deleteDir();

					}

					//download and extract artefact from tenant

					println("Downloading artefact");

					def tempfile = UUID.randomUUID().toString() + ".zip";

					def cpiDownloadResponse = httpRequest acceptType: 'APPLICATION_ZIP',

						customHeaders: [[maskValue: false, name: 'Authorization', value: token]],

						ignoreSslErrors: false,

						responseHandle: 'LEAVE_OPEN',

						validResponseCodes: '100:399, 404',

						timeout: 30,

						outputFile: tempfile,

						url: 'https://' + env.CPIHost + '/api/v1/IntegrationDesigntimeArtifacts(Id=\''+ env.IntegrationFlowID + '\',Version=\'active\')/$value';

					if (cpiDownloadResponse.status == 404){

						//invalid Flow ID

						error("Received http status code 404. Please check if the Artefact ID that you have provided exists on the tenant.");

					}

					def disposition = cpiDownloadResponse.headers.toString();

					def index=disposition.indexOf('filename')+9;

					def lastindex=disposition.indexOf('.zip', index);

					def filename=disposition.substring(index + 1, lastindex + 4);

					def folder=env.GITFolder + '/' + filename.substring(0, filename.indexOf('.zip'));

					def zipfolder=env.GITFolder + '/ZipFiles';

					fileOperations([fileUnZipOperation(filePath: tempfile, targetLocation: folder)])

					fileOperations([fileRenameOperation(source: tempfile,  destination: filename)])

					fileOperations([fileCopyOperation(includes: filename,  targetLocation: zipfolder)])

					env.Filename = filename;

					cpiDownloadResponse.close();

					//remove the zip

					fileOperations([fileDeleteOperation(excludes: '', includes: filename)])

					dir(env.GITFolder){

						sh 'git add .'

					}

					println("Store integration artefact in Git")

					withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: env.GITCredentials ,usernameVariable: 'GIT_AUTHOR_NAME', passwordVariable: 'GIT_PASSWORD']]) {

						sh 'git diff-index --quiet HEAD || git commit -am ' + '\'' + env.GitComment + '\''

						sh('git push https://${GIT_PASSWORD}...