""" 
Пример работы с match case. 
"""
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case _:
            return "Something's wrong whit the internet"

if __name__ == '__main__':
    print(http_error(400))
    print(http_error(418))
    print(http_error(418))