# Get Data

```python
get_data_controller = client.get_data
```

## Class Name

`GetDataController`

## Methods

* [View Get Data](../../doc/controllers/get-data.md#view-get-data)
* [View Get Data 1](../../doc/controllers/get-data.md#view-get-data-1)


# View Get Data

```python
def view_get_data(self,
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

result = get_data_controller.view_get_data(accept)
print(result)
```

## Example Response

```
{}
```


# View Get Data 1

```python
def view_get_data_1(self,
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

result = get_data_controller.view_get_data_1(accept)
print(result)
```

## Example Response

```
{}
```

