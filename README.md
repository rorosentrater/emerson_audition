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

* /library/transparent

Project specific library package, all prefixed with "qat"
Each distinguishable page should be a class
Each smallest function should be a def

* deploy-playbook.yml

Please change the project and container name to be unique to your project

* Makefile

Please change the name that contains "template" to the same as your project


