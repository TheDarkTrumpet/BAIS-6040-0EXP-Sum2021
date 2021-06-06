def load_credentials(file):
    """
    Given a file (absolute path), read the contents and return the connection string from the file

    Parameters
    ----------
    file : str
       The file name (absolute path) for the credentials file

    Returns
    -------
    connect_str
        Connection string
    """
    with open(file, "r") as creds:
        connect_str = creds.readline()
    return connect_str