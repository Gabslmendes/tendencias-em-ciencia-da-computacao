# Atividade Prática — Aula 01: Identificando a IA

**Disciplina:** Tendências em Ciência da Computação
**Consigna:** escolher 5 tecnologias ou aplicativos de uso cotidiano e responder, para cada um: (1) onde a IA está presente; (2) qual problema resolve; (3) quais dados provavelmente utiliza; (4) qual[...] 

**Recorte adotado:** as cinco tecnologias foram escolhidas dentro da rotina de uma serventia notarial, para que a análise de dados e riscos seja concreta e não genérica.

---

## 1. e-Notariado (atos notariais eletrônicos)

**Onde a IA está presente.** Na etapa de identificação da parte por videoconferência: verificação facial que compara a imagem capturada ao vivo com a foto do documento oficial, somada à detecç[...]

**Problema que resolve.** Garantir a identidade do comparecente sem presença física, sustentando a fé pública em ambiente remoto.

**Dados provavelmente utilizados.** Imagem facial capturada, imagem do documento de identidade, metadados da sessão (dispositivo, IP, horário), certificado digital ICP-Brasil.

**Benefício direto.** Ato praticado à distância com nível de segurança de identificação comparável ao presencial; alcance para partes fora do DF ou com dificuldade de locomoção.

**Risco ou limitação.** Sistemas de verificação facial apresentam taxas de erro desiguais entre grupos demográficos — o viés não vem do algoritmo, vem do conjunto de treinamento ("garbage in,[...]

---

## 2. Extração automatizada de dados de documentos (Gemini API / projeto próprio)

**Onde a IA está presente.** Modelo generativo multimodal que lê a imagem de um RG, CNH, certidão ou matrícula e devolve os campos já estruturados (nome, filiação, número, data), prontos para [...]

**Problema que resolve.** A digitação manual de qualificação de partes — a tarefa mais repetitiva e, ao mesmo tempo, a de maior potencial de erro material na lavratura.

**Dados provavelmente utilizados.** Imagem do documento enviada na requisição e o conhecimento prévio do modelo sobre layouts de documentos brasileiros. Note que aqui há tratamento de dado pessoal[...]

**Benefício direto.** Redução drástica do tempo de qualificação e menos erro de transcrição de números e grafias.

**Risco ou limitação.** É exatamente o cenário clássico de alucinação: o modelo prevê a próxima palavra, não consulta uma verdade absoluta. Um dígito plausível preenchido no lugar de um d�[...]

---

## 3. Assistente de IA generativa aplicada à redação notarial (Claude)

**Onde a IA está presente.** LLM usado para redigir e revisar minutas, corrigir concordância em linguagem jurídica formal e analisar contratos em busca de vícios de qualificação.

**Problema que resolve.** O custo de tempo da primeira versão do texto e da revisão gramatical de peças longas.

**Dados provavelmente utilizados.** O texto enviado no prompt, os modelos e padrões da serventia fornecidos como contexto, e o conhecimento geral do modelo sobre linguagem jurídica.

**Benefício direto.** Minuta inicial em minutos, padronização de estilo, revisão consistente.

**Risco ou limitação.** O modelo é fluente em direito, não é competente em direito: pode citar dispositivo revogado, inventar número de provimento ou afirmar exigência que não existe — sempr[...]

---

## 4. WhatsApp (canal de atendimento ao público)

**Onde a IA está presente.** Transcrição automática de áudios, classificação e bloqueio de spam, ordenação de conversas e sugestões de resposta rápida.

**Problema que resolve.** Volume: transformar áudio em texto pesquisável e separar mensagem legítima de contato indesejado.

**Dados provavelmente utilizados.** Áudio das mensagens, padrões de comportamento de envio (frequência, número de destinatários, denúncias de outros usuários), metadados de conversa.

**Benefício direto.** Atendimento mais rápido e registro textual do que foi pedido pelo cidadão.

**Risco ou limitação.** A transcrição erra em nomes próprios, termos jurídicos e sotaques — e o erro entra no histórico como se fosse o que a parte disse. Num canal de serventia, uma transcri[...]

---

## 5. Gmail (filtro de spam e categorização)

**Onde a IA está presente.** Classificação supervisionada: o filtro aprendeu com milhões de e-mails já rotulados como spam ou legítimo — é o exemplo canônico de Machine Learning citado na au[...]

**Problema que resolve.** Separar o que exige leitura do que é ruído, e sinalizar tentativas de phishing.

**Dados provavelmente utilizados.** Conteúdo e cabeçalhos das mensagens, reputação do remetente e do domínio, e o rótulo agregado de milhões de usuários que marcaram mensagens semelhantes como[...]

**Benefício direto.** Caixa de entrada utilizável e uma camada real de proteção contra fraude.

**Risco ou limitação.** Falso positivo silencioso. Uma intimação, uma nota de exigência ou um e-mail de parte pode ir para a lixeira sem qualquer aviso — e o custo do erro recai inteiramente so[...]

---

## Síntese

Os cinco casos se distribuem exatamente na arquitetura apresentada na aula: Gmail e WhatsApp operam por **Machine Learning** clássico (classificar, prever); o e-Notariado usa **Deep Learning** para r[...]

O padrão que atravessa todos eles é o mesmo: a IA reduz o custo da primeira versão e do trabalho repetitivo, e desloca — não elimina — o esforço humano para a etapa de **verificação**. Nos [...]

---

## Apêndice — Checkpoint de Compreensão

**Qual a diferença entre IA e Machine Learning?** IA é o campo amplo de construir sistemas que executam tarefas associadas à inteligência humana; ML é um subconjunto dentro dele, no qual o sistem[...]

**O que caracteriza o Deep Learning?** O aprendizado por redes neurais artificiais profundas — múltiplas camadas ocultas que processam padrões complexos, viabilizando reconhecimento de imagem e vo[...]

**Qual a função dos dados no aprendizado de máquina?** São a matéria-prima do modelo: substituem as regras escritas à mão. Dados incompletos ou enviesados produzem previsões falhas e discrimin[...]

**O que diferencia a IA Preditiva da Generativa?** A preditiva analisa dados existentes e aponta uma probabilidade (classificar, prever); a generativa recebe uma instrução e constrói conteúdo novo[...]

**Por que um prompt detalhado gera resultados melhores?** Porque fornece contexto, objetivo e formato. Sem eles o modelo preenche as lacunas com a interpretação mais provável, que raramente é a pr[...]

**Por que é necessário verificar as respostas de uma IA?** Porque o modelo prevê a próxima palavra em vez de consultar uma verdade, e apresenta o erro com o mesmo grau de confiança da acerto. A r[...]
