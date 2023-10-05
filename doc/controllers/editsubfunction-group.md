# Editsubfunction Group

```python
editsubfunction_group_controller = client.editsubfunction_group
```

## Class Name

`EditsubfunctionGroupController`

## Methods

* [Mrd Editsubfunction Group](../../doc/controllers/editsubfunction-group.md#mrd-editsubfunction-group)
* [Mrd Editsubfunction Group 1](../../doc/controllers/editsubfunction-group.md#mrd-editsubfunction-group-1)


# Mrd Editsubfunction Group

```python
def mrd_editsubfunction_group(self,
                             accept,
                             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`MrdEditsubfunctionGroupRequest`](../../doc/models/mrd-editsubfunction-group-request.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = MrdEditsubfunctionGroupRequest(
    sfg_name='develop',
    fg_id='1401463',
    last_modified_by='c36701',
    sfg_id='1501863'
)

result = editsubfunction_group_controller.mrd_editsubfunction_group(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Mrd Editsubfunction Group 1

```python
def mrd_editsubfunction_group_1(self,
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

result = editsubfunction_group_controller.mrd_editsubfunction_group_1(accept)
print(result)
```

## Example Response

```
{}
```

