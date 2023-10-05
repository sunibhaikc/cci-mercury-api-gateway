# Get Mercurylite

```python
get_mercurylite_controller = client.get_mercurylite
```

## Class Name

`GetMercuryliteController`

## Methods

* [Mrd Get Mercurylite](../../doc/controllers/get-mercurylite.md#mrd-get-mercurylite)
* [Mrd Get Mercurylite 1](../../doc/controllers/get-mercurylite.md#mrd-get-mercurylite-1)


# Mrd Get Mercurylite

```python
def mrd_get_mercurylite(self,
                       accept,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`MrdGetMercuryliteRequest`](../../doc/models/mrd-get-mercurylite-request.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = MrdGetMercuryliteRequest(
    user_id='C36701',
    page_name='MLITE'
)

result = get_mercurylite_controller.mrd_get_mercurylite(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Mrd Get Mercurylite 1

```python
def mrd_get_mercurylite_1(self,
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

result = get_mercurylite_controller.mrd_get_mercurylite_1(accept)
print(result)
```

## Example Response

```
{}
```

