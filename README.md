
# Getting Started with cci-mercury-api-gateway_postman

## Introduction

ui driven urls

## Building

You must have Python `3 >=3.7, <= 3.11` installed on your system to install and run this SDK. This SDK package depends on other Python packages like pytest, jsonpickle etc. These dependencies are defined in the `requirements.txt` file that comes with the SDK. To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type `pip --version`. This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including `requirements.txt`) for the SDK.
* Run the command `pip install -r requirements.txt`. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Ccimercuryapigatewaypostman-Python&step=installDependencies)

## Installation

The following section explains how to use the ccimercuryapigatewaypostman library in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Ccimercuryapigatewaypostman-Python&step=pyCharm)

Click on `Open` in PyCharm to browse to your generated SDK directory and then click `OK`.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Ccimercuryapigatewaypostman-Python&step=openProject0)

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Ccimercuryapigatewaypostman-Python&projectName=ccimercuryapigatewaypostman&step=openProject1)

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Ccimercuryapigatewaypostman-Python&projectName=ccimercuryapigatewaypostman&step=createDirectory)

Name the directory as "test".

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Ccimercuryapigatewaypostman-Python&step=nameDirectory)

Add a python file to this project.

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Ccimercuryapigatewaypostman-Python&projectName=ccimercuryapigatewaypostman&step=createFile)

Name it "testSDK".

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?workspaceFolder=Ccimercuryapigatewaypostman-Python&projectName=ccimercuryapigatewaypostman&step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```python
from ccimercuryapigatewaypostman.ccimercuryapigatewaypostman_client import CcimercuryapigatewaypostmanClient
```

![Add a new project in PyCharm - Step 5](https://apidocs.io/illustration/python?workspaceFolder=Ccimercuryapigatewaypostman-Python&projectName=ccimercuryapigatewaypostman&libraryName=ccimercuryapigatewaypostman.ccimercuryapigatewaypostman_client&className=CcimercuryapigatewaypostmanClient&step=projectFiles)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on `Run`

![Run Test Project - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Ccimercuryapigatewaypostman-Python&projectName=ccimercuryapigatewaypostman&libraryName=ccimercuryapigatewaypostman.ccimercuryapigatewaypostman_client&className=CcimercuryapigatewaypostmanClient&step=runProject)

## Test the SDK

You can test the generated SDK and the server with test cases. `unittest` is used as the testing framework and `pytest` is used as the test runner. You can run the tests as follows:

Navigate to the root directory of the SDK and run the following commands

```
pip install -r test-requirements.txt
pytest
```

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `environment` | Environment | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `http_call_back` | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |

The API client can be initialized as follows:

```python
from ccimercuryapigatewaypostman.ccimercuryapigatewaypostman_client import CcimercuryapigatewaypostmanClient
from ccimercuryapigatewaypostman.configuration import Environment

client = CcimercuryapigatewaypostmanClient()
```

## List of APIs

* [Get Stats Refresh](doc/controllers/get-stats-refresh.md)
* [Getdashboardview](doc/controllers/getdashboardview.md)
* [Listallview](doc/controllers/listallview.md)
* [Mapdashboardview](doc/controllers/mapdashboardview.md)
* [Creategroup](doc/controllers/creategroup.md)
* [Deletegroup](doc/controllers/deletegroup.md)
* [Editgroup](doc/controllers/editgroup.md)
* [Getgroups](doc/controllers/getgroups.md)
* [Getusergroup](doc/controllers/getusergroup.md)
* [Getviewbygroup](doc/controllers/getviewbygroup.md)
* [Mapgroupview](doc/controllers/mapgroupview.md)
* [Removegroupview](doc/controllers/removegroupview.md)
* [Get Moa](doc/controllers/get-moa.md)
* [Get Moa Agent](doc/controllers/get-moa-agent.md)
* [Get Resitech](doc/controllers/get-resitech.md)
* [Get View Meta](doc/controllers/get-view-meta.md)
* [Add Language](doc/controllers/add-language.md)
* [Add Lg](doc/controllers/add-lg.md)
* [Add Lob](doc/controllers/add-lob.md)
* [Add Lsg](doc/controllers/add-lsg.md)
* [Add S Lob](doc/controllers/add-s-lob.md)
* [Addfunction Group](doc/controllers/addfunction-group.md)
* [Addfunctioncode](doc/controllers/addfunctioncode.md)
* [Addlocation](doc/controllers/addlocation.md)
* [Addorganization](doc/controllers/addorganization.md)
* [Addsubfunction Group](doc/controllers/addsubfunction-group.md)
* [Edit FM](doc/controllers/edit-fm.md)
* [Edit Language](doc/controllers/edit-language.md)
* [Edit Lg](doc/controllers/edit-lg.md)
* [Edit Lob](doc/controllers/edit-lob.md)
* [Edit Lsg](doc/controllers/edit-lsg.md)
* [Edit S Lob](doc/controllers/edit-s-lob.md)
* [Editforecasted Group](doc/controllers/editforecasted-group.md)
* [Editfunction Code](doc/controllers/editfunction-code.md)
* [Editfunction Group](doc/controllers/editfunction-group.md)
* [Editfunction Mapping](doc/controllers/editfunction-mapping.md)
* [Editlocation](doc/controllers/editlocation.md)
* [Editmercurylite](doc/controllers/editmercurylite.md)
* [Editorganization](doc/controllers/editorganization.md)
* [Editstaffing Group](doc/controllers/editstaffing-group.md)
* [Editsubfunction Group](doc/controllers/editsubfunction-group.md)
* [Get Language](doc/controllers/get-language.md)
* [Get Master Reference Data](doc/controllers/get-master-reference-data.md)
* [Get Mercurylite](doc/controllers/get-mercurylite.md)
* [Get Popup](doc/controllers/get-popup.md)
* [Getlocation](doc/controllers/getlocation.md)
* [Get FM](doc/controllers/get-fm.md)
* [Add Template](doc/controllers/add-template.md)
* [Del Template](doc/controllers/del-template.md)
* [Drop Down](doc/controllers/drop-down.md)
* [Edit Template](doc/controllers/edit-template.md)
* [Get Template](doc/controllers/get-template.md)
* [Getby Id](doc/controllers/getby-id.md)
* [Checkusergroup](doc/controllers/checkusergroup.md)
* [Createuser](doc/controllers/createuser.md)
* [Edituser](doc/controllers/edituser.md)
* [Getusers](doc/controllers/getusers.md)
* [My Permissions](doc/controllers/my-permissions.md)
* [Updatelastlogindate](doc/controllers/updatelastlogindate.md)
* [Getuserbygroup](doc/controllers/getuserbygroup.md)
* [Mapgroupuser](doc/controllers/mapgroupuser.md)
* [Mapusergroup](doc/controllers/mapusergroup.md)
* [Removeusergroup](doc/controllers/removeusergroup.md)
* [Get U Setting](doc/controllers/get-u-setting.md)
* [Set U Settings](doc/controllers/set-u-settings.md)
* [Add View](doc/controllers/add-view.md)
* [Delete Views](doc/controllers/delete-views.md)
* [Generate View](doc/controllers/generate-view.md)
* [Get Agent Details by COE](doc/controllers/get-agent-details-by-coe.md)
* [Get All Views](doc/controllers/get-all-views.md)
* [Get Data](doc/controllers/get-data.md)
* [Get Half Hour Child Detail](doc/controllers/get-half-hour-child-detail.md)
* [Get View](doc/controllers/get-view.md)
* [Setviewdefault](doc/controllers/setviewdefault.md)
* [Setviewfavorite](doc/controllers/setviewfavorite.md)
* [Shareview](doc/controllers/shareview.md)
* [Shareviewlogs](doc/controllers/shareviewlogs.md)
* [Toggle Change](doc/controllers/toggle-change.md)
* [Viewconfig](doc/controllers/viewconfig.md)

## Classes Documentation

* [Utility Classes](doc/utility-classes.md)
* [HttpResponse](doc/http-response.md)
* [HttpRequest](doc/http-request.md)

