# Edit Template

```python
edit_template_controller = client.edit_template
```

## Class Name

`EditTemplateController`

## Methods

* [Template Filter Edit Template](../../doc/controllers/edit-template.md#template-filter-edit-template)
* [Template Filter Edit Template 1](../../doc/controllers/edit-template.md#template-filter-edit-template-1)


# Template Filter Edit Template

```python
def template_filter_edit_template(self,
                                 accept,
                                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`TemplateFilterEditTemplateRequest`](../../doc/models/template-filter-edit-template-request.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = TemplateFilterEditTemplateRequest(
    user_id='C36701',
    temp_name='Templatefilter',
    org_ids='0',
    org_desc='ALL',
    lob_ids='0',
    lob_desc='ALL',
    slob_ids='0',
    slob_desc='ALL',
    fg_ids='0',
    fg_desc='ALL',
    sfg_ids='1501161,1501001,1501241,1500441,1500981,1501061,1501181,1501301,1500501',
    sfg_desc='3rd Party Sales Support,ASC,Advanced Convention Services - Service Desk,Advanced Service Center,Agency Recovery Management,Bulk Owner Support,CB Access Transport Tech,CB Fulfillment,CB Network Provisioning',
    func_ids='1600427,1600429,1613419,1631354,1610793,1632938,1621495,1606337',
    func_desc='Accessibility Billing,Accessibility Tech,Agency Recovery Management,Agent Transfer Comm Center Missed Go Back,Alarm.com,Activation Support,Account Compromised 1,Advanced Convention Services - Service Desk',
    lng_ids='1100026,1249,1100024,1100021,1003,1100028,1182,1100045,1045',
    lng_desc='Bangla,Bhojpuri1,Bravvo,English,French,INDIA,KILKI1,Karanjohar,Lang',
    cust_reg_ids='0',
    cust_reg_desc='ALL',
    coe_ids='0',
    coe_desc='ALL',
    template_id='733'
)

result = edit_template_controller.template_filter_edit_template(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Template Filter Edit Template 1

```python
def template_filter_edit_template_1(self,
                                   accept)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

result = edit_template_controller.template_filter_edit_template_1(accept)
print(result)
```

## Example Response

```
{}
```

