**Project Title**:-
Helping Lawyers, General Public who cant afford lawyers and law Students to Navigate Evolving Supreme Court Precedents

All details regarding project is added to the documentation to keep the Readme file as simple and minimal as possible.

**Project Structure**:-
project/
├── dataset/ # Institutional memory nodes (JSON)
├── embeddings/ # Text embedding logic
├── memory/ # Memory storage & evolution (Qdrant)
├── search/ # Semantic retrieval
├── generation/ # LLM-based answer generation
├── main.py # End-to-end execution
└── README.md

**Setup Instructions**:-
1.Install dependencies:-
    pip install -r requirements.txt
2.Create a .env file
    API_KEY=google api key( I have sed google gemini for embedding as well as answer generation)
3.Run the system:-
    python main.py

**User Manual**

How to use the system
    1.Open main.py
    2.Replace the query text with your case context or legal question
    3.Run the script

**What the system does**

    Matches your query to relevant Supreme Court reasoning

    Identifies the governing doctrinal phase

    Surfaces relevant past cases

    Generates a grounded legal explanation

**Example Query**:-
    1.  I am a junior lawyer working on a case where a state government has been
        collecting mobile location data of citizens during protests through
        executive orders, without passing any legislation. The government is
        justifying this on grounds of national security.
        Based on current Supreme Court jurisprudence, is such surveillance
        constitutionally valid, and which judgments should I rely on?
        
    2.  I am assisting in a case where a government agency has been collecting call detail       records (CDRs) and metadata from telecom providers without informing the individuals concerned. The collection is being carried out through internal executive directions, without any publicly disclosed law or oversight mechanism. Does the right to privacy extend to metadata and telecom records, and which Supreme Court decisions support challenging such surveillance?

    3. A central government program involves large-scale digital surveillance of citizens’ online activities for national security purposes. The program operates without individual suspicion and lacks clear legislative safeguards. Based on current Supreme Court jurisprudence, can such mass surveillance be justified, and what constitutional standards apply when evaluating its legality?
    
    **Out of Scope query** 
 4.Does Article 14 allow classification based on economic criteria in government welfare schemes?

