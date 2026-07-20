def convert(message):
    message= message.replace(':)', '🙂')
    message= message.replace(':(', '🙁')
    return message
def main():
        message= input('Write a message: ')
        result= convert(message)
        print(result)
main()
