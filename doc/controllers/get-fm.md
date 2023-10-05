# Get FM

```python
get_fm_controller = client.get_fm
```

## Class Name

`GetFMController`

## Methods

* [Mrd Get FM](../../doc/controllers/get-fm.md#mrd-get-fm)
* [Mrd Get FM1](../../doc/controllers/get-fm.md#mrd-get-fm1)


# Mrd Get FM

```python
def mrd_get_fm(self,
              accept,
              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`MrdGetFMRequest`](../../doc/models/mrd-get-fm-request.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = MrdGetFMRequest(
    user_id='c36701',
    page_name='FM'
)

result = get_fm_controller.mrd_get_fm(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Mrd Get FM1

```python
def mrd_get_fm_1(self,
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

result = get_fm_controller.mrd_get_fm_1(accept)
print(result)
```

## Example Response

```
{}
```

