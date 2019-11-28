try:
    n=int(input())

except ValueError:
    raise ValueError("Value Error Occured")
except EOFError:
    raise EOFError("End of File(EOF) occured")
except KeyboardInterrupt:
    raise KeyboardInterrupt("Keyboard Interrupt Error Occured")
