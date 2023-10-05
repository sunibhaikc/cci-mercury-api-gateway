# Edit FM

```python
edit_fm_controller = client.edit_fm
```

## Class Name

`EditFMController`

## Methods

* [Mrd Edit FM](../../doc/controllers/edit-fm.md#mrd-edit-fm)
* [Mrd Edit FM1](../../doc/controllers/edit-fm.md#mrd-edit-fm1)


# Mrd Edit FM

```python
def mrd_edit_fm(self,
               accept,
               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`MrdEditFMRequest`](../../doc/models/mrd-edit-fm-request.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = MrdEditFMRequest(
    fm_id='516',
    f_id='1602065',
    org_id='1000',
    q_id='11',
    last_modified_by='c36701',
    fg_id='1400001',
    sfg_id='1500001',
    f_desc='XED-CCOps Test Function',
    activeflag='Y'
)

result = edit_fm_controller.mrd_edit_fm(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Mrd Edit FM1

```python
def mrd_edit_fm_1(self,
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

result = edit_fm_controller.mrd_edit_fm_1(accept)
print(result)
```

## Example Response

```
{}
```

