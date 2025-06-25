pipeline {
    agent any

    environment {
        PYTHONUNBUFFERED = '1'
    }

    stages {
        stage('Clone Repo') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh 'python -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running test suite...'
                sh 'pytest --html=reports/report.html --self-contained-html'
            }
        }

        stage('Archive Reports') {
            steps {
                echo 'Archiving HTML report...'
                archiveArtifacts artifacts: 'reports/*.html', fingerprint: true
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished. Cleaning up.'
        }
    }
}
