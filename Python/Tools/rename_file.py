import os

FILE_DIR = "C:/Users/taikh/Documents/GitHub/Code/Python/Tools/file"

def main():
    os.chdir(FILE_DIR)
    for file in os.listdir("./"):
        if file.find("Screenshot") == 0:
            raw_name = file.split("_")
            file_name_desc = "Question_" + raw_name[1]
            os.rename(file, file_name_desc)
            print('{} -> {}  (OK)'.format(file, file_name_desc))
		
if __name__ == "__main__":
    main()