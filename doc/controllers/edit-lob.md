# Edit Lob

```python
edit_lob_controller = client.edit_lob
```

## Class Name

`EditLobController`

## Methods

* [Mrd Edit Lob](../../doc/controllers/edit-lob.md#mrd-edit-lob)
* [Mrd Edit Lob 1](../../doc/controllers/edit-lob.md#mrd-edit-lob-1)


# Mrd Edit Lob

```python
def mrd_edit_lob(self,
                accept,
                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`MrdEditLobRequest`](../../doc/models/mrd-edit-lob-request.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = MrdEditLobRequest(
    lob_id='1200105',
    lob_name='cox media1',
    short_name='flob14',
    last_modified_by='c09739'
)

result = edit_lob_controller.mrd_edit_lob(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Mrd Edit Lob 1

```python
def mrd_edit_lob_1(self,
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

result = edit_lob_controller.mrd_edit_lob_1(accept)
print(result)
```

## Example Response

```
{}
```

