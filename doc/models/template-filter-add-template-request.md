
# Template Filter Add Template Request

## Structure

`TemplateFilterAddTemplateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `str` | Required | - |
| `temp_name` | `str` | Required | - |
| `org_ids` | `str` | Required | - |
| `org_desc` | `str` | Required | - |
| `lob_ids` | `str` | Required | - |
| `lob_desc` | `str` | Required | - |
| `slob_ids` | `str` | Required | - |
| `slob_desc` | `str` | Required | - |
| `fg_ids` | `str` | Required | - |
| `fg_desc` | `str` | Required | - |
| `sfg_ids` | `str` | Required | - |
| `sfg_desc` | `str` | Required | - |
| `func_ids` | `str` | Required | - |
| `func_desc` | `str` | Required | - |
| `lng_ids` | `str` | Required | - |
| `lng_desc` | `str` | Required | - |
| `cust_reg_ids` | `str` | Required | - |
| `cust_reg_desc` | `str` | Required | - |
| `coe_ids` | `str` | Required | - |
| `coe_desc` | `str` | Required | - |

## Example (as JSON)

```json
{
  "userId": "C36701",
  "tempName": "Templatefilter",
  "orgIds": "0",
  "orgDesc": "ALL",
  "lobIds": "0",
  "lobDesc": "ALL",
  "slobIds": "0",
  "slobDesc": "ALL",
  "fgIds": "0",
  "fgDesc": "ALL",
  "sfgIds": "1501001,1500192,1501161,1500441,1501241,1500981,1501301,1501181,1501061,1500501",
  "sfgDesc": "ASC,Abuse & Fraud,3rd Party Sales Support,Advanced Service Center,Advanced Convention Services - Service Desk,Agency Recovery Management,CB Fulfillment,CB Access Transport Tech,Bulk Owner Support,CB Network Provisioning",
  "funcIds": "1600429,1600427,1613419,1631354,1610793",
  "funcDesc": "Accessibility Tech,Accessibility Billing,Agency Recovery Management,Agent Transfer Comm Center Missed Go Back,Alarm.com",
  "lngIds": "1100024,1249,1100026,1045,1100045,1182,1100021,1003,1100028",
  "lngDesc": "Bravvo,Bhojpuri1,Bangla,Lang,Karanjohar,KILKI1,English,French,INDIA",
  "custRegIds": "0",
  "custRegDesc": "ALL",
  "coeIds": "0",
  "coeDesc": "ALL"
}
```

