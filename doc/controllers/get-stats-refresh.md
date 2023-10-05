# Get Stats Refresh

```python
get_stats_refresh_controller = client.get_stats_refresh
```

## Class Name

`GetStatsRefreshController`

## Methods

* [Alert Get Stats Refresh](../../doc/controllers/get-stats-refresh.md#alert-get-stats-refresh)
* [Alert Get Stats Refresh 1](../../doc/controllers/get-stats-refresh.md#alert-get-stats-refresh-1)


# Alert Get Stats Refresh

```python
def alert_get_stats_refresh(self,
                           accept,
                           body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`AlertGetStatsRefreshRequest`](../../doc/models/alert-get-stats-refresh-request.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = AlertGetStatsRefreshRequest(
    user_id='c27116',
    mtype='current'
)

result = get_stats_refresh_controller.alert_get_stats_refresh(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Alert Get Stats Refresh 1

```python
def alert_get_stats_refresh_1(self,
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

result = get_stats_refresh_controller.alert_get_stats_refresh_1(accept)
print(result)
```

## Example Response

```
{}
```

