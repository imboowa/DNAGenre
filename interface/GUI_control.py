import os
import secrets


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
    """ Database File Error """
    if userdb_content is None:
        return -2
    """ Splitting Buffer To Respective Values """
    # In Case Of Database Errors
    try: buffer_name, buffer_password, buffer_firstname, buffer_lastname, buffer_othername = buffer.split(',')
    except ValueError: return -2
    except Exception: return -2
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
        # In Case Of Database Errors
        try: username, password, firstname, lastname, othername = stuff[0].strip().split(',')
        except ValueError: return -2
        except Exception: return -2
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
    """ Database File Error """
    if usagedb_content is None:
        return -2
    """ Splitting Buffer To Respective Values """
    # In Case Of Database Errors
    try: buffer_name, buffer_folder_path, buffer_last_session = buffer.split(',')
    except ValueError: return -2
    except Exception: return -2
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
        # In Case Of Database Errors
        try: username, folder_path, last_session = stuff[0].strip().split(',')
        except ValueError: return -2
        except Exception: return -2
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
        else:
            return None
    # Any Exception Is An Error
    except Exception:
        return None


def insert_folder_path(filepath, username, data):

    """ Getting Target To Insert """

    file_contents = open_file(filepath)
    if file_contents is None:
        return
    # Where We accumulate The Edited Version Of Database
    updated_file_contents = list()
    for line in file_contents:
        # In Case Of Database Errors
        try: usagedb_username, usagedb_folder_path, usagedb_last_session = line[0].strip().split(",")
        except ValueError: return
        except Exception: return
        if usagedb_username == username:
            updated_file_contents.append(f"{usagedb_username},{data},{usagedb_last_session}\n")
        else:
            updated_file_contents.append(f"{usagedb_username},{usagedb_folder_path},{usagedb_last_session}\n")
    """ Setting The Last Newline To Nothing (removing it) """
    # If The List updated_file_contents Is Empty Then IndexError
    try: updated_file_contents[-1] = updated_file_contents[-1].strip("\n")
    except IndexError: pass
    except Exception: pass
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
    if file_contents is None:
        return
    # Where We Accumulate The Edited Version Of The Database
    updated_file_contents = list()
    for line in file_contents:
        # In Case Of Database Errors
        try: usagedb_username, usagedb_folder_path, usagedb_last_session = line[0].strip().split(",")
        except ValueError: return
        except Exception: return
        if usagedb_username == username:
            updated_file_contents.append(f"{usagedb_username},{usagedb_folder_path},{str(data)}\n")
        else:
            updated_file_contents.append(f"{usagedb_username},{usagedb_folder_path},{usagedb_last_session}\n")
    """ Setting The Last Newline To Nothing """
    # If The List updated_file_contents Is Empty Then IndexError
    try: updated_file_contents[-1] = updated_file_contents[-1].strip("\n")
    except IndexError: pass
    except Exception: pass
    """ Writing To That Target """
    try:
        with open(filepath, 'w') as file:
            for line in updated_file_contents:
                file.write(str(line))
    # Any Exception Is An Error
    except Exception:
        return


def delete_user(filepath, username):

    """ Deletes Target Account """

    file_contents = open_file(filepath)
    if file_contents is None:
        return -1
    # We Will Accumulate The List In Memory
    updated_file_contents = list()
    for line in file_contents:
        # In Case Of Database Errors
        try: userdb_username, userdb_password, userdb_firstname, userdb_lastname, userdb_othername = line[0].strip().split(",")
        except ValueError: return -1
        except Exception: return -1
        if userdb_username != username:
            updated_file_contents.append(f"{userdb_username},{userdb_password},{userdb_firstname},{userdb_lastname},{userdb_othername}\n")
        # If The username Is Found, The Loop Skips Adding Them And Their Data Is Lost Hence Successful Removal
    """ Setting The Last Newline To Nothing """
    # If The List updated_file_contents Is Empty Then IndexError
    try: updated_file_contents[-1] = updated_file_contents[-1].strip("\n")
    except IndexError: pass
    except Exception: pass
    """ Writing To That Target """
    try:
        with open(filepath, 'w') as file:
            for line in updated_file_contents:
                file.write(str(line))
            return 0
    # Any Exception Is An Error
    except Exception:
        return -1


def delete_data(filepath, username):

    """ Deletes Target Account Data In usagedb_file """

    file_contents = open_file(filepath)
    if file_contents is None:
        return -1
    # We Will Accumulate The List In Memory
    updated_file_contents = list()
    for line in file_contents:
        # In Case Of Database Errors
        try: usagedb_username, usagedb_folder_path, usagedb_last_session = line[0].strip().split(",")
        except ValueError: return -1
        except Exception: return -1
        if usagedb_username != username:
            updated_file_contents.append(f"{usagedb_username},{usagedb_folder_path},{usagedb_last_session}\n")
        # When username Is Found, It Is Skipped
    """ Setting The Last Newline To Nothing """
    # If The List updated_file_contents Is Empty Then IndexError
    try: updated_file_contents[-1] = updated_file_contents[-1].strip("\n")
    except IndexError: pass
    except Exception: pass
    """ Writing To That Target """
    try:
        with open(filepath, 'w') as file:
            for line in updated_file_contents:
                file.write(str(line))
            return 0
    # Any Exception Is An Error
    except Exception:
        return -1


def encrypt(real_filepath, file_with_real_file_header):

    """ Encrypts A File Using XOR With "secrets" Module """

    # Open File
    try:
        with open(real_filepath, 'rb') as file:
            plain_text = file.read()
    except FileNotFoundError:
        return None
    except Exception:
        return None

    # Open File With File Header
    try:
        with open(file_with_real_file_header, 'rb') as file:
            file_data = file.read()
    except FileNotFoundError:
        # If File With File Header And Key Does Not Exist Then Create It
        with open(file_with_real_file_header, 'wb') as _file: pass
        with open(file_with_real_file_header, 'rb') as file:
            file_data = file.read()
    except Exception:
        return None

    # Is File Length Long Enough For 4 Bytes
    if len(file_data) < 4:
        return None
    magic_prefix, header_value = file_data[0:3], file_data[3:4]
    if magic_prefix != b"#H9" or header_value != b"\x00":
        return None

    # Generate Cryptographically Secure Random Key
    key = secrets.token_bytes(len(plain_text))

    # File Header For Encrypted File
    magic_prefix, header_value = b"#H9", b"\x01"
    header = bytearray(magic_prefix) + bytearray(header_value)
    encrypted_text = bytearray()
    for b1, b2 in zip(plain_text, key):
        encrypted_text.append(b1 ^ b2)

    # Write To Real File
    try:
        with open(real_filepath, 'wb') as file:
            file.write(encrypted_text)
    except Exception:
        return None

    # Write To File With Real File Header
    try:
        with open(file_with_real_file_header, 'wb') as file:
            file.write(header + key)
    except Exception:
        return None


def decrypt(real_filepath, file_with_real_file_header, key):

    """ Decrypts A File Using XOR With "secrets" Module """

    # Open File
    try:
        with open(real_filepath, 'rb') as file:
            encrypted_text = file.read()
    except FileNotFoundError:
        return None
    except Exception:
        return None

    # Open File With Real File Header
    try:
        with open(file_with_real_file_header, 'rb') as file:
            file_data = file.read()
    except FileNotFoundError:
        return None
    except Exception:
        return None

    # Is File Long Enough For 4 Byte Header
    if len(file_data) < 4:
        # Write To File If It Does Not Meet Required File Length
        try:
            with open(file_with_real_file_header, 'wb') as file:
                file.write(bytearray(b"#H9") + bytearray(b"\x00") + file_data[4:])
        except Exception:
            return None
        return 0

    magic_prefix, header_value = file_data[0:3], file_data[3:4]
    if magic_prefix != b"#H9" or header_value != b"\x01":
        # Write To File If I Does Not Have Required Header
        try:
            with open(file_with_real_file_header, 'wb') as file:
                file.write(bytearray(b"#H9") + bytearray(b"\x00") + file_data[4:])
        except Exception:
            return None
        return 0

    # Is Key Valid
    if len(encrypted_text) != len(key):
        return None

    plain_text = bytes(b1 ^ b2 for b1, b2 in zip(encrypted_text, key))

    # New Magic Prefix And File Header
    new_magic_prefix, new_header_value = b"#H9", b"\x00"
    new_header = bytearray(new_magic_prefix) + bytearray(new_header_value)

    # Write To File
    try:
        with open(real_filepath, 'wb') as file:
            file.write(plain_text)
    except Exception:
        return None

    # Write To File WIth Real File Header
    try:
        with open(file_with_real_file_header, 'wb') as file:
            file.write(new_header + file_data[4:])
    except Exception:
        return None

    return 0