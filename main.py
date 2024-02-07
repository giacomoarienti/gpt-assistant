from llm import LLM
from interpreter import Interpreter
from tts import TTS

llm = LLM()
tts = TTS()

while True:
    message = input("> ")
    if message.lower() == "q":
        exit()

    code = llm.process(message)
    print("\nResponse:\n" + code)

    if input("Execute (y/N) > ").lower() == "y":
        print()
        output = Interpreter.exec_code(code)

        print("Output:\n" + output)
        tts.speak(output)

    print()
