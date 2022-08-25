import os
import shutil
import hashlib


BLOCKSIZE = 65536  # lets read stuff in 64kb chunks!

# src_path = "C:\\Users\\Desktop\\R\\Test\\IOS_v53.accdb"
# dst_path = "C:\\Users\\\Desktop\\R\\Test\\IOS3.accdb"
# shutil.copy(src_path, dst_path)
# print('Copied')

def hash_it(fileToOpen):
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    with open(fileToOpen, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)

        while len(buf) > 0:
            md5.update(buf)
            sha1.update(buf)

            buf = afile.read(BLOCKSIZE)

    return (format(sha1.hexdigest()))


def get_extension(fname):
    split_tup = os.path.splitext(fname)
    return (split_tup)


def main():
    source_folder = "C:\\Users\\Desktop\\R\\Test\\A\\"
    destination_folder = "C:\\Users\\Desktop\\R\\Test\\B\\"
    print("Start Copying..")

    i = 1000
    # fetch all files
    for file_name in os.listdir(source_folder):
        # construct full file path
        # print(file_name)

        split_tup = get_extension(file_name)
        # print(split_tup[0])
        # print(split_tup[1])
        file_ext_name = split_tup[1]

        source = source_folder + file_name
        dest_file_name = hash_it(source)
        # print(dest_file_name)
        # destination_folder + dest_file_name + file_ext_name
        destination = destination_folder + dest_file_name + file_ext_name
        shutil.copy(source, destination)


main()

# print("MD5: {0}\n".format(md5.hexdigest()))

# print("SHA1: {0}".format(sha1.hexdigest()))
