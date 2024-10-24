

def assignment(text):
    import nltk
    from textblob import TextBlob
    from nltk.corpus import stopwords, wordnet
    from autocorrect import Speller
    from nltk.stem import WordNetLemmatizer

    marks=10
    synonyms = []
    filtertext=[]
    filteranswer=[]
    filcheck=[]
    filanscheck=[]
    answer='it is the process by which plant use sunlight, water, and carbon dioxide to make their own food.'
    answerblob=TextBlob(answer)
    textblob=TextBlob(text)




    #tokenize
    textwordsplit=textblob.words
    answerwordsplit=answerblob.words




    #stopwards
    stopwords = set(stopwords.words('english'))
    for i in textwordsplit:
        if i in stopwords:
            pass
        else:
            filtertext.append(i)

    for i in answerwordsplit:
        if i in stopwords:
            pass
        else:
            filteranswer.append(i)


      




    #spellcheck
    spell = Speller(lang='en')
    spellmarks=0
    for i in filtertext:
        spellcheck=spell(i)
        i=spellcheck
        filcheck.append(spellcheck)
        if i in filtertext:
            pass
        else:
            spellmarks=spellmarks+0.25

    if spellmarks>=3:
        spellmarks=3
    else:
        pass
    marks = marks-spellmarks


    #baseword
    baseword=[]
    for i in filcheck:
        # Create a lemmatizer
        lemmatizer = WordNetLemmatizer()

        # Lemmatize a verb
        verb = i
        base_form = lemmatizer.lemmatize(verb, pos='v')
        baseword.append(base_form)

    filcheck=baseword
    baseword=[]
    for i in filteranswer:
        # Create a lemmatizer
        lemmatizer = WordNetLemmatizer()

        # Lemmatize a verb
        verb = i
        base_form = lemmatizer.lemmatize(verb, pos='v')
        baseword.append(base_form)
    filteranswer=baseword

    #wordcheck
    wordmarks=0
    for i in filcheck:
        if i in answerwordsplit:
            pass
        else:
            from nltk.corpus import wordnet
            def get_synonyms(word):
                synonyms = []
                for syn in wordnet.synsets(word):
                    for lemma in syn.lemmas():
                        synonyms.append(lemma.name())
                return set(synonyms)# Use set to remove duplicates
            word = i
            k=0
            syn=get_synonyms(word)
            for i in syn:
                if i in answerwordsplit:
                    pass
                else:
                    k=k+1
            m=len(syn)
            if m==k:
                wordmarks=wordmarks+0.5
    for i in filteranswer:
        if i in filcheck:
            pass
        else:
            from nltk.corpus import wordnet
            def get_synonyms(word):
                synonyms = []
                for syn in wordnet.synsets(word):
                    for lemma in syn.lemmas():
                        synonyms.append(lemma.name())
                return set(synonyms)# Use set to remove duplicates
            word = i
            k=0
            syn=get_synonyms(word)
            for i in syn:
                if i in filcheck:
                    wordmarks=wordmarks-0.5
                else:
                    k=k+1
            m=len(syn)
            
            wordmarks=wordmarks+0.5        

    marks=marks-wordmarks
    if marks<=0:
        print('you got 0 marks')




    #sentiments
    textsenti=textblob.polarity
    answersenti=answerblob.polarity
    neganswersenti = answersenti-0.25
    posanswersenti = answersenti+0.25
    if posanswersenti>textsenti and neganswersenti<textsenti:
        mm=1
        pass
    
    else:
        print('you got 0 marks')
        mm=0
    
    #subjectivity
    textsub=textblob.subjectivity
    answersub=answerblob.subjectivity
    neganswersub = answersub-0.25
    posanswersub = answersub+0.25
    if posanswersub>textsub and neganswersub<textsub:
        marks=marks/10
        print('you got',marks,'marks')
    else:
        if mm==1:
            print('you got 0 marks')

j=input('explain photosynthesis?')
assignment(j)
        
        
    
