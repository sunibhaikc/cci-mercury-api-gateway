# Shareview

```python
shareview_controller = client.shareview
```

## Class Name

`ShareviewController`

## Methods

* [View Shareview](../../doc/controllers/shareview.md#view-shareview)
* [View Shareview 1](../../doc/controllers/shareview.md#view-shareview-1)


# View Shareview

```python
def view_shareview(self,
                  accept,
                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`ViewShareviewrequest`](../../doc/models/view-shareviewrequest.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = ViewShareviewrequest(
    user_list=[
        'C36701'
    ],
    view_id='VIEW_917',
    user_id='c27116'
)

result = shareview_controller.view_shareview(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# View Shareview 1

```python
def view_shareview_1(self,
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

result = shareview_controller.view_shareview_1(accept)
print(result)
```

## Example Response

```
{}
```

