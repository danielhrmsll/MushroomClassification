import streamlit as st
import prediction
import pandas as pd
from sklearn.preprocessing import StandardScaler
st.set_page_config(
    page_title= "Mushroom Classification",
    initial_sidebar_state="expanded",
)
st.title("Mushroom Classification")
st.sidebar.title("Models")
model = st.sidebar.selectbox(
    'Selecciona el modelo:',
    [
        'Support Vector Machine',
        'Random Forest Classifier',
        'Extra Trees Classifier'
    ]
)
st.image("images/hongo.png", width=200)

if model == 'Support Vector Machine':
    st.sidebar.info('Accuracy: 100%', icon='✅')
elif model == 'Random Forest Classifier':
    st.sidebar.info('Accuracy: 100%', icon='✅')
elif model == 'Extra Trees Classifier':
    st.sidebar.info('Accuracy: 100%', icon='✅')

cap_shape_x=0
cap_shape_f=0
cap_shape_k=0
cap_shape_s=0
cap_shape_c=0

cap_surface_y=0
cap_surface_s=0
cap_surface_g=0

cap_color_n=0
cap_color_g=0
cap_color_e=0
cap_color_y=0
cap_color_w=0
cap_color_p=0
cap_color_c=0
cap_color_u=0
cap_color_r=0
bruises_t = 0

odor_n=0
odor_f=0
odor_y=0
odor_s=0
odor_l=0
odor_p=0
odor_c=0
odor_m=0

gill_attachment_f=0
gill_spacing_w=0
gill_size_n=0
gill_color_p = 0
gill_color_w = 0
gill_color_n = 0
gill_color_g = 0
gill_color_h = 0
gill_color_u = 0
gill_color_k = 0
gill_color_e = 0
gill_color_y = 0
gill_color_o = 0
gill_color_r = 0

stalk_shape_t=0
stalk_root_b=0
stalk_root_e=0
stalk_root_c=0
stalk_root_r=0

stalk_surface_above_ring_s=0
stalk_surface_above_ring_k=0
stalk_surface_above_ring_y=0
stalk_surface_below_ring_s=0
stalk_surface_below_ring_k=0
stalk_surface_below_ring_y=0

stalk_color_above_ring_w=0
stalk_color_above_ring_p=0
stalk_color_above_ring_g=0
stalk_color_above_ring_n=0
stalk_color_above_ring_o=0
stalk_color_above_ring_e=0
stalk_color_above_ring_c=0
stalk_color_above_ring_y=0
stalk_color_below_ring_w=0
stalk_color_below_ring_p=0
stalk_color_below_ring_g=0
stalk_color_below_ring_n=0
stalk_color_below_ring_o=0
stalk_color_below_ring_e=0
stalk_color_below_ring_c=0
stalk_color_below_ring_y=0

veil_color_w=0
veil_color_o=0
veil_color_y=0

ring_number_o=0
ring_number_t=0

ring_type_p=0
ring_type_l=0
ring_type_f=0
ring_type_n=0

spore_print_color_w=0
spore_print_color_n=0
spore_print_color_k=0
spore_print_color_h=0
spore_print_color_r=0
spore_print_color_u=0
spore_print_color_o=0
spore_print_color_y=0
population_v=0
population_y=0
population_s=0
population_n=0
population_c=0

habitat_g=0
habitat_p=0
habitat_l=0
habitat_u=0
habitat_m=0
habitat_w=0    
def dataC():
    data = {
        'cap-shape_c': cap_shape_c,
        'cap-shape_f': cap_shape_f,
        'cap-shape_k': cap_shape_k,
        'cap-shape_s': cap_shape_s,
        'cap-shape_x': cap_shape_x,
        
        'cap-surface_g': cap_surface_g,
        'cap-surface_s': cap_surface_s,
        'cap-surface_y': cap_surface_y,
        'cap-color_c': cap_color_c,
        'cap-color_e': cap_color_e,
        'cap-color_g': cap_color_g,
        'cap-color_n': cap_color_n,
        'cap-color_p': cap_color_p,
        'cap-color_r': cap_color_r,
        'cap-color_u': cap_color_u,
        'cap-color_w': cap_color_w,
        'cap-color_y': cap_color_y,
        'bruises_t': bruises_t,
        
        'odor_c': odor_c,
        'odor_f': odor_f,
        'odor_l': odor_l,
        'odor_m': odor_m,
        'odor_n': odor_n,
        'odor_p': odor_p,
        'odor_s': odor_s,
        'odor_y': odor_y,
        
        'gill-attachment_f': gill_attachment_f,
        'gill-spacing_w': gill_spacing_w,
        'gill-size_n': gill_size_n,
        'gill-color_e': gill_color_e,
        'gill-color_g': gill_color_g,
        'gill-color_h': gill_color_h,
        'gill-color_k': gill_color_k,
        'gill-color_n': gill_color_n,
        'gill-color_o': gill_color_o,
        'gill-color_p': gill_color_p,
        'gill-color_r': gill_color_r,
        'gill-color_u': gill_color_u,
        'gill-color_w': gill_color_w,
        'gill-color_y': gill_color_y,
        
        'stalk-shape_t': stalk_shape_t,
        'stalk-root_b': stalk_root_b,
        'stalk-root_c': stalk_root_c,
        'stalk-root_e': stalk_root_e,
        'stalk-root_r': stalk_root_r,
        'stalk-surface-above-ring_k': stalk_surface_above_ring_k,
        'stalk-surface-above-ring_s': stalk_surface_above_ring_s,
        'stalk-surface-above-ring_y': stalk_surface_above_ring_y,
    
        'stalk-surface-below-ring_k': stalk_surface_below_ring_k,
        'stalk-surface-below-ring_s': stalk_surface_below_ring_s,
        'stalk-surface-below-ring_y': stalk_surface_below_ring_y,
        'stalk-color-above-ring_c': stalk_color_above_ring_c,
        'stalk-color-above-ring_e': stalk_color_above_ring_e,
        'stalk-color-above-ring_g': stalk_color_above_ring_g,
        'stalk-color-above-ring_n': stalk_color_above_ring_n,
        'stalk-color-above-ring_o': stalk_color_above_ring_o,
        'stalk-color-above-ring_p': stalk_color_above_ring_p,
        'stalk-color-above-ring_w': stalk_color_above_ring_w,
        'stalk-color-above-ring_y': stalk_color_above_ring_y,
        
        'stalk-color-below-ring_c': stalk_color_below_ring_c,
        'stalk-color-below-ring_e': stalk_color_below_ring_e,
        'stalk-color-below-ring_g': stalk_color_below_ring_g,
        'stalk-color-below-ring_n': stalk_color_below_ring_n,
        'stalk-color-below-ring_o': stalk_color_below_ring_o,
        'stalk-color-below-ring_p': stalk_color_below_ring_p,
        'stalk-color-below-ring_w': stalk_color_below_ring_w,
        'stalk-color-below-ring_y': stalk_color_below_ring_y,
    
        'veil-color_o': veil_color_o,
        'veil-color_w': veil_color_w,
        'veil-color_y': veil_color_y,
        'ring-number_o': ring_number_o,
        'ring-number_t': ring_number_t,
        'ring-type_f': ring_type_f,
        'ring-type_l': ring_type_l,
        'ring-type_n': ring_type_n,
        'ring-type_p': ring_type_p,
        'spore-print-color_h': spore_print_color_h,
        'spore-print-color_k': spore_print_color_k,
        'spore-print-color_n': spore_print_color_n,
        'spore-print-color_o': spore_print_color_o,
        'spore-print-color_r': spore_print_color_r,
        'spore-print-color_u': spore_print_color_u,
        'spore-print-color_w': spore_print_color_w,
        'spore-print-color_y': spore_print_color_y,
        'population_c': population_c,
        'population_n': population_n,
        'population_s': population_s,
        'population_v': population_v,
        'population_y': population_y,
        
        'habitat_g': habitat_g,
        'habitat_l': habitat_l,
        'habitat_m': habitat_m,
        'habitat_p': habitat_p,
        'habitat_u': habitat_u,
        'habitat_w': habitat_w
    }
    return data

cap_shape = st.selectbox('Selecciona la forma de la cabeza.',
    ['Convex','Flat','Knobbed','Sunken','Conical']
)
if cap_shape == 'Convex':
    cap_shape_x = 1
elif cap_shape == 'Flat':
    cap_shape_f =1
elif cap_shape == 'Knobbed':
    cap_shape_k =1
elif cap_shape == 'Sunken':
    cap_shape_s =1
elif cap_shape == 'Conical':
    cap_shape_c =1  
cap_surface = st.selectbox("Selecciona la textura de la cabeza.",
                        ['Scaly','Smooth','Grooves'])
if cap_surface == 'Grooves':
    cap_surface_g = 1
elif cap_surface == 'Smooth':
    cap_surface_s = 1
elif cap_surface == 'Scaly':
    cap_surface_y = 1
    
cap_color = st.selectbox("Selecciona el color de la cabeza del hongo.",
                        ['Brown','Gray','Red','Yellow','White','Pink','Cinnamon','Purple','Green'])
if cap_color == 'Cinnamon':
    cap_color_c = 1
elif cap_color == 'Red':
    cap_color_e = 1
elif cap_color == 'Gray':
    cap_color_g = 1
elif cap_color == 'Brown':
    cap_color_n = 1
elif cap_color == 'Pink':
    cap_color_p = 1
elif cap_color == 'Green':
    cap_color_r = 1
elif cap_color == 'Purple':
    cap_color_u = 1
elif cap_color == 'White':
    cap_color_w = 1
elif cap_color == 'Yellow':
    cap_color_y = 1
    
bruises = st.selectbox("¿El hongo tiene manchas?",
                        ['False','True'])
if bruises == 'True':
    bruises_t = 1
    
odor = st.selectbox("odor",
                        ['None','Foul','Fishy','Spicy','Anise','Pungent','Creosote','Musty'])

if odor == 'Creosote':
    odor_c = 1
elif odor == 'Foul':
    odor_f = 1
elif odor == 'Anise':
    odor_l = 1
elif odor == 'Musty':
    odor_m = 1
elif odor == 'None':
    odor_n = 1
elif odor == 'Pungent':
    odor_p = 1
elif odor == 'Spicy':
    odor_s = 1
elif odor == 'Fishy':
    odor_y = 1
gill_attachment = st.selectbox("Selecciona la forma de las branqueas.",
                        ['Free','Atacched'])

if gill_attachment == 'Free':
    gill_attachment_f = 1
    
gill_spacing = st.selectbox("Selecciona el espaciado entre las branquias.",
                        ['Close','Crowded'])

    
if gill_spacing == 'Crowded':
    gill_spacing_w = 1

gill_size = st.selectbox("Selecciona el tamaño de las branqueas.",
                        ['Broad','Narrow'])

if gill_size == 'Narrow':
    gill_size_n = 1

gill_color = st.selectbox("Selecciona el color de las branqueas.",
                        ['Pink','White','Brown','Gray','Chocolate','Purple','Black','Red','Yellow','Orange','Green'])
if gill_color == 'Red':
    gill_color_e = 1
elif gill_color == 'Gray':
    gill_color_g = 1
elif gill_color == 'Chocolate':
    gill_color_h = 1
elif gill_color == 'Black':
    gill_color_k = 1
elif gill_color == 'Brown':
    gill_color_n = 1
elif gill_color == 'Orange':
    gill_color_o = 1
elif gill_color == 'Pink':
    gill_color_p = 1
elif gill_color == 'Green':
    gill_color_r = 1
elif gill_color == 'Purple':
    gill_color_u = 1
elif gill_color == 'White':
    gill_color_w = 1
elif gill_color == 'Yellow':
    gill_color_y = 1

stalk_shape  = st.selectbox("Selecciona la forma del tallo.",
                        ['Tapering','Enlarging'])

if stalk_shape == 'Tapering':
    stalk_shape_t = 1

stalk_root = st.selectbox("Selecciona la raiz del tallo.",
                        ['Bulbous','Equal','Club','Rooted'])

if stalk_root == 'Bulbous':
    stalk_root_b = 1
elif stalk_root == 'Club':
    stalk_root_c = 1
elif stalk_root == 'Equal':
    stalk_root_e = 1
elif stalk_root == 'Rooted':
    stalk_root_r = 1
    
stalk_surface_above_ring  = st.selectbox("Ingresa la superficie del tallo arriba del anillo",
                        ['Smooth','Silky','Scaly'])
if stalk_surface_above_ring == 'Silky':
    stalk_surface_above_ring_k = 1
elif stalk_surface_above_ring == 'Smooth':
    stalk_surface_above_ring_s = 1
elif stalk_surface_above_ring == 'Scaly':
    stalk_surface_above_ring_y = 1
    
stalk_surface_below_ring   = st.selectbox("Ingresa la superficie del tallo debajo del anillo. ",
                        ['Smooth','Silky','Scaly'])

if stalk_surface_below_ring == 'Silky':
    stalk_surface_below_ring_k = 1
elif stalk_surface_below_ring == 'Smooth':
    stalk_surface_below_ring_s = 1
elif stalk_surface_below_ring == 'Scaly':
    stalk_surface_below_ring_y = 1

stalk_color_above_ring   = st.selectbox("Ingresa el color del tallo arriba del anillo.",
                        ['White','Pink','Gray','Brown','Orange','Red','Cinnamon','Yellow'])

if stalk_color_above_ring == 'Cinnamon':
    stalk_color_above_ring_c = 1
elif stalk_color_above_ring == 'Red':
    stalk_color_above_ring_e = 1
elif stalk_color_above_ring == 'Gray':
    stalk_color_above_ring_g = 1
elif stalk_color_above_ring == 'Brown':
    stalk_color_above_ring_n = 1
elif stalk_color_above_ring == 'Orange':
    stalk_color_above_ring_o = 1
elif stalk_color_above_ring == 'Pink':
    stalk_color_above_ring_p = 1
elif stalk_color_above_ring == 'White':
    stalk_color_above_ring_w = 1
elif stalk_color_above_ring == 'Yellow':
    stalk_color_above_ring_y = 1
    
stalk_color_below_ring   = st.selectbox("Ingresa el color del tallo debajo del anillo.",
                        ['White','Pink','Gray','Brown','Orange','Red','Cinnamon','Yellow'])

if stalk_color_below_ring == 'Cinnamon':
    stalk_color_below_ring_c = 1
elif stalk_color_below_ring == 'Red':
    stalk_color_below_ring_e = 1
elif stalk_color_below_ring == 'Gray':
    stalk_color_below_ring_g = 1
elif stalk_color_below_ring == 'Brown':
    stalk_color_below_ring_n = 1
elif stalk_color_below_ring == 'Orange':
    stalk_color_below_ring_o = 1
elif stalk_color_below_ring == 'Pink':
    stalk_color_below_ring_p = 1
elif stalk_color_below_ring == 'White':
    stalk_color_below_ring_w = 1
elif stalk_color_below_ring == 'Yellow':
    stalk_color_below_ring_y = 1

veil_color  = st.selectbox("Ingresa el color del velo.",
                        ['White','Orange','Yellow'])

if veil_color == 'Orange':
    veil_color_o = 1
elif veil_color == 'White':
    veil_color_w = 1
elif veil_color == 'Yellow':
    veil_color_y = 1
    
ring_number  = st.selectbox("Ingresa el numero de anillos.",
                        ['One','Two','None'])

if ring_number == 'One':
    ring_number_o = 1
elif ring_number == 'Two':
    ring_number_t = 1
    
ring_type  = st.selectbox("Ingresa el tipo de anillo.",
                        ['Pendant','Large','Flaring','None'])

if ring_type == 'Flaring':
    ring_type_f = 1
elif ring_type == 'Large':
    ring_type_l = 1
elif ring_type == 'None':
    ring_type_n = 1
elif ring_type == 'Pendant':
    ring_type_p = 1
    
spore_print_color  = st.selectbox("Ingresa el color de la espora.",
                        ['White','Brown','Black','Chocolate','Green','Purple','Orange','Yellow'])

if spore_print_color == 'Chocolate':
    spore_print_color_h = 1
elif spore_print_color == 'Black':
    spore_print_color_k = 1
elif spore_print_color == 'Brown':
    spore_print_color_n = 1
elif spore_print_color == 'Orange':
    spore_print_color_o = 1
elif spore_print_color == 'Green':
    spore_print_color_r = 1
elif spore_print_color == 'Purple':
    spore_print_color_u = 1
elif spore_print_color == 'White':
    spore_print_color_w = 1
elif spore_print_color == 'Yellow':
    spore_print_color_y = 1
    

population  = st.selectbox("Elige la población.",
                        ['Several','Solitary','Scattered','Numerous','Clustered'])

if population == 'Clustered':
    population_c = 1
elif population == 'Numerous':
    population_n = 1
elif population == 'Scattered':
    population_s = 1
elif population == 'Several':
    population_v = 1
elif population == 'Solitary':
    population_y = 1

habitat  = st.selectbox("habitat",
                        ['Woods','Grasses','Paths','Leaves','Urban','Meadows','Wase'])
if habitat == 'Grasses':
    habitat_g = 1
elif habitat == 'Leaves':
    habitat_l = 1
elif habitat == 'Meadows':
    habitat_m = 1
elif habitat == 'Paths':
    habitat_p = 1
elif habitat == 'Urban':
    habitat_u = 1
elif habitat == 'Wase':
    habitat_w = 1   


data = dataC()
if st.button('Predecir'):
    user_df = pd.DataFrame(data, index=[0])
    scale = StandardScaler()
    X_scaled = scale.fit_transform(user_df)
    preditcion_result = prediction.preditct(user_df,model)
    if preditcion_result == 0:
        st.image("images/e.png", width=200)
        st.text("El hongo es comestible c:")
    else:
        st.image("images/p.png", width=200)
        st.text("El hongo no es comestible @_@")
    