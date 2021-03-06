
# incredibles script taken from https://transcripts.fandom.com/wiki/The_Incredibles
# 
# Code was written according to the tutorial at https://towardsdatascience.com/creating-word-clouds-with-python-f2077c8de5cc
# 
# contractions.py was written by dipanjanS: https://github.com/dipanjanS/practical-machine-learning-with-python/

import nltk, re, unicodedata
from contractions import CONTRACTION_MAP
from nltk.corpus import stopwords
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator



nltk.download('stopwords')
nltk.download('punkt')

# Get data for the given character
# Tutorial code modified to accommodate characters with multiple names, eg. Elastigirl and Helen
def get_char_lines(charNames):
    output =  []
    print ('Getting lines for ', charNames[0])
    with open ('incredibles.txt', 'r') as f:
        for line in f:
            hasLine = False
            for char in charNames:
                if re.findall(r'(^' + char + r'.*:.*)',line,re.IGNORECASE):
                    hasLine = True
            if hasLine:
                output.append(line)
    f.close()
    print(charNames[0], 'has ', len(output), 'lines')
    return output



def expand_contractions(text, contraction_mapping=CONTRACTION_MAP):  
    contractions_pattern = re.compile('({})'.format('|'.join(contraction_mapping.keys())), 
                                      flags=re.IGNORECASE|re.DOTALL)
    def expand_match(contraction):
        match = contraction.group(0)
        first_char = match[0]
        expanded_contraction = contraction_mapping.get(match)\
                                if contraction_mapping.get(match)\
                                else contraction_mapping.get(match.lower())                       
        expanded_contraction = first_char+expanded_contraction[1:]
        return expanded_contraction
        
    expanded_text = contractions_pattern.sub(expand_match, text)
    expanded_text = re.sub("'", "", expanded_text)
    return expanded_text
        

def clean_lines(lines):
    text = ""
    for line in lines:
        cur_line = line.lower()
        cur_line = expand_contractions(cur_line)
        cur_line = re.sub(r'.*:','', cur_line)
        cur_line = re.sub('[\(\[].*?[\)\]]', ' ', cur_line)
        cur_line = unicodedata.normalize('NFKD', cur_line).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        pattern = r'[^a-zA-Z\'0-9\s]'
        cur_line = re.sub(pattern, '', cur_line)
        stopword_list = stopwords.words('english')
        tokens = nltk.word_tokenize(cur_line)
        tokens = [token.strip() for token in tokens]
        cur_line = ' '.join([token for token in tokens if token not in stopword_list])
        text = text + ' ' + cur_line
    return text
        
def generate_cloud(names, image):
    char_mask = np.array(Image.open(image))
    image_colors = ImageColorGenerator(char_mask)
    text = clean_lines(get_char_lines(names))
    wc = WordCloud(background_color="white", max_words = 220, width = 400, height = 400, mask=char_mask, random_state=1).generate(text)
    plt.imshow(wc.recolor(color_func=image_colors))
    return wc


