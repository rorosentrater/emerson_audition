import unittest
import os

if __name__ == "__main__":
    try:
        import xmlrunner
    except ImportError:
        unittest.main()
    else:
        if not os.path.exists("test-reports"):
            os.makedirs("test-reports")
        unittest.main(verbosity=2, testRunner=xmlrunner.XMLTestRunner(output='test-reports'))