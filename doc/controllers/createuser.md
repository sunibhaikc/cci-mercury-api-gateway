# Createuser

```python
createuser_controller = client.createuser
```

## Class Name

`CreateuserController`

## Methods

* [User Createuser](../../doc/controllers/createuser.md#user-createuser)
* [User Createuser 1](../../doc/controllers/createuser.md#user-createuser-1)


# User Createuser

```python
def user_createuser(self,
                   accept,
                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`UserCreateuserrequest`](../../doc/models/user-createuserrequest.md) | Body, Required | - |

## Response Type

`object`

## Example Usage

```python
accept = 'application/json'

body = UserCreateuserrequest(
    user_id='C27116',
    user_samaccountname='C27116',
    user_upn='Deepak.Dash@cox.com',
    user_displayname='Dash, Deepak (CCI-Atlanta-CON)',
    user_name='Dash Deepak',
    user_jobtitle='Contractor',
    user_manager='',
    user_mail='Deepak.Dash@cox.com',
    user_location='',
    user_company='Genpact LLC',
    created_by='C27116',
    user_role=[
        'CCI_CLD_Mercury_Administrator'
    ]
)

result = createuser_controller.user_createuser(
    accept,
    body
)
print(result)
```

## Example Response

```
{}
```


# User Createuser 1

```python
def user_createuser_1(self,
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

result = createuser_controller.user_createuser_1(accept)
print(result)
```

## Example Response

```
{}
```

