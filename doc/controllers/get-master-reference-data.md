# Get Master Reference Data

```python
get_master_reference_data_controller = client.get_master_reference_data
```

## Class Name

`GetMasterReferenceDataController`

## Methods

* [Mrd Get Master Reference Data](../../doc/controllers/get-master-reference-data.md#mrd-get-master-reference-data)
* [Mrd Get Master Reference Data 1](../../doc/controllers/get-master-reference-data.md#mrd-get-master-reference-data-1)


# Mrd Get Master Reference Data

```python
def mrd_get_master_reference_data(self,
                                 accept,
                                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`MrdGetMasterReferenceDataRequest`](../../doc/models/mrd-get-master-reference-data-request.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = MrdGetMasterReferenceDataRequest(
    user_id='c36701',
    page_name='LOC'
)

result = get_master_reference_data_controller.mrd_get_master_reference_data(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Mrd Get Master Reference Data 1

```python
def mrd_get_master_reference_data_1(self,
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

result = get_master_reference_data_controller.mrd_get_master_reference_data_1(accept)
print(result)
```

## Example Response

```
{}
```

