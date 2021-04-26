from prettytable import PrettyTable
import datetime
def get_file_str(file_path:str=None)->str:
    if file_path is None or file_path == '':
        file_path='Project01_Gengwu_Zhao.ged'
        print("No input path, default test document will be used: Project01_Gengwu_Zhao.ged")        
    file_str=open(file_path,'r').read()
    #if the txt is empty, raise a valueError
    if len(file_str)==0:
        raise ValueError
    return file_str


