import plotly.graph_objects as go
import logging

logger = logging.getLogger(__name__)

def create_score_bar_chart(skill_score: float, semantic_score: float, experience_score: float, final_score: float) -> go.Figure:
    """
    Creates a horizontal bar chart displaying the breakdown of the candidate's scores.
    """
    categories = ['Final Match Score', 'Experience Match (20%)', 'Semantic Similarity (35%)', 'Skill Match (45%)']
    scores = [final_score, experience_score, semantic_score, skill_score]
    
    # Define colors based on score thresholds
    colors = []
    for score in scores:
        if score >= 80:
            colors.append('#2ca02c') # Green
        elif score >= 60:
            colors.append('#ff7f0e') # Orange
        else:
            colors.append('#d62728') # Red

    try:
        fig = go.Figure(go.Bar(
            x=scores,
            y=categories,
            orientation='h',
            marker_color=colors,
            text=[f"{score:.1f}%" for score in scores],
            textposition='auto'
        ))

        fig.update_layout(
            title="Candidate Evaluation Breakdown",
            xaxis=dict(title="Score (%)", range=[0, 100]),
            yaxis=dict(title=""),
            margin=dict(l=20, r=20, t=40, b=20),
            height=300
        )
        return fig
    except Exception as e:
        logger.error(f"Error generating chart: {str(e)}")
        return go.Figure() # Return empty figure on failure