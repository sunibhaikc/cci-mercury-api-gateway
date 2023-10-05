# Toggle Change

```python
toggle_change_controller = client.toggle_change
```

## Class Name

`ToggleChangeController`

## Methods

* [View Toggle Change](../../doc/controllers/toggle-change.md#view-toggle-change)
* [View Toggle Change 1](../../doc/controllers/toggle-change.md#view-toggle-change-1)


# View Toggle Change

```python
def view_toggle_change(self,
                      accept,
                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`ViewToggleChangeRequest`](../../doc/models/view-toggle-change-request.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = ViewToggleChangeRequest(
    user_id='c27116',
    toggle='ON'
)

result = toggle_change_controller.view_toggle_change(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# View Toggle Change 1

```python
def view_toggle_change_1(self,
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

result = toggle_change_controller.view_toggle_change_1(accept)
print(result)
```

## Example Response

```
{}
```

