# Plant Disease Treatment Remedies Mapping

REMEDIES_DATABASE = {
    "Apple___Apple_scab": "Apply fungicide containing captan or mancozeb. Prune affected leaves and destroy fallen leaf debris to prevent spore overwintering.",
    "Apple___Black_rot": "Remove and incinerate infected branches and mummified fruit. Spray copper-based fungicides before bud break.",
    "Apple___Cedar_apple_rust": "Apply myclobutanil or sulfur sprays during early leaf development. Remove nearby red cedar hosts if present.",
    "Apple___healthy": "Apple tree foliage is healthy! Maintain regular watering, balanced fertilization, and annual pruning.",
    "Blueberry___healthy": "Blueberry plant is in excellent health. Maintain acidic soil pH (4.5 - 5.5) and organic pine bark mulching.",
    "Cherry_(including_sour)___Powdery_mildew": "Apply sulfur or potassium bicarbonate sprays at early infection signs. Improve air circulation through canopy pruning.",
    "Cherry_(including_sour)___healthy": "Cherry foliage is healthy. Continue monitoring for aphid or fruit fly activity.",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": "Apply azoxystrobin or pyraclostrobin fungicides. Practice crop rotation with non-host crops like soybeans or legumes.",
    "Corn_(maize)___Common_rust_": "Use resistant maize hybrids. If severe, apply foliar fungicides during early silking.",
    "Corn_(maize)___Northern_Leaf_Blight": "Apply mancozeb or propiconazole fungicide upon first symptom appearance. Till crop residue under after harvest.",
    "Corn_(maize)___healthy": "Corn crop is healthy. Ensure adequate nitrogen top-dressing at silking stage.",
    "Grape___Black_rot": "Remove infected berries. Spray broad-spectrum fungicides such as chlorothalonil or mancozeb from pre-bloom to 4 weeks after bloom.",
    "Grape___Esca_(Black_Measles)": "Prune out dead wood and protect pruning wounds with sealant. Avoid over-irrigation.",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": "Apply copper hydroxide or sulfur sprays after harvest and early spring.",
    "Grape___healthy": "Grapevine is healthy. Maintain canopy management and cluster thinning for optimal fruit quality.",
    "Orange___Haunglongbing_(Citrus_greening)": "Control Asian citrus psyllid vectors using systemic insecticides (imidacloprid). Remove severely infected trees and provide micronutrient foliar sprays.",
    "Peach___Bacterial_spot": "Apply copper sprays during dormant season and early spring. Avoid excessive nitrogen fertilization.",
    "Peach___healthy": "Peach foliage is healthy. Ensure adequate thinning of fruit clusters for larger peaches.",
    "Pepper,_bell___Bacterial_spot": "Spray copper-based bactericides combined with mancozeb. Avoid overhead sprinkler irrigation.",
    "Pepper,_bell___healthy": "Bell pepper plants are healthy. Provide uniform drip irrigation to prevent blossom end rot.",
    "Potato___Early_blight": "Apply chlorothalonil or mancozeb at 7-10 day intervals. Ensure proper potassium nutrition.",
    "Potato___Late_blight": "Apply systemic fungicides (metalaxyl or cymoxanil) immediately. Remove infected vines before harvest to prevent tuber rot.",
    "Potato___healthy": "Potato plants are healthy. Maintain earthing up to protect developing tubers from light exposure.",
    "Raspberry___healthy": "Raspberry canes are healthy. Ensure trellising and annual removal of old floricanes.",
    "Soybean___healthy": "Soybean foliage is healthy. Monitor for stem borer or pod borer pests.",
    "Squash___Powdery_mildew": "Apply neem oil, sulfur, or potassium bicarbonate solutions to leaf surfaces.",
    "Strawberry___Leaf_scorch": "Remove infected older leaves. Apply copper fungicides after renovation.",
    "Strawberry___healthy": "Strawberry foliage is healthy. Keep beds weed-free and straw mulched.",
    "Tomato___Bacterial_spot": "Apply copper hydroxide sprays mixed with mancozeb. Avoid handling plants when wet.",
    "Tomato___Early_blight": "Prune lower leaves touching soil. Apply copper or chlorothalonil fungicide weekly during rainy periods.",
    "Tomato___Late_blight": "Destroy infected plants immediately. Spray copper fungicide proactively during cool, humid weather.",
    "Tomato___Leaf_Mold": "Improve greenhouse ventilation and lower relative humidity below 85%. Apply difenoconazole if needed.",
    "Tomato___Septoria_leaf_spot": "Remove affected lower leaves. Apply chlorothalonil or copper-based sprays every 7-14 days.",
    "Tomato___Spider_mites Two-spotted_spider_mite": "Spray abamectin or insecticidal soap under leaves. Increase ambient humidity.",
    "Tomato___Target_Spot": "Apply azoxystrobin or chlorothalonil fungicides. Ensure adequate plant spacing for airflow.",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": "Control whitefly vectors using yellow sticky traps and neem oil sprays. Remove infected plants to prevent viral spread.",
    "Tomato___Tomato_mosaic_virus": "Disinfect tools with 10% trisodium phosphate. Remove infected plants. Avoid using tobacco near plants.",
    "Tomato___healthy": "Tomato plant is vibrant and healthy! Continue balanced watering and regular staking."
}

def get_remedy(disease_name: str) -> str:
    clean_name = disease_name.strip()
    if clean_name in REMEDIES_DATABASE:
        return REMEDIES_DATABASE[clean_name]
    
    if "healthy" in clean_name.lower():
        return "Crop foliage appears healthy! Continue standard irrigation, fertilization, and crop monitoring."
    
    return "Apply suitable broad-spectrum organic or chemical fungicide/bactericide. Ensure proper field sanitation, crop rotation, and consult a local agricultural extension officer."

