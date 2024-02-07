import sys, io, pip

class Interpreter():
    @staticmethod
    def exec_code(code: str) -> str:
        """
        Execute the code and return the output
        """
        old_stdout = sys.stdout
        sys.stdout = output = io.StringIO()
        
        try:
            exec(code)
        except Exception as e:
            print("Error occured during execution: " + str(e))

            if isinstance(e, ImportError):
                # Install the module and retry
                module = e.msg.split("'")[1]
                pip.main(['install', module])

                Interpreter.exec_code(code)

        sys.stdout = old_stdout
        output = output.getvalue()
        return output