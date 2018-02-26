"""
src: https://courses.edx.org/courses/course-v1:UBCx+SoftConst2x+3T2017/courseware/5cb69b73e20d461ab3144b84b5c1c624/c4a4eecbc0a140c38484e07068799311/?child=first
Purpose: Throwing exceptions
"""


class FilipExcept(Exception):

    def __str__(self):
        return "My new error"

    pass


def my_func():
    raise FilipExcept


try:
    my_func()
except FilipExcept as err:
    print(err)
    pass
