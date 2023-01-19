#https://ethereum.org/pt/developers/docs/programming-languages/python/
# from brownie import AcademicToken, accounts

# def deploy_token():
#     my_token = AcademicToken.deploy({"from":accounts[0]})
#     return my_token
# def main():
#     deploy_token()

# main()
import streamlit as st
#from brownie import AcademicToken, accounts
from utils.abstract_terminal import emitir_pgto, cadastrar_disciplina, emitir_certificado, inscrever_aluno, lancar_nota


st.title("Academic Dapp")

aba_aluno, aba_professor, aba_certificados  = st.tabs(["Aluno", "Professor", "Certificados"])

with aba_aluno:
    st.header("Aluno")
    #Set student
    st.subheader("Nome")
    name = st.text_input("Digite o nome do aluno")
    #Set course
    st.subheader("Curso")
    course = st.selectbox("Selecione o curso do aluno", 
                           ["Ciência da Computação",
                            "Engenharia de Software",
                            "Engenharia de Computação",
                            "Engenharia de Produção"])
    send_course = st.button("Cadastrar curso")
    #st.write(send_course)
#    inserirDisciplina( course, nome, professor, idProfessor)

    if send_course:
        if name:
            aluno_contract = cadastrar_disciplina(name, course)#inscrever_aluno(name, course)
            st.write(f"Curso cadastrado com sucesso -> {course}")

        else:
            st.write("Por favor, digite o nome do aluno")
    send_course=False

    #Set grade
    st.subheader("Nota do aluno")
    #inserirNota(name, course, grade)
    grade = st.slider('Digite a nota que deseja dar ao aluno (0 a 100)',
                    0,
                    100)

    send_grade = st.button("Cadastrar nota")

    if send_grade:
        if name:
            if course:
                nota = lancar_nota(name, course, grade)
                st.write(f"Nota cadastrada com sucesso! {course}: {grade}")
            else:
                st.write("Por favor, selecione o curso do aluno")
        else:
            st.write("Por favor, digite o nome do aluno")
    
    send_grade=False


with aba_professor:
   st.header("Professor")

   
with aba_certificados:
    st.header("Certificados")

    st.subheader("Aluno")
    name_cert = st.text_input("Digite o nome do aluno para o certificado/pagamento")

    st.subheader("Pagamento de disciplina curso")
    certificado_pagamento = st.button("Emitir pgto.")

    if certificado_pagamento:
        if name_cert:
            pgto_token = emitir_pgto()
            st.write(f"Certificado de conclusão emitido com sucesso!")
            st.write(f"TOKEN -> {pgto_token}")

        else:
            st.write("Por favor, digite o nome do aluno")

    st.subheader("Certificado de conclusão de curso")
    certificado_conclusao = st.button("Emitir cert.")

    if certificado_conclusao:
        if name_cert:
            cert_token = emitir_certificado()
            st.write(f"Certificado de conclusão emitido com sucesso!")
            st.write(f"TOKEN -> {cert_token}")
        else:
            st.write("Por favor, digite o nome do aluno")
