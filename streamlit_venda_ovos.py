# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 22:36:09 2026

@author: Francisco
""
import streamlit as st
import requests
from datetime import datetime

# --- CONFIGURAÇÃO DO FIREBASE ---
# Substitui pelo teu link exato! (Sem barra no final)
FIREBASE_URL = "https://ovos-50d79-default-rtdb.europe-west1.firebasedatabase.app/"

st.set_page_config(page_title="Encomenda de Ovos", page_icon="🥚")

st.title("🥚 Encomenda de Ovos Frescos")

# --- FORMULÁRIO DO CLIENTE (SIMPLIFICADO E COM MEIAS DÚZIAS) ---
with st.form("form_encomenda"):
    nome = st.text_input("O seu Nome")
    # Alterado para aceitar decimais (min_value=0.5, step=0.5, valor inicial=1.0)
    duzias = st.number_input("Quantas dúzias deseja? (Ex: 0.5 para meia dúzia)", min_value=0.5, step=0.5, value=1.0)
    
    # Botão de envio
    submit = st.form_submit_button("Enviar Encomenda", type="primary")

# --- LÓGICA DE ENVIO ---
if submit:
    if nome:
        # Prepara os dados
        dados_encomenda = {
            "nome": nome,
            "duzias": duzias,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "estado": "Pendente"
        }
        
        try:
            url_envio = f"{FIREBASE_URL}/encomendas.json"
            resposta = requests.post(url_envio, json=dados_encomenda)
            
            if resposta.status_code == 200:
                st.success(f"✅ Obrigado, {nome}! A sua encomenda de {duzias} dúzia(s) foi registada.")
                st.balloons()
            else:
                st.error("❌ Erro de ligação. Tente novamente.")
                
        except Exception as e:
            st.error("Erro no sistema.")
    else:
        st.warning("⚠️ Por favor, preenche o teu nome para sabermos de quem é a encomenda!")
