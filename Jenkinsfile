pipeline {
    agent any
    triggers {
	pollSCM('* * * * *')
    }
    stages {
	stage("Check directory") {
	    steps {
		sh 'bash check_dir.sh'
	    }
	}
        stage("Unit test") {
            steps {
                sh "python -m unittest -v test_calc"
            }
        }
	stage("Run program ones") {
	    steps {
		sh "python calc.py 3 4"
	    }
	}
    }
}

