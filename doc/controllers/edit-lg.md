# Edit Lg

```python
edit_lg_controller = client.edit_lg
```

## Class Name

`EditLgController`

## Methods

* [Mrd Edit Lg](../../doc/controllers/edit-lg.md#mrd-edit-lg)
* [Mrd Edit Lg 1](../../doc/controllers/edit-lg.md#mrd-edit-lg-1)


# Mrd Edit Lg

```python
def mrd_edit_lg(self,
               accept,
               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`MrdEditLgRequest`](../../doc/models/mrd-edit-lg-request.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = MrdEditLgRequest(
    lg_cd='FDR',
    lg_id='1806174',
    lg_name='Development',
    org_id='2984',
    lsg_id='',
    coe_flag='',
    hotel_flag='Y',
    last_modified_by='c36701'
)

result = edit_lg_controller.mrd_edit_lg(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Mrd Edit Lg 1

```python
def mrd_edit_lg_1(self,
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

result = edit_lg_controller.mrd_edit_lg_1(accept)
print(result)
```

## Example Response

```
{}
```

