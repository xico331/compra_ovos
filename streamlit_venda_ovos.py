# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 22:36:09 2026

@author: Francisco
"""

import streamlit as st
import requests
from datetime import datetime

# --- CONFIGURAÇÃO DO FIREBASE ---
# Substitui pelo teu link exato, não te esqueças de remover a barra (/) no final!
FIREBASE_URL = "https://ovos-50d79-default-rtdb.europe-west1.firebasedatabase.app"

st.set_page_config(page_title="Encomenda de Ovos", page_icon="🥚")

st.title("🥚 Ovos Frescos da Quinta")
st.write("Faça aqui a sua encomenda! Os ovos serão entregues com a máxima frescura.")

# --- FORMULÁRIO DO CLIENTE ---
with st.form("form_encomenda"):
    st.subheader("Os seus dados")
    nome = st.text_input("O seu Nome")
    morada = st.text_input("Morada / Local de Entrega")
    telefone = st.text_input("Telemóvel (Opcional)")
    
    st.subheader("O seu pedido")
    duzias = st.number_input("Quantas dúzias deseja?", min_value=1, step=1)
    
    # Botão de envio
    submit = st.form_submit_button("Enviar Encomenda", type="primary")

# --- LÓGICA DE ENVIO ---
if submit:
    if nome and morada:
        # Prepara os dados do cliente num "pacote"
        dados_encomenda = {
            "nome": nome,
            "morada": morada,
            "telefone": telefone,
            "duzias": duzias,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "estado": "Pendente" # A tua app de gestão vai procurar as pendentes
        }
        
        try:
            # O .json no final do link é obrigatório para o Firebase entender!
            url_envio = f"{FIREBASE_URL}/encomendas.json"
            
            # Envia o pacote para o Firebase
            resposta = requests.post(url_envio, json=dados_encomenda)
            
            if resposta.status_code == 200:
                st.success(f"✅ Muito obrigado, {nome}! A sua encomenda de {duzias} dúzia(s) foi recebida com sucesso.")
                st.balloons()
            else:
                st.error("❌ Ocorreu um erro no servidor. Tente novamente mais tarde.")
                
        except Exception as e:
            st.error(f"Erro de ligação à base de dados: {e}")
    else:
        st.warning("⚠️ Por favor, preencha o seu nome e morada para sabermos onde entregar!")