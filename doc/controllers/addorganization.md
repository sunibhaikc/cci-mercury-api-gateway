# Addorganization

```python
addorganization_controller = client.addorganization
```

## Class Name

`AddorganizationController`

## Methods

* [Mrd Addorganization](../../doc/controllers/addorganization.md#mrd-addorganization)
* [Mrd Addorganization 1](../../doc/controllers/addorganization.md#mrd-addorganization-1)


# Mrd Addorganization

```python
def mrd_addorganization(self,
                       accept,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`MrdAddorganizationrequest`](../../doc/models/mrd-addorganizationrequest.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = MrdAddorganizationrequest(
    org_id='553',
    org_cd='33ff',
    org_name='test',
    curr_flag='Y',
    d_a_flag='Y',
    created_by='c09739'
)

result = addorganization_controller.mrd_addorganization(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Mrd Addorganization 1

```python
def mrd_addorganization_1(self,
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

result = addorganization_controller.mrd_addorganization_1(accept)
print(result)
```

## Example Response

```
{}
```

