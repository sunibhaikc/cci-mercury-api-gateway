# Shareviewlogs

```python
shareviewlogs_controller = client.shareviewlogs
```

## Class Name

`ShareviewlogsController`

## Methods

* [View Shareviewlogs](../../doc/controllers/shareviewlogs.md#view-shareviewlogs)
* [View Shareviewlogs 1](../../doc/controllers/shareviewlogs.md#view-shareviewlogs-1)


# View Shareviewlogs

```python
def view_shareviewlogs(self,
                      accept,
                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`ViewShareviewlogsrequest`](../../doc/models/view-shareviewlogsrequest.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = ViewShareviewlogsrequest(
    view_id='VIEW_917',
    user_id='C27116'
)

result = shareviewlogs_controller.view_shareviewlogs(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# View Shareviewlogs 1

```python
def view_shareviewlogs_1(self,
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

result = shareviewlogs_controller.view_shareviewlogs_1(accept)
print(result)
```

## Example Response

```
{}
```

