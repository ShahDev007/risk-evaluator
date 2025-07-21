pipeline {
  agent any

  environment {
    DOCKER_BUILDKIT = 1
    COMPOSE_DOCKER_CLI_BUILD = 1
  }

  stages {

    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build Containers') {
      steps {
        sh 'docker-compose build'
      }
    }

    stage('Start Backend & Frontend') {
      steps {
        sh 'docker-compose up -d backend frontend'
        sh 'sleep 5' // wait for services to be ready
      }
    }

    stage('Run API Tests (Newman)') {
      steps {
        sh 'docker-compose run --rm newman-runner'
      }
    }

    stage('Run UI Tests (Selenium)') {
      steps {
        sh 'docker-compose run --rm selenium-runner'
      }
    }

  }

  post {
    always {
      echo 'Cleaning up...'
      sh 'docker-compose down'
    }
  }
}
