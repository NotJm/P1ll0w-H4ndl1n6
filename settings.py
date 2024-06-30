import inquirer

LOGO = """
 _____                       _____        ______
/  __ \                     |____ |      |___  /
| /  \/  ___   _ __  __   __    / / _ __    / / 
| |     / _ \ | '_ \ \ \ / /    \ \| '__|  / /  
| \__/\| (_) || | | | \ V / .___/ /| |   ./ /   
 \____/ \___/ |_| |_|  \_/  \____/ |_|   \_/    
                                                                                             
"""


extensions = {
    "ICO": ".ico",
    "PNG": ".png",
    "JPEG": ".jpeg",
    "JPG": ".jpg",
}



select_extension = [
    inquirer.List(
        'format',
        message="What format do you want to convert it to?",
        choices=['ico', 'png' , 'jpeg']
    ),
]

question_configure_filename = [
    inquirer.Text('path_filename', message='File path'),
    inquirer.Text('out_path_filename', message="Converted file name")
]



