import streamlit as st
from agent import CallAIAgent

# Initialize the agent
agent = CallAIAgent()

# Streamlit app
st.set_page_config(page_title="CallAI - Contract Generator", layout="wide")

# Sidebar for inputs
with st.sidebar:
    st.title("Contract Generator")
    
    # Party Names
    party1 = st.text_input("Enter the first party name:", placeholder="e.g., Company A")
    party2 = st.text_input("Enter the second party name:", placeholder="e.g., Company B")

    # Start Date Input
    start_date = st.date_input("Select the contract start date:")

    # Section Inputs
    sections_data = {}
    sections_data["Introduction"] = st.text_area("1. Introduction", "Define the parties involved, the purpose of the agreement, and the collaboration objectives.", height=150, placeholder="e.g., Define the purpose of the agreement, parties involved, and collaboration objectives.")
    sections_data["Appointment"] = st.text_area("2. Appointment", "Specify that one party appoints the other on a non-exclusive basis to provide certain services.", height=150, placeholder="e.g., Specify non-exclusive appointments and services.")
    sections_data["Scope of Work"] = st.text_area("3. Scope of Work", "Describe the services provided, including key deliverables and responsibilities.", height=150, placeholder="e.g., Describe the deliverables, services, and responsibilities.")
    sections_data["Timeline"] = st.text_area("4. Timeline", "Specify the contract duration, initial deliverables, and review schedules.", height=150, placeholder="e.g., Specify contract duration and deliverables.")
    sections_data["Responsibilities"] = st.text_area("5. Responsibilities", "Detail the roles of both parties in project execution, approvals, and communication.", height=150, placeholder="e.g., Specify the roles, approvals, and communication.")
    sections_data["Compensation"] = st.text_area("6. Compensation", "Outline payment structures, commission rates, and any associated costs.", height=150, placeholder="e.g., Specify payment structures, commission rates, and costs.")
    sections_data["Confidentiality"] = st.text_area("7. Confidentiality", "Include clauses to protect sensitive business information exchanged between both parties.", height=150, placeholder="e.g., Define confidentiality clauses for sensitive information.")
    sections_data["Intellectual Property Rights"] = st.text_area("8. Intellectual Property Rights", "Define ownership of materials, tools, and technology developed under this agreement.", height=150, placeholder="e.g., Define ownership of materials, technology, and IP rights.")
    sections_data["Performance Metrics and Reporting"] = st.text_area("9. Performance Metrics and Reporting", "Specify reporting frequency, KPIs, and performance evaluation processes.", height=150, placeholder="e.g., Specify reporting and performance metrics.")
    sections_data["Dispute Resolution"] = st.text_area("10. Dispute Resolution", "Define the process for handling disputes, including mediation and legal jurisdiction.", height=150, placeholder="e.g., Define dispute resolution process, mediation, and jurisdiction.")
    sections_data["Termination"] = st.text_area("11. Termination", "Specify conditions under which the agreement can be terminated and any obligations post-termination.", height=150, placeholder="e.g., Specify conditions for termination and post-termination obligations.")
    sections_data["Training and Handover"] = st.text_area("12. Training and Handover", "Outline the training provided and the post-implementation handover process.", height=150, placeholder="e.g., Outline the training and handover process.")
    sections_data["Amendments"] = st.text_area("13. Amendments", "Describe how modifications to the contract will be made and documented.", height=150, placeholder="e.g., Describe amendments process and documentation.")
    sections_data["Marketing Rights"] = st.text_area("14. Marketing Rights", "Define the rights of either party to use non-sensitive work for marketing purposes.", height=150, placeholder="e.g., Define rights for using non-sensitive work for marketing.")

# Content display area
st.title("Generated Contract")
generated_content = st.empty()  # Placeholder for generated content

# A button to generate the contract after sections are filled
if st.button("Generate Full Contract"):
    if party1.strip() and party2.strip():
        with st.spinner("Generating contract..."):
            # Call agent to generate the full contract
            full_contract = agent.generate_full_contract(party1, party2, start_date, sections_data)
            st.success("Contract Generated!")
            generated_content.markdown(full_contract)  # Display the generated contract
    else:
        st.error("Please enter the names of both parties.")
