# Getgroups

```python
getgroups_controller = client.getgroups
```

## Class Name

`GetgroupsController`

## Methods

* [Group Getgroups](../../doc/controllers/getgroups.md#group-getgroups)
* [Group Getgroups 1](../../doc/controllers/getgroups.md#group-getgroups-1)


# Group Getgroups

```python
def group_getgroups(self,
                   accept,
                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`GroupGetgroupsrequest`](../../doc/models/group-getgroupsrequest.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = GroupGetgroupsrequest(
    user_id='c27116',
    request_name='Groupslist'
)

result = getgroups_controller.group_getgroups(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# Group Getgroups 1

```python
def group_getgroups_1(self,
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

result = getgroups_controller.group_getgroups_1(accept)
print(result)
```

## Example Response

```
{}
```

