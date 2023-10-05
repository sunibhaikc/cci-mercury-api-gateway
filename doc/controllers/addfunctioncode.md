# Addfunctioncode

```python
addfunctioncode_controller = client.addfunctioncode
```

## Class Name

`AddfunctioncodeController`

## Methods

* [Mrd Addfunctioncode](../../doc/controllers/addfunctioncode.md#mrd-addfunctioncode)
* [Mrd Addfunctioncode 1](../../doc/controllers/addfunctioncode.md#mrd-addfunctioncode-1)


# Mrd Addfunctioncode

```python
def mrd_addfunctioncode(self,
                       accept,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`MrdAddfunctioncoderequest`](../../doc/models/mrd-addfunctioncoderequest.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = MrdAddfunctioncoderequest(
    f_cd='BBB',
    f_name='77777',
    created_by='C09739'
)

result = addfunctioncode_controller.mrd_addfunctioncode(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Mrd Addfunctioncode 1

```python
def mrd_addfunctioncode_1(self,
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

result = addfunctioncode_controller.mrd_addfunctioncode_1(accept)
print(result)
```

## Example Response

```
{}
```

