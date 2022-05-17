from unicodedata import name
from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_lambda as lambda_,
    aws_s3 as s3,
)


class SampleAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        fn_role = iam.Role(self, "bi-createdatasetgroups",
                assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
                role_name="bi-createdatasetgroups",
                description="bi-createdatasetgroups"
            )
        
        fn_function = lambda_.Function(
            self,
            "bi-createdatasetgroups",
            runtime=lambda_.Runtime.PYTHON_3_9,
            function_name="bi-createdatasetgroups",
            description="bi-createdatasetgroups",
            code=lambda_.Code.from_asset('./lambda'),
            handler='lambda_code.handler',
            role=fn_role,
            environment={
                'NAME':'bi-createdatasetgroups'
            }
        )
