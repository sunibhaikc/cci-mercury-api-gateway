# Add Language

```python
add_language_controller = client.add_language
```

## Class Name

`AddLanguageController`

## Methods

* [Mrd Add Language](../../doc/controllers/add-language.md#mrd-add-language)
* [Mrd Add Language 1](../../doc/controllers/add-language.md#mrd-add-language-1)


# Mrd Add Language

```python
def mrd_add_language(self,
                    accept,
                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`MrdAddLanguageRequest`](../../doc/models/mrd-add-language-request.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = MrdAddLanguageRequest(
    lang_cd='MSS',
    lang_first_char_code='P',
    lang_name='English1',
    created_by='c36701'
)

result = add_language_controller.mrd_add_language(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Mrd Add Language 1

```python
def mrd_add_language_1(self,
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

result = add_language_controller.mrd_add_language_1(accept)
print(result)
```

## Example Response

```
{}
```

