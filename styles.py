def load_css():
    return """
    <style>

    .main{
        background-color:#0E1117;
    }

    h1,h2,h3,h4,h5{
        color:white;
    }

    div[data-testid="metric-container"]{
        background:#1f2937;
        border-radius:15px;
        padding:18px;
        border:1px solid #374151;
        box-shadow:0px 0px 12px rgba(0,255,255,0.2);
    }

    div[data-testid="metric-container"] label{
        color:#d1d5db;
    }

    div[data-testid="metric-container"] div{
        color:white;
    }

    .stButton>button{
        width:100%;
        background:#00B4D8;
        color:white;
        border-radius:10px;
        height:50px;
        font-size:18px;
        border:none;
    }

    .stButton>button:hover{
        background:#0096C7;
    }

    </style>
    """