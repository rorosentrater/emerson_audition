import os
import nose


if __name__ == "__main__":
    if not os.path.exists("test-reports"):
        os.makedirs("test-reports")
    else:
        nose.main()
