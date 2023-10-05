# Add Lob

```python
add_lob_controller = client.add_lob
```

## Class Name

`AddLobController`

## Methods

* [Mrd Add Lob](../../doc/controllers/add-lob.md#mrd-add-lob)
* [Mrd Add Lob 1](../../doc/controllers/add-lob.md#mrd-add-lob-1)


# Mrd Add Lob

```python
def mrd_add_lob(self,
               accept,
               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`MrdAddLobRequest`](../../doc/models/mrd-add-lob-request.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = MrdAddLobRequest(
    lob_cd='G',
    lob_name='git',
    short_name='github',
    created_by='c09739'
)

result = add_lob_controller.mrd_add_lob(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Mrd Add Lob 1

```python
def mrd_add_lob_1(self,
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

result = add_lob_controller.mrd_add_lob_1(accept)
print(result)
```

## Example Response

```
{}
```

