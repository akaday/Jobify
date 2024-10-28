import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def parse_resume(resume_text):
    doc = nlp(resume_text)
    experiences = [ent.text for ent in doc.ents if ent.label_ == "WORK_OF_ART"]
    return experiences

# Example usage
if __name__ == "__main__":
    sample_resume = "Experienced software engineer with a background in developing AI applications. Worked at Microsoft."
    parsed_experiences = parse_resume(sample_resume)
    print(parsed_experiences)
