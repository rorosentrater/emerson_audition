PROJECT := qat

# Conditional variables for bamboo
NAME := $(or ${bamboo_repository_name}, template)
PROJECT_REPOSITORY := ${NAME}

TEST_CONTAINER := ${NAME}_test
DIR := $(shell pwd)

# Hack for string equality.  Needed to check against multiple strings using or.
eq = $(and $(findstring $(1),$(2)),$(findstring $(2),$(1)))

# Conditional variables for bamboo
BRANCH := $(or ${bamboo_planRepository_branch},vagrant)
VERSION := $(if ${bamboo_buildNumber},1.0.${bamboo_buildNumber},0.0.0)-${BRANCH}

CLIENT_NAMESPACE := transparent_${PROJECT}
CLIENT_ARTIFACT := ${CLIENT_NAMESPACE}-${NAME}-${VERSION}.tar.gz

IS_BAMBOO := $(if ${bamboo_DOCKER_REGISTRY},1,)

PUBLISHABLE := $(or $(call eq,${BRANCH},master),$(call eq,${BRANCH},development))

PUBLISHABLE_IMAGE_NAMESPACE := $(or ${bamboo_DOCKER_REGISTRY},vagrant)
CD_IMAGE_NAMESPACE := $(if ${bamboo_DOCKER_REGISTRY},cd-registry.transparent.com,vagrant)
IMAGE_NAMESPACE := $(if ${PUBLISHABLE},${PUBLISHABLE_IMAGE_NAMESPACE},${CD_IMAGE_NAMESPACE})

IMAGE_NAME := ${IMAGE_NAMESPACE}/${PROJECT}-${PROJECT_REPOSITORY}:${VERSION}
IMAGE_LATEST := ${IMAGE_NAMESPACE}/${PROJECT}-${PROJECT_REPOSITORY}:latest


ARTIFACTORY_CREDENTIALS := U1ZOQnVpbGQgU25vb3B5KjA5
ARTIFACTORY_URL := http://192.168.254.81:81/artifactory/libs-release-local/${PROJECT}/${PROJECT_REPOSITORY}/
CLIENT_ARTIFACTORY_URL := http://192.168.254.81:81/artifactory/libs-release-local/qat/${CLIENT_NAMESPACE}-${NAME}


DOCKER := sudo docker

# ######################################################### #
# Run tests
test: stage-build test-reports bamboo.py
	${DOCKER} run --rm\
	              -e TLO_TEST_COVERAGE=TRUE \
				  -e TLO_TEST=TRUE \
				  -e PYTHONPATH=/opt \
				  -v $$(pwd)/utest/:/opt/tests/ \
				  -v $$(pwd)/test-reports/:/opt/test-reports/ \
	              -v $$(pwd)/virtualenv-1.11.6/:/tmp/virtualenv/ \
	              -v $$(pwd)/bamboo.py:/opt/bamboo.py \
	              -v $$(pwd)/requirements-cpython.txt:/opt/requirements-cpython.txt \
	              -v $$(pwd)/test-requirements-cpython.txt:/opt/test-requirements-cpython.txt \
	              --name ${TEST_CONTAINER} \
	              ${IMAGE_NAME} \
	              /opt/v/bin/python /opt/bamboo.py -c /tmp/virtualenv/virtualenv.py -d /opt


stage-build: virtualenv-1.11.6

bamboo.py:
	wget -O bamboo.py http://192.168.254.81:81/artifactory/simple/libs-release-local/bamboo/bamboo-1.0.1.py


test-reports:
	mkdir -p test-reports

virtualenv-1.11.6: virtualenv-1.11.6.tar.gz
	tar -xzvpf virtualenv-1.11.6.tar.gz -C ${DIR}

virtualenv-1.11.6.tar.gz:
	wget -O ${DIR}/virtualenv-1.11.6.tar.gz http://192.168.254.81:81/artifactory/static/virtualenv/virtualenv-1.11.6.tar.gz

venv: virtualenv-1.11.6
	./virtualenv-1.11.6/virtualenv.py venv


# ######################################################### #
#  Build main image
image:
	${DOCKER} build --rm -t ${IMAGE_NAME} .

client: venv client/dist/${CLIENT_NAMESPACE}-${NAME}-${VERSION}.tar.gz

client/dist/${CLIENT_ARTIFACT}: venv
	sed s/0.0.1/${VERSION}/ library/setup.template.py > library/setup.py
	cd library && ../venv/bin/python setup.py sdist

clean-client:
	rm -rf library/test-reports
	rm -rf library/dist
	rm -rf library/*.egg-info
	rm -f library/setup.py
	-rm -f *.pyc
	-rm -f **/*.pyc

publish-client: client/dist/${CLIENT_ARTIFACT}
ifneq (${PUBLISHABLE},)
	@echo "Publishing client: ${CLIENT_ARTIFACT}"
	curl --user "$$(echo ${ARTIFACTORY_CREDENTIALS} | base64 --decode | awk '{ sub(/ /, ":"); print }')" \
		 --data-binary \
		 @client/dist/${CLIENT_ARTIFACT} \
		 -X PUT \
		 ${CLIENT_ARTIFACTORY_URL}/${CLIENT_ARTIFACT}
else
	@echo "Not publishing client."
endif



# ######################################################### #
#  Publish docker image
publish:
ifneq (${IS_BAMBOO},)
	@echo "Publishing image ${IMAGE_NAME} to registry."
	${DOCKER} tag ${IMAGE_NAME} ${IMAGE_LATEST}
	${DOCKER} push ${IMAGE_NAME}
	${DOCKER} push ${IMAGE_LATEST}
else
	@echo "Image will not be published."
endif

clean: clean-main-image clean-orphaned clean-dangling

clean-main-image:
	@echo Removing image $*
	-${DOCKER} rmi -f ${IMAGE_NAME}
	-${DOCKER} rmi -f ${IMAGE_LATEST}

clean-orphaned:
	@echo Removing orphaned images.
	-${DOCKER} rmi -f $(${DOCKER} images | awk '/^<none>/ { print $3 }')

clean-dangling:
	@echo Removing dangling images.
	-${DOCKER} rmi -f $(${DOCKER} images -q --filter "dangling=true")

# ######################################################### #
#  Print out variables.
vars:
	@echo PROJECT = ${PROJECT}
	@echo NAME = ${NAME}
	@echo VERSION = ${VERSION}
	@echo IMAGE_NAME = ${IMAGE_NAME}
	@echo IMAGE_LATEST = ${IMAGE_LATEST}
	@echo IMAGE_NAMESPACE = ${IMAGE_NAMESPACE}
	@echo BRANCH = ${BRANCH}

	@echo PUBLISHABLE = ${PUBLISHABLE}
	@echo DOCKER = ${DOCKER}
	@echo CLIENT_ARTIFACT = ${CLIENT_ARTIFACT}