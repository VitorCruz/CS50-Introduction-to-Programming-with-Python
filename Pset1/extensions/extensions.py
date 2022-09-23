
dict_extensions = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip",
}

def main():
    user_input = input("Input a file name: ")
    print(media_type(user_input))

def media_type(file):
    for extension in dict_extensions:
        if extension in file:
            return dict_extensions[extension]
    return 'application/octet-stream'

if __name__ == "__main__":
    main()



