# Getdashboardview

```python
getdashboardview_controller = client.getdashboardview
```

## Class Name

`GetdashboardviewController`

## Methods

* [Dashboard Getdashboardview](../../doc/controllers/getdashboardview.md#dashboard-getdashboardview)
* [Dashboard Getdashboardview 1](../../doc/controllers/getdashboardview.md#dashboard-getdashboardview-1)


# Dashboard Getdashboardview

```python
def dashboard_getdashboardview(self,
                              accept,
                              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`DashboardGetdashboardviewrequest`](../../doc/models/dashboard-getdashboardviewrequest.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = DashboardGetdashboardviewrequest(
    user_id='c27116'
)

result = getdashboardview_controller.dashboard_getdashboardview(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Dashboard Getdashboardview 1

```python
def dashboard_getdashboardview_1(self,
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

result = getdashboardview_controller.dashboard_getdashboardview_1(accept)
print(result)
```

## Example Response

```
{}
```

