# Del Template

```python
del_template_controller = client.del_template
```

## Class Name

`DelTemplateController`

## Methods

* [Template Filter Del Template](../../doc/controllers/del-template.md#template-filter-del-template)
* [Template Filter Del Template 1](../../doc/controllers/del-template.md#template-filter-del-template-1)


# Template Filter Del Template

```python
def template_filter_del_template(self,
                                accept,
                                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`TemplateFilterDelTemplateRequest`](../../doc/models/template-filter-del-template-request.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = TemplateFilterDelTemplateRequest(
    user_id='C36701',
    template_id='733'
)

result = del_template_controller.template_filter_del_template(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Template Filter Del Template 1

```python
def template_filter_del_template_1(self,
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

result = del_template_controller.template_filter_del_template_1(accept)
print(result)
```

## Example Response

```
{}
```

