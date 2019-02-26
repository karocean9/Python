import re /*Package to Import regular expression*/
for i in range(int(input())) : 
    if re.match(r'[789]\d{9}$',input()): /*Regular expression checking using match */
        print('YES') 
    else: 
        print('NO')
