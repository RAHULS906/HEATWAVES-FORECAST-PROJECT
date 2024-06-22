from setuptools import find_packages,setup # type: ignore
from typing import List

HPEN_E_DOT='-e .'

def get_requirements(file_name:str)-> List[str]:
    requirements=[]
    with open (file_name) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HPEN_E_DOT in requirements:
            requirements.remove(HPEN_E_DOT)
            
    return requirements

setup(
name='HEATWAVES FORECAST PROJECT',
version='0.0.1',
author='rah',
author_email='rahulsa960@gmail.com',
packages=find_packages(),
install_requirements=get_requirements('requirements.txt')

)
    
