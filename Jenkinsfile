pipeline {
    agent any
    environment {
        DOCKER_IMG_NAME = "aichatbot:$BUILD_ID"
        ECR_REPO_URL = "991486635617.dkr.ecr.us-east-1.amazonaws.com/chatobott-img:latest"
        KUBE_CONFIG = "/path/to/your/kubeconfig"
        CLUSTER_NAME = "cluster"
        PATH = "/dockerNode/workspace/helmPipeline/K8s"
    }
    stages {
        stage("Authenticate AWSCLI") {
            steps {
                withCredentials([[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: 'aws-poonam',
                    accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                    secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                ]]) {
                    sh "aws s3 ls"
                }
            }
        }
        stage("Clone Code") {
            steps {
                echo "Cloning the code"
                git url:'git@github.com:poonamd1234/workingpythonapp1.git', branch: 'master'
            }
        }
    }
}
