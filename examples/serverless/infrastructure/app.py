#!/usr/bin/env python3
from aws_cdk import core as cdk
from stacks.chaliceapp import ChaliceApp

app = cdk.App()
int_stack = ChaliceApp(app, 'int')
prod_stack = ChaliceApp(app, 'prod')
app.synth()
