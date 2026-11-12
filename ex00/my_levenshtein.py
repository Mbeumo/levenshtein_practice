def my_levenshtein(word1:str,word2:str)->int:
    i=0
    sim=0
    #print(word1+" "+word2)
    if(len(word1)==len(word2)):
        while(i<len(word1)):
            if(word1[i]!=word2[i]):
                sim+=1
            
            i+=1
        return sim
    else:
        return -1  
#my_levenshtein("AAA","BBA")
#print(my_levenshtein("BAA","BBA"))   