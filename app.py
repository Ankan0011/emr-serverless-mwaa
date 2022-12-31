#!/usr/bin/env python3

import aws_cdk as cdk

from stack.vpc import VPCStack
from stack.common import CommonStack
from stack.mwaa import MwaaStack
from stack.emr_serverless import EMRServerlessStack

app = cdk.App()

vpc = VPCStack(app, "VPCStack")
common = CommonStack(app, "Dependencies")
emr_serverless = EMRServerlessStack(app, "EMRServerless", vpc.vpc)
mwaa = MwaaStack(app, "MWAAEMRServerless", vpc.vpc, common.bucket, emr_serverless.serverless_app.attr_arn, common.emr_serverless_job_role.role_arn)


app.synth()