import os


def open_file(filepath):

    """ If Exists """
    try:
        if os.path.exists(filepath):
            with open(filepath, "r") as file:
                file.seek(0)
                # Using Lists (we can expand, sort, insert, append, and delete dynamically)
                return [[line.strip()] for line in file.readlines()]
        elif not(os.path.exists(filepath)):
            return None
    # Any Exception Is An Error
    except Exception:
        return None


def write_userdb_file(filepath, buffer):

    """ Writing To Usage Database File """
    userdb_content = open_file(filepath)
    """ Splitting Buffer To Respective Values """
    buffer_name, buffer_password, buffer_firstname, buffer_lastname, buffer_othername = buffer.split(',')
    """ Database File Error """
    if userdb_content is None:
        return -2
    """ Plain Write If Empty File """
    try:
        if not userdb_content:
            with open(filepath, "a") as file:
                file.write(buffer)
            return 0
    # Any Exception Is An Error
    except Exception:
        return -2
    """ Check For Duplicates """
    for stuff in userdb_content:
        # Stuff Is A List (length is 1) But At Index 0, Is Our String ["content"]
        username, password, firstname, lastname, othername = stuff[0].split(',')
        if str(username) == str(buffer_name):
            return -1
    """ Write To The User File """
    try:
        with open(filepath, "a") as file:
            file.write('\n'+buffer)
            return 0
    # Any Exception Is An Error
    except Exception:
        return -2


def write_usagedb_file(filepath, buffer):

    """ Writing To Usage Database File """
    usagedb_content = open_file(filepath)
    """ Splitting Buffer To Respective Values """
    buffer_name, buffer_folder_path, buffer_last_session = buffer.split(',')
    """ Database File Error """
    if usagedb_content is None:
        return -2
    """ Plain Write If Empty File """
    try:
        if not usagedb_content:
            with open(filepath, "a") as file:
                file.write(buffer)
            return 0
    # Any Exception Is An Error
    except Exception:
        return -2
    """ Check For Duplicates """
    for stuff in usagedb_content:
        # Stuff Is A List (length is 1) But At Index 0, Is Our String ["content"]
        username, folder_path, last_session = stuff[0].split(',')
        if str(username) == str(buffer_name):
            return -1
    """ Write To The User File """
    try:
        with open(filepath, "a") as file:
            file.write("\n"+buffer)
            return 0
    # Any Exception Is An Error
    except Exception:
        return -2


def open_folder(folder_path):

    """ If Directory """
    try:
        if os.path.isdir(folder_path):
            return os.listdir(folder_path)
    # Any Exception Is An Error
    except Exception:
        return None


def insert_folder_path(filepath, username, data):

    """ Getting Target To Insert """
    file_contents = open_file(filepath)
    # Where We accumulate The Edited Version Of Database
    updated_file_contents = list()
    for line in file_contents:
        usagedb_username, usagedb_folder_path, usagedb_last_session = line[0].split(",")
        if usagedb_username == username:
            updated_file_contents.append(f"{line[0][:line[0].find(",")]},{data},{line[0][line[0].rfind(",")+1:]}\n")
        else:
            updated_file_contents.append(f"{usagedb_username},{usagedb_folder_path},{usagedb_last_session}\n")
    """ Setting The Last Newline To Nothing (removing it) """
    updated_file_contents[-1] = updated_file_contents[-1].strip("\n")
    """ Writing To That Target """
    try:
        with open(filepath, 'w') as file:
            for line in updated_file_contents:
                file.write(str(line))
    # Any Exception Is An Error
    except Exception:
        return


def insert_last_session(filepath, username, data):

    """ Getting Target To Insert """
    file_contents = open_file(filepath)
    # Where We Accumulate The Edited Version Of The Database
    updated_file_contents = list()
    for line in file_contents:
        usagedb_username, usagedb_folder_path, usagedb_last_session = line[0].split(",")
        if usagedb_username == username:
            updated_file_contents.append(f"{line[0][:line[0].find(",")]},{line[0][line[0].find(",")+1:line[0].rfind(",")]},{str(data)}\n")
        else:
            updated_file_contents.append(f"{usagedb_username},{usagedb_folder_path},{usagedb_last_session}\n")
    """ Setting The Last Newline To Nothing """
    updated_file_contents[-1] = updated_file_contents[-1].strip("\n")
    """ Writing To That Target """
    try:
        with open(filepath, 'w') as file:
            for line in updated_file_contents:
                file.write(str(line))
    # Any Exception Is An Error
    except Exception:
        return