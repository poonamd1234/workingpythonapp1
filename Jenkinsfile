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
             steps{
                 sh "whoami"
                echo "Building the image"
                sh "docker build -t newimg ."
                
            }
        }



    }
}
