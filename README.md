![](https://github.com/QualiSystems/cloudshell-shells-documentaion-templates/blob/master/cloudshell_logo.png)

# **BreakingPoint Chassis 2G Shell**  

Release date: September 2022

Shell version: 3.0.1

Document version: 1.1

# In This Guide

* [Overview](#overview)
* [Downloading the Shell](#downloading-the-shell)
* [Importing and Configuring the Shell](#importing-and-configuring-the-shell)
* [Updating Python Dependencies for Shells](#updating-python-dependencies-for-shells)
* [Associating a CloudShell Service to a Non-Global Domain](#associating-a-cloudShell-service-to-a-non-global-domain)
* [Typical Workflows](#typical-workflows)
* [References](#references)
* [Release Notes](#release-notes)


# Overview
A shell integrates a device model, application or other technology with CloudShell. A shell consists of a data model that defines how the device and its properties are modeled in CloudShell, along with automation that enables interaction with the device via CloudShell.

### Traffic Generator Shells
CloudShell's traffic generator shells enable you to conduct traffic test activities on Devices Under Test (DUT) or Systems Under Test (SUT) from a sandbox. In CloudShell, a traffic generator is typically modeled using a chassis resource, which represents the traffic generator device and ports, and a controller service that runs the chassis commands, such as Load Configuration File, Start Traffic and Get Statistics. Chassis and controllers are modeled by different shells, allowing you to accurately model your real-life architecture. For example, scenarios where the chassis and controller are located on different machines.

For additional information on traffic generator shell architecture, and setting up and using a traffic generator in CloudShell, see the [Traffic Generators Overiew](http://help.quali.com/Online%20Help/9.0/Portal/Content/CSP/LAB-MNG/Trffc-Gens.htm?Highlight=traffic%20generator%20overview) online help topic.

### BreakingPoint Chassis 2G Shell
To model the traffic generator in CloudShell, you must use the following shells:

▪ [BreakingPoint Chassis 2G Shell](https://github.com/QualiSystems/BreakingPoint-Chassis-Shell-2G) , which provides data model and autoload functionality to model and load the chassis to resource management.

▪ [BreakingPoint Controller Shell 2G](https://github.com/QualiSystems/BreakingPoint-Controller-Shell-2G) (service), which provides functionality to load test configuration, run tests, get test results, etc.

### Standard version

The BreakingPoint 2G shells are based on the **Traffic Generator Chassis Shell Standard version 1.0.3** and the **Traffic Generator Controller Shell Standard version 2.0.0**.

For detailed information about the shell’s structure and attributes, see the [Traffic Generator Chassis Shell Standard](https://github.com/QualiSystems/cloudshell-standards/blob/master/Documentation/Traffic%20Generator%20Chassis%20Standard.md) and the [Traffic Generator Controller Shell Standard](https://github.com/QualiSystems/cloudshell-standards/blob/master/Documentation/Traffic%20Generator%20Controller%20Shell%20Standard.md) in GitHub.

### Requirements

Release: **Ixia BreakingPoint 2G shells**

- CloudShell versions: 
  - v2022.1.0 and above patches
- BreakingPoint application:
  - 9.00 and above

### Data Model

The shell's data model includes all shell metadata, families, and attributes.

**BreakingPoint Families and Models**

The chassis families and models are listed in the following table:

|Family|Model|Description|
|:---|:---|:---|
|Traffic Generator Chassis|BreakingPoint Chassis|BreakingPoint Chassis|
|Module|Generic Traffic Generator Module|Modules located on the chassis|
|Port Group|Generic Port Group|Generic Port Group|
|Port|Generic Traffic Generator Port|Generic Traffic Generator Port|

#### **BreakingPoint Chassis 2G Shell Attributes**

The attribute names and types are listed in the following sections of the Traffic Generator Standard:

* [Traffic Generator Chassis Shell Standard attributes](https://github.com/QualiSystems/cloudshell-standards/blob/master/Documentation/Traffic%20Generator%20Chassis%20Standard.md#attributes)

### Automation
This section describes the automation (driver) associated with the data model. The shell’s driver is provided as part of the shell package. There are two types of automation processes, Autoload and Resource. Autoload is executed when creating the resource in the **Inventory** dashboard, while resource commands are run in the sandbox.

For Traffic Generator shells, commands are configured and executed from the controller service in the sandbox, with the exception of the Autoload command, which is executed when creating the resource.

|Command|Description|
|:-----|:-----|
|Autoload|Discovers the chassis, its hierarchy and attributes when creating the resource. The command can be rerun in the Inventory dashboard and not in the sandbox, as for other commands.|

The command names and types are listed in the following sections of the Traffic Generator Standard:

* [Traffic Generator Chassis Shell Standard commands](https://github.com/QualiSystems/cloudshell-standards/blob/master/Documentation/Traffic%20Generator%20Chassis%20Standard.md#Commands)

# Downloading the Shell
The **BreakingPoint Chassis 2G Shell** is available from the [Quali Community Integrations](https://community.quali.com/integrations) page. 

Download the files into a temporary location on your local machine. 

The shell comprises:

|File name|Description|
|:---|:---|
|BreakingPoint.Chassis.Shell.2G.zip|Device shell package|
|bp-offline-dependencies-2G-x.x.x.zip|Shell Python dependencies (for offline deployments only)|

# Importing and Configuring the Shell
This section describes how to import the **BreakingPoint Chassis 2G Shell** and configure and modify the shell’s devices.

### Importing the shell into CloudShell

**To import the shell into CloudShell:**
  1. Make sure you have the shell’s zip package. If not, download the shell from the [Quali Community's Integrations](https://community.quali.com/integrations) page.
  
  2. In CloudShell Portal, as Global administrator, open the **Manage – Shells** page.
  
  3. Click **Import**.
  
  4. In the dialog box, navigate to the shell's zip package, select it and click **Open**. <br><br>The shell is displayed in the **Shells** page and can be used by domain administrators in all CloudShell domains to create new inventory resources, as explained in [Adding Inventory Resources](http://help.quali.com/Online%20Help/9.0/Portal/Content/CSP/INVN/Add-Rsrc-Tmplt.htm?Highlight=adding%20inventory%20resources). 

### Offline installation of a shell

**Note:** Offline installation instructions are relevant only if CloudShell Execution Server has no access to PyPi. You can skip this section if your execution server has access to PyPi. For additional information, see the online help topic on offline dependencies.

In offline mode, import the shell into CloudShell and place any dependencies in the appropriate dependencies folder. The dependencies folder may differ, depending on the CloudShell version you are using:

* For CloudShell version 8.3 and above, see [Adding Shell and script packages to the local PyPi Server repository](#adding-shell-and-script-packages-to-the-local-pypi-server-repository).

* For CloudShell version 8.2, perform the appropriate procedure: [Adding Shell and script packages to the local PyPi Server repository](#adding-shell-and-script-packages-to-the-local-pypi-server-repository) or [Setting the Python pythonOfflineRepositoryPath configuration key](#setting-the-python-pythonofflinerepositorypath-configuration-key).

* For CloudShell versions prior to 8.2, see [Setting the Python pythonOfflineRepositoryPath configuration key](#setting-the-python-pythonofflinerepositorypath-configuration-key).

### Adding shell and script packages to the local PyPi Server repository
If your Quali Server and/or execution servers work offline, you will need to copy all required Python packages, including the out-of-the-box ones, to the PyPi Server's repository on the Quali Server computer (by default *C:\Program Files (x86)\QualiSystems\CloudShell\Server\Config\Pypi Server Repository*).

For more information, see [Configuring CloudShell to Execute Python Commands in Offline Mode](http://help.quali.com/Online%20Help/9.0/Portal/Content/Admn/Cnfgr-Pyth-Env-Wrk-Offln.htm?Highlight=Configuring%20CloudShell%20to%20Execute%20Python%20Commands%20in%20Offline%20Mode).

**To add Python packages to the local PyPi Server repository:**
  1. If you haven't created and configured the local PyPi Server repository to work with the execution server, perform the steps in [Add Python packages to the local PyPi Server repository (offline mode)](http://help.quali.com/Online%20Help/9.0/Portal/Content/Admn/Cnfgr-Pyth-Env-Wrk-Offln.htm?Highlight=offline%20dependencies#Add). 
  
  2. For each shell or script you add into CloudShell, do one of the following (from an online computer):
      * Connect to the Internet and download each dependency specified in the *requirements.txt* file with the following command: 
`pip download -r requirements.txt`. 
     The shell or script's requirements are downloaded as zip files.

      * In the [Quali Community's Integrations](https://community.quali.com/integrations) page, locate the shell and click the shell's **Download** link. In the page that is displayed, from the Downloads area, extract the dependencies package zip file.

3. Place these zip files in the local PyPi Server repository.
 
### Setting the Python PythonOfflineRepositoryPath configuration key
Before PyPi Server was introduced as CloudShell’s Python package management mechanism, the `PythonOfflineRepositoryPath` key was used to set the default offline package repository on the Quali Server machine, and could be used on specific Execution Server machines to set a different folder. 

**To set the offline Python repository:**
1. Download the *[Shell Offline Requirements .zip File Name]* file, see [Downloading the Shell](#downloading-the-shell).

2. Unzip it to a local repository. Make sure the execution server has access to this folder. 

3.  On the Quali Server machine, in the *~\CloudShell\Server\customer.config* file, add the following key to specify the path to the default Python package folder (for all Execution Servers):  
	`<add key="PythonOfflineRepositoryPath" value="repository 
full path"/>`

4. If you want to override the default folder for a specific Execution Server, on the Execution Server machine, in the *~TestShell\Execution Server\customer.config* file, add the following key:  
	`<add key="PythonOfflineRepositoryPath" value="repository 
full path"/>`

5. Restart the Execution Server.

### Configuring a new resource
This section explains how to create a new resource from the shell.

In CloudShell, the component that models the device is called a resource. It is based on the shell that models the device and allows the CloudShell user and API to remotely control the device from CloudShell.

You can also modify existing resources, see [Managing Resources in the Inventory](http://help.quali.com/Online%20Help/9.0/Portal/Content/CSP/INVN/Mng-Rsrc-in-Invnt.htm?Highlight=managing%20resources).

**To create a resource for the device:**
  1. In the CloudShell Portal, in the **Inventory** dashboard, click **Add New**. 
     ![](https://github.com/stsuberi/SaraTest/blob/master/create_a_resource_device.png)
     
  2. From the list, select **BreakingPoint Chassis 2G Shell**.
  
  3. Enter the **Name** and **IP address** of the device (if applicable).
  
  4. Click **Create**.
  
  5. In the **Resource** dialog box, enter the device's settings. For details, see [Device Name Attributes](#device-name-attributes). 
  
  6. Click **Continue**. <br><br>CloudShell validates the device’s settings and updates the new resource with the device’s structure (if the device has a structure).

# Updating Python Dependencies for Shells
This section explains how to update your Python dependencies folder. This is required when you upgrade a shell that uses new/updated dependencies. It applies to both online and offline dependencies.

### Updating offline Python dependencies
**To update offline Python dependencies:**
1. Download the latest Python dependencies package zip file locally.

2. Extract the zip file to the suitable offline package folder(s). 

3. Terminate the shell’s instance, as explained [here](http://help.quali.com/Online%20Help/9.0/Portal/Content/CSP/MNG/Mng-Exctn-Srv-Exct.htm#Terminat).

### Updating online Python dependencies
In online mode, the execution server automatically downloads and extracts the appropriate dependencies file to the online Python dependencies repository every time a new instance of the driver or script is created.

**To update online Python dependencies:**
* If there is a live instance of the shell's driver or script, terminate the shell’s instance, as explained [here](http://help.quali.com/Online%20Help/9.0/Portal/Content/CSP/MNG/Mng-Exctn-Srv-Exct.htm#Terminat). If an instance does not exist, the execution server will download the Python dependencies the next time a command of the driver or script runs.

# References
To download and share integrations, see [Quali Community's Integrations](https://community.quali.com/integrations). 

For instructional training and documentation, see [Quali University](https://www.quali.com/university/).

To suggest an idea for the product, see [Quali's Idea box](https://community.quali.com/ideabox). 

To connect with Quali users and experts from around the world, ask questions and discuss issues, see [Quali's Community forums](https://community.quali.com/forums). 

To use traffic generator ports as abstract resources, see [CloudShell's Online Help](https://help.quali.com/Online%20Help/9.1/Portal/Content/CSP/LAB-MNG/Traffic-Gens-Abst.htm?Highlight=traffic%20generator).

## Release Notes
### What's New
For release updates, see the shell's [GitHub releases page](https://github.com/QualiSystems/BreakingPoint-Chassis-Shell-2G/releases/tag/1.0.0).