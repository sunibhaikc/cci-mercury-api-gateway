
# Template Filter Edit Template Request

## Structure

`TemplateFilterEditTemplateRequest`

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
| `template_id` | `str` | Required | - |

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
  "sfgIds": "1501161,1501001,1501241,1500441,1500981,1501061,1501181,1501301,1500501",
  "sfgDesc": "3rd Party Sales Support,ASC,Advanced Convention Services - Service Desk,Advanced Service Center,Agency Recovery Management,Bulk Owner Support,CB Access Transport Tech,CB Fulfillment,CB Network Provisioning",
  "funcIds": "1600427,1600429,1613419,1631354,1610793,1632938,1621495,1606337",
  "funcDesc": "Accessibility Billing,Accessibility Tech,Agency Recovery Management,Agent Transfer Comm Center Missed Go Back,Alarm.com,Activation Support,Account Compromised 1,Advanced Convention Services - Service Desk",
  "lngIds": "1100026,1249,1100024,1100021,1003,1100028,1182,1100045,1045",
  "lngDesc": "Bangla,Bhojpuri1,Bravvo,English,French,INDIA,KILKI1,Karanjohar,Lang",
  "custRegIds": "0",
  "custRegDesc": "ALL",
  "coeIds": "0",
  "coeDesc": "ALL",
  "templateId": "733"
}
```

