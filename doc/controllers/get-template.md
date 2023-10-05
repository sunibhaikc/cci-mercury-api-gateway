# Get Template

```python
get_template_controller = client.get_template
```

## Class Name

`GetTemplateController`

## Methods

* [Template Filter Get Template](../../doc/controllers/get-template.md#template-filter-get-template)
* [Template Filter Get Template 1](../../doc/controllers/get-template.md#template-filter-get-template-1)


# Template Filter Get Template

```python
def template_filter_get_template(self,
                                accept,
                                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`TemplateFilterGetTemplateRequest`](../../doc/models/template-filter-get-template-request.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = TemplateFilterGetTemplateRequest(
    user_id='C36701',
    page_name='TEMPLATE'
)

result = get_template_controller.template_filter_get_template(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Template Filter Get Template 1

```python
def template_filter_get_template_1(self,
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

result = get_template_controller.template_filter_get_template_1(accept)
print(result)
```

## Example Response

```
{}
```

