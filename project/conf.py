def get_project_key():
    file = open('./project/key', 'r')
    key = file.read()
    file.close()
    return key