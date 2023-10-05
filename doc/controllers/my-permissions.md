# My Permissions

```python
my_permissions_controller = client.my_permissions
```

## Class Name

`MyPermissionsController`

## Methods

* [User My Permissions](../../doc/controllers/my-permissions.md#user-my-permissions)
* [User My Permissions 1](../../doc/controllers/my-permissions.md#user-my-permissions-1)


# User My Permissions

```python
def user_my_permissions(self,
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

result = my_permissions_controller.user_my_permissions(accept)
print(result)
```

## Example Response

```
{}
```


# User My Permissions 1

```python
def user_my_permissions_1(self,
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

result = my_permissions_controller.user_my_permissions_1(accept)
print(result)
```

## Example Response

```
{}
```

