def leiaInt(inteiro):
    while True:
        try:
            inteiro = int(input(inteiro))
        except (ValueError, TypeError):
            print("\033[0;31mERRO! Digite apenas números inteiros!\033[m")
            continue
        else:
            return inteiro
            break