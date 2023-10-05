
# User Createuserrequest

## Structure

`UserCreateuserrequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `str` | Required | - |
| `user_samaccountname` | `str` | Required | - |
| `user_upn` | `str` | Required | - |
| `user_displayname` | `str` | Required | - |
| `user_name` | `str` | Required | - |
| `user_jobtitle` | `str` | Required | - |
| `user_manager` | `str` | Required | - |
| `user_mail` | `str` | Required | - |
| `user_location` | `str` | Required | - |
| `user_company` | `str` | Required | - |
| `created_by` | `str` | Required | - |
| `user_role` | `List[str]` | Required | - |

## Example (as JSON)

```json
{
  "User_Id": "C27116",
  "User_Samaccountname": "C27116",
  "User_Upn": "Deepak.Dash@cox.com",
  "User_Displayname": "Dash, Deepak (CCI-Atlanta-CON)",
  "User_Name": "Dash Deepak",
  "User_Jobtitle": "Contractor",
  "User_Manager": "",
  "User_Mail": "Deepak.Dash@cox.com",
  "User_Location": "",
  "User_Company": "Genpact LLC",
  "Created_By": "C27116",
  "User_Role": [
    "CCI_CLD_Mercury_Administrator"
  ]
}
```

