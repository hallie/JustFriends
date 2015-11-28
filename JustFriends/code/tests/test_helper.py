import sys, os

# Absolure path to the current test file.
TEST_FILE_PATH = os.path.abspath(__file__)
# The path to the test directory.
TEST_DIR = os.path.dirname(TEST_FILE_PATH)
# The path to the directory of the main code.
CODE_DIR = os.path.dirname(TEST_DIR)

# Appending the path to the main code to the sys path.
sys.path.append(CODE_DIR)