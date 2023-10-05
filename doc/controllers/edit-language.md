# Edit Language

```python
edit_language_controller = client.edit_language
```

## Class Name

`EditLanguageController`

## Methods

* [Mrd Edit Language](../../doc/controllers/edit-language.md#mrd-edit-language)
* [Mrd Edit Language 1](../../doc/controllers/edit-language.md#mrd-edit-language-1)


# Mrd Edit Language

```python
def mrd_edit_language(self,
                     accept,
                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`MrdEditLanguageRequest`](../../doc/models/mrd-edit-language-request.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = MrdEditLanguageRequest(
    lang_id='1100065',
    lang_name='English11',
    last_modified_by='c36701'
)

result = edit_language_controller.mrd_edit_language(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Mrd Edit Language 1

```python
def mrd_edit_language_1(self,
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

result = edit_language_controller.mrd_edit_language_1(accept)
print(result)
```

## Example Response

```
{}
```

