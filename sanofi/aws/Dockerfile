# # FROM --platform=linux/amd64 python:3.10-slim
# FROM public.ecr.aws/amazonlinux/amazonlinux:latest

# RUN yum update -y 
# # && \
# #  yum install -y httpd 
# #  \
# #  yum install apt-get

# RUN yum install unzip
# RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
# RUN unzip awscliv2.zip
# RUN sudo ./aws/install
FROM --platform=linux/amd64 python:3.10-slim

# Install AWS CLI
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    awscli && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


WORKDIR /app
COPY . /app
# COPY requirements.txt ./
RUN pip install --upgrade pip

RUN pip install -r requirements.txt
# COPY Pipfile Pipfile.lock ./

# RUN aws s3 cp s3://airflow-s3-bucket-sigmoid/code ./ --recursive
# Copy your script or files needed for S3 operations
# COPY s3transfer.py /app
# COPY . /app

# Run your script
CMD ["python", "x_s3_transfer.py"]

# CMD ["python", "${filename}"]

# RUN pip install pipenv && \ 
#   apt-get update && \
#   apt-get install -y --no-install-recommends gcc python3-dev libssl-dev && \
#   pipenv install --deploy --system && \
#   python -m pip install -r requirements.txt 
#   apt-get remove -y gcc python3-dev libssl-dev && \
#   apt-get autoremove -y && \
#   pip uninstall pipenv -y 


# CMD ["python3","app.py"]