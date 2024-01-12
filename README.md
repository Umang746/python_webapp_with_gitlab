# Python Web App with GitLab CI/CD and Docker

![GitLab](https://img.shields.io/badge/GitLab-Continuous%20Integration-orange?style=for-the-badge&logo=gitlab)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Latest-green?style=for-the-badge&logo=flask)
![Docker](https://img.shields.io/badge/Docker-Latest-blue?style=for-the-badge&logo=docker)

This repository demonstrates a Python web app deployment workflow using GitLab CI/CD, Docker, and Flask. The process involves pushing Python code to GitLab, creating a Docker image with a Dockerfile, pushing the image to the GitLab Container Registry, and finally deploying and running the latest image in a Docker container.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Usage](#usage)


## Overview

This project showcases a robust continuous integration and deployment (CI/CD) pipeline using GitLab, Docker, and Flask. The workflow automates the deployment process, ensuring that the latest Python web app is seamlessly updated and running in a Docker container. For both stages we are using diffrent runners of GitLab.First job will pull code from SCM and build Docker image for latest code and push that image to Gitlab container registry.Second job will get newly created docker image and launch docker container from that image.As soon as developer update code all steps will be executed and we will get our latest webapp. This project is the best example of end to end pipeline.

## Features

- **GitLab CI/CD Pipeline:** Automates the build, test, and deployment process using GitLab CI/CD.

- **Docker Containerization:** Utilizes Docker to package the Python web app and its dependencies into a container.

- **Flask Web App:** Demonstrates a simple web app built with Flask, a popular Python web framework.

## Getting Started

To get started with deploying your Python web app using GitLab CI/CD and Docker, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Umang746/python_webapp_with_gitlab.git
    cd python_webapp_with_gitlab
    ```

2. **Configuration:**

    Review and modify the GitLab CI configuration file (`.gitlab-ci.yml`) and the Dockerfile based on your project's requirements.

## Project Structure

```plaintext
python_webapp_with_gitlab/
│
├── app/
│   ├── templates/
│   │   └── index.html
│   └── app.py
│
├── .gitlab-ci.yml
├── Dockerfile
└── README.md
```

- `app/`: Contains the Flask web app code and templates.
- `.gitlab-ci.yml`: GitLab CI/CD configuration file.
- `Dockerfile`: Docker configuration for building the Docker image.

## Configuration

The primary configuration for this project is handled through the `.gitlab-ci.yml` file.

```yaml
stages:
    - build
    - deploy

my build job:
    stage: build
    script:
        - echo "i am from build.."
        - echo $CI_PIPELINE_ID
    #   - docker build -t mypyapp:$CI_PIPELINE_ID .
        - docker login $CI_REGISTRY -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD
        - docker build -t registry.gitlab.com/myprojects1092852/project4/mypyapp:$CI_PIPELINE_ID .
        - docker push registry.gitlab.com/myprojects1092852/project4/mypyapp:$CI_PIPELINE_ID
    tags:
        - mybuild

my test job:
    stage: deploy
    script:
        - echo "i am from test"
        - docker login $CI_REGISTRY -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD
        - docker rm -f app123 || true
        - docker run -dit -p 80:8080 --name app123 registry.gitlab.com/myprojects1092852/project4/mypyapp:$CI_PIPELINE_ID
    tags:
        - production

```

Dockerfile

```yaml
FROM python:latest

WORKDIR  /app

ADD . /app

RUN pip install Flask

CMD ["python" , "app.py"]

```

## Usage

To deploy your Python web app using GitLab CI/CD and Docker, follow these steps:

1. **Push Code Changes:**
   - Make your Python web app code changes.
   - Push the changes to the GitLab repository.

2. **Monitor CI/CD Pipelines:**
   - Visit the GitLab repository.
   - Navigate to the CI/CD pipelines page.

3. **Review Build and Deploy Status:**
   - Monitor the automated build and deployment process as GitLab runs the CI/CD pipeline.
   - Ensure that both the build and deploy stages complete successfully.

4. **Access Deployed Web App:**
   - Once the pipeline is complete, access your deployed web app at the specified endpoint.
   - Example: http://your-username.gitlab.io/your-webapp

5. **Iterate and Improve:**
   - Make necessary adjustments to your Python web app based on the deployment results.
   - Commit and push the changes to trigger subsequent CI/CD pipelines.

6. **Continuous Integration:**
   - Enjoy the benefits of continuous integration, where your Python web app is automatically built, tested, and deployed upon each push, ensuring a reliable and up-to-date web application.

By following this process, you can seamlessly update and deploy your Python web app using the automated GitLab CI/CD and Docker setup.
