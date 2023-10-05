# Editforecasted Group

```python
editforecasted_group_controller = client.editforecasted_group
```

## Class Name

`EditforecastedGroupController`

## Methods

* [Mrd Editforecasted Group](../../doc/controllers/editforecasted-group.md#mrd-editforecasted-group)
* [Mrd Editforecasted Group 1](../../doc/controllers/editforecasted-group.md#mrd-editforecasted-group-1)


# Mrd Editforecasted Group

```python
def mrd_editforecasted_group(self,
                            accept,
                            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`MrdEditforecastedGroupRequest`](../../doc/models/mrd-editforecasted-group-request.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = MrdEditforecastedGroupRequest(
    sfg_id='1500001',
    slob_id='1300025',
    lang_id='1100021',
    comments='QA Testpp',
    last_modified_by='C36701',
    org_id='2984',
    wfm_fg_id='101'
)

result = editforecasted_group_controller.mrd_editforecasted_group(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Mrd Editforecasted Group 1

```python
def mrd_editforecasted_group_1(self,
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

result = editforecasted_group_controller.mrd_editforecasted_group_1(accept)
print(result)
```

## Example Response

```
{}
```

