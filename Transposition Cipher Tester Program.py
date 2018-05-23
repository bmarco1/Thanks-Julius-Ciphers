import random, sys, transpositionEncrypt, transcriptionDecrypt

def maiin():
    random.seed(42)

    for i in range (20):

        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)

        message = list(message)
        random.shuffle(message)
        message = ''.join(message)

        print('Test "#%s..."' % (i + 1, message[:50]))

        for key in range(1, len(message)):
            encrypted = transpositionEncrypt.encryptMessage(key, message)
            decrypted = transcriptionDecrypt.decryptMessage(key, message)


            if message != decrypted:
                print('Mismatch with key %s and message %s.' % (key, message))
                print(decrypted)
                sys.exit()

    print('Transpsition cipher test passed')

if __main__ == '__main__':
    main()
