import os
import nose

from constants import *

if __name__ == "__main__":
    if not os.path.exists("test-reports"):
        os.makedirs("test-reports")
    if TEST_MODULE:
        nose.runmodule(name=TEST_MODULE)
    else:
        nose.main()
