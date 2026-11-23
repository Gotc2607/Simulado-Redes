#!/usr/bin/env python3
"""
Simulado Interativo de Redes de Computadores (Capítulos 7 e 8)
Kurose & Ross - Redes de Computadores e a Internet (6ª edição)
"""

import json
import os
import sys
import time
from pathlib import Path

# Cores ANSI para o terminal
class Cores:
    RESET = "\033[0m"
    NEGRITO = "\033[1m"
    VERDE = "\033[92m"
    VERMELHO = "\033[91m"
    AMARELO = "\033[93m"
    AZUL = "\033[94m"
    CIANO = "\033[96m"
    CINZA = "\033[90m"
    MAGENTA = "\033[95m"

def carregar_questoes():
    caminho = Path(__file__).parent / "questoes.json"
    if not caminho.exists():
        print(f"{Cores.VERMELHO}Erro: arquivo questoes.json não encontrado!{Cores.RESET}")
        sys.exit(1)
    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)
    return dados["simulado"]

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def exibir_cabecalho(titulo, referencia):
    print(f"{Cores.CIANO}{'=' * 75}{Cores.RESET}")
    print(f"{Cores.NEGRITO}{Cores.AZUL}🎓 {titulo}{Cores.RESET}")
    print(f"{Cores.CINZA}📚 {referencia}{Cores.RESET}")
    print(f"{Cores.CIANO}{'=' * 75}{Cores.RESET}\n")

def menu_principal():
    print(f"{Cores.NEGRITO}Escolha o modo de estudo:{Cores.RESET}\n")
    print(f"  {Cores.VERDE}[1]{Cores.RESET} Modo Prática (Feedback imediato e opção de ver Teoria/Cálculo)")
    print(f"  {Cores.AMARELO}[2]{Cores.RESET} Modo Prova Real (Cronometrado, sem consulta nem gabarito até o fim)")
    print(f"  {Cores.AZUL}[3]{Cores.RESET} Filtrar por Capítulo ou Tipo (Prática focada)")
    print(f"  {Cores.CINZA}[4] Sair{Cores.RESET}\n")
    
    while True:
        opcao = input(f"{Cores.NEGRITO}Opção [1-4]: {Cores.RESET}").strip()
        if opcao in ["1", "2", "3", "4"]:
            return opcao
        print("Opção inválida, tente novamente.")

def filtrar_questoes(todas):
    print(f"\n{Cores.NEGRITO}Filtrar questões por:{Cores.RESET}")
    print("  [1] Apenas Capítulo 7 - Redes Multimídia (20 questões)")
    print("  [2] Apenas Capítulo 8 - Segurança em Redes (20 questões)")
    print("  [3] Apenas Questões de Cálculo / Práticas (11 questões)")
    print("  [4] Apenas Questões Conceituais / Teóricas (29 questões)")
    print("  [5] Todas as 40 questões")

    opcao = input(f"\n{Cores.NEGRITO}Escolha [1-5]: {Cores.RESET}").strip()
    if opcao == "1":
        return [q for q in todas if "7" in q["capitulo"]]
    elif opcao == "2":
        return [q for q in todas if "8" in q["capitulo"]]
    elif opcao == "3":
        return [q for q in todas if q["tipo"] == "calculo_pratico"]
    elif opcao == "4":
        return [q for q in todas if q["tipo"] == "conceitual"]
    return todas

def exibir_guia_teoria(q):
    print(f"\n{Cores.MAGENTA}{'=' * 75}{Cores.RESET}")
    print(f"{Cores.NEGRITO}{Cores.MAGENTA}📚 GUIA TEÓRICO & TERMOS EXPLICADOS{Cores.RESET}")
    print(f"{Cores.MAGENTA}{'=' * 75}{Cores.RESET}\n")

    guia = q.get("guia_estudo", {})
    if not guia:
        print("Guia teórico não disponível para esta questão.")
        return

    print(f"{Cores.NEGRITO}🎯 Conceito Geral:{Cores.RESET}")
    print(f"{Cores.CINZA}{guia.get('conceito_geral', '')}{Cores.RESET}\n")

    print(f"{Cores.NEGRITO}🏷️ Glossário de Termos e Siglas:{Cores.RESET}")
    for termo in guia.get("termos_chave", []):
        print(f"  • {Cores.CIANO}{termo['termo']}{Cores.RESET}: {termo['definicao']}")

    calc = guia.get("guia_calculo")
    if calc:
        print(f"\n{Cores.AMARELO}{'-' * 75}{Cores.RESET}")
        print(f"{Cores.NEGRITO}{Cores.AMARELO}🧮 COMO FUNCIONA O CÁLCULO E O QUE ELE REPRESENTA:{Cores.RESET}")
        print(f"{Cores.AMARELO}{'-' * 75}{Cores.RESET}\n")
        print(f"{Cores.NEGRITO}💡 O que representa:{Cores.RESET} {calc.get('o_que_representa')}\n")
        print(f"{Cores.NEGRITO}📐 Fórmula:{Cores.RESET}\n{Cores.CIANO}{calc.get('formula')}{Cores.RESET}\n")
        print(f"{Cores.NEGRITO}🔢 Passo a Passo da Resolução:{Cores.RESET}")
        for step in calc.get("passo_a_passo", []):
            print(f"  {step}")

    print(f"\n{Cores.MAGENTA}{'=' * 75}{Cores.RESET}")
    input(f"{Cores.CIANO}Pressione ENTER para voltar às alternativas da questão...{Cores.RESET}")

def executar_simulado(questoes, modo_prova=False):
    total = len(questoes)
    acertos = 0
    respostas_usuario = []
    tempo_inicio = time.time()

    for idx, q in enumerate(questoes, start=1):
        limpar_tela()
        progresso = f"Questão {idx}/{total}"
        tag_tipo = "🧮 CÁLCULO" if q["tipo"] == "calculo_pratico" else "📖 CONCEITUAL"
        
        print(f"{Cores.CINZA}[{progresso}] {tag_tipo} | {q['capitulo']} ({q['referencia_livro']}){Cores.RESET}")
        print(f"\n{Cores.NEGRITO}{q['id']}. {q['enunciado']}{Cores.RESET}\n")

        for letra, texto in q["alternativas"].items():
            print(f"  {Cores.NEGRITO}{letra}){Cores.RESET} {texto}")

        while True:
            dica_extra = " ou 'T' para Teoria/Cálculo" if not modo_prova else ""
            prompt_texto = f"\n{Cores.CIANO}Sua resposta [A/B/C/D]{dica_extra} (ou 'S' para pular): {Cores.RESET}"
            resp = input(prompt_texto).strip().upper()

            if resp == "T" and not modo_prova:
                exibir_guia_teoria(q)
                limpar_tela()
                print(f"{Cores.CINZA}[{progresso}] {tag_tipo} | {q['capitulo']} ({q['referencia_livro']}){Cores.RESET}")
                print(f"\n{Cores.NEGRITO}{q['id']}. {q['enunciado']}{Cores.RESET}\n")
                for letra, texto in q["alternativas"].items():
                    print(f"  {Cores.NEGRITO}{letra}){Cores.RESET} {texto}")
                continue

            if resp in ["A", "B", "C", "D", "S"]:
                break
            print(f"{Cores.VERMELHO}Entrada inválida! Digite A, B, C ou D (ou T para Teoria).{Cores.RESET}")

        correta = q["resposta_correta"]
        acertou = (resp == correta)
        if acertou:
            acertos += 1

        respostas_usuario.append({
            "questao": q,
            "resposta": resp,
            "correta": correta,
            "acertou": acertou
        })

        if not modo_prova:
            print()
            if resp == "S":
                print(f"{Cores.AMARELO}⏭️ Questão pulada. A resposta correta era: {correta}{Cores.RESET}")
            elif acertou:
                print(f"{Cores.VERDE}✅ Resposta CORRETA! Parabéns!{Cores.RESET}")
            else:
                print(f"{Cores.VERMELHO}❌ Resposta INCORRETA. Você marcou {resp}, o correto é {correta}.{Cores.RESET}")
            
            print(f"\n{Cores.NEGRITO}💡 Explicação detalhada:{Cores.RESET}")
            print(f"{Cores.CINZA}{q['explicacao']}{Cores.RESET}")
            input(f"\n{Cores.CIANO}Pressione ENTER para ir para a próxima questão...{Cores.RESET}")

    tempo_total = time.time() - tempo_inicio
    minutos = int(tempo_total // 60)
    segundos = int(tempo_total % 60)

    # Relatório Final
    limpar_tela()
    print(f"{Cores.CIANO}{'=' * 75}{Cores.RESET}")
    print(f"{Cores.NEGRITO}📊 RESULTADO FINAL DO SIMULADO{Cores.RESET}")
    print(f"{Cores.CIANO}{'=' * 75}{Cores.RESET}\n")

    percentual = (acertos / total) * 100 if total > 0 else 0
    cor_nota = Cores.VERDE if percentual >= 70 else (Cores.AMARELO if percentual >= 50 else Cores.VERMELHO)

    print(f"Pontuação: {cor_nota}{acertos}/{total} acertos ({percentual:.1f}%){Cores.RESET}")
    print(f"Tempo gasto: {minutos}m {segundos}s\n")

    # Estatísticas por capítulo
    cap7_total = len([r for r in respostas_usuario if "7" in r["questao"]["capitulo"]])
    cap7_acertos = len([r for r in respostas_usuario if "7" in r["questao"]["capitulo"] and r["acertou"]])
    cap8_total = len([r for r in respostas_usuario if "8" in r["questao"]["capitulo"]])
    cap8_acertos = len([r for r in respostas_usuario if "8" in r["questao"]["capitulo"] and r["acertou"]])

    if cap7_total > 0:
        p7 = (cap7_acertos / cap7_total) * 100
        print(f"  • Cap. 7 (Multimídia): {cap7_acertos}/{cap7_total} ({p7:.1f}%)")
    if cap8_total > 0:
        p8 = (cap8_acertos / cap8_total) * 100
        print(f"  • Cap. 8 (Segurança):  {cap8_acertos}/{cap8_total} ({p8:.1f}%)")

    # Se foi modo prova, mostrar revisão completa
    if modo_prova:
        print(f"\n{Cores.CIANO}{'=' * 75}{Cores.RESET}")
        print(f"{Cores.NEGRITO}📝 REVISÃO DE QUESTÕES{Cores.RESET}")
        print(f"{Cores.CIANO}{'=' * 75}{Cores.RESET}\n")

        for item in respostas_usuario:
            q = item["questao"]
            status = f"{Cores.VERDE}ACERTOU{Cores.RESET}" if item["acertou"] else f"{Cores.VERMELHO}ERROU (Marcou {item['resposta']}, Correto: {item['correta']}){Cores.RESET}"
            print(f"Q{q['id']} [{q['referencia_livro']}] - {status}")
            if not item["acertou"]:
                print(f"   {Cores.CINZA}💡 {q['explicacao']}{Cores.RESET}\n")

    input(f"\n{Cores.CIANO}Pressione ENTER para voltar ao menu principal...{Cores.RESET}")

def main():
    dados = carregar_questoes()
    todas = dados["questoes"]

    while True:
        limpar_tela()
        exibir_cabecalho(dados["titulo"], dados["referencia"])
        opcao = menu_principal()

        if opcao == "1":
            executar_simulado(todas, modo_prova=False)
        elif opcao == "2":
            executar_simulado(todas, modo_prova=True)
        elif opcao == "3":
            filtradas = filtrar_questoes(todas)
            executar_simulado(filtradas, modo_prova=False)
        elif opcao == "4":
            print(f"\n{Cores.VERDE}Bons estudos e boa prova! Até mais.{Cores.RESET}\n")
            break

if __name__ == "__main__":
    main()
