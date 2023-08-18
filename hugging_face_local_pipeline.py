from transformers import pipeline

classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")

linked_in_profile_to_classify = "Software engineer, java, python"

candidate_labels = ['technical', 'non-technical']

print(classifier(linked_in_profile_to_classify, candidate_labels))

