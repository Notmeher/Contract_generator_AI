import openai

def generate_prompt(section, party1, party2, details):
    """
    Generates a dynamic prompt based on the contract section.
    """
    return f"""
    Act as a legal contract generator.
    Create the section titled '{section}' for a service agreement between {party1} and {party2}.
    Ensure the section follows a formal tone and aligns with standard contract structures.
    Include all necessary legal terminology.
    Section Details:
    {details}
    Make sure the content is concise and doesn't have subsections or any bullet points. All responses should be in a single paragraph, clear and to the point.
    Keep it short and concise, avoiding excessive wording.
    """

sections = {
    "Introduction": "Define the parties involved, the purpose of the agreement, and the collaboration objectives.",
    "Appointment": "Specify that one party appoints the other on a non-exclusive basis to provide certain services.",
    "Scope of Work": "Describe the services provided, including key deliverables and responsibilities.",
    "Timeline": "Specify the contract duration, initial deliverables, and review schedules.",
    "Responsibilities": "Detail the roles of both parties in project execution, approvals, and communication.",
    "Compensation": "Outline payment structures, commission rates, and any associated costs.",
    "Confidentiality": "Include clauses to protect sensitive business information exchanged between both parties.",
    "Intellectual Property Rights": "Define ownership of materials, tools, and technology developed under this agreement.",
    "Performance Metrics and Reporting": "Specify reporting frequency, KPIs, and performance evaluation processes.",
    "Dispute Resolution": "Define the process for handling disputes, including mediation and legal jurisdiction.",
    "Termination": "Specify conditions under which the agreement can be terminated and any obligations post-termination.",
    "Training and Handover": "Outline the training provided and the post-implementation handover process.",
    "Amendments": "Describe how modifications to the contract will be made and documented.",
    "Marketing Rights": "Define the rights of either party to use non-sensitive work for marketing purposes.",
}
