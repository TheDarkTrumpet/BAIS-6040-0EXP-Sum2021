def load_credentials(cFile):
    """This function loads credentials from a file."""
    with open(cFile, "r") as creds:
        connect_str = creds.readline()
    return connect_str