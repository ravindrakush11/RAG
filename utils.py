import os

def save_uploaded_file(uploaded_file, upload_dir="uploads"):
    """
    Save the uploaded file to the specified directory.

    Parameters:
    uploaded_file: Uploaded file object
    upload_dir (str): Directory to save the uploaded file

    Returns:
    str: The file path of the saved file
    """
    os.makedirs(upload_dir, exist_ok=True)  # Ensure the upload directory exists
    file_path = os.path.join(upload_dir, uploaded_file.name)
    
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    return file_path
