# Edit Lsg

```python
edit_lsg_controller = client.edit_lsg
```

## Class Name

`EditLsgController`

## Methods

* [Mrd Edit Lsg](../../doc/controllers/edit-lsg.md#mrd-edit-lsg)
* [Mrd Edit Lsg 1](../../doc/controllers/edit-lsg.md#mrd-edit-lsg-1)


# Mrd Edit Lsg

```python
def mrd_edit_lsg(self,
                accept,
                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`MrdEditLsgRequest`](../../doc/models/mrd-edit-lsg-request.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = MrdEditLsgRequest(
    lsg_id='1434',
    lsg_name='Zodiac1',
    last_modified_by='c36701'
)

result = edit_lsg_controller.mrd_edit_lsg(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Mrd Edit Lsg 1

```python
def mrd_edit_lsg_1(self,
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

result = edit_lsg_controller.mrd_edit_lsg_1(accept)
print(result)
```

## Example Response

```
{}
```

