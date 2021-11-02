"""
\                       new line показывает что следующая строка являяется
                        продолжением предшествующей. испоьзуется для огромных строк
                        не умещающихся на экране
\n                      переход на новую строку
\t                      tab
\b                      backspace
\'                      экранирование кавычек
\"                      экранирование кавычек
\\                      экранирование слэша


"""

s = 'dfdfdddejfnilejkfmwerkjnvoisrjtfgisnrtvoinstorivnsiutnrviusntvuinrstiunv' \ 
    'iusntrviusntiuvnsiuntviustntrituvnirtusntviunrtiuvirutnviurtn' \ 
    'viunrtviunriutnviuntiun'
print(len(s))

print('Hellow\nWorld')
print('Hellow\tWorld')
print('Helloo\bw World')