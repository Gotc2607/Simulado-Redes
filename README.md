# Simulado de Redes de Computadores - Capítulos 7 e 8

Simulado interativo com 20 questões adaptadas dos exercícios do livro **"Redes de Computadores e a Internet: Uma Abordagem Top-Down"** (6ª edição), de Kurose & Ross.

---

## 📚 Conteúdo Coberto

- **Capítulo 7: Redes Multimídia** (10 questões)
  - Áudio digital PCM e taxa de bits
  - HTTP Streaming, atraso de buffer inicial e desperdício de banda
  - DASH (Dynamic Adaptive Streaming over HTTP)
  - VoIP: empacotamento, sobrecarga de cabeçalhos (IP + UDP + RTP)
  - Técnicas de FEC (Forward Error Correction) para VoIP (XOR vs Piggybacking)
  - SIP e RTP: identificação de sessões e fluxos (SSRC, Payload Type)
  - Escalonamento WFQ (Weighted Fair Queuing)
  - Policiamento de tráfego com Balde de Fichas (Token Bucket)

- **Capítulo 8: Segurança em Redes de Computadores** (10 questões)
  - Confidencialidade vs Integridade
  - Escala de chaves em Criptografia Simétrica vs Chave Pública
  - Aritmética Modular aplicada à criptografia
  - Algoritmo RSA (cálculo de $n$, $z$, $d$ e cifra $c$)
  - Troca de chaves Diffie-Hellman
  - Assinatura Digital e Autoridades Certificadoras (CA)
  - Handshake SSL/TLS e tratamento de números de sequência
  - IPsec em Modo Túnel com ESP e proteção contra replay
  - Criptografia WEP (IV, Keystream e ICV)
  - Firewalls com estado (Stateful) e Gateways de Aplicação

---

## 🚀 Como Treinar

### 1. Interface Web Interativa (Recomendado)
Basta abrir o arquivo [index.html](file:///home/giovani-coelho/Documentos/Simulado-Redes/index.html) no seu navegador:
- Funciona direto com duplo clique (não requer servidor web).
- **Modo Estudo**: feedback instantâneo e explicação passo a passo ao selecionar a alternativa.
- **Modo Prova**: cronômetro ativo, gabarito e relatório de pontuação por capítulo no final.
- **Filtros rápidos**: pratique apenas cálculos, apenas questões teóricas, ou filtre por capítulo.

Para rodar com um servidor local rápido (opcional):
```bash
python3 -m http.server 8000
```
Depois acesse `http://localhost:8000` no seu navegador.

---

### 2. No Terminal via Script Python
Você também pode treinar direto pelo terminal:
```bash
python3 simulado.py
```
O script oferece:
- Menu com Modo Prática, Modo Prova Real e Filtros.
- Interface colorida no terminal.
- Relatório final de acertos com percentual e revisão detalhada de erros.

---

### 3. Base de Dados em JSON
Todas as questões com enunciados, alternativas, gabarito e resoluções comentadas estão estruturadas em [questoes.json](file:///home/giovani-coelho/Documentos/Simulado-Redes/questoes.json).
