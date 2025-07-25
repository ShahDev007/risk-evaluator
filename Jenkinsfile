pipeline {
  agent any

  environment {
    DOCKER_BUILDKIT = 1
    COMPOSE_DOCKER_CLI_BUILD = 1
    WORKSPACE_DIR = "${env.WORKSPACE}" 
 }

  stages {
  
    stage('Clean Workspace') {
      steps {
        deleteDir()
      }
    }

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

    stage('Prepare Newman Reports Folder') {
      steps {
        sh 'mkdir -p reports'
      }
    }

    stage('Debug workspace') {
      steps {
        dir("${env.WORKSPACE}") {
         sh 'echo "[DEBUG] Listing workspace..."'
         sh 'ls -R'
         sh 'ls -R api_tests/collections || echo "[ERROR] Missing api_tests/collections directory"'
         sh 'ls -l api_tests/collections/score_api_tests.json || echo "[ERROR] File not found: score_api_tests.json"'
    }
  }
}


    stage('Run API Tests (Newman)') {
  steps {
    script {
      sh 'mkdir -p reports'
      def collectionPath = sh(script: "realpath api_tests/collections", returnStdout: true).trim()
      def reportPath = sh(script: "realpath reports", returnStdout: true).trim()

      sh """
        docker run --rm \
          -v ${collectionPath}:/etc/newman \
          -v ${reportPath}:/etc/newman/reports \
          postman/newman:alpine run /etc/newman/score_api_tests.json --reporters cli
      """
    }
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
