# Editstaffing Group

```python
editstaffing_group_controller = client.editstaffing_group
```

## Class Name

`EditstaffingGroupController`

## Methods

* [Mrd Editstaffing Group](../../doc/controllers/editstaffing-group.md#mrd-editstaffing-group)
* [Mrd Editstaffing Group 1](../../doc/controllers/editstaffing-group.md#mrd-editstaffing-group-1)


# Mrd Editstaffing Group

```python
def mrd_editstaffing_group(self,
                          accept,
                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`MrdEditstaffingGroupRequest`](../../doc/models/mrd-editstaffing-group-request.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = MrdEditstaffingGroupRequest(
    lang_id='1100021',
    org_id='2984',
    slob_id='1300024',
    sfg_id='1500187',
    comments='QA-Testing',
    wfm_sg_id='40',
    last_modified_by='C36701'
)

result = editstaffing_group_controller.mrd_editstaffing_group(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Mrd Editstaffing Group 1

```python
def mrd_editstaffing_group_1(self,
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

result = editstaffing_group_controller.mrd_editstaffing_group_1(accept)
print(result)
```

## Example Response

```
{}
```

