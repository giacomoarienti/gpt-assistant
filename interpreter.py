import sys, io, pip

class Interpreter():
    @staticmethod
    def install_module(module: str):
        """
        Install the module using pip
        """
        result = pip.main(['install', module])
        if result != 0:
            raise
        globals()[module] = __import__(module)

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
                sys.stdout = old_stdout
                output.flush()

                # Install the module and retry
                Interpreter.install_module(e.msg.split("'")[1])
                # skip the first line of the code
                code = "\n".join(code.split("\n")[1:])
                return Interpreter.exec_code(code)

        sys.stdout = old_stdout
        output = output.getvalue()
        return output