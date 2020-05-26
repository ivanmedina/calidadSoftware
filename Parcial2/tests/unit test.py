import sys
sys.path.append('../')
import unittest
import grades
from random import randrange


class testGrades(unittest.TestCase):

    def test_readGrades(self):
        class mock_file:
            def __init__(self):
                pass

            def get_mockFile(studs,subs):
                sub_n=subs
                students_n=studs
                gs=students_n/sub_n
                file=""
                for x in range(1,students_n):
                    for y in range(1,sub_n):
                        file=file+ "student{} subject{} {}\n".format(x,y,randrange(100))
                return file

            #el archivo no existe, formato incorrexto, validar cada campo, alumnos bien acomodados
            #file=open("grades.txt","r")

#

    def test_getAverages(self):
        pass

if __name__ == '__main__':
    unittest.main()
