# import mypackage.utils
# from mypackage.utils import *  # не явный импорт, не рекомендуется!
from mypackage.utils import multiply

if __name__ == '__main__':
    print(multiply(2, 3))
    # print(mypackage.utils.multiply(2, 3))
