# Addfunction Group

```python
addfunction_group_controller = client.addfunction_group
```

## Class Name

`AddfunctionGroupController`

## Methods

* [Mrd Addfunction Group](../../doc/controllers/addfunction-group.md#mrd-addfunction-group)
* [Mrd Addfunction Group 1](../../doc/controllers/addfunction-group.md#mrd-addfunction-group-1)


# Mrd Addfunction Group

```python
def mrd_addfunction_group(self,
                         accept,
                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`MrdAddfunctionGroupRequest`](../../doc/models/mrd-addfunction-group-request.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = MrdAddfunctionGroupRequest(
    fg_name='DEV',
    created_by='c36701'
)

result = addfunction_group_controller.mrd_addfunction_group(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Mrd Addfunction Group 1

```python
def mrd_addfunction_group_1(self,
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

result = addfunction_group_controller.mrd_addfunction_group_1(accept)
print(result)
```

## Example Response

```
{}
```

