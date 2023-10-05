# Listallview

```python
listallview_controller = client.listallview
```

## Class Name

`ListallviewController`

## Methods

* [Dashboard Listallview](../../doc/controllers/listallview.md#dashboard-listallview)
* [Dashboard Listallview 1](../../doc/controllers/listallview.md#dashboard-listallview-1)


# Dashboard Listallview

```python
def dashboard_listallview(self,
                         accept,
                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`DashboardListallviewrequest`](../../doc/models/dashboard-listallviewrequest.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = DashboardListallviewrequest(
    user_id='C27116'
)

result = listallview_controller.dashboard_listallview(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Dashboard Listallview 1

```python
def dashboard_listallview_1(self,
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

result = listallview_controller.dashboard_listallview_1(accept)
print(result)
```

## Example Response

```
{}
```

