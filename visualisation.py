import twint
import csv

from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 
import re


#get data---------------------

nom_fichier = "paris.csv"
coordone_centre_position = "48.857173,2.341018"
rayon_recherche = "5"
limite_recherche = 200

# Configure
c = twint.Config()
#mots rechercher
#c.Search = "macron"
#recherche selement par ville
c.Near = "paris"
#limite geographique du tweet
#c.Geo = coordone_centre_position + "," + rayon_recherche + "km"
#nombre de tweet recuperer au max
c.Limit = limite_recherche
#nom du fichier crée
c.Output = nom_fichier
#crée un fichier csv
c.Store_csv = True
#date debut
c.Since = "2022-05-01"
#date fin
c.Until = "2022-05-17"
#ne pas voir les tweet dans la console
c.Hide_output = True  


# Run
twint.run.Search(c)


#mise en forme------------------------

#mots a ne pas conserver
Stopwords = ['https',"ptdr","c'est","dâ","câ","dã","cã","trã","jâ","alors","mâ","mã","a",'personnes','dire','autres','lui','note','blog','monsieur','dai','via','seront','jour','car','instagr','suivez','veut','player','fortes','dire','mai','tour','cet','donner','dailymotion','actualites','grand','grande','encore','vive','video','bit','mettre','youtube','lui','cela','videos','frontnational','mlp','donnons','interview','toute','celui','retrouvez','parce','doivent','aura',"moments",'retrouvons','propose','souhaite','sarkozy','nicolas','pen','marine','html','revenu','generationsmvt','leurs','mois','leur','our','place','premier','ici','marche','construire','toujours','premier','facebook','chaque','vie','for''direct','macron','sera','pscp','and','live','devons','the','entre','toutes','plan','belle', 'lefigaro', 'accueil', 'deux', 'serai','temps','soit','bravo','rien','aussi','visite','ceux','depuis', 'sans','trop','non','partir','votre','bien','sommes','ils','hier','tinyurl','soutien','quand','status','grand','nouvelle','jamais','avoir','rendez','face','mes','suis','veux','comme','contre','bourdindirect','fait','https','pays','aujourd',"notre","de","en","alpes","ladroitederetour","politique","elle","politique","leur","tout","ont","de","la","à","le","les","et","pour","aux","pic","des","com","en","un","pas","une","je","ce","a","est","sur","twitter","cette","hui","être","sont","faut","faire","il","ne","avec","au","qui","que","du","dans","plus","on","http","se","y","nous","mais","fr","son","ai","avons","notre","vous","nos","par","www","tous","merci","ses","fait","doit","soir","demain","matin","soir","très","ces","ans","mon"]  
regex = re.compile('|'.join(r'\b{}\b'.format(word) for word in Stopwords))   

df = pd.read_csv(nom_fichier, encoding ="latin-1") 

#supression si la langue n'est pas français
df_s1 = df[:limite_recherche] 
  
df = df_s1.drop(df_s1[(df_s1.language != "fr")].index)

comment_words = '' 
stopwords = set(STOPWORDS) 


for val in df.tweet: 
      
    val = str(val) 
  
    
    tokens = val.split() 
      
    
    for i in range(len(tokens)): 
        tokens[i] = tokens[i].lower()   
        #netoie la liste
        
        if set('[ ðãâ,~!@#$%^&*()_+{}":;\']+$').intersection(tokens[i]):
            tokens[i] = ""
        if len(tokens[i]) > 4:
            #print(len(tokens[i]), tokens[i])
            comment_words = comment_words + " " + tokens[i]
         
    #comment_words += " ".join(tokens)+" "
  
wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = Stopwords,
                collocations = False,
                min_font_size = 10).generate(comment_words) 
  
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show() 