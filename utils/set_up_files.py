import os
import shutil

ROOT_DIR = "/comp0010"
TEST_DIR = "test-dir"


def set_up_files():
    """
    Creates the following file structure:
    /comp0010/
        test-dir/
            file1.txt
            dir1/
                file2.txt
                file3.txt
            dir2/
                file4.txt
    """
    os.chdir(ROOT_DIR)
    if os.path.exists(TEST_DIR):
        shutil.rmtree(TEST_DIR, ignore_errors=True)
    os.mkdir(TEST_DIR)

    with open(f'{TEST_DIR}/file1.txt', 'w') as f:
        f.write("aabc\n")
        f.write("zzxy\n")

    os.mkdir(f"{TEST_DIR}/dir1")

    with open(f'{TEST_DIR}/dir1/file2.txt', 'w') as f:
        f.write("bbb\n")
        f.write("aa\n")
        f.write("aa\n")
        f.write("ddd\n")
        f.write("ddd\n")
        f.write("cc\n")

    with open(f'{TEST_DIR}/dir1/file3.txt', 'w') as f:
        pass

    os.mkdir(f"{TEST_DIR}/dir2")

    with open(f'{TEST_DIR}/dir2/file4.txt', 'w') as f:
        for i in range(100):
            f.write(f"{i}\n")

    os.chdir(TEST_DIR)
