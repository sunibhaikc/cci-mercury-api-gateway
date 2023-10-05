# Add Template

```python
add_template_controller = client.add_template
```

## Class Name

`AddTemplateController`

## Methods

* [Template Filter Add Template](../../doc/controllers/add-template.md#template-filter-add-template)
* [Template Filter Add Template 1](../../doc/controllers/add-template.md#template-filter-add-template-1)


# Template Filter Add Template

```python
def template_filter_add_template(self,
                                accept,
                                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`TemplateFilterAddTemplateRequest`](../../doc/models/template-filter-add-template-request.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = TemplateFilterAddTemplateRequest(
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
    sfg_ids='1501001,1500192,1501161,1500441,1501241,1500981,1501301,1501181,1501061,1500501',
    sfg_desc='ASC,Abuse & Fraud,3rd Party Sales Support,Advanced Service Center,Advanced Convention Services - Service Desk,Agency Recovery Management,CB Fulfillment,CB Access Transport Tech,Bulk Owner Support,CB Network Provisioning',
    func_ids='1600429,1600427,1613419,1631354,1610793',
    func_desc='Accessibility Tech,Accessibility Billing,Agency Recovery Management,Agent Transfer Comm Center Missed Go Back,Alarm.com',
    lng_ids='1100024,1249,1100026,1045,1100045,1182,1100021,1003,1100028',
    lng_desc='Bravvo,Bhojpuri1,Bangla,Lang,Karanjohar,KILKI1,English,French,INDIA',
    cust_reg_ids='0',
    cust_reg_desc='ALL',
    coe_ids='0',
    coe_desc='ALL'
)

result = add_template_controller.template_filter_add_template(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Template Filter Add Template 1

```python
def template_filter_add_template_1(self,
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

result = add_template_controller.template_filter_add_template_1(accept)
print(result)
```

## Example Response

```
{}
```

