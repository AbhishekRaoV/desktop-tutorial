pipeline {
    agent {
        label 'master'
    }

    stages {
        stage('SCM Checkout') {
            steps {
                script {
                    git branch: 'main', url: 'https://github.com/AbhishekRaoV/Augmented_AI'
                }
            }
        }

        stage("Code Coverage") {
            steps {
                script {
                    dir('Augmented_AI') {
                        sh "cat binarytree.py | sgpt --code \"generate unit test cases\" --no-cache > CodeCoverage.txt  "
                    }
                }
            }
            post {
                success {
                    archiveArtifacts artifacts: 'Augmented_AI/CodeCoverage.txt'
                }
            }
        }
    }
}
