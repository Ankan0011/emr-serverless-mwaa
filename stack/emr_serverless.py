from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_emrserverless as emr,
    aws_cloudwatch as cw,
    CfnOutput as CfnOutput,
)
import aws_cdk as cdk
from constructs import Construct

# This stack creates a EMR 6.6.0 Spark application with minimum initial hardware capacity
class EMRServerlessStack(Stack):
    serverless_app: emr.CfnApplication

    def __init__(self, scope: Construct, construct_id: str, vpc: ec2.IVpc, **kwargs) -> None:

        super().__init__(scope, construct_id, **kwargs)

        # Create a EMR 6.6.0 for Spark 3.2 version
        self.serverless_app = emr.CfnApplication(
            self,
            "spark-test-app",
            release_label="emr-6.6.0",
            type="SPARK",
            name="spark-3.2",
            network_configuration=emr.CfnApplication.NetworkConfigurationProperty(
                subnet_ids=vpc.select_subnets().subnet_ids,
                security_group_ids=[self.cre]
            ),
            initial_capacity=[
                emr.CfnApplication.InitialCapacityConfigKeyValuePairProperty(
                    key="Driver",
                    value=emr.CfnApplication.WorkerConfigurationProperty(
                        cpu="4vCPU", memory="16gb"
                    )
                )
            ],

            auto_stop_configuration=emr.CfnApplication.AutoStopConfigurationProperty(
                enabled=True, idle_timeout_minutes=60
            )
        )

    # Creating a seperate security group for the Application
    def create_security_group(self, vpc: ec2.IVpc) -> ec2.SecurityGroup:
        return ec2.SecurityGroup(self, "EMRServerlessSG", vpc=vpc) 
