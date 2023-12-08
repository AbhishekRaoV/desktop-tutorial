
pipeline {
    agent {
        label 'master'
    }
    parameters {
        base64File description: 'Please upload a file to read', name: 'FilePath'
        choice choices: ['Technology-refreshment'], description: 'document generation and Technology refreshment', name: 'choice'
        choice choices: ['Python','Rust','Golang','java'], description: 'select the any one of the above Language', name: 'LanguageSection'
    }
    environment{
        LanguageSection = "Python,Rust,Golang,java"
    }

    stages {
        stage('Read File Contents') {
            steps {
                script {
                    withFileParameter('FilePath') {
                        sh "cat ${FilePath}"
                    }
                }
            }
        }
        stage('conversion of the File'){
            steps{
                script{
                    if (params.choice == "Technology-refreshment"){
                    withFileParameter('FilePath') {
                        LanguageSection.split(',').each { lang ->
                            echo "${lang}"
                            sh "cat ${FilePath} | sgpt --code \"convert to ${lang} code --no-cache\" >ConvertedFile.${lang}"
                            sh "cat ConvertedFile.${lang}"
                        }
                    }
                    }
                }
            }
            post {
                success {
                    script{
                    if("${params.LanguageSection}" == "Python"){
                        archiveArtifacts artifacts: 'ConvertedFile.py'
                    }
                    if("${params.LanguageSection}" == "Rust"){
                        archiveArtifacts artifacts: 'ConvertedFile.rs'
                    }
                    if("${params.LanguageSection}" == "Golang"){
                        archiveArtifacts artifacts: 'ConvertedFile.go'
                    }
                    if("${params.LanguageSection}" == "java"){
                        archiveArtifacts artifacts: 'ConvertedFile.java'
                    }
                    }
                }
            }
        }
        
        // stage('Execution') {
        //     steps {
        //         script {
        //             if (params.choice == "Technology-refreshment"){
        //                 if ("${LanguageSection}" == "Python") {
        //                     sh "mv ConvertedFile.Python ConvertedFile.py"
        //                     def a = sh(script: "python3 ConvertedFile.py | tail -1",returnStdout: true).trim()
        //                     def b = sh(script: "python3 ConvertedFile.py | tail -1",returnStdout: true).trim()
        //                     def c = sh(script: "python3 ConvertedFile.py | tail -1",returnStdout: true).trim()
        //                     ExecutionTime1 = sh(script:"echo ${a} ${b} ${c} | sgpt \"give only average --no-cache\" ",returnStdout: true).trim()
        //                 } else if ("${LanguageSection}" == "Rust") {
        //                     sh "mv ConvertedFile.Rust ConvertedFile.rs"
        //                     sh "/var/lib/jenkins/.cargo/bin/rustc ConvertedFile.rs"
        //                     def a = sh(script: "./ConvertedFile | tail -1",returnStdout: true).trim()
        //                     def b = sh(script: "./ConvertedFile | tail -1",returnStdout: true).trim()
        //                     def c = sh(script: "./ConvertedFile | tail -1",returnStdout: true).trim()
        //                     sh "rm -f ConvertedFile"
        //                     ExecutionTime2 = sh(script:"echo ${a} ${b} ${c} | sgpt \"give only average --no-cache\" ",returnStdout: true).trim()
        //                 } else if ("${LanguageSection}" == "Golang") {
        //                     sh "mv ConvertedFile.Golang ConvertedFile.go"
        //                     sh "go run ConvertedFile.go"
        //                     def a = sh(script: "go run ConvertedFile.go | tail -1",returnStdout: true).trim()
        //                     def b = sh(script: "go run ConvertedFile.go | tail -1",returnStdout: true).trim()
        //                     def c = sh(script: "go run ConvertedFile.go | tail -1",returnStdout: true).trim()
        //                     ExecutionTime3 = sh(script:"echo ${a} ${b} ${c} | sgpt \"give only average --no-cache\" ",returnStdout: true).trim()
                            
        //                 }
        //                 else if ("${LanguageSection}" == java) {
        //                     sh "mv ConvertedFile.java ConvertedFile.java"
        //                     // sh "go run ConvertedFile.go"
        //                     // def a = sh(script: "go run ConvertedFile.go | tail -1",returnStdout: true).trim()
        //                     // def b = sh(script: "go run ConvertedFile.go | tail -1",returnStdout: true).trim()
        //                     // def c = sh(script: "go run ConvertedFile.go | tail -1",returnStdout: true).trim()
        //                     // ExecutionTime3 = sh(script:"echo ${a} ${b} ${c} | sgpt \"give only average --no-cache\" ",returnStdout: true).trim()
                            
        //                 }
        //                 else {
        //                     error "Language not available"
        //                 }
        //             }
        //         }
        //     }
            
        // }


        // stage('Average') {
        //     steps {
        //         script {
        //             if (params.choice == "Technology-refreshment"){
        //                 echo "Python, average execution time = ${ExecutionTime1}"
        //                 echo "Rust, average execution time = ${ExecutionTime2}"
        //                 echo "Golang, average execution time = ${ExecutionTime3}"
        //             }
        //         }
        //     }
        // }
    }
}
