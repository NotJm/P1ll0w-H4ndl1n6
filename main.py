from PIL import Image
from settings import *

def execute(path_filename: str, out_path_filename:str, format:str, extension:str) -> bool:
    try:
        image = Image.open(path_filename)
        image.save(f"{out_path_filename}{extension}", format=format)
    except Exception as e:
        return False
    
def main() -> None:
    print(LOGO)
    print("Github: n07jm")
    # Configure image 
    filename_configure_answer = inquirer.prompt(question_configure_filename)
    format_answer = inquirer.prompt(select_extension)
    # Get values from config
    path_filename = filename_configure_answer['path_filename']
    out_path_filename = filename_configure_answer['out_path_filename']
    format = format_answer['format'].upper()
    extension = extensions[format]
    # Execute convert
    if execute(path_filename, out_path_filename, format, extension):
        print("Converted successfully")
    else:
        print("Failed to convert")
    
if __name__ == "__main__":
    main()
