class pycreete:
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