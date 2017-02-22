import nose
from constants import *

if __name__ == "__main__":
    if not os.path.exists("test-reports"):
        os.makedirs("test-reports")
    nose.main()