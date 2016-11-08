**Structure** 

* /utest 

Unit tests will go here
If one of the Automated tests is flawed from QAT perspective,
we need to test that out here, and prove we are flawed

* /atest

Automated tests will go here
Test can be written from Feature files or Unit Tests 

* /atest/constants.py

All global configuration variables will go here (ex: URL live vs. test)
Use for both Unit tests and Automatic tests

* /library/transparent

Project specific library package, all prefixed with "qat"
Each distinguishable page should be a class
Each smallest function should be a def



