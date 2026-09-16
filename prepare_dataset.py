import os
import xml.etree.ElementTree as ET
import pandas as pd


MEDQUAD_FOLDER = "MedQuAD"
OUTPUT_FILE = "medquad.csv"


def extract_text(element, tag_name):
    """
    Find the first matching XML element and return its text.
    """
    element_found = element.find(".//" + tag_name)

    if element_found is not None and element_found.text:
        return element_found.text.strip()

    return ""


def process_xml_file(file_path):

    records = []

    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        for qa in root.findall(".//QAPair"):

            question = extract_text(qa, "Question")
            answer = extract_text(qa, "Answer")

            if question and answer:

                records.append({
                    "question": question,
                    "answer": answer
                })

    except Exception as e:
        print("Error reading:", file_path)
        print(e)

    return records


all_records = []


for root_dir, directories, files in os.walk(MEDQUAD_FOLDER):

    for filename in files:

        if filename.lower().endswith(".xml"):

            file_path = os.path.join(root_dir, filename)

            print("Processing:", file_path)

            records = process_xml_file(file_path)

            all_records.extend(records)


df = pd.DataFrame(all_records)

df = df.drop_duplicates()

df.to_csv(
    OUTPUT_FILE,
    index=False,
    encoding="utf-8"
)

print()
print("Dataset preparation completed.")
print("Total QA pairs:", len(df))
print("Saved as:", OUTPUT_FILE)
