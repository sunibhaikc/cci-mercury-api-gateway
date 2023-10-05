# Editmercurylite

```python
editmercurylite_controller = client.editmercurylite
```

## Class Name

`EditmercuryliteController`

## Methods

* [Mrd Editmercurylite](../../doc/controllers/editmercurylite.md#mrd-editmercurylite)
* [Mrd Editmercurylite 1](../../doc/controllers/editmercurylite.md#mrd-editmercurylite-1)


# Mrd Editmercurylite

```python
def mrd_editmercurylite(self,
                       accept,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`MrdEditmercuryliterequest`](../../doc/models/mrd-editmercuryliterequest.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = MrdEditmercuryliterequest(
    viewname='be122',
    view_id='VIEW_902',
    temp_id='473',
    updated_by='C36701'
)

result = editmercurylite_controller.mrd_editmercurylite(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Mrd Editmercurylite 1

```python
def mrd_editmercurylite_1(self,
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

result = editmercurylite_controller.mrd_editmercurylite_1(accept)
print(result)
```

## Example Response

```
{}
```

