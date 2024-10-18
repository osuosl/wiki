pipeline {
  agent { label 'web2' }
  environment {
    GITHUB_TOKEN = credentials('site_pr_builder')
  }
  stages {
    stage('Checkout') {
      steps {
        checkout scm
        script {
          if (env.CHANGE_ID) {
            withCredentials([usernamePassword(credentialsId: 'site_pr_builder', usernameVariable: 'GIT_USERNAME', passwordVariable: 'GIT_PASSWORD')]) {
              sh 'git fetch https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/osuosl/wiki.git master:refs/remotes/origin/master'
            }
          }
        }
      }
    }
    stage('Build & Deploy Site') {
      steps {
        script {
          if (env.BRANCH_NAME == 'master') {
            env.RSYNC_TARGET_DIR = "/var/www/osuosl.org/wiki.osuosl.org/htdocs"
            sh 'bash -ex scripts/jenkins.sh'
          } else if (env.CHANGE_ID) {
            env.RSYNC_TARGET_DIR = "/var/www/staging.osuosl.org/htdocs/wiki-${env.CHANGE_ID}"
            env.CHECK_LINT = "1"
            sh 'bash -ex scripts/build.sh'
          } else {
            echo "Not a PR or main branch, skipping deployment"
          }
        }
      }
    }
  }
  post {
    always {
      script {
        def siteUrl = ""
        if (env.BRANCH_NAME == 'master') {
          siteUrl = "https://wiki.osuosl.org/"

          slackSend channel: "#alerts",
                    color: currentBuild.result == 'SUCCESS' ? 'good' : 'danger',
                    message: "osuosl/wiki - #${env.BUILD_ID} finished with status ${currentBuild.result} (<${env.BUILD_URL}|Open>)"
        } else if (env.CHANGE_ID) {
          siteUrl = "https://wiki-${env.CHANGE_ID}.staging.osuosl.org"
        }

        // Post build status with a link to the site
        githubNotify context: 'Published site URL',
                     description: 'Build completed',
                     status: currentBuild.result,
                     targetUrl: "${siteUrl}",
                     message: "Site available: ${siteUrl}"
      }
    }
  }
}
