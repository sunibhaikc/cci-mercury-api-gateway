# Get Agent Details by COE

```python
get_agent_details_by_coe_controller = client.get_agent_details_by_coe
```

## Class Name

`GetAgentDetailsByCOEController`

## Methods

* [View Get Agent Details by COE](../../doc/controllers/get-agent-details-by-coe.md#view-get-agent-details-by-coe)
* [View Get Agent Details by COE1](../../doc/controllers/get-agent-details-by-coe.md#view-get-agent-details-by-coe1)


# View Get Agent Details by COE

```python
def view_get_agent_details_by_coe(self,
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

result = get_agent_details_by_coe_controller.view_get_agent_details_by_coe(accept)
print(result)
```

## Example Response

```
{}
```


# View Get Agent Details by COE1

```python
def view_get_agent_details_by_coe_1(self,
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

result = get_agent_details_by_coe_controller.view_get_agent_details_by_coe_1(accept)
print(result)
```

## Example Response

```
{}
```

