# Editorganization

```python
editorganization_controller = client.editorganization
```

## Class Name

`EditorganizationController`

## Methods

* [Mrd Editorganization](../../doc/controllers/editorganization.md#mrd-editorganization)
* [Mrd Editorganization 1](../../doc/controllers/editorganization.md#mrd-editorganization-1)


# Mrd Editorganization

```python
def mrd_editorganization(self,
                        accept,
                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`MrdEditorganizationrequest`](../../doc/models/mrd-editorganizationrequest.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = MrdEditorganizationrequest(
    org_id='2862',
    org_name='test333',
    curr_flag='Y',
    d_a_flag='Y',
    modified_by='c36701'
)

result = editorganization_controller.mrd_editorganization(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Mrd Editorganization 1

```python
def mrd_editorganization_1(self,
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

result = editorganization_controller.mrd_editorganization_1(accept)
print(result)
```

## Example Response

```
{}
```

