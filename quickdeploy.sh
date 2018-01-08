#!/usr/bin/env bash
LOCAL_MACHINE=${1:-10.0.2.15}
LOCAL_USER=${2:-vagrant}
LOCAL_PW=${3:-vagrant}
CONNECTION='-c local'

buildAndDeploy() {
  LOCATION=$1
  TAG=${2:-0.0.0-vagrant}

  OLD_PWD=$(pwd)
  cd $LOCATION
  #change this depending on project
  docker build . -t vagrant/template:$TAG
  cd $OLD_PWD

  ansible-playbook ${LOCATION}/deploy-playbook.yml \
                   ${CONNECTION} \
                   -i '127.0.0.1,' \
                   --extra-vars "deploy_server=${LOCAL_MACHINE} deploy_user=${LOCAL_USER} deploy_password=${LOCAL_PW} registry=vagrant tag=${TAG}"  -vvvv
}

buildAndDeploy
