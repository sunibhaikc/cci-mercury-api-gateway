# Editfunction Code

```python
editfunction_code_controller = client.editfunction_code
```

## Class Name

`EditfunctionCodeController`

## Methods

* [Mrd Editfunction Code](../../doc/controllers/editfunction-code.md#mrd-editfunction-code)
* [Mrd Editfunction Code 1](../../doc/controllers/editfunction-code.md#mrd-editfunction-code-1)


# Mrd Editfunction Code

```python
def mrd_editfunction_code(self,
                         accept,
                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`MrdEditfunctionCodeRequest`](../../doc/models/mrd-editfunction-code-request.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = MrdEditfunctionCodeRequest(
    f_id='1633281',
    f_name='7',
    last_modified_by='C09739'
)

result = editfunction_code_controller.mrd_editfunction_code(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Mrd Editfunction Code 1

```python
def mrd_editfunction_code_1(self,
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

result = editfunction_code_controller.mrd_editfunction_code_1(accept)
print(result)
```

## Example Response

```
{}
```

