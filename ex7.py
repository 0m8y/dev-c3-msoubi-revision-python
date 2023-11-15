from datetime import datetime

def main():
    file_name = "textFile.txt"
    file_content = open(file_name, 'r', encoding='utf-8').read()
    open("len_" + file_name, 'w', encoding='utf-8').write(str(len(file_content)))

if __name__ == "__main__":
    main()