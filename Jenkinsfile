pipeline {
    agent any
    triggers {
	pollSCM('* * * * *')
    }
    stages {
	stage("Check directory") {
	    steps {
		sh 'if [ -d /home/jenkins/workspace/calculator/ ]; then echo "Directory exists"; fi'
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

