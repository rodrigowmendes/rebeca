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
                    docker.withCredentials(registryCredential) {
                        def customImage = docker.build("rodrigowmendes/rebeca:${env.BUILD_ID}")
                        /* Push the container to the custom Registry */
                        customImage.push()
                    }
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
