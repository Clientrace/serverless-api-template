# AWS Lambda File Upload for LINUX OS
# *Dependency: awscli

import sys
import os

if __name__ == '__main__':
    file_name = 'zf.zip'
    cli_zip_cmd = 'zip -r '+file_name+' * -x .git/ .vscode/ @'
    cli_aws_cmd = 'aws lambda update-function-code --function-name '+
    os.system(cli_cmd)
    os.system()









