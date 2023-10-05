# Get U Setting

```python
get_u_setting_controller = client.get_u_setting
```

## Class Name

`GetUSettingController`

## Methods

* [Usetting Get U Setting](../../doc/controllers/get-u-setting.md#usetting-get-u-setting)
* [Usetting Get U Setting 1](../../doc/controllers/get-u-setting.md#usetting-get-u-setting-1)


# Usetting Get U Setting

```python
def usetting_get_u_setting(self,
                          accept,
                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`UsettingGetUSettingRequest`](../../doc/models/usetting-get-u-setting-request.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = UsettingGetUSettingRequest(
    user_id='c27116',
    screen_name='appSettings'
)

result = get_u_setting_controller.usetting_get_u_setting(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Usetting Get U Setting 1

```python
def usetting_get_u_setting_1(self,
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

result = get_u_setting_controller.usetting_get_u_setting_1(accept)
print(result)
```

## Example Response

```
{}
```

