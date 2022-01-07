import string

def open_file():
    '''None->file object
    See the assignment text for what this function should do'''
    file=None
    try:
        file=input('Enter the name of the file: ').strip()
        f=open(file)
        f.close()
    except FileNotFoundError:
        print('There is no file with that name. Try again.')
        file=None
    return file

def cleanline(fp):
    ''' (file object)-> list
    takes file and removes punctuation and all uppercase letters
    returns list of these clean words '''
    file=open(fp).read().lower().split()
    lst=[]
    p='''!()-[]{};:'" <>,./?@#$%^&*_~'''
    for i in file:
        word=i.strip(p)
        lst.append(word)
    return lst

def process_lines(ls):
    ''' (file object,str)-> int
    Takes file object and counts how many lines there are'''
    file=open(ls).readlines()
    count=1
    lines=[]
    counter={}
    for i in file:
        lines.append(i)
        if i=='\n':
            count=count+1
            counter+=count
    return lines
def make_dict(lsw):
    '''(file object)-> dictionary
    Takes file object and returns clean words in dictionary with empty subdictionaries '''
    words=cleanline(lsw)
    dic={}
    for i in words:
        dic[i]={}
    return dic
    
def is_word(file):
    words=cleanline(file)
    for i in words:
        if len(i)<2 or not i.isalpha():
            words.remove(i)
        else:
            pass

def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do'''
    wordslst=cleanline(fp)
    word_ver=is_word(fp)
    dici=make_dict(fp)
    lines=process_lines(fp)
    for i in dici.keys():
        for j in range(len(lines)):
            if i in lines[j]:
                linum=[]
                linum.append(j+1)
                for m in linum:
                    dici[i]={m}
    return dici
 
def find_coexistance(D, query):
    '''(dict,str)->list
    See the assignment text for what this function should do'''
    query=query.split()
    for i in query:
        for j in range(len(query)):
            if i in D:
                x=D.get(i)
                query[j]=x
            else:
                pass
        return query

##############################
# main
##############################
file=open_file()
d=read_file(file)
query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
if query=='q' or query=='Q':
    pass
elif find_coexistance(d,query)== []:
    print('The word '+str(query)+' is not in the file')
else:
    print('The one or more words you entered coexisted in the following lines of the file:\n'+str(find_coexistance(d,query)))
    
