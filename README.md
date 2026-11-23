# Simulado de Redes de Computadores - Capítulos 7 e 8

[![GitHub Pages](https://img.shields.io/badge/Acessar%20Simulado%20Online-GitHub%20Pages-blue?style=for-the-badge&logo=github)](https://gotc2607.github.io/Simulado-Redes/)

Simulado interativo com **40 questões** (29 conceituais/teóricas e 11 de cálculo prático) baseadas nos exercícios e seções do livro **"Redes de Computadores e a Internet: Uma Abordagem Top-Down"** (6ª edição), de Kurose & Ross.

🔗 **Link do Simulado Online**: [https://gotc2607.github.io/Simulado-Redes/](https://gotc2607.github.io/Simulado-Redes/)

---

## 📚 Conteúdo Coberto

- **Capítulo 7: Redes Multimídia** (20 questões)
  - Categorias de aplicações multimídia (armazenado, conversacional, ao vivo) e tolerância a atraso/perda
  - Áudio digital PCM, amostragem, quantização e taxa de bits
  - UDP vs. HTTP Streaming, atraso de buffer inicial e desperdício de banda
  - DASH (Dynamic Adaptive Streaming over HTTP) e Redes de Distribuição de Conteúdo (CDNs: *Enter Deep* vs. *Bring Home*)
  - VoIP: empacotamento, sobrecarga de cabeçalhos (IP + UDP + RTP), *jitter* e *playout* adaptativo
  - Recuperação de perdas: FEC (XOR vs. Piggybacking) e Intercalação (*Interleaving*)
  - SIP (Registrador, Proxy, `INVITE`/`200 OK`/`ACK`), RTP (SSRC, Payload Type) e RTCP
  - QoS: Escalonamento (FIFO, Prioridade, Round Robin, WFQ), Policiamento (*Token Bucket*), DiffServ (Borda vs. Núcleo, DSCP, PHB) e IntServ (Controle de Admissão e RSVP)

- **Capítulo 8: Segurança em Redes de Computadores** (20 questões)
  - Pilares da segurança (Confidencialidade, Integridade, Autenticação, Segurança Operacional) e modelo de ameaça
  - Criptografia Simétrica (cifras de bloco, modo CBC e IV) vs. Chave Pública (escala de chaves)
  - Aritmética Modular, Algoritmo RSA e Troca de Chaves Diffie-Hellman
  - Funções de Hash Criptográficas (resistência a colisões), MAC, Assinaturas Digitais e Autoridades Certificadoras (CA)
  - Autenticação do ponto final (protocolos `ap1.0` a `ap4.0`, uso de *nonce* contra ataques de repetição)
  - E-mail seguro e PGP (criptografia híbrida com chave de sessão)
  - SSL/TLS: Handshake, 4 chaves derivadas, números de sequência implícitos e proteção contra ataque por truncamento
  - IPsec (AH vs. ESP, Modo Túnel, tabelas SPD e SAD, proteção anti-replay e protocolo IKE)
  - Segurança Wi-Fi 802.11: vulnerabilidades do WEP (IV de 24 bits, Keystream, ICV) e evolução para IEEE 802.11i (WPA2)
  - Segurança operacional: Firewalls com estado (*Stateful*), Gateways de Aplicação e Sistemas de Detecção/Prevenção de Invasão (IDS/IPS — assinaturas vs. anomalias)

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
