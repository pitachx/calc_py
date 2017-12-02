pipeline {
    agent any
    triggers {
	pollSCM('* * * * *')
    }
    stages {
        stage("Unit test") {
            steps {
                sh "python3 -m unittest -v test_calc.py"
            }
        }
	stage("Run program ones") {
	    steps {
		sh "python3 calc.py 3 4"
	    }
	}
    }
}

