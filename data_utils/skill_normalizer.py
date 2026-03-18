import re
from typing import List, Set

class SkillNormalizer:
    """
    Standardizes skill strings to improve match accuracy between 
    resumes and job descriptions.
    """

    # Mapping of common variations to a canonical form
    SKILL_MAP = {
        "python3": "python",
        "py": "python",
        "js": "javascript",
        "node": "nodejs",
        "reactjs": "react",
        "react.js": "react",
        "vuejs": "vue",
        "mongodb": "mongo",
        "postgres": "postgresql",
        "aws": "amazon web services",
        "ml": "machine learning",
        "ai": "artificial intelligence",
        "genai": "generative ai",
        "llms": "llm"
    }

    @staticmethod
    def normalize(skill: str) -> str:
        """
        Cleans and standardizes a single skill string.
        """
        # Lowercase and remove special characters/extra whitespace
        clean_skill = skill.lower().strip()
        clean_skill = re.sub(r'[^a-z0-9\s\.\+#]', '', clean_skill)
        
        # Apply mapping if exists
        return SkillNormalizer.SKILL_MAP.get(clean_skill, clean_skill)

    @classmethod
    def normalize_list(cls, skills: List[str]) -> List[str]:
        """
        Normalizes a list of skills and removes duplicates.
        """
        if not skills:
            return []
            
        normalized_set: Set[str] = set()
        for s in skills:
            normalized_val = cls.normalize(s)
            if normalized_val:
                normalized_set.add(normalized_val)
                
        return sorted(list(normalized_set))

    @classmethod
    def get_skill_intersection(cls, resume_skills: List[str], jd_skills: List[str]) -> List[str]:
        """
        Finds the common skills between the resume and JD after normalization.
        """
        res_set = set(cls.normalize_list(resume_skills))
        jd_set = set(cls.normalize_list(jd_skills))
        
        return sorted(list(res_set.intersection(jd_set)))