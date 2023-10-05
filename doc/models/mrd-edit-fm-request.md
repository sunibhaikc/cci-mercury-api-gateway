
# Mrd Edit FM Request

## Structure

`MrdEditFMRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fm_id` | `str` | Required | - |
| `f_id` | `str` | Required | - |
| `org_id` | `str` | Required | - |
| `q_id` | `str` | Required | - |
| `last_modified_by` | `str` | Required | - |
| `fg_id` | `str` | Required | - |
| `sfg_id` | `str` | Required | - |
| `f_desc` | `str` | Required | - |
| `activeflag` | `str` | Required | - |

## Example (as JSON)

```json
{
  "fmId": "516",
  "fId": "1602065",
  "orgId": "1000",
  "qId": "11",
  "lastModifiedBy": "c36701",
  "fgId": "1400001",
  "sfgId": "1500001",
  "fDesc": "XED-CCOps Test Function",
  "activeflag": "Y"
}
```

