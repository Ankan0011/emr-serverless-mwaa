# EMR Serverless with Amazon Managed Workflows for Apache Airflow (MWAA) Stack

This is a CDK Python project that deploys an MWAA environment with the EMR Serverless Operator pre-installed with one sample Airflow DAG.

# Getting Started

- Install [CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)
- Activate the Python virtualenv and install dependencies, run the below code in cli.

```
source .venv/bin/activate
pip install -r requirements.txt
```

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

## Further Improvement
Few improvements can be made on this application. Please keep in mind that this setup is good for one time runs on EMR Serverless instead of cron jobs style applications.
- Please keep the spark jobs in s3 or in other repos and make sure that the files are move to the location before the Airflow dags are triggered.
- Use a configuration file to keep the spark python files path or other environment variables.
- [TODO] Need to implement logs to s3 bucket.
- [TODO] Need to add the test scripts for the application.