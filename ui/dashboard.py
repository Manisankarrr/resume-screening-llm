import streamlit as st
from typing import List, Dict, Any

def render_header():
    """Renders the main application header and description."""
    st.title("🎯 AI Resume Screening System")
    st.markdown("""
    Evaluate candidate resumes against a job description using LLMs and Vector Embeddings.
    * **LLM Agents** extract structured data and perform logical evaluation.
    * **Embeddings** calculate semantic similarity between the resume and the job posting.
    """)
    st.divider()

def render_input_section() -> tuple:
    """
    Renders the file upload and job description input areas.
    Returns the uploaded files and the job description text.
    """
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. Upload Resumes")
        uploaded_files = st.file_uploader(
            "Upload 1 to 3 PDF resumes", 
            type=["pdf"], 
            accept_multiple_files=True
        )
        if len(uploaded_files) > 3:
            st.warning("Please upload a maximum of 3 resumes at a time.")
            uploaded_files = uploaded_files[:3]
            
    with col2:
        st.subheader("2. Job Description")
        job_description = st.text_area(
            "Paste the full Job Description here", 
            height=200,
            placeholder="e.g., We are looking for a Senior Software Engineer with 5+ years of experience in Python, React, and AWS..."
        )
        
    return uploaded_files, job_description

def render_candidate_results(candidate_name: str, results: Dict[str, Any], chart_fig):
    """
    Renders the evaluation results for a single candidate inside an expander.
    """
    with st.expander(f"Results for: {candidate_name}", expanded=True):
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.plotly_chart(chart_fig, use_container_width=True)
            
        with col2:
            st.markdown("### Evaluation Summary")
            st.write(results['explanation'])
            
            st.markdown("### Skill Gap Analysis")
            st.warning(results['skill_gap_analysis'])
            
        st.divider()
        st.markdown("#### Extracted Data Reference")
        st.json({
            "Extracted Skills": results['extracted_skills'],
            "Years of Experience": results['experience_years']
        })