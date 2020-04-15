pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                git branch: 'master', url: 'https://github.com/borisgu/flask-simple-app.git'
            }
        }
        stage('Build the Backend SVC') {
            steps {
                sh '''
                    cd ${WORKSPACE}/app
                    docker build -t boris1580/flask-python:0.0.${BUILD_NUMBER} .
                    docker tag boris1580/flask-python:0.0.${BUILD_NUMBER} boris1580/flask-python:latest
                '''
            }
        }
        stage('Build the Frontend SVC') {
            steps {
                sh '''
                    cd ${WORKSPACE}/nginx
                    docker build -t boris1580/webserver:0.0.${BUILD_NUMBER} .
                    docker tag boris1580/webserver:0.0.${BUILD_NUMBER} boris1580/webserver:latest
                '''
            }
        }
        stage('Push the Images') {
            steps {
                sh '''
                    docker push boris1580/flask-python:0.0.${BUILD_NUMBER}
                    docker push boris1580/flask-python:latest
                    docker push boris1580/webserver:0.0.${BUILD_NUMBER}
                    docker push boris1580/webserver:latest
                '''
            }
        }
    }
}
