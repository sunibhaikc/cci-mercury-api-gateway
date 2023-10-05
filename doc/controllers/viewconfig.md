# Viewconfig

```python
viewconfig_controller = client.viewconfig
```

## Class Name

`ViewconfigController`

## Methods

* [View Viewconfig](../../doc/controllers/viewconfig.md#view-viewconfig)
* [View Viewconfig 1](../../doc/controllers/viewconfig.md#view-viewconfig-1)


# View Viewconfig

```python
def view_viewconfig(self,
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

result = viewconfig_controller.view_viewconfig(accept)
print(result)
```

## Example Response

```
{}
```


# View Viewconfig 1

```python
def view_viewconfig_1(self,
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

result = viewconfig_controller.view_viewconfig_1(accept)
print(result)
```

## Example Response

```
{}
```

