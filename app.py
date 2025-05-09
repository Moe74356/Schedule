
import streamlit as st
import pandas as pd
import openai
import os

st.title("Construction Schedule Generator MVP")

st.markdown("Upload your project scope, BOQ, and productivity rates to generate a draft schedule.")

uploaded_boq = st.file_uploader("Upload BOQ (Excel or CSV)", type=["xlsx", "csv"])
uploaded_scope = st.file_uploader("Upload Scope Document (Text)", type=["txt"])
uploaded_productivity = st.file_uploader("Upload Productivity Rates (Excel or CSV)", type=["xlsx", "csv"])

if st.button("Generate Schedule"):
    if uploaded_boq and uploaded_scope and uploaded_productivity:
        try:
            # Read BOQ
            if uploaded_boq.name.endswith(".csv"):
                boq_df = pd.read_csv(uploaded_boq)
            else:
                boq_df = pd.read_excel(uploaded_boq)

            # Read Productivity
            if uploaded_productivity.name.endswith(".csv"):
                prod_df = pd.read_csv(uploaded_productivity)
            else:
                prod_df = pd.read_excel(uploaded_productivity)

            # Read Scope
            scope_text = uploaded_scope.read().decode("utf-8")

            # Mock WBS/Activity Generation
            boq_df['Activity'] = boq_df['Description']
            boq_df['Duration (days)'] = boq_df['Quantity'] / 10  # Simplified logic
            boq_df['Predecessors'] = ""

            st.success("Schedule generated successfully!")
            st.dataframe(boq_df[['Activity', 'Quantity', 'Unit', 'Duration (days)', 'Predecessors']])

            csv = boq_df.to_csv(index=False).encode('utf-8')
            st.download_button("Download Schedule CSV", csv, "schedule.csv", "text/csv")

        except Exception as e:
            st.error(f"Error processing files: {e}")
    else:
        st.warning("Please upload all required documents.")
