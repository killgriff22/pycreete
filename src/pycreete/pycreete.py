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
            tmp=[]
            key=[key[i:i+n] for i in range(0, len(key), n)]
            for code in key:
                n=4
                codend = [code[i:i+n] for i in range(0, len(code), n)][1]
                for char in expect:
                    if codend == char:
                        tmp.append(code)
            msg = [msg[i:i+5] for i in range(0, len(msg), 5)]
            decrypted=""
            for code in msg:
                decrypted += expect[tmp.index(code)]
            return decrypted