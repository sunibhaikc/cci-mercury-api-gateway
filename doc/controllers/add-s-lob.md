# Add S Lob

```python
add_s_lob_controller = client.add_s_lob
```

## Class Name

`AddSLobController`

## Methods

* [Mrd Add S Lob](../../doc/controllers/add-s-lob.md#mrd-add-s-lob)
* [Mrd Add S Lob 1](../../doc/controllers/add-s-lob.md#mrd-add-s-lob-1)


# Mrd Add S Lob

```python
def mrd_add_s_lob(self,
                 accept,
                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`MrdAddSLobRequest`](../../doc/models/mrd-add-s-lob-request.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = MrdAddSLobRequest(
    slob_cd='E',
    slob_name='sub',
    lob_id='1200022',
    created_by='c09739'
)

result = add_s_lob_controller.mrd_add_s_lob(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Mrd Add S Lob 1

```python
def mrd_add_s_lob_1(self,
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

result = add_s_lob_controller.mrd_add_s_lob_1(accept)
print(result)
```

## Example Response

```
{}
```

