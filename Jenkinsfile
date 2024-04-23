pipeline {
    agent any
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
                git url:'https://github.com/poonamd1234/workingpythonapp1.git', branch: 'master'
            }
        }
        stage("Build-img") {       
            steps {
                sh "whoami"
                echo "Building the image"
                sh "docker build -t 637423608548.dkr.ecr.us-east-1.amazonaws.com/my-ecs-repo:latest ."
            }
        }
        stage("Push into ECR") { 
            steps {
                withCredentials([[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: 'aws-poonam',
                    accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                    secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                ]]) {
                    sh "aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 637423608548.dkr.ecr.us-east-1.amazonaws.com"
                    
                    sh "docker push 637423608548.dkr.ecr.us-east-1.amazonaws.com/my-ecs-repo:latest"                 
                    sh "docker logout 637423608548.dkr.ecr.us-east-1.amazonaws.com"
                }
            }
        }
        stage("Deploy to Kubernetes") { 
            steps {
                withCredentials([[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: 'aws-poonam',
                    accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                    secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                ]]) {
                     sh "aws eks update-kubeconfig --region us-east-1 --name cluster"
                    sh "kubectl version"
                     sh "which kubectl"
                     sh "/root/bin/kubectl apply -f manifest.yaml"
                }
            }
        }
    }
}
