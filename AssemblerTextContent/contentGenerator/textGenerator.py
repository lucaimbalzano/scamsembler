

def GenerateTxtFile(input_string, file_name):
    try:
        with open(file_name, 'w') as file:
            file.write(input_string)
        print("Text file '{}' successfully created.".format(file_name))
    except Exception as e:
        print("Error:", e)
