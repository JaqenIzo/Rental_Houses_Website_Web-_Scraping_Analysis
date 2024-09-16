# import re

# cols = ['Furnished','Serviced','Bedrooms','Type','Ensuite','Location']
# data = []

# def checker(col,str):
#     match = re.search(f"{col}",str)
#     if match:
#         return True
#     else:
#        return  False

# def beds(str):
#     arr = str.split()
#     num=[]
#     for i in arr:
#         x = re.search(r"\d+",i)
#         if x:
#             num.append(x.group())
       
    
#     return num[0]
#--------------------------------------------------------------

# spans = soup.find_all('span', class_='relative top-[2px] hidden md:inline')
# spans
# text =[]
# for i in spans:
#     txt = i.string.strip()
#     text.append(txt)
    
# text
#-------------------------------------------------------------------

# cards = []
# for soup in main_soup :
#     card = soup.find_all("div", class_="listing-card mb-5 w-full md:mx-0 md:min-h-56")
#     cards.append(card)
    
    # for i in card:
    #    txt = i.string.strip()
    #    cards.append(txt)
# ----------------------------------------------------------------------------
# doc =requests.get('https://www.buyrentkenya.com/houses-for-rent?page=11')
# soup = bsoup(doc.content, 'html.parser')

# max_len= soup.find_all('div',class_='flex items-center justify-center text-xl font-bold leading-7 text-grey-900')
# for i in max_len:
#     print(i.text)
    
# max_len = np.int64(max_len[-1].string.strip())