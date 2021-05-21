s = "leetcode"
wordDict = ["leet","code"]

# s = "applepenapple"
# wordDict = ["apple","pen"]

# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]


wordSize = len(wordDict)
removeCount = 0
condition = True
for word in wordDict:

    print("Word In List: ", word)
    if word in s:
        s = s.replace(word, "", 1)

        print("New String: ", s)
        removeCount += 1
    print("")

if removeCount == wordSize:
    condition = True
else:
    condition = False

if condition:
    print("Breakable")
else:
    print("Not Breakable")
