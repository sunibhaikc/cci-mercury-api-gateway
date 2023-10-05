# Drop Down

```python
drop_down_controller = client.drop_down
```

## Class Name

`DropDownController`

## Methods

* [Template Filter Drop Down](../../doc/controllers/drop-down.md#template-filter-drop-down)
* [Template Filter Drop Down 1](../../doc/controllers/drop-down.md#template-filter-drop-down-1)


# Template Filter Drop Down

```python
def template_filter_drop_down(self,
                             accept,
                             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`TemplateFilterDropDownRequest`](../../doc/models/template-filter-drop-down-request.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = TemplateFilterDropDownRequest(
    user_id='C36701',
    mtype='SLOB',
    parent_id='1200145,1200023,1200247,1200021,1200024,1200226,1200306,1200165,1200125,1200248,1200022,1200308,1200206,1200085,1200086,1200065,1200025,1200307,1200227,1200001,1200105,1200185,1200107,1200087,1200106,1200327'
)

result = drop_down_controller.template_filter_drop_down(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Template Filter Drop Down 1

```python
def template_filter_drop_down_1(self,
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

result = drop_down_controller.template_filter_drop_down_1(accept)
print(result)
```

## Example Response

```
{}
```

