# Setviewfavorite

```python
setviewfavorite_controller = client.setviewfavorite
```

## Class Name

`SetviewfavoriteController`

## Methods

* [View Setviewfavorite](../../doc/controllers/setviewfavorite.md#view-setviewfavorite)
* [View Setviewfavorite 1](../../doc/controllers/setviewfavorite.md#view-setviewfavorite-1)


# View Setviewfavorite

```python
def view_setviewfavorite(self,
                        accept,
                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`ViewSetviewfavoriterequest`](../../doc/models/view-setviewfavoriterequest.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = ViewSetviewfavoriterequest(
    user_id='c27116',
    view_id=[
        'VIEW_917'
    ]
)

result = setviewfavorite_controller.view_setviewfavorite(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# View Setviewfavorite 1

```python
def view_setviewfavorite_1(self,
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

result = setviewfavorite_controller.view_setviewfavorite_1(accept)
print(result)
```

## Example Response

```
{}
```

