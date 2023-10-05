# Checkusergroup

```python
checkusergroup_controller = client.checkusergroup
```

## Class Name

`CheckusergroupController`

## Methods

* [User Checkusergroup](../../doc/controllers/checkusergroup.md#user-checkusergroup)
* [User Checkusergroup 1](../../doc/controllers/checkusergroup.md#user-checkusergroup-1)


# User Checkusergroup

```python
def user_checkusergroup(self,
                       accept,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`UserCheckusergrouprequest`](../../doc/models/user-checkusergrouprequest.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = UserCheckusergrouprequest(
    user_id='C27116'
)

result = checkusergroup_controller.user_checkusergroup(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# User Checkusergroup 1

```python
def user_checkusergroup_1(self,
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

result = checkusergroup_controller.user_checkusergroup_1(accept)
print(result)
```

## Example Response

```
{}
```

