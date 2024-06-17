from airflow import DAG
from airflow.providers.amazon.aws.operators.ecs import EcsRunTaskOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from airflow.models import Variable

# Define default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}
filename = Variable.get("filename", default_var=None)


# Define the DAG
dag = DAG(
    'ecs_task_operator_example',
    default_args=default_args,
    description='Run a task on AWS ECS using EcsTaskOperator',
    schedule_interval='@daily',
    start_date=datetime.today(),
    tags=['example'],
)

# Define the task
download_ecs_file = EcsRunTaskOperator(
    task_id='download_ecs_task',
    dag=dag,
    cluster='ECS-python-cluster',  # Replace with your ECS cluster name
    task_definition='s3operation',  # Replace with your task definition name
    launch_type='FARGATE',  # Or 'EC2' if using EC2 launch type
    overrides={
        'containerOverrides': [
            {
                'name':  's3operation',  #'s3trasfer',  # Replace with your container name
                'command': ['./execute_main.sh',filename],  # Command to run in the container
            }
        ],
    },
    network_configuration={
        'awsvpcConfiguration': {
            'subnets': ['subnet-07eccb9f704e34f41'],  # Replace with your subnet ID(s)
            'securityGroups': ['sg-02cb5968708f57e02'],  # Replace with your security group ID(s)
            'assignPublicIp': 'ENABLED',
        },
    },
    aws_conn_id='aws_default',  # AWS connection ID configured in Airflow
    region_name='us-east-1',  # Replace with your AWS region
)
# calling DAG
download_ecs_file 

