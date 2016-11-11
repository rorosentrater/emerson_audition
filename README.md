**Structure** 

* /utest 

Unit tests will go here

If one of the Automated tests is flawed from QAT perspective,
we need to test that out here, and prove we are flawed

They can be run manually in your dev environment, and then each class should be added
to the utest/__main__.py to be turned on for the project

* /atest

Automated tests will go here
Test can be written from Feature files or Unit Tests, and these
will not be run on commit, but will be run when our QA uses the project

* /atest/constants.py

All global configuration variables will go here (ex: URL live vs. test)
Use for both Unit tests and Automatic tests

* /library/setup.template.py

Helps turn your project specific code into a library we can all use.  make sure 
to change "template" out with your project name, (ex: lesson-gin)

* /library/transparent_qat

Project specific library package, all prefixed with "qat"
Each distinguishable page should be a class
Each smallest function should be a def

* requirements-cpython.txt

Project specific python install packages go here

* test-requirements-cpython,txt

Unit Testing Specific Python install packages go here, so they don't mingle with the Project overall

* deploy-playbook.yml

Please change the project and container name to be unique to your project

* Makefile

Please change the name that contains "template" to the same as your project


