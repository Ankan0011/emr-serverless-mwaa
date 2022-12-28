from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_mwaa as mwaa,
    aws_s3 as s3,
    aws_s3_deployment as s3d,
    aws_iam as iam
)
import aws_cdk as cdk
from constructs import Construct

class MwaaStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, vpc: ec2.IVpc, bucket: s3.Bucket, serverless_app_arn: str, serverless_job_arn: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Upload your spark codebase to s3
        files = s3d.BucketDeployment(
            self, "mwaa-assets", sources=[s3d.Source.asset("./assets/airflow")],
            destination_bucket=bucket,
        )

        # Define a name for the Airflow environment
        mwaa_name = "emr-serverless-airflow"

        mwaa_service_role = iam.Role(
            self,
            "mwaa-service-role",
            assumed_by=iam.CompositePrincipal(
                iam.ServicePrincipal("airflow.amazonaws.com"),
                iam.ServicePrincipal("airflow-env.amazonaws.com"),
            ),
            inline_policies={
                "CDKmwaaPolicyDocument": self.mwaa_policy_document(
                    mwaa_name, bucket.bucket_arn
                ),
                "AirflowEMRServerlessExecutionPolicy": self.emr_serverless_management_policy(serverless_app_arn, serverless_job_arn),
            },
            path="/service-role/",
        )

