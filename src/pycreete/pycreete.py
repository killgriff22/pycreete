defualtexpect=" Ω≈ç√∫˜µ≤≥÷åß∂ƒ©˙∆˚¬…æœ∑´®†¥¨ˆø“‘«`¡™£¢∞§¶•ªº–≠¸˛Ç◊ı˜¯˘¿ÅÍÎÏ˝ÓÔÒÚÆŒ„´‰ˇÁ¨ˆØ∏”’»`⁄€‹›ﬁﬂ‡°·‚—±ZXCVBNM<>?ASDFGHJKL:QWERTYUIOP}[|~!@#$%^&*()_+zxcvbnm,./asdfghjkl;qwertyuiop[]"
class pystring:
    def purge(string,purger):
        purgestring=purger
        tmp=""
        for purger in purgestring:
            for char in string:
                if char == purger:
                    tmp=string
                    string=""
                    for part in tmp.split(char):
                        string = string+part
        return string
class pycrypter:
    class x4x5:
        def generatekey(expect=defualtexpect):
            import random
            codes=[]
            random.seed(expect)
            for char in expect:
                code=""
                for i in range(4):
                    code+=random.choice(expect)
                code += char
                codes.append(code)
            key=""
            random.shuffle(codes)
            for code in codes:
                key+=code
            return key
        def decrypt(key,msg,expect=defualtexpect):
            n=5
            keys=[key[i:i+n] for i in range(0, len(key), n)]
            msg = [msg[i:i+n] for i in range(0, len(msg), n)]
            decrypted=""
            tmp=[]
            for char in expect:
                for keyx in keys:
                    if keyx[4] == char:  tmp.append(keyx)
                    else:  pass
            keys = tmp
            for code in msg:
                try:
                    decrypted += expect[keys.index(code)]
                except IndexError:
                    try:
                        print(keys.index(code),",",len(expect))
                        print(keys)
                    except:
                        print("code is not found in keys,dumping key\n",key)
            return decrypted
        def encrypt(key,msg,expect=defualtexpect):
            n=5
            encoded=""
            keys= [key[i:i+n] for i in range(0, len(key), n)]
            for char in msg:
                for key in keys:
                    if key[4] == char:  encoded+=key
            return encoded
