# Add Lg

```python
add_lg_controller = client.add_lg
```

## Class Name

`AddLgController`

## Methods

* [Mrd Add Lg](../../doc/controllers/add-lg.md#mrd-add-lg)
* [Mrd Add Lg 1](../../doc/controllers/add-lg.md#mrd-add-lg-1)


# Mrd Add Lg

```python
def mrd_add_lg(self,
              accept,
              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`MrdAddLgRequest`](../../doc/models/mrd-add-lg-request.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = MrdAddLgRequest(
    lg_cd='FDC',
    lg_name='Dev',
    org_id='2984',
    lsg_id='',
    coe_flag='',
    hotel_flag='Y',
    created_by='c36701'
)

result = add_lg_controller.mrd_add_lg(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Mrd Add Lg 1

```python
def mrd_add_lg_1(self,
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

result = add_lg_controller.mrd_add_lg_1(accept)
print(result)
```

## Example Response

```
{}
```

