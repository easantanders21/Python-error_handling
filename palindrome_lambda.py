def run():

    def palindrome(string):
        return string == string[::-1]
    
    print(palindrome('ana'))
    
    palindrome_l = lambda string: string == string[::-1]
    
    print(palindrome_l('oto'))


if __name__ == '__main__':
    run()
