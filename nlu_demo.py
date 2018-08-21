from rasa_nlu.model import Interpreter


if __name__ == '__main__':
    interpreter = Interpreter.load("./models/current/nlu")
    print("Your nlu service is ready ! Type your messages here or send 'stop'")
    while True:
        query = input()
        if query == 'stop':
            break
        result = interpreter.parse(query)
        print(result)
