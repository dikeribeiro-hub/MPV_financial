import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Finance AI", layout="wide")

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
# Header
# ------------------------
st.title("📊 Arbi Finance AI")
st.caption("Painel inteligente de gestão financeira")

# ------------------------
# KPIs
# ------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Receita (último mês)", f"R$ {data['Receita'].iloc[-1]:,.0f}")
col2.metric("Despesa (último mês)", f"R$ {data['Despesa'].iloc[-1]:,.0f}")
col3.metric("Saldo", f"R$ {data['Saldo'].iloc[-1]:,.0f}")

# ------------------------
# Gráfico Receita x Despesa
# ------------------------
st.subheader("📈 Receita vs Despesa")
st.line_chart(data.set_index("Mes")[["Receita", "Despesa"]])

# ------------------------
# Saldo acumulado
# ------------------------
st.subheader("💰 Evolução de Caixa")
st.line_chart(data.set_index("Mes")["Saldo Acumulado"])

# ------------------------
# Categorias
# ------------------------
st.subheader("📊 Despesas por Categoria")
st.bar_chart(categorias.set_index("Categoria"))

# ------------------------
# Insights automáticos
# ------------------------
st.subheader("🤖 Insights automáticos")

st.info("📌 Seu gasto com 'Pessoas' representa mais de 40% das despesas totais.")
st.info("📌 Marketing caiu 18% no último mês — pode impactar aquisição de clientes.")
st.info("📌 Seu burn rate atual indica 6 meses de runway.")

# ------------------------
# CFO Chat (fake)
# ------------------------
st.subheader("💬 Pergunte ao CFO")

pergunta = st.text_input("Faça uma pergunta:")

if pergunta:
    st.success(
        "Você gastou R$ 12.430 em marketing no último mês, representando 18% das despesas."
    )
