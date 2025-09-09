pipeline{
    agent any
    stages{
        stage("clean up"){
            steps{
                deleteDir()
            }
        }
        stage("clone repo"){
            steps{
                sh "git clone https://github.com/perisetlapujithalakshmi/git_learnings.git"
            }
        }
        stage("build"){
            steps{
                dir("my_second_repo"){
                    sh "echo 'Build stage executed successfully'"
                }
            }
        }
    }
}

