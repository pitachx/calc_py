pipeline {
    agent any
    triggers {
	pollSCM('* * * * *')
    }
    stages {
        stage("Unit test") {
            steps {
                sh "python -m unittest -v test_calc.py"
            }
        }
	stage("Run program ones") {
	    steps {
		sh "python calc.py 3 4"
	    }
	}
    }
}

