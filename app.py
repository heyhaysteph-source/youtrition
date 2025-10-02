# Start by importing the following libraries into the python script:
import pandas as pd # To import datasets as dataframes
pd.options.mode.chained_assignment = None  # default='warn'
import streamlit as st


import streamlit as st
st.set_page_config(page_title="Youtrition", layout="centered")


#The code for the UI- using the names from above:

st.markdown("""
    <style>
        html, body, [class*="css"]  {
            background-color: #000000;
            color: #ffffff;
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
    </style>
""", unsafe_allow_html=True)


st.markdown('<div class="header">Youtrition</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Personalized nutrition from your gut microbes</div>', unsafe_allow_html=True)
st.markdown('<div class="circle"></div><div class="semi-circle"></div><div class="rectangle"></div>', unsafe_allow_html=True)




st.write("Please answer the following questions to calculate your personalized nutrition advice:")

# Input fields
ibs = st.selectbox("Do you have Irritable Bowel Syndrome (IBS)?", 
                   ["Yes - Diagnosed by a Medical Professional", "Yes- Self Diagnosis", "No"])
ibd = st.selectbox("Do you have Inflammatory Bowel Disease (IBD)?", 
                   ["Yes - Diagnosed by a Medical Professional", "Yes- Self Diagnosis", "No"])
diet_type = st.selectbox("What is your current diet type?", ["Omnivore", "Omnivore without Red Meat", "Vegetarian", "Vegan", "Pescatarian",])
bowel_movement_frequency = st.slider("How many bowel movements do you have per day?", min_value=0, max_value=10, value=0)
bowel_movement_quality = st.selectbox(
    "How would you describe the quality of your bowel movements?",
    [
        "I don't know ",
        "I tend to have normal formed stool",
        "I tend to have diarrhea (watery stool)",
        "I tend to be constipated (have difficulty passing stool)"
    ]
)

dairy_indicated = st.selectbox("Do you consume dairy products?", ["Yes", "No"])
red_meat_indicated = st.selectbox("Do you consume red meat?", ["Yes", "No"])
alcohol_indicated = st.selectbox("Do you consume alcohol?", ["Yes", "No"])


# Country dropdown with 'United States' at the top
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
st.markdown("### Upload your gut microbiome data")
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


# Submit button
if st.button("Submit"):
    if uploaded_file and 'microbiome_data' in locals():
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

        # Build input dictionary for prediction
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

        # Run prediction
        try:
            prediction_df = predict_dietary_recommendations(
                input_data,
                microbiome_data,
                random_forest,
                encoder,
                scaler,
                X_features,
                y_features,
                unique_species,
                 complete_dataset_df_clean
            )

            st.markdown("### Your Predicted Dietary Frequencies")
            st.dataframe(prediction_df[y_features])

            st.markdown("### Recommended Adjustments")
            for col in prediction_df.columns:
                if "Recommendation" in col and pd.notna(prediction_df.loc[0, col]):
                    st.markdown(f"✅ **{col.replace('_', ' ')}:** {prediction_df.loc[0, col]}")

        except Exception as e:
            st.error(f"Prediction failed: {e}")
    else:
        st.error("Please upload your microbiome Excel file before submitting.")



def predict_dietary_recommendations(


# Increased Fiber Recommendation
    bowel_movement_quality = X_new['bowel_movement_quality'].iloc[0] if 'bowel_movement_quality' in X_new.columns else None
    vegetable_frequency = y_pred_unencoded_df['vegetable_frequency'].iloc[0] if 'vegetable_frequency' in y_pred_unencoded_df.columns else None
    bowel_movement_frequency = X_new['bowel_movement_frequency'].iloc[0] if 'bowel_movement_frequency' in X_new.columns else None

    if (bowel_movement_quality is not None and 'constipated' in str(bowel_movement_quality).lower()) or \
       (vegetable_frequency is not None and vegetable_frequency not in ['Daily', 'Regularly (3-5 times/week)', 'Never', 'Not provided', 'Not collected']) or \
       (bowel_movement_frequency is not None and bowel_movement_frequency in ['Four', 'Five or more']):
        recommendations['Increased Fiber Recommendation'] = 'Consider increasing fiber intake, including addition of soluble fiber-rich vegetables.'
    else:
        recommendations['Increased Fiber Recommendation'] = np.nan

    # Low FODMAP Recommendation
    ibs_status = X_new['ibs'].iloc[0] if 'ibs' in X_new.columns else None
    ibd_status = X_new['ibd'].iloc[0] if 'ibd' in X_new.columns else None

    if (ibs_status is not None and ibs_status not in [np.nan, 'I do not have this condition', 'Unspecified', 'Not provided', 'Not collected']) or \
       (ibd_status is not None and ibd_status not in [np.nan, 'I do not have this condition', 'Unspecified', 'Not provided', 'Not collected']):
        recommendations['Low FODMAP Recommendation'] = 'Consider a Low FODMAP diet with decreased carbohydrates.'
    else:
        recommendations['Low FODMAP Recommendation'] = np.nan

    # Reduce Dairy Intake Recommendation
    milk_cheese_frequency = y_pred_unencoded_df['milk_cheese_frequency'].iloc[0] if 'milk_cheese_frequency' in y_pred_unencoded_df.columns else None

    # No need to recommend the reduction of food categories the individual already indicated they don't include in their diet
    if 'dairy_indicated' in original_data.columns and original_data['dairy_indicated'].iloc[0] == 'No':
        recommendations['Reduce Dairy Recommendation'] = np.nan
    elif (milk_cheese_frequency is not None and milk_cheese_frequency not in ['Rarely (less than once/week)', 'Never', 'Not provided', 'Not collected']) and \
       ((ibs_status is not None and ibs_status not in [np.nan, 'I do not have this condition', 'Unspecified', 'Not provided', 'Not collected']) or \
        (ibd_status is not None and ibd_status not in [np.nan, 'I do not have this condition', 'Unspecified', 'Not provided', 'Not collected'])):
        recommendations['Reduce Dairy Recommendation'] = 'Consider reducing dairy intake or using dairy substitutes (such as soy or almond milk).'
    else:
        recommendations['Reduce Dairy Recommendation'] = np.nan

    # Reduce Red Meat Intake Recommendation
    red_meat_frequency = y_pred_unencoded_df['red_meat_frequency'].iloc[0] if 'red_meat_frequency' in y_pred_unencoded_df.columns else None

    if 'red_meat_indicated' in original_data.columns and original_data['red_meat_indicated'].iloc[0] == 'No':
        recommendations['Reduce Red Meat Recommendation'] = np.nan
    elif (red_meat_frequency is not None and red_meat_frequency not in ['Rarely (less than once/week)', 'Occasionally (1-2 times/week)', 'Never', 'Not provided', 'Not collected']) and \
       ((ibs_status is not None and ibs_status not in [np.nan, 'I do not have this condition', 'Unspecified', 'Not provided', 'Not collected']) or \
        (ibd_status is not None and ibd_status not in [np.nan, 'I do not have this condition', 'Unspecified', 'Not provided', 'Not collected'])):
        recommendations['Reduce Red Meat Recommendation'] = 'Consider reducing red meat intake.'
    else:
        recommendations['Reduce Red Meat Recommendation'] = np.nan

    # Reduce Alcohol Intake Recommendation
    alcohol_frequency = y_pred_unencoded_df['alcohol_frequency'].iloc[0] if 'alcohol_frequency' in y_pred_unencoded_df.columns else None
    if 'alcohol_indicated' in original_data.columns and original_data['alcohol_indicated'].iloc[0] == 'No':
        recommendations['Reduce Alcohol Recommendation'] = np.nan
    elif (alcohol_frequency is not None and alcohol_frequency not in ['Rarely (a few times/month)', 'Never', 'Not provided', 'Not collected']) or \
       (alcohol_frequency is not None and alcohol_frequency in ['Regularly (3-5 times/week)', 'Daily']):
        recommendations['Reduce Alcohol Recommendation'] = 'Consider reducing alcohol intake.'
    else:
        recommendations['Reduce Alcohol Recommendation'] = np.nan

# Add recommendations to the output DataFrame
    output_df = y_pred_unencoded_df.copy()
    for key, value in recommendations.items():
        output_df[key] = value

    return output_df
"""


