# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 22:36:09 2026

@author: Francisco
"""

import streamlit as st
import requests
from datetime import datetime

# --- CONFIGURAÇÃO DO FIREBASE ---
# Substitui pelo teu link exato! (Sem barra no final)
FIREBASE_URL = "https://AQUI_FICA_O_TEU_LINK.firebasedatabase.app"

st.set_page_config(page_title="Encomenda de Ovos", page_icon="🥚")

st.title("🥚 Encomenda de Ovos Frescos")

# --- FORMULÁRIO DO CLIENTE (SIMPLIFICADO) ---
with st.form("form_encomenda"):
    nome = st.text_input("O seu Nome")
    duzias = st.number_input("Quantas dúzias deseja?", min_value=1, step=1)
    
    # Botão de envio
    submit = st.form_submit_button("Enviar Encomenda", type="primary")

# --- LÓGICA DE ENVIO ---
if submit:
    if nome:
        # Prepara os dados só com o que pediste
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
                st.success(f"✅ Obrigado, {nome}! A tua encomenda de {duzias} dúzia(s) foi registada.")
                st.balloons()
            else:
                st.error("❌ Erro de ligação. Tenta novamente.")
                
        except Exception as e:
            st.error("Erro no sistema.")
    else:
        st.warning("⚠️ Por favor, preenche o teu nome para sabermos de quem é a encomenda!")
