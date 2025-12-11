"""
Kaggle Knowledge Base Dashboard
Dashboard Streamlit per visualizzare le risorse Kaggle del team AI.
"""

import streamlit as st
import pandas as pd
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Kaggle Knowledge Base",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #20BEFF;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #666;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .prize-high {
        background-color: #ffd700;
        color: black;
        padding: 0.2rem 0.5rem;
        border-radius: 5px;
        font-weight: bold;
    }
    .prize-mid {
        background-color: #c0c0c0;
        color: black;
        padding: 0.2rem 0.5rem;
        border-radius: 5px;
    }
    .level-beginner {
        background-color: #90EE90;
        color: black;
        padding: 0.2rem 0.5rem;
        border-radius: 5px;
    }
    .level-intermediate {
        background-color: #FFD700;
        color: black;
        padding: 0.2rem 0.5rem;
        border-radius: 5px;
    }
    .level-advanced {
        background-color: #FF6B6B;
        color: white;
        padding: 0.2rem 0.5rem;
        border-radius: 5px;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding-left: 20px;
        padding-right: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.image("https://www.kaggle.com/static/images/site-logo.png", width=150)
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "📍 Navigazione",
    ["🏠 Home", "🏆 Competizioni", "📚 Corsi", "🤖 Modelli", "⚡ Risorse Compute", "📖 API Reference", "👤 Profilo"]
)

# ==================== HOME PAGE ====================
if page == "🏠 Home":
    st.markdown('<p class="main-header">🏆 Kaggle Knowledge Base</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Dashboard per il Team AI Data Scientists - Account: fcwebdev</p>', unsafe_allow_html=True)

    # Quick Stats
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(label="🏆 Competizioni", value="2", delta="+1 Gemini 3")
    with col2:
        st.metric(label="📊 Dataset", value="3", delta="Pubblicati")
    with col3:
        st.metric(label="📓 Notebook", value="1", delta="Attivi")
    with col4:
        st.metric(label="👥 Following", value="3", delta="Grandmasters")

    st.markdown("---")

    # Mission
    st.subheader("🎯 Mission del Team")
    st.info("""
    **Obiettivo**: Creare un team di agenti AI che:
    - 🥇 Partecipa a competizioni Kaggle
    - 📈 Raggiunge posizioni top nelle leaderboard
    - 🌟 Costruisce visibilità nel panorama data science
    - 💼 Attrae opportunità professionali
    """)

    # Quick Links
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🚀 Quick Start")
        st.markdown("""
        1. **Leggi i dati** - Comprendi il problema
        2. **EDA veloce** - Identifica pattern
        3. **Baseline** - Submit rapidamente
        4. **Itera** - Migliora incrementalmente
        5. **Ensemble** - Combina modelli
        """)

    with col2:
        st.subheader("⚠️ Red Flags da Evitare")
        st.error("""
        - Overfitting (CV >> LB)
        - Data leakage
        - Target leakage
        - Submission format errato
        """)

    # Workflow
    st.markdown("---")
    st.subheader("📋 Workflow Vincente")

    workflow_cols = st.columns(5)
    steps = [
        ("1️⃣", "EDA", "CPU Only", "Pandas, Matplotlib, Seaborn"),
        ("2️⃣", "Features", "CPU", "Preprocessing, Encoding"),
        ("3️⃣", "Baseline", "CPU/GPU", "sklearn, XGBoost"),
        ("4️⃣", "Training", "GPU/TPU", "TensorFlow, PyTorch"),
        ("5️⃣", "Ensemble", "CPU", "Combine & Submit"),
    ]

    for col, (num, title, resource, desc) in zip(workflow_cols, steps):
        with col:
            st.markdown(f"### {num} {title}")
            st.caption(f"**{resource}**")
            st.write(desc)

# ==================== COMPETITIONS PAGE ====================
elif page == "🏆 Competizioni":
    st.markdown('<p class="main-header">🏆 Competizioni Attive</p>', unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["💰 Top Prize", "🎯 Per Iniziare", "🎮 Playground", "👥 Community"])

    with tab1:
        st.subheader("Competizioni con Premi Alti")

        top_competitions = pd.DataFrame({
            "Competizione": [
                "AI Mathematical Olympiad - Progress Prize 3",
                "Google DeepMind - Vibe Code with Gemini 3",
                "Hull Tactical - Market Prediction",
                "Vesuvius Challenge - Surface Detection",
                "Google Tunix Hack",
                "MITSUI&CO. Commodity Prediction",
                "CSIRO - Image2Biomass Prediction",
                "Santa 2025 - Christmas Tree Packing"
            ],
            "Premio": ["$2.2M", "$500k", "$100k", "$100k", "$100k", "$100k", "$75k", "$50k"],
            "Tipo": ["Code", "Hackathon", "Code", "Research", "Hackathon", "Code", "Research", "Featured"],
            "Teams": [671, 1471, 3430, 318, 80, 1711, 1888, 1581],
            "Scadenza": ["4 mesi", "12 Dic 2025", "5 giorni", "2 mesi", "1 mese", "1 mese", "2 mesi", "2 mesi"]
        })

        st.dataframe(
            top_competitions,
            column_config={
                "Competizione": st.column_config.TextColumn("Competizione", width="large"),
                "Premio": st.column_config.TextColumn("Premio 💰"),
                "Tipo": st.column_config.TextColumn("Tipo"),
                "Teams": st.column_config.NumberColumn("Teams", format="%d"),
                "Scadenza": st.column_config.TextColumn("Scadenza ⏰")
            },
            hide_index=True,
            use_container_width=True
        )

        # Gemini 3 Competition Stats (Live)
        st.markdown("---")
        st.subheader("🔥 Gemini 3 Hackathon - Stats Live")
        gem_col1, gem_col2, gem_col3, gem_col4 = st.columns(4)
        gem_col1.metric("Entrants", "17,291")
        gem_col2.metric("Participants", "1,594")
        gem_col3.metric("Teams", "1,471")
        gem_col4.metric("Submissions", "1,471")
        st.warning("⏰ **Deadline: 12 Dicembre 2025 - 23:59 UTC** (domani!)")

        # Submission Tracker
        st.markdown("---")
        st.subheader("📋 La Mia Submission - WorkflowLM")

        submission_status = {
            "Task": [
                "App funzionante",
                "Pubblicata su AI Studio (link pubblico)",
                "Video demo (max 2 min)",
                "Writeup su Kaggle (max 250 parole)",
                "Submit finale"
            ],
            "Status": ["✅ Completato", "⏳ Da fare", "⏳ Da fare", "⏳ Da fare", "⏳ Da fare"],
            "Note": [
                "WorkflowLM - AI Workflow Designer",
                "Clicca Share > Publish your app",
                "YouTube/Loom/X - pubblico",
                "What, How, Why + impact",
                "Entro 12 Dic 23:59 UTC"
            ]
        }

        st.dataframe(
            pd.DataFrame(submission_status),
            hide_index=True,
            use_container_width=True
        )

        st.info("""
        **Criteri di valutazione:**
        - 🎯 Impact: 40%
        - 🔧 Technical Depth: 30%
        - 💡 Creativity: 20%
        - 🎬 Presentation: 10%
        """)

    with tab2:
        st.subheader("🎯 Competizioni per Principianti")

        beginner_competitions = pd.DataFrame({
            "Competizione": [
                "Titanic - Machine Learning from Disaster",
                "House Prices - Advanced Regression",
                "Spaceship Titanic",
                "LLM Classification Finetuning"
            ],
            "Difficoltà": ["⭐ Facile", "⭐ Facile", "⭐⭐ Media", "⭐⭐ Media"],
            "Focus": ["ML basics, Classification", "Feature engineering, Regression", "Classification avanzata", "LLM Fine-tuning"],
            "Teams": [16638, 6063, 2589, 305]
        })

        st.dataframe(
            beginner_competitions,
            column_config={
                "Competizione": st.column_config.TextColumn("Competizione", width="large"),
                "Difficoltà": st.column_config.TextColumn("Difficoltà"),
                "Focus": st.column_config.TextColumn("Focus"),
                "Teams": st.column_config.NumberColumn("Teams", format="%d")
            },
            hide_index=True,
            use_container_width=True
        )

        st.success("💡 **Consiglio**: Hai già un progetto Titanic su Streamlit! Perfetto per migliorare il tuo score.")

    with tab3:
        st.subheader("🎮 Playground Series")
        st.info("**Diabetes Prediction Challenge (S5E12)** - 1,522 teams - Scadenza: 21 giorni")
        st.caption("Premi: Swag Kaggle")

    with tab4:
        st.subheader("👥 Community Competitions")

        community = pd.DataFrame({
            "Competizione": [
                "AIRR-ML-25: Adaptive Immune Profiling",
                "Ultimate AI & Tech Challenge",
                "Rental Product Recommendation System",
                "Brain-to-text '25",
                "Mercor Cheating Detection"
            ],
            "Premio": ["$10,000", "$10,000", "$10,000", "$9,000", "$5,000"],
            "Teams": [210, 37, 32, 317, 83]
        })

        st.dataframe(community, hide_index=True, use_container_width=True)

# ==================== COURSES PAGE ====================
elif page == "📚 Corsi":
    st.markdown('<p class="main-header">📚 Kaggle Learn - Corsi Gratuiti</p>', unsafe_allow_html=True)
    st.caption("Tutti i corsi offrono certificati gratuiti al completamento")

    tab1, tab2, tab3, tab4 = st.tabs(["🐍 Fondamentali", "🤖 Machine Learning", "📊 Data Analysis", "🗄️ SQL"])

    with tab1:
        st.subheader("Corsi Fondamentali")

        courses = [
            {"nome": "Intro to Programming", "desc": "Inizia con Python, se non hai esperienza di coding", "livello": "🟢 Principiante", "url": "https://www.kaggle.com/learn/intro-to-programming"},
            {"nome": "Python", "desc": "Impara il linguaggio più importante per la data science", "livello": "🟢 Principiante", "url": "https://www.kaggle.com/learn/python"},
            {"nome": "Pandas", "desc": "Perfeziona le tue skills di data manipulation", "livello": "🟢 Principiante", "url": "https://www.kaggle.com/learn/pandas"},
        ]

        for course in courses:
            with st.expander(f"{course['livello']} **{course['nome']}**"):
                st.write(course['desc'])
                st.link_button("Vai al corso →", course['url'])

    with tab2:
        st.subheader("Machine Learning & Deep Learning")

        ml_courses = [
            {"nome": "Intro to Machine Learning", "desc": "Concetti core del ML e primi modelli", "livello": "🟢 Principiante"},
            {"nome": "Intermediate Machine Learning", "desc": "Missing values, non-numeric values, data leakage", "livello": "🟡 Intermedio"},
            {"nome": "Feature Engineering", "desc": "Crea features migliori per modelli migliori", "livello": "🟡 Intermedio"},
            {"nome": "Machine Learning Explainability", "desc": "Estrai insights comprensibili da qualsiasi modello", "livello": "🟡 Intermedio"},
            {"nome": "Intro to Deep Learning", "desc": "TensorFlow e Keras per neural networks", "livello": "🟡 Intermedio"},
            {"nome": "Computer Vision", "desc": "Reti neurali convoluzionali", "livello": "🔴 Avanzato"},
        ]

        for course in ml_courses:
            st.markdown(f"{course['livello']} **{course['nome']}** - {course['desc']}")

    with tab3:
        st.subheader("Data Analysis & Visualization")

        data_courses = [
            {"nome": "Data Visualization", "desc": "Crea visualizzazioni eccellenti", "livello": "🟢 Principiante"},
            {"nome": "Data Cleaning", "desc": "Workflow per pulire dati reali", "livello": "🟡 Intermedio"},
            {"nome": "Geospatial Analysis", "desc": "Mappe interattive e dati geospaziali", "livello": "🟡 Intermedio"},
            {"nome": "Time Series", "desc": "ML per task di forecasting", "livello": "🟡 Intermedio"},
        ]

        for course in data_courses:
            st.markdown(f"{course['livello']} **{course['nome']}** - {course['desc']}")

    with tab4:
        st.subheader("SQL & Database")

        sql_courses = [
            {"nome": "Intro to SQL", "desc": "SQL con Google BigQuery", "livello": "🟢 Principiante"},
            {"nome": "Advanced SQL", "desc": "Porta le tue skills SQL al livello successivo", "livello": "🟡 Intermedio"},
        ]

        for course in sql_courses:
            st.markdown(f"{course['livello']} **{course['nome']}** - {course['desc']}")

    # Learning Path
    st.markdown("---")
    st.subheader("📍 Percorso Consigliato per fcWebDev")

    path_col1, path_col2 = st.columns(2)

    with path_col1:
        st.markdown("""
        **Fase 1: Fondamenta**
        1. Python
        2. Pandas
        3. Intro to SQL

        **Fase 2: Data Analysis**
        4. Data Visualization
        5. Data Cleaning
        6. Advanced SQL
        """)

    with path_col2:
        st.markdown("""
        **Fase 3: Machine Learning**
        7. Intro to Machine Learning
        8. Intermediate ML
        9. Feature Engineering

        **Fase 4: Specializzazione**
        10. Time Series
        11. ML Explainability
        """)

# ==================== MODELS PAGE ====================
elif page == "🤖 Modelli":
    st.markdown('<p class="main-header">🤖 Modelli Pre-Trainati</p>', unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["🔥 Trending", "📋 Per Task", "💻 Come Usare"])

    with tab1:
        st.subheader("Modelli più Utilizzati")

        trending = pd.DataFrame({
            "Modello": [
                "sentence-transformers/all-MiniLM-L6-v2",
                "google-bert/bert-base-uncased",
                "Google Gemma",
                "openai-community/gpt2",
                "distilbert/distilbert-base-uncased"
            ],
            "Uso": [
                "Sentence embeddings",
                "NLP tasks",
                "LLM lightweight",
                "Text generation",
                "NLP leggero"
            ],
            "Notebooks": [1067, 939, 383, 342, 341]
        })

        st.dataframe(trending, hide_index=True, use_container_width=True)

    with tab2:
        st.subheader("Modelli per Task")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🖼️ Computer Vision")
            st.markdown("""
            - **YOLOV8/YOLO11** - Object Detection
            - **MobileNet V2** - Classification leggera
            - **EfficientNet** - Classification SOTA
            - **MoveNet** - Pose Detection
            """)

            st.markdown("### 🔊 Audio")
            st.markdown("""
            - **YAMNet** - Audio classification
            - **Perch** - Bird vocalization
            - **Trillsson** - Speech embeddings
            """)

        with col2:
            st.markdown("### 📝 NLP")
            st.markdown("""
            - **BERT** - NLP tasks generali
            - **DistilBERT** - BERT leggero
            - **Gemma** - LLM Google
            - **all-MiniLM-L6-v2** - Embeddings veloci
            """)

            st.markdown("### 🎯 Consigliati per Competizioni")
            st.markdown("""
            - **Gemma** - Task di testo
            - **EfficientNet** - Immagini
            - **XGBoost/LightGBM** - Tabular data
            """)

    with tab3:
        st.subheader("Come Usare i Modelli")

        st.code("""
import kagglehub

# Scarica un modello
path = kagglehub.model_download("google/gemma/keras/gemma_2b_en")

# Usa il modello
from transformers import AutoModelForCausalLM
model = AutoModelForCausalLM.from_pretrained(path)
        """, language="python")

        st.info("💡 In un notebook Kaggle, puoi anche aggiungere modelli direttamente dall'UI: vai alla pagina del modello e clicca 'Add to Notebook'")

# ==================== COMPUTE RESOURCES PAGE ====================
elif page == "⚡ Risorse Compute":
    st.markdown('<p class="main-header">⚡ Risorse Compute</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🎮 GPU - Tesla P100")

        st.metric("Quota Settimanale", "30 ore")
        st.metric("VRAM", "16 GB")
        st.metric("CUDA Cores", "3584")

        st.markdown("---")
        st.markdown("**✅ Best For:**")
        st.success("Deep Learning, CNN, Transformers, PyTorch, TensorFlow")

        st.markdown("**❌ NON usare per:**")
        st.error("Pandas, scikit-learn, EDA, preprocessing")

        st.markdown("---")
        st.markdown("**💡 Tips:**")
        st.warning("""
        - Ferma sessioni prima di chiudere (risparmia fino a 60 min!)
        - Usa `kaggle kernels push` per evitare sessioni interattive
        - Non usare Commit solo per salvare - scarica il .ipynb
        """)

    with col2:
        st.subheader("🚀 TPU - v3-8")

        st.metric("Quota Settimanale", "20 ore")
        st.metric("Max Sessione", "9 ore")
        st.metric("RAM", "128 GB")

        st.markdown("---")
        st.markdown("**✅ Best For:**")
        st.success("Large batch training, TensorFlow, Image models")

        st.markdown("**⚠️ Requisiti:**")
        st.warning("""
        - Dati su GCS in TFRecords
        - Batch size: 128 × 8 = 1024
        - Learning rate scalato con batch size
        """)

        st.markdown("---")
        st.markdown("**💡 Setup Base:**")
        st.code("""
tpu = tf.distribute.cluster_resolver.TPUClusterResolver()
tf.tpu.experimental.initialize_tpu_system(tpu)
tpu_strategy = tf.distribute.TPUStrategy(tpu)

with tpu_strategy.scope():
    model = create_model()
        """, language="python")

    # Comparison Table
    st.markdown("---")
    st.subheader("📊 Quando Usare Cosa")

    comparison = pd.DataFrame({
        "Task": ["Training Neural Networks", "Image Classification", "NLP con Transformers",
                 "Data Preprocessing", "EDA/Visualizzazioni", "sklearn models", "XGBoost/LightGBM",
                 "Large batch training", "Debugging"],
        "GPU": ["✅", "✅", "✅", "❌", "❌", "❌", "⚠️", "⚠️", "✅"],
        "TPU": ["✅", "✅", "✅", "❌", "❌", "❌", "❌", "✅", "❌"],
        "CPU": ["❌", "❌", "❌", "✅", "✅", "✅", "✅", "❌", "✅"]
    })

    st.dataframe(comparison, hide_index=True, use_container_width=True)

# ==================== API PAGE ====================
elif page == "📖 API Reference":
    st.markdown('<p class="main-header">📖 Kaggle API Reference</p>', unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["🔧 Setup", "🏆 Competitions", "📊 Datasets", "📓 Notebooks"])

    with tab1:
        st.subheader("Setup e Autenticazione")

        st.code("pip install kaggle kagglehub", language="bash")

        st.markdown("**Credenziali:**")
        st.markdown("""
        1. Vai su [Account Settings](https://www.kaggle.com/settings/account)
        2. Clicca "Create New Token"
        3. Scarica `kaggle.json`
        4. Posiziona in:
           - **Linux/Mac**: `~/.kaggle/kaggle.json`
           - **Windows**: `C:\\Users\\<username>\\.kaggle\\kaggle.json`
        """)

    with tab2:
        st.subheader("Comandi Competizioni")

        commands = {
            "Lista competizioni": "kaggle competitions list",
            "Scarica dati": "kaggle competitions download -c [COMPETITION]",
            "Invia submission": "kaggle competitions submit -c [COMPETITION] -f [FILE] -m [MESSAGE]",
            "Lista submissions": "kaggle competitions submissions -c [COMPETITION]"
        }

        for desc, cmd in commands.items():
            st.markdown(f"**{desc}:**")
            st.code(cmd, language="bash")

    with tab3:
        st.subheader("Comandi Dataset")

        commands = {
            "Cerca dataset": "kaggle datasets list -s [KEYWORD]",
            "Scarica dataset": "kaggle datasets download -d [DATASET]",
            "Crea nuovo dataset": "kaggle datasets create -p /path/to/dataset",
            "Nuova versione": "kaggle datasets version -p /path/to/dataset -m 'message'"
        }

        for desc, cmd in commands.items():
            st.markdown(f"**{desc}:**")
            st.code(cmd, language="bash")

    with tab4:
        st.subheader("Comandi Notebook")

        commands = {
            "Cerca notebook": "kaggle kernels list -s [KEYWORD]",
            "Push notebook": "kaggle kernels push -p /path/to/folder",
            "Scarica notebook": "kaggle kernels pull [KERNEL] -p /path -m"
        }

        for desc, cmd in commands.items():
            st.markdown(f"**{desc}:**")
            st.code(cmd, language="bash")

        st.info("💡 Usare `kaggle kernels push` permette di eseguire notebook senza sessione interattiva, risparmiando quota!")

# ==================== PROFILE PAGE ====================
elif page == "👤 Profilo":
    st.markdown('<p class="main-header">👤 Profilo Kaggle</p>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mp&s=200", width=150)
        st.markdown("### fcWebDev")
        st.caption("Rome, Lazio, Italy")
        st.caption("Junior Data Analyst")

    with col2:
        st.markdown("### Bio")
        st.info("""
        Aspiring Data Analyst with a deep curiosity for uncovering insights from data.
        Currently working as a Frontend Developer, bringing a blend of analytical thinking
        and creative problem-solving to projects. Passionate about learning and exploring
        the intersection between data visualization and user interfaces.
        """)

        # Stats
        st.markdown("### Statistiche")
        stat_cols = st.columns(4)
        stats = [("Competizioni", "2"), ("Dataset", "3"), ("Notebooks", "1"), ("Discussions", "3")]

        for col, (label, value) in zip(stat_cols, stats):
            col.metric(label, value)

    st.markdown("---")

    # Following
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🌟 Following Strategici")
        st.markdown("""
        - **Chris Deotte** - Kaggle Grandmaster (notebook eccellenti)
        - **Alexis Cook** - Kaggle Staff
        """)

    with col2:
        st.subheader("📊 Dataset Pubblicati")
        st.markdown("""
        - **Synthetic Cybersecurity Logs for Anomaly Detection**
          - Tipo: Dataset tabellare
          - Upvotes: 1
        """)

    st.markdown("---")

    # Links
    st.subheader("🔗 Link Esterni")
    link_cols = st.columns(3)

    with link_cols[0]:
        st.link_button("🐙 GitHub", "https://github.com/fracabu")
    with link_cols[1]:
        st.link_button("💼 LinkedIn", "https://www.linkedin.com/in/francesco-~-capurso-5801031a9/")
    with link_cols[2]:
        st.link_button("🚀 Portfolio", "https://titanic-ml-kaggle.streamlit.app/")

    # Skills
    st.markdown("---")
    st.subheader("🛠️ Skills in Sviluppo")

    skills = ["Python", "SQL", "Data Analysis", "Data Visualization", "Tableau", "Power BI", "Machine Learning"]
    skill_cols = st.columns(len(skills))

    for col, skill in zip(skill_cols, skills):
        col.markdown(f"<div style='background: #f0f2f6; padding: 10px; border-radius: 10px; text-align: center;'>{skill}</div>", unsafe_allow_html=True)

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("📅 Ultimo aggiornamento: Dicembre 2025")
st.sidebar.caption("🤖 Team AI Data Scientists")
