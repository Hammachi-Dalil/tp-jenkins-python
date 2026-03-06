pipeline {
    agent any

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
    }

    post {
        success { echo 'Pipeline réussi !' }
        failure { echo 'Pipeline échoué !' }
    }
}
