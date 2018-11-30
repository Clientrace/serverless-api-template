# AWS Lambda File Upload for LINUX OS

import sys
import os
from util import settings


if __name__ == '__main__':
    function_name = settings._value('function_name')
    file_name = 'zf.zip'
    cli_zip_cmd = 'zip -r '+file_name+' * -x .git/ .vscode/ @'
    cli_aws_cmd = 'aws lambda update-function-code --function-name '+function_name+' --zip-file fileb://zf.zip'
    os.system(cli_zip_cmd)
    os.system(cli_aws_cmd)





