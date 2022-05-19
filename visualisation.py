import twint

from wordcloud import WordCloud
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np
from PIL import Image

import datetime

import publier_tweet

date_today = datetime.datetime.now().strftime("%Y-%m-%d")

recherches = [
    {
        "mot_rechercher": "python",
        "lieux_rechercher": "",
        "coordone_centre_position": "",
        "rayon_recherche": "",
        "date_debut": (datetime.datetime.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"),#yesterdays date
        "date_fin": date_today,#today's date
        "nom_fichier": "./csv/python_" + date_today + ".csv",
        "limite_recherche": 20000,
        "langue": "fr",
        "path_mask": "./img/mask/twiter_mask.png",
        "path_img_output": "./img/result/python_" + date_today +".png",
        "text_tweet": "les mots les plus utiliser en parlant de #python hier",
    },
    {
        "mot_rechercher": "JavaScript",
        "lieux_rechercher": "",
        "coordone_centre_position": "",
        "rayon_recherche": "",
        "date_debut": (datetime.datetime.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"),#yesterdays date
        "date_fin": date_today,#today's date
        "nom_fichier": "./csv/JavaScript" + date_today + ".csv",
        "limite_recherche": 20000,
        "langue": "fr",
        "path_mask": "./img/mask/twiter_mask.png",
        "path_img_output": "./img/result/JavaScript" + date_today +".png",
        "text_tweet": "les mots les plus utiliser en parlant de #JavaScript hier",
    },
    {
        "mot_rechercher": "Angular",
        "lieux_rechercher": "",
        "coordone_centre_position": "",
        "rayon_recherche": "",
        "date_debut": (datetime.datetime.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"),#yesterdays date
        "date_fin": date_today,#today's date
        "nom_fichier": "./csv/Angular" + date_today + ".csv",
        "limite_recherche": 20000,
        "langue": "fr",
        "path_mask": "./img/mask/twiter_mask.png",
        "path_img_output": "./img/result/Angular" + date_today +".png",
        "text_tweet": "les mots les plus utiliser en parlant de #Angular hier",
    },
    {
        "mot_rechercher": "PHP",
        "lieux_rechercher": "",
        "coordone_centre_position": "",
        "rayon_recherche": "",
        "date_debut": (datetime.datetime.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"),#yesterdays date
        "date_fin": date_today,#today's date
        "nom_fichier": "./csv/PHP" + date_today + ".csv",
        "limite_recherche": 20000,
        "langue": "fr",
        "path_mask": "./img/mask/twiter_mask.png",
        "path_img_output": "./img/result/PHP" + date_today +".png",
        "text_tweet": "les mots les plus utiliser en parlant de #PHP hier",
    }

]


#generation image------------------------

def generation_image(nom_fichier, path_mask, path_img_output, langue):
    #mots a ne pas conserver
    Stopwords = ['https',"ptdr","c'est","dâ","câ","dã","cã","trã","jâ","alors","mâ","mã","a",'personnes','dire','autres','lui','note','blog','monsieur','dai','via','seront','jour','car','instagr','suivez','veut','player','fortes','dire','mai','tour','cet','donner','dailymotion','actualites','grand','grande','encore','vive','video','bit','mettre','youtube','lui','cela','videos','frontnational','mlp','donnons','interview','toute','celui','retrouvez','parce','doivent','aura',"moments",'retrouvons','propose','souhaite','sarkozy','nicolas','pen','marine','html','revenu','generationsmvt','leurs','mois','leur','our','place','premier','ici','marche','construire','toujours','premier','facebook','chaque','vie','for''direct','macron','sera','pscp','and','live','devons','the','entre','toutes','plan','belle', 'lefigaro', 'accueil', 'deux', 'serai','temps','soit','bravo','rien','aussi','visite','ceux','depuis', 'sans','trop','non','partir','votre','bien','sommes','ils','hier','tinyurl','soutien','quand','status','grand','nouvelle','jamais','avoir','rendez','face','mes','suis','veux','comme','contre','bourdindirect','fait','https','pays','aujourd',"notre","de","en","alpes","ladroitederetour","politique","elle","politique","leur","tout","ont","de","la","à","le","les","et","pour","aux","pic","des","com","en","un","pas","une","je","ce","a","est","sur","twitter","cette","hui","être","sont","faut","faire","il","ne","avec","au","qui","que","du","dans","plus","on","http","se","y","nous","mais","fr","son","ai","avons","notre","vous","nos","par","www","tous","merci","ses","fait","doit","soir","demain","matin","soir","très","ces","ans","mon"]  
      

    df = pd.read_csv(nom_fichier, encoding ="latin-1") 

    #supression si la langue n'est pas français
    df_s1 = df

    if langue != "fr":  
        df = df_s1.drop(df_s1[(df_s1.language != langue)].index)

    comment_words = ''

    for val in df.tweet: 
      
        val = str(val) 
  
    
        tokens = val.split() 
      
    
        for i in range(len(tokens)): 
            tokens[i] = tokens[i].lower()   
            #netoie la liste
        
            if set('[ ¤¡´ìîë¥¦ª\\ø§ùðãâä,~!@#$%^&*()_+{}":;\']+$').intersection(tokens[i]):
                tokens[i] = ""
            if len(tokens[i]) > 4:
                #print(len(tokens[i]), tokens[i])
                comment_words = comment_words + " " + tokens[i]
         
        #comment_words += " ".join(tokens)+" "

    #mask
    mask = None
    if path_mask != "":
        mask = np.array(Image.open(path_mask))
        mask[mask == 1] = 255

    #couleur
    def couleur(*args, **kwargs):
        import random
        return "rgb({}, 100, 0)".format(random.randint(100, 255))
  
    wordcloud = WordCloud(width = 800, height = 800, 
                    background_color ='white', 
                    mask = mask,
                    stopwords = Stopwords,
                    collocations = False,
                    min_font_size = 10).generate(comment_words) 
  
    plt.figure(figsize = (8, 8), facecolor = None) 
    plt.imshow(wordcloud.recolor(color_func = couleur)) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 

    plt.savefig(path_img_output, format="png")

    #plt.show() 

#get data---------------------
def get_data_twiter(mot_rechercher, lieux_rechercher, coordone_centre_position, rayon_recherche, date_debut, date_fin, nom_fichier, limite_recherche, path_img_output, path_mask, langue):
    
    # Configure
    c = twint.Config()
    #mots rechercher
    if mot_rechercher != "":
        c.Search = mot_rechercher
    #recherche selement par ville
    if lieux_rechercher != "":
        c.Near = lieux_rechercher
    #limite geographique du tweet
    if rayon_recherche != "" and coordone_centre_position != "":
        c.Geo = coordone_centre_position + "," + rayon_recherche + "km"
    #nombre de tweet recuperer au max
    if limite_recherche != 0:
        c.Limit = limite_recherche
    #langue du tweet
    if langue != "":
        c.Lang = langue
    #nom du fichier crée
    c.Output = nom_fichier
    #crée un fichier csv
    c.Store_csv = True
    #date debut
    if date_debut != "":
        c.Since = date_debut
    #date fin
    if date_fin != "":
        c.Until = date_fin
    #ne pas voir les tweet dans la console
    c.Hide_output = True  

    # Run
    twint.run.Search(c)

    generation_image(nom_fichier, path_mask, path_img_output, langue)


for i in recherches:
    get_data_twiter(i["mot_rechercher"], i["lieux_rechercher"], i["coordone_centre_position"], i["rayon_recherche"], i["date_debut"], i["date_fin"], i["nom_fichier"], i["limite_recherche"], i["path_img_output"], i["path_mask"], i["langue"])
    publier_tweet.tweeter(i["text_tweet"], i["path_img_output"])