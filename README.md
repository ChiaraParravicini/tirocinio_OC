# Reference Matching Tool for Crossref and OpenCitations Meta

Repository for a bibliographic reference matching tool designed for my master thesis in Digital Humanities and Digital Knowledge entitled "A method for matching bibliographic references with incomplete metadata in OpenCitations Meta". The tool is designed to identify and align references between [Crossref](https://www.crossref.org/) and [OpenCitations Meta](https://opencitations.net/meta). It implements a heuristic-based approach, enabling the retrieval and validation of bibliographic metadata even in cases of incomplete or inconsistent citation records.

### Key Features

- Extracts reference metadata from Crossref (JSON format)
- Queries the OpenCitations Meta SPARQL endpoint
- Applies heuristics to determine matches without relying on unique identifiers (DOIs)
- Includes an evaluation script that uses DOI matching **post-hoc** to validate results

## Repository Structure
```
src/
│ ReferenceMatchingTool.py - Main matching tool
│ evaluation.py - Evaluation script using DOI-based matching

data/
│ crossref_dataset/
│ GoldStandard_TEI/
│ grobid/
│ results/

README.md
requirements.txt
LICENSE
```

## How to Run

### Installation

```bash
git clone https://github.com/ChiaraParravicini/tirocinio_OC.git
cd tirocinio_OC
pip install -r requirements.txt

```

### Usage

Run the matching tool:

```bash
python src/ReferenceMatchingTool.py
```

Evaluate the results:

```bash
python src/evaluation.py
```

## Datasets

- Crossref dataset: JSON records collected from Crossref API.

- Gold Standard: TEI-XML structured dataset with complete metadata, manually annotated.

- Results: tool outputs and evaluation results.

<br>



Author: Chiara Parravicini

Thesis Project at Alma Mater Studiourum - Università di Bologna
