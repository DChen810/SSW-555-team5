from datetime import datetime, timedelta
from typing import Tuple, List, Iterator,Dict
import prettytable,sys,os
from prettytable import PrettyTable
#part 1
def date_arithmetic() -> Tuple[datetime, datetime, int]:
    three_days_after_02272020: datetime = datetime.strptime('02 27 2020',"%m %d %Y")+timedelta(days=3)
    three_days_after_02272019: datetime = datetime.strptime('02 27 2019',"%m %d %Y")+timedelta(days=3)
    days_passed_02012019_09302019: int =abs((datetime.strptime('09 30 2019',"%m %d %Y")-datetime.strptime('02 01 2019',"%m %d %Y")).days)
    return three_days_after_02272020, three_days_after_02272019, days_passed_02012019_09302019
#part 2
def file_reader(path:str, fields: int, sep: str =',', header: bool=False) -> Iterator[List[str]]:
    try:
        a=open(path)
    except FileNotFoundError as e:
        print(e)
        sys.exit()
    lines=1
    while True:
        f=a.readline()
        if f != '':
            #Delete the last line break
            if f[-1]=='\n':
                f=f[:-1]
            result=f.split(sep)
            #if the length is not same, raise a ValueError
            if len(result)!=fields:
                raise ValueError(f"'{path}'has {len(result)} fields on line {lines} but expected {fields}")
            lines+=1
            #if header is true, pass the first line and change the header to false.
            if header:
                header=False
                continue
            yield result
        else:
            break
#part 3
class FileAnalyzer:
    """ Your docstring should go here for the description of the class."""
    def __init__(self, directory: str) -> None:
        """ Your docstring should go here for the description of the method."""
        self.directory: str = directory 
        self.files_summary: Dict[str, Dict[str, int]] = dict() 

        self.analyze_files() # summerize the python files data

    def analyze_files(self) -> None:
        os.chdir(self.directory)
        mean=os.listdir(self.directory)
        if len(mean)==0:
            raise ValueError('There are no files available in the folder')
        for file_ in mean:
            if file_.endswith('.py'):
                self.files_summary[file_]=self.files_summary.setdefault(file_,dict())
                try:
                    txt=open(file_).read()
                except FileNotFoundError as e:
                        print(e)
                        sys.exit()
                lines=open(file_).readlines()
                self.files_summary[file_]['class']=0
                self.files_summary[file_]['function']=0
                self.files_summary[file_]['line']=len(lines)
                self.files_summary[file_]['char']=len(txt)
                for line in lines:
                    l=line.strip(' ')
                    if l.startswith('class '):
                        self.files_summary[file_]['class']+=1
                    if l.startswith('def '):
                        self.files_summary[file_]['function']+=1
    def pretty_print(self) -> None:
        row:PrettyTable=PrettyTable()
        row.field_names=['File Name','Classes','Functions','Lines','Characters']
        for i,l in self.files_summary.items():
            row.add_row([self.directory+'\\'+i,l['class'],l['function'],l['line'],l['char']])
        print(row)
if __name__=='__main__':
    pass
