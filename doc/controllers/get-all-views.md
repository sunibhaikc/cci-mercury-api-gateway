# Get All Views

```python
get_all_views_controller = client.get_all_views
```

## Class Name

`GetAllViewsController`

## Methods

* [View Get All Views](../../doc/controllers/get-all-views.md#view-get-all-views)
* [View Get All Views 1](../../doc/controllers/get-all-views.md#view-get-all-views-1)


# View Get All Views

```python
def view_get_all_views(self,
                      accept,
                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`ViewGetAllViewsRequest`](../../doc/models/view-get-all-views-request.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = ViewGetAllViewsRequest(
    user_id='c27116',
    mtype='all',
    mobile_view=False
)

result = get_all_views_controller.view_get_all_views(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# View Get All Views 1

```python
def view_get_all_views_1(self,
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

result = get_all_views_controller.view_get_all_views_1(accept)
print(result)
```

## Example Response

```
{}
```

