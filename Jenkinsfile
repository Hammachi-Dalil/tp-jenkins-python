pipeline {
    agent any

    environment {
        DOCKER_USER = 'dalilhammachi'
    }

    stages {
        stage('Clone') {
            steps {
                checkout scm
            }
        }

        stage('Tests') {
            steps {
                sh '''
                    apt-get install -y python3 python3-pip -qq
                    python3 -m pip install pytest --quiet --break-system-packages
                    python3 -m pytest test_app.py -v
                '''
            }
        }

        stage('Build Docker') {
            steps {
                sh 'docker build -t mon-app:latest .'
            }
        }

        stage('Push Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh 'docker tag mon-app:latest $DOCKER_USER/mon-app:latest'
                    sh 'docker push $DOCKER_USER/mon-app:latest'
                }
            }
        }
    }

    post {
        success { echo 'Pipeline réussi !' }
        failure { echo 'Pipeline échoué !' }
    }
}
