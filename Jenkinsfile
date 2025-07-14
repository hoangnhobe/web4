pipeline {
    agent any
    stages {
        stage('Clone Source') {
            steps {
                git branch: 'main', url: 'https://github.com/hoangnhobe/web4.git'
            }
        }
        stage('Build Docker Images') {
            steps {
                sh 'docker-compose build'
            }
        }
        stage('Run Containers') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
}