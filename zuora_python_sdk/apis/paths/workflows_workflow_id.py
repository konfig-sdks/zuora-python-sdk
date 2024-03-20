from zuora_python_sdk.paths.workflows_workflow_id.get import ApiForget
from zuora_python_sdk.paths.workflows_workflow_id.delete import ApiFordelete
from zuora_python_sdk.paths.workflows_workflow_id.patch import ApiForpatch


class WorkflowsWorkflowId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
