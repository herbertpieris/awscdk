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

        lambda_datasetgroups_policy = iam.PolicyDocument(
            statements=[
                iam.PolicyStatement(
                    actions=["forecast:CreateDatasetGroup"],
                    resources=["*"],
                    effect=iam.Effect.ALLOW
                )
            ]
        )

        lambda_datasetgroups_role = iam.Role(self, "bi-lambda-datasetgroups-role",
                assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
                role_name="bi-lambda-datasetgroups-role",
                description="bi-lambda-datasetgroups-role",
                inline_policies={lambda_datasetgroups_policy}
            )    

        bi_lambda_datasetgroups_role_function = lambda_.Function(
            self,
            "bi-lambda-datasetgroups-role-function",
            runtime=lambda_.Runtime.PYTHON_3_9,
            function_name="bi-lambda-datasetgroups-function",
            description="bi-lambda-datasetgroups-function",
            code=lambda_.Code.from_asset('./lambda'),
            handler='forecastdatagroupset.lambda_handler',
            role=lambda_datasetgroups_role
        )
