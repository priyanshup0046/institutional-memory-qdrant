# ⚖️ Navigating Evolving Supreme Court Precedents

A legal research and reasoning system for lawyers, law students, and citizens who cannot afford legal counsel.

This project helps users understand how Supreme Court jurisprudence evolves over time by mapping legal queries to past judgments, doctrinal phases, and institutional reasoning patterns.
It is especially useful in constitutional and privacy law, where judicial reasoning has shifted significantly across decades.

All detailed technical and theoretical explanations are maintained in separate documentation to keep this README clean, minimal, and accessible.

🎯 Intended Users

Practicing lawyers seeking relevant precedents and evolved reasoning

Junior lawyers and law students learning doctrinal development

Members of the general public seeking constitutional clarity

Researchers studying institutional judicial behavior

🧠 What the System Does

The system goes beyond keyword-based legal search. It:

Matches user queries to relevant Supreme Court reasoning

Identifies the governing doctrinal or institutional phase

Retrieves contextually relevant past judgments

Generates a grounded legal explanation based on precedent evolution

This enables users to understand not only what the law is, but why courts reason the way they do today.

## Project Structure

```text
project/
├── dataset/        # Institutional memory nodes (JSON)
├── embeddings/     # Text embedding logic
├── memory/         # Memory storage & evolution (Qdrant)
├── search/         # Semantic retrieval
├── generation/     # LLM-based answer generation
├── main.py         # End-to-end execution
└── README.md

```

## Setup Instructions
1. Install Dependencies

pip install -r requirements.txt

2. Create a .env File

API_KEY=your_google_api_key

Google Gemini is used for both embedding generation and answer generation.

3. Run the System

python main.py

## User Manual
How to Use the System

Open main.py

Replace the existing query with your case facts or legal question

Run the script

Review the generated legal reasoning and surfaced precedents

## Example Queries
Executive Surveillance During Protests

1.I am a junior lawyer working on a case where a state government has been collecting mobile location data of citizens during protests through executive orders, without passing any legislation.
The government is justifying this on grounds of national security.

Based on current Supreme Court jurisprudence, is such surveillance constitutionally valid, and which judgments should I rely on?

Collection of Telecom Metadata Without Disclosure

2.I am assisting in a case where a government agency has been collecting call detail records (CDRs) and metadata from telecom providers without informing the individuals concerned.
The collection is being carried out through internal executive directions, without any publicly disclosed law or oversight mechanism.

Does the right to privacy extend to metadata and telecom records, and which Supreme Court decisions support challenging such surveillance?

Large-Scale Digital Surveillance Programs

3.A central government program involves large-scale digital surveillance of citizens’ online activities for national security purposes.
The program operates without individual suspicion and lacks clear legislative safeguards.

Based on current Supreme Court jurisprudence, can such mass surveillance be justified, and what constitutional standards apply when evaluating its legality?

🚫 Out-of-Scope Queries

The system does not currently handle purely doctrinal or non–precedent-evolution questions such as:

Does Article 14 allow classification based on economic criteria in government welfare schemes?



