pipeline{
    agent any
    stages{
        stage('Test Cases')
        {
            steps{
                sh '''
                docker-compose -f docker-compose-test.yml run test
                '''
            }
        }
        stage('Build')
        {
            steps{
                sh '''
                docker-compose up --build -d
                '''
            }
        }
    }
}