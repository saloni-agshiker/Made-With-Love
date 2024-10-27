from ultralytics import YOLO
from PIL import Image
import os
import cv2
import matplotlib.pyplot as plt
import streamlit as st
import time
import random

######################################## CSS ##########################
st.set_page_config(page_title="Made with Love", layout="wide")
page_bg_color = """
<style>
    .stApp {
        background-color: #F0E1D2;
    }
</style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)
st.image("/Users/saloni.agshiker/Saloni/Georgia Tech/FIRST YEAR 24-25/AI ATL Hackathon/AI ATL Front End/Made with Love Logo.png", width=400)
st.markdown(
    """
    <style>
    .stImage {
        display: flex;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

######################################## END OF CSS ##########################

def create_recipe_card(recipe, recipe_info):
    return f"""
    <div class="recipe-card">
        <h3>{recipe}</h3>
        <p><strong>Prep Time:</strong> {recipe_info['prep_time']} min</p>
        <p><strong>Cook Time:</strong> {recipe_info['cook_time']} min</p>
        <p><strong>Flavor Profile:</strong> {recipe_info['flavor_profile']}</p>
        <p><strong>Ingredients:</strong> {', '.join(recipe_info['ingredients'][:5])}</p>
        <p><strong>State:</strong> {recipe_info['state']}</p>
        <p><strong>Region:</strong> {recipe_info['region']}</p>
    </div>
    """

infile = open('indian_food.csv', 'r')
def createDict():
    recipeDict = {}
    firstline = infile.readline().strip()
    name, diet_pref, meal_pref = 0, -7, -3
    lines = infile.readlines()
    count = 0
    for line in lines:
        recipeList = line.strip().split(',')
        recipe = recipeList[name]
        ingreds = [i.strip().lower().strip('"') for i in recipeList[1:-7]]
        recipeDict[count] = {
            'ingredients': ingreds,
        }
        recipeDict[count]['name'] = recipeList[0]
        if recipeList[-6] == "-1":
            recipeDict[count]['prep_time'] = 'N/A'
        else:
            recipeDict[count]['prep_time'] = recipeList[-6]
        if recipeList[-5] == "-1":
            recipeDict[count]['cook_time'] = 'N/A'
        else:
            recipeDict[count]['cook_time'] = recipeList[-5]
        if recipeList[-4] == "-1":
            recipeDict[count]['flavor_profile'] = 'N/A'
        else:
            recipeDict[count]['flavor_profile'] = recipeList[-4]
        if recipeList[-2] == "-1":
            recipeDict[count]['state'] = 'N/A'
        else:
            recipeDict[count]['state'] = recipeList[-2]
        if recipeList[-1] == "-1":
            recipeDict[count]['region'] = 'N/A'
        else:
            recipeDict[count]['region'] = recipeList[-1]
        count += 1
    return recipeDict
    

######################################## RANDOM RECIPE FUNCTIONALITY ##########################
st.markdown("""
<style>
    .recipe-card {
        background-color: #f8f8f8;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        padding: 20px;
        height: 300px;
        box-sizing: border-box;
        margin: 10px;
    }
    .recipe-card h3 {
        color: #2c3e50;
        font-size: 1.2em;
        margin-bottom: 10px;
        text-align: center;
    }
    .recipe-card p {
        color: #34495e;
        font-size: 0.9em;
        margin: 5px 0;
    }
    .recipe-card strong {
        color: #16a085;
    }
</style>
""", unsafe_allow_html=True)

def select_random_recipe(recDict):
    random_index = random.randint(0, len(recDict) - 1)
    #st.write(random_recipe)
    # ## ADD A LINE FOR SWEET/SAVORY AND TYPE OF MEAL
    # st.write("## " + random_recipe['name'])
    # if (random_recipe['cook_time'] == -1):
    #    st.write("### Cook Time: info to be found")
    # else:
    #    st.write("### Cook Time: " , random_recipe['cook_time'])
    # if (random_recipe['state'] == -1):
    #    st.write("### State: info to be found")
    # else:
    #    st.write("### State: " , random_recipe['state'])
    # if (random_recipe['region'] == -1):
    #    st.write("### Region: info to be found")
    # else:
    #    st.write("### Region: " , random_recipe['region'])
    recipe_info = recDict[random_index]
    words = f"""
    <div class="recipe-card">
    <h3>{recipe_info['name']}</h3>
    <p><strong>Prep Time:</strong> {recipe_info['prep_time']} min</p>
    <p><strong>Cook Time:</strong> {recipe_info['cook_time']} min</p>
    <p><strong>Flavor Profile:</strong> {recipe_info['flavor_profile']}</p>
    <p><strong>Ingredients:</strong> {', '.join(recipe_info['ingredients'][:5])}</p>
    <p><strong>State:</strong> {recipe_info['state']}</p>
    <p><strong>Region:</strong> {recipe_info['region']}</p>
    </div>
    """
    st.markdown(words, unsafe_allow_html=True)

# label=st.markdown("<p class='expander-label'>Try This!</p>"
with st.expander("Try This!", icon="😋", expanded=False): 
    rDict = createDict()
    select_random_recipe(rDict)


######################################## END OF RANDOM RECIPE FUNCTIONALITY ##########################


######################################## TAKING PICTURE & PROCESSING IT FUNCTIONALITY ##########################
uploaded_image = st.camera_input("## Add Your Picture")
while uploaded_image is None:
   time.sleep(20)

if uploaded_image is not None:
   image = Image.open(uploaded_image)
   filename = "captured_image.png"
   image.save(filename)
   current_directory = os.getcwd()
   image_path = os.path.join(current_directory, filename)
  
model = YOLO('/Users/saloni.agshiker/Saloni/Georgia Tech/FIRST YEAR 24-25/AI ATL Hackathon/AI ATL Front End/best.pt')

found_ingreds = []
results = model.predict(image_path, conf=0.2)

for result in results:
   boxes = result.boxes 
   img = result.orig_img
   for box in boxes:
       x1, y1, x2, y2 = box.xyxy[0] 
       class_id = int(box.cls[0]) 
       confidence = box.conf[0] 
       class_label = model.names[class_id] 
       found_ingreds.append(class_label)
       cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
       label = f'{class_label}: {confidence:.2f}'
       cv2.putText(img, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
astr = "Ingredients Found: "
for item in found_ingreds:
    astr += item + ", "
astr = astr[:-1]
st.write(astr)
######################################## END OF TAKING PICTURE & PROCESSING IT FUNCTIONALITY ##########################



######################################## RECOMMENDATION FUNCTIONALITY ##########################

infile = open('indian_food.csv', 'r')

def createList(diet, meal, ingredient):
    if 'final_list' not in st.session_state:
        adict = {}
        recipeDict = {}
        firstline = infile.readline().strip()
        alist = firstline.split(',')
        name, diet_pref, meal_pref = 0, -7, -3
        lines = infile.readlines()
        least_needed, most_needed = float('inf'), -float('inf')

        for line in lines:
            recipeList = line.strip().split(',')
            if recipeList[diet_pref] != diet or recipeList[meal_pref] != meal:
                continue
            recipe = recipeList[name]
            ingreds = [i.strip().lower().strip('"') for i in recipeList[1:-7]]
            recipeDict[recipe] = {
                'ingredients': ingreds,
            }
            if recipeList[-6] == "-1":
                recipeDict[recipe]['prep_time'] = 'N/A'
            else:
                recipeDict[recipe]['prep_time'] = recipeList[-6]
            if recipeList[-5] == "-1":
                recipeDict[recipe]['cook_time'] = 'N/A'
            else:
                recipeDict[recipe]['cook_time'] = recipeList[-5]
            if recipeList[-4] == "-1":
                recipeDict[recipe]['flavor_profile'] = 'N/A'
            else:
                recipeDict[recipe]['flavor_profile'] = recipeList[-4]
            if recipeList[-2] == "-1":
                recipeDict[recipe]['state'] = 'N/A'
            else:
                recipeDict[recipe]['state'] = recipeList[-2]
            if recipeList[-1] == "-1":
                recipeDict[recipe]['region'] = 'N/A'
            else:
                recipeDict[recipe]['region'] = recipeList[-1]
            count = sum(1 for item in ingredient if any(item.lower() in food_item for food_item in ingreds))
            remaining_num = len(ingreds) - count

            if count >= 1:
                least_needed = min(least_needed, remaining_num)
                most_needed = max(most_needed, remaining_num)
                adict.setdefault(remaining_num, []).append(recipe)

        if least_needed <= most_needed:
            st.session_state.final_list = [recipe for val in range(least_needed, most_needed + 1) for recipe in adict.get(val, [])]
        else:
            st.session_state.final_list = []
        st.session_state.recipeDict = recipeDict

def create_recipe_card(recipe, recipe_info):
    return f"""
    <div class="recipe-card">
        <h3>{recipe}</h3>
        <p><strong>Prep Time:</strong> {recipe_info['prep_time']} min</p>
        <p><strong>Cook Time:</strong> {recipe_info['cook_time']} min</p>
        <p><strong>Flavor Profile:</strong> {recipe_info['flavor_profile']}</p>
        <p><strong>Ingredients:</strong> {', '.join(recipe_info['ingredients'][:5])}</p>
        <p><strong>State:</strong> {recipe_info['state']}</p>
        <p><strong>Region:</strong> {recipe_info['region']}</p>
    </div>
    """

def generateThree():
    if len(st.session_state.final_list) == 0:
        st.write("No More Recipes!")
    else:
        recipes_to_display = st.session_state.final_list[:3]
        st.session_state.final_list = st.session_state.final_list[3:]

        cols = st.columns(3)
        for idx, recipe in enumerate(recipes_to_display):
            with cols[idx]:
                st.markdown(create_recipe_card(recipe, st.session_state.recipeDict[recipe]), unsafe_allow_html=True)

# st.markdown("""
# <style>
#     .recipe-card {
#         background-color: #f8f8f8;
#         border-radius: 10px;
#         box-shadow: 0 4px 8px rgba(0,0,0,0.1);
#         padding: 20px;
#         height: 300px;
#         box-sizing: border-box;
#         margin: 10px;
#     }
#     .recipe-card h3 {
#         color: #2c3e50;
#         font-size: 1.2em;
#         margin-bottom: 10px;
#         text-align: center;
#     }
#     .recipe-card p {
#         color: #34495e;
#         font-size: 0.9em;
#         margin: 5px 0;
#     }
#     .recipe-card strong {
#         color: #16a085;
#     }
# </style>
# """, unsafe_allow_html=True)

dietPref = st.selectbox("Diet Preference", ("Vegetarian", "Non Vegetarian"))
mealType = st.selectbox("Meal Type", ("Main course", "Snack", "Dessert", "Starter"))

if 'generate_clicked' not in st.session_state:
    st.session_state.generate_clicked = False

if st.button('Generate', key='generate_button'):
    if 'final_list' in st.session_state:
        del st.session_state.final_list
    final_ingreds = []
    for veg in found_ingreds:
        if veg == "Chili Pepper -Khursani-":
            final_ingreds.append("chillies")
        else:
            final_ingreds.append(veg)
        if veg == "Rice -Chamal-":
            final_ingreds.append("rice")
        else:
            final_ingreds.append(veg)
    createList(dietPref.lower(), mealType.lower(), set(final_ingreds))
    st.session_state.generate_clicked = True
    generateThree()

if st.session_state.generate_clicked:
    if st.button('Regenerate', key='regenerate_button', icon=":material/restart_alt:"):
        if 'final_list' in st.session_state:
            generateThree()

######################################## END OF RECOMMENDATION FUNCTIONALITY ##########################