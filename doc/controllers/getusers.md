# Getusers

```python
getusers_controller = client.getusers
```

## Class Name

`GetusersController`

## Methods

* [User Getusers](../../doc/controllers/getusers.md#user-getusers)
* [User Getusers 1](../../doc/controllers/getusers.md#user-getusers-1)


# User Getusers

```python
def user_getusers(self,
                 accept,
                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`UserGetusersrequest`](../../doc/models/user-getusersrequest.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = UserGetusersrequest(
    user_id='c27116',
    request_name='Groupslist'
)

result = getusers_controller.user_getusers(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# User Getusers 1

```python
def user_getusers_1(self,
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

result = getusers_controller.user_getusers_1(accept)
print(result)
```

## Example Response

```
{}
```

