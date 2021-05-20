test = """케로 케로 케로 케로 힘차게 케로 케로 케로 나가자 우리 앞에 있는 모든 시련들 겹 낼 필요 ㅇ벗다 케로로 소대 오늘도 출동을 하네 큰맘 먹고 세차하면 비 오고 소풍 가면 소나기 습하게 탄 버스 방향 틀리고 건널목에 가면 항상 내 앞에서 너무 길어"""

textList = test.split()

wordDict = {}

for word in textList:
    if word in wordDict:
        wordDict[word] += 1
    else:
        wordDict[word] = 1

print(wordDict)
