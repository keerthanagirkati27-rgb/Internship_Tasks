def merge_the_tools(string, k):

    for i in range(0, len(string), k):
        s = string[i:i+k]
        result = ""

        for ch in s:
            if ch not in result:
                result += ch

        print(result)
