from tkinter import messagebox
import shortuuid
from datetime import date, time, datetime

def generateID():
    return shortuuid.ShortUUID(alphabet="0123456789").random(length=5)

def addFood(name_text, price_text, type_text, esid_text, desc_text):
    foodid = generateID()
    foodname = name_text.get()
    foodprice = price_text.get()
    foodtype = [type_text.get()]
    estabid = esid_text.get()
    fooddesc = desc_text.get("1.0",'end-1c')
    foodtype_quarray = []
    if(',' in foodtype[0]):
        foodtypearray = foodtype[0].split(',')
        for i in foodtypearray:
            foodtype_quarray.append(f'''INSERT INTO FOOD_ITEM_FOOD_TYPE(food_id, food_type) VALUES ({foodid}, "{i}")''')
    else:
        foodtype_quarray.append(f'''INSERT INTO FOOD_ITEM_FOOD_TYPE(food_id, food_type) VALUES ({foodid},"{foodtype[0]}")''')

    foodInsert = f'''INSERT INTO FOOD_ITEM(food_id, food_name, food_desc, price, estab_id) VALUES ({foodid}, "{foodname}", "{fooddesc}", {foodprice}, {estabid})\n'''
    return foodInsert, foodtype_quarray


def addEstab(name_text, desc_text, loc_text, mos_text, cd_text):
    # print(f"Estab Name: {name_text.get()}\nEstab Desc: {desc_text.get()}\nLocation: {loc_text.get()}\nMode of Service: {mos_text.get()}\nContact Details: {cd_text.get()}")
    estabid = generateID()
    estabname = name_text.get()
    estabdesc = desc_text.get()
    establoc = loc_text.replace(" ", "").split(",")
    mos = mos_text.replace(" ", "").split(",")
    cd = cd_text.replace(" ", "").split(",")
    establoc_query = []
    estabmos_query = []
    estabcd_query = []

    for i in establoc: 
        establoc_query.append(f'''INSERT INTO FOOD_ESTABLISHMENT_LOCATION(estab_id, loc) VALUES ({estabid}, '{i}')''')

    for i in mos:
        estabmos_query.append(f'''INSERT INTO FOOD_ESTABLISHMENT_MODE_OF_SERVICE(estab_id, serv_mod) VALUES ({estabid}, '{i}')''')

    for i in cd:
        estabcd_query.append(f'''INSERT INTO FOOD_ESTABLISHMENT_CONTACT(estab_id, contact) VALUES ({estabid}, '{i}')''')

    estabInsert = f'''INSERT INTO FOOD_ESTABLISHMENT(estab_id, estab_desc, estab_name) VALUES  ({estabid}, '{estabdesc}', '{estabname}')'''

    return estabInsert, establoc_query, estabmos_query, estabcd_query
            
            
def addReview(rate_text, food_text, estab_text, review_text):
    #print(f"Rating: {rate_text.get()}\nFood ID: {food_text.get()}\nEstab ID: {estab_text.get()}\nReview: {review_text.get('1.0', 'end-1c')}")
    reviewid = generateID()
    rating = rate_text.get()
    foodid = food_text.get()
    estabid = estab_text.get()
    review = review_text.get('1.0', 'end-1c')
    datereviewed = datetime.now().strftime("%Y-%m-%d")
    email = "customer1@email.com"
    reviewInsert = f'''INSERT INTO REVIEW(review_id, rating, rev_date, rev_stat, email, estab_id, food_id) VALUES ({reviewid}, {rating}, '{datereviewed}', '{review}', '{email}', {estabid}, {foodid})'''
    print(reviewInsert)


