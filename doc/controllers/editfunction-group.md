# Editfunction Group

```python
editfunction_group_controller = client.editfunction_group
```

## Class Name

`EditfunctionGroupController`

## Methods

* [Mrd Editfunction Group](../../doc/controllers/editfunction-group.md#mrd-editfunction-group)
* [Mrd Editfunction Group 1](../../doc/controllers/editfunction-group.md#mrd-editfunction-group-1)


# Mrd Editfunction Group

```python
def mrd_editfunction_group(self,
                          accept,
                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`MrdEditfunctionGroupRequest`](../../doc/models/mrd-editfunction-group-request.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = MrdEditfunctionGroupRequest(
    fg_id='1401503',
    fg_name='Develop',
    last_modified_by='c36701'
)

result = editfunction_group_controller.mrd_editfunction_group(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Mrd Editfunction Group 1

```python
def mrd_editfunction_group_1(self,
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

result = editfunction_group_controller.mrd_editfunction_group_1(accept)
print(result)
```

## Example Response

```
{}
```

