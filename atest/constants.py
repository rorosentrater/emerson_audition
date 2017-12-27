import os


TEST_MODULE = os.environ.get('TEST_MODULE', '')
COMMAND_EXECUTOR = os.environ.get('COMMAND_EXECUTOR', '')

os.environ.setdefault('NOSE_PROCESSES', '10')
os.environ.setdefault('NOSE_PROCESS_TIMEOUT', '18000')
os.environ.setdefault('NOSE_WITH_XUNITMP', 'TRUE')
os.environ.setdefault('NOSE_XUNITMP_FILE', 'test-reports/xunit.xml')
