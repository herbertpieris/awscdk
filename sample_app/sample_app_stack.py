from unicodedata import name
from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_s3 as s3,
)


class SampleAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        role = iam.Role(self, "MyRole",
                assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
                name="abc",
                description="abc"
            )

#        bucket = s3.Bucket(self, "herbertpierishuhuhaha")
