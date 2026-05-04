import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Arbi Finance AI", layout="wide")

# ------------------------
# CSS custom (visual premium)
# ------------------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.metric-card {
    background: #161b22;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.3);
}
.section {
    background: #161b22;
    padding: 25px;
    border-radius: 12px;
    margin-top: 20px;
}
h1, h2, h3 {
    color: #ffffff;
}
</style>
""", unsafe_allow_html=True)

# ------------------------
# Dados fictícios
# ------------------------
np.random.seed(42)

meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]

data = pd.DataFrame({
    "Mes": meses,
    "Receita": np.random.randint(20000, 50000, 6),
    "Despesa": np.random.randint(15000, 40000, 6)
})

data["Saldo"] = data["Receita"] - data["Despesa"]
data["Saldo Acumulado"] = data["Saldo"].cumsum()

categorias = pd.DataFrame({
    "Categoria": ["Marketing", "Tecnologia", "Pessoas", "Operacional"],
    "Valor": [12430, 9800, 22000, 7600]
})

# ------------------------
# HEADER
# ------------------------
st.title("🚀 Arbi Finance AI")
st.caption("Inteligência financeira para tomada de decisão")

# ------------------------
# KPIs PREMIUM
# ------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <h3>Receita</h3>
        <h2>R$ {data['Receita'].iloc[-1]:,.0f}</h2>
        <p>Último mês</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <h3>Despesa</h3>
        <h2>R$ {data['Despesa'].iloc[-1]:,.0f}</h2>
        <p>Último mês</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <h3>Saldo</h3>
        <h2>R$ {data['Saldo'].iloc[-1]:,.0f}</h2>
        <p>Resultado</p>
    </div>
    """, unsafe_allow_html=True)

# ------------------------
# GRÁFICOS
# ------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("📈 Receita vs Despesa")
st.line_chart(data.set_index("Mes")[["Receita", "Despesa"]])
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("💰 Evolução de Caixa")
st.line_chart(data.set_index("Mes")["Saldo Acumulado"])
st.markdown('</div>', unsafe_allow_html=True)

# ------------------------
# CATEGORIAS
# ------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("📊 Despesas por Categoria")
st.bar_chart(categorias.set_index("Categoria"))
st.markdown('</div>', unsafe_allow_html=True)

# ------------------------
# INSIGHTS (mais fortes)
# ------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("🤖 Insights Inteligentes")

st.success("📌 Seu gasto com 'Pessoas' representa 42% das despesas — principal alavanca de custo.")
st.warning("📌 Marketing caiu 18% no último mês — possível impacto em aquisição.")
st.info("📌 Runway estimado: 6 meses mantendo o burn atual.")

st.markdown('</div>', unsafe_allow_html=True)

# ------------------------
# CFO CHAT (premium feel)
# ------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("💬 CFO Inteligente")

pergunta = st.text_input("Faça uma pergunta sobre o financeiro:")

if pergunta:
    st.markdown(f"""
    <div class="metric-card">
        <b>Pergunta:</b> {pergunta}<br><br>
        <b>Resposta:</b> Você gastou R$ 12.430 em marketing no último mês, representando 18% das despesas totais.
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
