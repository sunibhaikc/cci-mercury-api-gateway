
# Client Class Documentation

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

## cci-mercury-api-gateway_postman Client

The gateway for the SDK. This class acts as a factory for the Controllers and also holds the configuration of the SDK.

## Controllers

| Name | Description |
|  --- | --- |
| get_stats_refresh | Gets GetStatsRefreshController |
| getdashboardview | Gets GetdashboardviewController |
| listallview | Gets ListallviewController |
| mapdashboardview | Gets MapdashboardviewController |
| creategroup | Gets CreategroupController |
| deletegroup | Gets DeletegroupController |
| editgroup | Gets EditgroupController |
| getgroups | Gets GetgroupsController |
| getusergroup | Gets GetusergroupController |
| getviewbygroup | Gets GetviewbygroupController |
| mapgroupview | Gets MapgroupviewController |
| removegroupview | Gets RemovegroupviewController |
| get_moa | Gets GetMoaController |
| get_moa_agent | Gets GetMoaAgentController |
| get_resitech | Gets GetResitechController |
| get_view_meta | Gets GetViewMetaController |
| add_language | Gets AddLanguageController |
| add_lg | Gets AddLgController |
| add_lob | Gets AddLobController |
| add_lsg | Gets AddLsgController |
| add_s_lob | Gets AddSLobController |
| addfunction_group | Gets AddfunctionGroupController |
| addfunctioncode | Gets AddfunctioncodeController |
| addlocation | Gets AddlocationController |
| addorganization | Gets AddorganizationController |
| addsubfunction_group | Gets AddsubfunctionGroupController |
| edit_fm | Gets EditFMController |
| edit_language | Gets EditLanguageController |
| edit_lg | Gets EditLgController |
| edit_lob | Gets EditLobController |
| edit_lsg | Gets EditLsgController |
| edit_s_lob | Gets EditSLobController |
| editforecasted_group | Gets EditforecastedGroupController |
| editfunction_code | Gets EditfunctionCodeController |
| editfunction_group | Gets EditfunctionGroupController |
| editfunction_mapping | Gets EditfunctionMappingController |
| editlocation | Gets EditlocationController |
| editmercurylite | Gets EditmercuryliteController |
| editorganization | Gets EditorganizationController |
| editstaffing_group | Gets EditstaffingGroupController |
| editsubfunction_group | Gets EditsubfunctionGroupController |
| get_language | Gets GetLanguageController |
| get_master_reference_data | Gets GetMasterReferenceDataController |
| get_mercurylite | Gets GetMercuryliteController |
| get_popup | Gets GetPopupController |
| getlocation | Gets GetlocationController |
| get_fm | Gets GetFMController |
| add_template | Gets AddTemplateController |
| del_template | Gets DelTemplateController |
| drop_down | Gets DropDownController |
| edit_template | Gets EditTemplateController |
| get_template | Gets GetTemplateController |
| getby_id | Gets GetbyIdController |
| checkusergroup | Gets CheckusergroupController |
| createuser | Gets CreateuserController |
| edituser | Gets EdituserController |
| getusers | Gets GetusersController |
| my_permissions | Gets MyPermissionsController |
| updatelastlogindate | Gets UpdatelastlogindateController |
| getuserbygroup | Gets GetuserbygroupController |
| mapgroupuser | Gets MapgroupuserController |
| mapusergroup | Gets MapusergroupController |
| removeusergroup | Gets RemoveusergroupController |
| get_u_setting | Gets GetUSettingController |
| set_u_settings | Gets SetUSettingsController |
| add_view | Gets AddViewController |
| delete_views | Gets DeleteViewsController |
| generate_view | Gets GenerateViewController |
| get_agent_details_by_coe | Gets GetAgentDetailsByCOEController |
| get_all_views | Gets GetAllViewsController |
| get_data | Gets GetDataController |
| get_half_hour_child_detail | Gets GetHalfHourChildDetailController |
| get_view | Gets GetViewController |
| setviewdefault | Gets SetviewdefaultController |
| setviewfavorite | Gets SetviewfavoriteController |
| shareview | Gets ShareviewController |
| shareviewlogs | Gets ShareviewlogsController |
| toggle_change | Gets ToggleChangeController |
| viewconfig | Gets ViewconfigController |

