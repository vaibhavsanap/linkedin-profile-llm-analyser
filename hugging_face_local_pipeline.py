from transformers import pipeline


classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")


def classify_user():
    # JSON file
    f = open('linkedin_scrapper/profile.json', "r")
    # Reading from file
    linked_in_profile_to_classify = f.read()

    candidate_labels = ['technical', 'non-technical']
    result = classifier(linked_in_profile_to_classify, candidate_labels)
    print(result['labels'], result['scores'])
    return result
