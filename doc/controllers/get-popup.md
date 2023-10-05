# Get Popup

```python
get_popup_controller = client.get_popup
```

## Class Name

`GetPopupController`

## Methods

* [Mrd Get Popup](../../doc/controllers/get-popup.md#mrd-get-popup)
* [Mrd Get Popup 1](../../doc/controllers/get-popup.md#mrd-get-popup-1)


# Mrd Get Popup

```python
def mrd_get_popup(self,
                 accept,
                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`MrdGetPopupRequest`](../../doc/models/mrd-get-popup-request.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = MrdGetPopupRequest(
    q_id='504',
    org_id='1000'
)

result = get_popup_controller.mrd_get_popup(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Mrd Get Popup 1

```python
def mrd_get_popup_1(self,
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

result = get_popup_controller.mrd_get_popup_1(accept)
print(result)
```

## Example Response

```
{}
```

