from myUtil.Config import Config
from myUtil.Post import get_contracts

if __name__ == '__main__':
    c = Config()
    print(get_contracts("https://12bccdb8-dcb3-46ff-8b17-51852b1e04f4.mock.pstmn.io/get_contacts"))
