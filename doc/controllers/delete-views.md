# Delete Views

```python
delete_views_controller = client.delete_views
```

## Class Name

`DeleteViewsController`

## Methods

* [View Delete Views](../../doc/controllers/delete-views.md#view-delete-views)
* [View Delete Views 1](../../doc/controllers/delete-views.md#view-delete-views-1)


# View Delete Views

```python
def view_delete_views(self,
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

result = delete_views_controller.view_delete_views(accept)
print(result)
```

## Example Response

```
{}
```


# View Delete Views 1

```python
def view_delete_views_1(self,
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

result = delete_views_controller.view_delete_views_1(accept)
print(result)
```

## Example Response

```
{}
```

