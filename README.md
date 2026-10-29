# CRIE CENAS VARIADAS

Versão 1.0.0 — expansão cinematográfica da mesma cena por novas posições de câmera.

Recebe uma imagem e entrega exatamente cinco opções, com prompt completo em português e inglês para cada uma: dez prompts no total. O princípio é mudar a câmera, nunca a arquitetura, a posição física dos objetos, os materiais ou a proporção da referência.

## Funções
Análise visual/arquitetônica, geometria relativa, profundidade, materiais, luz, perspectiva original e aspect ratio; planejamento de cinco posições e recortes distintos; lentes equivalentes, alturas, ângulos e movimentos virtuais de reposicionamento.

Padrões adaptáveis: geral expandido, lateral 3/4, baixo, elevado e próximo. Não são ângulos obrigatórios se exigirem inventar áreas ocultas. Uma foto não revela toda a geometria: limitar movimentos ou pedir vista adicional quando necessário.

## Preservação e limites
Não criar portas, janelas, paredes, escadas ou corredores. Não mover/remover objetos nem trocar materiais. Mudanças aparentes por perspectiva e oclusão são permitidas. Mesma luz e ratio exato em todas as propostas. Valores de altura e lente são propostas, não dados medidos ou EXIF.

Geração real, reconstrução 3D e validação geométrica automática não estão implementadas por esta Skill textual. As verificações incluídas cobrem contrato e proporção, não pixels. Mapa espacial, confiança e revisão são procedimentos textuais, não medições.

## Instalação e uso
Copiar `.agents/skills/crie-cenas-variadas/` para o diretório aceito pelo host. Ver [instalação](docs/INSTALLATION.md). Enviar imagem acessível e pedir cinco novas vistas. Sem referência, solicitar envio; sem dimensões verificáveis, pedir largura e altura para ratio exato. Publicação não instala a Skill automaticamente no ChatGPT.

## Estrutura
[Núcleo autossuficiente](.agents/skills/crie-cenas-variadas/SKILL.md), seis referências, três exemplos, auditoria, fonte integral, doze casos de aceitação, validador, helper de proporção e CI. Exemplos são sintéticos, não resultados visuais medidos.

## Validação
```bash
python -m pip install -r tests/requirements.txt
python tests/validate.py
python tests/test_validator.py
python .agents/skills/crie-cenas-variadas/scripts/aspect_ratio.py 1000 667
```
Python 3.9+ e PyYAML 6.x para o pacote; o helper de ratio usa biblioteca padrão e não lê dimensões da imagem automaticamente. Instalação inicial da dependência pode precisar de rede. Nenhuma credencial exigida.

## Evidência e manutenção
Fonte é especificação funcional, não execução do agente original. Testes estruturais não demonstram equivalência visual. [Auditoria](docs/AUDIT.md), [aceitação](tests/acceptance-tests.md), [comparação](tests/comparison-matrix.md), [histórico](CHANGELOG.md) e [contribuições](CONTRIBUTING.md).

MIT, copyright 2026 mxcapellani. Modelos de geração e seus recursos dependem de integração externa, sem suporte universal garantido.
