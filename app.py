#!/usr/bin/env python3

import aws_cdk as cdk

from stack.vpc import VPCStack
from stack.common import CommonStack

app = cdk.App()

vpc = VPCStack(app, "VPCStack")
common = CommonStack(app, "Dependencies")

app.synth()