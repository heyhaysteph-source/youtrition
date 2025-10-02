import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import streamlit as st
import random

# Page configuration
st.set_page_config(page_title="Youtrition", layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
        html, body, [class*="css"]  {
            background-color: #000000 !important;
            color: #ffffff !important;
        }
        .main {
            background-color: #000000 !important;
        }
        header, .css-1v3fvcr, .css-1dp5vir {
            background-color: #000000 !important;
        }
        .stApp {
            background-color: #000000 !important;
        }
        .circle {
            width: 60px;
            height: 60px;
            background-color: #6d31fd;
            border-radius: 50%;
            display: inline-block;
            margin: 10px;
        }
        .semi-circle {
            width: 60px;
            height: 30px;
            background-color: #ffdf5f;
            border-top-left-radius: 60px;
            border-top-right-radius: 60px;
            display: inline-block;
            margin: 10px;
        }
        .rectangle {
            width: 120px;
            height: 40px;
            background-color: #066b6b;
            display: inline-block;
            margin: 10px;
        }
        .header {
            font-size: 48px;
            color: #ffffff;
            font-weight: bold;
        }
        .subheader {
            font-size: 20px;
            color: #ff8127;
        }
        .subheader2 {
            font-size: 20px;
            color: #066b6b;
         }
        .subheader3 {
            font-size: 20px;
            color: #6d31fd;
        }
        .subheader4 {
            font-size: 20px;
            color: #ffdf5f;
        }
        
        
        .highlight {
            background-color: #ffdf5f;
            color: #000000;
            padding: 5px 10px;
            border-radius: 10px;
            font-weight: bold;
        }
        .cta-button {
            background-color: #ff8127;
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
            font-weight: bold;
            border: none;
        }
        /* Style radio buttons like neon buttons */
        div[data-baseweb="radio"] > div {
            background-color: #000000;
            border-radius: 8px;
            padding: 10px;
        }
        div[data-baseweb="radio"] label {
            color: #ffffff;
            font-weight: bold;
            background-color: #6d31fd;
            border-radius: 6px;
            padding: 8px 12px;
            margin: 5px;
            display: inline-block;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        div[data-baseweb="radio"] label:hover {
            background-color: #ff8127;
        }
        div[data-baseweb="radio"] input:checked + div {
            background-color: #ffdf5f !important;
            color: #000000 !important;
        }
        /* Style radio button labels (answers) */
            div[data-baseweb="radio"] label {
            color: #6d31fd !important; /* default text color */
            font-weight: bold;
        }

/* Style selected radio button answer */
div[data-baseweb="radio"] input:checked + div {
    background-color: #ffdf5f !important; /* yellow background */
    color: #000000 !important; /* black text */
    font-weight: bold;
    border-radius: 6px;
    padding: 8px 12px;
}

        /* Make form labels (questions) white */
        label, .stSelectbox label, .stRadio label, .stSlider label {
            color: #ffffff !important;
        }

        
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header">Youtrition</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Personalized nutrition from your gut microbes</div>', unsafe_allow_html=True)
st.markdown('<div class="circle"></div><div class="semi-circle"></div><div class="rectangle"></div>', unsafe_allow_html=True)

# Input fields
st.markdown('<div class="subheader4">Please answer the following questions to calculate your personalized nutrition advice:</div>', unsafe_allow_html=True)


ibs = st.selectbox("Do you have Irritable Bowel Syndrome (IBS)?", 
                   ["","Yes - Diagnosed by a Medical Professional", "Yes- Self Diagnosis", "No"])
ibd = st.selectbox("Do you have Inflammatory Bowel Disease (IBD)?", 
                   ["","Yes - Diagnosed by a Medical Professional", "Yes- Self Diagnosis", "No"])
diet_type = st.selectbox("What is your current diet type?", ["","Omnivore","Vegetarian", "Vegan", "Pescatarian"])
bowel_movement_frequency = st.slider("How many bowel movements do you have per day?", min_value=0, max_value=10, value=0)
bowel_movement_quality = st.selectbox(
    "How would you describe the quality of your bowel movements?",
    [   "",
        "I don't know ",
        "I tend to have normal formed stool",
        "I tend to have diarrhea (watery stool)",
        "I tend to be constipated (have difficulty passing stool)"
    ]
)
dairy_indicated = st.radio("Do you consume dairy products?", ["Yes", "No"], horizontal=True)
red_meat_indicated = st.radio("Do you consume red meat?", ["Yes", "No"], horizontal=True)
alcohol_indicated = st.radio("Do you consume alcohol?", ["Yes", "No"], horizontal=True)


# Country dropdown
countries = ['United states', 'Turkey', 'Australia', 'Singapore', 'Spain', 'Mexico', 'Czech republic',
             'Trinidad and tobago', 'Canada', 'India', 'Belgium', 'Korea, republic of', 'Bangladesh',
             'Philippines', 'Dominican republic', 'Moldova, republic of', 'China', 'Poland', 'Germany',
             'Denmark', 'United kingdom', 'Ireland', 'Russian federation', 'Kenya', 'France', 'South africa',
             'Venezuela', 'Guam', 'Argentina', 'Japan', 'Uruguay', 'Not provided', 'Greece', 'Switzerland',
             'New zealand', 'Malawi', 'Finland', 'Puerto rico', 'Brazil', 'Kuwait', 'Hong kong', 'Pakistan',
             'Italy', 'Jersey', 'Iran, islamic republic of', 'Romania', 'Zambia', 'Panama', 'Estonia', 'Chile',
             'Croatia', 'Tanzania, united republic of', 'Syrian arab republic', 'Hungary', 'Uzbekistan',
             'Gibraltar', 'Kazakhstan', 'Colombia', 'Norway', 'Ukraine', 'Albania', 'Serbia', 'Austria',
             'Malaysia', 'Latvia', 'Nepal', 'Guatemala', 'Belarus', 'Ghana', 'Jamaica', 'Israel', 'Bolivia',
             'Bulgaria', 'Portugal', 'Netherlands', 'Sweden', 'Viet nam', 'Mauritius', 'Tajikistan',
             'Netherlands antilles', 'Thailand', 'Bahrain', 'Iceland', 'Uganda', 'Cyprus', 'Egypt', 'Cambodia',
             'Luxembourg', 'Indonesia', 'Taiwan, province of china', 'Sri lanka', 'Slovenia', 'Peru',
             'Not collected', 'Bosnia and herzegovina', 'United arab emirates',
             'United states minor outlying islands', 'Saudi arabia', 'Mongolia', 'Malta', 'Zimbabwe',
             'Libyan arab jamahiriya', 'Lithuania', 'Morocco', 'El salvador', 'Guernsey', 'Azerbaijan', 'Fiji',
             'Tunisia', 'Virgin islands, u.s.', 'Nigeria', 'Costa rica', 'Cuba', 'Slovakia', 'Ethiopia',
             'Afghanistan', "Cote d'ivoire", 'Algeria', 'Paraguay', 'Lebanon', 'Dominica', 'Bermuda', 'Angola',
             'Somalia', 'Sudan', 'Guyana', 'Isle of man', 'Palestinian territory, occupied', 'Iraq', 'Botswana',
             'Seychelles', 'Macedonia, the former yugoslav republic of', 'Georgia']
sorted_countries = sorted(set(countries), key=lambda x: x.lower())
if 'United states' in sorted_countries:
    sorted_countries.remove('United states')
    sorted_countries.insert(0, 'United states')
country_of_birth = st.selectbox("What country were you born in?", sorted_countries)

# Microbiome Excel uploader
st.markdown('<div class="subheader3">Upload Your Gut Biome Data </div>', unsafe_allow_html=True)
uploaded_file = st.file_uploader(
    "Upload your gut microbiome data (Excel format: .xlsx or .xls)",
    type=["xlsx", "xls"]
)

required_species = [
    's__copri', 's__stutzeri', 's__uniformis', 's__johnsonii', 's__faecis', 's__mucosae', 's__mucilaginosa',
    's__diminuta', 's__luteciae', 's__rhizosphaerae', 's__catus', 's__eutactus', 's__perfringens',
    's__adolescentis', 's__prausnitzii', 's__gnavus', 's__biforme', 's__stercorea', 's__veronii', 's__lwoffii',
    's__piliforme', 's__bromii', 's__dispar', 's__muciniphila', 's__caccae', 's__ruminis', 's__acidaminiphila',
    's__ovatus', 's__aerofaciens', 's__nitroreducens', 's__parainfluenzae', 's__obeum'
]

# Microbiome Excel uploader logic
if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)
        missing_cols = [col for col in required_species if col not in df.columns]

        if missing_cols:
            st.error(f"Missing required species columns: {missing_cols}")
        else:
            st.success("All required species columns are present.")
            microbiome_data = df[required_species].copy()
            for col in microbiome_data.columns:
                microbiome_data[col] = pd.to_numeric(microbiome_data[col], errors='coerce')
            st.write("Preview of your formatted microbiome data:")
            st.dataframe(microbiome_data.head())

    except Exception as e:
        st.error(f"Error reading or processing file: {e}")

# Recommendation function
def predict_dietary_recommendations(input_data):
    list1 = [1, 2, 3, 4, 5]
    rando_rec = random.choice(list1)
    return rando_rec

# Submit button logic
if st.button("Submit"):
    if uploaded_file and 'microbiome_data' in locals():
        # Validate required fields
        required_fields = [ibs, ibd, diet_type, bowel_movement_quality, country_of_birth]
        if "" in required_fields:
            st.error("Please complete all fields before submitting.")
            st.stop()

        st.success("Thank you! Your responses have been recorded.")
        st.write("Here's a summary of your input:")
        st.write({
            "IBS": ibs,
            "IBD": ibd,
            "Diet Type": diet_type,
            "Bowel Movement Frequency": bowel_movement_frequency,
            "Bowel Movement Quality": bowel_movement_quality,
            "Country of Birth": country_of_birth,
        })

        input_data = {
            'ibs': 'True' if 'Yes' in ibs else 'False',
            'ibd': 'True' if 'Yes' in ibd else 'False',
            'diet_type': diet_type,
            'Do you consume dairy products?': dairy_indicated,
            'Do you consume red meat?': red_meat_indicated,
            'Do you consume alcohol?': alcohol_indicated,
            'bowel_movement_frequency_numerical': bowel_movement_frequency,
            'bowel_movement_quality': bowel_movement_quality,
            'country_of_birth': country_of_birth,
            'dairy_indicated': dairy_indicated,
            'red_meat_indicated': red_meat_indicated,
            'alcohol_indicated': alcohol_indicated
        }

        try:
            rando_rec = predict_dietary_recommendations(input_data)

            if rando_rec == 1:
                recommendation = 'Consider increasing fiber intake, including addition of soluble fiber-rich vegetables.'
            elif rando_rec == 2:
                recommendation = 'Consider a Low FODMAP diet with decreased carbohydrates.'
            elif rando_rec == 3:
                recommendation = 'Consider reducing red meat intake.'
            elif rando_rec == 4:
                recommendation = 'Consider reducing dairy intake.'
            elif rando_rec == 5:
                recommendation = 'Consider reducing alcohol intake.'
            else:
                recommendation = 'Maintain your current diet and lifestyle.'

            st.markdown('<div class="circle"></div><div class="semi-circle"></div><div class="rectangle"></div>', unsafe_allow_html=True)
            st.markdown('<div class="subheader">Your personalized nutrition recommendations:</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="highlight">{recommendation}</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Prediction failed: {e}")
    else:
        st.error("Please upload your microbiome Excel file before submitting.")
