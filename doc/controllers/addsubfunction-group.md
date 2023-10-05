# Addsubfunction Group

```python
addsubfunction_group_controller = client.addsubfunction_group
```

## Class Name

`AddsubfunctionGroupController`

## Methods

* [Mrd Addsubfunction Group](../../doc/controllers/addsubfunction-group.md#mrd-addsubfunction-group)
* [Mrd Addsubfunction Group 1](../../doc/controllers/addsubfunction-group.md#mrd-addsubfunction-group-1)


# Mrd Addsubfunction Group

```python
def mrd_addsubfunction_group(self,
                            accept,
                            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`MrdAddsubfunctionGroupRequest`](../../doc/models/mrd-addsubfunction-group-request.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = MrdAddsubfunctionGroupRequest(
    sfg_name='development',
    fg_id='1401463',
    created_by='c36701'
)

result = addsubfunction_group_controller.mrd_addsubfunction_group(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Mrd Addsubfunction Group 1

```python
def mrd_addsubfunction_group_1(self,
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

result = addsubfunction_group_controller.mrd_addsubfunction_group_1(accept)
print(result)
```

## Example Response

```
{}
```

