# Edit S Lob

```python
edit_s_lob_controller = client.edit_s_lob
```

## Class Name

`EditSLobController`

## Methods

* [Mrd Edit S Lob](../../doc/controllers/edit-s-lob.md#mrd-edit-s-lob)
* [Mrd Edit S Lob 1](../../doc/controllers/edit-s-lob.md#mrd-edit-s-lob-1)


# Mrd Edit S Lob

```python
def mrd_edit_s_lob(self,
                  accept,
                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`MrdEditSLobRequest`](../../doc/models/mrd-edit-s-lob-request.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = MrdEditSLobRequest(
    slob_id='1300025',
    slob_name='Back Office',
    lob_id='1200022',
    last_modified_by='c09739'
)

result = edit_s_lob_controller.mrd_edit_s_lob(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Mrd Edit S Lob 1

```python
def mrd_edit_s_lob_1(self,
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

result = edit_s_lob_controller.mrd_edit_s_lob_1(accept)
print(result)
```

## Example Response

```
{}
```

