### Directory Structure

* **/utest**: Unit tests
    * Unit tests can be placed here to be automatically run prior to a build.
        * This can be especially useful for catching logical errors in our code prior to use in production.
    * Any code that's to be re-used that isn't exercised by our automated tests, should be tested here.
    * To ensure your tests are ran, be sure to include the test module in *utest/__main__.py*.

* **/atest**: Automated test
    * This directory will be where Concourse sniffs through to find test modules.
    * All of your selenium related automated tests should be placed in this directory.
        * You may additionally add subdirectories for organization as you see fit.

* **/library/qat/**: Client package
    * *set.template.py* will be run after a successful build to create a re-usable client package to be used by other projects.
    * Controllers and related components should be placed in this directory.
