# Add Lsg

```python
add_lsg_controller = client.add_lsg
```

## Class Name

`AddLsgController`

## Methods

* [Mrd Add Lsg](../../doc/controllers/add-lsg.md#mrd-add-lsg)
* [Mrd Add Lsg 1](../../doc/controllers/add-lsg.md#mrd-add-lsg-1)


# Mrd Add Lsg

```python
def mrd_add_lsg(self,
               accept,
               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`MrdAddLsgRequest`](../../doc/models/mrd-add-lsg-request.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = MrdAddLsgRequest(
    lsg_cd='ZSW',
    lsg_name='Zodiac',
    created_by='c36701'
)

result = add_lsg_controller.mrd_add_lsg(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Mrd Add Lsg 1

```python
def mrd_add_lsg_1(self,
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

result = add_lsg_controller.mrd_add_lsg_1(accept)
print(result)
```

## Example Response

```
{}
```

