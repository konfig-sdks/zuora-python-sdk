from zuora_python_sdk.paths.v1_fulfillments_key.get import ApiForget
from zuora_python_sdk.paths.v1_fulfillments_key.put import ApiForput
from zuora_python_sdk.paths.v1_fulfillments_key.delete import ApiFordelete


class V1FulfillmentsKey(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
