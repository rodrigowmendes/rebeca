pipeline {
    environment {
        registry = "rodrigowmendes/rebeca"
        registryCredential = "Dockerhub"
    }
    agent any

    stages {
        stage('Building image') {
            steps {
                echo 'Building..'
                sh 'python3 --version'
                script {
                    docker.build registry + ":$BUILD_NUMBER"
                    docker.push registry + ":$BUILD_NUMBER"
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'ls'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
